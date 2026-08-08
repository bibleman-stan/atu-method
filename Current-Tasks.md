# Current Tasks — what is actually in flight

**The consolidated in-flight board.** Before this file existed, live state was split across my session todo list (which dies at compaction), [[Pending-Decisions.md]] (decisions only), `loop_health.py` output (mechanical only), and chat. Nothing held all of it, so the answer to *"what are we in the middle of?"* required reassembling it every time — and things fell through, which is how a whole-chapter hole in the Isaiah gold survived 73 days unnoticed.

**Organised by what unblocks it**, because that is the axis that matters when you open this file.

- **Updated 2026-08-08.** `loop_health.py` warns if this board goes untouched more than 14 days while commits land — a date check catches a *stale* board, not a *wrong* one, which is its honest limit.
- **Companion files**: [[Pending-Decisions.md]] holds the full argument for each decision (recommendation + why + cons); this board holds one line and a pointer. Settled things live in `memories/operational/_north_star.md` and do not appear here.

---

## 1. Waiting on you — nothing moves until you rule

| # | Decision | Where the argument lives | If you say yes |
|---|---|---|---|
| D1 | **Cross-repo loop redesign** — retire the wiki's `findings/`, wiki becomes write-protected from the field, this repo becomes loop-closer with read access to theory | [[Pending-Decisions.md]] `[2026-08-08]` | 5 execution steps, in order; includes receiving F-001 here and renaming improvement→maturation |
| D2 | **Framework §1 NOT-list** — do aural and rhetorical lenses stay excluded? | [[Pending-Decisions.md]] `[2026-08-07]` | Category B canon edit, cited from every reader repo |
| D3 | **Retraction-protocol amendment** — strikes count *distinct events*, not log entries | [[Pending-Decisions.md]] `[2026-08-07]`, defect found in [[4-process/draft-promotions-2026-08-07.md|draft-promotions-2026-08-07.md]] | One-line edit to [[4-process/retraction-log-protocol.md|retraction-log-protocol.md]]; unblocks every future promotion count |
| D4 | **Substrate loop — build the English bidirectional filter?** | [[2-evidence/finding-substrate-loop-diagnosis.md|finding-substrate-loop-diagnosis.md]] | A `Workflow` fan-out over ~503 candidate over-merges; the one unbuilt part of an otherwise complete loop |
| D5 | **Collapse to two conversation partners?** | [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] | Reader Claudes retire; readers keep independently-authored gates. Non-negotiable condition stated in the doc |

## 2. Ruled, but gated — you decided; a gate stands between the ruling and the edit

| # | Item | Ruling | What must happen first |
|---|---|---|---|
| G1 | **Non-finite predication** — allow restoring a shared subject and modal, not only a gapped finite verb | Yours, 2026-08-07 | §7.3 adversarial audit (over-merge + atomicity, as a `Workflow`), **then** yardstick measurement with the change in and out. Survivors only; each retraction logged. Detail in [[4-process/proposal-2026-08-06-criterion-reconstruction.md|proposal-2026-08-06-criterion-reconstruction.md]] |

## 3. In flight — mine, no decision needed

| # | Item | State |
|---|---|---|
| W1 | **Per-violation set-diff for validator baselines** | In progress. You ruled "build it" 2026-08-07. Turns a bare count-drift into a named list, so a baseline can be re-blessed knowingly |
| W2 | **Loop 1 commit-message gate** — refuse a canon-touching commit with no §7.5 declaration | Not started. Mechanical replacement for a self-report currently running at 24% |
| W3 | **Rule-set-vs-theory audit** — the second domino | Not started. You named it: nobody has audited the rule set against the theory, *or* the theory against the scholarship |

## 4. Known broken, not scheduled — standing failures the health check reports every session

These are real and none is currently assigned. Listed so they stop being background noise.

| Failure | Evidence |
|---|---|
| **Retraction→promotion loop has never fired** — 31 entries, 0 promotions, corpus-wide | `loop_health.py`; [[4-process/improvement-loops.md|improvement-loops.md]] Loop 2 |
| **Validator baselines dead as controls** — gnt 2026-05-21 and tanakh 2026-06-02 both predate their newest corpus commit (2026-06-13); bofm likewise | `loop_health.py`; W1 addresses the diagnosis, not the re-blessing |
| **Four readers have no retraction log** — lxx, vulgate, gnt-morph, rev-reader | `loop_health.py` |
| **Gold yardstick 69 days old** | `loop_health.py`; the outcome instrument is not being re-run |
| **Full hostile audit never recorded**, 188 moves accumulated | `loop_health.py`; run the `atu-audit-tier` skill to set the mark |
| **65 broken doc paths** | `check_broken_pointers.py`. Mostly retired-doc mentions and sibling-repo paths, but not triaged — so the number is uninformative, which is its own defect |
| **Substrate loop missing its filter** | [[2-evidence/finding-substrate-loop-diagnosis.md|finding-substrate-loop-diagnosis.md]] — D4 above |

---

## How this file stays true

1. **I update it in the same turn** a task changes state — the same discipline as file-back (standing default #5(c)).
2. **`loop_health.py` checks it** on every session start and warns past 14 days of drift.
3. **Decisions live in [[Pending-Decisions.md]]**, not here. This board points; it does not argue. When a decision resolves, it moves to that file's Resolved section and leaves this board.

## Related

- [[00-start-here.md]] — the vault map; start there if you are looking for a document rather than a task
- [[Pending-Decisions.md]] — full argument, recommendation, and cons for every open decision
- [[4-process/improvement-loops.md|improvement-loops.md]] — why these loops exist and which are measured broken
- `memories/operational/_north_star.md` — settled decisions: closed routes, banked gold, parked work
