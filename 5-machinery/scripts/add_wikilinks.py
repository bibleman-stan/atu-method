#!/usr/bin/env python3
"""Turn unlinked doc mentions into Obsidian [[wikilinks]] so the vault is navigable.

The gap this closes: canon prose is full of mentions like ``substrate.md`` §1 or
``framework.md`` §2.1 that read as citations but are dead text in Obsidian. You
cannot click them. link_canon_refs.py already handled the citations that were
written as markdown links; this handles the ones that were never links at all.

Three rules make it safe to run over the whole vault:

  1. NEVER INVENT A TARGET. A mention is linked only if its basename resolves to
     exactly one file in the vault. The 5 ambiguous basenames (README.md,
     SKILL.md, _index.md, and the two feedback_* files duplicated between
     memories/ and memories/operational/) are skipped, because a wikilink that
     silently resolves to the wrong one of two files is worse than plain text.

  2. NEVER TOUCH AN EXISTING LINK. Markdown links and existing wikilinks are
     masked out before matching and restored after, so this is idempotent and
     cannot produce [[[[nested]]]] or eat a link's display text.

  3. PRESERVE THE PROSE VERBATIM. `substrate.md` §1 becomes
     [[substrate.md#1. The mechanical ceiling...|substrate.md §1]] — the alias
     carries the original text, so reading is unchanged and only clicking is
     added. This is the same discipline link_canon_refs.py follows.

Section resolution handles both heading dialects in this repo: framework.md
writes "§2.1 The bidirectional test", substrate.md writes "1. The mechanical
ceiling". If no heading matches the §-id, the file still gets linked and the
§-id stays as plain text — a partial win, never a broken anchor.

    python 5-machinery/scripts/add_wikilinks.py            # dry run, shows every change
    python 5-machinery/scripts/add_wikilinks.py --apply
"""

import argparse
import collections
import re
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
# Where prose lives. memories/operational/ is deliberately excluded for the same
# reason check_broken_pointers.py excludes it: it is the recovered cross-repo
# archive and its mentions point at sibling repos this vault cannot resolve.
TARGET_GLOBS = [
    "*.md",
    "1-method/*.md",
    "2-evidence/*.md",
    "2-evidence/scholarship/*.md",
    "2-evidence/scholarship/*/*.md",
    "3-implementation/*.md",
    "4-process/*.md",
    "memories/*.md",
]

INDEX_SKIP = {"_old", ".archive", "__pycache__", ".git", ".obsidian",
              "node_modules", ".claude"}

# Retired docs are named in retirement notices ON PURPOSE ("replaced by ...").
# Linking them would imply they are live; they are not in the vault at all.
NEVER_LINK = {"change-protocol.md", "canon-validator-alignment-protocol.md",
              "editorial-review-protocol.md", "rule-template.md",
              "rule-equivalence-map.md", "structural-licenses.md"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
# Two citation dialects, both live in this repo:
#   A  `framework.md §1.2`   — file and § inside one tick pair (83 occurrences)
#   B  `framework.md` §1.2   — ticks close before the § (52 occurrences)
# Bare unticked "framework.md §1.2" is deliberately NOT matched: hyphenated
# basenames make the left boundary unreliable (cross-corpus-principles.md
# matches starting at "corpus-"), and most bare mentions name reader-repo files
# that are not in this vault at all.
TICKED_RE = re.compile(
    r"`([\w.-]+\.md)(\s*§\s*\d+(?:\.\d+[a-z]?)*)?`(\s*§\s*\d+(?:\.\d+[a-z]?)*)?")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")


def build_index():
    """basename -> live path, plus the set of names that need path-qualifying.

    Two different questions, and conflating them was a real bug. A file under
    _old/ is never a LINK TARGET, but Obsidian still indexes it, so [[framework.md]]
    is ambiguous to the resolver even though only one framework.md is live. The
    first pass skipped _old/ when building the index and emitted 7 shadowed
    names — framework.md, apparatus.md, architecture.md, glossary.md,
    retraction-log-protocol.md, toolset-architecture.md, _index.md — that
    Obsidian flagged as ambiguous the moment the file was written.

    So: targets come from the live tree; ambiguity is judged against the WHOLE
    vault, and a shadowed name is emitted path-qualified ([[1-method/framework.md
    |framework.md]]) rather than short.
    """
    live, everything = collections.defaultdict(list), collections.Counter()
    for p in REPO.rglob("*.md"):
        if set(p.relative_to(REPO).parts) & {".git", "node_modules", ".obsidian"}:
            continue
        everything[p.name] += 1
        if not set(p.relative_to(REPO).parts) & INDEX_SKIP:
            live[p.name].append(p)

    index, ambiguous, shadowed = {}, set(), set()
    for name, paths in live.items():
        if len(paths) != 1:
            ambiguous.add(name)          # two LIVE files — unresolvable, skip
            continue
        index[name] = paths[0]
        if everything[name] > 1:
            shadowed.add(name)           # live is unique, but _old/ shadows it
    return index, ambiguous, shadowed


def link_target(name, index, shadowed):
    """Always vault-relative path.

    Bare basenames were the first design and they were wrong twice over. Obsidian
    resolves [[framework.md]] ambiguously because _old/ shadows 7 live names, and
    the editor's markdown linter flags EVERY bare target as an ambiguous
    identifier — correctly, since a basename is not a unique resource id and a
    name that is unique today stops being unique the moment a second file is
    added. The alias carries the original prose, so path-qualifying costs only
    source verbosity and buys permanent resolvability.
    """
    return index[name].relative_to(REPO).as_posix()


def headings_of(path: Path):
    out = []
    in_fence = False
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.append(m.group(1))
    return out


def find_heading(headings, sec: str):
    """Map a §-id to a heading, across both dialects used in this repo."""
    sec = sec.strip()
    for h in headings:
        stripped = h.lstrip("#").strip()
        # "§2.1 The bidirectional test"
        if stripped.startswith(f"§{sec}") and (
                len(stripped) == len(sec) + 1 or not stripped[len(sec) + 1].isdigit()):
            return h
        # "1. The mechanical ceiling" / "1a. Past-ceiling levers"
        if stripped.startswith(f"{sec}.") or stripped.startswith(f"{sec} "):
            return h
    return None


def mask_existing(text):
    """Hide existing links so they can never be re-matched. Returns (masked, restore)."""
    stash = []

    def keep(m):
        stash.append(m.group(0))
        return f"\x00{len(stash) - 1}\x00"

    # order matters: wikilinks first, then markdown links
    masked = re.sub(r"\[\[[^\]]*\]\]", keep, text)
    masked = re.sub(r"\[[^\]]*\]\([^)]*\)", keep, masked)
    return masked, stash


def unmask(text, stash):
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def requalify(line, index, shadowed):
    """Rewrite already-written [[shadowed]] links into path-qualified form.

    Needed because mask_existing() protects existing wikilinks from the main
    pass, so links emitted before the shadowing bug was found would never be
    revisited by a re-run.
    """
    def fix(m):
        tgt, frag, alias = m.group(1), m.group(2), m.group(3)
        if "/" in tgt or tgt not in index:
            return m.group(0)
        newtgt = index[tgt].relative_to(REPO).as_posix()
        if newtgt == tgt:                 # a root-level file is already exact
            return m.group(0)
        out = f"[[{newtgt}"
        if frag:
            out += f"#{frag}"
        out += f"|{alias if alias is not None else tgt}]]"
        return out

    return re.sub(r"\[\[([^\]|#]+?)(?:#([^\]|]+?))?(?:\|([^\]]*?))?\]\]", fix, line)


def process(path: Path, index, ambiguous, heading_cache, shadowed):
    original = path.read_text(encoding="utf-8", errors="replace")
    out_lines, changes, phantoms = [], [], []
    in_fence = False

    for lineno, line in enumerate(original.splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        # NEVER rewrite inside a heading. Headings are anchor TARGETS: every
        # [[doc#Heading]] and [](file.md#Heading) elsewhere must match the
        # heading text exactly, so putting link markup in one makes every
        # inbound anchor depend on that markup surviving verbatim. Caught
        # 2026-08-08 after the first pass rewrote 7 headings, two of which
        # (cross-corpus-principles §1.4 / §1.5) are cited anchors.
        if HEADING_RE.match(line):
            out_lines.append(line)
            continue

        line_in = line
        line = requalify(line, index, shadowed)
        masked, stash = mask_existing(line)

        def repl(m):
            name = m.group(1)
            inside, outside = m.group(2), m.group(3)   # dialect A vs dialect B
            sec = inside or outside
            if name in NEVER_LINK or name in ambiguous or name not in index:
                return m.group(0)
            target = index[name]
            if target == path:          # never self-link
                return m.group(0)
            link = link_target(name, index, shadowed)
            # Preserve the prose exactly as written, ticks aside.
            display = name + (sec if sec else "")
            if sec:
                secid = sec.replace("§", "").strip()
                if target not in heading_cache:
                    heading_cache[target] = headings_of(target)
                h = find_heading(heading_cache[target], secid)
                if h:
                    return f"[[{link}#{h}|{display}]]"
                # A §-id with no matching heading is a phantom anchor. Link the
                # file so the citation is still navigable, and report it — this
                # is the same class canon-index.md tracks.
                phantoms.append((lineno, f"{name} §{secid}"))
            if sec or link != name:
                return f"[[{link}|{display}]]"
            return f"[[{link}]]"

        new_masked = TICKED_RE.sub(repl, masked)
        new_line = unmask(new_masked, stash)
        # Compare against the ORIGINAL line, not the requalified one — otherwise
        # a line whose only change came from requalify() is written but reported
        # as unchanged, and the dry run understates what --apply will do.
        if new_line != line_in:
            changes.append((lineno, line_in.strip()[:100], new_line.strip()[:100]))
        out_lines.append(new_line)

    new_text = "\n".join(out_lines) + ("\n" if original.endswith("\n") else "")
    return new_text, changes, phantoms


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    index, ambiguous, shadowed = build_index()
    heading_cache = {}

    targets = []
    for g in TARGET_GLOBS:
        for p in sorted(REPO.glob(g)):
            if p.is_file() and not set(p.relative_to(REPO).parts) & INDEX_SKIP:
                targets.append(p)

    total, touched, all_phantoms = 0, {}, {}
    for path in targets:
        new_text, changes, phantoms = process(path, index, ambiguous,
                                              heading_cache, shadowed)
        if phantoms:
            all_phantoms[path] = phantoms
        if changes:
            touched[path] = changes
            total += len(changes)
            if args.apply:
                path.write_text(new_text, encoding="utf-8", newline="\n")

    print("=" * 72)
    print(f"wikilink sweep — {total} mention(s) in {len(touched)} file(s)")
    print(f"vault index: {len(index)} unique basenames, "
          f"{len(ambiguous)} ambiguous (skipped), {len(shadowed)} shadowed by "
          f"_old/ (path-qualified), {len(NEVER_LINK)} retired (skipped)")
    print("=" * 72)
    for path, changes in sorted(touched.items(), key=lambda kv: -len(kv[1])):
        print(f"\n{path.relative_to(REPO)}  ({len(changes)})")
        for lineno, before, after in (changes if args.verbose else changes[:3]):
            print(f"  {lineno}: {before}")
            print(f"   -> {after}")
        if not args.verbose and len(changes) > 3:
            print(f"  ... +{len(changes) - 3} more")

    if all_phantoms:
        n = sum(len(v) for v in all_phantoms.values())
        counts = collections.Counter(ref for v in all_phantoms.values()
                                     for _, ref in v)
        print(f"\n{'=' * 72}")
        print(f"PHANTOM §-ANCHORS — {n} citation(s), {len(counts)} distinct")
        print("The file is linked; the § matched no heading in it. Either the")
        print("section was renumbered/retired, or it never existed.")
        print("=" * 72)
        for ref, c in counts.most_common(20):
            print(f"  {c:3}x  {ref}")

    if not args.apply:
        print("\nDRY RUN — re-run with --apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
