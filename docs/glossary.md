# Glossary — Universal Defined Terms

This document defines terms used universally across all atu-method reader editions. Project-specific terms (te'amim for Tanakh, periphrastic for GNT, EME swap-list for BoFM, etc.) are defined in each per-repo canon's glossary.

Reference convention: term names are bolded in source documents; first use in any document SHOULD link to this glossary.

---

## A

- **Anaphoric failure** — a line whose referents depend on prior context not present on the line (pronouns without antecedent, deictic demonstratives like "these things" / "that day," discourse-anaphoric particles like "therefore" / `לָכֵן` / causal `כִּי`); fails backward referential self-containment. See `framework.md §1.2`.
- **ATU** (atomic thought unit) — a span of text the reader can take in as a single complete unit of meaning without needing the next line to resolve it. One ATU per line in the rendered output.
- **Audit-then-apply discipline** — the workflow rule that distinguishes proposing a change (audit gate) from applying it (commit). See `change-protocol.md`.

## B

- **Bidirectional test** — the criterion for whether a line is an ATU: BOTH forward grammatical closure AND backward referential self-containment must hold. See `framework.md §1.2`.

## C

- **Canon** — the project-specific operational specification of editorial rules; per-repo `private/01-method/colometry-canon.md`.
- **Cataphoric introduction** — forward-pointing reference (presentative `הִνֵּה` + indefinite NP, "thus says X:" announcing speech, etc.) — does NOT fail the bidirectional test because the forward content is being introduced, not depended on.
- **Char-offset** — the column position within a rendered line where an applier inserts a break or merges to the previous line.
- **Coarse anchor** — the coarsest reliable signal used as the primary candidate-break source (typically versification). Finer signals (te'amim, punctuation, parse boundaries) are informational, not adjudicative. See `toolset-architecture.md`.
- **Cognitive identification first; constraints second** — the architectural principle that ATU identification is a cognitive task done by the LLM with the minimal rubric, and syntactic constraints audit the result. Producer-style validators (rules that GENERATE ATU rendering) are forbidden.
- **Constraint catalog** — per-language inventory of syntactic constraints expressed as yes/no grammatical questions; runs in Stage 2 of the three-stage pipeline.

## E

- **EME English** — Early Modern English register (KJV / Skousen-edition BoFM); has its own constraint catalog distinct from modern English.
- **Editorial review** — Stage 3 of the three-stage pipeline; human adjudicates conflicts between LLM proposal and constraint audit flags.

## F

- **Forward grammatical closure** — the line is grammatically complete on its own terms in the target language (pro-drop OK for languages that license it; verbless predication OK for Hebrew / Greek; EME English requires overt copula). One half of the bidirectional test.

## L

- **LLM identification stage** — Stage 1 of the three-stage pipeline; the LLM applies the minimal rubric to source text and proposes ATU-segmented rendering.

## M

- **Minimal rubric** — the prompt the LLM identification stage uses: bidirectional test + restrictive-relative binding + small set of language-specific syntactic constraints + default KEEP-AS-IS. Excludes cognitive-unity gates, parallelism class adjudication, and genre anchors as primary licenses.

## P

- **Producer-style rule** — FORBIDDEN framing. A rule that GENERATES ATU rendering (e.g., "split parallel clauses," "merge synonymous cola"). Constraints AUDIT a proposed rendering; they do not generate it.
- **Pro-drop** — null-subject licensing in languages where finite-verb morphology supplies the subject (Hebrew, Greek, Latin). Hebrew finite verbs license forward closure without overt subject NP. EME English does NOT license pro-drop except in imperatives.

## R

- **Restrictive relative clause binding** — restrictive (defining) relative clauses bind to their head noun and cannot stand as separate ATUs. Universal across Hebrew `אֲשֶׁר`, Greek `ὅς` / `ὅστις` / `ὅπου`, EME English "which" / "who" / "that." See `framework.md §1.3`.

## S

- **Stage 1 / Stage 2 / Stage 3** — the three-stage pipeline: LLM identification → constraint catalog audit → editorial review. See `toolset-architecture.md`.

## T

- **Three-stage pipeline** — the architecture of the apparatus: LLM identification (minimal rubric) → constraint catalog audit (syntactic yes/no questions) → editorial review (human adjudication).
- **TxLog** — transaction log for corpus mutations supporting rollback.

## U

- **UD** — Universal Dependencies; the parsed-corpus annotation system feeding the constraint catalog audit stage.

## V

- **v2-mine / v2-he / v2-greek** — per-repo rendered-corpus directories holding the current state of the colometric edition.
- **Violation report** — output of Stage 2 (constraint catalog audit); per-break list of constraint violations flagged for editorial review. Does NOT auto-correct.
