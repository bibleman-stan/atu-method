# Finding — the substrate loop is not missing an instrument. It is missing a filter.

**Diagnosed 2026-08-08**, in answer to Stan's question: *"tell me about the substrate loop that is still missing."*

`improvement-loops.md` Gap 3 says there is **no substrate loop**: "UD corrections happen in waves when somebody runs one, not as a cycle with a trigger and a measure." That is true about the *cadence* and wrong about the *cause*. The measure exists, it was built, it produced a hard number, and Stan correctly demoted it — and the one thing needed to make it usable was never built. Naming the missing part precisely is the difference between a buildable loop and a wish.

---

## What a substrate loop needs, and which part is actually absent

| part | status |
|---|---|
| **trigger** — what fires a correction round | **absent.** No cadence, no threshold, no hook. |
| **instrument** — what measures substrate quality | **EXISTS.** `readers-bofm/5-machinery/scripts/isaiah_oracle.py`, built 2026-05-27. |
| **filter** — what converts a measurement into an admissible change | **absent, and this is the load-bearing gap.** |
| **return edge** — what consumes the result | **absent.** Nothing reads the oracle's output. |

---

## The instrument, and the number it produced

`isaiah_oracle.py` exploits the program's one genuine natural experiment. The BoFM quotes Isaiah and Malachi verbatim; `readers-tanakh` publishes BHSA-anchored ATU segmentation of the same chapters; `data/kjv_diff_index.json` maps each BoFM-Isaiah verse to its KJV source with a word-level diff. Project the gold break positions through the diff and you get a reference segmentation for BoFM wording, **inherited rather than parsed** — which is exactly what a weak-substrate corpus cannot otherwise obtain.

Coverage on disk, counted 2026-08-08 from `readers-bofm/research/isaiah-gold/`:

| book | verses | chapters |
|---|---|---|
| 1 Nephi | 48 | 20–21 |
| 2 Nephi | 301 | 6–9, 12–18, 20–24, 30 |
| 3 Nephi | 30 | 16, 20, 22 |
| Mosiah | 16 | 12, 14 |
| **total** | **395** | |

**The number, from `project_bofm_substrate_quality.md`:** deployed fabric against gold breaks **F1 0.561** (precision .750, recall .448), with **fn=503 over-merges against fp=136**. Malachi, measured independently as a second datapoint, gave F1 0.591 and the same profile. That is a hard, gold-anchored, direction-bearing measurement of the exact defect that no validator in the program can see — and over-merge is Stan's red line.

## Why it stopped — and it was the right call

Stan issued a GIGO correction the same day (2026-05-27): the tanakh gold is **BHSA-anchored**, meaning break positions derive from *Hebrew* syntax with KJV English laid over them. It is gold for Hebrew idea-units and an **imperfect proxy for English ones**, because the KJV is a defective bridge — it smooths wayyiqtol into English subordination, supplies italic words, reorders. His words: *"let's not GIGO this."*

So the oracle was correctly demoted from deploy-template to **candidate-generator / second opinion**, with the correct use specified precisely:

> each candidate break must pass the **English bidirectional ATU test** before it is a boundary — agree → high-confidence over-merge; disagree → investigate (KJV defectiveness vs. fabric error).

**That filter was never built.** Without it every candidate is unusable, so the instrument has sat idle for 73 days. The loop did not fail from neglect; it stalled on one unbuilt component, and nothing was tracking that it had stalled.

## What went wrong in the meantime — three verified symptoms

**1. The correction cadence died.** UD corrections to `v0-cache-conllu` ran 2026-06-01 through 2026-06-05 (482 gated edits, then waves of 334 / 327 / 216 / 131 / 42 / 37, then 150 lever-2 edits) and **stopped**. Nothing has touched substrate since. No trigger existed to fire a next round.

**2. An entire chapter is missing from the gold set and nobody noticed.** 2 Nephi covers 12–18 and 20–24 — **19 is absent**, a hole in the middle of a contiguous run. Verified: `2nephi` chapter `19` **is present** in `kjv_diff_index.json`, so the input existed; the gold output has zero entries for it. Cause not determined (candidate: no tanakh-side gold for Isaiah 9, or a guard rejection). **The point is not the cause — it is that no coverage report exists, so a whole-chapter hole survived 73 days unreported.**

**3. I re-derived in August what was already measured in May.** `finding-isaiah-cross-corpus-divergence.md` (2026-08-07) measured MT Isaiah 9 against 2 Nephi 19 by hand, found BoFM 34% coarser, and reported it as a new result. It is the same over-merge signal the oracle quantified as F1 0.561 in May — and, by an accident worth noting, on **the one chapter the oracle does not cover**, which is why hand-measurement was the only way it surfaced.

Symptom 3 is the missing loop biting the loop-keeper. A substrate loop with a return edge would have surfaced the May measurement the moment Isaiah came up in August.

---

## Why this loop bounds the others

`substrate.md` §1 argues the mechanical ceiling is set by fabric quality. Everything downstream inherits it: binding rules over a weak parse re-hit the same wall (proven 2026-05-27, three rule designs killed at the §7.3 gate before code), and `overrides.json` is per-instance and does not generalize. **A loop that improves the parse is the only one that raises the ceiling rather than working beneath it.**

It also has an evidence property none of the others have. The gold yardstick cannot detect a systematically coarse bar because the gold shares the bar's calibration. The Isaiah oracle is calibrated *elsewhere* — Hebrew syntax, via an edition built by a different pipeline. It is the one instrument in the program that can see a defect the project's own judgment shares. Its weakness (cross-language proxy) and its strength (genuine independence) are the same fact.

---

## Recommendation

**Build the English bidirectional filter, and nothing else, first.** It is the single unbuilt component; every other piece of this loop already exists and is idle behind it.

Concretely: for each of the ~503 candidate over-merges, apply the §2.1/§2.2 bidirectional test to the *English* — forward grammatical closure, backward referential self-containment. Agreement makes a high-confidence over-merge; disagreement routes to investigation as a KJV artifact. This is per-instance judgment inside a fixed rule, which is a `Workflow` fan-out, not hand-adjudication.

**Why this rather than the alternatives.** Restarting UD corrections re-runs the lever that has no measure attached — more waves, same blindness. Building trigger and cadence first schedules a loop whose output is still unusable. The filter is the only piece that converts a real existing measurement into admissible change, and it is also the piece that decides whether the whole approach survives: if the English test rejects most candidates, the oracle is a dead end and we learn that cheaply.

**Cons, stated plainly.**
- The filter's judge is the same instrument whose calibration is in question. Mitigation is that it adjudicates *English* against a *Hebrew-derived* candidate — two different bases — but this is genuinely weaker than an independent judge, and the residual should be sampled by Stan.
- ~503 candidates is real adjudication cost, and dispatched agents have been wrong before.
- The 2 Nephi 19 hole means coverage is not what the file names claim; a coverage report is a prerequisite, not an afterthought.
- Success creates a methodology fork Stan already flagged and held: whether BoFM poetic quotations inherit Hebrew-anchored colometry, which the ~44 structural divergences (R5/R10/R17/R19 in poetry contexts) would force to a decision. **That ratification is his, not mine.**

---

## Related

- [`improvement-loops.md`](../4-process/improvement-loops.md) — Gap 3, which this corrects
- [`substrate.md`](../3-implementation/substrate.md) — §1 the ceiling, §1a the three levers
- [`finding-isaiah-cross-corpus-divergence.md`](finding-isaiah-cross-corpus-divergence.md) — the August re-derivation
- `memories/operational/project_bofm_substrate_quality.md` — the May measurement and the GIGO correction
