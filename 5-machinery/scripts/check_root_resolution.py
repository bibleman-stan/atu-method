#!/usr/bin/env python3
"""Verify — and optionally fix — that every moved script still resolves the repo root.

THE CLASS OF BUG THIS EXISTS FOR. Moving a directory deeper silently breaks any
file that finds the repo root by walking `__file__` upward:

    scripts/x.py          Path(__file__).resolve().parent.parent      -> repo
    5-machinery/scripts/x.py   same expression                        -> 5-machinery

Nothing textual is wrong, so a path-rewrite verifier passes. `--help` passes
because argparse never touches the filesystem. It surfaces only when something
reads real data — in readers-gnt, a pre-commit hook, after the same breakage had
already been pushed to two other repos.

A first fix added one `.parent` to two-level walks and missed the three-level
walks used by files nested one deeper (`validators/syntax/check_r2.py`). Guessing
a uniform depth is the same mistake twice, so this computes the REQUIRED depth
from each file's own position and compares it to what the file actually does.

    python scripts/check_root_resolution.py readers-gnt
    python scripts/check_root_resolution.py readers-gnt --fix
"""

import argparse
import re
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent.parent

# THERE IS MORE THAN ONE WAY TO WALK UP, and a checker that knows only one is
# blind. The first version matched only the pathlib idiom and reported
# readers-gnt clean while its validators were still resolving `research/` inside
# 5-machinery/ — because _shared/macula_clauses.py uses the os.path idiom:
#
#     _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#     _REPO_ROOT  = os.path.dirname(os.path.dirname(_SCRIPT_DIR))
#
# Both are matched now. A third idiom (parents[N], os.pardir joins) would be a
# third blind spot; the check reports what it examined so the gap is visible.
ROOT_ASSIGN = re.compile(
    r"^(?P<indent>\s*)(?P<name>_?(?:REPO_ROOT|REPO|ROOT|PROJECT_ROOT))\s*=\s*"
    r"Path\(__file__\)\.resolve\(\)(?P<walk>(?:\.parent)+)\s*$", re.M)

# os.path.dirname(...) nesting around a *_DIR seeded from __file__.
DIRNAME_ASSIGN = re.compile(
    r"^(?P<indent>\s*)(?P<name>_?(?:REPO_ROOT|REPO|ROOT|PROJECT_ROOT))\s*=\s*"
    r"(?P<walk>(?:os\.path\.dirname\()+)(?P<seed>_?\w*(?:SCRIPT_DIR|HERE|THIS_DIR))"
    r"(?P<close>\)+)\s*$", re.M)


def required_depth(py: Path, root: Path) -> int:
    """How many .parent hops from this file to the repo root."""
    return len(py.resolve().relative_to(root.resolve()).parts) - 1 + 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    root = REPOS / args.repo
    if not (root / "5-machinery").exists():
        print(f"{args.repo}: no 5-machinery/ — nothing moved")
        return 0

    wrong, checked, fixed = [], 0, 0
    for py in sorted((root / "5-machinery").rglob("*.py")):
        src = py.read_text(encoding="utf-8", errors="replace")
        changed = False
        rel = py.relative_to(root).as_posix()
        need = required_depth(py, root)

        for m in ROOT_ASSIGN.finditer(src):
            checked += 1
            have = m.group("walk").count(".parent")
            if have == need:
                continue
            wrong.append((rel, m.group("name"), have, need))
            if args.fix:
                src = src.replace(m.group(0),
                                  f"{m.group('indent')}{m.group('name')} = "
                                  f"Path(__file__).resolve()" + ".parent" * need)
                changed = True

        # The os.path idiom seeds from a *_DIR that is already one level up
        # (dirname of __file__), so it needs one FEWER dirname than the pathlib
        # walk needs .parent hops.
        for m in DIRNAME_ASSIGN.finditer(src):
            checked += 1
            have = m.group("walk").count("os.path.dirname(")
            want = need - 1
            if have == want:
                continue
            wrong.append((rel, m.group("name"), have, want))
            if args.fix:
                src = src.replace(
                    m.group(0),
                    f"{m.group('indent')}{m.group('name')} = "
                    + "os.path.dirname(" * want + m.group("seed") + ")" * want)
                changed = True
        if changed:
            py.write_text(src, encoding="utf-8", newline="\n")
            fixed += 1

    print(f"{args.repo}: {checked} root-resolution(s) checked")
    if not wrong:
        print("  all resolve to the repo root")
        return 0
    for rel, name, have, need in wrong[:10]:
        print(f"  {rel}: {name} walks {have}, needs {need}")
    if len(wrong) > 10:
        print(f"  ... +{len(wrong) - 10} more")
    if args.fix:
        print(f"  FIXED in {fixed} file(s)")
        return 0
    print("  re-run with --fix")
    return 1


if __name__ == "__main__":
    sys.exit(main())
