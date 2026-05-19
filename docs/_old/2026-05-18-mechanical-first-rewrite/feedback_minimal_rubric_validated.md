---
name: minimal-rubric-validated
description: "Minimal-rubric ATU rendering empirically validated 2026-05-17 across 8 chapters / 3 corpora / 3 languages. Stan: 'clearly superior in all sections, 100% aligned with how I see the line breaks.' The rubric (bidirectional test + restrictive-relative binding + small set of language-specific syntactic constraints, NO cognitive-unity gate, NO parallelism class adjudication, NO genre anchors as primary licenses) is the load-bearing ATU-identification engine. Subsequent work defaults to the minimal rubric, not legacy producer-style validator stacks."
metadata:
  type: feedback
---

**The principle:** When designing or scaling ATU rendering, the minimal rubric is the load-bearing engine. Use it as the LLM's primary identification step. Do not pre-process with validators that produce ATU rendering; do not add cognitive-unity / parallelism-class / genre-anchor gates as primary licenses. Syntactic rules are constraints (audit-mode), not producers.

**The minimal rubric (as validated 2026-05-17):**

1. Bidirectional test — forward grammatical closure (with language-specific allowances for pro-drop, verbless predication, participial predications, discourse-particle-headed units, conditional protasis in legal-casuistic) + backward referential self-containment (with same-discourse-subject chain continuity).
2. Restrictive relative clause binding — restrictive relatives bind to head noun regardless of internal completeness.
3. Small set of language-specific constraints:
   - Hebrew: gapped finite verb tolerance in immediate parallel cola
   - Greek: aorist-participle attendant-circumstance binding; restrictive ὅς/ὅπου binding; speech-frame binding
   - EME English: discourse-particle binding ("behold", "wherefore", "yea"); restrictive "which/who/that" binding
4. Default KEEP-AS-IS unless rule affirmatively fires.

**Why — empirical evidence (2026-05-17):**

Hand-verification across 8 chapters, 3 corpora, 3 languages:

| Chapter | Corpus / Genre | Source → ATUs | Direction |
|---|---|---|---|
| Genesis 22 | Hebrew narrative+dialogue | 79 → 83 (+5%) | mildly under-broken |
| Leviticus 11 | Hebrew legal list | 87 → 64 (-26%) | over-broken |
| Isaiah 53 | Hebrew poetic prophecy | 37 → 51 (+38%) | heavily under-broken |
| Jonah 1 | Hebrew narrative+dialogue | 53 → 56 (+6%) | slightly under-broken |
| Matthew 28 | Koine narrative+dialogue | 53 → 50 (-6%) | near-balanced |
| Ephesians 1 | Koine Pauline epistle | 38 → 35 (-8%) | near-balanced |
| Revelation 5 | Koine apocalyptic | 57 → 36 (-37%) | NP-enumeration collapse |
| Enos | EME English BoFM | 124 → 70 (-44%) | heavily over-broken |

Stan verbatim: *"the minimal rubric produces better results (maybe not perfect, but clearly superior) in all sections... my spot checks everywhere were that the minimal rubric seems to be 100% aligned with how i see the line breaks."*

Earlier confirmation on Psalm 1: minimal rubric output = 14/14 exact match with Stan's manual baseline.

**Calibration items surfaced by the 2026-05-17 chapters (for codification in v0.2):**

- **Speech-intro + short particle-led reply/vocative**: Gen 22:1 inconsistency. Stan's resolution: speech-intro + vocative addressee = one ATU AND speech-intro + short particle-led reply (הִנֵּנִי) = one ATU. Unified discourse-particle-binding extension.
- **Doxological NP enumeration**: Rev 5:12 seven-fold attribute list collapsed to ~2 ATUs because bare NPs without predication; question whether liturgical/doxological enumeration deserves enumeration-as-ATU sub-rule.
- **Continuative-vs-restrictive ἐν ᾧ**: currently interpretive in Eph 1; explicit sub-rule may be needed for Pauline corpus.
- **Wayyiqtol hendiadys** (וַיָּקָם וַיֵּלֶךְ): rubric splits; question whether hendiadys merits a cognitive-pair carve-out.

These are codification items for the constraint catalog / rubric v0.2, not contradictions of the minimal rubric itself.

**How to apply:**

- Default ATU-rendering pipeline: LLM with minimal-rubric prompt → outputs ATU-segmented text. That is the engine.
- Syntactic constraints (Joüon-Muraoka, Smyth, Wallace, Skousen, etc.) live as audit-mode constraint catalog — applied AFTER the LLM proposal, answer yes/no grammatical questions, flag violations for editorial review.
- When source rendering and minimal-rubric rendering diverge by large %, trust the rubric's signal. Large deltas tend to be CORRECTIONS (over-broken or under-broken source), not over-corrections.
- The cognitive-unity gate (legacy addition to make LLM output match producer-validator output) is empirically inert. Do not re-introduce it.
- Parallelism is off-axis from ATU rendering. Synonymous bicola correctly kept as separate ATUs with no cognitive-unity merging. Parallelism is a poetic-rhetorical feature on a separate axis.

**See also:** [[feedback_architecture_must_match_method]] (the empirical proof that the architecture-method realignment was correct), [[feedback_production_tier_empirical]] (the model tier that operationalizes this rubric at scale), `atu-method/docs/framework.md` §1 (canonical methodology spec), `atu-method/docs/toolset-architecture.md` (Stage 1 implementation at production scale).
