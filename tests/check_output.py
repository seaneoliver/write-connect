#!/usr/bin/env python3
"""Check a write-connect test run against tests/expect.md.

Usage: check_output.py <case> <project-dir> <run-log> [--host HOST]

<project-dir> is the scratch project the run used. The draft is the one .md
file under <project-dir>/Drafts/. Exits non-zero and prints each failed check.
"""
import argparse
import re
import sys
from pathlib import Path

LIMITS = {"1": 6000, "2": 1000, "4": 1000}
GOAL_LIMIT = 1200
FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"

failures = []


def check(ok, message):
    if not ok:
        failures.append(message)


def form_count(text):
    text = text.strip("\n")
    return len(text) + text.count("\n")


def sections(draft):
    """Map section keys ('1', '2', 'goal1'.., '4', 'gap') to their body text."""
    out = {}
    key = None
    buf = []

    def flush():
        if key:
            body = [l for l in buf if not l.startswith("Character count:")]
            out[key] = "\n".join(body).strip("\n")

    for line in draft.splitlines():
        m = re.match(r"^## Section (\d)", line)
        g = re.match(r"^### Goal (\d)", line)
        if m or g or line.startswith("## Gap Analysis") or line.strip() == "---":
            flush()
            buf = []
            if m:
                key = m.group(1)
            elif g:
                key = "goal" + g.group(1)
            elif line.startswith("## Gap Analysis"):
                key = "gap"
            else:
                key = None
            continue
        if key:
            buf.append(line)
    flush()
    # Section 3 goals end at the next goal header; the section 3 header itself has no body.
    out.pop("3", None)
    return out


def allowed_numbers():
    nums = set()
    for p in FIXTURES.rglob("*.md"):
        nums.update(re.findall(r"\d+", p.read_text()))
    return nums


def unsupported_numbers(text, allowed):
    text = re.sub(r"\d{4}-\d{2}-\d{2}", " ", text)  # dates
    text = re.sub(r"Goal #?\d", " ", text)            # goal labels
    return sorted({n for n in re.findall(r"\d+", text) if n not in allowed})


def main():
    parser = argparse.ArgumentParser(description="Check a write-connect test run.")
    parser.add_argument("case")
    parser.add_argument("project")
    parser.add_argument("runlog")
    parser.add_argument("--host")
    args = parser.parse_args()
    case, project, runlog, host = args.case, args.project, args.runlog, args.host
    project = Path(project)
    log = Path(runlog).read_text(errors="replace") if Path(runlog).exists() else ""
    drafts = sorted((project / "Drafts").glob("*.md"))

    if host:
        named = f"hosts/{host}.md"
        in_draft = any(named in d.read_text() for d in drafts)
        check(named in log or in_draft, f"neither the run log nor the draft names {named}")

    if case in ("missing-goals", "zero-evidence"):
        check(not drafts, f"{case}: expected no draft, found {[d.name for d in drafts]}")
        if case == "missing-goals":
            check("missing-GOALS.md" in log, "missing-goals: run log does not name missing-GOALS.md")
        return

    check(len(drafts) == 1, f"expected exactly one draft in Drafts/, found {len(drafts)}")
    if len(drafts) != 1:
        return
    draft = drafts[0].read_text()
    sec = sections(draft)

    for key, limit in LIMITS.items():
        check(key in sec, f"Section {key} missing")
        if key in sec:
            n = form_count(sec[key])
            check(n <= limit, f"Section {key} is {n} form characters, limit {limit}")
    goals = [k for k in sec if k.startswith("goal")]
    for k in goals:
        n = form_count(sec[k])
        check(n <= GOAL_LIMIT, f"{k} is {n} form characters, limit {GOAL_LIMIT}")

    allowed = allowed_numbers()
    for key in ("1", "2"):
        bad = unsupported_numbers(sec.get(key, ""), allowed)
        check(not bad, f"Section {key} has numbers not in any fixture: {bad}")

    gap = sec.get("gap", "")
    if case in ("normal", "four-goal"):
        form_text = "\n".join(v for k, v in sec.items() if k != "gap")
        for name in ("Heron", "Kestrel"):
            check(name not in form_text, f"out-of-period item leaked into the form sections: {name}")
        src = next((l for l in draft.splitlines() if l.startswith("Source logs:")), "")
        used = re.split(r"[Ee]xclud", src)[0]
        check("2026-09-14" not in used, "out-of-period log 2026-09-14 listed as a source")
        check("Osprey" in sec.get("1", ""), "boundary-week in-period item (Osprey) missing from Section 1")
        check("Wren" in sec.get("1", ""), "alternate-heading week (Wren) missing from Section 1")
        check("2026-10-19" in gap, "thin week 2026-10-19 not flagged in gap analysis")
        check("2026-10-26" in gap, "missing week 2026-10-26 not flagged in gap analysis")
    if case == "normal":
        check(len(goals) == 3, f"expected 3 goals in Section 3, found {len(goals)}")
    if case == "four-goal":
        check(len(goals) == 4, f"expected 4 goals in Section 3, found {len(goals)}")
        check(re.search(r"Goal #?4", sec.get("1", "")) is not None, "fourth goal bucket missing from Section 1")
    if case == "paste":
        check("Curlew" in sec.get("1", ""), "pasted item (Curlew) missing from Section 1")
        check(re.search(r"past(e|ed)", gap, re.I) is not None, "gap analysis does not say the input was pasted")


if __name__ == "__main__":
    main()
    for f in failures:
        print("FAIL:", f)
    print("PASS" if not failures else f"{len(failures)} check(s) failed")
    sys.exit(1 if failures else 0)
