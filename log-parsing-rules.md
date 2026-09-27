# Log Parsing Rules

## Log format

Logs are expected to follow `templates/weekly-log-template.md`: one Markdown file per week, with the `##` section headings below. Logs that use different headings still work, but extraction quality drops.

## File discovery

Configure your log location in `USER-CONFIG.md`:
- `log_folder` - the folder containing your work logs (e.g., `Logs/`)
- `log_pattern` - a glob pattern for log files (e.g., `* Work.md`). Use `*` as the wildcard. Do not write `YYYY-MM-DD` here: Glob treats it as literal text and matches nothing.

Use Glob to find all matching files: `{log_folder}/{log_pattern}`
Read the date from each filename (the first `YYYY-MM-DD` in the name). If a filename has no date, use the date in the file's first heading.
Filter to files whose date falls within the review period.
Read each file.

If no files match, stop and tell the user the exact pattern you searched, the folder, and how many files that folder contains. Do not generate a draft from zero logs.

## Section parsing

Match headings by their text, ignoring a trailing colon (`## What I'm Working on:` counts).

- `## Completed` - PRIMARY extraction target. Each top-level bullet is one accomplishment, ideally written as an outcome headline. Nested sub-bullets are the evidence for their parent bullet: read them together, never as separate accomplishments.
- `## What I'm Working on` - workstream headings. Use for goal bucket mapping only, not for content extraction.
- `## Priorities` (if present) - use as a hint for goal bucket mapping only.
- `## Questions/Risks/Blockers` - primary source of setback material for Section 2.
- Daily journal entries (Mon-Fri) - read for context. They are a secondary source for Section 2: frustrations, rework, overload, and things that went wrong often show up here before (or instead of) the Blockers section.
- **Reminders block** - static boilerplate at the bottom of every log. Skip entirely. Do not extract from it.
- Any other heading - ignore for extraction.

## Coverage flagging

Note any weeks where `## Completed` is missing, empty, or has fewer than 2 top-level bullets (sub-bullets don't count). List these at the end as potential coverage gaps.
