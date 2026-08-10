#!/usr/bin/env python3
"""Fill Status / Blast radius / Blocked on / Priority across the seeded board.

Separate from seed_board.py deliberately: seeding runs once, filling runs
whenever judgements change. Matching is by title substring so the script stays
readable and survives titles being edited in the UI — a miss is reported, never
silently skipped.

Why fill before adding more fields: `Blast radius` and `Status` sat blank on all
16 items, and a board with empty columns trains you to ignore columns. That is
how Current-Tasks.md went stale in 36 hours.

    python scripts/fill_board.py --dry-run
    python scripts/fill_board.py
"""

import argparse
import json
import subprocess
import sys

GH = r"C:\Program Files\GitHub CLI\gh.exe"
PROJECT, OWNER = "1", "bibleman-stan"
PROJECT_ID = "PVT_kwHOD78t2c4Bf4iM"

FIELDS = {
    "Status":       "PVTSSF_lAHOD78t2c4Bf4iMzhaIKiw",
    "Blast radius": "PVTSSF_lAHOD78t2c4Bf4iMzhaIQ9s",
    "Blocked on":   "PVTSSF_lAHOD78t2c4Bf4iMzhaISHA",
    "Priority":     "PVTSSF_lAHOD78t2c4Bf4iMzhaISH4",
}
OPTIONS = {
    "Status": {"Todo": "f75ad846", "In Progress": "47fc9ee4", "Done": "98236657"},
    "Blast radius": {"skill": "bd1ffb90", "hook": "70572b11", "autonomous": "56492e7a"},
    "Blocked on": {"stan": "99521998", "claude": "ce3ea14b",
                   "gate": "9b50a106", "external": "f9cd716b"},
    "Priority": {"now": "0defdfee", "next": "494dfad4", "later": "3eafb413"},
}

# (title-substring, blast-radius, blocked-on, priority)
# Status is Todo for everything — nothing is in progress until it is.
PLAN = [
    ("Untrack 5 private",          "skill",      "claude",   "now"),
    ("rewrite git history",        "autonomous", "stan",     "next"),
    ("Move Pages off repo root",   "autonomous", "stan",     "next"),
    ("bypass #1",                  "hook",       "claude",   "now"),
    ("bypass #3",                  "hook",       "claude",   "now"),
    ("bypass #4",                  "hook",       "claude",   "now"),
    ("approval log against GNT",   "skill",      "claude",   "now"),
    ("approval log against BoFM",  "skill",      "claude",   "now"),
    ("1.5 GB audio",               "autonomous", "stan",     "next"),
    ("requirements phase",         "skill",      "stan",     "next"),
    ("greenfield vs new core",     "autonomous", "gate",     "next"),
    ("Pin dependencies",           "skill",      "claude",   "next"),
    ("NOT-list ruling",            "skill",      "stan",     "later"),
    ("Non-finite predication",     "autonomous", "gate",     "later"),
    ("Triage the 43 parked",       "skill",      "claude",   "later"),
    ("5-machinery",                "hook",       "gate",     "later"),
]


def sh(args):
    r = subprocess.run(args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(f"    FAILED: {(r.stderr or r.stdout).strip()[:160]}")
        return None
    return (r.stdout or "").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    raw = sh([GH, "project", "item-list", PROJECT, "--owner", OWNER,
              "--format", "json", "--limit", "100"])
    if not raw:
        return 1
    items = json.loads(raw)["items"]
    print(f"{len(items)} items on the board\n")

    done, missed = 0, []
    for frag, blast, blocked, prio in PLAN:
        hit = next((i for i in items if frag.lower() in i.get("title", "").lower()), None)
        if not hit:
            missed.append(frag)
            continue
        print(f"{hit['title'][:56]:58} {blast:11} {blocked:8} {prio}")
        if args.dry_run:
            continue
        for field, value in (("Status", "Todo"), ("Blast radius", blast),
                             ("Blocked on", blocked), ("Priority", prio)):
            sh([GH, "project", "item-edit", "--id", hit["id"],
                "--project-id", PROJECT_ID, "--field-id", FIELDS[field],
                "--single-select-option-id", OPTIONS[field][value]])
        done += 1

    print(f"\n{done}/{len(PLAN)} filled")
    if missed:
        print("NOT MATCHED (reported, not skipped silently):")
        for m in missed:
            print(f"  {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
