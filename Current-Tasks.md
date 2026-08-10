# Current Tasks — the one place

> **Plain-language version.** Stan: *"the problem has been you have had lots of places to hide the pending things; if there's only one place to look, I'll be able to catch up."* He is right. Pending work was spread across **eight** surfaces. This file now consolidates all of them, and it is the **seed for the GitHub Project board** — when that exists, this file is retired rather than maintained alongside it.

**Rebuilt 2026-08-09.** The previous version went stale in 36 hours while I was working in the repo — 21 commits behind, and reported `ok` by a staleness check calibrated to 14 days. Both are now fixed; the check triggers on commit drift.

---

## Where things were hiding, and what happened to each

| Surface | Items | Disposition |
|---|---|---|
| [[Pending-Decisions.md]] | 10 open | **Stays.** Decisions needing an argument — recommendation, why, cons. Titles only below. |
| `Current-Tasks.md` (old) | 9 rows | **Replaced by this file.** |
| [[4-process/lessons.md]] | 5 unpromoted | **Stays.** Capture buffer; promotion is a separate act. |
| `loop_health.py` output | 11 warnings | **Listed below.** Runs at every session start. |
| `memories/operational/_deferred_queue.md` | **43** | **Pointer below — NOT triaged today.** Untouched since 2026-08-07; content dates to ~2026-06. |
| `4-process/audit-*.md` | 4 files | Summarised into decisions; **individual findings not itemised**. |
| My session todo list | 6 | **Folded in below.** It dies at compaction and you could never see it. |
| Commit messages | **6,120 words today** | The worst one. Findings, corrections and caveats went into a channel you do not read. **Stopping.** |

---

## 1. 🔴 Live — unresolved right now

| | What | Where |
|---|---|---|
| L1 | **`private/` files served publicly** on four domains; repos are public, so history retains the rest | [[Pending-Decisions.md]] |
| L2 | **Three HIGH gate-bypass findings** parked since ~2026-06 and never surfaced — Gate 10's citation allowlist is a finite list, its file-edit regex is enumerable, and a paraphrase passes its "verbatim" demand | [[memories/operational/_deferred_queue.md|_deferred_queue.md]] |
| L3 | **BoFM: a rule applied to one book of fifteen for 65 days**; 789 of 23,112 lines unreproducible | [[Pending-Decisions.md]] |
| L4 | **1.5 GB of audio over GitHub's 1 GB Pages ceiling**; the `readers-bofm` repo is 2.1 GB | audit-repo-architecture |

**L2 is the one that should sting.** I spent today asking whether our validators can be trusted while three HIGH-severity findings about gate bypasses sat unread in a file I had access to the whole time.

## 2. Waiting on you

Ten open entries in [[Pending-Decisions.md]], each with recommendation / why / cons. Titles only, so this stays scannable:

1. **GitHub Project** — set one up to corral the repos *(new today)*
2. **Live exposure** — untrack `private/`, move Pages off the repo root, decide on history rewrite
3. **Reproducibility gate first** — before any architectural decision
4. **Greenfield vs new core** — the architecture question *(v1 withdrawn; v3 recommends greenfield)*
5. **Cross-repo loop redesign (D1)** — the wiki already executed its half; ours is undone, and F-001 now has no home
6. **Framework §1 NOT-list** — do the aural and rhetorical lenses stay excluded?
7. **Non-finite predication** — ruled by you, gated on a §7.3 audit plus yardstick
8. **Four validator regressions** — set-diff in progress
9. **Retraction protocol amendment** — count distinct events, not log entries *(promotions denied)*
10. **Repo reorganisation shape** — largely overtaken by the greenfield question

## 3. Mine — in flight, no decision needed

| | What | State |
|---|---|---|
| W1 | Per-violation set-diff for validator baselines | in progress |
| W2 | Loop 1 commit-message gate requiring a §7.5 declaration | not started |
| W3 | Rule-set-vs-theory audit — the second domino | not started |
| W4 | §7.3 audit + yardstick before any §2.1 canon edit | blocked on 7 above |
| W5 | Run the approval log across every corpus | ready — `scripts/decision_log.py`, calibrated |

## 4. Known broken — reported every session, unassigned

Retraction→promotion has **never fired** (31 entries, 0 promotions) · validator baselines dead as controls in gnt and tanakh · **four readers have no retraction log** · gold yardstick 69 days old · full hostile audit never recorded, 188 moves accumulated · 59 broken doc paths · substrate loop missing its filter · **this file was 20 commits behind** *(now fixed)*.

## 5. Lessons captured, not promoted

Five in [[4-process/lessons.md]], each with a candidate rule: proxy-trust · a detector is a claim, assert both poles in the script · do not propose what the repo already tried · do not architect from an uninventoried system · write the thing, not about the thing. **Promotion is the audit's job and your ratification.**

## 6. Parked — 43 items, honestly not triaged

[`memories/operational/_deferred_queue.md`](memories/operational/_deferred_queue.md) — untouched since 2026-08-07, content dating to ~2026-06. Contains the L2 gate bypasses above, the BHSA-canon migration, binding-engine extraction, cross-verse BoFM classes, and pointer-integrity findings. **I did not read all 43 today and am not pretending otherwise.** Triaging this queue is itself a task.

---

## How this file stays true

1. **It is the seed for the board, not a permanent fixture.** When the GitHub Project exists, this file is retired — not maintained in parallel.
2. **`loop_health.py` now warns on commit drift**, not a 14-day clock that never fired.
3. **Findings go in files, not commit messages.** 6,120 words in one day went somewhere you do not read.
