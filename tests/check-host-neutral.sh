#!/bin/sh
# Fail if host-specific wording appears in the files every host reads.
# Host-specific wording belongs in hosts/, README.md, agents/, tests/ and fixtures/.
#
# Usage: sh tests/check-host-neutral.sh   (run from anywhere)

repo=$(cd "$(dirname "$0")/.." && pwd)
cd "$repo" || exit 2

# Neutral files: every .md except the allowlisted places.
files=$(find . -name '*.md' \
  -not -path './.git/*' -not -path './hosts/*' -not -path './agents/*' \
  -not -path './tests/*' -not -path './fixtures/*' -not -name 'README.md' -not -name 'LICENSE*' | sort)

# Case-sensitive terms, POSIX ERE (no \b, which BSD tools don't support).
# "Glob" capitalized is the tool name; "a glob pattern" in prose is fine.
w='[^[:alnum:]_]'
terms="(^|$w)Glob(\$|$w)|Claude Code|[$]ARGUMENTS|~/[.]claude|/skills(\$|$w)|python3"

hits=0
for f in $files; do
  # Blank out the SKILL.md frontmatter (keeping line numbers), then search.
  out=$(awk -v F="$f" '
    NR == 1 && $0 == "---" && F ~ /SKILL[.]md$/ { infm = 1; print ""; next }
    infm && $0 == "---" { infm = 0; print ""; next }
    infm { print ""; next }
    { print }
  ' "$f" | grep -nE "$terms" | sed "s|^|$f:|")
  if [ -n "$out" ]; then
    printf '%s\n' "$out"
    hits=1
  fi
done

if [ "$hits" -ne 0 ]; then
  echo "host-neutral check: FAIL (move host-specific wording into hosts/)"
  exit 1
fi
echo "host-neutral check: PASS"
