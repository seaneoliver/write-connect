# write-connect

Draft your Microsoft Connect performance review from weekly work logs - not from memory.

---

## What it does

`write-connect` reads your work logs for the review period, extracts completed work, and generates a full four-section Connect draft in one pass. It applies the What/How/Impact structure, maps work to your defined goal buckets, counts characters per section against form limits, and flags gaps before you submit. The output is paste-ready into the Connect form with no reformatting needed.

### What you get

A single Markdown draft containing all four Connect sections, each already within its character limit:

1. **Results** (6,000 chars) - What/How/Impact per initiative, grouped by goal bucket
2. **Setbacks** (1,000 chars) - Name/Changed/Result structure
3. **Goals** (1,200 chars each) - percentage-weighted, with validated measures
4. **Culture Behaviors** (1,000 chars) - grounded in specific examples from your logs

Plus a **gap analysis** flagging anything thin (missing security/quality/AI coverage, sections near their limit) so you know what to shore up before submitting.

---

## Prerequisites

1. Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
2. Weekly work logs, one Markdown file per week, in one folder, with the date in each filename (e.g., `Logs/2026-09-21 Work.md`). **They need the headings the skill reads**: `## Completed`, `## What I'm Working on`, and `## Questions/Risks/Blockers`. Start from [`templates/weekly-log-template.md`](templates/weekly-log-template.md). The more weeks of logs you have, the better the draft.
3. A role summary or job description file (used for IC-level framing)
4. A goals file covering the review period
5. Optional: a past Connect review (used as a style and structure reference). If this is your first Connect, skip it.

---

## Setup for Claude Code

1. Clone or copy this skill folder into your Claude skills directory:
   ```bash
   git clone https://github.com/seaneoliver/write-connect ~/.claude/skills/write-connect
   ```
   That folder location is all it takes to install it. There's nothing to register.
2. Create your config from the template:
   ```bash
   cd ~/.claude/skills/write-connect && cp USER-CONFIG.example.md USER-CONFIG.md
   ```
3. Fill in `USER-CONFIG.md` with your file paths and goal names (see [Configure it for yourself](#configure-it-for-yourself)). Your copy is gitignored, so `git pull` updates won't touch it.
4. Start a new Claude Code session and type `/skills`. You should see `write-connect` in the list.

---

## Setup for VS Code + Copilot

1. Install the GitHub Copilot extension in VS Code.
2. Copy this skill folder into your workspace, then copy `USER-CONFIG.example.md` to `USER-CONFIG.md` and fill it in.
3. Open Copilot Chat in Agent mode so it can read files in your workspace.
4. Attach `SKILL.md` as context (type `#file:SKILL.md`, or drag the file into the chat), and ask it to follow the steps for your review period.
5. Copilot will walk through the steps; paste your work log contents when prompted if auto-discovery is not available.

---

## Configure it for yourself

Fill in `USER-CONFIG.md` (copied from `USER-CONFIG.example.md`) before your first run. All paths are relative to the folder you open Claude Code in, not the skill folder. The table below shows what you need:

| Question | Where it goes |
|---|---|
| Where are your work logs stored? | `log_folder` in USER-CONFIG |
| What is your log file naming pattern? Use `*` as the wildcard, e.g. `* Work.md` | `log_pattern` in USER-CONFIG |
| Where is your most recent Connect review? (optional) | `past_review_path` in USER-CONFIG |
| Where is your role summary or job description? | `role_summary_path` in USER-CONFIG |
| Where is your goals file? | `goals_path` in USER-CONFIG |
| Do you have a voice or style guide? (optional) | `voice_notes_path` in USER-CONFIG |
| What are your goal bucket names? | `goal_1_title` to `goal_3_title` (plus optional `goal_4_title`) in USER-CONFIG |
| What is the compliance goal wording on your form? | `compliance_goal_text` in USER-CONFIG |
| Any recurring feedback from your manager this cycle? (optional) | `manager_feedback_themes` in USER-CONFIG |
| Where should the draft be saved? | `output_path` in USER-CONFIG |

See `USER-CONFIG.example.md` for the full fill-in-the-blank template.

---

## Run it

1. Open a Claude Code session in your vault or project directory.
2. Type `/write-connect H2 FY26` (replace with your review period).
3. Answer the setup questions (any org/role changes since last cycle, and any supplemental notes), then let the skill generate the full draft. It asks for the review period too if you didn't include one.
4. Refine any section, then tell it to save. Expect one permission prompt the first time it runs Python to count characters.

---

## File structure

```
write-connect/
├── SKILL.md                        # Entry point - orchestrates all steps
├── README.md                       # This file
├── USER-CONFIG.example.md          # Config template: copy to USER-CONFIG.md (gitignored) and fill in
├── connect-form-reference.md       # Section names, character limits, form guidance
├── extraction-rules.md             # Activity test, impact categories, coverage mapping
├── log-parsing-rules.md            # File discovery and section parsing rules
├── section-1-results.md            # Generation rules for Section 1 (Results, 6,000 chars)
├── section-2-setbacks.md           # Generation rules for Section 2 (Setbacks, 1,000 chars)
├── section-3-goals.md              # Generation rules for Section 3 (Goals, 1,200 chars each)
├── section-4-behaviors.md          # Generation rules for Section 4 (Culture Behaviors, 1,000 chars)
├── references/
│   ├── goal-buckets.md             # Maps work types to Connect goal buckets
│   └── executive-language.md      # Translates output language to impact language
└── templates/
    ├── output-template.md          # Assembly format and gap analysis structure
    └── weekly-log-template.md      # Starting point for your weekly work logs
```
