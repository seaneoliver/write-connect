---
name: write-connect
description: |
  Draft a complete Microsoft Connect performance review from weekly work logs,
  goals, and past review context. Use when: (1) preparing a Connect submission,
  (2) translating work logs into impact-driven review language, (3) drafting
  any of the four Connect sections (results, setbacks, goals, culture behaviors).
  Reads all weekly work logs for the review period automatically — just provide
  the period and any supplemental notes.
argument-hint: "[review period, e.g. 'H2 FY26' or 'November 2025 to May 2026']"
context: fork
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Grep
---

# connect: Microsoft Connect Review Drafter

Generates a complete, paste-ready Connect review draft from weekly work logs.
Translates raw output language into executive-level impact statements, maps work
to Connect goal buckets, counts characters per section, and flags gaps.

---

## Step 1: Load Configuration and Context

Read `USER-CONFIG.md` and hold all values throughout generation.

Then read the files specified in USER-CONFIG:
1. The path in `voice_notes_path` — voice and tone rules
2. The path in `past_review_path` — most recent completed Connect (structure, language, what landed well)
3. The path in `role_summary_path` — role framing at your level
4. The path in `goals_path` — current goals and priorities

Also read `connect-form-reference.md` for section names, character limits, and form guidance.

## Step 2: Gather Inputs

Ask the user three questions only:

1. **Review period:** "What period does this Connect cover?" (e.g., "H2 FY26", "November 2025 to May 2026")
2. **Org/role changes:** "Have your role or org responsibilities changed since last cycle? Any programs, tracking systems, or teams you no longer own?" This determines which measures are still valid for Section 3 goals.
3. **Supplemental notes:** "Any accomplishments, context, or notes to include beyond the work logs?" (optional — they can skip)

Do not ask about file paths. The skill discovers logs automatically.

## Step 3: Discover and Read Work Logs

Read `log-parsing-rules.md` and apply it to discover and parse all work logs within the review period.

## Step 4: Extract and Translate

For every `## Completed` bullet across all logs, read `extraction-rules.md` and apply the full extraction pipeline: classify into goal buckets (see `references/goal-buckets.md`), translate using `references/executive-language.md`, run the Activity Test, apply impact categories, and map security/quality/AI coverage.

## Step 5: Generate Section 1 — Results (6,000 chars)

Read `section-1-results.md` and generate the results section using the What/How/Impact structure.

## Step 6: Generate Section 2 — Setbacks (1,000 chars)

Read `section-2-setbacks.md` and generate the setbacks section using the Name/Changed/Result structure.

## Step 7: Generate Section 3 — Goals (1,200 chars per goal)

Read `section-3-goals.md` and generate goals using the percentage-weighted WHAT/HOW/Measures structure.

## Step 8: Generate Section 4 — Culture Behaviors (1,000 chars)

Read `section-4-behaviors.md` and generate the behaviors section grounded in specific log examples.

## Step 9: Assemble, Count, and Analyze

Read `templates/output-template.md` and assemble the full draft.

**Character counting rules:**
- Count raw (LF newlines) using Python or a script — do not eyeball
- The Connect form uses Windows CRLF line endings. Add 1 char per newline to estimate the form count.
- Flag any section over 90% of its limit before reporting complete (e.g., Section 1 over 5,400, Section 2 over 900, any goal over 1,080, Section 4 over 900)
- If Section 1 is over 5,800 raw chars, convert labeled What/How/Impact sub-sections to prose paragraphs — do not cut proof points

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
