# USER-CONFIG — write-connect

Fill in each field before your first run. The skill reads this file in Step 1 to resolve all personal paths and labels.

---

## File Paths

```yaml
# Folder where your weekly work logs live
log_folder: "Logs/"

# Naming pattern for log files (use YYYY-MM-DD for date placeholder)
# Examples: "YYYY-MM-DD Work.md" or "YYYY-MM-DD-work-log.md"
log_pattern: "YYYY-MM-DD Work.md"

# Path to your most recent completed Connect review
# Used as style and structure reference
past_review_path: "References/Connect-Review-[Period].md"

# Path to your role summary or job description
# Used for IC-level framing in Section 1 and Section 3
role_summary_path: "Role-Summary.md"

# Path to your current goals file
# Used to populate Section 3 (Goals) and cross-reference Section 1 themes
goals_path: "GOALS.md"

# Path to your voice/tone notes (optional)
# If you have a style guide or writing rules file, add it here
# Leave blank to skip
voice_notes_path: ""

# Where to save the finished draft
# [Period] will be replaced with the review period you provide at runtime
output_path: "References/Connect-Review-[Period].md"
```

---

## Goal Bucket Names

Replace these with your actual Connect goal titles. These appear in Section 1 groupings and Section 3.

```yaml
goal_1_title: "Compliance"
# Description: Trust Code, ethics training, values-based actions
# Note: Goal #1 is usually the standard Microsoft compliance goal — keep the title but customize measures

goal_2_title: "Goal #2 Title Here"
# Description: Your primary delivery or program goal
# Example: "Drive Governance and Stakeholder Experience"

goal_3_title: "Goal #3 Title Here"
# Description: Your operational excellence or enablement goal
# Example: "Operational Excellence and Tooling Adoption"
```

---

## Manager Reference

```yaml
# How to refer to your manager in the review (used in Section 2 feedback themes)
manager_name: "your manager"
```

---

## Notes

- Do not leave any path pointing to a file that does not exist — the skill will fail to read it.
- If you do not have a voice/tone notes file, leave `voice_notes_path` blank. The skill will skip it.
- Goal bucket names drive grouping in Section 1 and the goal structure in Section 3. Match them to what is in your actual Connect form.
- The `past_review_path` file is read for structural and language reference only — no content is copied verbatim.
