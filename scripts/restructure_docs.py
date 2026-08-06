#!/usr/bin/env python3
"""One-shot: move docs/ into the numbered hierarchy and repair every link.

The move is the easy half. The hard half is that docs/ links were written flat
(`[text](framework.md)`), so every one of them breaks the moment a file lands in
a subfolder. This script does both in one pass and is therefore the only safe way
to perform the move:

  1. `git mv` each doc to its tier (history preserved).
  2. Rewrite EVERY markdown link destination in the repo — docs, memories,
     scholarship, root — to the correct relative path for the new layout,
     preserving any `#anchor` fragment.

Deliberately NOT moved: canon-index.md stays at repo root. It is a top-level
index whose 119 `file:line` receipts are written relative to the root; relocating
it would invalidate their context for no navigation gain. docs/_old/ is retired
canon and stays frozen.

Run with no args for a dry run. --apply to execute.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"

LAYOUT = {
    "01-normative": ["framework.md", "cross-corpus-principles.md", "glossary.md"],
    "02-registries": ["binding-rules-hebrew.md", "binding-rules-lxx.md"],
    "03-implementation": ["toolset-architecture.md", "architecture.md",
                          "substrate.md", "apparatus.md"],
    "04-process": ["retraction-log-protocol.md", "improvement-loops.md"],
    "05-status": ["deployment-status.md", "methodology-position.md"],
}
# _index.md becomes the orientation doc at docs/ root, renamed so it sorts first
RENAMES = {"_index.md": "00-start-here.md"}

LINK_RE = re.compile(r"(?<!\!)\[([^\]\n]*)\]\((<[^>\n]*>|[^)\s\n]*)\)")
SCAN_GLOBS = ["*.md", "docs/*.md", "docs/*/*.md", "memories/*.md",
              "memories/operational/*.md", "scholarship/*.md", "scholarship/*/*.md"]
SKIP_DIRS = {"_old", ".archive", "__pycache__"}


def build_destination_map() -> dict:
    """basename -> new path relative to REPO."""
    out = {}
    for tier, names in LAYOUT.items():
        for n in names:
            out[n] = f"docs/{tier}/{n}"
    for old, new in RENAMES.items():
        out[old] = f"docs/{new}"
    return out


def files_to_scan() -> list:
    seen = []
    for g in SCAN_GLOBS:
        for p in REPO.glob(g):
            if set(p.relative_to(REPO).parts) & SKIP_DIRS:
                continue
            if p.is_file() and p not in seen:
                seen.append(p)
    return seen


def new_location(path: Path, dest_map: dict) -> Path:
    """Where a file lives AFTER the move."""
    rel = path.relative_to(REPO).as_posix()
    if rel.startswith("docs/") and "/" not in rel[5:]:
        name = rel[5:]
        if name in dest_map:
            return REPO / dest_map[name]
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    dest_map = build_destination_map()

    # --- 1. the moves -------------------------------------------------------
    moves = []
    for tier, names in LAYOUT.items():
        for n in names:
            src = DOCS / n
            if src.exists():
                moves.append((src, DOCS / tier / n))
    for old, new in RENAMES.items():
        if (DOCS / old).exists():
            moves.append((DOCS / old, DOCS / new))

    print(f"MOVES ({len(moves)}):")
    for s, d in moves:
        print(f"  {s.relative_to(REPO).as_posix()} -> {d.relative_to(REPO).as_posix()}")

    if args.apply:
        for tier in LAYOUT:
            (DOCS / tier).mkdir(exist_ok=True)
        for s, d in moves:
            subprocess.run(["git", "mv", str(s.relative_to(REPO)),
                            str(d.relative_to(REPO))], cwd=REPO, check=True)

    # --- 2. link repair -----------------------------------------------------
    # Done AFTER the move so paths resolve against the real new tree.
    scanned = files_to_scan() if args.apply else [
        p for p in files_to_scan()]
    rewritten, touched = 0, {}

    for path in scanned:
        src_after = new_location(path, dest_map) if not args.apply else path
        text = path.read_text(encoding="utf-8")
        out, changed = [], 0
        pos = 0
        for m in LINK_RE.finditer(text):
            dest = m.group(2)
            bare = dest.strip("<>")
            if bare.startswith(("http", "mailto", "#")) or not bare:
                continue
            fpart, sep, frag = bare.partition("#")
            name = os.path.basename(fpart)
            if name not in dest_map:
                continue
            target_after = REPO / dest_map[name]
            newrel = os.path.relpath(target_after, src_after.parent).replace(os.sep, "/")
            newdest = newrel + sep + frag
            wrapped = f"<{newdest}>" if (dest.startswith("<") or " " in newdest) \
                else newdest
            if wrapped == dest:
                continue
            out.append(text[pos:m.start(2)])
            out.append(wrapped)
            pos = m.end(2)
            changed += 1
        if changed:
            out.append(text[pos:])
            rewritten += changed
            touched[path.relative_to(REPO).as_posix()] = changed
            if args.apply:
                path.write_text("".join(out), encoding="utf-8", newline="\n")

    print(f"\nLINK DESTINATIONS REWRITTEN: {rewritten} across {len(touched)} files")
    for f, n in sorted(touched.items(), key=lambda kv: -kv[1])[:15]:
        print(f"  {f:52} {n}")
    if not args.apply:
        print("\nDRY RUN — re-run with --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
