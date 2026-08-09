#!/usr/bin/env python3
"""Growth snapshot — is this repo's knowledge COMPOUNDING or merely accumulating?

Ported 2026-08-08 from meta-wiki's admin/growth-snapshot.py, whose sharpest
contribution is the choice of metric:

    The discriminating metric is LINKS-PER-PAGE, not pages.
    Page count tracks EFFORT (how much got written).
    Link density tracks INTEGRATION (whether it landed in a richer base).

That distinction is the whole compounding claim. Karpathy's mechanism is not
store-and-retrieve but integrate — a new source updates the pages that already
exist. Plain accumulation is the trap: "append-only aggregation earns nothing."

Predictions, so this instrument can be WRONG rather than merely descriptive:
  - compounding  -> links/page RISES as pages grow (each lands in a richer base)
  - accumulating -> links/page stays FLAT
  - drifting     -> orphans rise and density falls
  - append-trap  -> words/page rises without bound

Counts BOTH link syntaxes. This repo uses wikilinks and markdown links side by
side, and counting only one would understate density by roughly half — the kind
of miscalibration that makes a metric manufacture its own conclusion.

    python scripts/growth_snapshot.py            # print, do not record
    python scripts/growth_snapshot.py --record   # append a row to the series
"""

import argparse
import collections
import csv
import datetime
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "2-evidence" / "growth-data.csv"

# The compiled layer — the pages that are supposed to integrate.
TIERS = ["1-method", "2-evidence", "3-implementation", "4-process"]
ROOT_DOCS = ["00-start-here.md", "canon-index.md", "Current-Tasks.md",
             "Pending-Decisions.md", "README.md"]
# memories/ is the capture buffer, not the compiled layer (per meta-wiki's
# ops-improvement-loop: the log is a buffer between raw and compiled). Measured
# separately so a growing buffer never flatters the compiled density.
BUFFER = ["memories"]

STRIP = re.compile(r"```.*?```|`[^`\r\n]+`", re.S)
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)")
MD_LINK = re.compile(r"\[[^\]]*\]\(<?([^)>#\s]+)")


def collect(paths):
    pages, words, links = [], 0, 0
    targets = collections.defaultdict(set)
    for p in paths:
        name = p.name
        pages.append(name)
        body = STRIP.sub("", p.read_text(encoding="utf-8", errors="replace"))
        words += len(body.split())
        for rx in (WIKI_LINK, MD_LINK):
            for m in rx.finditer(body):
                t = m.group(1).strip().split("/")[-1]
                if not t.endswith(".md"):
                    continue
                links += 1
                targets[t].add(name)
    # An orphan is a page nothing else points at. Self-links do not count.
    orphans = [n for n in pages if not (targets.get(n, set()) - {n})]
    return pages, words, links, targets, orphans


def gather():
    compiled = []
    for t in TIERS:
        compiled += sorted((REPO / t).glob("*.md"))
    compiled += sorted((REPO / "2-evidence" / "scholarship").rglob("*.md"))
    for d in ROOT_DOCS:
        if (REPO / d).exists():
            compiled.append(REPO / d)
    buffer_pages = sorted((REPO / "memories").glob("*.md"))
    return compiled, buffer_pages


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", action="store_true")
    args = ap.parse_args()

    compiled, buffered = gather()
    pages, words, links, targets, orphans = collect(compiled)
    bpages, bwords, blinks, _, borphans = collect(buffered)

    density = round(links / max(1, len(pages)), 2)
    wpp = round(words / max(1, len(pages)))
    schema_chars = len((REPO / "CLAUDE.md").read_text(encoding="utf-8",
                                                      errors="replace"))
    row = {
        "date": datetime.date.today().isoformat(),
        "pages": len(pages),
        "words": words,
        "links": links,
        "links_per_page": density,
        "words_per_page": wpp,
        "targets": len(targets),
        "orphans": len(orphans),
        "buffer_pages": len(bpages),
        "buffer_links_per_page": round(blinks / max(1, len(bpages)), 2),
        "schema_chars": schema_chars,
    }

    print("=" * 72)
    print("atu-method growth snapshot — compiled layer")
    print("=" * 72)
    for k, v in row.items():
        print(f"  {k:24} {v}")
    if orphans:
        print(f"\n  ORPHANS ({len(orphans)}) — nothing links to these:")
        for o in sorted(orphans):
            print(f"    {o}")

    if args.record:
        new = not DATA.exists()
        with DATA.open("a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(row))
            if new:
                w.writeheader()
            w.writerow(row)
        print(f"\nrecorded -> {DATA.relative_to(REPO).as_posix()}")
    else:
        print("\nnot recorded — re-run with --record to append to the series")
    return 0


if __name__ == "__main__":
    sys.exit(main())
