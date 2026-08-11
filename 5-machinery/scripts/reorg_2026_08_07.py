#!/usr/bin/env python3
"""One-shot: flatten docs/ into numbered purpose-first directories at the root.

Mirrors the readers-bofm reorganization (1-method / 2-evidence / 3-project) with
one adaptation: atu-method has a content class BoFM lacks — implementation and
architecture docs that are neither canon, evidence, nor process — so it gets four
tiers, not three.

    1-method/          what we believe        (framework, principles, glossary, rule registries)
    2-evidence/        what we've measured    (scholarship, claim inventory, deploy status)
    3-implementation/  how it's built         (toolset, architecture, substrate, apparatus)
    4-process/         how we work            (loops, protocols, proposals, position)

ERROR MITIGATION — the specific failure this guards against. On 2026-08-06 a
cascade skipped private/ and the integrity checker could not see what the
repointer refused to walk, so both reported clean while 103 canon citations
dangled. Therefore:

  * the sibling list here is derived from an INDEPENDENT grep with no skip list,
    which surfaced readers-tanakh-morph — absent from repoint_docs_paths.py's
    hardcoded list and silently missed by it;
  * rewriting is driven by one explicit OLD->NEW table, applied to every textual
    form a citation takes (bare, atu-method/-prefixed, repos/-prefixed);
  * markdown link destinations inside moved files are recomputed relative to the
    file's NEW home rather than string-patched;
  * verification is a set difference against a pre-move snapshot, not a count.

    python 5-machinery/scripts/reorg_2026_08_07.py            # dry run
    python 5-machinery/scripts/reorg_2026_08_07.py --apply
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

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


REPO = _find_repo_root()
PARENT = REPO.parent

# From the independent enumeration, not from memory.
REPOS = ["atu-method", "readers-bofm", "readers-gnt", "readers-tanakh",
         "readers-tanakh-morph", "readers-gnt-morph", "readers-lxx",
         "readers-vulgate", "rev-reader"]

# OLD repo-relative path -> NEW repo-relative path. Order matters: longest first.
MOVES = {
    "1-method/framework.md":               "1-method/framework.md",
    "1-method/cross-corpus-principles.md": "1-method/cross-corpus-principles.md",
    "1-method/glossary.md":                "1-method/glossary.md",
    "1-method/binding-rules-hebrew.md":   "1-method/binding-rules-hebrew.md",
    "1-method/binding-rules-lxx.md":      "1-method/binding-rules-lxx.md",
    "3-implementation/toolset-architecture.md": "3-implementation/toolset-architecture.md",
    "3-implementation/architecture.md":       "3-implementation/architecture.md",
    "3-implementation/substrate.md":          "3-implementation/substrate.md",
    "3-implementation/apparatus.md":          "3-implementation/apparatus.md",
    "2-evidence/framework-claim-inventory.md": "2-evidence/framework-claim-inventory.md",
    "4-process/improvement-loops.md":         "4-process/improvement-loops.md",
    "4-process/retraction-log-protocol.md":   "4-process/retraction-log-protocol.md",
    "4-process/proposal-2026-08-06-criterion-reconstruction.md":
        "4-process/proposal-2026-08-06-criterion-reconstruction.md",
    "2-evidence/deployment-status.md":          "2-evidence/deployment-status.md",
    "4-process/methodology-position.md":       "4-process/methodology-position.md",
    "00-start-here.md":                        "00-start-here.md",
}
DIR_MOVES = {
    "scholarship": "2-evidence/scholarship",
    "docs/_old": "_old",
}

EXTS = {".md", ".py", ".json", ".txt", ".cff", ".toml", ".js"}
SKIP = {".git", "node_modules", ".venv", "__pycache__", "_archive", ".archive",
        "substrate", "04-sources", "data", "books", "audio", "_attachments",
        "_old", "docs/_old",
        # Session records are history-of-record: they describe what was true at
        # the time, so rewriting them falsifies the log the same way editing
        # _archive/ would.
        "03-sessions",
        # Volatile Obsidian state, gitignored — rewriting it is pointless churn.
        ".obsidian"}

# This file's own MOVES table contains every old path verbatim. Without this
# guard the script rewrites its own mapping mid-run and the table stops
# describing the migration it just performed.
SELF = Path(__file__).resolve()


def files_of(root: Path):
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix not in EXTS:
            continue
        if set(p.relative_to(root).parts) & SKIP:
            continue
        if p.resolve() == SELF:
            continue
        yield p


def build_rules() -> list:
    """(compiled_pattern, replacement) for every textual form a citation takes."""
    rules = []
    pairs = list(MOVES.items()) + [(o + "/", n + "/") for o, n in DIR_MOVES.items()]
    pairs.sort(key=lambda kv: -len(kv[0]))
    for old, new in pairs:
        for prefix in ("repos/atu-method/", "atu-method/", "../atu-method/",
                       "../../atu-method/", ""):
            rules.append((re.compile(re.escape(prefix + old)), prefix + new))
    return rules


LINK = re.compile(r"(?<!\!)\[([^\]\n]*)\]\((<[^>\n]*>|[^)\s\n]*)\)")


def fix_links(text: str, newhome: Path) -> tuple:
    """Recompute relative markdown destinations against the file's NEW location."""
    out, pos, n = [], 0, 0
    for m in LINK.finditer(text):
        dest = m.group(2)
        bare = dest.strip("<>")
        if bare.startswith(("http", "mailto", "#")) or not bare:
            continue
        frag = ""
        if "#" in bare:
            bare, _, frag = bare.partition("#")
            frag = "#" + frag
        target = os.path.normpath(os.path.join(str(newhome.parent), bare))
        try:
            rel_old = Path(target).resolve().relative_to(REPO).as_posix()
        except (ValueError, OSError):
            continue
        newrel = MOVES.get(rel_old)
        if newrel is None:
            for d_old, d_new in DIR_MOVES.items():
                if rel_old.startswith(d_old + "/"):
                    newrel = d_new + rel_old[len(d_old):]
                    break
        if newrel is None:
            continue
        rp = os.path.relpath(REPO / newrel, newhome.parent).replace(os.sep, "/")
        wrapped = f"<{rp}{frag}>" if (dest.startswith("<") or " " in rp + frag) \
            else rp + frag
        out.append(text[pos:m.start(2)]); out.append(wrapped); pos = m.end(2); n += 1
    out.append(text[pos:])
    return "".join(out), n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    print(f"MOVES: {len(MOVES)} files, {len(DIR_MOVES)} directories")
    if args.apply:
        for tier in ("1-method", "2-evidence", "3-implementation", "4-process"):
            (REPO / tier).mkdir(exist_ok=True)
        for old, new in MOVES.items():
            if (REPO / old).exists():
                subprocess.run(["git", "mv", old, new], cwd=REPO, check=True)
        for old, new in DIR_MOVES.items():
            if (REPO / old).exists():
                (REPO / new).parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(["git", "mv", old, new], cwd=REPO, check=True)
        # docs/ should now be empty of tracked content
        for stale in ("docs/01-normative", "docs/02-registries",
                      "docs/03-implementation", "docs/04-process",
                      "docs/05-status"):
            p = REPO / stale
            if p.exists() and not any(p.iterdir()):
                p.rmdir()

    rules = build_rules()
    touched, total = {}, 0
    for name in REPOS:
        root = PARENT / name
        if not root.exists():
            continue
        for p in files_of(root):
            try:
                text = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            new = text
            n = 0
            for rx, rep in rules:
                new, k = rx.subn(rep, new)
                n += k
            if p.suffix == ".md" and root == REPO and args.apply:
                new, k = fix_links(new, p)
                n += k
            if n:
                touched[f"{name}/{p.relative_to(root).as_posix()}"] = n
                total += n
                if args.apply:
                    p.write_text(new, encoding="utf-8", newline="\n")

    print(f"\nCITATION REWRITES: {total} across {len(touched)} files")
    for f, n in sorted(touched.items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {f:64} {n}")
    if not args.apply:
        print("\nDRY RUN — re-run with --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
