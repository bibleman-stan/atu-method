#!/usr/bin/env python3
"""Normalize the private/ ignore rule to one pattern across every reader repo.

Two patterns existed for one intent:

    readers-tanakh, readers-bofm     private/
    readers-lxx, readers-vulgate     /private/*
                                     !/private/README.md

The second publishes a file whose entire content is "this folder is private" —
the one thing from the private folder that is public, which is self-defeating and
was the source of a false leak finding during the 2026-08-09 audit. The README's
one piece of durable information (substrate lives in ~/repos/biblical-corpora/)
moves into the .gitignore comment, where anyone reading the rule will see it.

Result: every reader repo carries the same three lines, nothing under private/ is
tracked anywhere, and `loop_health.check_private_tracked` has no exceptions to
reason about.

    python 5-machinery/scripts/normalize_private_ignore.py --dry-run
    python 5-machinery/scripts/normalize_private_ignore.py
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent
TARGETS = ["readers-lxx", "readers-vulgate"]

OLD = """# This repo is PUBLIC. Private/working material goes in /private/ (never published).
/private/*
!/private/README.md"""

NEW = """# This repo is PUBLIC. Private/working material goes in private/ — never
# published, never tracked. Substrate data lives in ~/repos/biblical-corpora/
# (also unpublished); private/ here is repo-local working material only.
private/"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for name in TARGETS:
        root = REPOS / name
        gi = root / ".gitignore"
        readme = root / "private" / "README.md"
        print(f"\n{name}")

        text = gi.read_text(encoding="utf-8")
        if OLD not in text:
            print("  SKIP — .gitignore does not match the expected old block")
            continue
        print("  .gitignore: /private/* + negation  ->  private/")
        print(f"  untrack + delete: private/README.md ({readme.stat().st_size}b)"
              if readme.exists() else "  private/README.md already absent")
        if args.dry_run:
            continue

        gi.write_text(text.replace(OLD, NEW), encoding="utf-8", newline="\n")
        if readme.exists():
            subprocess.run(["git", "rm", "-q", "--cached", "private/README.md"],
                           cwd=root, check=False)
            readme.unlink()
        # Prove it: nothing under private/ tracked, and the dir is now ignored.
        left = subprocess.run(["git", "ls-files", "private"], cwd=root,
                              capture_output=True, text=True).stdout.strip()
        print(f"  tracked under private/ now: {len(left.splitlines()) if left else 0}")

    if args.dry_run:
        print("\nDRY RUN — re-run without --dry-run")
    return 0


if __name__ == "__main__":
    sys.exit(main())
