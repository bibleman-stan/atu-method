#!/usr/bin/env python3
"""Per-violation baseline: name what changed, instead of counting it.

WHY THIS EXISTS. The baselines store one integer per rule. A commit that changes
counts is blocked with "R10: 73 -> 135" and no way to see WHICH 62 are new, so
the only moves available are rubber-stamp the baseline or bypass the gate. On
2026-08-10 I bypassed twice in one session, each time for a defensible reason,
which is how a standing problem becomes a habit.

Counts also cancel. Two rules fixed and two broken shows as no change at all, so
a clean count is not evidence of a clean corpus — the same silent-pass defect as
a validator that returns 0 when its inputs are missing.

A Candidate already carries a stable identity: (rule, verse_ref, line_index).
Storing the SET makes the diff a named list — these are new, these are resolved —
which is what makes re-blessing a decision rather than a shrug.

    python baseline_setdiff.py readers-gnt              # what changed, named
    python baseline_setdiff.py readers-gnt --bless      # accept current as new baseline
    python baseline_setdiff.py --calibrate
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent.parent


def identity(c) -> str:
    """Stable per-violation key. line_text is deliberately excluded — a
    reworded line is the same finding, and including it would report every
    editorial touch as a new violation."""
    return f"{getattr(c, 'verse_ref', '?')}#{getattr(c, 'line_index', -1)}"


def collect(repo: Path) -> dict:
    """Import the repo's own run_all and use its collector, rather than
    reimplementing discovery and getting a different answer than the gate does."""
    mach = repo / "5-machinery"
    sys.path.insert(0, str(mach))
    sys.path.insert(0, str(mach / "validators"))
    import importlib
    for mod in list(sys.modules):
        if mod.startswith(("validators", "run_all")):
            del sys.modules[mod]
    run_all = importlib.import_module("validators.run_all")
    out = run_all.collect_candidates()
    cands = out[0] if isinstance(out, tuple) else out
    by_rule: dict[str, set] = {}
    for c in cands:
        by_rule.setdefault(getattr(c, "rule", "?"), set()).add(identity(c))
    return by_rule


def calibrate() -> bool:
    """Both poles on the diff itself, which is the part that can lie."""
    ok = True

    def diff(base, cur):
        new = {r: sorted(cur.get(r, set()) - base.get(r, set())) for r in
               set(base) | set(cur)}
        gone = {r: sorted(base.get(r, set()) - cur.get(r, set())) for r in
                set(base) | set(cur)}
        return ({r: v for r, v in new.items() if v},
                {r: v for r, v in gone.items() if v})

    cases = [
        ({"R1": {"a", "b"}}, {"R1": {"a", "b"}}, 0, 0, "identical sets: nothing reported"),
        ({"R1": {"a"}}, {"R1": {"a", "b"}}, 1, 0, "one added is named"),
        ({"R1": {"a", "b"}}, {"R1": {"a"}}, 0, 1, "one resolved is named"),
        # The case counts cannot see at all:
        ({"R1": {"a", "b"}}, {"R1": {"a", "c"}}, 1, 1,
         "SAME COUNT, different members: both reported"),
    ]
    for base, cur, want_new, want_gone, why in cases:
        n, g = diff(base, cur)
        got_new = sum(len(v) for v in n.values())
        got_gone = sum(len(v) for v in g.values())
        hit = (got_new, got_gone) == (want_new, want_gone)
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?")
    ap.add_argument("--bless", action="store_true")
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration — the diff must name additions, removals, and swaps")
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED")
        return 0 if ok else 1
    if not args.repo:
        ap.error("repo required (or --calibrate)")
    if not calibrate():
        print("MISCALIBRATED — refusing to report", file=sys.stderr)
        return 1
    print()

    repo = REPOS / args.repo
    store = repo / "5-machinery" / "validators" / ".baseline-set.json"
    current = collect(repo)

    if not store.exists():
        if args.bless:
            store.write_text(json.dumps(
                {r: sorted(v) for r, v in sorted(current.items())},
                indent=1), encoding="utf-8")
            total = sum(len(v) for v in current.values())
            print(f"{args.repo}: seeded set-baseline with {total} violation(s) "
                  f"across {len(current)} rule(s)")
            return 0
        print(f"{args.repo}: no set-baseline yet. Re-run with --bless to seed it "
              f"from the current state.")
        return 1

    base = {r: set(v) for r, v in json.loads(store.read_text(encoding="utf-8")).items()}
    rules = sorted(set(base) | set(current))
    new = {r: sorted(current.get(r, set()) - base.get(r, set())) for r in rules}
    gone = {r: sorted(base.get(r, set()) - current.get(r, set())) for r in rules}
    new = {r: v for r, v in new.items() if v}
    gone = {r: v for r, v in gone.items() if v}

    if not new and not gone:
        print(f"{args.repo}: identical to baseline — no violations added or resolved")
        return 0

    for label, d in (("NEW", new), ("RESOLVED", gone)):
        if not d:
            continue
        print(f"{label}:")
        for rule, items in sorted(d.items()):
            print(f"  {rule} ({len(items)})")
            for i in items[:6]:
                print(f"      {i}")
            if len(items) > 6:
                print(f"      ... +{len(items) - 6} more")

    if args.bless:
        store.write_text(json.dumps(
            {r: sorted(v) for r, v in sorted(current.items())}, indent=1),
            encoding="utf-8")
        print("\nblessed — the listed changes are now the baseline")
        return 0
    print("\nReview the named findings above, then --bless to accept them.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
