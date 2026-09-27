# Manual test: Claude Cowork

Cowork has no headless runner and loads skills from your claude.ai account, so this test is run by hand.

1. Make a test folder with `fixtures/Logs`, `fixtures/GOALS.md`, `fixtures/Role-Summary.md` and an empty `Drafts/` folder.
2. Copy the skill to a folder named `write-connect`, without `tests/`, `fixtures/` or `.git/`. Put `fixtures/config/normal.md` in it as `USER-CONFIG.md` and add `host: "cowork"`. Paths in the config are relative to the test folder.
3. Zip the `write-connect` folder and upload it in the Claude app's skill settings. Remove any older write-connect upload first.
4. Start a Cowork session, connect the test folder, and ask: "Draft my Connect review for 2026-10-01 to 2026-11-13." Answer the setup questions: no role changes, no supplemental notes. Tell it to save.
5. Copy the session's first message into `run.log` in the test folder (it should say "Using hosts/cowork.md").
6. Check: `python3 tests/check_output.py normal <test-folder> <test-folder>/run.log --host cowork`.
7. Repeat with the `paste` case (`fixtures/config/paste.md`, paste `fixtures/paste-notes.md` when offered).
8. Record where relative paths resolved (connected folder root or elsewhere) in `tests/expect.md` under Host notes, and the result in the README table.
