#!/usr/bin/env python3
"""Normalize a reader repo to the five-tier shape. One repo per run, dry by default.

Target shape, agreed 2026-08-09:

    1-method/     per-corpus canon (colometry-canon, scholarship)   [PUBLIC]
    2-evidence/   measurements, findings, draft corpora
    3-project/    deployment status, build plans, inventories
    4-process/    loops, protocols, retraction-log
    5-machinery/  5-machinery/scripts, validators, 5-machinery/tests
    private/      gitignored — substrate, licensed sources
    books/ data/ index.html sw.js CNAME   ← the SERVED SITE, deliberately unnumbered

The last line is load-bearing: GitHub Pages serves from the repo root, so the
site files must stay where they are. Numbering them would break four live
domains.

WHY A SCRIPT AND NOT git mv BY HAND: the moves are the easy part. The cascade is
the path references — 12 tracked files in readers-vulgate alone name `5-machinery/scripts/`
or `research/`. Hand-moving produced 103 dangling citations the last time this
was attempted repo-wide, so every run repoints references and then VERIFIES no
old path survives.

    python 5-machinery/scripts/reorg_reader.py readers-vulgate            # dry run
    python 5-machinery/scripts/reorg_reader.py readers-vulgate --apply
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent

# Per-repo move plan. Each repo differs — tanakh has canon/ and handoffs/, gnt
# has validators/, vulgate has research/ — so "the same reorg" is really five
# different operations sharing a shape. Enumerated rather than guessed.
PLANS = {
    "readers-vulgate": {
        "moves": [
            ("5-machinery/scripts", "5-machinery/scripts"),
            ("research/OT-BUILD-PLAN.md", "3-project/OT-BUILD-PLAN.md"),
            ("research/SUBSTRATE-INVENTORY.md", "3-project/SUBSTRATE-INVENTORY.md"),
            ("research/dr-coverage.json", "2-evidence/dr-coverage.json"),
            ("research/lexham-v1", "2-evidence/lexham-v1"),
        ],
        "stubs": ["1-method", "4-process"],
    },
    "readers-lxx": {
        "moves": [
            ("5-machinery/scripts", "5-machinery/scripts"),
            ("research/SUBSTRATE-INVENTORY.md", "3-project/SUBSTRATE-INVENTORY.md"),
            ("research/TOOLING-TEXTFABRIC.md", "4-process/TOOLING-TEXTFABRIC.md"),
            ("research/brenton-coverage.json", "2-evidence/brenton-coverage.json"),
            ("research/projection-v1-stats.md", "2-evidence/projection-v1-stats.md"),
            ("research/projection-v1-validation", "2-evidence/projection-v1-validation"),
            ("research/projection-v1", "2-evidence/projection-v1"),
        ],
        "stubs": ["1-method"],
    },
    "readers-gnt": {
        "moves": [
            ("5-machinery/scripts", "5-machinery/scripts"),
            ("validators", "5-machinery/validators"),
            ("5-machinery/tests", "5-machinery/tests"),
            ("retraction-log.md", "2-evidence/retraction-log.md"),
            ("handoffs/00-index.md", "3-project/00-index.md"),
            ("handoffs/01-project-overview.md", "3-project/01-overview.md"),
            ("handoffs/04-editorial-workflow.md", "3-project/02-text-editorial.md"),
            ("handoffs/03-architecture.md", "4-process/03-architecture.md"),
        ],
        "stubs": ["1-method"],
    },
    "readers-tanakh": {
        "moves": [
            ("5-machinery/scripts", "5-machinery/scripts"),
            ("validators", "5-machinery/validators"),
            ("5-machinery/tests", "5-machinery/tests"),
            ("canon", "1-method/canon"),
            ("retraction-log.md", "2-evidence/retraction-log.md"),
            ("handoffs/00-index.md", "3-project/00-index.md"),
            ("handoffs/01-project-overview.md", "3-project/01-overview.md"),
            ("handoffs/04-editorial-workflow.md", "3-project/02-text-editorial.md"),
            ("handoffs/03-architecture.md", "4-process/03-architecture.md"),
            ("handoffs/14-operational-protocols.md", "4-process/02-operational-protocols.md"),
        ],
        "stubs": [],
    },
    "atu-method": {
        "moves": [
            ("5-machinery/scripts", "5-machinery/scripts"),
            ("5-machinery/tests", "5-machinery/tests"),
        ],
        "stubs": [],
    },
}

STUB = """# {tier}

{blurb}

Part of the five-tier reader shape: `1-method` (canon) · `2-evidence`
(measurements) · `3-project` (deployment state) · `4-process` (loops and
protocols) · `5-machinery` (code). The served site — `books/`, `data/`,
`index.html`, `sw.js`, `CNAME` — stays unnumbered at the root because GitHub
Pages serves from there.
"""

# Aligned 2026-08-10 to readers-bofm's ACTUAL practice, not my first draft.
# Surveyed bofm — 33 real documents in place against vulgate's two stubs — and
# it disagreed with my written definition in three places. bofm won each time:
#   - retraction-log.md lives in 2-evidence, not 4-process. A retraction records
#     a claim that turned out false, which is evidence.
#   - deployment-infra lives in 4-process, not 3-project. 4-process is HOW the
#     work runs, including how deployment runs; 3-project is WHAT this corpus is
#     and where it stands.
#   - 3-project is a handbook (overview, editorial, UI/UX, audio, bugs,
#     glossary), not a status page.
# bofm also numbers files within 3-project and 4-process, where the documents
# read in sequence, and does not in 1-method or 2-evidence, where they do not.
BLURBS = {
    "1-method": "Per-corpus canon: colometry rules, pericope rules, scholarly "
                "grounding, rules audit. Public by decision — publishing Stan's "
                "own method canon is fine; third-party licensed material is not.",
    "2-evidence": "What has been measured, and what turned out wrong: research "
                  "notes, coverage reports, comparisons against external "
                  "witnesses, and the retraction log.",
    "3-project": "The handbook — what this corpus is and where it stands: "
                 "overview, editorial decisions, UI/UX, audio, future plans, "
                 "bugs, glossary. Files numbered, because they read in order.",
    "4-process": "How the work runs: improvement loops, pipeline and gates, "
                 "operational protocols, build pipeline, deployment infra, "
                 "pending tasks, skills. Files numbered, because they read in "
                 "order.",
}

TEXT_EXT = {".md", ".py", ".json", ".html", ".js", ".txt", ".yaml", ".yml"}

# NEVER rewrite inside the corpus. data/ holds vendored source text and generated
# editions; a path-repoint has no business there, and readers-gnt proved why —
# TAGNT_Mat-Jhn.txt and TAGNT_Act-Rev.txt accounted for 2,254 of 2,825 "matches"
# because the apparatus says "manuscripts" constantly. books/ is generated HTML.
SKIP_DIRS = ("data/", "books/", "_archive/")

# Both boundaries. The first version had only a trailing guard, so `5-machinery/scripts`
# matched inside `manuscripts` and `5-machinery/tests` inside `attests` — one --apply from
# rewriting the Greek New Testament's apparatus into `manu5-machinery/scripts`.
# Caught by the dry run on readers-gnt; the calibration poles missed it because
# they tested the trailing boundary and not the leading one.
def _pat(src, dst=None):
    guard = ""
    if dst and dst.endswith(src) and len(dst) > len(src):
        guard = f"(?<!{re.escape(dst[:-len(src)])})"
    return guard + r"(?<![\w/-])" + re.escape(src) + r"(?![\w-])"


def sh(root, *args, check=True):
    r = subprocess.run(args, cwd=root, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        print(f"    ! {(r.stderr or r.stdout).strip()[:160]}")
    return (r.stdout or "").strip()


def calibrate() -> bool:
    """Both poles, in-file, per the lesson captured 2026-08-09: no checker gets
    wired in until it can be shown to find a real defect and not flag a clean
    result. This verifier failed exactly that on its first run."""
    ok = True

    def stale(body, src, dst):
        return len(re.findall(_pat(src, dst), body))

    cases = [
        ("see 5-machinery/scripts/build.py", "5-machinery/scripts", "5-machinery/scripts",
         0, "a correctly-rewritten path is NOT stale"),
        ("see 5-machinery/scripts/build.py", "5-machinery/scripts", "5-machinery/scripts",
         1, "a genuinely unrewritten path IS stale"),
        ("see research/old.md", "research", "2-evidence",
         1, "non-nested move still detects"),
        ("see scriptsfoo/x", "5-machinery/scripts", "5-machinery/scripts",
         0, "trailing word-boundary guard holds"),
        ("the manuscripts agree", "5-machinery/scripts", "5-machinery/scripts",
         0, "LEADING boundary: manuscripts is not 5-machinery/scripts"),
        ("it attests the reading", "5-machinery/tests", "5-machinery/tests",
         0, "LEADING boundary: attests is not 5-machinery/tests"),
    ]
    for body, src, dst, expect, why in cases:
        got = stale(body, src, dst)
        hit = got == expect
        ok &= hit
        print(f"  [{'PASS' if hit else 'FAIL'}] {why} — found {got}, expected {expect}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", nargs="?")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--calibrate", action="store_true")
    args = ap.parse_args()

    if args.calibrate:
        print("calibration — the verifier must find real staleness and only that")
        ok = calibrate()
        print("\nCALIBRATED" if ok else "\nMISCALIBRATED")
        return 0 if ok else 1
    if not args.repo:
        ap.error("repo required (or --calibrate)")
    if not calibrate():
        print("MISCALIBRATED — refusing to run", file=sys.stderr)
        return 1

    plan = PLANS.get(args.repo)
    if not plan:
        print(f"no plan for {args.repo}; add one to PLANS after surveying it")
        return 1
    root = REPOS / args.repo
    if not (root / ".git").exists():
        print(f"{root} is not a git repo")
        return 1

    # Build the rewrite table from the moves, longest source first so that a
    # prefix never eats a longer path.
    rewrites = sorted(plan["moves"], key=lambda m: -len(m[0]))

    print(f"=== {args.repo} ===\nmoves:")
    for src, dst in plan["moves"]:
        exists = (root / src).exists()
        print(f"  {'ok ' if exists else 'MISSING'} {src}  ->  {dst}")

    tracked = [p for p in sh(root, "git", "ls-files").splitlines()
               if Path(p).suffix in TEXT_EXT
               and not p.startswith(SKIP_DIRS)]
    hits = {}
    for p in tracked:
        f = root / p
        try:
            body = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        n = sum(len(re.findall(_pat(src, dst), body))
                for src, dst in rewrites)
        if n:
            hits[p] = n
    print(f"\nreferences to repoint: {sum(hits.values())} in {len(hits)} file(s)")
    for p, n in sorted(hits.items(), key=lambda kv: -kv[1])[:8]:
        print(f"  {n:3}  {p}")

    if not args.apply:
        print("\nDRY RUN — re-run with --apply")
        return 0

    for tier in plan["stubs"]:
        d = root / tier
        d.mkdir(exist_ok=True)
        (d / "README.md").write_text(
            STUB.format(tier=tier, blurb=BLURBS[tier]), encoding="utf-8",
            newline="\n")
    for src, dst in plan["moves"]:
        if not (root / src).exists():
            continue
        (root / dst).parent.mkdir(parents=True, exist_ok=True)
        # git mv only moves TRACKED paths. readers-lxx carries 12 untracked
        # 5-machinery/scripts and an 8 MB untracked projection-v1/ corpus; leaving them
        # behind would orphan the folder the move exists to retire. Move them on
        # the filesystem instead — they stay untracked at the new location, and
        # the separate commit-or-discard decision is unaffected.
        if sh(root, "git", "ls-files", "--error-unmatch", src, check=False):
            sh(root, "git", "mv", src, dst)
        else:
            shutil.move(str(root / src), str(root / dst))
            print(f"    (untracked, moved on disk) {src}")
        # A partially-tracked directory: git mv moved the tracked members, the
        # rest remain. Sweep them across too.
        if (root / src).exists() and (root / src).is_dir():
            for leftover in list((root / src).iterdir()):
                shutil.move(str(leftover), str(root / dst / leftover.name))
            try:
                (root / src).rmdir()
            except OSError:
                pass

    for p in tracked:
        f = root / p
        # a moved file lives at its new path now
        for src, dst in rewrites:
            if p == src or p.startswith(src + "/"):
                f = root / (dst + p[len(src):])
                break
        if not f.exists():
            continue
        body = f.read_text(encoding="utf-8", errors="replace")
        new = body
        for src, dst in rewrites:
            new = re.sub(_pat(src, dst), dst, new)
        if new != body:
            f.write_text(new, encoding="utf-8", newline="\n")

    # VERIFY: no old path may survive in a tracked text file.
    #
    # The obvious check is wrong, and its first run proved it: `5-machinery/
    # 5-machinery/scripts` CONTAINS `5-machinery/scripts`, so searching for the old path matches the new
    # one and reported 24 stale references against a clean rewrite. A verifier
    # that cannot tell its own success from failure is worse than none.
    #
    # Fix: when the destination ends with the source, require the match NOT be
    # preceded by the destination's prefix.
    left = {}
    for p in sh(root, "git", "ls-files").splitlines():
        if Path(p).suffix not in TEXT_EXT or p.startswith(SKIP_DIRS):
            continue
        f = root / p
        if not f.exists():
            continue
        body = f.read_text(encoding="utf-8", errors="replace")
        for src, dst in rewrites:
            for m in re.finditer(_pat(src, dst), body):
                left.setdefault(src, []).append(p)
    print("\nVERIFY:", "clean — no old paths remain" if not left
          else f"{sum(len(v) for v in left.values())} STALE REFERENCES REMAIN")
    for src, ps in left.items():
        print(f"  {src}: {sorted(set(ps))[:4]}")
    return 0 if not left else 1


if __name__ == "__main__":
    sys.exit(main())
