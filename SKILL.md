---
name: write-connect
description: |
  Draft a complete Microsoft Connect performance review from weekly work logs,
  goals, and past review context. Use when: (1) preparing a Connect submission,
  (2) translating work logs into impact-driven review language, (3) drafting
  any of the four Connect sections (results, setbacks, goals, culture behaviors).
  Reads all weekly work logs for the review period automatically - just provide
  the period and any supplemental notes.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3 *)
---

# connect: Microsoft Connect Review Drafter

Generates a complete, paste-ready Connect review draft from weekly work logs.
Translates raw output language into executive-level impact statements, maps work
to Connect goal buckets, counts characters per section, and flags gaps.

---

## Step 1: Load Configuration and Context

Read `USER-CONFIG.md` (in this skill's folder) and hold all values throughout generation. If it doesn't exist, stop and tell the user: "Copy `USER-CONFIG.example.md` to `USER-CONFIG.md` in the skill folder and fill it in."

**Select the host file.** Read the `host` value in USER-CONFIG: `claude-code`, `copilot`, `codex` or `cowork`. If it is blank or missing, use `claude-code`. Read `hosts/<host>.md` from this skill's folder and start your first message with "Using hosts/<host>.md". Also record it in the draft header (see `templates/output-template.md`). Every action in the steps below ("list the files matching", "read", "write", "run a command", "ask the user and wait", "count characters") uses the tool that host file maps it to. If the host file doesn't exist, stop and tell the user the valid `host` values.

Paths in USER-CONFIG are relative to the user's working folder as your host file defines it, not the skill folder.

Then read the files specified in USER-CONFIG.

**Required.** If either of these is blank, missing or unreadable, stop before drafting and tell the user which setting and path failed. A draft without them would invent your role and goals.
1. The path in `role_summary_path` - role framing at your level
2. The path in `goals_path` - current goals and priorities

**Optional.** If one of these is blank or missing, skip it, note it in the gap analysis, and keep going.
3. The path in `voice_notes_path` - voice and tone rules
4. The path in `past_review_path` - most recent completed Connect (structure, language, what landed well). First-time users won't have one

Also read `connect-form-reference.md` for section names, character limits, and form guidance.

## Step 2: Gather Inputs

If the user's request already names a review period (for example, text after the skill name), use it and skip question 1.

Ask the user these questions in a single message, not one at a time:

1. **Review period:** "What period does this Connect cover?" (e.g., "H2 FY26", "November 2025 to May 2026")
2. **Org/role changes:** "Have your role or org responsibilities changed since last cycle? Any programs, tracking systems, or teams you no longer own?" This determines which measures are still valid for Section 3 goals.
3. **Supplemental notes:** "Any accomplishments, context, or notes to include beyond the work logs?" (optional - they can skip)

Do not ask about file paths. The skill discovers logs automatically.

## Step 3: Discover and Read Work Logs

Read `log-parsing-rules.md` and apply it to discover and parse all work logs within the review period. If there are no logs, it tells you how to work from pasted notes instead.

## Step 4: Extract and Translate

For every `## Completed` bullet across all logs, read `extraction-rules.md` and apply the full extraction pipeline: classify into goal buckets (see `references/goal-buckets.md`), translate using `references/executive-language.md`, run the Activity Test, apply impact categories, and map security/quality/AI coverage.

## Step 5: Generate Section 1: Results (6,000 chars)

Read `section-1-results.md` and generate the results section using the What/How/Impact structure.

## Step 6: Generate Section 2: Setbacks (1,000 chars)

Read `section-2-setbacks.md` and generate the setbacks section using the Name/Changed/Result structure.

## Step 7: Generate Section 3: Goals (1,200 chars per goal)

Read `section-3-goals.md` and generate goals using the percentage-weighted WHAT/HOW/Measures structure.

## Step 8: Generate Section 4: Culture Behaviors (1,000 chars)

Read `section-4-behaviors.md` and generate the behaviors section grounded in specific log examples.

## Step 9: Assemble, Count, and Analyze

Read `templates/output-template.md` and assemble the full draft.

**Character counting rules:**
- Count characters with the character counter in your host file, never by eye. Count each section separately, and leave no temp files in the user's folder. The counter reports the raw count (LF newlines) and the form count.
- The Connect form uses Windows CRLF line endings. Add 1 char per newline to estimate the form count.
- **Limits are hard.** A section fits only when its form count is at or under its limit. Before saving, revise every section that doesn't fit, then count it again. Never save a draft with a section over its limit.
- To shorten Section 1, first convert labeled What/How/Impact sub-sections to prose paragraphs, then merge or cut the weakest initiatives. Cut labels and filler before proof points.
- Flag any section over 90% of its limit in the gap analysis, so the user knows edits there have little room (e.g., Section 1 over 5,400, Section 2 over 900, any goal over 1,080, Section 4 over 900)

**Each section should have been counted during generation (Steps 5-8). Step 9 is a final sanity check, not the first count.**

Include the gap analysis.

## Step 10: Refinement Loop

Ask: "Which section do you want to refine, or shall I save the draft?"

If user requests refinement:
- Regenerate that section only
- Re-count characters
- Show before/after if helpful

If user says save:
- Write draft to the path specified in `output_path` in USER-CONFIG
- Use frontmatter: `aliases`, `created`, `modified`, `tags: [performance, review, connect]`, `categories: ["career"]`

---

## References

See [references/](references/) for Executive Language Quick Reference and Connect Goal Bucket mapping.
