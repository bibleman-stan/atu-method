#!/usr/bin/env python3
"""Undo path-rewrites that landed inside Python import statements.

THE DAMAGE: a directory rename rewrote `validators` -> `5-machinery/validators`
everywhere it appeared, including in

    from validators.common import ...
    import validators.syntax

producing `from 5-machinery/validators.common import ...`, which is a
SyntaxError. 21 files in readers-gnt stopped compiling.

WHY IT HAPPENED: a module name and a directory name are the same token, and a
path rewriter cannot tell them apart from the outside. `validators` in
`from validators.common import x` is a MODULE PATH resolved through sys.path —
it does not change when the directory moves, provided sys.path points at the new
parent. Rewriting it is always wrong.

THE GENERAL RULE, worth more than this fix: never rewrite inside an import
statement. Imports are resolved by the interpreter, not the filesystem, and the
correct response to a moved package is to fix sys.path or the package's install
location — never the import line.

    python scripts/fix_broken_imports.py --dry-run
    python scripts/fix_broken_imports.py
"""

import argparse
import ast
import re
import subprocess
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent
TARGETS = ["readers-gnt", "readers-lxx", "readers-vulgate", "readers-tanakh"]

# `from 5-machinery/pkg...` / `import 5-machinery/pkg...` -> strip the prefix.
BROKEN = re.compile(r"^(\s*(?:from|import)\s+)5-machinery/", re.M)


def calibrate() -> bool:
    ok = True
    cases = [
        ("from 5-machinery/validators.common import x",
         "from validators.common import x", "broken import is repaired"),
        ("import 5-machinery/validators.syntax",
         "import validators.syntax", "plain import is repaired"),
        ("path = '5-machinery/validators/common.py'",
         "path = '5-machinery/validators/common.py'",
         "a genuine PATH string is left alone"),
        ("# see 5-machinery/scripts for details",
         "# see 5-machinery/scripts for details",
         "prose mentioning the path is left alone"),
    ]
    for body, expect, why in cases:
        got = BROKEN.sub(r"\1", body)
        hit = got == expect
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("calibration — repair imports, never touch real path strings")
    if not calibrate():
        print("MISCALIBRATED — refusing to run", file=sys.stderr)
        return 1
    print()

    for name in TARGETS:
        root = REPOS / name / "5-machinery"
        if not root.exists():
            continue
        fixed = 0
        for f in sorted(root.rglob("*.py")):
            body = f.read_text(encoding="utf-8", errors="replace")
            new = BROKEN.sub(r"\1", body)
            if new == body:
                continue
            fixed += 1
            if not args.dry_run:
                f.write_text(new, encoding="utf-8", newline="\n")
        # Also repair prose examples inside markdown, which mislead a reader.
        for f in sorted(root.rglob("*.md")):
            body = f.read_text(encoding="utf-8", errors="replace")
            new = BROKEN.sub(r"\1", body)
            if new != body and not args.dry_run:
                f.write_text(new, encoding="utf-8", newline="\n")

        # PROVE it: every .py must compile. This is the check that `--help`
        # could never be, because a SyntaxError is not reachable by argparse.
        # ast.parse rather than py_compile: it needs no output file, so it
        # cannot hit the Windows temp-file permission error py_compile does,
        # and a SyntaxError is exactly what we are checking for.
        bad = []
        if not args.dry_run:
            for f in sorted(root.rglob("*.py")):
                try:
                    ast.parse(f.read_text(encoding="utf-8", errors="replace"),
                              filename=str(f))
                except SyntaxError:
                    bad.append(f.name)
        print(f"{name}: {fixed} import(s) repaired, "
              f"{len(bad)} file(s) still failing to compile"
              + (f" — {bad[:4]}" if bad else ""))

    if args.dry_run:
        print("\nDRY RUN — re-run without --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
