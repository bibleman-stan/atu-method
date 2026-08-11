#!/usr/bin/env python3
"""Repair repo-root resolution in scripts moved one directory deeper.

THE REGRESSION THIS FIXES, stated plainly: moving `scripts/` to
`5-machinery/scripts/` silently broke every script that finds the repo root with
`Path(__file__).resolve().parent.parent`. That expression walked
`scripts/x.py -> scripts -> repo`; from one level deeper it now walks
`5-machinery/scripts/x.py -> 5-machinery/scripts -> 5-machinery` and stops
inside the machinery folder.

Nothing caught it. The rewrite verifier passed — no path STRING was wrong. The
smoke test passed — `--help` only parses arguments and never touches the
filesystem. It surfaced only when readers-gnt's pre-commit hook actually ran a
script that reads the corpus, and by then the same breakage had been pushed to
readers-lxx and readers-vulgate.

The lesson is about the smoke test, not the rewrite: `--help` proves a file
imports, not that it can find its data. A move that changes DEPTH needs a check
that resolves a real path.

    python scripts/fix_script_depth.py --dry-run
    python scripts/fix_script_depth.py
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent
TARGETS = ["readers-gnt", "readers-lxx", "readers-vulgate"]

# Only files that moved exactly one level deeper get one more `.parent`.
MOVED_UNDER = "5-machinery"
OLD = "Path(__file__).resolve().parent.parent"
NEW = "Path(__file__).resolve().parent.parent.parent"


def calibrate() -> bool:
    """A move that changes depth must be detected; one that does not must not be."""
    ok = True
    cases = [
        ("REPO = Path(__file__).resolve().parent.parent", 1,
         "the two-level walk is rewritten"),
        ("REPO = Path(__file__).resolve().parent.parent.parent", 0,
         "an already-correct three-level walk is left alone"),
        ("HERE = Path(__file__).resolve().parent", 0,
         "a one-level walk is not depth-sensitive here"),
    ]
    for body, expect, why in cases:
        # count only exact two-level walks not already followed by .parent
        got = len(re.findall(re.escape(OLD) + r"(?!\.parent)", body))
        hit = got == expect
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why} — found {got}, expected {expect}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("calibration — rewrite two-level walks, leave correct ones alone")
    if not calibrate():
        print("MISCALIBRATED — refusing to run", file=sys.stderr)
        return 1
    print()

    pat = re.compile(re.escape(OLD) + r"(?!\.parent)")
    for name in TARGETS:
        root = REPOS / name / MOVED_UNDER
        if not root.exists():
            print(f"{name}: no {MOVED_UNDER}/ — skipped")
            continue
        touched = 0
        for f in sorted(root.rglob("*.py")):
            body = f.read_text(encoding="utf-8", errors="replace")
            new = pat.sub(NEW, body)
            if new == body:
                continue
            touched += 1
            if not args.dry_run:
                f.write_text(new, encoding="utf-8", newline="\n")
        print(f"{name}: {touched} file(s) {'would be ' if args.dry_run else ''}fixed")

    if args.dry_run:
        print("\nDRY RUN — re-run without --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
