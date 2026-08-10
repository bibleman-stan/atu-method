#!/usr/bin/env python3
"""Seed the colometry-project board from the consolidated backlog.

Exists because Projects v2 imposes a constraint that makes hand-typing wasteful
and scripting awkward in equal measure — from GitHub's own docs:

    "You cannot add and update an item in the same call."

So every item costs 1 + N calls: one `item-create`, then one `item-edit` per
field. Fifteen items with two fields each is 45 round-trips. That is a script's
job, not a person's.

Source of the items: Current-Tasks.md, which consolidated the eight surfaces
where pending work was hiding. This is the same list, typed once, in the shape
the board wants.

    python scripts/seed_board.py --dry-run
    python scripts/seed_board.py
"""

import argparse
import json
import subprocess
import sys

GH = r"C:\Program Files\GitHub CLI\gh.exe"
PROJECT, OWNER = "1", "bibleman-stan"

# Resolved 2026-08-09 via `gh api graphql`. gh 2.97.0's `item-edit` takes IDs
# ONLY — there is no by-name support, contrary to what the skill file first
# claimed on the strength of a search result. These IDs are stable; recorded
# here so they are never re-derived.
PROJECT_ID = "PVT_kwHOD78t2c4Bf4iM"
FIELDS = {
    "Corpus":       "PVTSSF_lAHOD78t2c4Bf4iMzhaIO78",
    "Phase":        "PVTSSF_lAHOD78t2c4Bf4iMzhaIQ80",
    "Blast radius": "PVTSSF_lAHOD78t2c4Bf4iMzhaIQ9s",
    "Status":       "PVTSSF_lAHOD78t2c4Bf4iMzhaIKiw",
}
OPTIONS = {
    "Corpus": {"tanakh": "946ed6ed", "bofm": "841b8a6b", "gnt": "2c474d67",
               "lxx": "0b9bc4b7", "vulgate": "81823e00", "cross": "f77f9cc4",
               "none": "ff3a1117"},
    "Phase": {"requirements": "092b59be", "design": "edbbff64",
              "implementation": "999dae30", "deployment": "707b1f31"},
    "Blast radius": {"skill": "bd1ffb90", "hook": "70572b11",
                     "autonomous": "56492e7a"},
    "Status": {"Todo": "f75ad846", "In Progress": "47fc9ee4",
               "Done": "98236657"},
}

# (title, corpus, phase)  — body is added for the ones that need context.
ITEMS = [
    ("Untrack 5 private/ files still served on 4 live domains", "cross", "deployment",
     "Verified 2026-08-09: .gitignore is correct but never untracked files committed "
     "before it. 4 return HTTP 200. Repos are public, so history retains the rest."),
    ("Decide: rewrite git history to purge colometry-canon.md?", "cross", "deployment",
     "Present in tanakh/bofm/gnt history. GitHub's guidance is to treat anything "
     "committed to a public repo as compromised, so a rewrite reduces but does not "
     "eliminate exposure — and it breaks every clone and every cited SHA."),
    ("Move Pages off repo root (stops publishing the source tree)", "cross", "deployment",
     "Root CNAME per repo means GitHub Pages serves the whole working tree — "
     "CLAUDE.md and scripts/ included. Orphan gh-pages branch or actions/deploy-pages."),
    ("Fix Gate 10 bypass #1 — citation allowlist is a finite list", None, "implementation",
     "HIGH, parked since ~2026-06 in _deferred_queue.md, never surfaced. Misses any "
     "§-number outside [12], binding-rules-*.md, apparatus/substrate/toolset docs."),
    ("Fix Gate 10 bypass #3 — file-edit regex misses Write", None, "implementation",
     "HIGH. Enumerates Edit.*bofm_v1_fabric.py; misses Write (different param), new "
     "helper modules, and one-line import edits."),
    ("Fix Gate 10 bypass #4 — paraphrase passes the verbatim demand", None, "implementation",
     "HIGH. No mechanical paraphrase detector; a paraphrase threading the firewall's "
     "key tokens passes self-attestation."),
    ("Run approval log against GNT (expect 0 divergences)", "gnt", "design",
     "scripts/decision_log.py, calibrated on 3 poles. GNT reportedly reproduces 100%."),
    ("Run approval log against BoFM (expect ~789 divergences)", "bofm", "design",
     "789 of 23,112 deployed lines not reproducible. Alma + Words of Mormon are the "
     "only books at 0.0% — the only two regenerated since 2026-06-03."),
    ("Decide: 1.5 GB audio exceeds the 1 GB Pages ceiling", "bofm", "deployment",
     "239 tracked MP3s, repo is 2.1 GB. Not build output, not regenerable. Needs "
     "release assets, an external host, or LFS."),
    ("Write the requirements phase — what is good colometry?", "cross", "requirements",
     "The phase this program never had. Naming the deliverable colometry rather than "
     "ATU makes the acceptance criterion answerable: measurable against Skousen, "
     "Marschall, the Masoretic tradition and reader use."),
    ("Decide: greenfield vs new core", "cross", "design",
     "v1 withdrawn (8 false inventory claims). v3 recommends greenfield with proven "
     "artifacts copied in. Gated on the reproducibility runs above."),
    ("Pin dependencies + back up the 1.87 GB substrate offsite", "cross", "design",
     "Zero lockfiles across five repos; use('etcbc/bhsa') unpinned. A baseline whose "
     "inputs can move proves nothing. Substrate is on one disk with no offsite copy."),
    ("Framework §1 NOT-list ruling", "cross", "requirements",
     "Do the aural and rhetorical lenses stay excluded? Category B canon edit, cited "
     "from every reader repo."),
    ("Non-finite predication — §7.3 audit + yardstick", "cross", "implementation",
     "Ruled by Stan 2026-08-07: allow restoring a shared subject and modal. Gated on "
     "an adversarial audit and yardstick measurement with the change in and out."),
    ("Triage the 43 parked items in _deferred_queue.md", "cross", "requirements",
     "Untouched since 2026-08-07, content dating to ~2026-06. Contains the three HIGH "
     "Gate 10 bypasses above, BHSA-canon migration, binding-engine extraction."),
    ("Create 5-machinery/, move scripts+tests, repoint the SessionStart hook", None,
     "design",
     "Stan's fifth-folder ask. atu_method/ cannot move yet — three reader repos import "
     "it by path and the fixes cannot be pushed from the sandbox."),
]


def run(args, dry):
    if dry:
        print("  would run:", " ".join(args[1:]))
        return None
    r = subprocess.run(args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(f"  FAILED: {(r.stderr or r.stdout).strip()[:200]}")
        return None
    return (r.stdout or "").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ok = 0
    for title, corpus, phase, *rest in ITEMS:
        body = rest[0] if rest else ""
        print(f"\n{title}")
        out = run([GH, "project", "item-create", PROJECT, "--owner", OWNER,
                   "--title", title, "--body", body, "--format", "json"], args.dry_run)
        if args.dry_run:
            continue
        if not out:
            continue
        try:
            item_id = json.loads(out)["id"]
        except Exception as e:
            print(f"  could not read item id: {e}")
            continue
        # Second and third calls — the docs' add-then-update constraint.
        for field, value in (("Corpus", corpus), ("Phase", phase)):
            if not value:
                continue
            run([GH, "project", "item-edit", "--id", item_id,
                 "--project-id", PROJECT_ID, "--field-id", FIELDS[field],
                 "--single-select-option-id", OPTIONS[field][value]], False)
        ok += 1
        print("  created")

    print(f"\n{ok}/{len(ITEMS)} items created")
    return 0


if __name__ == "__main__":
    sys.exit(main())
