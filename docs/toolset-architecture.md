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

Holistic "is the rendering over-broken?" check. Operates over rendered v2 output (not UD parse input like Leg 3). Catches over-breaking that point-rules structurally cannot see — failures where every individual break is independently legal but the rendering as a whole over-segments.

- Reads the rendered ATU lines for a passage
- Applies the extended bidirectional test (forward grammatical closure + backward referential self-containment + cognitive-unity for parallelism)
- Returns per-line verdicts (keep / merge-with-prior / merge-with-next / ambiguous) + proposed corrected rendering + observed patterns

Status: demonstrated 2026-05-16 via Deut 6:1-12 (deuteronomic prose) and Gen 22:1-12 (narrative). The tool correctly identifies well-segmented verses (does NOT default to "merge everything") and surfaces genre-specific over-breaking patterns:

- Prose (deuteronomic): coordinate-series fragmentation (bare members, tricolons, infinitival series)
- Narrative: speech-verb extraction (bare וַיֹּאמֶר on its own line failing forward closure)

Both genres yielded ~60-75% over-breaking under the test. The unifying principle: **every individual break is legal under point-rule validators, but the cumulative effect fails the bidirectional test at the line level**. Point-rules answer "is this break placed correctly?"; the passage-level audit answers "is this break necessary?"

---

## The unifying rubric: extended bidirectional test

**Necessary condition (applies universally):** a line is a legitimate standalone ATU only if it satisfies BOTH:

1. **Forward grammatical closure** — the line is grammatically complete: subject + verb + obligatory complements present such that the line can stand syntactically on its own.
2. **Backward referential self-containment** — the line's referents are either already-established in prior discourse or self-introducing within the line.

A break between two adjacent lines is licensed only if BOTH lines independently satisfy these two conditions.

**Sufficiency extension for parallel poetry:** the necessary condition above is NOT sufficient for poetry. Adjacent parallel cola may each independently satisfy forward closure + backward containment, yet jointly express a single propositional content via paraphrase, antithesis, or emphatic doubling.

**Three parallelism classes handled differently:**

- **Synonymous parallelism** (saying the same thing twice — Ps 117:1 *"Praise the LORD, all you nations / extol him, all you peoples"*) → ONE ATU. The cognitive unit is the imperative repeated for rhetorical emphasis, not each colon.
- **Antithetic parallelism** (*"the righteous flourish / but the wicked perish"*) → ONE ATU. The comparison IS the thought.
- **Synthetic parallelism** (B advances A — *"blessed is the man who walks not... / nor stands... / nor sits..."*) → judgment call. If B is propositionally distinct, two ATUs; if B is rhetorical extension, one ATU.

**Critical claim:** surface signals — coordination (וְ / καί / et), parallelism marks, te'amim hierarchical disjunctives, editorial commas — DO NOT automatically license breaks. They generate CANDIDATES (Phase A below). The bidirectional test + cognitive-unity gate adjudicate which candidates become actual breaks (Phase B).

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

Structural-segmentation criticism is feasible at scale **precisely because cognitive labor is partitioned correctly between mechanical / LLM / human layers**. Pre-LLM, the same framework would have required months of human work per book; LLM-alone would hallucinate too freely; mechanical-alone would miss too much. The methodological contribution isn't only the ATU theory — it's the ATU theory + the discipline-floor + the cognitive-labor partitioning that makes it executable across corpora.

For the methodology paper this is its own section. For LXX / Vulgate spin-up this is what justifies the claim that they can reach "an equally mature state quickly." For the Container-Not-Originator paper this is direct evidence — the human and tools are doing different cognitive work, not just one substituting for the other.

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

## Empirical evidence base (2026-05-16)

- **Deut 6:1-12 audit** — 9 of 12 verses over-broken under bidirectional test; 9-verse re-rendering committed to `readers-tanakh` (`6933d793f`)
- **Gen 22:1-12 cross-genre validation** — 7 of 12 verses over-broken; different failure pattern (speech-verb extraction) from Deut 6 (coordinate-series fragmentation); same unifying rubric catches both
- **R19 resolver calibration** — 75-case sample, ~87% unanimous agreement, ~73% auto-applicable at unanimous-all-high gate (`readers-bofm/directives/replies/2026-05-16-2101-...`)
- **§7.3 audit gate effectiveness** — caught BoFM-2203 (Option E parser-suspect collision with CATAPHORIC closed list) and GNT-2400 (Pass D Rule 2 English-surface-heuristic anti-pattern) before code-lands
