# Operations log

Append-only. One entry per operation, newest last. The parseable prefix
`## [YYYY-MM-DD] op | title` lets a lint pass scope itself to what changed since
it last ran — which is what makes scheduled linting affordable rather than a full
re-read. Ops: `measure` · `audit` · `propose` · `build` · `schema` · `deploy`.

Distinct from two neighbours, deliberately. `2-evidence/approval-log.jsonl`
records what the **system** decided (per-verse cases). `4-process/lessons.md`
records **corrections** awaiting promotion. This file records what **we** did.

Seeded 2026-08-09 by the session that created it. Operations before that date
were never captured and are **not** reconstructed here — an empty history is
honest; a backfilled one would be invented.

---

## [2026-08-09] audit | four commissioned audits of master-proposal-rebuild

Linguistic, repo-architecture, web/frontend, migration-cost. 130 external
sources harvested. Proposal **withdrawn** — eight inventory claims false.
Filed: `4-process/audit-*.md`, `2-evidence/external-practice.md`.

## [2026-08-09] measure | private/ exposure verified live

`.gitignore` correct in all five reader repos, but five files remain **tracked**
under `private/` and four return HTTP 200. Repos are public, so ever-committed
paths — including `colometry-canon.md` in three repos — sit in public history.
Filed: [[Pending-Decisions.md]].

## [2026-08-09] build | approval log (`scripts/decision_log.py`)

Set-diff of deployed against regenerated, per-verse rows at `status: unreviewed`.
Self-calibrating: three poles asserted in-file, refuses to report if any fails.
First detector built this session that asserts its own poles.

## [2026-08-09] measure | link density, neutral metric

atu-method 5.80 against meta-wiki 12.84 links/page (~45%). The earlier
5.54-vs-12.85 figure used a filter that penalised the comparator's link style.
Filed: `2-evidence/growth-data.csv`.

## [2026-08-09] propose | master-proposal-v3

Greenfield in `atu-method`; sites become build output; `5-machinery/` as the code
bin; log / lessons / lint as three distinct organs. First version argued from
external evidence rather than from my own reasoning.

## [2026-08-09] measure | workflow consult ingested

Stan's claude.ai session on streamlining the reader workflow, read in full.
Central critique: v3 is machinery a non-coder cannot debug. Adopted blast-radius
phasing, save/undo, visual diffs, deploy previews, version-stamped chapters,
touch-tax, rule reach. Flagged the plugin-vs-project-skills conflict.
Filed: 2-evidence/external-practice.md §9

## [2026-08-09] propose | SDLC reframe folded into v3

Stan: this matches requirements -> design -> implementation -> deployment. The
project has run implementation->deployment only. V-model makes the validator
problem exact: 75 validators with nothing on the left to verify against.
Gate 0 reframed from epistemology to requirements.

## [2026-08-09] measure | tooling corrected — GitHub Desktop is installed

I wrote "gh is not installed" in a way that implied the tooling is missing.
GitHub Desktop IS installed (AppData/Local/GitHubDesktop); gh CLI is not; git
2.53.0. Consequence: the visual-diff guardrail is already on the machine and
unused, and push is solved -- I stage, Stan reviews the diff and pushes.
Desktop has no Projects UI, so the board is still browser work.
