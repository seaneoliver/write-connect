# Test expectations

Every host's output must satisfy these facts. They check what was extracted, not how it was worded. `tests/check_output.py` automates them.

Test review period: **2026-10-01 to 2026-11-13**. All fixtures are fictional.

## Every drafting case

- Exactly one draft is saved under `Drafts/`.
- Every section fits its limit as the Connect form counts it (characters plus one per line break): Results 6,000, Setbacks 1,000, each goal 1,200, Behaviors 1,000.
- Results and Setbacks contain no number that doesn't appear somewhere in `fixtures/`.

## `normal` and `four-goal`

- Nothing from the out-of-period week appears in the four form sections (no "Heron"), and `2026-09-14` is not listed as a source. The header and gap analysis may mention it as excluded.
- In the boundary week (`2026-09-28 Work.md`), the October item (Project Osprey) appears in Results and the September item (Project Kestrel) appears in no form section.
- The alternate-heading week (`## Accomplishments:`) is read: Project Wren appears in Results.
- The gap analysis flags the thin week (2026-10-19) and the missing week (2026-10-26).
- `normal`: 3 goals. `four-goal`: 4 goals, and Results has a Goal #4 bucket.

## `paste`

- The log folder is empty. The prompt supplies `fixtures/paste-notes.md` as pasted notes.
- Project Curlew appears in Results, and the gap analysis says the input was pasted notes.

## `missing-goals`

- `goals_path` points to a file that doesn't exist. The run stops before drafting, names `missing-GOALS.md`, and saves nothing.

## `zero-evidence`

- Every `## Completed` section is empty. The run stops with a clear message and saves nothing.

## Host notes

Facts confirmed or refuted while running each host are recorded here.

Recorded 2026-09-27 on macOS:

- **Claude Code:** `claude -p` prints only the final message, so the runner saves the full transcript (`--output-format stream-json`) to see the "Using hosts/..." line on runs that stop before drafting.
- **Copilot CLI:** project skills in `.github/skills` are discovered, and `/write-connect` and a plain request both start the skill. `$ARGUMENTS` isn't needed: the period is read from the request. Headless runs need `--allow-tool 'shell(python3:*)' --allow-tool write`. The model sometimes tries to write section text to temp files first; those shell writes are denied and it falls back to stdin. About 50 AI credits per run.
- **Codex CLI:** the CLI bundled in ChatGPT.app works with its saved sign-in. Skills in `.agents/skills` are discovered in `codex exec`, and `$write-connect` starts the skill. The trimmed frontmatter (`name`, `description`, `allowed-tools`) loads without a validation error. With many user-level skills installed, Codex warns it exceeded its skills context budget and drops skill descriptions, which makes automatic invocation unreliable on such machines.
- **Cowork and Copilot in VS Code:** not yet run.

