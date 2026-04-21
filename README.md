# write-connect

Draft your Microsoft Connect performance review from weekly work logs — not from memory.

---

## What it does

`write-connect` reads your work logs for the review period, extracts completed work, and generates a full four-section Connect draft in one pass. It applies the What/How/Impact structure, maps work to your defined goal buckets, counts characters per section against form limits, and flags gaps before you submit. The output is paste-ready into the Connect form with no reformatting needed.

---

## Prerequisites

1. Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
2. Weekly work logs in a consistent folder and naming pattern (e.g., `Logs/YYYY-MM-DD Work.md`)
3. A copy of a past Connect review (used as style and structure reference)
4. A role summary or job description file (used for IC-level framing)
5. A goals file covering the review period

---

## Setup for Claude Code

1. Clone or copy this skill folder into your Claude skills directory:
   ```bash
   git clone https://github.com/your-org/write-connect ~/.claude/skills/write-connect
   ```
2. Register the skill by adding it to your `.claude/settings.json` skills path (or place it directly in `~/.claude/skills/`).
3. Fill in `USER-CONFIG.md` with your personal file paths and goal names (see [Configure it for yourself](#configure-it-for-yourself)).
4. Update `log-parsing-rules.md` if your log folder path or file naming pattern differs from the default.
5. Verify the skill is available: run `/skill-check write-connect` in a Claude Code session.

---

## Setup for VS Code + Copilot

1. Install the GitHub Copilot extension in VS Code.
2. Copy this skill folder into your workspace or a shared location your Copilot session can access.
3. Open `SKILL.md` and update the context file paths in Step 1 to match your local setup.
4. Open a Copilot Chat panel, attach `SKILL.md` as context (`@workspace /SKILL.md`), and invoke with your review period.
5. Copilot will walk through the steps; paste your work log contents when prompted if auto-discovery is not available.

---

## Configure it for yourself

Fill in `USER-CONFIG.md` before your first run. The table below shows what you need:

| Question | Where it goes |
|---|---|
| Where are your work logs stored? | `log_folder` in USER-CONFIG |
| What is your log file naming pattern? | `log_pattern` in USER-CONFIG |
| Where is your most recent Connect review? | `past_review_path` in USER-CONFIG |
| Where is your role summary or job description? | `role_summary_path` in USER-CONFIG |
| Where is your goals file? | `goals_path` in USER-CONFIG |
| What are your three goal bucket names? | `goal_1_title`, `goal_2_title`, `goal_3_title` in USER-CONFIG |
| Where should the draft be saved? | `output_path` in USER-CONFIG |

See `USER-CONFIG.md` for the full fill-in-the-blank template.

---

## Run it

1. Open a Claude Code session in your vault or project directory.
2. Type `/write-connect H2 FY26` (replace with your review period).
3. Answer the two setup questions (review period confirmation, any supplemental notes), then let the skill generate the full draft.

---

## File structure

```
write-connect/
├── SKILL.md                        # Entry point — orchestrates all steps
├── README.md                       # This file
├── USER-CONFIG.md                  # Your personal configuration (fill in before use)
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
    └── output-template.md          # Assembly format and gap analysis structure
```
