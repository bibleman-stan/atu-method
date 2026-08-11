#!/usr/bin/env python3
"""Replace counted directory walks with a marker-anchored repo-root lookup.

WHY THIS EXISTS, and it is the real lesson of the 2026-08-10 reorg.

Moving `scripts/` and `validators/` one level deeper broke every file that found
the repo root by COUNTING directories upward. Each fix caught one idiom and
missed the next:

    Path(__file__).resolve().parent.parent            pathlib walk
    os.path.dirname(os.path.dirname(_SCRIPT_DIR))     os.path chain, one name
    os.path.dirname(_VALIDATORS_DIR)                  os.path chain, another name

Three rounds of patching, three misses, because a pattern-matcher over idiom
NAMES can never be exhaustive. The defect is not the idioms — it is that
counting hops encodes the file's depth in the tree, so any move invalidates it
silently. Nothing textual is wrong afterwards, so no rewrite-verifier can catch
it, and `--help` cannot either because argparse never touches the filesystem.

THE FIX: anchor on a marker instead of counting. Walking up until `.git` is
found is depth-independent, so the next reorg cannot break it.

    def _repo_root() -> Path:
        p = Path(__file__).resolve()
        for parent in p.parents:
            if (parent / ".git").exists():
                return parent
        return p.parent

Idempotent: files already anchored are skipped.

    python scripts/anchor_repo_root.py readers-gnt --dry-run
    python scripts/anchor_repo_root.py readers-gnt
"""

import argparse
import ast
import re
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent.parent

HELPER_PATHLIB = '''

def _find_repo_root():
    """Repo root by MARKER, not by counting parents.

    Counting encodes this file's depth in the tree, so moving the file silently
    breaks it and no text-based check notices. Anchoring on .git survives any
    move. Added 2026-08-10 after a reorg broke three different counted idioms.
    """
    from pathlib import Path as _P
    _here = _P(__file__).resolve()
    for _p in _here.parents:
        if (_p / ".git").exists():
            return _p
    return _here.parent

'''

# Any assignment whose right side is a counted walk from __file__, however
# spelled, and whatever the variable is called.
COUNTED = re.compile(
    r"^(?P<indent>[ \t]*)(?P<name>_?[A-Z][A-Z0-9_]*)\s*=\s*"
    r"(?:"
    r"Path\(__file__\)\.resolve\(\)(?:\.parent)+"
    r"|(?:os\.path\.dirname\()+\s*_?[A-Z][A-Z0-9_]*\s*\)+"
    r"|(?:os\.path\.dirname\()+os\.path\.abspath\(__file__\)\)+"
    r")\s*$", re.M)

ROOTISH = re.compile(r"_?(?:REPO_ROOT|REPO|ROOT|PROJECT_ROOT)$")


def calibrate() -> bool:
    ok = True
    cases = [
        ("REPO_ROOT = Path(__file__).resolve().parent.parent", True,
         "pathlib counted walk is detected"),
        ("_REPO_ROOT = os.path.dirname(os.path.dirname(_SCRIPT_DIR))", True,
         "os.path chain is detected whatever the seed is called"),
        ("_REPO_ROOT = os.path.dirname(_VALIDATORS_DIR)", True,
         "the name that broke round three is detected"),
        ("HERE = Path(__file__).resolve().parent", False,
         "a one-hop 'directory of this file' is NOT a repo-root walk"),
        ("DATA = os.path.join(REPO_ROOT, 'data')", False,
         "a join is not a walk"),
    ]
    for body, should_match, why in cases:
        m = COUNTED.search(body)
        hit_root = bool(m) and bool(ROOTISH.search(m.group("name")))
        hit = hit_root == should_match
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("calibration — detect counted repo-root walks in any spelling")
    if not calibrate():
        print("MISCALIBRATED — refusing to run", file=sys.stderr)
        return 1
    print()

    root = REPOS / args.repo
    target = root / "5-machinery"
    if not target.exists():
        print(f"{args.repo}: no 5-machinery/")
        return 0

    changed, skipped, broke = 0, 0, []
    for py in sorted(target.rglob("*.py")):
        src = py.read_text(encoding="utf-8", errors="replace")
        hits = [m for m in COUNTED.finditer(src) if ROOTISH.search(m.group("name"))]
        if not hits:
            skipped += 1
            continue
        new = src
        for m in hits:
            new = new.replace(
                m.group(0),
                f"{m.group('indent')}{m.group('name')} = _find_repo_root()")
        if "_find_repo_root" not in src:
            # insert the helper after the import block
            lines = new.split("\n")
            idx = 0
            for i, ln in enumerate(lines[:60]):
                if ln.startswith(("import ", "from ")):
                    idx = i + 1
            new = "\n".join(lines[:idx]) + HELPER_PATHLIB + "\n".join(lines[idx:])
        try:
            ast.parse(new)
        except SyntaxError as e:
            broke.append(f"{py.name}:{e.lineno}")
            continue
        changed += 1
        if not args.dry_run:
            py.write_text(new, encoding="utf-8", newline="\n")

    print(f"{args.repo}: {changed} file(s) anchored, {skipped} untouched"
          + (f", {len(broke)} would break — {broke[:3]}" if broke else ""))
    if args.dry_run:
        print("DRY RUN — re-run without --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
