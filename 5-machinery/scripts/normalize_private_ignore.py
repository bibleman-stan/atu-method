#!/usr/bin/env python3
"""Normalize each repo's `private/` ignore so a README stub can be tracked.

WHY THIS EXISTS. A bare `private/` line ignores the directory itself, and git
will not descend into an ignored directory to honour a later negation. So
`!private/README.md` under a bare `private/` does nothing at all -- the stub
stays untracked and the folder's purpose vanishes with the machine.

The working form ignores the CONTENTS and then re-admits one file:

    /private/*
    !/private/README.md

readers-gnt already had this and still had zero tracked files under private/,
because the `git add` that was meant to stage the stub hit a fatal pathspec and
the commit reported success anyway. Hence: this script rewrites, and a separate
--verify pass asks git what is actually tracked rather than trusting exit codes.

    python normalize_private_ignore.py --calibrate
    python normalize_private_ignore.py            # rewrite
    python normalize_private_ignore.py --verify   # what git actually tracks
"""

import argparse
import pathlib
import subprocess
import sys

REPOS = pathlib.Path(__file__).resolve().parent.parent.parent.parent

TARGETS = ["readers-tanakh", "readers-bofm", "readers-lxx",
           "readers-vulgate", "rev-reader", "readers-gnt-morph"]

NEW = ("# Private material stays local. The README stub is the exception and IS\n"
       "# tracked, so the folder's purpose and layout survive even though its\n"
       "# contents cannot. A bare `private/` cannot be negated into -- git will not\n"
       "# descend into an ignored directory -- so the contents are ignored instead.\n"
       "/private/*\n"
       "!/private/README.md\n")


def rewrite(text: str) -> tuple[str, bool]:
    """Replace the first bare `private/` line. Returns (text, changed)."""
    out, done = [], False
    for ln in text.splitlines(keepends=True):
        if ln.strip() == "private/" and not done:
            out.append(NEW)
            done = True
        else:
            out.append(ln)
    return "".join(out), done


def calibrate() -> bool:
    """Poles on the rewrite itself. The known-bad cases matter more than the
    known-good one: rewriting a line that only LOOKS like the target would
    silently change what a repo publishes."""
    ok = True
    cases = [
        ("x\nprivate/\ny\n", True, "bare private/ is rewritten"),
        ("x\n/private/*\n!/private/README.md\n", False,
         "already-correct form is left alone (idempotent)"),
        ("x\nnot-private/\n", False, "suffix match is NOT rewritten"),
        ("x\nprivate/substrate/\n", False, "deeper path is NOT rewritten"),
        ("x\n#private/\n", False, "commented line is NOT rewritten"),
        ("private/\nprivate/\n", True, "only the first occurrence changes"),
    ]
    for text, want, why in cases:
        _, changed = rewrite(text)
        hit = changed == want
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}")
    # the multi-occurrence case also needs its count checked
    result, _ = rewrite("private/\nprivate/\n")
    hit = result.count("/private/*") == 1 and result.count("\nprivate/") == 1
    ok &= hit
    print(f"  [{'PASS' if hit else 'FAIL'}] second occurrence survives untouched")
    return ok


def verify() -> int:
    """Ask git what is tracked. Not what a command's exit code claimed."""
    bad = 0
    for r in TARGETS + ["readers-gnt"]:
        repo = REPOS / r
        if not (repo / ".git").exists():
            continue
        tracked = subprocess.run(
            ["git", "-C", str(repo), "ls-files", "--cached", "private"],
            capture_output=True, text=True).stdout.split()
        on_disk = (repo / "private" / "README.md").exists()
        readme = [t for t in tracked if t.endswith("private/README.md")]
        leak = [t for t in tracked if t not in readme]
        status = "ok"
        if leak:
            status = f"LEAK: {len(leak)} non-README file(s) tracked"
            bad += 1
        elif on_disk and not readme:
            status = "stub on disk but NOT tracked"
            bad += 1
        elif not on_disk:
            status = "no README stub on disk"
        print(f"    {r:18} {status}")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration -- the rewrite must be exact and idempotent")
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED")
        return 0 if ok else 1

    if args.verify:
        return 1 if verify() else 0

    if not calibrate():
        print("MISCALIBRATED -- refusing to rewrite", file=sys.stderr)
        return 1
    print()
    for r in TARGETS:
        p = REPOS / r / ".gitignore"
        if not p.exists():
            print(f"    {r:18} no .gitignore")
            continue
        text, changed = rewrite(p.read_text(encoding="utf-8"))
        if changed:
            p.write_text(text, encoding="utf-8")
        print(f"    {r:18} {'rewritten' if changed else 'no bare private/ line'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
