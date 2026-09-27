# USER-CONFIG - write-connect

This is a template. Copy it to `USER-CONFIG.md` in the same folder and fill that in (`cp USER-CONFIG.example.md USER-CONFIG.md`). Your copy is gitignored, so `git pull` updates never overwrite it.

All paths are relative to the folder you open Claude Code in (usually your notes or vault root), not this skill folder.

Fill in each field before your first run. The skill reads this file in Step 1 to resolve all personal paths and labels.

---

## File Paths

```yaml
# Folder where your weekly work logs live
log_folder: "Logs/"

# Glob pattern for log files. Use * as the wildcard, not YYYY-MM-DD.
# Each filename must contain its date as YYYY-MM-DD (e.g. "2026-09-21 Work.md")
# Examples: "* Work.md" or "*-work-log.md"
# Log format: see templates/weekly-log-template.md
log_pattern: "* Work.md"

# Path to your most recent completed Connect review (optional)
# Used as style and structure reference
# First Connect? Leave blank and the skill will skip it
# Use the real filename, e.g. "References/Connect-Review-H1 FY26.md". Don't use [Period]:
# that resolves to the CURRENT period, the same file output_path writes to
past_review_path: ""

# Path to your role summary or job description
# Used for IC-level framing in Section 1 and Section 3
role_summary_path: "Role-Summary.md"

# Path to your current goals file
# Used to populate Section 3 (Goals) and cross-reference Section 1 themes
goals_path: "GOALS-4.md"

# Path to your voice/tone notes (optional)
# If you have a style guide or writing rules file, add it here
# Leave blank to skip
voice_notes_path: ""

# Where to save the finished draft
# [Period] will be replaced with the review period you provide at runtime
output_path: "Drafts/Connect-Review-[Period].md"
```

---

## Compliance Goal Text

```yaml
# Paste the standard compliance goal wording from your Connect form.
# Used verbatim for Goal #1. Leave blank and the draft will show a placeholder.
compliance_goal_text: "Complete all required compliance trainings on time and handle customer data according to policy."
```

---

## Goal Bucket Names

Replace these with your actual Connect goal titles. These appear in Section 1 groupings and Section 3.

```yaml
goal_1_title: "Compliance"
# Description: Trust Code, ethics training, values-based actions
# Note: Goal #1 is usually the standard Microsoft compliance goal. Keep the title; paste its wording into compliance_goal_text below

goal_2_title: "Deliver Harbor Analytics reporting tools"
# Description: Your primary delivery or program goal
# Example: "Drive Governance and Stakeholder Experience"

goal_3_title: "Repeatable team processes"
# Description: Your operational excellence or enablement goal
# Example: "Operational Excellence and Tooling Adoption"

goal_4_title: "Grow the team AI skills"
# Optional. Leave blank if your Connect form has three goals
```

---

## Manager Reference

```yaml
# How to refer to your manager in the review (used in Section 2 feedback themes)
manager_name: "my manager"

# Optional. Recurring feedback from your manager this cycle, one theme per line.
# Section 2 addresses these only where your logs show evidence. Leave blank to skip.
manager_feedback_themes: ""
```

---

## Notes

- `log_folder`, `role_summary_path`, and `goals_path` should point to real files. `past_review_path` and `voice_notes_path` are optional: leave them blank and the skill skips them and notes it in the gap analysis.
- Goal bucket names drive grouping in Section 1 and the goal structure in Section 3. Match them to what is in your actual Connect form.
- The `past_review_path` file is read for structural and language reference only - no content is copied verbatim.
