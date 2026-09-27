# Host: GitHub Copilot

Read this file in Step 1 when `host` is `copilot`. It covers Copilot CLI and Copilot agent mode in VS Code.

## Capabilities

| Capability | Copilot |
|---|---|
| Run a command (shell) | Yes. The user approves it, or it is pre-approved (for example `--allow-tool 'shell(python3:*)'` in Copilot CLI) |
| Ask the user and wait | Yes in chat and the interactive CLI. Not when Copilot CLI runs with `-p` and `--no-ask-user` |
| Invocation arguments | No `$ARGUMENTS`. Read the review period from the user's request text |
| Where relative paths resolve | The folder Copilot CLI was started in, or the open workspace folder in VS Code |

## Verb-to-tool map

| Verb in the skill | Tool |
|---|---|
| List files matching a pattern | The glob or file search tool (`glob` in Copilot CLI, workspace file search in VS Code) |
| Read a file | The file read tool |
| Write a file | The file create or edit tool |
| Run a command | The shell or terminal tool |
| Ask the user and wait | Reply in chat and wait. In a non-interactive run, use the answers already given in the request |
| Count characters | Run the counter below in the shell tool |

## Character counter

Pass each section on stdin, one section per command. The first number is the raw count, the second is the form count (one extra character per line break, because the Connect form uses CRLF).

```bash
python3 -c "import sys; t=sys.stdin.read().rstrip('\n'); print(len(t), len(t)+t.count('\n'))" <<'EOF'
[section text]
EOF
```
