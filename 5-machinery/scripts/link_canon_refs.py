#!/usr/bin/env python3
"""Turn plain-text canon cross-references into clickable markdown links.

Navigation-only transform: display text is preserved VERBATIM, only wrapped in a
link. No citation is ever repointed — an unresolvable section-ID is REPORTED, not
guessed at (silent repointing is the failure mode the canon-xref arc exists to fix).

Link form follows the house style already in these docs — markdown links, not
wikilinks: ``[`framework.md`](framework.md)`` (40 pre-existing instances). Section
anchors use angle-bracket destinations so heading text stays readable in raw
markdown: ``[`framework.md §2.1`](<framework.md#§2.1 The bidirectional test ...>)``.
Wikilinks were rejected: they resolve by bare filename, and `_old/framework.md`
would make every `[[framework]]` ambiguous.

Anchor styles:
  obsidian (default) — `#<full heading text>`; Obsidian jumps to the section.
                       On GitHub the anchor misses and the file opens at the top.
  github             — `#slugified-heading`; inverse tradeoff.
  none               — file-level links only; correct everywhere, no section jump.

Section-ID schemes handled (the ID is whatever leads the heading):
  framework.md / cross-corpus-principles.md   §2.1, §7.3
  substrate.md                                 10.2
  toolset-architecture.md                      v1.5
  binding-rules-*.md                           B7

A bare section-ID with no filename (e.g. "see §7.3") is self-linked ONLY when the
ID matches a heading in the same file. In every other file a bare ID refers to some
other document's numbering — inferring the target would be a guess, so it is left
alone and counted in the report.

Usage:
    python 5-machinery/scripts/link_canon_refs.py              # dry run, prints the report
    python 5-machinery/scripts/link_canon_refs.py --apply
    python 5-machinery/scripts/link_canon_refs.py --apply --anchor-style none
"""

import argparse
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

# Live canon only. _old/ is retired canon: it is cited BY path as historical
# receipts (canon-index.md rows), never navigated to, and linking into it would
# invite exactly the archived-vs-live confusion the index calls "phantom".
EXCLUDE_DIRS = {"_old"}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# Leading section-ID of a heading, across the four numbering schemes in use.
ID_RE = re.compile(
    r"^(?:"
    r"(§\d+(?:\.\d+)*[a-z]?)"      # §2.1, §1.3a
    r"|(\d+(?:\.\d+)*)\.?(?=\s)"   # 10.  /  10.2
    r"|(v\d+(?:\.\d+)*)(?=\s|—|-)" # v1.5
    r"|([A-Z]\d+)(?=\s|—|-)"       # B7, J3, M1
    r")"
)

FENCE_RE = re.compile(r"^\s*(```|~~~)")

# Spans that must never be rewritten: existing links (label AND destination),
# and `file.md:123` line-receipts, which are provenance not navigation.
PROTECT_RES = [
    re.compile(r"\[[^\]\n]*\]\([^)\n]*\)"),
    re.compile(r"\[\[[^\]\n]*\]\]"),
    re.compile(r"`?[\w.-]+\.md`?:\d+(?:-\d+)?"),
    re.compile(r"\]\(<[^>\n]*>\)"),
]


def slugify(heading: str) -> str:
    """GitHub's heading-anchor algorithm."""
    s = heading.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())


def load_headings(path: Path) -> dict:
    """file -> {section-id: heading text}. First heading wins on duplicate IDs
    (cross-corpus-principles.md repeats §1.4 across an umbrella and its members)."""
    out, ambiguous = {}, []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        text = m.group(2).strip()
        idm = ID_RE.match(text)
        if not idm:
            continue
        sid = next(g for g in idm.groups() if g)
        if sid in out:
            ambiguous.append((path.name, sid))
            continue
        out[sid] = text
    return out, ambiguous


def protected_spans(line: str) -> list:
    spans = []
    for rx in PROTECT_RES:
        spans.extend((m.start(), m.end()) for m in rx.finditer(line))
    return spans


def in_protected(start: int, end: int, spans: list) -> bool:
    return any(s < end and start < e for s, e in spans)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--anchor-style", choices=["obsidian", "github", "none"],
                    default="obsidian")
    ap.add_argument("--files", nargs="*", default=None,
                    help="Limit REWRITING to these docs/ filenames. Headings are "
                         "still read from every doc so anchors resolve. Use to keep "
                         "link edits out of files carrying uncommitted prose.")
    args = ap.parse_args()

    files = sorted(p for p in DOCS.rglob("*.md")
                   if not (set(p.relative_to(DOCS).parts[:-1]) & EXCLUDE_DIRS))
    headings, all_ambiguous = {}, []
    for p in files:
        h, amb = load_headings(p)
        headings[p.name] = h
        all_ambiguous.extend(amb)

    names = sorted(headings, key=len, reverse=True)
    name_alt = "|".join(re.escape(n) for n in names)
    # `file.md §2.1` / `file.md` §2.1 / file.md §2.1 / `file.md` / file.md
    ref_re = re.compile(
        r"(?P<tick>`)?(?P<file>" + name_alt + r")(?(tick)`|)"
        r"(?P<gap>\s+)?(?P<idtick>`)?"
        r"(?P<id>§\d+(?:\.\d+)*[a-z]?|v\d+(?:\.\d+)*|[A-Z]\d+)?"
        r"(?(idtick)`|)"
    )
    bare_id_re = re.compile(r"(?<![\w#/.-])(§\d+(?:\.\d+)*[a-z]?)(?![\w.-])")

    linked_file = linked_anchor = self_linked = 0
    dead, skipped_bare, changed = [], {}, {}

    def anchor_for(target: str, heading: str, same_file: bool) -> str:
        base = "" if same_file else target
        if args.anchor_style == "none":
            return base or target
        frag = heading if args.anchor_style == "obsidian" else slugify(heading)
        return f"<{base}#{frag}>"

    targets = [p for p in files if args.files is None or p.name in args.files]
    for path in targets:
        src = path.read_text(encoding="utf-8")
        out_lines, in_fence = [], False
        for lineno, line in enumerate(src.splitlines(), 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                out_lines.append(line)
                continue
            if in_fence or line.lstrip().startswith("#"):
                out_lines.append(line)
                continue

            spans = protected_spans(line)
            edits = []

            for m in ref_re.finditer(line):
                if in_protected(m.start(), m.end(), spans):
                    continue
                fname, sid = m.group("file"), m.group("id")
                # `file.md` followed by a §-id belonging to a *different* doc is
                # still a file+id cite; the id must resolve in the CITED file.
                if sid and m.group("gap") is None:
                    sid = None
                end = m.end() if sid else m.end("file") + (1 if m.group("tick") else 0)
                text = line[m.start():end]
                if sid and sid not in headings.get(fname, {}):
                    dead.append((path.name, lineno, fname, sid))
                    sid = None
                    end = m.end("file") + (1 if m.group("tick") else 0)
                    text = line[m.start():end]
                if sid:
                    dest = anchor_for(fname, headings[fname][sid], same_file=False)
                    linked_anchor += 1
                else:
                    dest = fname
                    linked_file += 1
                edits.append((m.start(), end, f"[{text}]({dest})"))

            own = headings.get(path.name, {})
            for m in bare_id_re.finditer(line):
                if in_protected(m.start(), m.end(), spans):
                    continue
                if any(s <= m.start() < e for s, e, _ in edits):
                    continue
                sid = m.group(1)
                if sid not in own:
                    skipped_bare[path.name] = skipped_bare.get(path.name, 0) + 1
                    continue
                if args.anchor_style == "none":
                    continue
                dest = anchor_for(path.name, own[sid], same_file=True)
                edits.append((m.start(), m.end(), f"[{sid}]({dest})"))
                self_linked += 1

            for start, end, repl in sorted(edits, reverse=True):
                line = line[:start] + repl + line[end:]
            out_lines.append(line)

        new = "\n".join(out_lines) + ("\n" if src.endswith("\n") else "")
        if new != src:
            changed[path.name] = sum(1 for a, b in zip(src.splitlines(),
                                                        new.splitlines()) if a != b)
            if args.apply:
                path.write_text(new, encoding="utf-8", newline="\n")

    print("=" * 72)
    print(f"Canon cross-reference linker — {'APPLIED' if args.apply else 'DRY RUN'}"
          f" (anchor-style: {args.anchor_style})")
    print("=" * 72)
    print(f"\nFiles scanned: {len(files)}   changed: {len(changed)}")
    print(f"  file-level links:      {linked_file}")
    print(f"  section-anchor links:  {linked_anchor}")
    print(f"  intra-doc self-links:  {self_linked}")
    if changed:
        print("\nLines changed per file:")
        for name, n in sorted(changed.items(), key=lambda kv: -kv[1]):
            print(f"  {name:38} {n}")
    if dead:
        print(f"\nDEAD SECTION-IDs — cited but no matching heading ({len(dead)}).")
        print("  Left as file-level links; NOT repointed. Canon-xref findings:")
        seen = set()
        for fn, ln, target, sid in dead:
            key = (target, sid)
            if key in seen:
                continue
            seen.add(key)
            hits = sum(1 for d in dead if (d[2], d[3]) == key)
            print(f"  {target} {sid:8} — {hits}x, first at {fn}:{ln}")
    if skipped_bare:
        print("\nBare §-IDs left unlinked (belong to another doc's numbering):")
        for name, n in sorted(skipped_bare.items(), key=lambda kv: -kv[1]):
            print(f"  {name:38} {n}")
    if all_ambiguous:
        print(f"\nDuplicate heading IDs (first wins): "
              + ", ".join(f"{f}:{s}" for f, s in all_ambiguous))
    if not args.apply and changed:
        print("\nRe-run with --apply to write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
