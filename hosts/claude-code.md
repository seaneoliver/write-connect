# Host: Claude Code

Read this file in Step 1 when `host` is `claude-code` or blank.

## Capabilities

| Capability | Claude Code |
|---|---|
| Run a command (shell) | Yes, with the Bash tool. `python3` is pre-approved by the skill's `allowed-tools` |
| Ask the user and wait | Yes, in an interactive session |
| Invocation arguments | Text after `/write-connect` arrives as `$ARGUMENTS` |
| Where relative paths resolve | The directory Claude Code was launched from, not the skill folder |

## Verb-to-tool map

| Verb in the skill | Tool |
|---|---|
| List files matching a pattern | Glob |
| Read a file | Read |
| Write a file | Write (new file) or Edit (existing file) |
| Run a command | Bash |
| Ask the user and wait | Reply in chat and wait for the next message |
| Count characters | Run the counter below with Bash |

## Character counter

Pass each section on stdin, one section per command. The first number is the raw count, the second is the form count (one extra character per line break, because the Connect form uses CRLF).

```bash
python3 -c "import sys; t=sys.stdin.read().rstrip('\n'); print(len(t), len(t)+t.count('\n'))" <<'EOF'
[section text]
EOF
```
