# Framework — Methodology Specification

This document is the canonical statement of the methodology framework shared across all atu-method reader editions. It is operational — consumed by LLM agents, validators, and editorial discipline. Rationale, defensibility arguments, and intellectual lineage live in the [scholarship companion](../scholarship/) and are deliberately absent here.

Per-corpus canons cite this document by stable section ID (e.g., "see `atu-method/docs/framework.md §1.3 Bidirectional test`"). They MUST NOT inline framework prose.

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

The apparatus DOES format text so that any reader — from ESL or child all the way to serious researcher — can take canonical scripture one atomic thought at a time.

## §0.2 Method

**Cognitive identification first; syntactic constraints second.** The bidirectional test (§1.3) is the criterion for whether a line is an atomic thought unit. Syntactic rules (per-language constraint catalogs) audit proposed ATU boundaries; they do not generate them. Parallelism is a poetic-rhetorical feature operating on a separate axis from ATU rendering.

The asymmetry: cognition determines, grammar constrains. Stan verbatim 2026-05-13: *"grammar doesn't determine ATU boundaries, but it can constrain them."*

## §0.3 Pragmatic stance

This methodology is a set of conventions reflecting what the apparatus is trying to reveal. It is not derived from a cognitive theory; no such claim is asserted. The apparatus operates as what it is: a consistently-applied editorial practice grounded in the bidirectional test, audited against the target language's syntactic constraint catalog, and refined by editorial review.

## §0.4 Scope

Each per-corpus instantiation of this framework governs **where lines break** in its source texts. It does NOT govern:

- Punctuation (inherited from the source; preserved unchanged)
- Words (never added, removed, or altered)
- Layout beyond break positions
- External editorial overlays (te'amim, NA28 paragraph structure, ancient codex colometric arrangements — informational only)

---

# Part II — The Framework

## §1.1 What an ATU is

An ATU is the smallest cognitive chunk an attentive reader processes as a discrete unit. One ATU per line in the rendered output.

## §1.2 The bidirectional test (the criterion)

A line is a legitimate standalone ATU if and only if BOTH:

1. **Forward grammatical closure** — the line is grammatically complete on its own terms in the target language. Languages with morphologically-encoded subjects (Hebrew finite verbs, Greek finite verbs, Latin finite verbs) license pro-drop; the verb's inflection supplies the subject. Verbless / nominal-predicate constructions count as closed when subject + predicate are juxtaposed (Hebrew, Greek). EME English requires overt copula.

2. **Backward referential self-containment** — the line's referents are established in prior discourse (immediately, via chain-continuity) or self-introducing within the line. Long-range antecedent dependencies (more than one ATU back, no chain continuity) fail backward containment.

A break between two adjacent lines is licensed if and only if both lines independently satisfy these two conditions.

**The bidirectional test is asymmetric:**

- **Anaphoric failure** (backward-dangling): a line whose referents are anaphoric to prior context — pronouns without antecedent on the line, deictic demonstratives ("these things," "that day," "the same"), discourse-anaphoric particles ("therefore," "thus," `לָכֵן`, `עַל־כֵּן`, causal `כִּי`) — fails backward containment.
- **Cataphoric introduction** (forward-pointing) does NOT fail: presentative `הִנֵּה` + indefinite NP introducing new content, or "thus says X:" announcing speech about to follow, is licensed because the forward content is being introduced, not depended on.

Canonical example: Gen 22:1 `wayehi achar ha-devarim ha-eleh` ("and it came to pass after these things") is NOT an ATU on its own line — `ha-devarim ha-eleh` ("these things") is a deictic pointer to undefined antecedent narrative. The whole construction (frame + apodosis) is one ATU because the frame is referentially anaphoric and the apodosis is what the frame opens into.

## §1.3 Restrictive relative clause binding

Restrictive relative clauses bind to their head noun and cannot stand as separate ATUs regardless of internal completeness. Diagnostic: would removing the relative clause leave the head uniquely identified? If no → restrictive → bind.

This is universal across the framework's target languages (Hebrew `אֲשֶׁר` / `שֶׁ`, Greek `ὅς` / `ὅστις` / `ὅπου`, EME English "which" / "who" / "that").

Non-restrictive (descriptive) relative clauses may stand alone as ATUs when they pass the bidirectional test AND the head is already identified.

## §1.4 Default action

KEEP-AS-IS unless the bidirectional test fails or the restrictive-relative binding rule fires. The framework does not include affirmative cognitive-unity gates, parallelism class adjudication, or genre anchors as primary licenses. The bidirectional test is the criterion; constraints audit the proposal.

## §1.5 Per-corpus constraint catalog

Each per-corpus canon maintains a constraint catalog encoding language-specific syntactic constraints as yes/no grammatical questions:

- **Hebrew** (Joüon-Muraoka primary; GKC and Waltke-O'Connor cross-reference): construct chain bare-governor indivisibility, verbless clause closure, participial predication, gapped-verb tolerance in immediate parallel cola, discourse-particle binding, conditional protasis in legal-casuistic, coordinate-vs-subordinate `וְ`, restrictive-vs-non-restrictive `אֲשֶׁר`.
- **Greek** (Smyth primary; Wallace, Robertson, Funk cross-reference): genitive-absolute closure, attendant-circumstance participle binding, restrictive `ὅς` / `ὅπου` binding, purposive-infinitive binding, speech-frame binding, articular-infinitive nominal handling, apposition.
- **EME English** (Cawdrey, Skousen *Critical Text*, EME grammar references): discourse-particle binding ("behold," "wherefore," "yea"), "and it came to pass" frame handling, coordinate-vs-subordinate "and" / "for," restrictive "which" / "who" / "that" binding.
- **Latin** (planned): TBD per Allen-Greenough.

Constraints AUDIT a proposed ATU rendering. They do not generate ATU rendering. Producer-style framing ("split parallel clauses," "merge synonymous cola," "split at clause boundary") is forbidden.

See [`rule-template.md`](rule-template.md) for the operational template every constraint catalog entry follows.

---

# Part III — The Three-Stage Pipeline

## §2.1 Stage 1 — LLM identification (minimal rubric)

The LLM is the primary identifier. It reads source text and proposes ATU-segmented output by applying the bidirectional test (§1.2), restrictive-relative binding (§1.3), and a small set of language-specific syntactic constraints supplied via the per-language minimal-rubric prompt.

The minimal rubric does NOT include cognitive-unity gates on parallel cola, parallelism class adjudication (synonymous / antithetic / synthetic categorization), or genre anchors as primary licenses. These are off-axis from ATU identification.

**Production protocol: Opus 3-pass with agreement scoring.** Three independent passes; unanimous verdicts auto-apply; non-unanimous verdicts surface to editorial review. Empirically validated 2026-05-17 across prose and poetic content in Hebrew, Greek, and EME English. See `toolset-architecture.md` for the production tier specification and `memories/feedback_production_tier_empirical.md` for the empirical study.

Output: a proposed rendering — ATU-segmented text per chapter, ready for audit.

## §2.2 Stage 2 — Constraint catalog audit

The constraint catalog audit runs each constraint entry against the proposed rendering and emits a violation report per proposed break.

Constraint format (yes/no grammatical questions):

- "Is this break inside a construct chain (bare governor + genitive)?" → if yes, MERGE
- "Is this `אֲשֶׁר`-clause restrictive (head not uniquely identified without it)?" → if yes, BIND
- "Is this `וְ` coordinating two finite verbs with the same subject?" → if yes, candidate SPLIT
- "Is this colon's finite verb gapped from the immediately preceding parallel colon?" → if yes, COUNT AS CLOSED
- (and so on)

Constraints do not auto-correct the proposal; they surface conflicts.

## §2.3 Stage 3 — Editorial review

The editor adjudicates between the Stage-1 proposal and Stage-2 violations. Output is the final ATU rendering, committed to the corpus's `data/text-files/v2/` directory.

For chapters where the editor has already produced a hand-validated rendering, Stages 1–2 run as a verification cross-check, not as a replacement.

---

# Part IV — Cross-Corpus Pattern

## §3.1 Per-corpus instantiation

The framework is corpus-agnostic. Each corpus instantiates:

1. **Data layer**: source text, version-anchoring (TAHOT for Tanakh, Strong's for GNT, Skousen for BoFM), Macula constituent trees or equivalent UD parses, render-pipeline file structure
2. **Minimal rubric prompt**: language-specific bidirectional-test extension under `scripts/atu_pipeline/prompts/`
3. **Constraint catalog**: language-specific syntactic catalog
4. **Editorial review surface**: per-repo workflow for adjudicating Stage-1-vs-Stage-2 conflicts

## §3.2 Cross-corpus constraint equivalence

Some constraints map directly across languages (restrictive relative binding, discourse-particle binding, gapped-verb tolerance). Others are corpus-unique (Hebrew construct-chain indivisibility, Greek genitive absolute, EME "and it came to pass" frame). The equivalence map lives in [`rule-equivalence-map.md`](rule-equivalence-map.md).

When porting to a new corpus, the existing equivalence map provides a starting catalog; corpus-specific extensions are added per the §7 change protocol.

---

# Part V — Change Discipline

## §7.1 Framework authority

This framework is the authoritative source for cross-corpus methodology. Per-corpus canons MAY extend (corpus-specific constraints), but MUST NOT contradict.

## §7.2 Proposal requirements

A proposal to add, modify, or retire a framework section MUST include:

- The encoded claim (what the proposal is asserting)
- The empirical evidence base (which corpus passages, what hand-verified baselines, what experiment results)
- The §7.3 audit triggers fired (if any)
- The cross-corpus impact assessment

## §7.3 Mandatory-audit triggers

See [`change-protocol.md`](change-protocol.md) for the 12 mandatory-audit triggers and the §7.3 / §7.4 audit-skippable distinction.

## §7.4 Self-test before commit

Before committing a framework change, the proposer MUST:

- Verify the proposed change does not contradict existing memories (especially `feedback_minimal_rubric_validated`, `feedback_architecture_must_match_method`, `feedback_three_anti_default_factors`)
- Verify the proposed change does not invent a producer-style rule when a constraint-form already exists
- Verify the proposed change has empirical evidence beyond a single test case

## §7.5 Retraction discipline

When a framework section is retracted, the retraction is recorded in the per-repo `retraction-log.md` per [`retraction-log-protocol.md`](retraction-log-protocol.md). The 3-strike threshold applies: three retractions of related sections trigger a structural review of the relevant Part.

---

## Where to read next

- [`apparatus.md`](apparatus.md) — High-level scope and output description
- [`architecture.md`](architecture.md) — Four-plane technical architecture
- [`toolset-architecture.md`](toolset-architecture.md) — Cognitive-labor partitioning across the toolset
- [`rule-template.md`](rule-template.md) — Operational template for constraint catalog entries
- [`change-protocol.md`](change-protocol.md) — Audit-extension rules for canon changes
- [`../memories/`](../memories/) — Cross-project discipline lessons
