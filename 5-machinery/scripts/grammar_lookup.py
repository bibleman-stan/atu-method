#!/usr/bin/env python3
"""Look up a numbered section in a reference grammar PDF, and print what it says.

WHY THIS EXISTS. The Tanakh constraint catalog carries 26 citations of the form
"Joüon §129; WO §9.3". Until 2026-08-11 none had ever been opened -- there was
no receipt in atu-nlp-wiki/raw/ at all. "26/26 constraints carry a Source" was
counting citation-shaped strings.

Checking one costs a lookup. This does the lookup, and reports the three things
the citation protocol requires: the section heading as printed, the PRINTED page
number (not the PDF page -- scans carry front-matter offsets), and the opening
text so the claim can be judged against what the grammar actually says.

Joüon-2006.pdf is 218 MB, past the Read tool's 100 MB extraction ceiling, which
is why this exists as a script rather than a tool call.

EDITION MATTERS AND IS NOT OPTIONAL. Joüon-Muraoka renumbers between the 1923
French, the 1991 English, the 1993 corrected printing and the 2006 revised
English edition. A bare "§147" is unresolvable. Whatever this reports is true of
the PDF passed in and of no other edition, so the --edition label is echoed into
the output and belongs in any citation derived from it.

    python grammar_lookup.py 147
    python grammar_lookup.py 129 --chars 1200
    python grammar_lookup.py 165 --pdf /path/to/other.pdf --edition "J-M 1991"
"""

import argparse
import os
import re
import sys

DEFAULT_PDF = os.path.join(os.path.expanduser("~"), "work", "atu-nlp-wiki",
                           "raw", "Jouon-2006.pdf")


def printed_page(text: str):
    """Recover the printed page number from a page's own text.

    Joüon-2006 sets a running head with the page number at the margin, and the
    body carries inline markers like 'p xxiv'. Try the inline marker first --
    it is unambiguous -- then fall back to a bare number on its own line."""
    m = re.search(r"\bp\s+([ivxlcdm]+|\d+)\b", text[:400], re.I)
    if m:
        return m.group(1)
    for line in text.splitlines()[:4]:
        s = line.strip()
        if re.fullmatch(r"\d{1,4}", s):
            return s
    return "?"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("section", help="section number, e.g. 147 or 129c")
    ap.add_argument("--pdf", default=DEFAULT_PDF)
    ap.add_argument("--edition", default="Joüon-Muraoka, revised English edition, 2006")
    ap.add_argument("--chars", type=int, default=700)
    ap.add_argument("--all", action="store_true", help="show every hit, not just the heading")
    args = ap.parse_args()

    try:
        import fitz
    except ImportError:
        print("PyMuPDF (fitz) required", file=sys.stderr)
        return 1
    if not os.path.exists(args.pdf):
        print(f"no such PDF: {args.pdf}", file=sys.stderr)
        return 1

    doc = fitz.open(args.pdf)
    num = re.match(r"(\d+)", args.section)
    if not num:
        print("section must start with a number", file=sys.stderr)
        return 1
    n = num.group(1)

    # A section HEADING looks like "§ 147." or "§147." near a line start. A
    # cross-reference looks like "see § 147" mid-sentence. Prefer the heading.
    heading = re.compile(r"(?:^|\n)\s*§\s*" + n + r"[\s.]", re.M)
    anywhere = re.compile(r"§\s*" + n + r"\b")

    hits = []
    for i in range(doc.page_count):
        t = doc.load_page(i).get_text()
        if heading.search(t):
            hits.append((i, t, True))
        elif args.all and anywhere.search(t):
            hits.append((i, t, False))

    if not hits:
        print(f"    §{n} not found in {os.path.basename(args.pdf)}")
        return 1

    print(f"\n    EDITION: {args.edition}")
    print(f"    FILE:    {os.path.basename(args.pdf)} ({doc.page_count} pages)\n")
    for i, t, is_head in hits[:4]:
        pp = printed_page(t)
        kind = "HEADING" if is_head else "mention"
        print(f"    --- PDF page {i+1}  |  printed page {pp}  |  {kind} ---")
        m = heading.search(t) or anywhere.search(t)
        start = max(0, m.start() - 40)
        body = " ".join(t[start:start + args.chars].split())
        print(f"    {body}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
