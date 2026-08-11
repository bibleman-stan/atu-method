#!/usr/bin/env python3
"""Move `_find_repo_root` above its first use where the inserter put it below.

anchor_repo_root.py placed the helper after the last import found in the first
60 lines. In files whose root assignment sits ABOVE that point — common.py
assigns at line 35 — the definition landed after the call, giving
`NameError: name '_find_repo_root' is not defined` at import time.

Correct rule: a helper must be defined before its first use, so the anchor is
the first CALL, not the import block.

    python scripts/fix_helper_placement.py readers-gnt --dry-run
    python scripts/fix_helper_placement.py readers-gnt
"""

import argparse
import ast
import re
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent.parent

DEF_RE = re.compile(
    r"\n*def _find_repo_root\(\):.*?\n    return _here\.parent\n", re.S)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    target = REPOS / args.repo / "5-machinery"
    if not target.exists():
        print(f"{args.repo}: no 5-machinery/")
        return 0

    fixed, ok_already, broke = 0, 0, []
    for py in sorted(target.rglob("*.py")):
        src = py.read_text(encoding="utf-8", errors="replace")
        if "_find_repo_root()" not in src:
            continue
        m = DEF_RE.search(src)
        if not m:
            broke.append(f"{py.name} (calls it, never defines it)")
            continue
        first_call = src.find("_find_repo_root()")
        if first_call > m.start():
            ok_already += 1
            continue                      # definition already precedes use

        body = src[:m.start()] + src[m.end():]        # lift the definition out
        call = body.find("_find_repo_root()")
        line_start = body.rfind("\n", 0, call) + 1
        new = body[:line_start] + m.group(0).strip("\n") + "\n\n\n" + body[line_start:]
        try:
            ast.parse(new)
        except SyntaxError as e:
            broke.append(f"{py.name}:{e.lineno}")
            continue
        fixed += 1
        if not args.dry_run:
            py.write_text(new, encoding="utf-8", newline="\n")

    print(f"{args.repo}: {fixed} moved above first use, {ok_already} already correct"
          + (f", {len(broke)} unresolved — {broke[:3]}" if broke else ""))
    if args.dry_run:
        print("DRY RUN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
