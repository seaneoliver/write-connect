# Log Parsing Rules

## File discovery

Configure your log location in `USER-CONFIG.md`:
- `log_folder` — the folder containing your work logs (e.g., `Logs/`)
- `log_pattern` — the glob pattern for log files (e.g., `*Work.md`)

Use Glob to find all matching files: `{log_folder}/{log_pattern}`
Filter to files whose date falls within the review period.
Read each file.

## Section parsing

- `## Completed` — PRIMARY extraction target. Bullet list of work completed that week.
- `## What I'm Working on` — workstream headings. Use for goal bucket mapping only, not for content extraction.
- `## Questions/Risks/Blockers` — may surface setback material for Section 2.
- Daily journal entries (Mon-Fri) — sparse, mostly meeting names. Read for context but low signal.
- **Reminders block** — static boilerplate at the bottom of every log. Skip entirely. Do not extract from it.

## Coverage flagging

Note any weeks where `## Completed` is empty or has fewer than 2 bullets. List these at the end as potential coverage gaps.
