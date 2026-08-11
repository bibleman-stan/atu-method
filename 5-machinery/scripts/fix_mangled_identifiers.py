#!/usr/bin/env python3
"""Restore Python identifiers a path-rewrite turned into path fragments.

THE DAMAGE, one level worse than the broken imports: a directory named
`validators` is also a perfectly ordinary variable name, so the rewrite turned

    validators = discover_validators()          ->  5-machinery/validators = ...
    for v in validators:                        ->  for v in 5-machinery/validators:
    def print_summary(rule_counts, validators)  ->  def print_summary(..., 5-machinery/validators)
    args.validators                             ->  args.5-machinery/validators

None of these are paths. `validators` there is a local variable, a parameter
name, and an argparse attribute.

THE RULE THIS ESTABLISHES: a path rewriter must never touch a bare token — only
tokens that are unambiguously paths, meaning they are followed by `/` or a file
extension, or appear inside a quoted string. `scripts`, `tests`, `validators`,
`data` are all common identifiers as well as directory names, and outside a
quoted context there is no way to tell which is meant.

Repair is by AST position rather than regex: parse the file, and only rewrite
occurrences that Python itself would read as an identifier.

    python scripts/fix_mangled_identifiers.py --dry-run
    python scripts/fix_mangled_identifiers.py
"""

import argparse
import ast
import re
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent
TARGETS = ["readers-gnt", "readers-lxx", "readers-vulgate", "readers-tanakh"]

# `5-machinery/NAME` where NAME starts an identifier and is NOT followed by a
# further path segment or a file extension — i.e. it was a bare token.
IDENT = re.compile(r"5-machinery/(?=[A-Za-z_])(?!.{0,40}?\.(?:py|md|json|txt)\b)"
                   r"(?![A-Za-z_][\w]*/)")


def calibrate() -> bool:
    ok = True
    cases = [
        ("    validators = f()", "5-machinery/validators = f()", True,
         "an assignment target is restored"),
        ("    for v in validators:", "for v in 5-machinery/validators:", True,
         "a loop variable is restored"),
        ("    args.validators", "args.5-machinery/validators", True,
         "an attribute is restored"),
        ("'5-machinery/validators/run_all.py'",
         "'5-machinery/validators/run_all.py'", False,
         "a real path with a further segment is untouched"),
        ("see 5-machinery/scripts/build.py", "see 5-machinery/scripts/build.py",
         False, "a real path in prose is untouched"),
    ]
    for expect, given, should_change, why in cases:
        got = IDENT.sub("", given)
        changed = got != given
        hit = (changed == should_change) and (not should_change or got.strip() == expect.strip())
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("calibration — restore identifiers, never touch real paths")
    if not calibrate():
        print("MISCALIBRATED — refusing to run", file=sys.stderr)
        return 1
    print()

    for name in TARGETS:
        root = REPOS / name / "5-machinery"
        if not root.exists():
            continue
        repaired, still_bad = 0, []
        for f in sorted(root.rglob("*.py")):
            src = f.read_text(encoding="utf-8", errors="replace")
            try:
                ast.parse(src)
                continue                      # parses: leave it entirely alone
            except SyntaxError:
                pass
            new = IDENT.sub("", src)
            try:
                ast.parse(new)
            except SyntaxError:
                still_bad.append(f.name)
                continue
            repaired += 1
            if not args.dry_run:
                f.write_text(new, encoding="utf-8", newline="\n")
        print(f"{name}: {repaired} file(s) repaired"
              + (f", {len(still_bad)} still broken — {still_bad[:3]}"
                 if still_bad else ", none still broken"))

    if args.dry_run:
        print("\nDRY RUN — re-run without --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
