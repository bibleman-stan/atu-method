#!/usr/bin/env python3
# PROVENANCE: recovered 2026-08-06 from Claude Code file-history
# (b15d8d3f-13d4-4a90-bd66-6ad57e8b4350/f3b1940b03ed6ed6@v3, state 2026-05-22),
# then RETARGETED 2026-08-06 from its original reader-repo layout
# (private/01-method/, handoffs/, REPO_ROOT=parents[2]) to this hub. Original
# recovered text is in git history at commit 3920810.
"""
Detect broken pointers in atu-method canon, memories, scholarship, and CLAUDE.md.

Two failure classes, both of which have actually bitten this repo:

  1. BROKEN PATH — a cited file that does not exist. Origin: the 2026-04-27
     detritus audit found ~12 references to `10-colometry.md` after the
     methodology moved. Still live: `feedback_sense_line_mission.md` cites that
     same dead file today.

  2. BROKEN ANCHOR — a link destination `file.md#Heading` whose fragment matches
     no heading in the target. This class was created 2026-08-06 when
     scripts/link_canon_refs.py made section citations clickable: an anchor
     silently stops resolving the moment a heading is reworded, and a link that
     lands on the wrong section is worse than plain text. Also catches the
     phantom §-IDs the canon-xref arc tracks (e.g. glossary.md's framework.md
     §1.2 / §1.3, where live framework §1 has no sub-sections).

  3. BROKEN WIKILINK — an Obsidian [[target]] / [[target#Heading|alias]] whose
     basename resolves to no file, or to MORE than one. Added 2026-08-08 with
     scripts/add_wikilinks.py, and added in the SAME pass for a specific reason:
     link_canon_refs.py shipped a new link class with no validator and created
     the broken-anchor class above. A link syntax the checker cannot read is a
     link syntax that rots silently. Ambiguity counts as broken because Obsidian
     resolves a duplicate basename to whichever file it likes, and a link that
     lands on the wrong one of two files is worse than plain text.

This is the mechanical half of the CLAUDE.md audit tier. It exists because the
tool existing was never the problem — nothing ran it. Run it on the weekly audit
wake, and before/after any file move.

Exit code: 0 clean, 1 if anything is broken.

Usage:
    python scripts/check_broken_pointers.py
    python scripts/check_broken_pointers.py --verbose
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SCAN_GLOBS = [
    "CLAUDE.md",
    "README.md",
    "canon-index.md",
    "Pending-Decisions.md",
    "00-start-here.md",
    "1-method/*.md",
    "2-evidence/*.md",
    "3-implementation/*.md",
    "4-process/*.md",
    "memories/*.md",
    "2-evidence/scholarship/*.md",
    "2-evidence/scholarship/*/*.md",
]

# memories/operational/ is deliberately NOT path-linted. It is the recovered
# cross-repo archive (2026-08-06): its citations point at sibling reader repos,
# reader-repo scripts, and ~/.claude paths that this repo neither owns nor can
# resolve, so linting it reports noise rather than rot.

# _old/ is retired canon kept as a historical receipt; its internal pointers
# are frozen artifacts of the state they were archived in, so linting them would
# report rot that is intentional.
EXCLUDE_PARTS = {"_old", ".archive", "__pycache__"}

PATH_RE = re.compile(
    r"`((?:[\w./\\-]+/)*[\w.-]+\.(?:md|py|html|js|json|txt|sh|ipynb|cff|toml))`"
    r"|"
    r"\]\(<?((?:[\w./\\-]+/)*[\w.-]+\.(?:md|py|html|js|json|txt|sh|ipynb|cff|toml))"
    r"(?:#[^)>]*)?>?\)"
    r"|"
    r"(?<![\w`/.~-])((?:[\w-]+/)+[\w.-]+\.(?:md|py|html|js|json|txt|sh|ipynb))(?![\w/-])"
)

# Link destinations, for anchor checking: [text](dest) and [text](<dest>)
LINK_RE = re.compile(r"\]\((<[^>\n]*>|[^)\s\n]*)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Obsidian [[target]], [[target#Heading]], [[target|alias]], [[target#H|alias]]
WIKI_RE = re.compile(r"\[\[([^\]|#]+?)(?:#([^\]|]+?))?(?:\|[^\]]*?)?\]\]")

# Wikilink ambiguity must be judged the way OBSIDIAN judges it — over the whole
# vault, including _old/. Skipping _old/ here was a real bug: it made this
# checker report 0 broken wikilinks on a file Obsidian immediately flagged,
# because _old/ shadows 7 live basenames (framework.md, apparatus.md,
# architecture.md, glossary.md, retraction-log-protocol.md,
# toolset-architecture.md, _index.md). Validating against our own index instead
# of the resolver that actually runs is the same proxy-trust failure the repo
# keeps finding elsewhere. Only truly non-vault dirs are skipped.
INDEX_SKIP_PARTS = {".git", ".obsidian", "node_modules", "__pycache__"}

SKIP_PATHS = {
    "example.md", "tmp/file.py", "10-colometry.md",
    "transcript.md", "session-notes.md", "decisions.md", "pending.md",
    "Welcome.md",
}

SKIP_PREFIXES = (
    "C:/", "c:/", "/", "~",
    "readers-", "biblical-corpora/", "rev-reader/",   # sibling repos
    "atu-nlp-wiki/",                                  # the theory vault (work/, not repos/)
    "private/",                                       # gitignored per-repo substrate
    "handoffs/",                                      # reader-repo convention
    "archive/", ".archive/",
    "http://", "https://",
)

# Memory files are cited bare by filename across the canon; they live in
# memories/ or memories/operational/ and resolve() finds them there.
SEARCH_SUBDIRS = ["", "1-method", "2-evidence", "3-implementation", "4-process",
                  "memories", "memories/operational", "scripts",
                  "2-evidence/scholarship", "2-evidence/scholarship/bofm",
                  "2-evidence/scholarship/gnt", "2-evidence/scholarship/methodology",
                  "data", "atu_method", "tests"]


def slugify(h: str) -> str:
    return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", h.lower()).strip())


def build_vault_index():
    """basename -> [paths]. Wikilinks resolve by basename, so ambiguity matters."""
    import collections
    names = collections.defaultdict(list)
    for p in REPO_ROOT.rglob("*.md"):
        if set(p.relative_to(REPO_ROOT).parts) & INDEX_SKIP_PARTS:
            continue
        names[p.name].append(p)
    return names


def scan_paths() -> list:
    out = []
    for pattern in SCAN_GLOBS:
        for p in sorted(REPO_ROOT.glob(pattern)):
            if set(p.relative_to(REPO_ROOT).parts) & EXCLUDE_PARTS:
                continue
            if p.is_file():
                out.append(p)
    return out


def headings_of(path: Path) -> set:
    if not path.exists() or path.suffix != ".md":
        return set()
    hs = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = HEADING_RE.match(line)
        if m:
            hs.add(m.group(1))
            hs.add(slugify(m.group(1)))
    return hs


def is_skip(ref: str) -> bool:
    return ref in SKIP_PATHS or ref.startswith(SKIP_PREFIXES)


def resolve(ref: str, source: Path):
    rel = ref.replace("\\", "/")
    # Canon cites this repo's own files with the repo name attached
    # ("atu-method/3-implementation/substrate.md") as often as bare; both are correct.
    for prefix in ("repos/atu-method/", "atu-method/", "./"):
        if rel.startswith(prefix):
            rel = rel[len(prefix):]
    cand = (source.parent / rel).resolve()
    if cand.exists():
        return cand
    for sub in SEARCH_SUBDIRS:
        cand = (REPO_ROOT / sub / rel) if sub else (REPO_ROOT / rel)
        if cand.exists():
            return cand
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    files = scan_paths()
    broken_paths, broken_anchors, advisory, broken_wiki = [], [], [], []
    heading_cache = {}
    vault = build_vault_index()

    for path in files:
        in_fence = False
        for i, line in enumerate(path.read_text(encoding="utf-8",
                                                errors="replace").splitlines(), 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            for m in PATH_RE.finditer(line):
                ref = m.group(1) or m.group(2) or m.group(3)
                if not ref or is_skip(ref):
                    continue
                if resolve(ref, path) is None:
                    # Code files named in canon prose are overwhelmingly
                    # reader-repo scripts this hub cannot see; they are advisory,
                    # not failures, so the weekly signal stays actionable.
                    bucket = broken_paths if ref.endswith(".md") else advisory
                    bucket.append((path, i, ref, line.strip()[:110]))

            for m in WIKI_RE.finditer(line):
                tgt, frag = m.group(1).strip(), (m.group(2) or "").strip()
                # A bare slug with no "/" and no ".md" is a MEMORY-style soft
                # link. The memory spec makes those deliberately aspirational:
                # "a [[name]] that doesn't match an existing memory yet is fine;
                # it marks something worth writing later, not an error." So an
                # unresolved bare slug under memories/ is signal, not rot.
                # Anything naming a path or an extension is a file reference and
                # is always validated.
                is_file_ref = "/" in tgt or tgt.endswith(".md")
                in_memories = "memories" in path.relative_to(REPO_ROOT).parts
                base = tgt.split("/")[-1]
                if not base.endswith(".md"):
                    base += ".md"
                # A path-qualified target ("memories/operational/foo") is how
                # Obsidian disambiguates a duplicated basename, so resolve it as
                # a path FIRST — otherwise the only available fix for an
                # ambiguity would still report as ambiguous.
                if "/" in tgt:
                    rel = tgt if tgt.endswith(".md") else tgt + ".md"
                    exact = REPO_ROOT / rel
                    hits = [exact] if exact.exists() else []
                else:
                    hits = vault.get(base, [])
                if not hits:
                    if is_file_ref or not in_memories:
                        broken_wiki.append((path, i, m.group(0),
                                            "no such file in vault"))
                    continue
                if len(hits) > 1:
                    where = ", ".join(h.relative_to(REPO_ROOT).as_posix()
                                      for h in hits)
                    broken_wiki.append((path, i, m.group(0),
                                        f"ambiguous — {where}"))
                    continue
                if frag:
                    target = hits[0]
                    if target not in heading_cache:
                        heading_cache[target] = headings_of(target)
                    hs = heading_cache[target]
                    if hs and frag not in hs and slugify(frag) not in hs:
                        broken_wiki.append((path, i, m.group(0),
                                            "heading not found in target"))

            for m in LINK_RE.finditer(line):
                dest = m.group(1).strip("<>")
                if "#" not in dest or dest.startswith(("http", "mailto")):
                    continue
                fpart, _, frag = dest.partition("#")
                if not frag:
                    continue
                target = path if not fpart else resolve(fpart, path)
                if target is None:
                    continue  # already reported as a broken path
                if target not in heading_cache:
                    heading_cache[target] = headings_of(target)
                hs = heading_cache[target]
                if hs and frag not in hs and slugify(frag) not in hs:
                    broken_anchors.append((path, i, dest, line.strip()[:110]))

    print("=" * 72)
    print("atu-method pointer integrity")
    print("=" * 72)
    print(f"\nFiles scanned: {len(files)}")
    print(f"  broken doc paths: {len(broken_paths)}")
    print(f"  broken anchors:   {len(broken_anchors)}")
    print(f"  broken wikilinks: {len(broken_wiki)}")
    print(f"  advisory (non-.md, likely reader-repo): {len(advisory)}")

    if broken_wiki:
        print("\nBROKEN WIKILINKS")
        for path, line, ref, why in broken_wiki[:30]:
            print(f"  {path.relative_to(REPO_ROOT)}:{line}  {ref}")
            print(f"    {why}")
        if len(broken_wiki) > 30:
            print(f"  ... +{len(broken_wiki) - 30} more")

    for label, items in (("BROKEN DOC PATHS", broken_paths),
                         ("BROKEN ANCHORS", broken_anchors),
                         ("ADVISORY — unresolved non-.md references", advisory)):
        if not items:
            continue
        print(f"\n{label}")
        by_ref = {}
        for path, line, ref, ctx in items:
            by_ref.setdefault(ref, []).append((path, line, ctx))
        for ref, hits in sorted(by_ref.items(), key=lambda kv: -len(kv[1])):
            print(f"  {ref}  ({len(hits)}x)")
            for path, line, ctx in hits[:3 if not args.verbose else 99]:
                print(f"    {path.relative_to(REPO_ROOT)}:{line}")
                if args.verbose:
                    print(f"      {ctx}")
            if not args.verbose and len(hits) > 3:
                print(f"    ... +{len(hits) - 3} more")

    if broken_paths or broken_anchors or broken_wiki:
        print("\nFix the pointer, or add a genuinely-external ref to SKIP_PATHS /"
              " SKIP_PREFIXES.")
        return 1
    print("\nAll pointers and anchors resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
