# Manual test: Copilot in VS Code agent mode

Copilot's VS Code agent mode has no headless runner, so this test is run by hand. Use the same fixtures and checks as the headless hosts.

1. Build a test project: `sh tests/run-host.sh copilot normal` creates one and runs Copilot CLI. Or copy what it does by hand: make an empty folder, copy `fixtures/Logs`, `fixtures/GOALS.md` and `fixtures/Role-Summary.md` into it, make an empty `Drafts/`, and copy the skill to `.github/skills/write-connect/` without `tests/` and `fixtures/`.
2. Put `fixtures/config/normal.md` in the skill folder as `USER-CONFIG.md` and add `host: "copilot"`.
3. Open the project folder in VS Code. In Copilot Chat, switch to Agent mode.
4. Send: `/write-connect 2026-10-01 to 2026-11-13`. Answer the setup questions: no role changes, no supplemental notes. When asked, tell it to save.
5. Save the chat's first message to `run.log` in the project folder (it should say "Using hosts/copilot.md").
6. Check: `python3 tests/check_output.py normal <project-folder> <project-folder>/run.log --host copilot`.
7. Repeat with the `paste` case: use `fixtures/config/paste.md`, and paste `fixtures/paste-notes.md` when the skill offers the paste path.
8. Record the date, OS, VS Code and Copilot versions, and the result in the README table.
