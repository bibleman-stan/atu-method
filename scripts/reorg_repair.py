#!/usr/bin/env python3
"""Repair pass for the 2026-08-07 reorg, driven by the verification set-diff.

The first pass rewrote citations that named the old paths with a `docs/` prefix,
and missed two classes that the set-difference against the pre-move baseline
exposed. Recorded because both are generic traps:

1. RELATIVE FORMS. Docs inside docs/ cited each other as `../01-normative/x.md`
   or bare `01-normative/x.md`. The rules keyed on `docs/01-normative/...`, so
   none of those matched. Every intra-tree link was invisible to a rule table
   written from the outside.

2. SEQUENTIAL DOUBLE-APPLICATION. Rules ran one after another, so
   `atu-method/scholarship/` -> `atu-method/2-evidence/scholarship/` was then
   re-matched by the bare `scholarship/` rule, yielding
   `atu-method/2-evidence/2-evidence/scholarship/`. The fix is a single pass
   over one combined alternation, longest-first, so no output is ever re-read
   as input.

    python scripts/reorg_repair.py            # dry run
    python scripts/reorg_repair.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PARENT = REPO.parent
REPOS = ["atu-method", "readers-bofm", "readers-gnt", "readers-tanakh",
         "readers-tanakh-morph", "readers-gnt-morph", "readers-lxx",
         "readers-vulgate", "rev-reader"]

TIER = {
    "01-normative/framework.md":               "1-method/framework.md",
    "01-normative/cross-corpus-principles.md": "1-method/cross-corpus-principles.md",
    "01-normative/glossary.md":                "1-method/glossary.md",
    "02-registries/binding-rules-hebrew.md":   "1-method/binding-rules-hebrew.md",
    "02-registries/binding-rules-lxx.md":      "1-method/binding-rules-lxx.md",
    "03-implementation/toolset-architecture.md": "3-implementation/toolset-architecture.md",
    "03-implementation/architecture.md":       "3-implementation/architecture.md",
    "03-implementation/substrate.md":          "3-implementation/substrate.md",
    "03-implementation/apparatus.md":          "3-implementation/apparatus.md",
    "04-process/framework-claim-inventory.md": "2-evidence/framework-claim-inventory.md",
    "04-process/improvement-loops.md":         "4-process/improvement-loops.md",
    "04-process/retraction-log-protocol.md":   "4-process/retraction-log-protocol.md",
    "04-process/proposal-2026-08-06-criterion-reconstruction.md":
        "4-process/proposal-2026-08-06-criterion-reconstruction.md",
    "05-status/deployment-status.md":          "2-evidence/deployment-status.md",
    "05-status/methodology-position.md":       "4-process/methodology-position.md",
    "00-start-here.md":                        "00-start-here.md",
}

EXTS = {".md", ".py", ".json", ".txt", ".cff", ".toml", ".js"}
SKIP = {".git", "node_modules", ".venv", "__pycache__", "_archive", ".archive",
        "substrate", "04-sources", "data", "books", "audio", "_attachments",
        "_old", "03-sessions", ".obsidian"}
SELF = Path(__file__).resolve()


def build_pattern():
    """One alternation, longest key first, so a single pass cannot re-match."""
    pairs = []
    for old, new in TIER.items():
        for lead in ("docs/", "../", "../../", "./", ""):
            pairs.append((lead + old, (lead if lead in ("../", "../../", "./")
                                       else "") + new))
    # scholarship/ -> 2-evidence/scholarship/, but never when already correct
    pairs.append(("scholarship/", "2-evidence/scholarship/"))
    # and undo the double-prefix the sequential pass produced
    pairs.append(("2-evidence/2-evidence/", "2-evidence/"))
    pairs.sort(key=lambda kv: -len(kv[0]))
    table = dict(pairs)
    rx = re.compile("(?<!2-evidence/)(" +
                    "|".join(re.escape(k) for k in table) + ")")
    return rx, table


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    rx, table = build_pattern()

    touched, total = {}, 0
    for name in REPOS:
        root = PARENT / name
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if not p.is_file() or p.suffix not in EXTS:
                continue
            if set(p.relative_to(root).parts) & SKIP or p.resolve() == SELF:
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            new, n = rx.subn(lambda m: table[m.group(1)], text)
            if n:
                touched[f"{name}/{p.relative_to(root).as_posix()}"] = n
                total += n
                if args.apply:
                    p.write_text(new, encoding="utf-8", newline="\n")

    print(f"REPAIRS: {total} across {len(touched)} files")
    for f, n in sorted(touched.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {f:60} {n}")
    if not args.apply:
        print("\nDRY RUN — re-run with --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
