# Pending Decisions — atu-method

Every decision that is Stan's to make, in one place instead of scattered through
chat. Same name and format as `atu-nlp-wiki/Pending-Decisions.md` and
`readers-bofm/Pending-Decisions.md`, so it is the same muscle memory in every repo.

**Format**: each entry states the decision, a **recommendation**, **why** that one,
and its **cons** — per `memories/operational/feedback_always_recommend_in_options.md`.
A recommendation carrying only upside is advocacy, not advice.

Resolved entries move to the bottom with their date and outcome.

---

## Open

### [2026-08-09] 🔴 LIVE EXPOSURE — `private/` content is published, and the repos are public

**Stan asked whether `.gitignore` actually hid the `private/` folders. Verified this turn: the ignore rules are correct in all five reader repos, but `.gitignore` never untracks a file that was already committed — and files were.**

**Currently tracked under `private/`, and serving HTTP 200 right now:**

| File | Site |
|---|---|
| `private/01-method/scholarship/README.md` | tanakh-reader.com |
| `private/03-sessions/2026-04-29-audit-waves/wave2-latter-prophets.md` | tanakh-reader.com |
| `private/03-sessions/2026-04-29-audit-waves/wave4-former-prophets.md` | tanakh-reader.com |
| `private/README.md` | lxx-reader.com |
| `private/README.md` | vulgate-reader.com |

**And the repos are public** — `github.com/bibleman-stan/readers-tanakh` and `readers-bofm` both return 200 unauthenticated. So **everything ever committed under `private/` is retrievable from git history**, including `private/01-method/colometry-canon.md` in the tanakh, bofm and gnt histories, plus eight GNT `private/01-method/audit-trail/*.md` files. Those return 404 on the sites — removed from HEAD — but they live in public history permanently.

**The irony worth noting:** `lxx-reader.com/private/README.md` is itself publicly served and reads *"This repo is public. Everything in `private/` is gitignored (except this README) and is never published."* The document asserting the folder is never published is proof that it is.

**Severity, stated accurately rather than alarmingly.** No credentials and no personal data are involved — the exposed material is methodology working notes and per-corpus method canon. But keeping the private method canon off public remotes is a standing project decision, and it has not held. This sits alongside the broader finding that [[CLAUDE.md]] and `Pending-Decisions.md` are served on every live domain.

**Recommendation, three parts in order:**

1. **Stop the live serving now** — `git rm --cached` the five tracked `private/` files, commit, push. Removes them from HEAD and from the sites within a Pages cycle. Cheap, reversible, no history rewrite.
2. **Fix the root cause** — move Pages off the repo root to an orphan `gh-pages` branch or Pages-from-Actions, per [[4-process/audit-repo-architecture.md|audit-repo-architecture.md]]. This is the only change that stops the *whole source tree* being published, and it fixes the [[CLAUDE.md]] exposure at the same time.
3. **Decide on history** — rewriting with `git-filter-repo` or BFG plus force-push is the only way to remove `colometry-canon.md` from public history. **This is your call, not mine.**

**Why history rewrite is genuinely optional.** GitHub's own guidance is to treat anything committed to a public repo as already compromised: clones, forks, and caches may retain it, so a rewrite reduces but does not eliminate exposure. Weigh that against the cost — force-pushing rewritten history across three repos breaks every existing clone and every commit SHA cited in the canon, and this repo's documents cite reader-repo SHAs extensively.

**Cons of acting.** Step 1 is safe. Step 2 changes the deploy path for five live sites and needs the reproducibility gate in place first, or a broken deploy will be indistinguishable from a broken build. Step 3 is destructive, invalidates cited SHAs across the documentation, and buys less protection than it appears to.

**Note on execution:** I cannot push — `readers-bofm/4-process/04-deployment-infra.md` records *"sandbox can't push — gets 403 proxy error."* I can stage steps 1 and 2 locally for you to push.

---

### [2026-08-09] DO THIS FIRST — the reproducibility gate (supersedes the architecture question)

**Four audits converged on the same conclusion: the architecture decision cannot be made yet, because we cannot regenerate what is deployed.** The migration-cost audit ran the current BoFM generator over all 15 books and diffed against the live corpus:

- **789 of 23,112 deployed lines are not reproduced by the current code**, divergence running both directions.
- **Alma and Words of Mormon are the only books at 0.0%** — the only two regenerated since 2026-06-03. Commit `726fa3a` reverted a rule and regenerated **one book of fifteen**.
- So the live reader has had a rule applied in Alma and not elsewhere **for 65 days**, undetected by 75 validators, 3 pre-commit hooks, and a "single source of truth" deployment record.
- **Cause:** the deployed corpus is not the output of any runnable program. `apply_frame_merges.py` and 16 siblings mutate `data/text-files/v2/` in place, hand-run, in an order recorded nowhere (`run_all.py` discovers only `validate_*.py`).

**This kills the behavioral-snapshot idea on the corpus that most needs it** — you cannot "capture every decision mechanically against code that already runs" when the deployed state is not that code's output. But it is survivable: **GNT reproduces 100%**, `build_book.py` reproduces deployed HTML byte-for-byte, and the generator is deterministic run-to-run. The failure is one corpus's segmentation stage, not the system.

**Recommendation: build the reproducibility gate before deciding anything architectural.** For each corpus, regenerate from source and diff against deployed; emit one integer per corpus that should be zero.

**Why this first.** It is **path-independent** — greenfield, completion, and do-nothing all need it. It costs 1–2 days. It converts the architecture question from speculation into measurement, because a corpus that cannot be regenerated cannot be migrated *or* rebuilt safely. And it has already paid for itself by finding the 789-line defect in a single session.

**Cons.** It delays the architecture decision by days (mild — nothing is burning). It will likely surface more divergence, which is discouraging and creates work that competes with the rebuild. It does not tell you *which* side of a divergence is correct — only that one exists — so each finding still needs adjudication, and without an external arbiter (Gate 0 is unresolved and te'amim are now disqualified) some may not be adjudicable at all.

---

### [2026-08-08] Greenfield rebuild, or a new core with the old parts? — THE ARCHITECTURAL DECISION

> **⚠ 2026-08-09 — the master proposal built on this entry is [[4-process/master-proposal-rebuild.md|WITHDRAWN]].** Its inventory was wrong on eight counts, including that a 62-spec YAML rule system already exists in `readers-tanakh/validators/specs/`. This entry's *question* stands; its framing of what exists does not. **Decide the reproducibility gate above first.**

Stan: *"I fear we need to blow up the current system and build a greenfield… the current system seems too complex and dysfunctional to maintain; there was not enough forethought given to the engineering design workflow; there are a lot of good pieces, but they might not be from the right LEGO sets, or at least not assembled correctly."*

**The forethought criticism is correct and I concede it without qualification.** The loops were written up on 2026-08-06 — *after* three years of accreted machinery. Nothing was designed against a workflow spec; it was assembled and then described.

**But "too complex" is not what the measurement says.** Counted 2026-08-08, excluding `.venv/`, `private/`, `_old/`, and generated `data/` (the first count returned 9,441 scripts for `readers-bofm` — all but 153 were a vendored virtualenv, a miscalibrated scan of exactly the kind this repo keeps catching):

| repo | authored .py | validators | prose .md | commits |
|---|---|---|---|---|
| atu-method | 42 | 0 | 183 | 143 |
| readers-tanakh | 101 | 27 | 66 | 447 |
| readers-bofm | 153 | 43 | 67 | 1,149 |
| readers-gnt | 118 | 3 | 47 | 607 |
| readers-lxx | 22 | 1 | 6 | 17 |
| readers-vulgate | 34 | 1 | 5 | 19 |

~470 authored scripts and ~374 prose files is a **medium** system, not a sprawling one. What is disproportionate is the **coordination surface** — 75 validators, 3 cascading [[CLAUDE.md]] files, 106 memories, 6 repos — relative to the product, which is 4 live sites.

### The actual defect: one architectural omission with six symptoms

Every dysfunction found today traces to a single missing thing — **there is no decision record**:

| symptom | how it traces back |
|---|---|
| `overrides.json`: 911 keys, **all 911 values bare lists** (verified) | no verdict, rule, adjudicator, or date — so a rule change cannot be tested against past calls |
| retraction→promotion has **never fired** in the program's history | no unit that counts as a distinct event; the protocol pools log entries instead |
| findings don't integrate (5.80 vs 12.84 links/page) | no anchor for a finding to attach to |
| validator baselines dead as controls | drift is a bare count, not a per-violation list |
| **no external arbiter** — the Isaiah oracle turned out rule-derived | never designed in; discovered by audit, not by construction |
| §7.5 declared on 24% of canon commits | the audit record is prose, not data |

That is not six problems. It is one omission, and it is exactly what a "design the workflow first" pass would have produced.

### The fact that decides greenfield-vs-rebuild

**The past decisions are already lost.** Those 911 adjudications have no verdicts to recover; the reasoning is gone. So a greenfield does not *cost* us them — and equally, **we do not need a greenfield to start recording them properly.** The clean decision layer is available either way, because it does not exist yet in either world.

Meanwhile the assets that look expensive are mostly **portable, not re-earned**: BHSA, Macula/N1904, and PROIEL→TF are external imports that re-import mechanically; the closed routes, the 14-rule Hebrew catalog, and the negative knowledge (parser training lost 21–6; genre is never a criterion; punctuation has zero force) are prose that copies. What genuinely does not port is the generators — `bofm_generate.py`, `build_books.py` — which encode instance-by-instance correctness earned over 1,149 commits, with **no live regression control**, since every baseline is stale.

**Recommendation: greenfield the CORE, not the repo — and answer the arbiter question first.**

1. **Settle the arbiter question before building anything.** Both sub-agents converged that we have no external arbiter. Candidates that are genuinely not rule-derived: Masoretic *te'amim*, Skousen's manuscript lineation, Marschall's syllable bands. **If none is adequate, no architecture fixes this** — the system would be additive by nature and should be run that way. This is cheap to answer and it gates everything.
2. **Design the decision record from scratch**, with a real contract, as the new spine. Not retrofitted onto `overrides.json`'s shape — that shape is the defect.
3. **Demote everything existing to inputs.** Substrates, corpora, rule catalogs, deployed editions become sources feeding the spine; nothing is authoritative until re-expressed as cases.
4. **The live sites keep serving off the old path** while the spine is built.

**Why this over a full greenfield:** the broken layer does not exist yet, so building it fresh costs the same either way — while a full rebuild also re-does substrate wiring, generators, and deploys that are *working*, and does it without regression control.

**Why this over "just refactor":** refactoring in place has a specific known failure — you keep the dysfunction because it is load-bearing. The record has to be designed against a contract, not grown out of what is there.

**Cons, stated plainly.**
- **I am not neutral.** I built or touched much of what I am recommending we keep, and "rebuild the core, keep my parts" is exactly what a sunk-cost defence sounds like. Weigh this accordingly.
- **Strangler-fig rebuilds stall.** The characteristic failure is two systems running forever, which is worse than either. If this is chosen it needs a date at which the old path is retired, decided in advance.
- **It does not address the coordination surface** — 3 [[CLAUDE.md]]s, 106 memories, 75 validators — which is a real part of what feels unmaintainable and would survive untouched.
- **If the arbiter question fails, step 1 is the whole answer** and steps 2–4 are wasted motion. That is a feature (it fails cheap) but it means this plan may terminate at step 1.
- **A full greenfield has one advantage this forfeits**: it forces every convention to be re-justified, and some of ours — the five-tier scheme, per-repo naming drift, the memory namespace — have never been justified at all.


### [2026-08-08] Cross-repo: retire the wiki's `findings/`, make atu-method the loop-closer — PROPOSED IN CHAT, NOT FILED ANYWHERE

Worked out in the atu-nlp-wiki session 2026-08-08 and originally **recorded here because it existed only in that session's transcript**.

> **⚠ RE-VERIFIED 2026-08-08, later the same day — the paragraph below this one is now false and is kept only as a record of what changed.** The earlier text read: *"`findings/F-001-marschall-1ne3.md` is still present, `admin/maturation-loops.md` was never created."* Both clauses have since flipped. Re-checked in this turn: `ls -d findings` → **GONE**; `ls -la admin/maturation-loops.md` → **exists, 6,493 bytes, Aug 8 11:25**. The wiki session **executed D1 while this entry sat here claiming it hadn't.** Flagged independently by two sub-agents.
>
> **What this means for the decision:** D1 is no longer a proposal awaiting ratification on the wiki side — it is already done there, and this repo has not caught up. What remains open is *our* half: receiving F-001 into `2-evidence/`, redrawing Loop 5, the improvement→maturation rename, recording the loop-closer role, and the re-adjudication obligation. **It also demonstrates the exact failure it describes**: a dated verification claim about another workspace went stale within hours, and nothing here would have noticed.

**Stan's alternative, which that session judged better than its own proposal:** the wiki keeps improving from `raw/` alone and is **write-protected from the field entirely**; atu-method gets **read access** to the theory and becomes "the end of the loop on the measuring/modifying side." Two inputs to the wiki, no others: `raw/` (Stan curates) and synthesis grounded in `raw/`.

**Why it beats the `findings/` exception:** self-containment is the wiki's trust anchor; `findings/` was a hole in it and ratifying it would have legalized the hole. This removes the hole instead. It also gives the orphaned **findings→canon** edge an owner — that session's words: atu-method "is the one layer with read access to both the theory and the measurements," so carrying a measurement into a rule change "is atu-method's job."

**Third path, layered rather than competing:** a measurement that matures to publication rigor is admitted to `raw/` as an immutable source, needing no exception. Bar = the circularity guard: measured against an external standard, provenance-pinned and reproducible, scope-adequate, and **disconfirming findings admissible on equal footing**. F-001 fails it today (`status: pilot`, one chapter). Their framing: "a high bar with an empty shelf beats a low bar with a leak."

**If ratified, what changes here:**
1. Receive F-001 into `2-evidence/` (explicitly left for cross-repo coordination, i.e. this repo).
2. Redraw Loop 5: the findings→theory edge **disappears** — field measurements never reach the wiki directly. Replaced by atu-method reading the wiki read-only and adjudicating locally, plus a `raw/`-graduation edge gated by Stan.
3. Rename `4-process/improvement-loops.md` → maturation. *Improvement* implies monotonic accretion; the thesis matures by narrowing, retracting, and letting go, and the wiki's Purpose forbids the accretion reading ("adjudicate, **not** accrete support"). Four of six loops in that document are reported broken — that is maturation, not improvement.
4. Record atu-method's assigned role as loop-closer.
5. Add the **re-adjudication obligation**: a thesis-lens shift stales every adjudication made under the old lens. The wiki's version sweeps its Confirms/Collides; **ours is the rule-set audit** — rules derived under "syntactic closure is sole arbiter" go stale wholesale if the criterion moves to breath-bounded chunks. Same obligation, two sides.

**Recommendation: ratify, then execute 1–5 in that order.** *Why:* it dissolves a constitutional problem rather than patching it, assigns the one edge that had no owner, and keeps the wiki's trust anchor intact. *Cons:* the wiki and atu-method will diverge on purpose — the wiki's thesis page will keep saying the grain is right while this repo knows the deployed grain runs coarse — and someone must keep straight which layer is which. It also leaves the wiki showing **no** field evidence until something graduates, which is honest but looks empty.

**Also:** that session cites `atu-method/docs/04-process/improvement-loops.md`; there is no `docs/` since the 2026-08-07 reorg. Tell them.


### [2026-08-07] Framework §1's NOT-list — do the aural and rhetorical lenses stay excluded?

`1-method/framework.md` §1 says the apparatus does NOT "produce typography or oral-delivery markup" and does NOT "reveal rhetorical parallelism." Stan's 2026-08-06 correction — *"the whole point of colometry is to SHOW how the different types of cola (rhetorical, aural, cognitive) reveal the meaning and sense"* — names both of those as in scope.

**Recommendation:** amend the NOT-list to distinguish *what the apparatus reveals* from *what licenses a break*.

**Why:** the two lists are currently conflated. Rhetoric and prosody can be things the edition surfaces without being things that determine ATU boundaries — that is exactly the licensor / constraint / witness / candidate-generator distinction already in use for te'amim. Keeping the exclusion as written contradicts what Stan says the edition is for; deleting it wholesale would let rhetoric back in as a determinant, which the §2.2:116 firewall forbids for good reason.

**Cons:** any edit to §1 is a scope claim, Category B by §7.0's own diagnostic, and §1 is cited from every reader repo's canon. It also risks reopening the "rhetoric bandwagon" failure the canon has fought repeatedly — a NOT-list is a cheap defence and a nuanced replacement is a more expensive one to maintain.

---

### [2026-08-07] Non-finite predication — RULED, execution gated

**Stan's ruling (2026-08-07): allow restoring a shared subject and modal, not only a gapped finite verb.**

This governs the §2.1 reconstruction in `4-process/proposal-2026-08-06-criterion-reconstruction.md`: three of six allowances fail forward-closure only because non-finite material cannot be restored under the current §2.2(ii) wording.

**What must happen before any canon edit** — not optional, and not yet done:
1. A §7.3 adversarial audit (over-merge and atomicity lenses, dispatched as a Workflow). Retiring or rewriting live allowances is trigger #5; the register extension is trigger #1/#4.
2. Measurement against the BoFM gold yardstick with the change in and out.
3. Only survivors of both get applied, each retraction logged.

**Cons of the ruling, recorded so they are not lost:** it loosens the objectivity guarantee §2.2's quarantine exists to protect, makes the corpus finer everywhere including sermon and Isaiah passages where the yardstick already says we over-split, and cascades into every reader repo's rule catalog. Expensive to reverse after regeneration.

---

### [2026-08-07] The four validator regressions in readers-bofm

`rule_12` +2, `rule_15` +3, `rule_19` +10, `rule_29` +1 above a baseline last captured 2026-05-29. **Stan's decision: build the per-violation set-diff first** — in progress.

Corpus-wide context from `loop_health.py`: every reader's baseline is stale against its own corpus (bofm 2026-05-29 vs 2026-08-06; gnt 2026-05-21 vs 2026-06-13; tanakh 2026-06-02 vs 2026-06-13). The regression gate has stopped controlling everywhere, not just in BoFM.

---

### [2026-08-07] Retraction promotions — TWO drafted, awaiting review

Drafts ready in [`4-process/draft-promotions-2026-08-07.md`](4-process/draft-promotions-2026-08-07.md). **Stan's decision: draft for review, do not auto-promote.** These would be the loop's first firing in the program's history.

**Corrected count.** I first reported four qualifying sub-patterns. Extracting the actual `Sub-pattern:` fields rather than grepping strings shows **two** qualify — `rhetorical-figure smuggling` (3 distinct events) and `new-rule reflex` (3). The other two were a single cascaded canon change logged in three repos, citing the same atu-method commits.

**A protocol defect fell out of that, and it needs its own ruling.** [[4-process/retraction-log-protocol.md|retraction-log-protocol.md]] says "The 3 strikes need not all come from one repo," written for independent recurrences — but cascaded changes are logged in every repo by design, so pooling counts log entries rather than distinct events and can triple a single mistake. **Proposed amendment:** strikes count distinct retraction events (date + retracted claim), not log entries.

**Cons of promoting:** Promotion 1 sits adjacent to `feedback_rhetoric_figures_constrain_atu` and could be called redundant; Promotion 2 adds real friction to every rule proposal and risks the opposite failure — suppressing a needed rule because the residue looked small, which is how the six underived §2.1 allowances arose from the other direction.

---

### [2026-08-07] Repo reorganization — shape needs Stan's eye

readers-bofm reorganized to numbered, purpose-first directories at the repo root (`1-method/`, `2-evidence/`, `3-project/`) and Stan asked for the same here. The mapping is not mechanical, because atu-method has a content class BoFM does not: implementation and architecture docs that are neither canon nor evidence nor process. See the proposal in chat 2026-08-07; execution is a four-repo path cascade and waits on the tier shape being right.

---

## Resolved

*(none yet — entries move here with date and outcome)*
