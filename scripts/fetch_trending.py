#!/usr/bin/env python3
"""Collect the past week's hottest GitHub repos in the LLM / agent space.

Deterministic and stdlib-only: it scrapes github.com/trending (which is the only
place GitHub exposes real weekly star velocity), supplements with the Search API
so a week dominated by non-AI projects still yields enough candidates, enriches
everything through the REST API, ranks, and prints JSON to stdout.

The agent that calls this writes the prose; this script never editorializes.
"""

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "topics.json"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()


def warn(msg):
    print(f"WARN: {msg}", file=sys.stderr)


def info(msg):
    print(f"[grab] {msg}", file=sys.stderr)


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

def fetch_text(url, headers=None, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def api_get(path, retries=3):
    """GET the GitHub API, backing off on rate limits. Returns parsed JSON or None."""
    url = path if path.startswith("http") else f"{API}{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    for attempt in range(retries):
        try:
            return json.loads(fetch_text(url, headers=headers))
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429):
                wait = _retry_after(exc)
                if attempt == retries - 1:
                    warn(f"rate limited on {url}, giving up")
                    return None
                info(f"rate limited on {url}, sleeping {wait}s")
                time.sleep(wait)
                continue
            if exc.code == 404:
                return None
            warn(f"HTTP {exc.code} on {url}")
            return None
        except Exception as exc:  # noqa: BLE001 - one bad call must not kill the run
            warn(f"{type(exc).__name__} on {url}: {exc}")
            return None
    return None


def _retry_after(exc):
    """Seconds to sleep, from Retry-After or x-ratelimit-reset. Capped so a
    weekly run never hangs for the full hour of an exhausted core quota."""
    retry_after = exc.headers.get("Retry-After")
    if retry_after and retry_after.isdigit():
        return min(int(retry_after), 90)
    reset = exc.headers.get("x-ratelimit-reset")
    if reset and reset.isdigit():
        delta = int(reset) - int(time.time()) + 2
        if delta > 0:
            return min(delta, 90)
    return 20


# --------------------------------------------------------------------------
# Source 1: the trending page (real weekly star velocity)
# --------------------------------------------------------------------------

ARTICLE_SPLIT = '<article class="Box-row">'
RE_FULLNAME = re.compile(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', re.S)
RE_WEEKLY = re.compile(r"([\d,]+)\s+stars\s+this\s+week")
RE_DESC = re.compile(r'<p[^>]*class="col-9[^"]*"[^>]*>\s*(.*?)\s*</p>', re.S)
RE_LANG = re.compile(r'<span itemprop="programmingLanguage">\s*(.*?)\s*</span>', re.S)
RE_TAG = re.compile(r"<[^>]+>")


def strip_tags(fragment):
    return html.unescape(RE_TAG.sub("", fragment)).strip()


def fetch_trending(language=""):
    """Parse one trending page. Language '' is the global page."""
    path = f"/trending/{language}" if language else "/trending"
    url = f"https://github.com{path}?since=weekly"
    out = []
    try:
        page = fetch_text(url)
    except Exception as exc:  # noqa: BLE001
        warn(f"trending fetch failed for '{language or 'all'}': {exc}")
        return out

    for chunk in page.split(ARTICLE_SPLIT)[1:]:
        m = RE_FULLNAME.search(chunk)
        if not m:
            continue
        full_name = m.group(1).strip().strip("/")
        if full_name.count("/") != 1:
            continue
        weekly = RE_WEEKLY.search(chunk)
        desc = RE_DESC.search(chunk)
        lang = RE_LANG.search(chunk)
        out.append(
            {
                "full_name": full_name,
                "stars_this_week": int(weekly.group(1).replace(",", "")) if weekly else None,
                "description": strip_tags(desc.group(1)) if desc else "",
                "language": strip_tags(lang.group(1)) if lang else None,
                "source": "trending",
            }
        )

    if not out:
        warn(f"trending page for '{language or 'all'}' parsed 0 repos - markup may have changed")
    else:
        info(f"trending/{language or 'all'}: {len(out)} repos")
    return out


# --------------------------------------------------------------------------
# Source 2: the Search API (topic-targeted backfill)
# --------------------------------------------------------------------------

def fetch_search(topic, since_date, per_page=15):
    q = urllib.parse.quote(f"topic:{topic} pushed:>={since_date}", safe=":>=")
    data = api_get(f"/search/repositories?q={q}&sort=stars&order=desc&per_page={per_page}")
    if not data or "items" not in data:
        return []
    out = []
    for item in data["items"]:
        out.append(
            {
                "full_name": item["full_name"],
                "stars_this_week": None,
                "description": item.get("description") or "",
                "language": item.get("language"),
                "source": "search",
                "_prefetched": item,
            }
        )
    info(f"search topic:{topic}: {len(out)} repos")
    return out


# --------------------------------------------------------------------------
# Filtering / scoring
# --------------------------------------------------------------------------

def haystack(repo, topics=None):
    parts = [repo["full_name"], repo.get("description") or ""]
    parts.extend(topics or [])
    return " ".join(parts).lower()


def topic_score(text, keywords):
    """Sum of weights for keywords present. Word-boundary matched so 'ai' does
    not fire on 'chain' and 'rag' does not fire on 'fragment'."""
    score = 0
    for kw, weight in keywords.items():
        if re.search(rf"(?<![a-z0-9]){re.escape(kw)}(?![a-z0-9])", text):
            score += weight
    return score


def is_excluded(full_name, patterns):
    name = full_name.split("/")[-1].lower()
    return any(re.search(p, name) for p in patterns)


# --------------------------------------------------------------------------
# Enrichment + ranking
# --------------------------------------------------------------------------

def enrich(repo):
    detail = repo.pop("_prefetched", None) or api_get(f"/repos/{repo['full_name']}")
    if not detail:
        warn(f"could not enrich {repo['full_name']}, dropping")
        return None

    license_info = detail.get("license") or {}
    repo.update(
        {
            "html_url": detail.get("html_url"),
            "description": detail.get("description") or repo.get("description") or "",
            "stars": detail.get("stargazers_count"),
            "forks": detail.get("forks_count"),
            "open_issues": detail.get("open_issues_count"),
            "language": detail.get("language") or repo.get("language"),
            "topics": detail.get("topics") or [],
            "license": license_info.get("spdx_id") or license_info.get("name"),
            "homepage": (detail.get("homepage") or "").strip() or None,
            "created_at": detail.get("created_at"),
            "pushed_at": detail.get("pushed_at"),
            "archived": detail.get("archived", False),
        }
    )
    return repo


def estimated_weekly(repo):
    """Rough weekly velocity for search-only repos, so they can be interleaved
    with trending hits without pretending to be measured. Total stars spread
    over the repo's age, which under-reports breakouts - hence the source flag."""
    stars = repo.get("stars") or 0
    created = repo.get("created_at")
    if not created:
        return 0
    try:
        born = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return 0
    weeks = max((datetime.now(timezone.utc) - born).days / 7.0, 1.0)
    return int(stars / weeks)


def prerank_key(repo):
    """Ordering used to spend the enrichment budget, before any repo has been
    enriched. Trending hits carry a measured weekly delta; search hits carry
    nothing, so estimate from the prefetched payload instead of letting them all
    collapse to 0 - otherwise a theme whose repos only ever arrive via search
    (every theme but ai-agent) never survives the pool cut."""
    measured = repo.get("stars_this_week")
    if measured:
        return measured
    pre = repo.get("_prefetched") or {}
    return estimated_weekly(
        {"stars": pre.get("stargazers_count"), "created_at": pre.get("created_at")}
    ) * 0.5


# --------------------------------------------------------------------------

def load_theme(name):
    """Resolve one theme's knobs, merged over the shared block."""
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    themes = config["themes"]
    if name not in themes:
        sys.exit(f"unknown theme '{name}'; config has: {', '.join(themes)}")
    theme = dict(config.get("shared", {}))
    theme.update(themes[name])
    theme["slug"] = name
    return theme, list(themes)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--theme", help="which theme in config/topics.json to grab")
    ap.add_argument("--list-themes", action="store_true", help="print the configured theme slugs and exit")
    ap.add_argument("--out", help="also write the JSON to this path")
    ap.add_argument("--limit", type=int, help="how many repos to emit (default: theme's 'limit')")
    ap.add_argument("--enrich-pool", type=int, help="candidates to enrich before ranking")
    ap.add_argument("--week-of", help="YYYY-MM-DD anchor date (default: today)")
    ap.add_argument(
        "--min-repos",
        type=int,
        help="exit 2 if fewer than this many repos survive (default: theme's 'min_repos')",
    )
    args = ap.parse_args()

    if args.list_themes:
        _, names = load_theme(next(iter(json.loads(CONFIG.read_text(encoding="utf-8"))["themes"])))
        print("\n".join(names))
        return
    if not args.theme:
        ap.error("--theme is required (use --list-themes to see the options)")

    config, _ = load_theme(args.theme)
    keywords = config["keywords"]
    min_score = config.get("min_score", 3)
    min_stars = config.get("min_stars", 0)
    excludes = config.get("exclude_patterns", [])
    limit = args.limit if args.limit is not None else config.get("limit", 20)
    enrich_pool = args.enrich_pool if args.enrich_pool is not None else config.get("enrich_pool", 30)
    min_repos = args.min_repos if args.min_repos is not None else config.get("min_repos", 5)
    info(f"theme '{args.theme}' ({config.get('title', args.theme)}): limit={limit} min_stars={min_stars}")

    anchor = (
        datetime.strptime(args.week_of, "%Y-%m-%d").date()
        if args.week_of
        else datetime.now(timezone.utc).date()
    )
    since_date = (anchor - timedelta(days=7)).isoformat()

    if not TOKEN:
        info("no GITHUB_TOKEN set - running unauthenticated (60 core req/hr)")

    # 1. collect
    candidates = {}
    for lang in config["trending_languages"]:
        for repo in fetch_trending(lang):
            key = repo["full_name"].lower()
            existing = candidates.get(key)
            if existing is None or (existing.get("stars_this_week") is None and repo.get("stars_this_week")):
                candidates[key] = repo

    for topic in config["search_topics"]:
        for repo in fetch_search(topic, since_date):
            key = repo["full_name"].lower()
            if key not in candidates:
                candidates[key] = repo
        time.sleep(1.2)  # search API allows only 10 req/min unauthenticated

    info(f"{len(candidates)} unique candidates before filtering")

    # 2. filter on topic relevance before spending core API quota on enrichment
    scored = []
    for repo in candidates.values():
        if is_excluded(repo["full_name"], excludes):
            continue
        prefetched = repo.get("_prefetched") or {}
        score = topic_score(haystack(repo, prefetched.get("topics")), keywords)
        if score < min_score:
            continue
        repo["_score"] = score
        scored.append(repo)

    # cheap pre-rank so the enrichment budget goes to the most promising repos
    scored.sort(key=lambda r: (prerank_key(r), r["_score"]), reverse=True)
    scored = scored[:enrich_pool]
    info(f"{len(scored)} candidates passed the topic filter; enriching")

    # 3. enrich
    enriched = []
    for repo in scored:
        full = enrich(repo)
        if full and not full.get("archived") and (full.get("stars") or 0) >= min_stars:
            # re-score now that real topics are known
            full["_score"] = topic_score(haystack(full, full.get("topics")), keywords)
            if full["_score"] >= min_score:
                enriched.append(full)

    # 4. rank: measured weekly velocity wins; estimated velocity fills the tail
    for repo in enriched:
        measured = repo.get("stars_this_week")
        repo["stars_this_week_estimated"] = None if measured else estimated_weekly(repo)
        repo["_rank_key"] = measured if measured else repo["stars_this_week_estimated"] * 0.5

    enriched.sort(key=lambda r: (r["_rank_key"], r["_score"]), reverse=True)
    top = enriched[:limit]
    for repo in top:
        repo.pop("_rank_key", None)
        repo["score"] = repo.pop("_score")

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "theme": args.theme,
        "theme_title": config.get("title", args.theme),
        "theme_subtitle": config.get("subtitle", ""),
        "week_start": since_date,
        "week_end": anchor.isoformat(),
        "authenticated": bool(TOKEN),
        "candidate_count": len(candidates),
        "repos": top,
    }

    # A run that collected nothing is a failure, not an empty result. Exit
    # non-zero so a scheduled caller can tell "GitHub blocked us" apart from
    # "quiet week" instead of silently succeeding with repos: [].
    if len(top) < min_repos:
        warn(
            f"only {len(top)} repos survived (need >= {min_repos}); "
            f"{len(candidates)} raw candidates collected. Treating this run as failed."
        )
        if args.out:
            _write(args.out, result)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(2)

    info(f"emitting {len(top)} repos")
    payload = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        _write(args.out, result)
    print(payload)


def _write(out, result):
    out_path = Path(out)
    if not out_path.is_absolute():
        out_path = ROOT / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    info(f"wrote {out_path}")


if __name__ == "__main__":
    main()
