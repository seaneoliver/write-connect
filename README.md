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

## Where it runs

write-connect is one skill folder that several AI tools can load. Each tool gets a short file in `hosts/` that tells the skill which of its tools to use.

| Host | Status | Last test | Invocation | Notes |
|---|---|---|---|---|
| Claude Code 2.1.283 | Supported | 2026-09-27, macOS 26.6.2 | explicit | All 5 test cases pass |
| GitHub Copilot CLI 1.0.88 | Supported | 2026-09-27, macOS 26.6.2 | explicit and automatic | All 5 test cases pass. About 50 Copilot AI credits per run |
| OpenAI Codex CLI 0.153.1 | Experimental | 2026-09-27, macOS 26.6.2 | explicit | 3 of 5 cases pass. The four-goal and paste runs stopped at the ChatGPT usage limit before saving |
| GitHub Copilot in VS Code (agent mode) | Experimental | not yet run | | Manual guide: `tests/copilot-vscode-manual.md` |
| Claude Cowork | Experimental | not yet run | | Manual guide: `tests/cowork-manual.md` |

A host is **Supported** only after it passes the full test set in `tests/` on the date shown. Anything else is **Experimental**: it may work, but nobody has proven it yet. Tests so far ran on macOS only. Windows is untested. Headless test runs can't exercise the interactive questions or the refine step.

---

## Prerequisites

1. One of the hosts above, installed and signed in.
2. Python 3, available as `python3`. The skill uses it to count characters exactly the way the Connect form does.
3. Weekly work logs, one Markdown file per week, in one folder, with the date in each filename (e.g., `Logs/2026-09-21 Work.md`). **They need the headings the skill reads**: `## Completed`, `## What I'm Working on`, and `## Questions/Risks/Blockers`. Start from [`templates/weekly-log-template.md`](templates/weekly-log-template.md). No logs? The skill can draft from pasted notes instead (see [Run it](#run-it)).
4. A role summary or job description file. Required: the skill stops without it.
5. A goals file covering the review period. Required: the skill stops without it.
6. Optional: a past Connect review (used as a style and structure reference). If this is your first Connect, skip it.

---

## Install

Every host uses the same two steps after installing: copy `USER-CONFIG.example.md` to `USER-CONFIG.md` in the skill folder, then fill it in, including `host` (see [Configure it for yourself](#configure-it-for-yourself)). Your `USER-CONFIG.md` is gitignored, so `git pull` updates never touch it.

**Claude Code**
```bash
git clone https://github.com/seaneoliver/write-connect ~/.claude/skills/write-connect
```
Start a new session and type `/skills`. You should see `write-connect`. Leave `host` blank or set it to `claude-code`.

**GitHub Copilot (CLI or VS Code agent mode)**
```bash
git clone https://github.com/seaneoliver/write-connect ~/.copilot/skills/write-connect
```
Or put it in a project at `.github/skills/write-connect`. Set `host: "copilot"`.

**OpenAI Codex**
```bash
git clone https://github.com/seaneoliver/write-connect ~/.agents/skills/write-connect
```
Or put it in a project at `.agents/skills/write-connect`. Set `host: "codex"`.

**Claude Cowork**

Cowork loads skills from your claude.ai account, not from a folder on disk. Fill in `USER-CONFIG.md` first, with `host: "cowork"` and paths relative to the folder you'll connect to Cowork. Then zip the `write-connect` folder and upload it in the Claude app under your skill settings. To change your config later, edit it and upload the zip again.

---

## Configure it for yourself

Fill in `USER-CONFIG.md` (copied from `USER-CONFIG.example.md`) before your first run. Paths are relative to your working folder, not the skill folder. Your host file in `hosts/` says which folder that is. The table below shows what you need:

| Question | Where it goes |
|---|---|
| Which AI tool runs the skill? | `host` in USER-CONFIG (`claude-code`, `copilot`, `codex` or `cowork`; blank means `claude-code`) |
| Where are your work logs stored? | `log_folder` in USER-CONFIG |
| What is your log file naming pattern? Use `*` as the wildcard, e.g. `* Work.md` | `log_pattern` in USER-CONFIG |
| Where is your most recent Connect review? (optional) | `past_review_path` in USER-CONFIG |
| Where is your role summary or job description? (required) | `role_summary_path` in USER-CONFIG |
| Where is your goals file? (required) | `goals_path` in USER-CONFIG |
| Do you have a voice or style guide? (optional) | `voice_notes_path` in USER-CONFIG |
| What are your goal bucket names? | `goal_1_title` to `goal_3_title` (plus optional `goal_4_title`) in USER-CONFIG |
| What is the compliance goal wording on your form? | `compliance_goal_text` in USER-CONFIG |
| Any recurring feedback from your manager this cycle? (optional) | `manager_feedback_themes` in USER-CONFIG |
| Where should the draft be saved? | `output_path` in USER-CONFIG |

See `USER-CONFIG.example.md` for the full fill-in-the-blank template.

---

## Run it

1. Open your host in your notes or project folder.
2. Invoke the skill with your review period: `/write-connect H2 FY26` in Claude Code or Copilot, `$write-connect H2 FY26` in Codex. In Cowork, ask for your Connect review draft for the period.
3. Answer the setup questions (any org or role changes since last cycle, and any supplemental notes). The skill drafts all four sections.
4. Refine any section, then tell it to save. Expect a permission prompt the first time it runs Python to count characters.

**No weekly logs?** If no log files match, the skill offers to draft from notes you paste instead. The draft will be thinner, and its gap analysis says it came from pasted notes. Pasted notes go to whichever AI tool you are running, so paste only what your company allows you to share with it.

**Accuracy.** The skill only uses facts and numbers that appear in your logs or notes. Where a number would help and you didn't write one down, the draft shows `[number from your log]` and the gap analysis asks you for it. Every section is at or under its Connect character limit before the draft is saved.

---

## Testing

`tests/` holds a fictional fixture set and a headless runner:

```bash
sh tests/check-host-neutral.sh              # shared files name no host-specific tool
sh tests/run-host.sh claude-code normal     # hosts: claude-code, codex, copilot
```

Cases: `normal`, `four-goal`, `paste`, `missing-goals`, `zero-evidence`. What each case must produce is in `tests/expect.md`. Manual guides for Copilot in VS Code and Cowork are in `tests/`.

---

## File structure

```
write-connect/
├── SKILL.md                        # Entry point - orchestrates all steps
├── README.md                       # This file
├── USER-CONFIG.example.md          # Config template: copy to USER-CONFIG.md (gitignored) and fill in
├── hosts/                          # One file per AI tool: capabilities and tool names
├── agents/openai.yaml              # Codex display metadata
├── connect-form-reference.md       # Section names, character limits, form guidance
├── extraction-rules.md             # Traceability gate, activity test, impact categories, coverage mapping
├── log-parsing-rules.md            # File discovery, boundary weeks, section parsing, pasted notes
├── section-1-results.md            # Generation rules for Section 1 (Results, 6,000 chars)
├── section-2-setbacks.md           # Generation rules for Section 2 (Setbacks, 1,000 chars)
├── section-3-goals.md              # Generation rules for Section 3 (Goals, 1,200 chars each)
├── section-4-behaviors.md          # Generation rules for Section 4 (Culture Behaviors, 1,000 chars)
├── references/
│   ├── goal-buckets.md             # Maps work types to Connect goal buckets
│   └── executive-language.md       # Translates output language to impact language
├── templates/
│   ├── output-template.md          # Assembly format and gap analysis structure
│   └── weekly-log-template.md      # Starting point for your weekly work logs
├── fixtures/                       # Fictional test inputs
└── tests/                          # Checks, runner and manual test guides
```
