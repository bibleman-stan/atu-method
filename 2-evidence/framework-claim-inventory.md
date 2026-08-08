# Framework claim inventory — what carries weight, and what backs it

**Summary**: A read-only pass over [`framework.md`](../1-method/framework.md) enumerating its load-bearing assertions and typing each by epistemic status, so the citation project can be scoped before any source-hunting begins. Headline: the framework is **overwhelmingly `[OURS]`** — original normative construction, not compiled scholarship — which is what a specification *is*, and the honest output of the citation project is therefore mostly **labeling**, not a bibliography. The claims that most need external grounding are not the ones that look uncited; they are the theoretical load-bearers stated in a single clause and passed over. Two structural weaknesses surfaced: the framework's deepest assumption (grammatical closure as a *proxy* for thought) is asserted without support, and its headline empirical claim generalizes from four chapters.

**Method**: full read of [[1-method/framework.md#§1 Purpose|framework.md §1]]–§7 on 2026-08-06; assertions extracted by hand (a judgment task, deliberately not delegated). No citations were added and no claim was altered — this is an inventory, not an edit.

**Last updated**: 2026-08-06

---

## The type system

| Type | Meaning |
|---|---|
| `[OURS]` | Original normative claim. No external support, and none needed — the framework asserts it. |
| `[SOURCED]` | Rests on external scholarship; a receipt into `atu-nlp-wiki/raw/` should exist. |
| `[CONVERGENT]` | We derived it independently; an external parallel exists. Cite as **comparison**, never as warrant. |
| `[MEASURED]` | We tested it. Must carry the number and the sample. |
| `[UNPROVEN]` | Asserted, untested, or predictive. Honest to say so. |
| `[TUNED]` | A numeric threshold presented as a criterion. Its value is a parameter, not a finding. |

The `[CONVERGENT]` / `[SOURCED]` distinction is the safety-critical one. `feedback_rhetoric_bandwagon.md` names "misframes convergence as authorization" as a listed danger: a citation attached to a claim we reached independently implies the authority runs from the literature to us, which inverts the actual epistemics and weakens the method it decorates.

## The inventory

### §1 Purpose

| # | Assertion | Type |
|---|---|---|
| 1 | Each line renders one ATU — a span a reader takes in as one complete unit before needing the next | `[OURS]` definitional |
| 2 | NOT-list: no variant adjudication, no typography/oral-delivery markup, no rhetorical parallelism, no word changes | `[OURS]` scope claim — **CONTESTED by Stan 2026-08-06**, ruling pending |

### §2 The criterion

| # | Assertion | Type |
|---|---|---|
| 3 | The unit is the atomic *thought* unit, not the atomic predication | `[OURS]` core commitment |
| 4 | **Grammatical closure is a *proxy* for thought** | `[UNPROVEN]` — **the single most load-bearing theoretical claim in the document**, asserted in one clause |
| 5 | A line is an ATU if it satisfies EITHER (A) bidirectional test OR (B) marker license | `[OURS]` |
| 6 | "(A) does the overwhelming majority of the work" | `[UNPROVEN]` — no ratio given anywhere; trivially measurable and never measured |

### §2.1 Bidirectional test

| # | Assertion | Type |
|---|---|---|
| 7 | Pro-drop licensed for morphologically-encoded-subject languages | `[SOURCED]` — standard reference grammars |
| 8 | Verbless/nominal predicates count as closed (Heb, Grk); EME English requires overt copula | `[SOURCED]` |
| 9 | Ellipsis-restoration is permitted | `[OURS]` methodological choice |
| 10 | Valency: a transitive verb missing its obligatory complement is not forward-closed | `[SOURCED]` valency theory |
| 11 | Antecedents more than **one ATU** back without chain-continuity fail backward containment | `[TUNED]` — the distance is a parameter with no stated derivation |
| 12 | Anaphoric/cataphoric asymmetry | `[CONVERGENT]` — information-structure literature |
| 13 | The discriminator is **complement-vs-quote, not verb class** | `[OURS]` — hard-won; replaced an earlier wrong framing |
| 14 | Object-slot test via Macula `that-VP`/`role=o` vs `sub-CL`/`role=adv` | `[MEASURED]` + `[SOURCED]` — treebank features; Rev 10:6, Matt 5:36, John 2:18, 1Cor 3:13 |
| 15 | Deixis test: shared deictic center binds, own deictic center stands | `[OURS]` + `[CONVERGENT]` (deixis/participant-tracking literature); Rom 8:16, Rom 9:17, Gal 3:8, Mark 5:23 |
| 16 | Person morphology alone cannot carry the bind/stand call | `[MEASURED]` — minimal-pair counterexample (Rom 9:17 vs 2Thess 2:5) |
| 17 | Restrictive relatives bind to head noun — **universal** across Hebrew/Greek/EME | `[SOURCED]` for restrictiveness; `[UNPROVEN]` for the universality quantifier |
| 18 | Serial circumstantial participial chains: **≥2** coordinated participials each with own complement | `[OURS]` + `[TUNED]` — 1 exemplar (Mosiah 27:35) |
| 19 | Discrete cognitive-state circumstance chain | `[OURS]` + `[SOURCED]` — **already cites Langacker**, the one real external citation in the document |
| 20–23 | Relative-clause-embedded speech-frame; discourse-particle attribution; particle amplification; cognition-frame participial allowance | `[OURS]` — each on 1–2 exemplars; #22 self-flags "highest false-positive risk" |
| 24 | Cross-corpus expectation: rare in BoFM, likelier in Greek/Hebrew/Latin | `[UNPROVEN]` — explicitly predictive, correctly hedged |
| 25 | **Punctuation has ZERO force, including parser labels conditioned on it** | `[OURS]` firewall + `[MEASURED]`-able — the `ccomp`/`parataxis` comma-flip is a testable empirical claim about parser behaviour |

### §2.2 Explicit-marker license

| # | Assertion | Type |
|---|---|---|
| 26 | (B) is the framework's only *productive* licensor, quarantined by two preconditions | `[OURS]` |
| 27 | Registry conditions (i) discrete author lexeme, (ii) closure-eligible under (A), (iii) not already licensed | `[OURS]` |
| 28 | Default KEEP-AS-IS; cognitive-unity gates, parallelism-class adjudication, te'amim hierarchy, genre anchors are NOT licensors | `[OURS]` firewall |

### §3–§4 Architecture

| # | Assertion | Type |
|---|---|---|
| 29–30 | v0→v3 staging; all bindings fire within a single verse | `[OURS]` design |
| 31 | v1.6 cross-verse continuity: sense-line stays in the earlier verse's block | `[OURS]` |
| 32 | Petucha/setuma and per-language paragraph markers take precedence — never merge across an author-placed break | `[SOURCED]` (Masoretic paragraphing) — and worth noting it sits in visible tension with #25's te'amim ban; both are "on the page," one is honoured and one is barred |
| 33 | "The framework is corpus-agnostic" | `[UNPROVEN]` — cross-corpus convergence is recorded elsewhere as *thesis, not result* |

### §5 Validation

| # | Assertion | Type |
|---|---|---|
| 34 | Hebrew validated across 4 genres — Gen 22 F1 91.2%, Ps 1 88.9%, Isa 53 88.3%, Lev 11 85.2% | `[MEASURED]` **n=4 chapters**, one of them 12 verses |
| 35 | "Boundary F1 is genre-stable (85–91%)" | `[MEASURED]` + `[UNPROVEN]` — *stability* is a generalization from four points |
| 36 | The 14-rule layer needs 5–25% editorial absorption depending on genre | `[MEASURED]` |
| 37 | LDHB consulted as calibration, not a runtime dependency | `[SOURCED]` |

## What the inventory shows

**Roughly three quarters of the load-bearing assertions are `[OURS]`.** That is the correct shape for a normative specification and should be stated as a feature, not repaired. The deliverable of the citation project is therefore *labeling* — and an honest `[OURS]` is worth more than a found citation, because it makes the framework's actual claim to originality visible and defensible.

**The four highest-value targets, ranked — none of which look uncited at a glance:**

1. **#4, the proxy claim.** "Grammatical closure is a proxy for thought" is the hinge the entire method turns on: it is what licenses a *syntactic* test to answer a *cognitive* question. It has no support, no hedge, and no cross-reference. This is where Chafe's idea units, Cresti's information units, and Langacker actually bear — and where [[memories/feedback_atu_and_rhetorical_lenses_distinct.md|feedback_atu_and_rhetorical_lenses_distinct.md]] has already done much of the comparative thinking, unlinked from the framework itself.
2. **#34–35, the empirical base.** The headline "85–91%, genre-stable" generalizes from four chapters and is quoted downstream as though settled. It needs either a larger sample or an explicit `[MEASURED, n=4]` qualifier. The BoFM gold yardstick (33 stratified verses, F1 ≈ 0.67) already shows what happens when the sample gets harder.
3. **#6, the (A)-vs-(B) ratio.** Trivial to compute from deployed output and never computed, yet "the overwhelming majority" is doing real rhetorical work in justifying (B)'s quarantine.
4. **#11 / #18, the unmarked parameters.** "More than one ATU back" and "≥2 coordinated participials" read as criteria but are tuned values. Marking them `[TUNED]` is honest and costs nothing.

**One tension worth a ruling** (#32 vs #25): petucha/setuma are honoured as author-placed breaks while te'amim are barred as editorial overlay. Both are Masoretic. The distinction is defensible — paragraphing may encode a different transmission layer than accentuation — but the framework does not currently make the argument, and an external reader will notice.

## Next step

Typing is cheap and already done. Citation-hunting should start with target #1 only, sourcing from `atu-nlp-wiki` pages rather than `raw/` directly so the synthesis is written once and reused. Targets #2–#4 need measurement, not sources — they are re-runs of gates we already own.

## Related

- [`framework.md`](../1-method/framework.md) — the document inventoried
- [`../../memories/feedback_atu_and_rhetorical_lenses_distinct.md`](../../memories/feedback_atu_and_rhetorical_lenses_distinct.md) — existing comparative work on Chafe / Cresti / Korpel, currently unlinked from the framework
- [`improvement-loops.md`](improvement-loops.md) — loop 5 is the theory↔experiment cycle this project feeds
