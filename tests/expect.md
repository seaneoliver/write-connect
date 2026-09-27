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
