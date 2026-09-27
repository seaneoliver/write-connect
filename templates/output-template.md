# Output Template

## Assembly Format

```
# Connect Review Draft: [Review Period]
Generated: [date]
Source logs: [list of log files read, date range]

---

## Section 1: What results did you deliver, and how did you do it?
Character count: [X] / 6,000 (form count, must be at or under the limit)

[Draft]

---

## Section 2: Reflect on recent setbacks: what did you learn and how did you apply a growth mindset?
Character count: [X] / 1,000 (form count, must be at or under the limit)

[Draft]

---

## Section 3: Goals for the upcoming period

### Goal 1: [Title]
Character count: [X] / 1,200 (form count, must be at or under the limit)
[Draft]

### Goal 2: [Title]
Character count: [X] / 1,200 (form count, must be at or under the limit)
[Draft]

### Goal 3: [Title]
Character count: [X] / 1,200 (form count, must be at or under the limit)
[Draft]

### Goal 4: [Title] (only if goal_4_title is set in USER-CONFIG)
Character count: [X] / 1,200 (form count, must be at or under the limit)
[Draft]

---

## Section 4: How will your actions and behaviors help you reach your goals?
Character count: [X] / 1,000 (form count, must be at or under the limit)

[Draft]
```

## Gap Analysis (append after draft)

```
---

## Gap Analysis

### Coverage gaps (sparse and missing weeks)
[List each week by date (YYYY-MM-DD): weeks where ## Completed had fewer than 2 bullets, and weeks with no log file]

### Evidence to add
[Every `[number from your log]` placeholder in the draft, and any claim that would be stronger with a number or result the logs don't state]

### Check these dates
[Boundary-week items that couldn't be dated, and files that used an alternate heading for ## Completed]

### Sections near their limit
[Any section over 90% of its limit, so the user knows edits there have little room]

### Missing inputs
[Any USER-CONFIG file that was blank or not found and was skipped, e.g. no past review]

### Missing requirements
[Flag if security, quality, or AI are not addressed in Section 1]
[Flag if Section 3 has no goal with a security reference]

### Themes in logs not captured
[Any significant recurring workstream that didn't make it into the draft - user may want to add]
```
