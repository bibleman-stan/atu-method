#!/usr/bin/env python3
"""Measure framework claim #6: how much work does the bidirectional test do?

WHY THIS EXISTS. framework-claim-inventory.md types claim #6 as
`[UNPROVEN] — "no ratio given anywhere; trivially measurable and never
measured"`. §2.1 (the bidirectional test) is asserted to be the sole arbiter and
to do "the overwhelming majority of the work"; §2.2 (the explicit-marker
license) is the framework's ONLY break-generating licensor and is described as
"deliberately quarantined". Nobody has ever counted the split.

It matters before any grounding work: the scholarship effort rests on §2.1 being
load-bearing. If the marker license turns out to produce most breaks, then "the
bidirectional test decides" is false as practised, and the rules would be
grounded against the wrong criterion.

HOW THIS IS EXACT RATHER THAN AN UPPER BOUND. In bofm_generate.py, §2.2 is
implemented as `_marker_split`, a single pass that runs LAST, after every merge
(line ~973). It is the only break-GENERATING rule in the pipeline. So counting
how many times it fires is a direct count of §2.2-licensed breaks -- no
inference from line-initial tokens, which would over-count (a segment-LEADING
marker is skipped by condition (iii) and handled by other passes).

Counting lines that merely BEGIN with "yea" would answer a different and weaker
question. This instruments the licensor itself.

    python measure_licensor_share.py            # whole BoFM corpus
    python measure_licensor_share.py 1nephi     # one book
"""

import argparse
import os
import sys

REPOS = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
BOFM = os.path.join(REPOS, "readers-bofm")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("books", nargs="*")
    args = ap.parse_args()

    sys.path.insert(0, os.path.join(BOFM, "5-machinery", "scripts"))
    os.chdir(BOFM)
    import bofm_generate as G

    # Wrap the licensor. _split_one returns [a] + _split_one(b) when it fires and
    # [seg] when it does not, so a return longer than one element is one break.
    fired = {"n": 0}
    original = G._split_one

    def counting_split_one(seg):
        res = original(seg)
        if len(res) > 1:
            fired["n"] += len(res) - 1
        return res

    G._split_one = counting_split_one
    G._marker_split.__globals__["_split_one"] = counting_split_one

    books = args.books or list(G.BOOKS) if hasattr(G, "BOOKS") else args.books
    if not books:
        # fall back to whatever the conllu cache holds
        d = os.path.join(BOFM, "data", "parses", "v0-cache-conllu")
        books = sorted(f[:-7] for f in os.listdir(d) if f.endswith(".conllu"))

    total_lines = 0
    per_book = []
    for b in books:
        before = fired["n"]
        try:
            lines = G.generate(b)
        except Exception as e:  # noqa: BLE001 -- report, do not mask
            print(f"    {b:18} FAILED: {type(e).__name__}: {e}", file=sys.stderr)
            continue
        n = len(lines)
        total_lines += n
        per_book.append((b, n, fired["n"] - before))

    print(f"\n    {'book':18} {'ATU lines':>10} {'§2.2 breaks':>12} {'share':>8}")
    for b, n, f in per_book:
        pct = (f / n * 100) if n else 0
        print(f"    {b:18} {n:>10} {f:>12} {pct:>7.2f}%")

    tot_f = fired["n"]
    pct = (tot_f / total_lines * 100) if total_lines else 0
    print(f"\n    {'TOTAL':18} {total_lines:>10} {tot_f:>12} {pct:>7.2f}%")
    print(f"\n    §2.2 (explicit-marker license) generated {tot_f} of {total_lines} lines.")
    print(f"    Everything else -- {total_lines - tot_f} lines, {100 - pct:.2f}% -- comes")
    print("    from §2.1 and the KEEP-AS-IS default.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
