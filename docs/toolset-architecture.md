# Toolset architecture — cognitive-labor partitioning

The ATU apparatus identifies Atomic Thought Units in a source text by partitioning the work across three stages: cognitive identification (LLM applying the bidirectional test), syntactic constraint audit (rule catalog answering grammatical yes/no questions), and editorial review (human adjudicates conflicts). The architecture is feasible at scale because each stage handles a task type fit for the kind of agent doing it.

This document is normative for any project consuming `atu-method`. It complements `architecture.md` (four-planes engineering separation: data / specification / tooling / delivery) by describing which TASK TYPE each stage is fit for.

---

## What an ATU is

An ATU is the smallest cognitive chunk an attentive reader processes as a discrete unit. One ATU per line in the rendered output. The criterion for ATU well-formedness is the **bidirectional test**:

A line is a legitimate standalone ATU if and only if BOTH:

1. **Forward grammatical closure** — the line is grammatically complete: subject + verb + obligatory complements present such that the line can stand syntactically on its own. For languages with morphologically-encoded subjects (Hebrew finite verbs, Greek finite verbs, Latin finite verbs), the subject does not need to be lexically present on the line; the verb's inflection supplies it. Verbless / nominal-predicate constructions count as closed when subject + predicate are juxtaposed (Hebrew, Greek). EME English requires overt copula.

2. **Backward referential self-containment** — the line's referents are either established in prior discourse (immediately, via chain-continuity) or self-introducing within the line. Long-range antecedent dependencies (more than one ATU back, no chain continuity) fail backward containment.

A break between two adjacent lines is licensed if and only if both lines independently satisfy these two conditions.

The bidirectional test is the criterion. Surface signals (coordination, parallelism marks, te'amim hierarchical disjunctives, editorial punctuation) generate candidate breaks but do not license them. Parallelism is a poetic-rhetorical feature operating on a separate axis from ATU rendering: parallel cola where each colon independently passes the bidirectional test are separate ATUs regardless of whether the parallelism is synonymous, antithetic, or synthetic.

---

## The three-stage pipeline

```
Source text (with verse markers, optional pre-existing line breaks)
  ↓
Stage 1 — LLM ATU identification (minimal rubric prompt)
  ↓
Stage 2 — Constraint catalog audit (syntactic yes/no questions)
  ↓
Stage 3 — Editorial review (human adjudicates conflicts)
  ↓
Final ATU rendering
```

### Stage 1 — LLM identification (minimal rubric)

The LLM is the primary identifier. It reads source text and proposes ATU-segmented output by applying:

1. The bidirectional test (forward closure + backward containment)
2. Restrictive relative clause binding — restrictive relatives bind to their head noun regardless of internal completeness
3. A small set of language-specific syntactic constraints (see per-language minimal rubric documents):
   - Hebrew: gapped finite verb tolerance in immediate parallel cola; speech-intro + short particle-led reply/vocative binding; discourse-particle binding (`לָכֵן`, `הִנֵּה`, `אַשְׁרֵי`, etc.)
   - Greek: aorist-participle attendant-circumstance binding; speech-frame binding; restrictive `ὅς` / `ὅπου` binding; purposive-infinitive binding
   - EME English: discourse-particle binding ("behold", "wherefore", "yea"); restrictive "which" / "who" / "that" binding; "and it came to pass" frame handling
4. Default KEEP-AS-IS unless a rule affirmatively fires.

The LLM does NOT apply: cognitive-unity gates on parallel cola; parallelism class adjudication (synonymous / antithetic / synthetic categorization); genre anchors as primary licenses. These are off-axis from ATU identification.

The output of Stage 1 is a proposed rendering — ATU-segmented text per chapter, ready for audit.

### Stage 2 — Constraint catalog audit

The constraint catalog is a per-language inventory of syntactic constraints, each expressed as a yes/no grammatical question. Constraints AUDIT the Stage-1 proposal; they do not produce ATU rendering.

Each constraint:

- Encoded question (yes/no): "Is this break inside a construct chain?" "Is this `אֲשֶׁר`-clause restrictive?" "Is this `וְ` coordinating two finite verbs with the same subject?"
- Verdict family: BIND / SPLIT-CANDIDATE / MERGE / VIOLATION-FLAG / NO-EFFECT
- Source reference: grammar authority (Joüon-Muraoka §X for Hebrew, Smyth §Y for Greek, etc.)
- Diagnostic examples (positive and negative)
- Edge-case handling

The catalog is organized by language:

- **Hebrew Constraint Catalog**: Joüon-Muraoka primary (§158 relatives, §159 subordinates, §170–177 coordination, §150 verbless, §121 participles, §174 gapping, §155 construct chains, §164–169 conditionals); GKC, Waltke-O'Connor as cross-reference.
- **Greek Constraint Catalog**: Smyth primary; Wallace, Robertson, Funk as cross-reference.
- **EME English Constraint Catalog**: Cawdrey, Skousen *Critical Text*, EME grammar references.

Audit output: a violation report per proposed ATU break, flagged for editorial review. Constraints DO NOT auto-correct the proposal; they surface conflicts.

### Stage 3 — Editorial review

Stan (or the corpus editor) adjudicates between the Stage-1 proposal and Stage-2 violations. Output is the final ATU rendering, committed to the corpus's `data/text-files/v2/` directory.

For chapters where the editor has already produced a hand-validated rendering (e.g., Psalm 1 baseline), Stages 1–2 run as a verification cross-check, not as a replacement.

---

## The coarse-anchor principle

**The mechanical anchor should be the coarsest reliable signal, not the finest possible signal.** Finer signals introduce more potential break-points than are warranted; the LLM identification stage decides actual ATU boundaries.

| Corpus | Coarse anchor (primary) | Informational signals | Adjudicator |
|---|---|---|---|
| Tanakh (prose) | Versification | Te'amim, editorial punctuation | LLM + bidirectional test |
| Tanakh (poetry) | Versification | Te'amim, parallelism marks | LLM + bidirectional test |
| GNT | Versification | Strong's, Macula constituency, editorial punctuation | LLM + bidirectional test |
| Latin (Vulgate, planned) | Versification | UD-Latin dependency, medieval punctuation | LLM + bidirectional test |
| BoFM | Versification (Skousen-anchored) | Stanza UD, editorial punctuation | LLM + bidirectional test |

**Te'amim** are PERFORMANCE anchors (oral cantillation hierarchy: pause-points for breath, pitch contours for melisma), not COGNITIVE anchors (atomic-thought boundaries). They correlate with syntactic structure because chanting follows syntax, but the correlation is not isomorphism. Treating te'amim as ATU-adjudicators introduces systematic over-segmentation. For poetry specifically, te'amim track parallelism reliably and so are more useful than for prose, but they remain informational, not adjudicative.

**Editorial punctuation** (KJV / Stephanus / Masoretic) was added by editors who were making cognitive segmentation decisions, however inexpert. Their decisions are a noisy signal of where someone thought a cognitive boundary was. Noisy ≠ useless. Punctuation contributes candidate breaks without binding the adjudication.

---

## Two-phase processing model

The architecture separates "what signals are available" from "what signals determine the segmentation":

### Phase A — Candidate signal generation (mechanical, cheap)

Every available signal contributes candidates; no signal binds.

- Versification (coarsest; high reliability as a boundary)
- Major punctuation (period, full stop)
- Minor punctuation (comma, colon) when available and trustworthy
- UD-parser sentence boundaries
- Te'amim / accent-marks (Hebrew / Greek) — informational only
- Strong's / Macula / TAHOT anchoring data

Output: source text with annotated candidate signals. Denser than the eventual ATU rendering.

### Phase B — ATU identification + audit (LLM-cost-bearing)

- LLM identifies ATUs per minimal rubric (Stage 1 above)
- Constraint catalog audits the proposal (Stage 2 above)
- Editorial review resolves conflicts (Stage 3 above)

Phase A is cheap and deterministic; Phase B is the LLM-cost-bearing layer but operates on a bounded set of decisions, not free-form text.

---

## Meta-discipline layer

The pipeline relies on disciplines governing HOW the stages are used:

- **§7.3 audit gate** (`change-protocol.md`) — discipline-floor for closed-list / new-rule / new-subtype proposals. ≥2 parallel adversarial agents pre-build. New constraint catalog entries and rubric refinements gate through this.
- **Retraction-log protocol** (`retraction-log-protocol.md`) — 3-strike threshold; per-repo `retraction-log.md`; catches discipline drift over time.
- **Directive-queue protocol** (`memories/feedback_directive_protocol.md`) — async cross-repo coordination via `directives/pending/` → `processed/` + `replies/`. Canonical trigger word: `directive`.
- **Compaction-resume protocol** (`memories/feedback_compaction_resume_protocol.md`) — JSONL re-read on context loss to preserve fidelity.
- **Canon-validator alignment protocol** (`canon-validator-alignment-protocol.md`) — keeps canon prose synchronized with constraint catalog implementations.
- **Three anti-default factors** (`memories/feedback_three_anti_default_factors.md`) — Factor A surface-feature smuggling, Factor B new-rule reflex, Factor C sample-size discipline.
- **Rule-proposal gates** (`memories/feedback_rule_proposal_gates.md`) — four pre-proposal gates before any new constraint is drafted.
- **Architecture-method alignment** (`memories/feedback_architecture_must_match_method.md`) — periodic check that the as-built architecture matches what the method claims; the bidirectional test identifies ATUs cognitively, syntactic rules audit them.

---

## Cross-corpus structure

The pipeline is corpus-agnostic. Each corpus instantiates:

1. **Data layer**: source text, version-anchoring (TAHOT for Tanakh, Strong's for GNT, Skousen for BoFM), Macula constituent trees or equivalent UD parses, render-pipeline file structure
2. **Minimal rubric prompt**: language-specific bidirectional-test extension document under `scripts/atu_pipeline/prompts/`
3. **Constraint catalog**: language-specific syntactic catalog (Hebrew / Greek / EME English / Latin / etc.)
4. **Editorial review surface**: per-repo workflow for adjudicating Stage-1-vs-Stage-2 conflicts

The architecture is shared; the per-corpus work is real (source text anchoring, grammar-source mining for the catalog, editorial calibration on first chapters).

---

## The methodological claim this architecture supports

Structural-segmentation criticism is feasible at scale because cognitive labor is partitioned across an LLM identification stage (cheap per-instance judgment fit for cognitive chunking), a constraint catalog audit stage (deterministic grammatical questions), and an editorial review stage (human adjudication where the prior two conflict). Pre-LLM, the same framework would have required months of human work per book; LLM-alone would hallucinate too freely; mechanical-alone misses cognitive-segmentation judgments deterministic rules cannot encode. The three-stage partitioning is a coverage-and-efficiency claim.

**What this claim extends to:**

- The discipline-floor (§7.3 + retraction-log + canon-validator alignment + architecture-method check) is what makes the partitioning trustworthy under fast iteration. Without it, the LLM and audit stages would accumulate silent inconsistency.
- Cross-corpus port benefits from the shared architecture and discipline-floor; the spin-up timeline depends on per-corpus anchoring, catalog construction, and editorial calibration, not on the architecture itself.

**What this claim does NOT extend to:**

- The architecture does not claim the three stages cover every editorial failure mode. Mature corpus work continues to surface calibration items; these get added to the rubric or the constraint catalog over time per §7.3 discipline.
- The architecture does not claim the LLM stage is methodology-shifting. It is the cognitive identifier; without it, the bidirectional test would be applied by hand. The LLM does identification at scale; it does not redefine the criterion.
- The architecture does not claim cross-corpus port is free. Each new corpus requires its own anchoring infrastructure, its own constraint catalog, and its own editorial calibration. The methodology gives a template; the per-corpus work is real.

---

## Cross-references

- `framework.md` — universal framework structure (§0 / §1 / §2 / §7)
- `architecture.md` — four-planes engineering separation (data / spec / tooling / delivery)
- `apparatus.md` — system-level claims about what the apparatus is for
- `change-protocol.md` — §7.3 audit triggers and the change-protocol governing rule modifications
- `rule-equivalence-map.md` — cross-corpus constraint porting
- `rule-template.md` — operational template for constraint-catalog entries
- `retraction-log-protocol.md` — discipline-drift safeguard
- `canon-validator-alignment-protocol.md` — keeping canon prose synced with catalog implementations
- `memories/feedback_directive_protocol.md` — cross-repo coordination
- `memories/feedback_three_anti_default_factors.md` — rule-proposal anti-pattern catalog
- `memories/feedback_compaction_resume_protocol.md` — context-loss recovery
- `memories/feedback_architecture_must_match_method.md` — periodic alignment check
