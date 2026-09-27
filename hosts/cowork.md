# Host: Claude Cowork

Read this file in Step 1 when `host` is `cowork`.

## Capabilities

| Capability | Cowork |
|---|---|
| Run a command (shell) | Yes, in Cowork's isolated VM. `python3` is available there |
| Ask the user and wait | Yes |
| Invocation arguments | No `$ARGUMENTS`. Read the review period from the user's request text |
| Where relative paths resolve | The root of the folder the user connected to the session. Write paths in `USER-CONFIG.md` relative to that folder |

## Verb-to-tool map

| Verb in the skill | Tool |
|---|---|
| List files matching a pattern | Glob, inside the connected folder |
| Read a file | Read |
| Write a file | Write, into the connected folder so the user can open the draft |
| Run a command | Bash, in the VM |
| Ask the user and wait | Reply in the session and wait |
| Count characters | Run the counter below with Bash |

## Character counter

Pass each section on stdin, one section per command. The first number is the raw count, the second is the form count (one extra character per line break, because the Connect form uses CRLF).

```bash
python3 -c "import sys; t=sys.stdin.read().rstrip('\n'); print(len(t), len(t)+t.count('\n'))" <<'EOF'
[section text]
EOF
```
