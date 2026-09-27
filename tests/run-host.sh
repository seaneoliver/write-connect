#!/bin/sh
# Run write-connect headless on one host against one fixture case, then check the output.
#
# Usage: sh tests/run-host.sh <host> <case> [--expect-host]
#   host: claude-code | codex | copilot
#   case: normal | four-goal | paste | missing-goals | zero-evidence
#   --expect-host: also require the run to name the host file it loaded
#
# Each run uses a brand-new scratch project and leaves it in place for inspection.
# Prints the scratch path and the check result. Exit code is the check's.

set -u
host=${1:?host required}
case_name=${2:?case required}
expect_host=${3:-}

repo=$(cd "$(dirname "$0")/.." && pwd)
config="$repo/fixtures/config/$case_name.md"
[ -f "$config" ] || { echo "unknown case: $case_name" >&2; exit 2; }

scratch=$(mktemp -d "${TMPDIR:-/tmp}/write-connect-$host-$case_name.XXXXXX")
case "$host" in
  claude-code) skill_dir="$scratch/.claude/skills/write-connect" ;;
  codex)       skill_dir="$scratch/.agents/skills/write-connect" ;;
  copilot)     skill_dir="$scratch/.github/skills/write-connect" ;;
  *) echo "unknown host: $host" >&2; exit 2 ;;
esac

# Install the skill as a user would: no git history, tests or fixtures.
mkdir -p "$skill_dir"
rsync -a --exclude .git --exclude tests --exclude fixtures "$repo/" "$skill_dir/"
cp "$config" "$skill_dir/USER-CONFIG.md"
# Claude Code keeps a blank host to prove the default (existing installs have no host field).
if [ "$host" != claude-code ]; then
  printf '\n## Host\n\n```yaml\nhost: "%s"\n```\n' "$host" >> "$skill_dir/USER-CONFIG.md"
fi

# Fixtures go to fixed paths under the project root, whatever the host.
cp -R "$repo/fixtures/Logs" "$repo/fixtures/Logs-empty" "$scratch/"
cp "$repo/fixtures/GOALS.md" "$repo/fixtures/GOALS-4.md" "$repo/fixtures/Role-Summary.md" "$scratch/"
mkdir -p "$scratch/NoLogs" "$scratch/Drafts"

period="2026-10-01 to 2026-11-13"
prompt="Answers to your setup questions: 1. Review period: $period. 2. No role or org changes since last cycle. 3. No supplemental notes.
This is a non-interactive test run. Do not wait for replies. When you reach the refine-or-save question, save the draft to output_path."
if [ "$case_name" = paste ]; then
  prompt="$prompt
I don't keep weekly logs. If no log files match, use these pasted notes as my input:
$(cat "$repo/fixtures/paste-notes.md")"
fi

log="$scratch/run.log"
cd "$scratch" || exit 2
case "$host" in
  claude-code)
    claude -p "/write-connect $period
$prompt" --permission-mode acceptEdits \
      --allowedTools "Read,Write,Edit,Glob,Grep,Bash(python3 *)" --max-turns 60 > "$log" 2>&1
    ;;
  codex)
    codex_bin=${CODEX_BIN:-/Applications/ChatGPT.app/Contents/Resources/codex}
    "$codex_bin" exec --sandbox workspace-write --skip-git-repo-check \
      "\$write-connect $period
$prompt" > "$log" 2>&1
    ;;
  copilot)
    copilot -p "/write-connect $period
$prompt" --allow-tool 'shell(python3:*)' --allow-tool write --no-ask-user > "$log" 2>&1
    ;;
esac

echo "scratch: $scratch"
if [ "$expect_host" = --expect-host ]; then
  python3 "$repo/tests/check_output.py" "$case_name" "$scratch" "$log" --host "$host"
else
  python3 "$repo/tests/check_output.py" "$case_name" "$scratch" "$log"
fi
