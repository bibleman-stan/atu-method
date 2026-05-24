# Methodology Position — LDHB, Discourse Grammar, and the Bidirectional Test

This document specifies the relationship between the ATU apparatus and adjacent published discourse-linguistic work (primarily the Lexham Discourse Hebrew Bible / Lexham Discourse Greek New Testament). It is a methodological-positioning document for the apparatus and for any methodology-paper claims it supports.

---

## The position

**LDHB and LDGNT are consulted as calibration references; the apparatus does not depend on them at runtime.**

- The pipeline reads BHSA / Macula / CoNLL-U parses and applies the binding rules of `binding-rules-hebrew.md`. It does NOT read LDHB tags.
- LDHB is used POST-HOC to verify that the apparatus's output is in the same discourse-linguistic neighborhood as published scholarship.
- Where the apparatus's output diverges from LDHB, the divergence is either:
  - **Methodological** — the apparatus chooses a different granularity than LDHB intentionally (e.g., absorbing speech-margin + vocative into one ATU where LDHB tags two SENTENCEs)
  - **Architectural** — a known gap (`framework.md` §6) that future v2 LLM adjudication or editorial review handles
  - **Calibration** — LDHB surfaces a case the apparatus had missed, and the apparatus is refined (e.g., B8 hineh-presentative + ZQt0 attribute was added after LDHB tagging revealed the pattern)

## Why this position

**Licensing.** LDHB is Lexham Press commercial. Logos resources are typically licensed for personal use; derivative works that propagate the tagged data require explicit permission. The apparatus stays cleanly within fair-use comparison ("compared against a reference") rather than redistribution ("uses LDHB tags at runtime").

**Coverage.** LDHB covers Hebrew Tanakh; LDGNT covers Greek NT. There is no Lexham Discourse work for LXX or Vulgate. An apparatus that depends on LDHB at runtime cannot extend uniformly to LXX / Vulgate. The mechanical-first architecture (BHSA / Macula / CoNLL-U parses) extends uniformly because parse layers exist for each corpus or can be built.

**Methodological integrity.** The apparatus's claim is that the bidirectional test plus a small catalog of grammar-derived binding rules produces ATU-aligned discourse segmentation from first principles. If LDHB were a runtime input, the apparatus would be presenting Lexham's analytical choices wrapped in a reader-apparatus shell, not making an independent methodological contribution.

**Resilience.** If LDHB is restricted or changed, the apparatus is unaffected. The pipeline reads parse data that is publicly licensed (BHSA: CC BY-NC 4.0; Macula: CC BY 4.0) or built from public sources.

## Field positioning and theoretical grounding

Three program-level framing decisions (made 2026-05-24; recorded canonically in the vault orientation docs at `vaults-nano/my_brain/10_Projects/Readers/00-ATU-research-program.md` §1/§3). They do not alter the runtime pipeline; they govern how the apparatus is described and cited in methodology-paper claims.

1. **Field name — delimitation criticism (DC), generalized.** The program situates *within* Korpel & Oesch's delimitation criticism rather than coining a rival critical method, taking "delimitation" in a generalized sense that extends the founders' manuscript-marker-bound definition **forward** (cognitive constraints on unit-packaging at composition, not only the markers scribes left), **prescriptively** (designing reader editions, not only describing ancient ones), and **cross-corpus** (incl. corpora with no manuscript-marker tradition — e.g. the Book of Mormon, where there are no setumot/petuchot to read). Korpel & Oesch's manuscript work is the descriptive/scribal core; this apparatus is part of the forward/prescriptive generalization. Retires the prior internal label *structural segmentation criticism / presentation criticism*.

2. **Unit — conceptual unit, operationalized as the ATU.** The ATU is this apparatus's *operationalization* — via the bidirectional atomic-thought test — of the **conceptual unit** already described in the discourse-linguistic literature, not a newly posited theoretical entity. Maps to neighbors: ≈ Chafe's idea unit minus its prosodic anchoring; ⊃ but ≠ RST's clause-bound *elementary discourse unit*; ≈ Hannay & Kroon's *basic conceptual unit* (verify). Consistent with the granularity table below: the conceptual/ATU grain is coarser than LDHB's analytical splits.

3. **Cognitive grounding — Langacker + Givón primary; Chafe a foil.** The "atomic thought" claim grounds primarily in conceptualization-based cognitive linguistics (Langacker: units as conventional packagings of meaning; Givón: information flow, topic continuity), not in Chafe's prosody-anchored idea units. Rationale: the corpora are mediated *written conceptual artifacts*, not speech transcripts, so prosodic chunking under-fits; Chafe is retained as the closest prosodic-cousin foil. Again, runtime is unaffected — the pipeline reads parses and applies binding rules regardless of which cognitive literature grounds the unit.

## Where LDHB is used

- **Validation comparisons** in the pilot (`v3_three_way_compare.py`): pipeline / cold-eye / LDHB three-way.
- **Calibration during rule development**: when a chapter's pipeline output diverged from LDHB, the divergence was investigated and either (a) a new binding rule was added that traces to the bidirectional test, or (b) the divergence was documented as a known methodological choice.
- **Methodology-paper citations**: the apparatus may cite van der Merwe / Bailey / Westbury as influences and as calibration witnesses, without depending on LDHB at runtime.

## Where LDHB is NOT used

- **Runtime pipeline input**: no LDHB markup is read by `v1_extract_clauses.py`, `v1_5_apply_bindings.py`, `v2_llm_atu_judgments.py`, or downstream rendering.
- **Distributed apparatus output**: the apparatus's `data/text-files/v2/` output is ATU-segmented text, not LDHB tags.

## Granularity relationship

Across the four validated chapters, the pattern is:

| Source | Granularity tendency |
|---|---|
| LDHB | Most granular — analytical splits at every grammatical sub-unit (each parallel colon, each subordinate clause, each free-standing relative) |
| Pipeline (BHSA-derived) | Mid-granularity — inherits BHSA clause-atom boundaries, modified by binding rules |
| ATU (editorial cold-eye) | Coarsest — binds for reader-flow, absorbs both LDHB SUB-POINTs and BHSA clause-atom splits |

The pipeline lives in the middle and is designed to. It produces a draft that an editor refines toward the ATU goal by absorbing the cases where the pipeline matches LDHB but cold-eye binds more tightly.

## Future direction

If at some future point the apparatus is to be distributed AS a Lexham-derivative product (e.g., a reader app that surfaces LDHB tags as a study layer), explicit Lexham permission must be sought. The mechanical-first architecture does not preclude that future — it just doesn't depend on it now.

---

## Citations

- Christo van der Merwe (ed.), *Lexham Hebrew-English Interlinear Bible* (Bellingham, WA: Lexham Press, 2004) — discourse-tagged Hebrew Bible.
- Steven E. Runge, *Discourse Grammar of the Greek New Testament* (Bellingham, WA: Lexham Press, 2010).
- van der Merwe, Naudé & Kroeze, *A Biblical Hebrew Reference Grammar* (2nd ed., Bloomsbury 2017) — discourse-linguistic Hebrew reference; same author school as LDHB.
- Niccacci, *The Syntax of the Verb in Classical Hebrew Prose* — textlinguistic theory of Hebrew verbs; cited as influence on the wayhi macrosyntactic-frame rule (B5).
- Korpel, Marjo C.A., and Josef M. Oesch, eds., *Delimitation Criticism: A New Tool in Biblical Scholarship* (Pericope series; Assen: Van Gorcum / Leiden: Brill, 2000–) — the founding field this program generalizes (forward/prescriptive/cross-corpus).
- Langacker, Ronald W., *Foundations of Cognitive Grammar* (Stanford UP, 1987/1991) and "Discourse in Cognitive Grammar," *Cognitive Linguistics* 12 (2001) — primary grounding for the conceptual unit (conceptualization).
- Givón, T., *Topic Continuity in Discourse* (Benjamins, 1983) — co-anchor (information flow, topic continuity).

These references are consulted as scholarship, not embedded in the pipeline.
