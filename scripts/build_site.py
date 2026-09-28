#!/usr/bin/env python3
"""Turn reports/ into the static site under docs/, which GitHub Pages serves.

Reads every reports/<DATE>/<theme>/report.md (plus its raw.json for the
structured bits) and emits:

    docs/index.html          the last three months, filterable by theme
    docs/archive.html        everything, grouped by year
    docs/r/<DATE>-<theme>.html   one rendered report
    docs/assets/site.css     shared styling
    docs/data/reports.json   the same index as data, for anything else to read

Stdlib only, same as the grabber - the weekly run is unattended and must not
depend on a venv surviving between runs. Idempotent: it rebuilds docs/ from
scratch every time, so a deleted report disappears from the site instead of
lingering as an orphan page.
"""

import html
import json
import re
import shutil
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
DOCS = ROOT / "docs"
CONFIG = ROOT / "config" / "topics.json"

# Reports older than this fall off the front page into the archive.
RECENT_DAYS = 92

# Reports written before the four-theme split live directly in reports/<DATE>/
# with no theme directory. They were all LLM/agent digests, so that is where
# they belong on the site.
LEGACY_THEME = "ai-agent"


def info(msg):
    print(f"[site] {msg}", file=sys.stderr)


def warn(msg):
    print(f"WARN: {msg}", file=sys.stderr)


# --------------------------------------------------------------------------
# Markdown subset renderer
#
# Not a general Markdown implementation on purpose. report.md is written to the
# fixed template in .claude/commands/github-weekly.md, so the handful of
# constructs below is all that ever appears. A real parser would be more code
# and more failure modes for no gain here.
# --------------------------------------------------------------------------

RE_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
RE_BOLD = re.compile(r"\*\*([^*]+)\*\*")
RE_CODE = re.compile(r"`([^`]+)`")


def inline(text):
    """Escape first, then re-introduce the few inline constructs we allow. Doing
    it in this order means repo descriptions containing < or & cannot inject
    markup."""
    out = html.escape(text, quote=False)
    out = RE_CODE.sub(r"<code>\1</code>", out)
    out = RE_LINK.sub(lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', out)
    out = RE_BOLD.sub(r"<strong>\1</strong>", out)
    return out


def render_markdown(md):
    """Render the report body. Returns HTML for everything after the H1, which
    the page template renders itself as the cover title."""
    lines = md.splitlines()
    out = []
    para, bullets, quote = [], [], []

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()
        if bullets:
            items = "".join(f"<li>{inline(b)}</li>" for b in bullets)
            out.append(f'<ul class="evidence">{items}</ul>')
            bullets.clear()
        if quote:
            out.append(f'<blockquote>{inline(" ".join(quote))}</blockquote>')
            quote.clear()

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush()
            continue
        if stripped.startswith("# "):
            flush()
            continue  # the H1 is the page title, rendered by the template
        if set(stripped) <= {"-"} and len(stripped) >= 3:
            flush()
            continue  # horizontal rules just separate repos; sections carry that
        if stripped.startswith("## "):
            flush()
            out.append(f"<h2>{inline(stripped[3:].strip())}</h2>")
            continue
        if stripped.startswith("### "):
            flush()
            out.append(f"<h3>{inline(stripped[4:].strip())}</h3>")
            continue
        if stripped.startswith("> "):
            if para or bullets:
                flush()
            quote.append(stripped[2:].strip())
            continue
        if stripped.startswith(("- ", "* ")):
            if para or quote:
                flush()
            bullets.append(stripped[2:].strip())
            continue

        if bullets or quote:
            flush()
        para.append(stripped)

    flush()
    return "\n".join(out)


def split_sections(body_html):
    """Wrap each <h2> and the content after it in its own <section>, so the
    per-repo blocks get the card styling instead of running together."""
    parts = re.split(r"(?=<h2>)", body_html)
    out = []
    for i, part in enumerate(parts):
        if not part.strip():
            continue
        if part.startswith("<h2>"):
            out.append(f'<section class="repo">{part}</section>')
        else:
            out.append(f'<div class="lede">{part}</div>' if i == 0 else part)
    return "\n".join(out)


# --------------------------------------------------------------------------
# Collecting reports
# --------------------------------------------------------------------------

def load_themes():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    return cfg["themes"]


def collect(themes):
    """Every report on disk, newest first. Supports both the current
    reports/<DATE>/<theme>/ layout and the pre-split reports/<DATE>/ one."""
    found = []
    for date_dir in sorted(REPORTS.iterdir(), reverse=True):
        if not date_dir.is_dir() or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_dir.name):
            continue

        legacy = date_dir / "report.md"
        if legacy.exists():
            found.append(_one(date_dir.name, LEGACY_THEME, date_dir, themes, legacy=True))

        for theme_dir in sorted(date_dir.iterdir()):
            if not theme_dir.is_dir() or theme_dir.name not in themes:
                continue
            md = theme_dir / "report.md"
            if md.exists():
                found.append(_one(date_dir.name, theme_dir.name, theme_dir, themes))

    return [f for f in found if f]


def _one(date_str, theme, folder, themes, legacy=False):
    md_path = folder / "report.md"
    raw_path = folder / "raw.json"
    try:
        md = md_path.read_text(encoding="utf-8")
    except OSError as exc:
        warn(f"cannot read {md_path}: {exc}")
        return None

    raw = {}
    if raw_path.exists():
        try:
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            warn(f"cannot parse {raw_path}: {exc}")

    spec = themes.get(theme, {})
    title_line = next((l[2:].strip() for l in md.splitlines() if l.startswith("# ")), "")

    # The repos actually written up are the H2 headings, which the template
    # writes as "N. [owner/repo](url)". raw.json holds the 20 candidates, not
    # the 10 that made the cut, so the prose is the source of truth here.
    picks = []
    for m in re.finditer(r"^##\s+\d+\.\s+\[([^\]]+)\]\(([^)]+)\)", md, re.M):
        picks.append({"name": m.group(1), "url": m.group(2)})

    return {
        "date": date_str,
        "theme": theme,
        "theme_title": spec.get("title", theme),
        "theme_subtitle": spec.get("subtitle", ""),
        "accent": spec.get("accent", "#2f6f5e"),
        "title": title_line or f"{spec.get('title', theme)} 周报",
        "week_start": raw.get("week_start", ""),
        "week_end": raw.get("week_end", date_str),
        "count": len(picks),
        "picks": picks,
        "slug": f"{date_str}-{theme}",
        "legacy": legacy,
        "md": md,
    }


# --------------------------------------------------------------------------
# Page templates
# --------------------------------------------------------------------------

def shell(title, body, css_depth=0, extra_head=""):
    prefix = "../" * css_depth
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{prefix}assets/site.css">
{extra_head}
</head>
<body>
{body}
</body>
</html>
"""


def theme_chips(themes, active="all"):
    chips = ['<button class="chip is-on" data-theme="all">全部</button>']
    for slug, spec in themes.items():
        chips.append(
            f'<button class="chip" data-theme="{slug}" '
            f'style="--chip:{spec.get("accent", "#2f6f5e")}">{html.escape(spec.get("title", slug))}</button>'
        )
    return f'<div class="chips" role="tablist">{"".join(chips)}</div>'


def card(rep, depth=0):
    prefix = "../" * depth
    top = "".join(
        f'<li><a href="{html.escape(p["url"], quote=True)}">{html.escape(p["name"])}</a></li>'
        for p in rep["picks"][:3]
    )
    more = f'<li class="more">…另有 {rep["count"] - 3} 个</li>' if rep["count"] > 3 else ""
    return f"""
<article class="card" data-theme="{rep['theme']}" style="--accent:{rep['accent']}">
  <div class="card-head">
    <span class="badge">{html.escape(rep['theme_title'])}</span>
    <time>{rep['date']}</time>
  </div>
  <h3><a href="{prefix}r/{rep['slug']}.html">{html.escape(rep['theme_title'])} · {rep['date']} 周报</a></h3>
  <p class="card-sub">{html.escape(rep['theme_subtitle'])}</p>
  <ul class="card-picks">{top}{more}</ul>
  <div class="card-foot">
    <span>{rep['count']} 个项目</span>
    <a class="go" href="{prefix}r/{rep['slug']}.html">阅读 →</a>
  </div>
</article>
"""


FILTER_JS = """
<script>
  // Theme filtering is client-side so the whole site stays static files.
  document.addEventListener('click', function (e) {
    var chip = e.target.closest('.chip');
    if (!chip) return;
    var want = chip.dataset.theme;
    document.querySelectorAll('.chip').forEach(function (c) { c.classList.toggle('is-on', c === chip); });
    document.querySelectorAll('.card').forEach(function (card) {
      card.hidden = want !== 'all' && card.dataset.theme !== want;
    });
    document.querySelectorAll('.week, .year').forEach(function (group) {
      var any = group.querySelector('.card:not([hidden])');
      group.hidden = !any;
    });
  });
</script>
"""


def build_index(reports, themes):
    cutoff = date.today() - timedelta(days=RECENT_DAYS)
    recent = [r for r in reports if _as_date(r["date"]) >= cutoff]
    older = len(reports) - len(recent)

    by_week = {}
    for r in recent:
        by_week.setdefault(r["date"], []).append(r)

    groups = []
    for week in sorted(by_week, reverse=True):
        cards = "".join(card(r) for r in by_week[week])
        groups.append(f'<div class="week"><h2>{week}</h2><div class="grid">{cards}</div></div>')

    empty = '<p class="empty">最近三个月还没有报告。</p>' if not recent else ""

    body = f"""
<div class="page">
  <header class="cover">
    <h1>GitHub 周报</h1>
    <p class="subtitle">每周六自动抓取四个赛道的 GitHub 热门开源项目，人读的那种周报，不是 star 排行榜。</p>
    {theme_chips(themes)}
  </header>

  <p class="scope">下面是最近三个月的报告（{len(recent)} 篇）。{f'更早的 {older} 篇在<a href="archive.html">历史归档</a>。' if older else ''}</p>

  {empty}
  {''.join(groups)}

  <footer class="foot">
    <a href="archive.html">历史归档 →</a>
    <span>数据源：github.com/trending + GitHub Search API</span>
  </footer>
</div>
{FILTER_JS}
"""
    return shell("GitHub 周报", body)


def build_archive(reports, themes):
    by_year = {}
    for r in reports:
        by_year.setdefault(r["date"][:4], []).append(r)

    groups = []
    for year in sorted(by_year, reverse=True):
        cards = "".join(card(r) for r in by_year[year])
        groups.append(
            f'<div class="year"><h2>{year} 年 · {len(by_year[year])} 篇</h2><div class="grid">{cards}</div></div>'
        )

    body = f"""
<div class="page">
  <header class="cover">
    <a class="back" href="index.html">← 返回首页</a>
    <h1>历史归档</h1>
    <p class="subtitle">全部 {len(reports)} 篇报告，按年份倒序。可以按主题筛选。</p>
    {theme_chips(themes)}
  </header>

  {''.join(groups)}

  <footer class="foot">
    <a href="index.html">← 返回首页</a>
  </footer>
</div>
{FILTER_JS}
"""
    return shell("历史归档 · GitHub 周报", body)


def build_report(rep, reports):
    body_html = split_sections(render_markdown(rep["md"]))

    # Same theme, adjacent weeks, so a reader can follow one track through time.
    same = [r for r in reports if r["theme"] == rep["theme"]]
    idx = same.index(rep)
    prev_r = same[idx + 1] if idx + 1 < len(same) else None
    next_r = same[idx - 1] if idx > 0 else None
    nav = []
    if next_r:
        nav.append(f'<a href="{next_r["slug"]}.html">← 更新一期（{next_r["date"]}）</a>')
    if prev_r:
        nav.append(f'<a href="{prev_r["slug"]}.html">更早一期（{prev_r["date"]}）→</a>')

    window = (
        f'{rep["week_start"]} – {rep["week_end"]}' if rep["week_start"] else rep["date"]
    )

    body = f"""
<div class="page report" style="--accent:{rep['accent']}">
  <header class="cover">
    <a class="back" href="../index.html">← 返回首页</a>
    <h1>{html.escape(rep['title'])}</h1>
    <div class="meta">
      <span class="badge">{html.escape(rep['theme_title'])}</span>
      <span>{window}</span>
      <span>{rep['count']} 个项目</span>
    </div>
    <p class="subtitle">{html.escape(rep['theme_subtitle'])}</p>
  </header>

  {body_html}

  <nav class="pager">{''.join(nav)}</nav>
  <footer class="foot">
    <a href="../index.html">← 返回首页</a>
    <a href="../archive.html">历史归档</a>
  </footer>
</div>
"""
    return shell(f"{rep['theme_title']} · {rep['date']} · GitHub 周报", body, css_depth=1)


def _as_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


# --------------------------------------------------------------------------

CSS = """
/* Shared styling. Palette and type follow the industry-analysis reports:
   warm paper background, serif CJK, one accent per theme. */
:root {
  --bg: #faf9f7;
  --bg-card: #ffffff;
  --text: #1f2320;
  --text-dim: #5b6560;
  --border: #e4e1da;
  --accent: #2f6f5e;
  --accent-soft: #e8f2ee;
  font-family: "Songti SC", "Noto Serif SC", "PingFang SC", "Hiragino Sans GB", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #161915; --bg-card: #1f231e; --text: #e8e6e0;
    --text-dim: #a3a89e; --border: #333a32; --accent-soft: #23342c;
  }
}
:root[data-theme="dark"] {
  --bg: #161915; --bg-card: #1f231e; --text: #e8e6e0;
  --text-dim: #a3a89e; --border: #333a32; --accent-soft: #23342c;
}

* { box-sizing: border-box; }
body { background: var(--bg); color: var(--text); margin: 0; line-height: 1.75; }
a { color: var(--accent); }
.page { max-width: 880px; margin: 0 auto; padding: 48px 24px 96px; }

.cover h1 { font-size: 2.1rem; margin: 0 0 8px; letter-spacing: 0.02em; }
.cover .subtitle { color: var(--text-dim); font-size: 1rem; margin: 0 0 20px; }
.back { display: inline-block; font-size: 0.85rem; color: var(--text-dim); text-decoration: none; margin-bottom: 16px; }
.back:hover { color: var(--accent); }
.scope { color: var(--text-dim); font-size: 0.9rem; margin: 24px 0 8px; }
.empty { color: var(--text-dim); padding: 32px 0; }

/* ---- theme filter ---- */
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 20px 0 8px; }
.chip {
  --chip: var(--accent);
  font: inherit; font-size: 0.85rem; cursor: pointer;
  padding: 5px 14px; border-radius: 999px;
  border: 1px solid var(--border); background: var(--bg-card); color: var(--text-dim);
}
.chip:hover { border-color: var(--chip); color: var(--chip); }
.chip.is-on { background: var(--chip); border-color: var(--chip); color: #fff; font-weight: 600; }

/* ---- listings ---- */
.week, .year { margin: 32px 0; }
.week h2, .year h2 {
  font-size: 1.05rem; color: var(--text-dim); font-weight: 600;
  border-bottom: 1px solid var(--border); padding-bottom: 6px; margin-bottom: 16px;
}
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }

.card {
  --accent: #2f6f5e;
  background: var(--bg-card); border: 1px solid var(--border);
  border-top: 3px solid var(--accent); border-radius: 10px;
  padding: 16px 18px; display: flex; flex-direction: column;
}
.card[hidden] { display: none; }
.card-head { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.badge {
  display: inline-block; padding: 2px 10px; border-radius: 999px;
  font-size: 0.75rem; font-weight: 600; background: var(--accent); color: #fff;
}
.card-head time { color: var(--text-dim); font-size: 0.8rem; }
.card h3 { font-size: 1.05rem; margin: 10px 0 4px; line-height: 1.5; }
.card h3 a { text-decoration: none; color: var(--text); }
.card h3 a:hover { color: var(--accent); }
.card-sub { color: var(--text-dim); font-size: 0.85rem; margin: 0 0 10px; }
.card-picks { list-style: none; padding: 0; margin: 0 0 12px; font-size: 0.85rem; }
.card-picks li { padding: 2px 0; border-bottom: 1px dashed var(--border); }
.card-picks li:last-child { border-bottom: none; }
.card-picks a { text-decoration: none; }
.card-picks a:hover { text-decoration: underline; }
.card-picks .more { color: var(--text-dim); }
.card-foot {
  margin-top: auto; display: flex; justify-content: space-between; align-items: center;
  font-size: 0.8rem; color: var(--text-dim);
}
.card-foot .go { text-decoration: none; font-weight: 600; }

/* ---- a single report ---- */
.report .meta { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; font-size: 0.85rem; color: var(--text-dim); margin-bottom: 8px; }
.report .lede { font-size: 1.02rem; margin: 24px 0 8px; padding: 16px 20px; background: var(--accent-soft); border-radius: 10px; }
.report .lede p:first-child { margin-top: 0; }
.report .lede p:last-child { margin-bottom: 0; }
section.repo {
  background: var(--bg-card); border: 1px solid var(--border);
  border-left: 4px solid var(--accent); border-radius: 10px;
  padding: 4px 22px 18px; margin: 18px 0;
}
section.repo h2 { font-size: 1.15rem; margin: 18px 0 6px; }
section.repo h2 a { text-decoration: none; }
blockquote {
  margin: 10px 0; padding: 8px 14px; color: var(--text-dim);
  border-left: 2px solid var(--border); font-size: 0.92rem;
}
ul.evidence { margin: 8px 0; padding-left: 1.2em; }
ul.evidence li { margin: 4px 0; font-size: 0.92rem; color: var(--text-dim); }
/* Inside a repo block the only list is the stars/language/homepage meta line,
   which reads as metadata rather than as bullet points. */
section.repo ul.evidence { list-style: none; padding-left: 0; margin: 6px 0 10px; }
section.repo ul.evidence li { font-size: 0.85rem; margin: 2px 0; }
code { background: var(--accent-soft); padding: 1px 5px; border-radius: 4px; font-size: 0.88em; }

.pager { display: flex; justify-content: space-between; gap: 12px; margin: 40px 0 0; font-size: 0.9rem; }
.pager a { text-decoration: none; }
.foot {
  margin-top: 56px; padding-top: 16px; border-top: 1px solid var(--border);
  color: var(--text-dim); font-size: 0.85rem;
  display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px;
}

@media (max-width: 600px) {
  .page { padding: 32px 16px 64px; }
  .cover h1 { font-size: 1.6rem; }
  .grid { grid-template-columns: 1fr; }
  .pager { flex-direction: column; }
}
"""


def main():
    themes = load_themes()
    reports = collect(themes)
    if not reports:
        sys.exit("no reports found under reports/ - nothing to build")

    # Rebuild from scratch so deleted reports do not linger as orphan pages.
    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "r").mkdir(parents=True)
    (DOCS / "assets").mkdir()
    (DOCS / "data").mkdir()

    # Pages is Jekyll-backed by default and would skip anything it considers
    # special; this opts the whole site out of that processing.
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "assets" / "site.css").write_text(CSS.strip() + "\n", encoding="utf-8")

    for rep in reports:
        (DOCS / "r" / f"{rep['slug']}.html").write_text(build_report(rep, reports), encoding="utf-8")

    (DOCS / "index.html").write_text(build_index(reports, themes), encoding="utf-8")
    (DOCS / "archive.html").write_text(build_archive(reports, themes), encoding="utf-8")

    index_data = [
        {k: r[k] for k in ("date", "theme", "theme_title", "title", "count", "slug", "picks")}
        for r in reports
    ]
    (DOCS / "data" / "reports.json").write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    per_theme = {}
    for r in reports:
        per_theme[r["theme"]] = per_theme.get(r["theme"], 0) + 1
    info(f"built {len(reports)} reports -> docs/  ({', '.join(f'{k}:{v}' for k, v in per_theme.items())})")


if __name__ == "__main__":
    main()
