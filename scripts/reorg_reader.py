#!/usr/bin/env python3
"""Normalize a reader repo to the five-tier shape. One repo per run, dry by default.

Target shape, agreed 2026-08-09:

    1-method/     per-corpus canon (colometry-canon, scholarship)   [PUBLIC]
    2-evidence/   measurements, findings, draft corpora
    3-project/    deployment status, build plans, inventories
    4-process/    loops, protocols, retraction-log
    5-machinery/  scripts, validators, tests
    private/      gitignored — substrate, licensed sources
    books/ data/ index.html sw.js CNAME   ← the SERVED SITE, deliberately unnumbered

The last line is load-bearing: GitHub Pages serves from the repo root, so the
site files must stay where they are. Numbering them would break four live
domains.

WHY A SCRIPT AND NOT git mv BY HAND: the moves are the easy part. The cascade is
the path references — 12 tracked files in readers-vulgate alone name `scripts/`
or `research/`. Hand-moving produced 103 dangling citations the last time this
was attempted repo-wide, so every run repoints references and then VERIFIES no
old path survives.

    python scripts/reorg_reader.py readers-vulgate            # dry run
    python scripts/reorg_reader.py readers-vulgate --apply
"""

import argparse
import re
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
            ("scripts", "5-machinery/scripts"),
            ("research/OT-BUILD-PLAN.md", "3-project/OT-BUILD-PLAN.md"),
            ("research/SUBSTRATE-INVENTORY.md", "3-project/SUBSTRATE-INVENTORY.md"),
            ("research/dr-coverage.json", "2-evidence/dr-coverage.json"),
            ("research/lexham-v1", "2-evidence/lexham-v1"),
        ],
        "stubs": ["1-method", "4-process"],
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

BLURBS = {
    "1-method": "Per-corpus canon: colometry rules, pericope rules, scholarly "
                "grounding. Public by decision — publishing Stan's own method "
                "canon is fine; third-party licensed material is not.",
    "2-evidence": "What has been measured: findings, coverage reports, draft "
                  "corpora, comparisons against external witnesses.",
    "3-project": "Where this corpus stands: build plans, substrate inventory, "
                 "deployment state.",
    "4-process": "How the work governs itself: loops, protocols, the retraction "
                 "log.",
}

TEXT_EXT = {".md", ".py", ".json", ".html", ".js", ".txt", ".yaml", ".yml"}


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
        guard = ""
        if dst.endswith(src) and len(dst) > len(src):
            guard = f"(?<!{re.escape(dst[:-len(src)])})"
        return len(re.findall(guard + re.escape(src) + r"(?![\w-])", body))

    cases = [
        ("see 5-machinery/scripts/build.py", "scripts", "5-machinery/scripts",
         0, "a correctly-rewritten path is NOT stale"),
        ("see scripts/build.py", "scripts", "5-machinery/scripts",
         1, "a genuinely unrewritten path IS stale"),
        ("see research/old.md", "research", "2-evidence",
         1, "non-nested move still detects"),
        ("see scriptsfoo/x", "scripts", "5-machinery/scripts",
         0, "word-boundary guard holds"),
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
               if Path(p).suffix in TEXT_EXT]
    hits = {}
    for p in tracked:
        f = root / p
        try:
            body = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        n = sum(len(re.findall(re.escape(src) + r"(?![\w-])", body))
                for src, _ in rewrites)
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
        sh(root, "git", "mv", src, dst)

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
            new = re.sub(re.escape(src) + r"(?![\w-])", dst, new)
        if new != body:
            f.write_text(new, encoding="utf-8", newline="\n")

    # VERIFY: no old path may survive in a tracked text file.
    #
    # The obvious check is wrong, and its first run proved it: `5-machinery/
    # scripts` CONTAINS `scripts`, so searching for the old path matches the new
    # one and reported 24 stale references against a clean rewrite. A verifier
    # that cannot tell its own success from failure is worse than none.
    #
    # Fix: when the destination ends with the source, require the match NOT be
    # preceded by the destination's prefix.
    left = {}
    for p in sh(root, "git", "ls-files").splitlines():
        if Path(p).suffix not in TEXT_EXT:
            continue
        f = root / p
        if not f.exists():
            continue
        body = f.read_text(encoding="utf-8", errors="replace")
        for src, dst in rewrites:
            guard = ""
            if dst.endswith(src) and len(dst) > len(src):
                guard = f"(?<!{re.escape(dst[:-len(src)])})"
            for m in re.finditer(guard + re.escape(src) + r"(?![\w-])", body):
                left.setdefault(src, []).append(p)
    print("\nVERIFY:", "clean — no old paths remain" if not left
          else f"{sum(len(v) for v in left.values())} STALE REFERENCES REMAIN")
    for src, ps in left.items():
        print(f"  {src}: {sorted(set(ps))[:4]}")
    return 0 if not left else 1


if __name__ == "__main__":
    sys.exit(main())
