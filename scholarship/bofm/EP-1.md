# EP-1: "According To" Manner vs. Source — Scholarship Companion

**Operational entry:** see `readers-bofm/private/01-method/colometry-canon.md §5 EP-1` (current).

**Status:** This is the scholarship companion documenting WHY EP-1 exists, HOW we know it is correctly framed, and what intellectual / empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

EP-1 ("According To" Manner vs. Source) directs editors to read PPs headed by *according to* as either manner adverbials (HOW the matrix predication unfolds — its mechanism, style, measure, or conformity) or source/authority adverbials (BY WHAT POWER or FROM WHAT SOURCE the matrix predication is warranted). Manner readings merge with the matrix predication; source/authority readings earn their own line. When the reading is genuinely ambiguous, the case routes to REVIEW.

EP-1 is a Category B editorial principle (judgment-required) and a Tier 7 post-hoc tiebreaker — it fires only when Tiers 1-6 (syntax vetoes, formula/vocative integrity, complement integrity, merge-overrides, split-triggers, N=2 adjudication) have not already settled the break.

## Rationale

The preposition *according to* is functionally bivalent in the BoFM-archaic register: the same lexical head can introduce a manner adverbial (an embedded modifier whose presence does not change the matrix's predicative weight) or a source/authority adverbial (an independent theological-or-factual assertion the matrix predication presupposes for its warrant). The two readings carry different cognitive weight for the reader:

- **Manner readings** are *part of the action* — they specify mechanism, conformity, or measure. The reader processes them with the matrix in a single attention chunk: *spoke according to his word* is one cognitive event (a speaking-conforming-to-a-prior-instruction), not two.
- **Source / authority readings** are *separately predicated* — they assert a locus of authorization. The PP's complement (the Spirit, the power of God, the spirit which is in me) is itself a theological entity whose claim on the action is the rhetorically-loaded content. The reader processes the matrix and the source as two attention chunks: *it whispereth me* (a fact) — *according to the workings of the Spirit* (an independent claim about the agency behind that fact).

EP-1 codifies this distinction so that line-break placement reveals it. Merge for manner, split for source. The rule does NOT generate breaks beyond what the matrix predication already supports; it only adjudicates whether an *according to* PP is bonded to its matrix (manner) or floats free as its own atomic thought (source/authority).

The rule is editorial (Category B) because the manner-vs-source disambiguation requires reading the complement-noun against the matrix's discourse frame. There is no purely-syntactic test that resolves it — the same *according to your faith* can read manner (the mechanism by which a blessing comes) or source (the warrant that authorizes the blessing) depending on the surrounding context's framing. Per-case editorial judgment is therefore irreducible.

## Grammatical grounding

CGEL Chapter 6 §11 on prepositional phrases as adverbial modifiers distinguishes between adjunct PPs (manner, time, place — embedded modifiers of the matrix's core predication) and what CGEL Chapter 8 §17 calls *attribution adjuncts* (PPs naming the source, warrant, or authority of a predication). The bivalent prepositions that can introduce either type include *according to*, *by*, *through*, *in* — language-historical study shows these have always done double-duty across the early-modern English register the KJV preserves.

Quirk et al. *Comprehensive Grammar of the English Language* (CGEL-Quirk, 1985) §8.79-8.86 on *manner adjuncts* and §8.91-8.94 on *source/warrant adjuncts* names the same distinction in different vocabulary. The KJV translation tradition retains the early-modern-English usage where *according to* heads both classes; the BoFM inherits this bivalence and exhibits it at higher frequency than modern English.

Traditional Hebrew/Greek grammars handling the *kata* (Greek) and *k-* prefix (Hebrew) cognates name the same manner-vs-source bivalence in those languages — see Wallace *Greek Grammar Beyond the Basics* on *kata + accusative* (manner/standard) vs. *kata + accusative* (source/conformity), with the disambiguation requiring complement-noun-class analysis.

The PP-classification typology that taxonomizes *according to*'s complement-noun classes (faculty/agent/warrant for source; standard/measure/instruction for manner) is the operational distillation of this grammatical literature applied to the BoFM corpus.

## Empirical evidence

### 2026-03-24 punctuation-dependency audit (origin event)

EP-1's distinction was discovered during a corpus-wide audit testing the principle that punctuation is not a break signal (now formalized as `framework.md` §2.1, "Punctuation has ZERO force", and BoFM canon §1 Punctuation is not a break signal).

The audit method: identify every existing v2-mine break that fell at a comma boundary, mentally strip the comma, and re-evaluate whether the break still held on purely grammatical/structural grounds. *According to* PPs were the densest cluster of comma-dependent breaks in the corpus — the orthographic comma before *according to* had been treated as a break-signal across hundreds of instances without per-case grammatical analysis.

Re-evaluating each break on grammar-alone produced a clean bimodal distribution:

- A majority of the comma-coincident breaks were **manner-mechanism / manner-conformity readings**. Stripping the comma, the *according to* PP read as an embedded manner adjunct of the matrix verb — *spoke according to his word*, *gave a genealogy according to his memory*, *answered for the space of an hour according to their time*. These were punctuation-artifact splits; the break was inherited from the 1830 typesetter's comma but not warranted by grammar. They should merge.
- A minority of the comma-coincident breaks were **source/authority readings** where the *according to* PP made an independent theological assertion about the warrant or agency behind the matrix action — *it whispereth me, / according to the workings of the Spirit of the Lord*; *I give unto you a prophecy, / according to the spirit which is in me*. These were grammatically-justified splits; the *according to* complement named an autonomous theological entity whose claim on the action was load-bearing. They should split.

The bimodal distribution was the empirical proof that *according to* is bivalent in BoFM-archaic register and that line-break placement should reveal the function, not blindly track the orthographic comma. EP-1 (then numbered Rule 21) was codified as the formal disambiguation rule on 2026-03-24.

### 2026-04-19 reclassification to EP-tier

When the BoFM canon was restructured into mechanical-rules vs. editorial-principles tiers (2026-04-19 three-layer architecture session — see `private/2026-04-19-canon-v2-and-merge-overrides/transcript.md`), Rule 21 was reclassified as EP-1 alongside three other judgment-required rules (EP-3 inverted predicate, EP-4 title/role + domain, EP-5 virtue/vice lists).

The reclassification recognized that the manner-vs-source disambiguation, while well-grounded grammatically, cannot be reduced to a mechanical UD test. The PP's surface form, the matrix verb's lemma, and the complement noun's class together *focus* the reading but do not determine it. The same complement-noun (*faith*) can read manner-mechanism in one context (*manifest according to their faith* = via-the-mechanism-of-faith) and source-authority in another (*given according to their faith* = warranted-by-faith). The disambiguation is therefore irreducibly editorial.

### Corpus distribution (informal, pre-systematic-sweep)

The 2026-03-24 audit examined ~50 *according to* instances across 1 Nephi, 2 Nephi, and Alma; the bimodal distribution observed was roughly 60% manner / 30% source / 10% genuinely ambiguous. The 10% ambiguous cases were the empirical motivation for the REVIEW routing in the operational rule.

A full-corpus systematic sweep with the current rule shape has not yet been run. Pending tasks for EP-1 corpus-fit work are tracked in BoFM canon §7.3 trigger #12 (post-codification corpus-fit verification) — EP-1 was carried forward through the 2026-04-19 restructuring without a fresh full-corpus sweep, so the sweep remains an open obligation if EP-1 is materially refined again.

### Tier 7 ordering precedent

EP-1's Tier-7 placement was confirmed during the 2026-05-10 UD-detector-framework session (see `private/2026-05-10-ud-detector-framework-and-corpus-sweep/canon-3.5-draft.md`). The session formalized the §3.5 precedence hierarchy and placed all EP-rules at Tier 7 as post-hoc editorial tiebreakers — they fire only when Tiers 1-6 leave a candidate boundary unresolved. This means EP-1 NEVER overrides a J5 substantive-adjunct split (Tier 5) or an R15 vocative integrity merge (Tier 2); it operates strictly in the residual decision space.

## Intellectual lineage

### Punctuation-is-not-a-break-signal principle

EP-1 is the working example that originally proved (and continues to demonstrate) the punctuation-is-not-a-break-signal principle. The 2026-03-24 audit's comma-stripping test was the methodological move that surfaced the manner-vs-source distinction; without that test, the punctuation-artifact breaks would have remained invisible. The principle was generalized from EP-1's specific case to all break-signal analysis (now `framework.md` §2.1, "Punctuation has ZERO force", and BoFM canon §1 Punctuation is not a break signal).

This methodological lineage is preserved in the BoFM `memories/feedback_punctuation_not_evidence.md`: "Punctuation is inherited text, not adjudication evidence."

### Manner-vs-source PP distinction in grammar literature

The manner-vs-source distinction for *according to* PPs has a long pedigree in English grammatical analysis:

- **CGEL** (Huddleston & Pullum, 2002) Chapter 8 §17 on attribution adjuncts vs. manner adjuncts.
- **CGEL-Quirk** (Quirk et al., 1985) §8.79-8.86 (manner adjuncts) and §8.91-8.94 (source/warrant adjuncts).
- **Smyth's Greek Grammar** §1690 on *kata + accusative* manner vs. source readings (the Greek cognate distinction).
- **Wallace's Greek Grammar Beyond the Basics** Ch. 12 on *kata + accusative* category disambiguation.

EP-1 instantiates this universal grammatical category for the BoFM-archaic English register. As the apparatus extends to additional corpora, the same bivalence will surface in any language with cognate manner/source prepositions — Greek *kata*, Hebrew *k-* prefix, Latin *secundum*, etc. The disambiguation method (complement-noun class focus + paraphrase substitution + independence test) is portable; the closed-list indicators are language-specific.

### Editorial-principle vs. mechanical-rule distinction

EP-1's status as Category B (editorial, judgment-required) reflects a foundational distinction in the apparatus between rules that can fire from UD-parse signals alone and rules whose disambiguation requires reading discourse content the parser cannot represent. The other Tier-7 EP-rules (EP-3 inverted predicate, EP-4 title/role + domain, EP-5 virtue/vice lists) share this property — each is well-grounded but irreducibly editorial. They are documented as principles precisely because they cannot be reduced to mechanical detectors without sacrificing accuracy.

This distinction is the conceptual basis for the MISRA-style rule template's Decidability field (Surface-pattern / UD-pattern / Discourse-context-needed): EP-rules are Discourse-context-needed by construction.

## Adversarial history

EP-1 (and predecessor Rule 21) has had two substantive review cycles:

### 1. Initial codification (2026-03-24)

The punctuation-dependency audit surfaced the manner-vs-source bimodal distribution. Adversarial pushback raised:

- **Risk: the distinction is theological-not-grammatical** — i.e., that the rule was importing doctrinal categories ("divine source" = different break-treatment than mundane source) rather than grammatical ones. Resolution: the disambiguation tracks the grammatical category (attribution adjunct vs. manner adjunct), which CGEL treats separately for mundane sources too. The fact that BoFM source/authority readings are densely theological is a corpus characteristic, not a rule-content claim.
- **Risk: the rule may over-fire on genuinely ambiguous middle cases.** Resolution: the rule explicitly routes ambiguous cases to REVIEW (operationalized as Category B, not Category A). The 10% ambiguous middle is the honest empirical residue; it does not invalidate the rule, only constrains its automation.

### 2. Reclassification to EP-tier (2026-04-19)

When the canon's three-layer architecture session reclassified judgment-heavy rules into the EP-tier, Rule 21 was renumbered EP-1. Adversarial review confirmed:

- The distinction remains well-grounded grammatically (CGEL Chapter 8 §17).
- The disambiguation is irreducibly editorial — no UD signature can mechanically resolve the manner-vs-source ambiguity for a parser that lacks discourse-frame access.
- Tier-7 post-hoc precedence is correct: when a higher-tier rule (J5 substantive adjunct, R15 vocative, R1 AICTP) applies to an *according to* PP, that rule wins before EP-1 is consulted. EP-1 is the tiebreaker for the residual decision space only.

No retirement or material rescoping has occurred since 2026-04-19. The rule is stable as currently scoped.

### 3. Pending: post-codification corpus-fit verification

The 2026-03-24 codification rested on an informal ~50-instance sample. Per BoFM canon §7.3 trigger #12 (post-codification corpus-fit verification), a full-corpus systematic sweep remains an open obligation. The sweep would:

- Enumerate every *according to* PP in v2-mine (likely ~200-300 instances across the corpus, given the formulaic frequency).
- Apply the manner/source/ambiguous classification under the current rule shape.
- Verify line-break treatment matches the rule's direction for unambiguous cases.
- Enumerate residual ambiguous-but-decided cases for editorial review.

Until this sweep is run, EP-1's claim of corpus-wide conformity rests on partial-sample evidence.

## Future work

### Phase-2 discourse-context refinement

The manner-vs-source disambiguation is a canonical Discourse-context-needed case — exactly the class of decisions a Phase-2 discourse-aware validator could lift into mechanical resolution. The required infrastructure:

- **Complement-NP semantic classification.** Tag complement nouns with a manner/source/ambiguous label based on lemma + immediate-context features (modifier presence, definiteness, agentive vs. instrumental reading).
- **Matrix-predication frame analysis.** Tag the matrix verb's argument frame to determine whether an *according to* PP is most naturally a manner adjunct or a warrant adjunct given the verb's lexical semantics (*speak* canonically takes manner *according-to*; *give a prophecy* canonically takes source *according-to*).
- **Discourse-frame coherence check.** When the prior discourse establishes a theological-agency frame (the Spirit, the power of God, prophetic commission as the active warrant), source readings win; when prior discourse establishes a procedural/mechanism frame (instructions, measures, standards), manner readings win.

With this infrastructure, the 60/30/10 (manner/source/ambiguous) distribution could shift to ~95/5 mechanical-vs-REVIEW, leaving only genuinely-ambiguous middle cases for editorial review. This is future work; for now Category B + REVIEW is the honest output.

### Closed-list indicator refinement

The current heuristic indicator lists (SOURCE_AUTHORITY_INDICATORS, MANNER_INDICATORS) are non-exhaustive and based on the 2026-03-24 sample. A systematic corpus sweep would refine the lists with the full inventory of complement-noun heads, with manner/source proportions per head. Some heads (notably *faith*, *will*, *word*) appear in BOTH directions depending on context and would warrant context-sensitive sub-clauses. The closed lists serve as editorial-attention focuses, not gating conditions — they will remain heuristic even after refinement.

### Cross-corpus instantiation

When the apparatus extends to GNT, the same bivalence will surface on *kata + accusative* PPs. A sister rule (GNT EP-1 or equivalent) would instantiate the same manner-vs-source disambiguation for the Greek complement-noun classes. The disambiguation method is portable across languages with bivalent manner/source prepositions; the closed-list indicators are language-specific. Similarly Tanakh's *k-* prefix would warrant its own per-corpus instantiation.

### Punctuation-audit follow-on

The 2026-03-24 *according to* punctuation-audit was a one-of-N corpus-wide audit. Similar audits could be productively run on other comma-prone prepositional environments — *for* PPs, *in* PPs, *unto* PPs — to surface other bivalent classes where punctuation-artifact breaks may have sedimented. EP-1's discovery method is replicable.

---

*References:*

- Operational canon entry: `readers-bofm/private/01-method/colometry-canon.md §5 EP-1` (current state)
- Universal framework: [`../../docs/framework.md`](../../docs/framework.md) §2.1 (punctuation has zero force) + §7.0 (Category B editorial-judgment) + §1.5 J5 (substantive adjunct as own focus — interaction)
- Historical Rule-21 codification: `readers-bofm/private/01-method/archive/colometry-canon-v1-archive-2026-04-13.md` (2026-03-24 update entry)
- 2026-04-19 three-layer architecture restructuring: `readers-bofm/private/2026-04-19-canon-v2-and-merge-overrides/transcript.md`
- 2026-05-10 §3.5 precedence-hierarchy formalization: `readers-bofm/private/2026-05-10-ud-detector-framework-and-corpus-sweep/canon-3.5-draft.md`
- Cross-cutting discipline memory: `readers-bofm/memories/feedback_punctuation_not_evidence.md`
- Per-rule audit trail (corpus-fit sweep dates, closed-list refinements): `readers-bofm/private/audit-trail/EP-1.md` (to be created during BoFM canon migration)
