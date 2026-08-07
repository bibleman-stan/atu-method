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

**A protocol defect fell out of that, and it needs its own ruling.** `retraction-log-protocol.md` says "The 3 strikes need not all come from one repo," written for independent recurrences — but cascaded changes are logged in every repo by design, so pooling counts log entries rather than distinct events and can triple a single mistake. **Proposed amendment:** strikes count distinct retraction events (date + retracted claim), not log entries.

**Cons of promoting:** Promotion 1 sits adjacent to `feedback_rhetoric_figures_constrain_atu` and could be called redundant; Promotion 2 adds real friction to every rule proposal and risks the opposite failure — suppressing a needed rule because the residue looked small, which is how the six underived §2.1 allowances arose from the other direction.

---

### [2026-08-07] Repo reorganization — shape needs Stan's eye

readers-bofm reorganized to numbered, purpose-first directories at the repo root (`1-method/`, `2-evidence/`, `3-project/`) and Stan asked for the same here. The mapping is not mechanical, because atu-method has a content class BoFM does not: implementation and architecture docs that are neither canon nor evidence nor process. See the proposal in chat 2026-08-07; execution is a four-repo path cascade and waits on the tier shape being right.

---

## Resolved

*(none yet — entries move here with date and outcome)*
