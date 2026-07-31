#!/usr/bin/env python3
"""Validate a generated rednote.md against Xiaohongshu's hard limits.

A numeric limit is not something to leave to the model's judgement: the first
launchd run produced a 1618-character body against a 1000-character cap. This
runs after generation and fails the build, so an over-length draft never gets
committed as if it were publishable.
"""

import argparse
import re
import sys
from pathlib import Path

TITLE_MAX = 20
BODY_MAX = 1000
BODY_MIN = 300


def section(text, name):
    """Return the text under '## <name>' up to the next '## ' heading."""
    m = re.search(rf"^##\s*{re.escape(name)}.*?$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="path to rednote.md")
    args = ap.parse_args()

    p = Path(args.path)
    if not p.exists():
        print(f"FAIL: {p} does not exist", file=sys.stderr)
        return 1

    text = p.read_text(encoding="utf-8")
    problems = []

    title_block = section(text, "标题")
    body = section(text, "正文")
    tags = section(text, "话题标签")

    if title_block is None:
        problems.append("missing '## 标题' section")
        title = ""
    else:
        lines = [l.strip() for l in title_block.splitlines() if l.strip()]
        title = lines[0] if lines else ""
        if not title:
            problems.append("'## 标题' section is empty")
        elif len(title) > TITLE_MAX:
            problems.append(f"title is {len(title)} chars, limit {TITLE_MAX}: {title!r}")

    # The command's template used to carry parenthetical hints in its headings;
    # if one survives into the output, the model copied the template verbatim.
    for leak in ("≤20 字", "≤ 20 字", "<DATE>", "owner/repo", "<full_name>"):
        if leak in text:
            problems.append(f"template placeholder leaked into output: {leak!r}")

    if body is None:
        problems.append("missing '## 正文' section")
    else:
        n = len(body)
        if n > BODY_MAX:
            problems.append(f"body is {n} chars, limit {BODY_MAX} (over by {n - BODY_MAX})")
        elif n < BODY_MIN:
            problems.append(f"body is only {n} chars — suspiciously short")
        if "https://" in body:
            problems.append("body contains 'https://' — Xiaohongshu strips full URLs, use bare github.com/...")

    if tags is None:
        problems.append("missing '## 话题标签' section")
    elif not tags.lstrip().startswith("#"):
        problems.append("'## 话题标签' section does not start with a # tag")

    if problems:
        print(f"FAIL: {p}", file=sys.stderr)
        for prob in problems:
            print(f"  - {prob}", file=sys.stderr)
        return 1

    print(f"OK: {p} (title {len(title)} chars, body {len(body)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
