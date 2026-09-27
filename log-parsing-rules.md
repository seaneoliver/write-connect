# Log Parsing Rules

## Log format

Logs are expected to follow `templates/weekly-log-template.md`: one Markdown file per week, with the `##` section headings below. Logs that use different headings still work, but extraction quality drops.

## File discovery

Configure your log location in `USER-CONFIG.md`:
- `log_folder` - the folder containing your work logs (e.g., `Logs/`)
- `log_pattern` - a glob pattern for log files (e.g., `* Work.md`). Use `*` as the wildcard. Do not write `YYYY-MM-DD` here: it is matched as literal text and finds nothing.

List the files matching `{log_folder}/{log_pattern}`.
Read the date from each filename (the first `YYYY-MM-DD` in the name). If a filename has no date, use the date in the file's first heading. That date is the start of the log's week.
Keep every file whose week (its date plus 6 days) overlaps the review period, and read each one.

**Boundary weeks.** When a week starts before the period or ends after it, keep only the items dated inside the period:
- A `## Completed` item written with a date, such as `(2026-10-01)`, uses that date.
- An undated item takes the date of the daily note that mentions the same work.
- An item you can't date is kept, and the gap analysis lists it under "Check these dates".

**Missing weeks.** List every week in the review period that has no log file. They go in the gap analysis as coverage gaps.

If no files match, tell the user the exact pattern you searched, the folder, and how many files that folder contains. Then offer the paste path: "If you don't keep weekly logs, paste your notes for the period and I'll draft from those." Do not generate a draft from zero logs. Also offer the paste path when the user says they don't keep logs.

## Pasted notes

When the user pastes notes instead of logs:
- If the paste is empty or has no work items, stop and say so. Do not draft from nothing.
- Map each item to `## Completed` (finished work), `## What I'm Working on` (ongoing work) or `## Questions/Risks/Blockers` (setbacks, problems), then extract exactly as you would from a log.
- Treat items without a date as inside the review period, and say so in the gap analysis.
- The Traceability Gate in `extraction-rules.md` applies to every pasted line.
- In the gap analysis under "Missing inputs", write: "Input: pasted notes, not weekly logs." Skip the per-week coverage checks, which need weekly files.

If files match but none of them has a single item under `## Completed` (or an alias below) inside the review period, stop and tell the user which files you read and that none had completed work to draft from. Do not generate a draft from zero evidence.

## Section parsing

Match headings by their text, ignoring case and a trailing colon (`## What I'm Working on:` counts).

These alternate headings count as `## Completed`: `## Done`, `## Accomplishments`, `## Wins`, `## Shipped`, `## Completed this week`. Say in the gap analysis which files used an alternate heading.

- `## Completed` - PRIMARY extraction target. Each top-level bullet is one accomplishment, ideally written as an outcome headline. Nested sub-bullets are the evidence for their parent bullet: read them together, never as separate accomplishments.
- `## What I'm Working on` - workstream headings. Use for goal bucket mapping only, not for content extraction.
- `## Priorities` (if present) - use as a hint for goal bucket mapping only.
- `## Questions/Risks/Blockers` - primary source of setback material for Section 2.
- Daily journal entries (Mon-Fri) - read for context. They are a secondary source for Section 2: frustrations, rework, overload, and things that went wrong often show up here before (or instead of) the Blockers section.
- **Reminders block** - static boilerplate at the bottom of every log. Skip entirely. Do not extract from it.
- Any other heading - ignore for extraction.

## Coverage flagging

Note any weeks where `## Completed` is missing, empty, or has fewer than 2 top-level bullets (sub-bullets don't count), plus every week with no log file at all. List each by its week date (`YYYY-MM-DD`) in the gap analysis as a coverage gap.
