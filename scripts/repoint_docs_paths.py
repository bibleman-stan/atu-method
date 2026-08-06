#!/usr/bin/env python3
"""Rewrite PROSE path references after the docs/ restructure.

restructure_docs.py fixed markdown link destinations. This fixes the other half:
paths named in prose, backticks, tables, and code comments — `docs/01-normative/framework.md`,
`atu-method/docs/01-normative/framework.md`, `../../docs/01-normative/framework.md`. Any path ending in
`docs/<name>.md` gains its tier; `_index.md` becomes `00-start-here.md`.

Runs over this repo AND the sibling reader repos, which cite atu-method canon by
path (measured 2026-08-06: 7 files in readers-bofm, 12 in readers-gnt, others
unmeasured). Per the atomic-ship doctrine the cascade is one operation.

    python scripts/repoint_docs_paths.py                 # dry run, this repo
    python scripts/repoint_docs_paths.py --apply --all-repos
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIBLINGS = ["readers-bofm", "readers-gnt", "readers-tanakh", "readers-lxx",
            "readers-vulgate", "readers-gnt-morph", "rev-reader"]

TIERS = {
    "framework.md": "01-normative", "cross-corpus-principles.md": "01-normative",
    "glossary.md": "01-normative",
    "binding-rules-hebrew.md": "02-registries", "binding-rules-lxx.md": "02-registries",
    "toolset-architecture.md": "03-implementation", "architecture.md": "03-implementation",
    "substrate.md": "03-implementation", "apparatus.md": "03-implementation",
    "retraction-log-protocol.md": "04-process", "improvement-loops.md": "04-process",
    "deployment-status.md": "05-status", "methodology-position.md": "05-status",
}

SKIP_PARTS = {"_old", ".archive", "_archive", ".git", "__pycache__",
              "node_modules", "private", "data", "_attachments"}
EXTS = {".md", ".py", ".json", ".txt", ".cff", ".toml"}

# `docs/` NOT already followed by a tier dir, then a known basename.
PATTERN = re.compile(
    r"(docs/)(?!0[1-5]-|00-)(" + "|".join(re.escape(k) for k in TIERS) + r")")
INDEX_PATTERN = re.compile(r"(docs/)_index\.md")


def rewrite(text: str) -> tuple:
    text, n1 = PATTERN.subn(lambda m: m.group(1) + TIERS[m.group(2)] + "/" + m.group(2),
                            text)
    text, n2 = INDEX_PATTERN.subn(r"\g<1>00-start-here.md", text)
    return text, n1 + n2


def walk(root: Path):
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix not in EXTS:
            continue
        if set(p.relative_to(root).parts) & SKIP_PARTS:
            continue
        yield p


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--all-repos", action="store_true")
    args = ap.parse_args()

    roots = [REPO]
    if args.all_repos:
        roots += [REPO.parent / s for s in SIBLINGS if (REPO.parent / s).exists()]

    grand = 0
    for root in roots:
        touched, total = {}, 0
        for p in walk(root):
            try:
                text = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            new, n = rewrite(text)
            if n:
                touched[p.relative_to(root).as_posix()] = n
                total += n
                if args.apply:
                    p.write_text(new, encoding="utf-8", newline="\n")
        grand += total
        print(f"\n{root.name}: {total} references in {len(touched)} files")
        for f, n in sorted(touched.items(), key=lambda kv: -kv[1])[:10]:
            print(f"   {f:56} {n}")
    print(f"\nTOTAL: {grand}" + ("" if args.apply else "   (DRY RUN — use --apply)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
