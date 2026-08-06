---
name: atu-audit-tier
description: Run the atu-method machinery audit. Use on the first wake of any ISO week, on any wake after >7 days with no commit in this repo, or whenever asked to audit the repo's own discipline. Checks that cited paths and link anchors resolve, that memories are indexed, that retraction logs are alive across the reader repos, and that the standing defaults are being enacted rather than merely stored.
---

# Audit tier — the machinery that audits the machinery

**Why this exists.** On 2026-08-06 the user-home memory namespace — 57 files including `_north_star.md`, which `CLAUDE.md` called "never optional" — was discovered deleted after roughly six weeks. Three signals had been sitting in plain sight: dead mandatory-read paths in the constitution, a migration flagged "pending" in three places since 2026-06-28, and a broken-pointer detector that already existed and that no cadence ever ran.

**The generalisable lesson: the tool was never the missing piece.** That is why this audit is calendar-triggered, not activity-triggered — drift accumulates fastest when nothing is happening, so a trigger that depends on activity cannot fire during the exact window it is needed.

## Trigger

First wake of any ISO week, OR any wake after >7 days with no commit in this repo. Run it before substantive work; it is cheap.

## 1. Mechanical lint

```bash
python scripts/check_broken_pointers.py            # add --verbose for context lines
```

Validates two failure classes: cited paths that do not resolve, and link anchors (`](<file.md#Heading>)`) whose fragment no longer matches a real heading. The second class matters because anchors rot silently the moment a heading is reworded, and a link landing on the wrong section is worse than plain text.

Baseline as of 2026-08-06: **0 broken anchors, 61 broken doc paths, 81 advisory** (non-`.md`, overwhelmingly reader-repo scripts this hub cannot see — advisory, not failures). A rise in broken anchors means link rot; a rise in broken doc paths means something moved without its citers.

Then check, in order:

- **Every memory file is indexed and every index entry resolves** — `memories/_index.md` and `memories/operational/MEMORY.md` against the actual directory contents, both directions.
- **Retraction-log liveness across ALL reader repos** — the spokes are in scope; this is a hub and discipline-propagation is manual by design. Measured 2026-08-06: bofm 16 entries, gnt 10, tanakh 5, **zero `DISCIPLINE PROMOTED` blocks in any log**, all frozen 2026-05-17, and no log at this hub or in the other four repos. If that is still true, the retraction→promotion loop is still stalled — say so plainly rather than re-discovering it.
- **Staleness** — anything claiming to be "live" but unedited >60 days gets flagged, especially `docs/05-status/deployment-status.md`.

## 2. Hostile audit

One adversarial pass, written down — not vibes:

- Are the 8 standing defaults being **enacted** in recent sessions, or only stored? Read the last few sessions' commits and check for the shape, not the citation.
- Is any flagged-pending item stalled? **>2 weeks → surface it to Stan by name.** This is the check that would have caught the 2026-06-28 migration.
- Is the retraction 3-recurrence threshold actually being evaluated, or are entries just accumulating?
- Is `CLAUDE.md` over its salience budget? Measure it (`wc -c CLAUDE.md`). Note the budget is stated in lines in `feedback_lean_entry_points.md` but the real cost is bytes — the file passed the line test at 139 lines while being roughly twice the intended size. If it is over, the fix is usually moving an on-demand procedure into `.claude/skills/`, not deleting content.

## The rule that makes it worth running

**Findings convert to edits, or they recur.** A finding that ends the turn as prose is not a finding. It lands as an edit, as a `memories/operational/_deferred_queue.md` entry, or as a named Stan-facing decision. Nothing else counts.

Related: `docs/04-process/improvement-loops.md` (loop 4 is this loop, and records that it has completed zero cycles).
