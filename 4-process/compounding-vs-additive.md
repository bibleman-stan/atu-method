---
cssclasses:
  - wide
---

# Compounding vs additive — what our loops actually are

> **Plain-language version.** Stan asked whether I actually understand the Karpathy-inspired "compounding artifact" in `meta-wiki`, because the maturation-loops diagrams did not feel right. I read the source. The key idea is that **some loops compound and some merely add up** — and a loop that merely adds up eventually plateaus, which is fine, but it will never make the system smarter. My first draft of this page claimed our loop documents had missed that distinction. Checking showed one of them had it and the other didn't, so that claim is retracted below rather than quietly fixed. What survives is sharper: we have a layer here that *could* compound, a prior ruling that wrote it off, and a measurement showing we file findings without folding them into what we already wrote.

**Written 2026-08-08** after reading `meta-wiki/wiki/`: `meta-wiki/wiki/compounding-artifact.md`, `meta-wiki/wiki/ops-improvement-loop.md`, `meta-wiki/wiki/schema-layer.md`, `meta-wiki/wiki/lint-workflow.md`, `meta-wiki/wiki/drift.md`, `meta-wiki/wiki/growth-curve.md`.

---

## 1. How the compounding artifact works

Four loops, all depositing back into **one** artifact:

| Loop | What it does | Output goes |
|---|---|---|
| **A — knowledge** | ingest → query → file back | into the wiki |
| **B — lint** | defects, gaps, orphans, stale claims | into A, as questions and source hunts |
| **C — schema** | friction → human-promoted amendment | into the maintainer itself |
| **D — horizon** | purpose-built tools; eventually weights | into capability |

The engine is **integration, not aggregation**. Ingest does not file a document for later retrieval — it *integrates*: updating the pages that already exist, revising summaries, flagging where new data contradicts old claims. Queries then start from pre-built synthesis instead of re-deriving it. That is the whole mechanism; plain accumulation produces nothing.

**The compound-interest mapping** (Stan's own framing, in that vault):

1. **File-back = dividend reinvestment.** An answer that dies in chat is a dividend spent.
2. **The schema is the interest rate.** Loop A grows the principal; loop C raises the rate *every future deposit compounds at* — which is why practitioners rank the schema file above any content page.
3. **Drift = negative interest.** An unmaintained wiki is not paused; it is bleeding.
4. **Integration is the deposit; aggregation earns nothing.** Append-only accumulation is the trap.
5. **The account is portable** — every loop's state is markdown.

**Why the flywheel does not stall:** human wikis die because maintenance grows faster than value. LLM bookkeeping is near-free, so upkeep never eats the compounding.

**The one failure bearing:** the cycle self-improves *only if loop B actually runs*. The loops are positive feedback, so they amplify whatever is present — including errors. Skip lint and **the compounding does not merely slow; it reverses.**

---

## 2. How it should interact with this project — and what I got wrong

**The meta-wiki has a page for exactly our case:** `meta-wiki/wiki/ops-improvement-loop.md` describes a log/lessons ops pattern — corrections → rules and guards — and its verdict is blunt:

> it is **additive, not compounding** … closing one error-class here does not make the next cheaper — reliability accrues without accelerating … calling it a "compounding artifact" would be the wrong shape, which is why the name is avoided.

**RETRACTED, same day, before this page was presented.** My first draft said [[4-process/improvement-loops.md|improvement-loops.md]] "never names that shape, which is the real defect Stan felt." That is false, and I asserted it about a document in this repo without re-reading it — a negative claim about an artifact, which is the highest verification bar my own standing rules set. What that document actually contains: the shape named in its Summary ("**additive, not compounding** — closing one rule-class does not make the next cheaper"); a dedicated section *The shape — additive, with one unmeasured channel*; the explicit line "Calling it a 'compounding artifact' would be the wrong shape"; a section *Why this is not a wiki's virtuous cycle*; and a History note recording that it was written **against** the traps `meta-wiki/wiki/ops-improvement-loop.md` had to audit out of its own draft. It is better aligned with the source than my critique of it was.

**What actually holds after checking:**

- [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] contains **zero** mentions of additive or compounding. The shape framing lives in one document and did not carry into the other — and the second is the one Stan was reading when he said the loops felt wrong.
- The shape is named at the **document** level but not at the **per-loop** level: the six loop frames and their diagrams are drawn identically, so nothing on the page tells you which loops plateau and which could accelerate.
- **My real disagreement is with a different claim.** That document argues *"there is no ingest loop and no source-fidelity lint"* because the canon is normative and authored. I now think that is wrong, and it is the load-bearing error. We do have an immutable layer — the corpora and external instruments — and we do have a source-fidelity lint: the Isaiah oracle measures our output against Hebrew-anchored gold and returned F1 0.561. Segmentation claims are not purely normative; they are checkable against sources. Ruling out the ingest/lint analogy ruled out the one loop in this project that could genuinely compound.

**But the project also has a genuine compounding layer available, and we are not running it as one.** The three-layer architecture maps cleanly:

| Wiki layer | Ours |
|---|---|
| immutable `raw/` | the corpora and external scholarship — BHSA, Macula, Skousen, Marschall, the Hebrew edition |
| compiled pages | `1-method/` canon, binding-rule catalogs, `2-evidence/` findings |
| capture buffer | retraction logs, `memories/` |
| schema | [[CLAUDE.md]] |

Findings about how language segments *should* compound: each measurement ought to make the next question cheaper. **They do not, because we aggregate them.**

### The evidence — measured, not asserted

`scripts/growth_snapshot.py` ports the meta-wiki instrument. Its key choice of metric is the contribution: **links-per-page, not pages.** Page count tracks effort; link density tracks integration.

| | atu-method | meta-wiki (2026-07-18) |
|---|---|---|
| pages | 61 | 46 |
| **links per page** | **5.54** | **12.85** |
| words per page | 1,907 | ~525 |
| orphans | 0 | 0 |
| schema chars | **18,410** | 9,497 |

Our density is **43% of theirs**, our pages are **3.6× longer**, and our constitution is **nearly twice the size with no budget**. Rising words-per-page is the named signature of the append-only trap. *One snapshot is a baseline, not a curve — interpretation begins around five rows — and some of the page-length gap is genre, since [[1-method/framework.md|framework.md]] is a specification and their pages are synthesis notes. The direction is still the direction.*

### Verified: the findings did not integrate

- [[2-evidence/finding-isaiah-cross-corpus-divergence.md|The Isaiah finding]] (34% divergence) **never updated** [[3-implementation/substrate.md|substrate.md]]'s fabric-parity tiers or [[2-evidence/framework-claim-inventory.md|framework-claim-inventory.md]]'s hinge claim. Zero mentions in the latter.
- [[4-process/improvement-loops.md|improvement-loops.md]] records that the finding *was filed* — the deposit — but not what it *says*.
- Worst: [[2-evidence/finding-substrate-loop-diagnosis.md|today's substrate diagnosis]] directly refutes Gap 3's claim that there is "no measure," **and Gap 3 still stood** hours later. I created a live contradiction between two pages in this repo and could not see it, because I agreed with the new claim.

That last one is the meta-wiki's **drift variant 1** (cross-reference drift), produced by me, the same day, in the document that exists to catch drift.

---

## 3. What would make the cycle actually smarter

Six insights that port, ordered by how much rate they buy.

### a. Integration is part of filing, not a follow-up
File-back must name which existing pages a finding revises **and revise them in the same turn**. A finding filed without integration is a dividend spent. This is the single highest-leverage change and it is free — it is a discipline, not a build.

### b. Budget the schema; every amendment names what it displaces
[[CLAUDE.md]] is the interest rate, and ours grows monotonically. The meta-wiki budgets its constitution to policy only and requires each amendment to name what it displaces, so "the constitution compounds discipline without compounding length." An 18K-char schema that only grows *lowers* the rate — more tokens, less salience — while feeling like investment. This is also the honest answer to the worry-bead pattern: collecting rules instead of changing behavior.

### c. Lint must be scheduled **and independent** — author-blindness is proven
Semantic lint by the author of the day's edits **cannot see the contradictions those edits just created**; the author agrees with the new claim. Demonstrated twice in that vault, and now a third time here, by me, today.

**This is a stronger argument against collapsing to one node than the one I made in [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]].** I argued "gates I authored do not catch me." The sharper claim: *no* author-run semantic check catches author-created contradictions, regardless of who wrote the gate. Our `loop_health.py` is structural-only. The semantic half requires fresh-context adversarial readers, and that requirement does not go away by wanting fewer conversations.

### d. Calibrate the detector before sweeping — the detector is a claim too
Assert **both poles as executable assertions in the script**: a known-good case that must be found, a known-bad case that must not be. The family's most mature vault produced five-plus miscalibrated detectors in days, each alarming, each noise.

This lands on today's work. My pointer checker reported **0 broken wikilinks while the resolver was flagging them** — it judged ambiguity against its own index instead of the thing that actually resolves links. And the **65 broken doc paths** I keep reporting is an uncalibrated number: mostly retired-doc mentions and sibling-repo paths, never triaged. *"When a scan says most of the wiki is broken, suspect the scan."*

### e. Ground-truth anchoring — never canon-vs-canon
Contradiction verdicts need an arbiter, and only the immutable layer can be it. Two of our pages disagreeing tells us *that* something is wrong; only the sources tell us *which*. This is precisely why the Isaiah oracle matters: it is calibrated in Hebrew syntax, outside our own judgment — and precisely why the gold yardstick cannot referee, since it shares the bar's calibration.

### f. Measure the curve, so the claim can be wrong
`growth_snapshot.py` records pages, words, links, density, orphans, and schema size. Predictions are stated in the script so it can fail: compounding → density rises; accumulating → flat; drifting → orphans rise and density falls; append-trap → words-per-page climbs.

---

## What I propose to change in the loop documents

**Carry the shape down to each loop, and reopen the one ruling that closed off compounding.**

1. **Per-loop shape labels.** The document names the shape once, in the Summary. Loops 1, 2 and 4 (canon amendment, retraction→promotion, audit) are **additive — they plateau, and the plateau is success**. Loops 3, 5, 6 and the missing substrate loop are the **knowledge pattern — compounding if and only if they integrate**. Right now every loop frame is drawn identically, so the page cannot tell you which is which.

2. **Reopen "there is no ingest loop and no source-fidelity lint."** This is the substantive change. That ruling is what makes the whole program look additive, and the Isaiah oracle is a standing counterexample: an immutable external layer, a measurement of our output against it, and a number. If it stands, the ceiling is reliability. If it falls, there is a compounding loop here and it is the substrate loop.

3. **Give [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] the shape framing it entirely lacks** — or fold it in, since the topology question matters far less than whether the knowledge loop integrates.

**Why this is not a taxonomy game:** an additive loop that has closed most of its error classes is *finished*, and pushing it looks like diligence while buying nothing. A compounding loop that is merely aggregating looks healthy — findings keep landing — while earning zero. The two failures are indistinguishable from inside and have opposite fixes.

**Cons, stated plainly.** It is a third rewrite of the same document in three days, and rewrite-churn is itself a cost Stan is paying in attention. The additive/compounding split is my analysis, not his ruling and not the corpus's — the corpus draws the line for *its* two patterns, and applying it to a normative-canon project is my extension. Item 2 reopens a considered judgment that a prior version of me made deliberately, and I have been wrong once already on this page. And any taxonomy risks becoming the thing we maintain instead of the loops.

## Related

- [[4-process/improvement-loops.md|improvement-loops.md]] · [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] — the documents this corrects
- [[2-evidence/finding-substrate-loop-diagnosis.md|finding-substrate-loop-diagnosis.md]] — the compounding loop we are missing
- `meta-wiki/wiki/compounding-artifact.md`, `meta-wiki/wiki/ops-improvement-loop.md`, `meta-wiki/wiki/lint-workflow.md`, `meta-wiki/wiki/drift.md`, `meta-wiki/wiki/growth-curve.md`, `meta-wiki/wiki/schema-layer.md` — the sources
