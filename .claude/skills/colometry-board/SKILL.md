---
name: colometry-board
description: Operate the colometry-project GitHub Project board — add, update, and query items. Fires on "add this to the board", "update the board", "what's on the board", or any request to track work in the Project.
---

# colometry-board — operating contract

**What this is.** The minimum needed to *act* on the board without re-deriving it. Not a documentation dump — GitHub's docs are the docs. This holds the facts that are ours, the constraints that bite, and the commands that work.

**Provenance, because standing default #7 applies to me here.** Written 2026-08-09 from: GitHub Docs "Using the API to manage Projects" (fetched), the `gh project` manual pages and the GitHub CLI GA post (searched), and the Zornek transcript at `work/whispersync/transcripts/`. **I have NOT run any `gh project` command** — `gh` is not installed. Everything marked *[unverified]* below is from docs and must be confirmed on first real use, then this file corrected.

---

## The board

| | |
|---|---|
| Owner | `bibleman-stan` (**user**-level, not org) |
| Number | **1** — `github.com/users/bibleman-stan/projects/1` |
| Name | `colometry-project` |
| Visibility | private (the six repos it points at are public) |

**Why it is named for colometry and not ATU:** colometry is the deliverable; ATU is the contested explanation of it, and `framework-claim-inventory.md:38` types its hinge claim `[UNPROVEN]`. Full reasoning in [[Pending-Decisions.md]].

## The hard constraint that shapes everything

**Projects v2 is GraphQL-only. There is no REST API.** And from the docs, verbatim:

> "You cannot add and update an item in the same call. You must use `addProjectV2ItemById` to add the item and then use `updateProjectV2ItemFieldValue` to update the item."

So every item costs **1 + N calls** (add, then one per field). Fifteen seed items with three fields each is ~60 mutations. **Batch deliberately; do not design a flow that assumes one-call-per-item.**

## Auth

Scopes: **`read:project`** to query, **`project`** to mutate.

```
gh auth status                 # check what you have
gh auth refresh -s project     # add the mutation scope
```

`gh` is **not installed** as of 2026-08-09 (verified: not on PATH, not in the standard Windows install dirs). Until it is, the board is browser-only and I can draft item text but not create items.

## ⚠ CORRECTED 2026-08-09 on first real use

**`gh` 2.97.0's `item-edit` takes IDs ONLY.** The claim below that recent `gh` accepts fields and options *by name* came from a search result and is **false for this version** — `gh project item-edit --help` lists `--field-id`, `--project-id`, `--single-select-option-id` and no name equivalents. So the ID table is required, not a fallback.

**Resolved IDs — stable, recorded so they are never re-derived:**

```
PROJECT_ID   PVT_kwHOD78t2c4Bf4iM
Corpus       PVTSSF_lAHOD78t2c4Bf4iMzhaIO78
  tanakh 946ed6ed · bofm 841b8a6b · gnt 2c474d67 · lxx 0b9bc4b7
  vulgate 81823e00 · cross f77f9cc4 · none ff3a1117
Phase        PVTSSF_lAHOD78t2c4Bf4iMzhaIQ80
  requirements 092b59be · design edbbff64 · implementation 999dae30 · deployment 707b1f31
Blast radius PVTSSF_lAHOD78t2c4Bf4iMzhaIQ9s
  skill bd1ffb90 · hook 70572b11 · autonomous 56492e7a
Status       PVTSSF_lAHOD78t2c4Bf4iMzhaIKiw
  Todo f75ad846 · In Progress 47fc9ee4 · Done 98236657
```

Live copy in `scripts/seed_board.py`. Re-query with:
`gh api graphql -f query='{user(login:"bibleman-stan"){projectV2(number:1){id fields(first:30){nodes{... on ProjectV2SingleSelectField{id name options{id name}}}}}}}'`

**Verified working:** `field-list`, `field-create --data-type SINGLE_SELECT --single-select-options`, `item-create --format json` (returns the item id), `item-edit --id --project-id --field-id --single-select-option-id`, `item-list --format json`. **Board seeded with 16 items, 0 missing field values.**

**Note the auth gap this exposed:** `gh auth login` grants `gist, read:org, repo, workflow` — **not** `project`. `gh auth refresh -s project` is a required separate step, and without it the failure is a permissions error that does not name the missing scope.

## Commands *[the by-name claim below is superseded — see the correction above]*

```
gh project field-list   1 --owner bibleman-stan
gh project item-list    1 --owner bibleman-stan
gh project item-create  1 --owner bibleman-stan --title "..." --body "..."
gh project item-add     1 --owner bibleman-stan --url <issue-or-pr-url>
gh project item-edit    1 --owner bibleman-stan --url <url> \
                          --field "Corpus" --value "bofm"
gh project item-archive 1 --owner bibleman-stan --id <item-id>
```

**The one that saves real work:** recent `gh` lets `item-edit` and `item-list` reference fields and single-select options **by name** rather than by opaque node ID. If `--field "Status" --value "Todo"` fails, the `gh` build is too old and the GraphQL path below is needed instead.

## GraphQL fallback, if `gh` is too old

```
# project id
user(login:"bibleman-stan"){ projectV2(number:1){ id } }
# field + single-select option ids
node(id:"<PROJECT_ID>"){ ... on ProjectV2 { fields(first:20){ nodes {
  ... on ProjectV2FieldCommon { id name }
  ... on ProjectV2SingleSelectField { id name options { id name } } } } } }
```
Mutations: `addProjectV2DraftIssue` · `addProjectV2ItemById` · `updateProjectV2ItemFieldValue` (single-selects take `singleSelectOptionId`, not the label).

**If IDs are ever needed, record them here on first lookup** — they are stable, opaque, and expensive to re-derive.

## Our field vocabulary — what the values mean

| Field | Values | Meaning |
|---|---|---|
| `Corpus` | tanakh · bofm · gnt · lxx · vulgate · cross · none | `cross` = spans corpora; `none` = tooling/process, no corpus |
| `Phase` | requirements · design · implementation · deployment | Stan's SDLC framing. **`requirements` is the phase this program never had** — items there define what correct output *is*. |
| `Blast radius` | skill · hook · autonomous | Sequencing rule: ship in that order. A bad skill makes an ignorable suggestion; a bad hook blocks every session. |
| `Rules version` | number | For version-stamping chapters against the rules version they were built under. |

## What belongs on the board, and what does not

**Board:** items whose *status changes* — the rework/stale queue, per-corpus migration phase, adjudication backlog from the approval log, remediation steps.

**`Pending-Decisions.md`:** decisions needing an *argument* — recommendation, why, cons. Prose, not a card.

**If the same thing lands in both, one will rot.** That is the failure this board exists to fix, so do not recreate it.

## Gotchas found the hard way

- **The 2023 Zornek video says "Item added to project" is off by default. It ships ON**, configured to `Status: Todo`. Its trigger filter reads `issue, pull request` — **draft items may not be covered**, so a typed row can land with no status.
- **A view grouped by Repository is empty until items become issues.** Draft items have no repo. Expected, not a bug.
- **Leave "Auto-add to project" OFF** until there are issues worth bulk-importing; it pulls everything matching a filter.
- **`Current-Tasks.md` is the seed for this board and is retired once the board is live** — not maintained alongside it.

## First real use — do this, then correct this file

1. `gh auth status`, then `gh auth refresh -s project` if needed.
2. `gh project field-list 1 --owner bibleman-stan` — confirms auth, the project number, and the field names actually created.
3. Try one `item-edit` with `--field`/`--value` by name. If it works, delete the GraphQL section as unnecessary. If it fails, record the `gh` version and the IDs.
4. **Strike the *[unverified]* marks on whatever ran.**
