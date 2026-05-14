# Framework — Methodology Specification

**This document is the canonical statement of the methodology framework shared across all atu-method reader editions.** It is operational — consumed by LLM agents, validators, and editorial discipline. Rationale, defensibility arguments, and intellectual lineage live in the [scholarship companion](../scholarship/) and are deliberately absent here.

Per-corpus canons cite this document by stable section ID (e.g., "see `atu-method/docs/framework.md §1.5 M1`"). They MUST NOT inline framework prose.

Normative keywords (MUST, MUST NOT, SHALL, SHOULD, MAY) follow RFC 2119 / BCP 14 / RFC 8174.

---

# Part I — Purpose and Stance

## §0.1 Mission

The apparatus reveals **atomic thought units (ATUs)** — units of meaning a reader can process discretely. Each line on the page renders one ATU; each ATU is a span the reader can take in before needing the next.

The apparatus does NOT:
- Produce typography
- Reveal rhetorical parallelism (separate scholarly layer — may overlap but is not the target)
- Prescribe oral delivery
- Adjudicate textual variants (the source text is a fixed input)

The apparatus DOES format text so that a non-expert reader — student, ESL learner, child, newcomer — can take canonical scripture one atomic thought at a time.

## §0.2 Method

**The mission is sense-driven. The method is syntax-constrained.** A break that violates the target language's syntax is always wrong regardless of how strong the sense argument; a sense judgment within the permitted space is editorially recoverable. Leading with syntax preserves the discipline that lets sense work — it does not demote the mission.

Novel rules MAY originate from sense-driven observation. The method accommodates this: sense proposes, syntax filters, the combination becomes a rule. But every break that survives to the corpus MUST be affirmable by the target language's syntax.

## §0.3 Pragmatic stance

This methodology is a set of conventions reflecting what the apparatus is trying to reveal. It is not derived from a cognitive theory; no such claim is asserted. The apparatus operates as what it is: a consistently-applied editorial practice grounded in target-language syntax, tested against the corpus, and refined by validator sweeps.

## §0.4 Scope

Each per-corpus instantiation of this framework governs **where lines break** in its source texts. It does NOT govern:
- Punctuation (inherited from the source; preserved unchanged)
- Words (never added, removed, or altered)
- Layout beyond break positions
- External editorial overlays (te'amim, NA28 paragraph structure, ancient codex colometric arrangements, etc. — see §1.10 and §1.11)

---

# Part II — The Framework

## §1.1 Generative principle

**Each proposition splits by default.**

A proposition is the prototypical ATU — a complete predication (subject + finite verb + complement) the reader can process as a single cognitive bite. Propositions drive line breaks. There is no positive requirement to break beyond propositions; there is no positive requirement to merge beyond them. At every candidate location, the operational question is: *is this a proposition boundary?*

The five structural justifications (§1.4) extend this rule: non-predicated units that function as atomic thoughts via formal-structural recoverability qualify as proposition-equivalents for break purposes.

**Referential self-containment — the atomic-thought test is bidirectional.** "Single cognitive bite" requires the line to stand on its own *referentially*, not just *grammatically*. A line whose content is anaphoric to prior context — pronouns without antecedent on the line, deictic demonstratives (*these things*, *that day*, *the same*), discourse-anaphoric particles (*therefore*, *thus*, *לָכֵן*, *עַל־כֵּן*, causal *כִּי*) — does not satisfy atomic-thought standing alone, even when it passes forward grammatical closure. The reader's understanding dangles BACKWARD into unresolved context, not just forward into missing complements. The atomic-thought test requires referential self-containment, not merely forward grammatical closure.

The test is asymmetric: **cataphoric** reference (forward-pointing, e.g., presentative *הִנֵּה* + indefinite NP introducing new content, or *thus says X:* announcing speech about to follow) does NOT fail the test, because the forward content is being *introduced*, not *depended on*. Only **anaphoric** unresolved-backward-dependence fails.

Canonical example: Gen 22:1 *wayehi achar ha-devarim ha-eleh* ("and it came to pass after these things") is NOT an ATU on its own line — *ha-devarim ha-eleh* ("these things") is a deictic pointer to undefined antecedent narrative. The line as content is referentially empty without prior context. The whole construction (frame + apodosis) is one ATU because the frame is referentially anaphoric and the apodosis is what the frame opens into. This corrects a class of "fronted-temporal-as-J5" misclassifications: J5 requires *substantive* adjunct content (§1.4 J5: "answers a 'when/where/why/how' question from the matrix's own content"), and a deictic pointer to prior narrative is not substantive content.

**Relationship to §1.5 merge-overrides.** This is a refinement of the §1.1 atomic-thought test itself, not a new merge-override. M3 (Bare-Governor Indivisibility) and M4 (Fragmented Atomic Thought-Unit) are §1.5 mechanisms that catch *forward*-dangling heads and *symmetric* fragmentation respectively. Backward-anaphoric failure is caught upstream of those mechanisms — at §1.1, by the atomic-thought test stated bidirectionally. A line that fails the bidirectional test fails atomic-thought, full stop; the merge is the consequence, not a separate rule. Per-corpus canons need not write a new merge-override for backward-anaphoric cases unless local diagnostic conditions warrant a closed-list operationalization.

**Status — informational diagnostic, not precedence override.** The bidirectional test sits at §1.1 as an *informational diagnostic* about whether each candidate line stands as an ATU. It is **not a precedence override**: it does not adjudicate between competing rules in the §1.8 application-order step machinery, and it is not invoked to resolve intra-Layer-3 conflicts (those go through per-corpus §3.5 precedence hierarchies). It fires *upstream* of the application-order steps — at the point where the candidate ATU is being validated for atomic-thought standing. Treating it as a precedence override (e.g., "the bidirectional test trumps rule X" used to resolve a rule conflict) is a category error: precedence resolves rule conflicts among the rules in §1.4 / §1.5 / per-corpus §5; the bidirectional test resolves whether a line is an ATU at all. (Lesson surfaced by gnt-reader the hard way, 2026-05-13.)

(Codified 2026-05-13 from cross-conversation refinement. See [`memories/feedback_atu_test_is_bidirectional.md`](../memories/feedback_atu_test_is_bidirectional.md).)

## §1.2 Syntax forbids splits (three closed-list ways)

Syntax does not generate breaks. Syntax only vetoes them. A split that the generative principle would otherwise produce is forbidden when one of these three applies:

1. **Layer 1 mid-phrase prohibitions.** Splits mid-predication, mid-phrase, or mid-lexical-unit. The specific prohibitions are language-specific and live in each per-corpus repo's Layer 1 break-legality table (`data/syntax-reference/<language>-break-legality.md`). Universal pattern: line-final CCONJ seeking next member, DET seeking head, AUX seeking V, ADP seeking object, transitive V seeking DO, mid-vocative split, mid-fixed-unit split.

2. **Layer 3 complement integrity.** When a matrix verb's or adjective's valence is unsatisfied without its clausal complement (e.g., *he said that X*, *it is expedient that X*), the matrix is grammatically incomplete on its own; the complement must merge. Per-corpus rules implementing this principle are language-specific (see each canon's §5 — the verb classes that require complement-integrity merging differ by language).

3. **Layer 3 formula integrity.** Lexicalized multi-word frames function as single units. Per-corpus rules implementing this principle are language-specific (formula content varies — BoFM has *And it came to pass*; Tanakh has wayyiqtol formulae; GNT has *καὶ ἐγένετο*).

These are the "unless" clauses of "split each proposition unless syntax forbids."

**Constraint vs. determination — the asymmetry between §1.1 and §1.2.** §1.1 (the generative principle) is the DETERMINATION engine: it positively prescribes where breaks should go (each proposition splits). §1.2 (syntax forbids splits) is the CONSTRAINT layer: it negatively prohibits breaks that would violate Layer 1 grammar, complement valence, or fixed-formula integrity. **Grammar does not determine ATU boundaries; grammar can constrain them.** A grammatical pattern's existence in the parsed corpus does NOT auto-justify a determination-rule. Closed-list rule extensions (per-corpus canon §5) operationalize where the atomic-thought-failure test fires under specific grammatical conditions — they are NOT grammatical-pattern catalogs. The threshold for a closed-list entry is "is this position content-empty such that breaking here leaves a line with no atomic thought?" — that's the determination-engine principle, applied through grammar-as-constraint. Audits that propose new rules grounded purely in "grammatical pattern X is present/absent" fail this asymmetry check and must be rejected. (Codified verbatim by Stan 2026-05-13: *"grammar doesn't determine ATUs boundaries, but it can constrain them."* See `memories/feedback_grammar_constrains_not_determines.md` for full discipline + cross-cutting connections.)

## §1.3 Image sharpens ambiguous proposition boundaries

**Camera-angle test (DEPRECATED — see caveat).** When proposition-first is ambiguous, ask: does the mind's eye reposition between candidate frames? Camera-angle shift → SPLIT. No shift → MERGE.

**Caveat (added 2026-05-13).** The camera-angle diagnostic is DEPRECATED in favor of the bidirectional atomic-thought test (§1.1 refinement; see [`../memories/feedback_atu_test_is_bidirectional.md`](../memories/feedback_atu_test_is_bidirectional.md)). Stan's verbatim observation: *"the more I see it at work, the less confident I am it's helpful."* When invoked, camera-angle reasoning either (a) COLLAPSES to the atomic-thought test ("each side has its own atomic content") or (b) SMUGGLES IN aesthetic-rhetorical preference (`feedback_rhetoric_bandwagon` failure mode). Camera-angle never adds independent diagnostic force. Treat invocations as a warning signal for bandwagon/aesthetic reasoning. Use the bidirectional atomic-thought test instead. See [`../memories/feedback_camera_angle_diagnostic_demote.md`](../memories/feedback_camera_angle_diagnostic_demote.md) for full discipline.

## §1.3a Rhetoric and ATU — figures constrain, atomic-thought determines

**Principle (added 2026-05-13).** Rhetorical figures (hendiadys, merism, parallelism, chiasm, anaphora, climax, etc.) have DEFAULT ATU dispositions that flow from their referential structure — but they never independently DETERMINE ATU boundaries. Each figure CONSTRAINS the candidate space; atomic-thought (§1.1, bidirectional) determines the answer. Same asymmetry as §1.2 (grammar constrains, atomic-thought determines): rhetoric is a second constraint layer over the same determination engine.

**Default dispositions (figure → predicted disposition, not determinant):**

- **Hendiadys** (synonymous doubling → one concept): MERGE under M1 (synonymy-coextension)
- **Merism** (polar binary representing totality): MERGE under M1 (polar-totality-coextension)
- **Parallelism** (synonymous/antithetic/synthetic): SPLIT each member per J1
- **Chiasm** (A-B-C-B'-A' inverted mirror): NO FORCE on ATU (structural observation across multiple ATUs, not a determination within them)
- **Anaphora / epistrophe / repetition figures**: SPLIT each member per J1 (repetition is signal, not force)
- **Climax / gradatio**: SPLIT each member per J1

**Critical:** the figure's default is a HYPOTHESIS; the atomic-thought test confirms or overrides. When they disagree, atomic-thought wins. Example: `"hardness of HEARTS / blindness of MINDS"` is formally hendiadys-shaped but each member has distinct sub-referent modifier (hearts vs minds) → atomic-thought-test passes for each → SPLIT despite hendiadys surface. Example: `"commandments of God, / and his statutes, according to the law of Moses"` is formally parallel-shaped but unified under shared framing PP → MERGE despite J1 surface (M1 hendiadys absorbs).

**Stan's verbatim 2026-05-13:** *"this is a key insight: the interaction of rhetorical devices/figures of speech with ATUs."* See [`../memories/feedback_rhetoric_figures_constrain_atu.md`](../memories/feedback_rhetoric_figures_constrain_atu.md) for full discipline + cross-cutting connections.

## §1.4 The Five Structural Justifications (closed list)

Non-predicated units that function as atomic thoughts via formal-structural recoverability. The reader reconstructs "who did what" because formal markers in the text make the missing predicate recoverable.

The list is extensible only by worked corpus example + adversarial validation. A proposed sixth justification MUST demonstrate (a) that it is a genuinely distinct instance of the same generating principle, and (b) that it survives an adversarial challenge.

### J1 — Formally-marked parallel series

Members connected by formal markers (*and also*, *nor*, correlative particles, polysyndetic *and*, language-specific equivalents) where the shared predicate is recoverable from the parallel structure. Each member earns its own beat.

**Compound list break signals.** In a compound list governed by one preposition or verb, bare coordinate items (e.g., *"and [noun]"*) are compound objects and stay merged. A break inside a compound list is justified only when one of these signals is present:

1. **Elided auxiliary + stacked participles** — each is an implied predication.
2. **Possessive restart** — a new possessor or possessive after items without possessive. *Repeated identical possessive* is formulaic and does NOT alone justify a break.
3. **Demonstrative** — a new demonstrative signals a new specified noun phrase.
4. **Attached relative clause** — a relative adds predication to the item.

Without one of these signals, bare coordinate items merge.

**M1 bonded-pair precedence inside compound lists.** When a compound-list item is itself an M1 bonded pair (§1.5), the bonded pair is the item — the pair treats as one atomic unit within the larger series. None of the four compound-list break signals reaches inside a bonded pair to split it.

### J2 — Portrait accumulation

A set of attributes building one mental picture, sharing a copular or attributive frame from context. Applies only when the stack IS the portrait, not when it is a catalogue.

### J3 — Speech-act announcement

Complete communicative predication introducing direct discourse. Announcement and quoted content are separate cognitive frames.

Per-corpus instantiations of this justification may name specific formula patterns (e.g., recurring speech-tag formulae in the language's literary register). Those named patterns are operational sub-clauses of J3 and are documented in the respective per-corpus canon §5.

### J4 — Classical commata

Short fragmentary utterances carrying full communicative weight (typically 1-3 words). Brevity + isolation = deliberate emphasis.

### J5 — Substantive adjunct as own focus

A fronted or trailing adjunct (temporal PP, locative PP, causal PP, etc.) that (a) is grammatically peripheral to the matrix predication's core truth AND (b) carries substantial content earns its own line.

**Grammatical grounding.** The target language treats peripheral adjuncts as syntactically detachable — they can front, trail, or be omitted without breaking the matrix. When the content is substantial, the detachability becomes cognitively active.

**Test.** Can the adjunct be paraphrased as its own "when/where/why/how" clause answering a question the matrix leaves open? If yes, it is a slot-filler and earns its own line.

**Exclusion: degree quantifiers.** Short PPs that modify the *degree* of a predicate do NOT pass the slot-paraphrase test — they modify how-much, not when/where/why. Treat as predicate modifiers, not slot-fillers.

**Same-slot vs distinct-slot diagnostic (matrix-cumulation disambiguation).** When a short matrix predicate (≤10 words with finite verb) is followed by N≥3 adjunct lines each leading with a preposition / fixed MWPP (e.g., `even from`, `notwithstanding`, `according to`) / participial frame (`having…`, `being…`) / infinitival lead (`to declare…`), J5 surface-form risks colliding with J1 (formally-marked parallel series). The discriminator:

- **Uniform-type adjuncts** (all PPs with the same preposition, or all infinitives, or all participials, with parallel surface form) → these occupy the same argument slot N times. J1 wins per the N≥3 cliff (§1.9): each member is its own beat in a formally-marked series.
- **Mixed-type adjuncts** (different argument-frame slots: when / how / despite-what / for-what-purpose / for-whom) → these jointly qualify one act rather than enumerating peers. J5 does NOT license each on its own line; the matrix + adjuncts may form a single cognitive proposition that should cluster onto 1-2 lines.

**Application.** Mixed-type matrix-cumulation does NOT mechanically force a merge — apply criterion 1 (atomic-thought test) to confirm whether the cluster reads as one claim with its qualifications or as N independent beats. The diagnostic surfaces candidates; semantic-content judgment decides.

**Canonical examples (BoFM corpus, 2026-05-11):**
- **Cluster (mixed-type):** Alma 30:32 — matrix `for behold I have labored` + temporal `from the commencement of the reign of the judges until now` + manner `with mine own hands for my support` + adversative `notwithstanding my many travels round about the land` + purpose `to declare the word of God unto my people`. Four distinct argument-frame slots; merged to 2 lines.
- **Cluster (mixed-type):** Mosiah 29:14 — matrix `And even I myself have labored` + manner `with all the power…` + purpose `to teach…` + purpose `and to establish peace…` + result `that there should be no wars…`. Twin of Alma 30:32; merged to matrix+manner / purpose+purpose / result.
- **Stay split (uniform-type):** 2 Nephi 16:2 (Isaiah seraphim) — `with twain he covered his face / and with twain he covered his feet / and with twain he did fly`. Three uniform `with twain`-fronted finite clauses; J1 parallel series at N=3.
- **Stay split (uniform-type):** Alma 12:1 — `he opened his mouth and began to speak unto him / and to establish… / and to explain… / or to unfold…`. Four purpose-infinitives; J1 stack of speech-acts per N≥3 cliff.

**Common false-positive (genuine Cat B):** Alma 13:3 — mixed-type adjunct surface form (participial / causal-PP / locative-participial) but each line delivers a discrete substantive doctrinal beat (ordination origin / faith-basis / agency-condition). Same-slot test surfaces it as MERGE-CANDIDATE; atomic-thought test correctly stays split. Editorial judgment required.

## §1.5 The Four Merge-Override Conditions (closed list)

**Symmetric counterpart to structural justifications.** Where structural justifications describe cases where the default (merge under propositions-first) is overridden to produce a split, merge-overrides describe cases where an apparent split-trigger is itself overridden — returning the members to one line. The default is still merge; these overrides catch cases where naive application of split-triggers would fragment a unit that should stay whole.

**Generating principle.** Even when a line passes the structural prong (formal markers present), merge wins when the resulting fragments would fail on more basic grounds — the chunk is not actually two propositions, the clause nucleus would be ruptured, the fragment cannot stand as atomic thought, or the cognitive prong itself fails.

**Strict-application caveat — rejection ≠ split license.** When a merge-override does NOT apply to a given case, that does NOT automatically mean the case should split. It just means THAT override doesn't fire. The default behavior is still determined by the generative principle (proposition-first) and by other applicable rules (other merge-overrides, syntactic vetoes, structural justifications). Reason: *"override rejected → apply remaining analysis,"* NOT *"override rejected → must split."*

The list is extensible only by worked corpus example + adversarial validation, same rule as the structural justifications.

### M1 — Gorgianic bonded pair

**Definition.** N=2 coordinate members joined by a coordinating particle where the pair functions as a single unified hendiadys or bonded rhetorical image — not two independent propositions. Even under formal coordination (which would normally trigger J1), if the pair is bonded, merge.

**Test.** Can the two members be paraphrased as a single unified image or hendiadys? Do they carry shared rhetorical weight without independent predicative force?

**N=2-only caveat.** M1 fires ONLY on N=2 coordinate pairs. It does NOT fire on:
- N=3+ chains (J1 wins per the N=3+ cliff, §1.9)
- Mixed-class coordinates (one finite + one participial, or one verb + one noun)
- Re-naming appositives (covered by language-specific apposition rules, not by M1)

**Critical distinction — what M1 does NOT cover.** M1 covers true synonymy / cognate acts / hendiadys (one act named twice for emphasis). It does NOT cover:
- **Sequential narrative bonding** — two distinct actions in sequence (e.g., draw + smite as draw-weapon-then-strike).
- **Distinct speech acts** — two different communicative actions even when thematically related.
- **Rhetorical/thematic clustering** that names sequential or distinct actions.

Sequential distinct actions split per the generative principle even when they form a recognizable rhetorical figure. See [`../memories/feedback_rhetoric_bandwagon.md`](../memories/feedback_rhetoric_bandwagon.md).

**Tie-breaker when M1 and J1 both fire on the same N=2 pair:**
- Each member has a distinct non-synonymous finite verb → J1 wins (SPLIT).
- Members are semantically synonymous, cognate, or intensification variants → M1 wins (MERGE).
- Bonded-pair nouns/adjectives with unified rhetorical weight → M1 wins (MERGE).

This tie-breaker is the canonical specific case of the cross-cutting **N=2 Adjudication Principle** (§1.9).

**Asymmetric-modifier sub-clause.** When an M1-candidate pair has one member carrying a PP modifier or relative clause the other lacks, M1 still wins → MERGE if the modifier attaches semantically to the pair AS A UNIT. SPLIT only if the modifier scopes over only one member to the exclusion of the other, producing genuinely distinct predicative force. Apply the **joint-attachment test**: paraphrase with the modifier distributed to both members. If the paraphrase preserves meaning, joint-attachment holds → MERGE.

**Per-corpus instantiations.** Each per-corpus canon §5 maintains its own M1 closed-list (nominal pairs, verb pairs) drawn from corpus-attested cases.

### M2 — Verb-object clause-nucleus bond

This merge-override is an alias for the per-corpus complement-integrity rule (in BoFM canon, Rule 17; in GNT canon, Rule 8; in Tanakh canon, Rule H7). A governing verb or adjective requiring a clausal complement forms one integrated predication with its complement. The matrix verb alone does not carry complete predication.

See each per-corpus canon §5 for the complement-integrity rule's full treatment including the verb-class closed list, exceptions, and delete-test diagnostic.

### M3 — Bare-governor indivisibility

**Definition.** A head word that cannot stand on its own line without at least one complement, object, or dependent — participial adjective functioning predicatively, governing participle awaiting content, discourse particle standing alone. The bare governor fails the atomic-thought test because it is grammatical machinery awaiting content, not a complete predication.

**Test.** Can the isolated head-word be read as a complete thought? Or does the reader's attention dangle forward, expecting completion on the next line?

**Contrast with J3 (speech-act announcement).** Finite speech-act formulas with their accompanying speech-tag punctuation ARE complete speech-act predications. Bare participial frames awaiting content are NOT — they fall under M3.

**Contrast with participial absolute.** A full participial absolute with its own subject + participle + optional complement IS a complete predication and earns its own line (a structural-justification case, language-specific). M3 catches BARE participial heads WITHOUT the subject-bearing absolute structure.

**Bare trailing participials (M3 extension).** Bare trailing participial heads (subject-inheriting; no own-named subject; in adjunct position relative to a matrix predication) are M3 cases — they merge with their matrix predication.

Four structural carve-outs keep certain bare trailing participials on their own line:

1. **Stack-cap.** Adjacent participials stay own-line when stacking IS the rhetorical structure: N≥3 adjacent participials, OR N≥2 with the same -ing lemma (anaphoric repetition), OR merged-line would exceed 130 characters.
2. **Coord-list member.** When the participial is a parallel beat in an open coordinate list of participial-fronted lines, the participial earns its own beat.
3. **Antecedent-locality fail.** When the nearest preceding NP supplying the participial subject is NOT the matrix subject, the participial modifies the embedded NP, not the matrix.
4. **Fronted-position participial.** When the participial precedes the matrix verb, backward-merging would split subject from predicate.

**Length backstop.** Merged-line > 130 characters → REVIEW-REQUIRED (per-corpus appliers may tune the threshold).

### M4 — Fragmented atomic thought-unit

**Definition.** If splitting a line would produce fragments that individually fail the atomic-thought test, merge. The inverse of the cognitive prong: the cognitive prong requires each resulting chunk to be its own atomic thought for a split to proceed; if any resulting fragment fails that test, the split is blocked.

**Test.** Read each proposed resulting line aloud as a standalone unit. Does it constitute one focused-attention chunk with bounded information? If any resulting line fails, the split is over-fragmenting.

**Scope discipline — prospective not retroactive.** M4 fires ONLY when evaluating a PROPOSED split. **M4 is NOT a retrospective merge generator.** When an existing split shows both fragments individually passing atomic-thought, M4 does not fire, even if the two events are causally, narratively, or rhetorically linked. "Narrative completion" and "atomic-thought failure" are different tests; conflating them is a documented failure mode (see [`../memories/feedback_rhetorical_force.md`](../memories/feedback_rhetorical_force.md)).

**Precedence over structural justifications.** M4 fires ONLY when splitting produces a fragment that **fails** the atomic-thought test. A fragment that PASSES atomic-thought via another structural justification's cognitive prong does NOT fail. Specifically:
- **J1 members** of a 3+ member series pass cognitive-prong via shared-predicate recovery. M4 does NOT fire on J1 series members.
- **J5 substantive adjuncts** (year-formulas, proper-noun entities, institutional bodies) earn own lines. M4 does NOT fire on J5 cases.

**Unified principle.** Merge-overrides (M1–M4) block split-triggers ONLY when splitting would produce true atomic-thought failure. Fragments that pass atomic-thought via a structural justification's cognitive prong are not merge-override fragments; the structural justification wins.

## §1.6 Summary — the four forces

| Force | Direction | Role |
|---|---|---|
| Propositions + 5 structural justifications | GENERATIVE | Default split at every proposition or justified non-proposition boundary |
| Syntax (Layer 1 + complement-integrity + formula-integrity) | SUBTRACTIVE | Forbids some splits the generative principle would produce |
| Merge-overrides (M1–M4) | SUBTRACTIVE | Block split-triggers when resulting fragments fail on more basic grounds |
| Image (camera angle) | DIAGNOSTIC (DEPRECATED 2026-05-13 — see §1.3 caveat) | Use bidirectional atomic-thought test (§1.1) instead |
| Rhetorical figures (hendiadys, merism, parallelism, chiasm, etc.) | CONSTRAINT | Default dispositions correlate with atomic-thought outcomes; figures never independently determine. See §1.3a. |

## §1.7 Decision procedure

At every candidate boundary:

1. **Default:** merge (propositions share one predicate; atomic-thought test applies at the predication level).
2. **Split-trigger fires** (proposition boundary OR any of J1–J5): tentative split.
3. **Syntax veto** (Layer 1 mid-phrase prohibition; complement integrity; formula integrity): blocks the split → **merge**.
4. **Merge-override fires** (M1 / M2 / M3 / M4): blocks the split → **merge**. **When split-trigger and merge-override both fire on the same location, merge-override wins.** The merge-override list is the mechanism that prevents split-triggers from producing non-atomic or bonded-pair fragments.
5. **Bidirectional atomic-thought test** (§1.1 refinement): when 1–4 leave room for editorial judgment, run the bidirectional referential-self-containment test in both directions (forward grammatical closure + backward anaphoric resolution per [`../memories/feedback_atu_test_is_bidirectional.md`](../memories/feedback_atu_test_is_bidirectional.md)). This replaces the deprecated camera-angle diagnostic (§1.3 caveat).

The framework is a default-merge with two closed lists of exceptions — five structural justifications (add splits beyond propositions) and four merge-overrides (block splits that would fragment unity) — plus the syntax-subtractive veto and the image diagnostic.

## §1.8 Application order — explicit step-by-step

The Decision Procedure above gives the high-level 5-step ordering. This subsection makes the step-internal ordering explicit so rule application is provably deterministic — two appliers following the canon converge on the same output regardless of which rule they check first within a step.

**Step 0 — Input filter.** Punctuation is never a break signal (§1.10). Versification is never a break signal (§1.11). Authorial asymmetry (§1.13) governs batch-sweep discipline — filters what counts as a candidate signal *before* generative evaluation begins. None operate within the per-location procedure; they operate upstream of it.

**Step 1 — Syntax veto.** At most one of the three closed-list ways fires per location (commutative within-step). When both a Layer 1 and a Layer 3 rule could apply, Layer 1 wins. Intra-Layer-3 precedence conflicts are adjudicated by per-corpus §3.5 precedence hierarchies.

**Step 2 — Split-trigger (generative).** Proposition-first split, plus structural justifications J1–J5. **Multiple justifications firing are co-compatible — they all agree on SPLIT; no adjudication needed.** N=2 Adjudication Principle governs coordinate-pair cases (§1.9). The N=3+ cliff governs N≥3 (J1 wins over merge-rules at N≥3 for coordinate predications).

**Step 3 — Merge-override (subtractive).** M1 / M2 / M3 / M4 plus any per-corpus specialized merge rules. **Multiple merge-overrides firing are co-compatible — they all agree on MERGE; no adjudication needed.** M4's precedence refinements govern M4 vs. J1 / J5. Step 3 wins over Step 2 when both fire on the same location.

**Step 4 — Diagnostic.** Image / camera-angle test only when Steps 1-3 leave ambiguity.

## §1.9 N=2 Adjudication Principle

**The problem this solves.** Several rules mandate MERGE for N=2 coordinate constructions (M1, complement-integrity two-member that-series, etc.). Simultaneously, J1 mandates SPLIT when each member earns its own atomic beat. At N=2 both rules can fire on the same construction.

**The principle.** When a merge-mandating rule and a split-mandating rule (J1) both fire on the same N=2 coordinate construction:

- **Bonded / synonymous / cognate / intensification variants → merge wins.** The two members form a single unified image, action, or proposition under one cognitive chunk.
- **Distinct non-synonymous → split wins.** Each member is its own atomic beat per J1.

**Diagnostic.** Apply the M1 verb-synonymy test (§1.5 M1): *can the two members be paraphrased as a single unified image or proposition without loss of content?* If yes → merge. If the paraphrase requires dropping semantic content unique to one member → split.

**Does NOT apply to appositional constructions.** Appositional rules (divine-title appositives, vocative+close-appositive) are NOT adjudicated by the N=2 Principle's synonymy test. Appositives are semantically synonymous by definition — the second member re-names the first — so the synonymy test would mechanically fire "merge" on every appositive. Per-corpus appositional rules and their formal-anchor diagnostics are the correct adjudications for these cases.

**Does NOT apply at N=3+.** The N=3+ cliff (canonical case across the readers: BoFM Helaman 3:16 six-verb cascade) establishes that at N=3+ formally-marked parallel series, J1 wins regardless of whether a merge-rule is also firing. The N=2 vs. N=3+ cliff is principled: two items invite bonding (doublet reading); three or more invite cataloguing (series reading).

**Scope of the N=3+ cliff.** Applies to coordinate **predications** (compound verbs under shared auxiliary, coordinate that-clauses, coordinate finite clauses). Does NOT apply to coordinate **objects** under a single shared verb — those are governed by J1's compound-list-break-signals sub-rule.

## §1.10 Punctuation is not a break signal

The source text's punctuation is preserved for fidelity but has **no deterministic role** in line-break decisions. Periods, commas, semicolons, colons, em-dashes, and question marks mark orthographic and grammatical pauses in the printed text, but they do not encode the atomic-thought boundaries the apparatus reveals. A break MAY coincide with a punctuation mark, but the mark does not license the break — syntax does.

**Test.** If the only reason cited for a break is "there's a comma here" or "the sentence ends," the break is not affirmed. Find the syntactic feature or merge.

Punctuation in canonical texts was added or revised by editors over time and reflects editorial decisions the apparatus is not trying to preserve or privilege.

**What the apparatus DOES preserve.** Every punctuation mark from the source text stays in place. The apparatus does not alter, add, or remove punctuation. Line breaks are the only editorial tool.

## §1.11 Versification is not a break signal

Verse divisions in canonical texts are editorial overlay (same status as punctuation). No break versification imposes is canonical. If a cross-verse merge case is identified, flag per the applicable Category (§2).

## §1.12 Parallel-List Uniformity Principle

When a multi-verse list of parallel members exists with a shared explicit frame, list members receive uniform line-treatment regardless of their individual syntactic shape. Per-construction rules yield to the list-uniformity principle within the list's scope.

**Trigger.** All four conditions MUST hold:
1. **Multi-verse list, N≥3 members.** Two-member coordinate cases are governed by §1.9; isolated occurrences aren't a list.
2. **Shared explicit frame.** A repeated lexical anchor introduces each member.
3. **Parallel members.** Each list-item is the same kind of thought.
4. **Authorial-symmetric.** Members do NOT have the finite-verb-count or predicative-head-count asymmetries that §1.13 protects.

**Default direction.** Uniform treatment of all members under the dominant pattern. Outliers conform to the majority.

**SCOPE — does NOT apply to:**
- N=2 coordinate cases (governed by §1.9).
- Authorial-asymmetric series (§1.13 takes precedence).
- Lists without a repeated explicit frame.
- Within-verse coordinate predications (governed by the N=3+ cliff — J1 wins over merge-rules at N≥3).

## §1.13 Authorial asymmetry overrides editorial symmetry

When a passage contains a serial construction (wo/blessed series, positive/negative conditional pair, beatitude chain, interrogative chain) and the author treats members asymmetrically — expanded mechanism for some, compact for others — **preserve the authorial asymmetry**. Do not pressure compact members to expand, or expanded members to compress, in order to achieve uniform line-treatment across the series.

**Test.** Count the finite verbs, elided verbs, and predicative heads in each member of the series. If counts differ between members in the received text, the asymmetry is authorial and the line-structure reflects it. If counts match but editorial line-treatment diverges, that is editorial drift and should converge.

**SCOPE.** Does NOT apply to same-rule-uniformly-applied cases — `feedback_application_consistency_vs_rule_coverage` (see [`../memories/`](../memories/)) governs those (same rule, inconsistent application). §1.13 governs the distinct failure mode: imposed uniform structure where the author wrote variation.

---

# Part III — Autonomy Boundary

## §2 Categories A / B / C

Every proposed change falls into one of three categories:

- **Category A — Editorial slippage.** Suboptimal break with no theological or rhetorical stakes. Apply confidently.
- **Category B — Rhetorical shape.** The break changes how the speaker builds an argument. Flag and ask before applying.
- **Category C — Theological / textual-critical weight.** Break placement carries doctrinal or textual-critical implication. Flag and discuss before touching.

**Mechanical-rule authority.** When a settled mechanical rule's UD signature fires unambiguously and the rule's heuristics resolve without ambiguity, the change is **Category A by default**. The canon IS the approval — no per-item flagging is required. Bump to Category B only when rhetorical weight is independently implicated. Bump to Category C only when theological weight is independently implicated. **Default-bumping mechanical hits to B out of caution is a failure mode** — it inverts the canon's authority and creates unnecessary friction.

**Default.** When uncertain between mechanical and non-mechanical, treat as mechanical if the UD signature is clean. When uncertain between A and B/C on editorial/rhetorical grounds, treat as Category B.

**Scope/precedence/closed-list diagnostic.** Canon additions that include ANY of the following are **Category B by default**, regardless of how they are framed:
- A scope claim (*"rule X applies to / does not apply to Y"*)
- A precedence claim (*"rule A trumps rule B"*)
- A closed-list extension (adding a verb class, a named category, a SCOPE-exclusion item)
- A named-category carve-out (introducing a new gating category)

This diagnostic catches the failure mode where a canon change is self-framed as "documenting existing practice" or "scope clarification" but substantively asserts a new judgment. §7 operationalizes this diagnostic for commit-time discipline.

---

# Part IV — Change Protocol

## §7.1 Authority

This document is the authoritative specification of the framework, categories, and change protocol. Per-corpus canons reference this document by stable section ID. They MUST NOT inline framework prose.

## §7.2 Proposal requirements

Proposals to change an existing rule, add a new rule, or retire a rule MUST:

1. **State the target-language syntactic fact.** Cite the UD label and traditional-grammar vocabulary. If no such fact can be cited, the proposal is insufficient.
2. **Provide corpus evidence.** Worked examples from the actual text — not hypotheticals.
3. **Survive adversarial audit** (when any mandatory-audit trigger fires; see §7.3).
4. **Apply uniformly.** If the rule fires in one place, run the validator or equivalent sweep to catch every instance. Sedimented inconsistency is the primary failure mode.
5. **Defensibility capture.** Every new rule, sub-rule, or merge-override added to the canon MUST carry three elements:
   - **WHY** — the editorial reason the rule exists.
   - **HOW WE KNOW** — corpus evidence + adversarial validation.
   - **SCOPE** — where the rule applies, where it doesn't, interaction with other rules.
   
   These elements live in the per-rule scholarship file (`scholarship/<rule-id>.md`), not in the operational canon entry.
6. **Re-evaluate deferred items when the rule-set changes.** Items previously classified as REVIEW-REQUIRED or deferred-editorial MUST be re-evaluated against the updated rule-set.
7. **Update the canon.** Per-change rationale (audit-dispatch evidence, retraction precedent, scope claim) lives in the commit message — the durable audit trail. The canon prose itself reads as the current method. Never edit history silently.

## §7.3 Mandatory-audit triggers (12 categories)

For proposals matching ANY of the following triggers, an adversarial audit (hostile-agent dispatch or equivalent external skeptical review) MUST be dispatched and its findings reflected in the commit. Skipping audit on a triggered proposal is a protocol violation.

1. **New named rules / sub-clauses / categories** — including precedence cross-references between rules.
2. **Rule status promotions** — *proposed* → *settled*. Removes the hedge; stakes increase.
3. **Spot-check-based proposals** — any canon claim resting on less than full-corpus-sweep evidence.
4. **Reclassification of canon-recorded Category B/C items** — once recorded, subsequent sessions cannot silently reclassify under a different rule-framing.
5. **Rule deletions or SCOPE narrowings that retire live applications** — retiring a rule is as high-stakes as adding one.
6. **Mechanical signature / validator changes under settled rules** — adding a verb class, refining a UD trigger, changing validator conditions silently expands or contracts rule coverage.
7. **Corpus sweeps ≥5 instances under a settled rule** — the collective scope-claim needs audit even when individual instances are Category A.
8. **Canonical example additions to settled rules** — examples shape rule interpretation.
9. **Meta-rule changes to §7 Change Protocol itself.**
10. **Discipline-shifting memory file additions** — new memory files that shape how the apparatus is operated are behaviorally-governing.
11. **Cross-project imports or recoveries from retired canon** — provenance from a sibling project or older version is not validation; the imported claim MUST have target-corpus evidence independent of its source.
12. **Corpus-fit verification — post-codification AND post-detection.**
    - **(a) Post-codification.** When a new rule, sub-clause, or named pattern is codified, the rule is **not "closed" until a corpus-wide goal-fit audit has confirmed** (i) all eligible instances conform OR (ii) all residuals are explicitly enumerated. Codifications based on partial-corpus evidence are vulnerable to undercount.
    - **(b) Post-detection.** This trigger ALSO fires when an existing (settled) rule's violation is detected. Application drift accumulates on long-codified rules. Schedule same-rule full-corpus re-sweep within the same session or as the next session's first task. Goal-fit failures cluster — finding one of a shape elsewhere is the predictable outcome of partial-sweep history.

**Audit dispatch — parallel by default.** When a proposal triggers multiple audit dimensions, dispatch all in a single message with multiple agent calls. Sequential only when audit A's verdict determines whether audit B should run.

## §7.4 Audit-skippable categories

All of the following MUST hold for a proposal to bypass audit:

- Category A mechanical corpus edits per already-codified rules (sweep-scale ≥5 still triggers #7 regardless).
- Typo fixes; cross-reference updates that don't assert precedence; internal formatting cleanups.
- Deletions of items already reverted in the same session (audit-trail cleanup).
- Defensibility-capture additions (WHY/HOW WE KNOW/SCOPE) to already-settled rules **without changing the rule's scope**.

## §7.5 Audit-evidence in commit messages

Every commit message that touches a per-corpus canon MUST declare audit-status explicitly:

- `Audit-skippable per §7.3 ([reason])` with the reason citing one of §7.4 categories; OR
- `Audit dispatched: [evidence]` with concrete reference (parallel-agent verdicts, prior-commit pointer).

Omission is itself a discipline failure — visible at a glance in `git log`. The mechanical commit-msg gate detects extension patterns and requires an audit-evidence keyword; the explicit declaration is the editor-side discipline that front-loads (and complements) the gate.

## §7.6 Self-test before commit

Before committing a canon change, run the five-question self-test:

1. Does this change include a scope claim, a precedence claim, a closed-list extension, or a named-category carve-out? → audit.
2. Does this change rest on spot-check evidence rather than a full-corpus classification? → audit.
3. Does this change reclassify or delete previously-settled canon content? → audit.
4. Did this session codify a new rule or named pattern, AND has the corpus-fit sweep NOT yet been run on the full corpus? → run goal-fit + application-consistency audits before commit, OR enumerate residuals in the session's pending file as next-session FIRST item.
5. If no to all four → probably skip-safe.

## §7.7 Self-consistency audit trigger

When a session adds ≥2 new canon subsections, rules, or merge-overrides, run a light self-consistency audit before wrap:

- All new cross-references resolve.
- No new rule contradicts an existing rule.
- All three defensibility elements (WHY / HOW WE KNOW / SCOPE per §7.2) are captured for each addition (in the scholarship companion, not the canon).

Short pass; catches stale cross-refs and incompatibilities cheaply.

## §7.8 Proposed-rule adoption protocol

A rule labeled *proposed* is a rule awaiting corpus verification. "Proposed" is a testable state, not a hedging license.

**Adoption criteria.** A proposed rule is adopted when its first corpus sweep produces **≥80% clean categorization** — 80%+ of matched instances resolve to unambiguous SPLIT or MERGE decisions without heuristic ambiguity. Ambiguous residue ≥20% signals the rule needs refinement before adoption.

**Sweep-then-decide workflow.**
1. Write validator implementing the rule's conditions.
2. Run against full corpus.
3. If clean ≥80% → apply clean decisions mechanically (Category A per §2), remove "proposed" label; capture the adoption evidence (sweep counts, audit verdicts) in the commit message.
4. If clean <80% → identify the ambiguity pattern, refine the rule with an explicit sub-clause, re-run.
5. Repeat until clean ≥80%, then adopt.

**Do not flag clean categorizations for per-item review.** A proposed rule whose conditions are met is as authoritative as an adopted rule on those specific instances; the "proposed" label only gates corpus-wide sweep confidence, not per-instance application.

---

*End of framework specification. For rationale, intellectual lineage, and empirical evidence supporting each section, see the [scholarship companion](../scholarship/methodology/). For per-corpus rule detail (§5), see each reader edition's `private/01-method/colometry-canon.md`.*
