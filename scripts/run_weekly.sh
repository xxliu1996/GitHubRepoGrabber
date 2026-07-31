#!/bin/bash
# Weekly runner for launchd. Invokes Claude Code headlessly on /github-weekly.
#
# launchd starts jobs with a near-empty environment and no login shell, so
# everything the run needs — PATH, the repo location, credentials — has to be
# set up explicitly here rather than inherited.

set -uo pipefail

ROOT="/Users/xingxingliu/Projects/CluadeProjects/GitHubRepoGrabber"
CLAUDE="/Users/xingxingliu/.local/bin/claude"
LOG_DIR="$ROOT/logs"
DATE="$(date +%F)"
LOG="$LOG_DIR/$DATE.log"
START_EPOCH="$(date +%s)"

mkdir -p "$LOG_DIR"

# git needs to find its credential helper and the system binaries
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$HOME/.local/bin"

# claude reads its login token from the "Claude Code-credentials" keychain item,
# and the keychain lookup needs USER/LOGNAME set. Without these the run dies
# with "Not logged in · Please run /login" — verified, not hypothetical.
export HOME="${HOME:-/Users/xingxingliu}"
export USER="${USER:-xingxingliu}"
export LOGNAME="${LOGNAME:-$USER}"
export SHELL="${SHELL:-/bin/zsh}"

{
  echo "==================== $(date '+%F %T %Z') ===================="
  echo "runner  : $0"
  echo "root    : $ROOT"
  echo "claude  : $($CLAUDE --version 2>&1)"

  # Raises the GitHub API ceiling from 60/hr to 5000/hr. Read straight from the
  # keychain rather than a .env file so no plaintext token ever lands on disk.
  # Optional: without it the run still works, it just backs off for a few minutes.
  GITHUB_TOKEN="$(printf 'protocol=https\nhost=github.com\n\n' | git credential fill 2>/dev/null | sed -n 's/^password=//p')"
  if [ -n "$GITHUB_TOKEN" ]; then
    export GITHUB_TOKEN
    echo "token   : loaded from keychain (${#GITHUB_TOKEN} chars)"
  else
    echo "token   : none — anonymous, expect rate-limit backoff"
  fi

  cd "$ROOT" || { echo "FATAL: cannot cd to $ROOT"; exit 1; }

  # Pull first so a report written on another machine does not cause a
  # conflict when this run tries to push.
  git pull --rebase --quiet origin main 2>&1 || echo "WARN: git pull failed, continuing"

  echo "--- running /github-weekly ---"
  "$CLAUDE" -p "/github-weekly" \
    --permission-mode acceptEdits \
    --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,Agent,TodoWrite" \
    2>&1
  STATUS=$?

  echo "--- claude exited with $STATUS ---"

  # Checking that the files merely exist is not enough: a re-run on a date that
  # already has a report will happily exit 0 without regenerating anything.
  # Require all four to have been written during THIS run.
  MISSING=0
  STALE=0
  for f in raw.json report.md rednote.md image-prompts.md; do
    path="$ROOT/reports/$DATE/$f"
    if [ ! -f "$path" ]; then
      echo "MISSING: $f"
      MISSING=$((MISSING + 1))
    elif [ "$(stat -f %m "$path")" -lt "$START_EPOCH" ]; then
      echo "STALE: $f (not rewritten this run)"
      STALE=$((STALE + 1))
    else
      echo "ok: $f ($(wc -c < "$path" | tr -d ' ') bytes)"
    fi
  done

  if [ "$MISSING" -gt 0 ] || [ "$STALE" -gt 0 ]; then
    echo "FAILED: $MISSING missing, $STALE stale — the run did not actually produce a report"
    STATUS=1
  fi

  # Surface the outcome in Notification Center so a silent failure is visible
  # without having to open the log.
  if [ "$STATUS" -eq 0 ]; then
    osascript -e "display notification \"周报已生成：reports/$DATE\" with title \"GitHubRepoGrabber\"" 2>/dev/null
  else
    osascript -e "display notification \"运行失败（退出码 $STATUS），见 logs/$DATE.log\" with title \"GitHubRepoGrabber\" sound name \"Basso\"" 2>/dev/null
  fi

  echo "==================== done: $(date '+%F %T %Z') ===================="
  exit "$STATUS"
} 2>&1 | tee -a "$LOG"

exit "${PIPESTATUS[0]}"
