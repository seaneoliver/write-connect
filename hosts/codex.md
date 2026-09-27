# Host: OpenAI Codex

Read this file in Step 1 when `host` is `codex`.

## Capabilities

| Capability | Codex |
|---|---|
| Run a command (shell) | Yes, inside the sandbox. Saving the draft needs the `workspace-write` sandbox |
| Ask the user and wait | Yes in the interactive CLI and the IDE extension. Not in `codex exec` |
| Invocation arguments | No `$ARGUMENTS`. Read the review period from the user's request text, for example after `$write-connect` |
| Where relative paths resolve | The directory Codex was started in |

## Verb-to-tool map

| Verb in the skill | Tool |
|---|---|
| List files matching a pattern | A shell listing, for example `ls Logs/*" Work.md"`, or `find` with `-name` |
| Read a file | `cat` in the shell, or the file read tool |
| Write a file | The apply-patch or file write tool |
| Run a command | The shell tool |
| Ask the user and wait | Reply and wait in interactive use. In `codex exec`, use the answers already given in the request |
| Count characters | Run the counter below in the shell |

## Character counter

Pass each section on stdin, one section per command. The first number is the raw count, the second is the form count (one extra character per line break, because the Connect form uses CRLF).

```bash
python3 -c "import sys; t=sys.stdin.read().rstrip('\n'); print(len(t), len(t)+t.count('\n'))" <<'EOF'
[section text]
EOF
```
