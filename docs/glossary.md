# Glossary — Universal Defined Terms

**This document defines terms used universally across all atu-method reader editions.** Project-specific terms (AICTP for BoFM, te'amim for Tanakh, periphrastic for GNT, etc.) are defined in each per-repo canon's glossary.

Reference convention: term names are bolded in source documents; first use in any document SHOULD link to this glossary.

---

**Status: SCAFFOLD** — to be populated by extraction from the per-repo canons (§0/§1 of each, plus retired §9/§10 glossaries). Initial list of terms requiring definition:

## A

- **ATU** (atomic thought unit) — a span of text the reader can take in as a single complete unit of meaning without needing the next line to resolve it.
- **AICTP** — "And it came to pass" / "And it came to pass that". (BoFM-specific; not universal.)

## C

- **Camera angle** — diagnostic for ambiguous proposition-boundary cases; whether the mind's eye repositions between candidate frames.
- **Canon** — the project-specific operational specification of editorial rules; per-repo `private/01-method/colometry-canon.md`.
- **Category A / B / C** — application-confidence tiers (mechanical / editorial-judgment / theological).
- **Char-offset** — the column position within a v2-mine line where an applier inserts a break or merges to the previous line; emitted by detectors per the T1.1 char-offset pattern.

## D

- **Decision procedure** — the §1.7 step-by-step procedure for resolving any candidate boundary against the framework.
- **Detector** — a validator implementing a specific rule's UD signature; emits STRONG-* and REVIEW-REQUIRED verdicts.

## G

- **Generative principle** — each proposition splits by default; the §1.1 starting position of the decision procedure.

## H

- **Helaman 3:16 cliff** — the N=3+ precedent establishing that Justification 1 wins over merge-overrides for coordinate predications at three or more members.

## J

- **J1 — Formally-marked parallel series** — members joined by formal markers (and also, nor, polysyndetic and) where shared predicate is recoverable.
- **J2 — Portrait accumulation** — attributes building one mental picture under a shared copular/attributive frame.
- **J3 — Speech-act announcement** — complete communicative predication introducing direct discourse.
- **J4 — Classical commata** — short fragmentary utterances carrying full communicative weight.
- **J5 — Substantive adjunct as own focus** — a fronted or trailing adjunct that is grammatically peripheral but carries substantial content.

## L

- **Layer 1** — generic-grammar break-legality table; what any competent editor of a text in this language would observe.
- **Layer 3** — project-specific editorial rule detail; the per-corpus operational canon.

## M

- **M1 — Gorgianic bonded pair** — N=2 coordinate members forming a single unified hendiadys (synonymy / cognate / intensification).
- **M2 — Verb-object clause-nucleus bond** — R17 alias; complement integrity.
- **M3 — Bare-governor indivisibility** — a head word that cannot stand on its own line without a complement.
- **M4 — Fragmented atomic thought-unit** — a split that would produce fragments individually failing the atomic-thought test.

## N

- **N=2 Adjudication Principle** — for two-member coordinate constructions, the M1 verb-synonymy paraphrase test resolves merge-vs-split. See §1.5.
- **N=3+ cliff** — at three or more coordinate members, Justification 1 wins unconditionally.

## P

- **Proposition** — the prototypical ATU; a complete predication (subject + finite verb + complement).

## R

- **REVIEW-REQUIRED** — detector verdict for cases needing human editorial judgment; not auto-applied.

## S

- **STRONG-MERGE-CANDIDATE / STRONG-SPLIT-CANDIDATE** — detector verdicts for cases mechanically resolvable; auto-apply per Category A discipline.
- **Subtractive force** — syntax as a veto over splits the generative principle would produce; the §1.2 second force.

## T

- **T1.1 char-offset pattern** — the detector pattern where validators emit char-offset split positions directly (via `build_line_map_full`) so appliers can mutate without regex position-finding.
- **TxLog** — transaction log for corpus mutations supporting rollback.

## U

- **UD signature** — the Universal Dependencies query pattern that triggers a rule's detector; encoded in YAML in each rule's §5 entry.

## V

- **v2-mine / v2-he / v2-greek** — per-repo edited corpus directories holding the current state of the colometric edition.

---

**This scaffold will be expanded as content is extracted from per-repo canons.**
