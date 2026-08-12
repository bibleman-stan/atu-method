#!/usr/bin/env python3
"""Count retraction sub-patterns cross-corpus and report 3-strike candidates.

WHY THIS EXISTS. The retraction protocol promotes a sub-pattern to
`memories/feedback_three_anti_default_factors.md` on 3 strikes under a shared
factor + sub-pattern. Each reader repo tracks its own counts by hand, and
readers-gnt's own note says the obvious thing: "cross-corpus alignment via the
sibling logs may narrow or rename them before promotion." Nobody had done that
count, so `loop_health` reported "31 entries, zero promotions" and left the
threshold question unanswerable from the number alone.

TWO WAYS TO GET THIS WRONG, both hit on the first attempt:

1. DOUBLE-COUNTING. Five entries dated 2026-05-17 appear verbatim in all three
   repos — one retraction event, logged three times. Counting rows makes a
   single event look like an instant 3-strike. Entries are therefore deduped on
   (date, title) before counting.

2. TRUNCATED NAMES. A first pass cut sub-patterns at the first hyphen, turning
   "rhetorical-figure smuggling" into "rhetorical" and merging it with anything
   else starting the same way. Every apparent 3-strike was an artifact. Names
   are now taken whole, to end of line.

    python retraction_threshold.py
    python retraction_threshold.py --calibrate
"""

import argparse
import collections
import os
import re
import sys

REPOS = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
LOGS = ["readers-bofm", "readers-gnt", "readers-tanakh", "atu-method"]
THRESHOLD = 3

ENTRY = re.compile(r"^### (.+)$", re.M)
FACTOR = re.compile(r"\*\*Factor:\*\*\s*(.+)")
# To END OF LINE. Hyphens are part of sub-pattern names, not delimiters.
SUBPAT = re.compile(r"\*\*Sub-pattern:\*\*\s*(.+)")


def parse(repo: str):
    """Yield (repo, date, title, factor, subpattern) per entry."""
    for rel in ("2-evidence/retraction-log.md", "retraction-log.md"):
        p = os.path.join(REPOS, repo, rel)
        if os.path.exists(p):
            break
    else:
        return
    text = open(p, encoding="utf-8", errors="replace").read()
    if "## Retractions" not in text:
        return
    body = text.split("## Retractions", 1)[1]
    body = re.split(r"^## ", body, flags=re.M)[0]
    parts = re.split(r"^### ", body, flags=re.M)[1:]
    for blk in parts:
        head = blk.splitlines()[0].strip()
        m = re.match(r"(\d{4}-\d{2}-\d{2})\s*—\s*(.+)", head)
        date, title = (m.group(1), m.group(2)) if m else ("?", head)
        f = FACTOR.search(blk)
        s = SUBPAT.search(blk)
        fac = f.group(1).strip() if f else "(unclassified)"
        sub = s.group(1).strip() if s else "(unclassified)"
        # A sub-pattern line reads "name — gloss" or "name (gloss)". Keep the
        # NAME. Split only on the em-dash separator, never on hyphens, then drop
        # a trailing parenthetical.
        #
        # THIS NORMALISATION DECIDES THE ANSWER. Without the parenthetical strip,
        # "rhetorical-figure smuggling" and "rhetorical-figure smuggling
        # (treating a rhetorical pattern...)" count as two different sub-patterns
        # and the tally reports 0 at threshold. With it, they are one pattern at
        # 3. Same for "new-rule reflex". The glosses are commentary, not
        # identity, so they are stripped -- but a reader should know the count is
        # sensitive to this and check the names below before trusting a promotion.
        sub = re.split(r"\s+—\s+", sub)[0].strip()
        sub = re.sub(r"\s*\(.*$", "", sub).strip()
        fac = re.sub(r"\s*\(.*$", "", fac).strip()
        yield (repo, date, title, fac, sub)


def calibrate() -> bool:
    ok = True
    cases = [
        ("**Sub-pattern:** rhetorical-figure smuggling — breath as a gate",
         "rhetorical-figure smuggling", "hyphenated name survives; em-dash gloss dropped"),
        ("**Sub-pattern:** surface-evidence-overweight",
         "surface-evidence-overweight", "multi-hyphen name survives whole"),
        ("**Sub-pattern:** new-rule reflex over uniform-application",
         "new-rule reflex over uniform-application", "spaces and hyphens both survive"),
    ]
    for line, want, why in cases:
        m = SUBPAT.search(line)
        got = re.split(r"\s+—\s+", m.group(1).strip())[0].strip() if m else None
        hit = got == want
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}", file=sys.stderr)
        if not hit:
            print(f"        got {got!r}", file=sys.stderr)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration -- sub-pattern names keep their hyphens", file=sys.stderr)
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED", file=sys.stderr)
        return 0 if ok else 1
    if not calibrate():
        print("MISCALIBRATED -- refusing to report", file=sys.stderr)
        return 1

    rows = [r for repo in LOGS for r in parse(repo)]
    # Dedupe on (date, title): the same retraction logged in three repos is ONE
    # strike, not three.
    seen, distinct = set(), []
    dupes = collections.defaultdict(list)
    for repo, date, title, fac, sub in rows:
        key = (date, title)
        dupes[key].append(repo)
        if key in seen:
            continue
        seen.add(key)
        distinct.append((date, title, fac, sub))

    counts = collections.Counter((f, s) for _, _, f, s in distinct)
    shared = {k: v for k, v in dupes.items() if len(v) > 1}

    print(f"\n    rows across all logs      : {len(rows)}")
    print(f"    distinct retractions      : {len(distinct)}")
    print(f"    logged in >1 repo         : {len(shared)}"
          f"  (one event, {sum(len(v) for v in shared.values())} rows)")
    print(f"\n    sub-pattern counts (deduped), threshold = {THRESHOLD}:\n")
    hits = 0
    for (f, s), n in counts.most_common():
        flag = "   <== AT THRESHOLD" if n >= THRESHOLD else ""
        hits += n >= THRESHOLD
        print(f"      {n}  [{f}] {s}{flag}")
    print(f"\n    sub-patterns at or over threshold: {hits}")
    if not hits:
        print("    The loop is not stalled — nothing has recurred often enough")
        print("    to promote. Zero promotions is the CORRECT output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
