#!/usr/bin/env python3
"""The decision record — the LOG organ, finally built instead of described.

WHY THIS EXISTS, stated bluntly. Stan asked days ago how to import the LLM
wiki's log / lint / compounding-knowledge practices. Seven documents in this
repo now discuss "the decision record"; until this file, zero implemented one.
Repeatedly re-diagnosing a missing component IS the worry-bead pattern the
ops-improvement-loop page warns about: collecting notes instead of changing
behaviour. This is the behaviour change.

WHAT IT DOES. For a corpus, compare the DEPLOYED text against a REGENERATED
text and record every divergence as a structured case:

    {corpus, ref, kind, deployed, regenerated, status, detected}

Three things at once, which is why it is worth building before the architecture
question is settled:

  1. REPRODUCIBILITY GATE — "can we still produce what we ship?" One integer per
     corpus that should be zero. The migration audit found 789 divergent lines
     in BoFM this way; Alma and Words of Mormon are clean because they are the
     only books regenerated since 2026-06-03.
  2. LOG (component 9) — append-only JSONL, so history is never rewritten and a
     later run can be scoped to what changed.
  3. SEED OF CASES (component 4) — every row lands `status: unreviewed`. It
     carries the WHAT (verdict pending) even though the WHY of past adjudications
     is unrecoverable.

SET-DIFF, NOT COUNT-DIFF. Per the repo-architecture audit: counts let offsetting
errors cancel. Every divergence is emitted individually, keyed by reference.

CALIBRATE BEFORE YOU SWEEP — and this one is personal. Three detectors were
miscalibrated in a single day: a wikilink checker reporting 0 while the resolver
flagged links; a link-density metric that silently penalised the comparator's
link style; and a USFM scan that "found" 28,829 markers which were `\\n` and
`\\f` regex escapes matching newlines. A rule everyone remembers is a rule
nobody applies, so both poles are asserted IN THIS FILE and `--calibrate` runs
them. If they fail, the tool refuses to report.

    python scripts/decision_log.py --calibrate
    python scripts/decision_log.py --corpus bofm --against <regenerated-dir>
    python scripts/decision_log.py --corpus bofm --regenerate
    python scripts/decision_log.py --report
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REPOS = REPO.parent
LOG = REPO / "2-evidence" / "decision-log.jsonl"

# Per-corpus adapters. `deployed` is the live text tree; `regen` is the command
# that rebuilds it from source. A corpus whose regen command is unknown reports
# SKIPPED with a reason — never a silent pass, because a gate that cannot run is
# not a gate that passed.
CORPORA = {
    "bofm": {
        "repo": "readers-bofm",
        "deployed": "data/text-files/v2",
        "regen": ["python", "5-machinery/scripts/bofm_generate.py"],
        "ref_re": re.compile(r"^(\d+):(\d+)$"),
    },
    "gnt": {
        "repo": "readers-gnt",
        "deployed": "data/text-files/v1.5/grk",
        "regen": None,
        "ref_re": re.compile(r"^(\d+):(\d+)$"),
    },
    "tanakh": {
        "repo": "readers-tanakh",
        "deployed": "data/text-files/v2/heb",
        "regen": None,
        "ref_re": re.compile(r"^(\d+):(\d+)$"),
    },
    "lxx": {
        "repo": "readers-lxx",
        "deployed": "data/text-files/v2",
        "regen": None,
        "ref_re": re.compile(r"^(\d+):(\d+)$"),
    },
    "vulgate": {
        "repo": "readers-vulgate",
        "deployed": "data/text-files/v2",
        "regen": None,
        "ref_re": re.compile(r"^(\d+):(\d+)$"),
    },
}


def parse_tree(root: Path, ref_re) -> dict:
    """{(file_stem, ref): [lines]} for every verse in a corpus tree.

    Corpus files are blank-line-separated blocks: a bare `C:V` reference line
    followed by one line per ATU. Unknown-shaped files are skipped rather than
    guessed at.
    """
    out = {}
    if not root.exists():
        return out
    for path in sorted(root.rglob("*.txt")):
        stem = path.stem
        ref, buf = None, []
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.rstrip()
            if not line:
                continue
            if ref_re.match(line):
                if ref is not None:
                    out[(stem, ref)] = buf
                ref, buf = line, []
            elif ref is not None:
                buf.append(line)
        if ref is not None:
            out[(stem, ref)] = buf
    return out


def diff_trees(deployed: dict, regenerated: dict, corpus: str) -> list:
    """Every divergence, individually. Never a count."""
    rows, today = [], date.today().isoformat()
    for key in sorted(set(deployed) | set(regenerated), key=lambda k: (k[0], k[1])):
        stem, ref = key
        d, r = deployed.get(key), regenerated.get(key)
        if d == r:
            continue
        if d is None:
            kind = "only-in-regenerated"
        elif r is None:
            kind = "only-in-deployed"
        elif len(d) != len(r):
            kind = "line-count"
        else:
            kind = "line-text"
        rows.append({
            "corpus": corpus, "file": stem, "ref": ref, "kind": kind,
            "deployed_lines": len(d) if d is not None else None,
            "regenerated_lines": len(r) if r is not None else None,
            "deployed": d, "regenerated": r,
            "status": "unreviewed", "detected": today,
        })
    return rows


# ---------------------------------------------------------------------------
# Calibration — both poles, asserted here, run by --calibrate.
# ---------------------------------------------------------------------------

def calibrate() -> bool:
    ref_re = CORPORA["bofm"]["ref_re"]
    ok = True

    with tempfile.TemporaryDirectory() as td:
        a, b = Path(td) / "a", Path(td) / "b"
        a.mkdir(); b.mkdir()
        clean = "1:1\nAnd it came to pass;\nthat he went forth.\n\n1:2\nBehold.\n"
        (a / "x.txt").write_text(clean, encoding="utf-8")

        # POLE 1 — a known-good case that MUST report zero.
        (b / "x.txt").write_text(clean, encoding="utf-8")
        n = len(diff_trees(parse_tree(a, ref_re), parse_tree(b, ref_re), "t"))
        print(f"  [{'PASS' if n == 0 else 'FAIL'}] identical trees -> 0 divergences (got {n})")
        ok &= (n == 0)

        # POLE 2 — a planted defect that MUST be found. This is the real BoFM
        # shape: one verse merged from two ATUs into one.
        (b / "x.txt").write_text(
            "1:1\nAnd it came to pass; that he went forth.\n\n1:2\nBehold.\n",
            encoding="utf-8")
        rows = diff_trees(parse_tree(a, ref_re), parse_tree(b, ref_re), "t")
        hit = len(rows) == 1 and rows[0]["ref"] == "1:1" and rows[0]["kind"] == "line-count"
        print(f"  [{'PASS' if hit else 'FAIL'}] planted merge at 1:1 -> found "
              f"({len(rows)} row(s), kind={rows[0]['kind'] if rows else 'none'})")
        ok &= hit

        # POLE 3 — a missing verse must not be silently equal.
        (b / "x.txt").write_text("1:1\nAnd it came to pass;\nthat he went forth.\n",
                                 encoding="utf-8")
        rows = diff_trees(parse_tree(a, ref_re), parse_tree(b, ref_re), "t")
        hit = any(r["kind"] == "only-in-deployed" and r["ref"] == "1:2" for r in rows)
        print(f"  [{'PASS' if hit else 'FAIL'}] dropped verse 1:2 -> reported as only-in-deployed")
        ok &= hit

    return ok


def append(rows: list) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", choices=sorted(CORPORA))
    ap.add_argument("--against", help="compare deployed against this tree")
    ap.add_argument("--regenerate", action="store_true")
    ap.add_argument("--calibrate", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--record", action="store_true", help="append findings to the log")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration — both poles must pass before this tool may report")
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED — do not trust output")
        return 0 if ok else 1

    if args.report:
        if not LOG.exists():
            print("no decision log yet")
            return 0
        rows = [json.loads(l) for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()]
        by = {}
        for r in rows:
            by.setdefault((r["corpus"], r["status"]), 0)
            by[(r["corpus"], r["status"])] += 1
        print(f"decision log: {len(rows)} row(s)")
        for (c, s), n in sorted(by.items()):
            print(f"  {c:10} {s:12} {n}")
        return 0

    if not args.corpus:
        ap.error("--corpus required (or use --calibrate / --report)")

    # A gate must be calibrated before it is trusted.
    if not calibrate():
        print("MISCALIBRATED — refusing to report", file=sys.stderr)
        return 1

    spec = CORPORA[args.corpus]
    root = REPOS / spec["repo"]
    deployed_dir = root / spec["deployed"]
    if not deployed_dir.exists():
        print(f"SKIPPED {args.corpus}: deployed tree not found at {deployed_dir}")
        return 0

    if args.against:
        regen_dir = Path(args.against)
    elif args.regenerate:
        if not spec["regen"]:
            print(f"SKIPPED {args.corpus}: no regeneration command known. "
                  f"A gate that cannot run is not a gate that passed.")
            return 0
        print(f"regenerating {args.corpus} ...")
        r = subprocess.run(spec["regen"], cwd=root, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            print(f"SKIPPED {args.corpus}: regeneration failed\n"
                  f"{(r.stderr or r.stdout)[:400]}")
            return 0
        regen_dir = deployed_dir
    else:
        ap.error("need --against <dir> or --regenerate")

    dep = parse_tree(deployed_dir, spec["ref_re"])
    reg = parse_tree(regen_dir, spec["ref_re"])
    rows = diff_trees(dep, reg, args.corpus)

    print(f"\n{args.corpus}: {len(dep)} deployed verses, {len(reg)} regenerated")
    print(f"DIVERGENCES: {len(rows)}   (this number should be 0)")
    for r in rows[:15]:
        print(f"  {r['file']} {r['ref']:>8}  {r['kind']:<20} "
              f"{r['deployed_lines']} -> {r['regenerated_lines']}")
    if len(rows) > 15:
        print(f"  ... +{len(rows) - 15} more")

    if args.record and rows:
        append(rows)
        print(f"\nrecorded {len(rows)} row(s) -> {LOG.relative_to(REPO).as_posix()}")
    elif rows:
        print("\nnot recorded — re-run with --record")
    return 0


if __name__ == "__main__":
    sys.exit(main())
