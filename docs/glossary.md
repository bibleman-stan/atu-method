# Glossary — Universal Defined Terms

This document defines terms used universally across all atu-method reader editions. Project-specific terms (te'amim for Tanakh, periphrastic for GNT, EME swap-list for BoFM, etc.) are defined in each per-repo canon's glossary.

Reference convention: term names are bolded in source documents; first use in any document SHOULD link to this glossary.

---

## A

- **Anaphoric failure** — a line whose referents depend on prior context not present on the line (pronouns without antecedent, deictic demonstratives like "these things" / "that day," discourse-anaphoric particles like "therefore" / `לָכֵן` / causal `כִּי`); fails backward referential self-containment. See `framework.md §1.2`.
- **ATU** (atomic thought unit) — a span of text the reader can take in as a single complete unit of meaning without needing the next line to resolve it. One ATU per line in the rendered output. A line qualifies if it satisfies EITHER the **bidirectional test** (primary) OR the **explicit-marker license** (secondary). Note: the unit is the atomic *thought*, not the atomic predication — grammatical closure is a proxy for thought, completed by the marker license where the proxy under-captures. See `framework.md §2`.
- **Audit-then-apply discipline** — the workflow rule that distinguishes proposing a change (audit gate) from applying it (commit). See `change-protocol.md`.

## B

- **Bidirectional test** — the PRIMARY criterion for whether a line is an ATU: BOTH forward grammatical closure AND backward referential self-containment must hold. A line that fails it may still qualify under the **explicit-marker license** (secondary). See `framework.md §2.1`.

## C

- **Canon** — the project-specific operational specification of editorial rules; per-repo `private/01-method/colometry-canon.md`.
- **Cataphoric introduction** — forward-pointing reference (presentative `הִנֵּה` + indefinite NP, a **quotative** "thus says X:" / "and he said:" frame announcing distinct direct discourse) — does NOT fail the bidirectional test because the forward content is introduced, not depended on. **Narrow carve-out:** it covers a quotative *announcement* (the quote is its own ATU), NOT a performative **assertion-matrix** (a speech/assertion verb taking a `ccomp` proposition — "I say [that] X"), which binds its complement. Discriminator: direct-speech/parataxis → frame stands; `ccomp` → matrix binds. See `framework.md §2.1`.
- **Explicit-marker license** — the SECONDARY criterion: a **break-license**, not an ATU-from-fragment rule. A colon that is already closure-eligible under the bidirectional test (often via elision-restoration of a gapped finite verb from the prior parallel clause) but which the KEEP-AS-IS default holds merged may be broken onto its own line when it opens with an author-placed token from the closed **Marker Registry** (sub-clausal asseveratives like `yea`/`or rather`; parallel subordinator-stacks like "that … that … that"). Firewall-safe by the conjunction of (a) the colon independently satisfying the test and (b) a closed discrete-lexeme list — NOT by "the token is on the page" (te'amim are on the page too, and stay banned). Does NOT cover clause-level connectives (δέ/γάρ/"for"), which already pass the primary test. See `framework.md §2.2`.
- **Char-offset** — the column position within a rendered line where an applier inserts a break or merges to the previous line.
- **Coarse anchor** — the coarsest reliable signal used as the primary candidate-break source (typically versification). Finer signals (te'amim, punctuation, parse boundaries) are informational, not adjudicative. See `toolset-architecture.md`.
- **Cognitive identification first; constraints second** — *(RETIRED 2026-05-18)* the short-lived 2026-05-17 principle that ATU identification was a cognitive task done by the LLM (minimal rubric), with syntactic constraints auditing the result. Superseded by **mechanical-first**: binding rules are the primary segmenter; LLM adjudication is optional and narrow-task on residuals. See `framework.md` §3.
- **Binding-rule catalog** — per-language inventory of binding rules; each fires on a parse-derived feature condition to merge clause units into ATU candidate groups (v1.5). The validated Hebrew set is B1–B14; see `binding-rules-hebrew.md`. *(Replaces the retired "constraint catalog" / Stage-2 audit concept.)*

## E

- **EME English** — Early Modern English register (KJV / Skousen-edition BoFM); has its own binding-rule catalog distinct from modern English.
- **Editorial review** — v3 of the mechanical-first pipeline; the human adjudicates between the binding-rule output and any optional v2 LLM verdicts, and inspects flagged-uncertain cases, to produce the final rendering.

## F

- **Forward grammatical closure** — the line is grammatically complete on its own terms in the target language (pro-drop OK for languages that license it; verbless predication OK for Hebrew / Greek; EME English requires overt copula). One half of the bidirectional test.

## L

- **LLM adjudication (v2, optional)** — narrow-task per-group LLM calls on the residual cases the binding rules cannot decide (one yes/no question per group, 3 passes, agreement-scored). The LLM does NOT do chapter-level rendering. *(Supersedes the retired "LLM identification stage", which made the LLM the primary identifier.)*

## M

- **Marker Registry** — the closed, per-corpus, audited list of explicit author-placed boundary tokens that trigger the **explicit-marker license** (§2.2). A token enters only if (i) it is an explicit source lexeme, (ii) the clause it heads is propositionally complete minus the marker (or a shared element), and (iii) it is not already covered by the bidirectional test. Adding a marker is a §7.3 closed-list-extension audit trigger. See `framework.md §2.2`.
- **Minimal rubric** — *(RETIRED 2026-05-18)* the LLM-primary identification prompt from the 2026-05-17 design (bidirectional test + restrictive-relative binding + small constraint set + default KEEP-AS-IS). Retired with that architecture; the optional v2 adjudication uses narrow per-group yes/no prompts instead.

## P

- **Producer-style rule** — FORBIDDEN framing. A rule that GENERATES ATU rendering (e.g., "split parallel clauses," "merge synonymous cola"). Constraints AUDIT a proposed rendering; they do not generate it.
- **Pro-drop** — null-subject licensing in languages where finite-verb morphology supplies the subject (Hebrew, Greek, Latin). Hebrew finite verbs license forward closure without overt subject NP. EME English does NOT license pro-drop except in imperatives.

## R

- **Restrictive relative clause binding** — restrictive (defining) relative clauses bind to their head noun and cannot stand as separate ATUs. Universal across Hebrew `אֲשֶׁר`, Greek `ὅς` / `ὅστις` / `ὅπου`, EME English "which" / "who" / "that." See `framework.md §1.3`.

## S

- **Pipeline stages (v0 / v1 / v1.5 / v2 / v3)** — the mechanical-first pipeline: v0 source → v1 parse-derived clauses → v1.5 binding rules (primary segmenter) → optional v2 narrow-task LLM adjudication on residuals → v3 editorial review. See `framework.md` §3 and `toolset-architecture.md`. *(Supersedes the retired Stage 1/2/3 LLM-primary scheme.)*

## T

- **Mechanical-first pipeline** — the architecture of the apparatus: v0 source → v1 parse-derived clauses → v1.5 binding rules (the primary segmenter, producing a publishable draft) → optional v2 narrow-task LLM adjudication on residuals → v3 editorial review. *(Replaced the retired three-stage LLM-primary pipeline on 2026-05-18.)*
- **TxLog** — transaction log for corpus mutations supporting rollback.

## U

- **UD** — Universal Dependencies; the parsed-corpus annotation system feeding v1 parse extraction (EME English via CoNLL-U).

## V

- **v2-mine / v2-he / v2-greek** — per-repo rendered-corpus directories holding the current state of the colometric edition.
- **Violation report** — *(RETIRED 2026-05-18)* output of the retired Stage-2 constraint audit. In mechanical-first, the per-repo validator baseline-check plays the analogous audit-gate role: it flags deviations for editorial review and does NOT auto-correct.
