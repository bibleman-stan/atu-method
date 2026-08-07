# Toolset architecture — cognitive-labor partitioning

The ATU apparatus is feasible at scale because cognitive labor is partitioned across **four substantive legs** plus a **meta-discipline layer**. Each leg handles a different task type; the system-level capability emerges from the combination. Pre-LLM, the framework would have required months of human work per book; LLM-alone hallucinates too freely; mechanical-alone misses too much. The methodological contribution isn't only the ATU theory — it's the ATU theory + the discipline-floor + the cognitive-labor partitioning that makes it executable across corpora.

This document is normative for any project consuming `atu-method`. It complements `architecture.md` (which describes the four-PLANES engineering separation — data / specification / tooling / delivery). Where `architecture.md` describes where code and data live, this document describes which TASK TYPE each tool is fit for.

---

## The four substantive legs

### Leg 1 — Mechanical floor

Cheap, deterministic, scales freely. Handles tasks with crisp answers.

- **UD parsing** (Stanza for Hebrew / Greek / Latin / English). Token boundaries, POS tags, dependency arcs.
- **Layer-1 prohibitions** (universal grammatical floor). Hard constraints — no break inside a noun phrase, no break between a verb and its obligatory complement, etc.
- **Source-text anchoring** — Strong's (GNT), TAHOT (Tanakh), corpus-equivalent per-repo.
- **Coarse-anchor candidate-break generation** (see `Coarse-anchor principle` below).

Status: in place across BoFM / GNT / Tanakh. Cross-corpus port-ready for LXX / Vulgate via Stanza-compatible UD treebanks.

### Leg 2 — Point-rule validators (R/H stack)

Pattern-specific break-legality checks. Each rule encodes a known structural pattern and the editorial verdict on how that pattern segments. Mechanical execution; audit-discipline-gated.

- Per-rule mechanical checks (R19 acl:relcl, R17 ὅτι complementizer, H5 messenger formula, etc.)
- §7.3 mandatory-audit triggers gate the proposal of new rules, closed lists, or sub-categories (see `change-protocol.md`)
- Cross-corpus rule-equivalence map (`rule-equivalence-map.md`) tracks which rules port directly, which re-instantiate, which are corpus-unique

Status: in place across all reader-repos; maturing. The §7.3 audit gate has fired twice in observed practice (BoFM-2203 Option E parser-suspect; GNT-2400 Pass D alignment rules) — catching design defects before code lands.

### Leg 3 — LLM resolver for validator-flagged residue

Per-instance judgment within bounded rule scope. Operates on the REVIEW residue that point-rule validators flag as needing editorial adjudication.

- Reads validator-flagged cases with full rule context
- Applies the bidirectional test (see `Extended bidirectional test` below) per instance
- Returns verdict + confidence + reasoning
- Agreement-scoring across multiple runs surfaces resolver self-consistency
- Auto-apply gate (unanimous-all-high-confidence-STRONG-MERGE) extracts mechanical wins from the LLM's judgment

Status: demonstrated via BoFM R19 work (`scripts/resolve_review_required.py`). 75-case calibration showed ~87% unanimous agreement; ~73% auto-applicable at the unanimous-all-high gate. Pattern extends to any rule with a defined ambiguity surface.

### Leg 4 — LLM passage-level audit over rendered output

**Coverage-extension** check that surfaces forward-closure and backward-containment failures the R/H validator stack does not enumerate. Operates over rendered v2 output (not UD parse input like Leg 3). Complementary to the validator stack, not competing with it.

- Reads the rendered ATU lines for a passage
- Applies the bidirectional test (forward grammatical closure + backward referential self-containment)
- Returns per-line verdicts (keep / merge-with-prior / merge-with-next / ambiguous) + proposed corrected rendering

What this leg legitimately catches (forward-closure or backward-containment failures NOT in the R/H validator catalog):

- **Bare speech verbs without obligatory complement** — narrative `וַיֹּאמֶר` alone on a line, with speech content on the next line, fails forward closure (speech verb requires speech content as obligatory complement)
- **Bare coordinate pronouns or NPs filling a single syntactic slot** — Deut 6:2 `אַתָּה / וּבִנְךָ / וּבֶן־בִּנְךָ` lines fail forward closure (no predicate of their own; all three pronouns appose a single matrix-clause subject)
- **Bare temporal infinitival PPs as adverbial modifiers** — Deut 6:7 `בְּשִׁבְתְּךָ / וּבְלֶכְתְּךָ / וּבְשָׁכְבְּךָ / וּבְקוּמֶךָ` are construct-infinitival PPs without their own finite verbs; adverbial modifiers of the matrix verb above them
- **Bare appositional / specifying PPs** — Deut 6:12 `מִבֵּית עֲבָדִים` is an appositive expanding `מֵאֶרֶץ מִצְרַיִם`; fails backward containment as a standalone line
- **Stranded subordinate clauses** — `כִּי`-clause / `אֲשֶׁר`-clause / `לְמַעַן`-clause separated from the matrix verb it modifies

What this leg does NOT do:

- It does NOT override Leg 2 (R/H validators) on cases where the validator's rule and the bidirectional test agree. For example, `validate_parallel_clause_split` correctly identifies two finite-verb-headed clauses on one line as candidates for splitting; the bidirectional test agrees (each clause is its own ATU). Leg 4 must not invent additional criteria (such as "cognitive unity of parallel cola") to override the validator's verdict; doing so smuggles colometric criteria into ATU theory.
- It does NOT adjudicate poetic-parallelism structure. Per `apparatus.md`, the apparatus deliberately does not "reveal rhetorical parallelism." Synonymous, antithetic, and synthetic parallelism are poetic features that operate on a different axis from ATU rendering; the bidirectional test treats each grammatically-complete clause as its own ATU regardless of the parallelism relationship it stands in.

Status: demonstrated 2026-05-16 via Deut 6:1-12 (deuteronomic prose) and Gen 22:1-12 (narrative). The tool correctly catches forward-closure failures that the R/H validator stack does not enumerate (bare elements, speech-frame extractions, appositives). The day-formula `וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר` refrains stand correctly as independent ATUs (well-segmented baseline), demonstrating the tool does not default to "merge everything."

Net over-breaking rate (forward-closure / backward-containment failures only) is substantive across the tested chapters but materially lower than the inflated rate claimed in the earlier draft of this section, which conflated genuine ATU-criterion failures with parallelism-relationship merges that were not in fact failures of the bidirectional test.

---

## The unifying rubric: bidirectional test

A line is a legitimate standalone ATU if and only if it satisfies BOTH:

1. **Forward grammatical closure** — the line is grammatically complete: subject + verb + obligatory complements present such that the line can stand syntactically on its own. For languages with morphologically-encoded subjects (Hebrew finite verbs; Greek finite verbs), the subject does not need to be lexically present on the line; the verb's inflection supplies it.
2. **Backward referential self-containment** — the line's referents are either already-established in prior discourse or self-introducing within the line.

A break between two adjacent lines is licensed if and only if BOTH lines independently satisfy these two conditions.

**Critical caveat — the bidirectional test is the criterion. Period.**

Surface signals — coordination (וְ / καί / et), parallelism marks, te'amim hierarchical disjunctives, editorial commas — DO NOT automatically license breaks. They generate CANDIDATES (Phase A below). The bidirectional test adjudicates which candidates become actual breaks (Phase B).

**The framework does NOT include a "cognitive-unity gate" or similar sufficiency extension for parallelism cases.** An earlier draft of this document proposed such an extension (synonymous / antithetic parallel cola jointly forming one propositional content collapse into one ATU). That extension was retracted on empirical and methodological grounds:

- It conflated poetic-rhetorical features (parallelism) with ATU criteria (cognitive chunking). Per `apparatus.md`, the apparatus deliberately does not adjudicate rhetorical parallelism.
- It contradicted `validate_parallel_clause_split` on the validator's canonical motivating case (Ps 23:2), and on direct examination the validator's verdict aligned with the bidirectional test applied honestly: each colon independently passes forward closure and backward containment; two ATUs.
- The "validations" of the extension across multiple chapters were circular — the audit agents were instructed with the extension as part of their rubric, then dutifully applied it. Successful application of a rule is not evidence the rule is correct.

**For parallel cola where each colon independently passes the bidirectional test, the verdict is two (or more) ATUs.** This holds regardless of whether the parallelism is synonymous, antithetic, or synthetic. Parallelism is a poetic feature operating on a separate axis from ATU rendering.

**Where parallel-looking cases ARE single ATUs**, the bidirectional test alone produces the merge verdict, without any parallelism-specific gate:

- A colon that is a bare prepositional phrase modifying a matrix verb on a different line (Deut 6:5 heart/soul/might tricolon; each `בְּכָל־X` lacks its own verb)
- A colon that is a bare construct infinitival adverbial without a finite verb (Deut 6:7 temporal "when you sit / walk / lie / rise" series)
- A colon that is a bare coordinate noun phrase with no predicate (Deut 6:2 `אַתָּה / וּבִנְךָ / וּבֶן־בִּנְךָ` apposition)
- A subordinate clause that depends on a matrix verb on another line (relative `אֲשֶׁר`-clause, causal `כִּי`-clause where the causal-`כִּי` is grammatically subordinate, infinitival purpose-clause)

In all these cases the bidirectional test produces the merge verdict via forward-closure failure, not via cognitive-unity. The verdict is empirically the same; the methodology is different. The methodology matters because the cognitive-unity framing produced the contradiction with `validate_parallel_clause_split`; the bidirectional-test-only framing does not.

---

## The coarse-anchor principle

**The mechanical anchor should be the coarsest reliable signal, not the finest possible signal.** Finer signals introduce more potential break-points than are warranted; the LLM-judgment layer is where actual ATU boundaries are decided.

| Corpus | Coarse anchor (primary) | Informational signals | Adjudicator |
|---|---|---|---|
| Tanakh (prose) | Versification | Te'amim, editorial punctuation | Bidirectional test |
| Tanakh (poetry) | Versification | Te'amim (more informative than for prose, but still non-adjudicative), parallelism | Bidirectional + cognitive-unity |
| GNT | Versification | Strong's, Macula constituency, editorial punctuation | Bidirectional test |
| Latin (Vulgate, planned) | Versification | UD-Latin dependency, medieval punctuation | Bidirectional test |
| BoFM | Versification (Skousen-anchored) | Stanza UD, editorial punctuation | Bidirectional test |

**Methodological note on te'amim:** te'amim are PERFORMANCE anchors (oral cantillation hierarchy: pause-points for breath, pitch contours for melisma), not COGNITIVE anchors (atomic-thought boundaries). They are correlated with syntactic structure because chanting follows syntax, but the correlation is not isomorphism. Trusting te'amim as ATU-adjudicators introduces systematic over-segmentation — confirmed empirically by the Deut 6 audit (9 of 12 verses over-broken). For poetry specifically, te'amim track parallelism reliably and so are MORE useful than for prose, but they remain informational, not adjudicative.

**Methodological note on punctuation:** editorial punctuation (KJV / Stephanus / Masoretic) was added by editors who WERE making cognitive segmentation decisions, however inexpert. Their decisions are a noisy signal of where someone thought a cognitive boundary was. Noisy ≠ useless. Punctuation contributes candidate breaks (Phase A) without binding the adjudication (Phase B). This is methodologically defensible against the standard "punctuation is just editorial" critique: we are not treating punctuation as a CRITERION for ATU determination; we are treating it as a CANDIDATE signal whose validity is then tested against the bidirectional rubric.

---

## Two-phase processing model

The architecture cleanly separates "what signals are available" from "what signals determine the segmentation":

### Phase A — Candidate-break generation (mechanical, multi-grained)

Every available signal contributes candidates; no signal binds.

- Versification (coarsest; high reliability as a boundary)
- Major punctuation (period, full stop, semicolon)
- Minor punctuation (comma, colon) — only when available and trustworthy
- UD-parser sentence boundaries
- Te'amim / accent-marks (Hebrew/Greek) — informational only
- Point-rule validator outputs (R/H stack — flags structural patterns)

Output: a candidate-break-annotated source text — denser than the eventual ATU rendering.

### Phase B — Adjudication (LLM + bidirectional test + cognitive-unity)

- Walk the candidate-break list
- For each candidate, apply the extended bidirectional test
- Reject candidates where the resulting lines fail forward closure or backward containment
- Reject candidates where rejecting preserves cognitive-rhetorical unity (parallel poetry case)
- Accept candidates that survive both gates
- Surface ambiguous candidates for editorial review

Output: the v2-rendered ATU segmentation, with confidence + reasoning per accepted/rejected break.

This two-phase separation is what makes scaling tractable. Phase A is cheap and deterministic; Phase B is the LLM-cost-bearing layer but operates on a bounded candidate set, not on free-form text.

---

## Meta-discipline layer (orthogonal but load-bearing)

The toolset architecture relies on disciplines that govern HOW the legs are used:

- **§7.3 audit gate** (`change-protocol.md`) — discipline-floor for closed-list / new-rule / new-subtype proposals. ≥2 parallel adversarial agents pre-build. Caught design defects in BoFM-2203 and GNT-2400 in observed practice.
- **Retraction-log protocol** (`retraction-log-protocol.md`) — 3-strike threshold; per-repo `retraction-log.md`; catches discipline drift over time.
- **Directive-queue protocol** (`memories/feedback_directive_protocol.md`) — async cross-repo coordination via `directives/pending/` → `processed/` + `replies/`. Canonical trigger word: `directive`.
- **Compaction-resume protocol** (`memories/feedback_compaction_resume_protocol.md`) — JSONL re-read on context loss to preserve fidelity.
- **Canon-validator alignment protocol** (`canon-validator-alignment-protocol.md`) — keeps §5 canon prose synchronized with actual validator implementations.
- **Three anti-default factors** (`memories/feedback_three_anti_default_factors.md`) — Factor A surface-feature smuggling, Factor B new-rule reflex, Factor C sample-size discipline.
- **Rule-proposal gates** (`memories/feedback_rule_proposal_gates.md`) — four pre-proposal gates before any new rule is drafted.

---

## What is still missing

**Automated v1→v2 first-pass editorial transformation.** Currently manual, anchored on Stan's intuition and the existing v1 (te'amim-anchored for Hebrew; alternative anchors for other corpora). For LXX / Vulgate / Quran to spin up rapidly, this leg needs to exist as automation.

The same cognitive-labor partitioning principle applies:

- **Mechanical leg**: Phase A candidate-break generation (versification + major punctuation + UD-sentence boundaries) — corpus-specific configurations
- **LLM leg**: Phase B applied generatively rather than diagnostically — Sonnet produces a v2 candidate from v1 input + bidirectional rubric + cognitive-unity check

The audit-layer prototype (Leg 4) operates DIAGNOSTICALLY on existing v2. The natural extension is GENERATIVE — same rubric, applied to produce v2 from v1 baseline. If this experiment validates, the v1→v2 leg is feasible.

**Statistical / distributional priors** (per-genre ATU-length distributions, outlier detection) — surfaced as candidate; may not be necessary if legs 1-4 catch enough.

**Discourse-cohesion signals** (coreference chains, topic continuity, predicate-argument repetition) — surfaced as candidate; likely unnecessary if leg 4 is strong enough.

---

## The methodological claim this architecture supports

Structural-segmentation criticism is more feasible at scale than purely-manual editorial work would allow, because cognitive labor is partitioned across mechanical / LLM / human layers each handling task types they are fit for. Pre-LLM, the same framework would have required months of human work per book; LLM-alone would hallucinate too freely; mechanical-alone misses failure modes the R/H validator catalog does not enumerate. The four-leg partitioning is a coverage-and-efficiency claim, not a paradigm shift.

**What this claim does NOT extend to:**

- The framework does not claim the four legs cover every editorial failure mode. Mature corpus work will continue to surface cases none of the four legs handle; these get added to the R/H validator stack or the audit-layer rubric over time per §7.3 discipline.
- The framework does not claim Leg 4 (audit-layer) is methodology-shifting. It is a coverage extension. The R/H stack catches certain failure modes; Leg 4 catches forward-closure / backward-containment failures the stack does not enumerate. These are complementary, not competing.
- The framework does not claim cross-corpus port is free. Each new corpus requires its own anchoring infrastructure, its own R/H rule porting, and its own audit-layer prompt calibration. The methodology gives a template; the per-corpus work is real.

**What this claim does extend to:**

- The discipline-floor (§7.3 + retraction-log + canon-validator alignment) is what makes the cognitive-labor partitioning trustworthy under fast iteration. Without it, mechanical / LLM legs would accumulate silent inconsistency.
- LXX / Vulgate spin-up benefits from the existing methodology + discipline-floor, but the spin-up timeline depends on the per-corpus anchoring + rule-porting work, not just on the methodology.

For the methodology paper: this is its own section, but it should be framed as cognitive-labor partitioning + discipline-floor enabling scalable structural-segmentation criticism, not as an LLM-driven breakthrough. The LLM legs are useful tools within the discipline-floor; they do not stand alone.

---

## Cross-references

- `framework.md` — universal framework structure (§0/§1/§2/§7)
- `architecture.md` — four-planes engineering separation (data / spec / tooling / delivery)
- `apparatus.md` — system-level claims about what the apparatus is for
- `change-protocol.md` — §7.3 audit triggers and the change-protocol governing rule modifications
- `rule-equivalence-map.md` — cross-corpus rule porting
- `rule-template.md` — operational template for §5 rule entries
- `retraction-log-protocol.md` — discipline-drift safeguard
- `canon-validator-alignment-protocol.md` — keeping canon prose synced with validator implementations
- `memories/feedback_directive_protocol.md` — cross-repo coordination
- `memories/feedback_three_anti_default_factors.md` — rule-proposal anti-pattern catalog
- `memories/feedback_compaction_resume_protocol.md` — context-loss recovery

---

## Empirical evidence base (2026-05-16 / 2026-05-17, retracted-and-corrected)

The earlier version of this section claimed cross-genre validation of an "extended bidirectional test" (necessary condition + cognitive-unity gate) on Deut 6, Gen 22, Ps 1, Gen 1, Isa 53, Ps 23. That framing has been retracted on the grounds noted in the rubric section above.

**What the audit work actually demonstrated** (after retracting the cognitive-unity gate):

- **Forward-closure / backward-containment failures are real and substantial** across the corpus. The Deut 6 and Gen 22 audits surfaced genuine bare-element extractions, speech-frame extractions, and appositive extractions that the R/H validator stack does not currently catalog. These are legitimate audit-layer catches.
- **Parallelism-based merges (Ps 1:1, Ps 1:6, Ps 23:2, Ps 23:4, Deut 6:11 stock-pair) were artifacts of the cognitive-unity gate.** On honest application of the bidirectional test alone, these are NOT over-breaking failures; each colon independently satisfies forward closure and backward containment. The validator's verdict on these (split, where applicable) aligns with the bidirectional test. The audit-layer should not have merged them.
- **Several already-committed corrections require partial revert.** The Deut 6 commit (`6933d793f`) and Ps 1 commit (`39f39d886`) contain a mix of legitimate audit catches and parallelism merges that need to be reverted. The Gen 22 + Ps 23 working-tree edits were blocked at pre-commit baseline-check (`validate_parallel_clause_split` regression +5) — that block was the discipline-floor working correctly.
- **R19 resolver calibration** (BoFM, 75-case sample, ~87% unanimous agreement) — stands. This work operates within validator-flagged scope (Leg 3) and does not interact with the cognitive-unity question.
- **§7.3 audit gate effectiveness** — confirmed three times in observed practice: BoFM-2203 (Option E parser-suspect collision with CATAPHORIC closed list); GNT-2400 (Pass D Rule 2 English-surface-heuristic anti-pattern); the Gen 22 + Ps 23 pre-commit block surfacing the cognitive-unity conflict. The discipline-floor caught design defects before code-lands in all three cases.
