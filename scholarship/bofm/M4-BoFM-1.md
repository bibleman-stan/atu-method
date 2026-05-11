# M4-BoFM-1: Subject-Orphan Predicate Completion — Scholarship Companion

**Operational entry:** see `readers-bofm/private/01-method/colometry-canon.md §5 M4-BoFM-1`.

**Codification date:** 2026-05-11. Commits: `fb82c55` (initial R18a sub-clause) → `e20a4b9` (parallel-consistency extension) → `45ff06b` (promotion to standalone rule; 25 Cat A corpus merges).

**Status:** This is the scholarship companion documenting WHY M4-BoFM-1 exists, HOW we know it is correctly framed, and what intellectual and empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

M4-BoFM-1 (Subject-Orphan Predicate Completion) requires that a v2-mine line whose content is a subject NP of one of the closed-list-eligible shapes be merged with the bare finite predicate on the immediately-following line. A subject NP terminating at a line boundary — with its matrix predicate exiled to the next line — fails the atomic-thought test: the subject-line is not a proposition (no predication), the predicate-line is not a proposition (no anchor), and the merged subject+predicate is one proposition (one image, one cognitive frame). Merge is therefore mandatory.

The rule is the **predicate-side dual of R17** (Complement Integrity). R17 protects the predicate→complement bond; M4-BoFM-1 protects the subject→predicate bond. Together they close the subject–predicate–complement triad that constitutes a complete syntactic clause.

## Rationale

### The architectural gap

Before 2026-05-11, the operational canon contained rules that were predominantly **prohibitive** (Layer 1 vetoes: don't break here) and **protective** (formula integrity: keep these spans whole). The corpus had been edited primarily by applying these subtractive constraints. What it lacked was a corresponding affirmative rule codifying the positive direction of the merge-override principle: *when splitting a span produces fragments that individually fail the atomic-thought test, merge*.

Framework §1.5 M4 (Fragmented atomic thought-unit) stated this principle at the universal level. Per-corpus instantiation of M4 as a mechanical rule with a validator had not been done for the BoFM. The principle was enforced editorially — by Stan's eye catching orphaned predicates on review — but not by the apparatus's mechanical pipeline. This created a gap between the framework's stated merge-override and its operational teeth.

The gap was not random. Subject NPs often span multiple tokens — a relative clause, an appositive title, a participial modifier — and when editors apply line-break discipline, the natural impulse is to treat a long NP as a complete line (the NP is long; it feels like a unit). The predicate then falls to the next line. The NP *is* a unit, but it is not an atomic *thought*: no predication, no image, no bounded frame. The rule closes this specific failure mode.

### The predicate→complement dual

R17's protective logic is symmetrical: a matrix verb that governs an obligatory clausal complement must keep that complement on the same line, because the matrix without its complement is incomplete. The logic applies one layer out: a subject NP that governs (in the sense of requiring) a matrix predicate must keep that predicate on the same line, because the subject without its predicate is equally incomplete.

The parallelism is exact:

| Relation | Fragment A alone | Fragment B alone | Merged |
|---|---|---|---|
| Subject → Predicate (M4-BoFM-1) | Subject NP (no predication) | Bare predicate (no subject) | One proposition |
| Predicate → Complement (R17) | Matrix verb (no complement) | Complement clause (no matrix) | One proposition |

In both cases, splitting a bond that the atomic-thought test requires to remain whole produces two non-atomic fragments. In both cases, the apparatus's answer is the same: the bond is the ATU.

## Grammatical grounding

Subject-verb agreement is the foundational clause-construction relation in English syntax: the subject NP selects the verb's person/number features; the finite verb anchors the proposition. CGEL Chapter 2 §1 establishes the clause as the canonical unit of propositional predication: a clause consists minimally of a subject NP and a predicate VP. Neither constituent, taken alone, constitutes a complete proposition in the clause sense.

The BoFM-archaic register extends this structure with complex subject NPs that include relative clauses, appositives, and participial modifiers. These long NPs do not change the propositional completeness argument; they complicate the surface signal. The closed-list subject shapes in M4-BoFM-1's `SUBJECT_SHAPES_M4_BOFM1` inventory are the corpus-attested shapes that create the orphan-predicate failure mode in the BoFM:

- **A1 — Patriarch-deity-triad as subject** (R18a formula in subject position)
- **A2 — AICTP head NP + comma + orphan predicate** ("And it came to pass that [NP],")
- **B1 — NP-with-relative-clause** ("that same God who delivered them out of the hands of the Egyptians")
- **B2 — NP-with-appositive** ("the Lord God, the Holy One of Israel,")
- **B3 — NP-with-participial modifier** ("Laman and Lemuel, being the eldest,")
- **B5 — Self-identifying pronoun + RC/appositive** ("I, Pahoran, who am the chief governor...")

Each shape produces a line-terminal comma or semicolon that marks the subject's right boundary — the same punctuation signal that in other constructions marks a complete clause or a coordinated member. The surface ambiguity is why mechanical detection requires a Stage 2 UD filter to confirm `nsubj` relation to a matrix verb on the following line, rather than relying solely on surface pattern.

## Empirical evidence

### Discovery sequence

**Alma 29:11 (2026-05-11).** Stan flagged `did deliver them out of bondage.` as a hanging fragment. The immediately-preceding line was `yea, the Lord God, the God of Abraham, the God of Isaac, and the God of Jacob,` — the patriarch-deity-triad in subject position, also governed by R18a. The predicate-line was orphaned. The fix was clear: merge.

**R18a sub-clause (commit `fb82c55`).** The initial response was to codify a sub-clause within R18a handling the specific case where the triad appears as the grammatical subject of a finite predicate on the following line. Scope at that point: "when the R18a-protected triad is the subject of a predicate orphaned on the next line." Three corpus instances fell into this scope.

**Alma 29:12 (same session).** Stan immediately caught `did deliver them out of bondage.` at 29:12, where the subject was not the triad but `that same God who delivered them out of the hands of the Egyptians` — an extended NP with a relative clause. This was the same orphan-predicate pattern but with a B1-shape subject rather than an A1-shape subject. The R18a sub-clause had been set too narrowly: it captured the surface signal (the triad) without fully capturing the underlying principle (any subject NP + bare predicate = one ATU).

**Parallel-consistency merge (commit `e20a4b9`).** The 29:12 case was applied under the same principle, producing the first non-triad merge under what would become M4-BoFM-1.

### Broader audit (task `aec7492d96ab06a3c`)

An Opus-level hostile audit was dispatched with widened scope: *"what is the full corpus distribution of the subject-orphan predicate pattern across all subject shapes?"* Findings:

- Approximately 27 corpus instances across 11 books (1 Nephi, 2 Nephi, Jacob, Mosiah, Alma, Helaman, 3 Nephi, Mormon, Ether, Moroni, plus the Words of Mormon).
- Subject shapes break into A-class (formula-anchored: A1 triad, A2 AICTP-head-NP) and B-class (extended NP with structural modifier: B1–B5).
- The five SCOPE-exclusion categories correctly discriminated non-firing cases: R15 vocatives (O Lord, alone), J1 coordinate-subject-series tails, J3 speech-act parentheticals (saith the Lord), J5 save-clauses, R21 participial-lead lines (being X, having Y). Zero false-negative exclusions found in audit review.
- The length backstop (>130 characters → REVIEW) correctly routed 2 cases to editorial judgment rather than mechanical auto-apply.

### Post-codification corpus state

Commit `45ff06b` applied 25 Category A corpus merges (Cat B/REVIEW cases excluded). Post-codification, the corpus is uniformly compliant against the closed-list-eligible subject shapes. The validator `validators/colometry/validate_m4_bofm_1_subject_orphan.py` reports zero violations in Stage 1 surface-pattern mode.

### Corpus distribution (by book)

The 27 pre-codification violations distributed across 11 books with notable clustering in Alma (the longest book) and in narrative-discourse sections where extended-NP subjects with appositives and relative clauses are most frequent. The BoFM register's characteristic formulaic subjects — "I, Nephi/Alma/Mormon, who am/was..." in colophon-adjacent self-identification passages; "the Lord God, the Holy One of Israel" in prophetic citation chains; AICTP-headed narrative transitions — are the primary generation sites.

## Intellectual lineage

### Framework M4 as the universal anchor

Framework §1.5 M4 (Fragmented atomic thought-unit) states: if splitting would produce fragments that individually fail the atomic-thought test, merge. M4-BoFM-1 is the corpus-specific instantiation of this universal principle for the BoFM's attested subject-shape inventory. The framework principle is abstract; the per-corpus rule is what gives it mechanical teeth.

### R17 as the predicate→complement dual

R17 (Complement Integrity) was codified in 2026-03-12. Its logic: a matrix verb and its obligatory clausal complement form one cognitive frame and must be presented as one visual unit. M4-BoFM-1 instantiates the structurally symmetric logic one level up: a subject NP and its matrix predicate form one cognitive frame (the proposition) and must be presented as one visual unit. The apparatus now has both halves of the clause-integrity principle:

- **Subjectward (M4-BoFM-1):** subject + predicate = one ATU
- **Complementward (R17):** predicate + complement = one ATU

### Cross-tradition support

The subject→predicate bond as a minimum clause unit is not an apparatus innovation; it is the foundational claim of Western syntactic theory. Its support in editing traditions is correspondingly broad:

- **TEI Guidelines P5 §16** on linguistic corpus annotation: the clause (*s* element) is the annotatable minimum unit encompassing subject and predicate; sub-clause annotation of subjects or predicates in isolation is non-standard. TEI's annotation discipline implies the same integrity the ATU apparatus enforces at the display level.
- **MISRA-style mandatory-merge directives** in code-readability standards offer an analog from a different domain: certain syntactic constructions must not be split across lines because their unity is load-bearing for comprehension. Subject+finite-verb is the natural-language equivalent.
- **Classical-edition per-cola layouts:** Codex Vaticanus and Codex Sinaiticus per-cola arrangements of NT Greek consistently place subjects and their immediate predicates on a single cola. The scribal discipline that produced the great codices treated subject-verb as one visual unit as a matter of editorial convention — antedating modern syntax theory by seventeen centuries.
- **Parry-Lord oral-formulaic theory** (the analytic layer this apparatus explicitly does not target as primary): even within the OFT's emphasis on formula and theme, the minimum oral-compositional unit is the colon — and in Greek epic, a colon almost invariably encompasses at least a subject and its predicate together. The apparatus does not derive its rules from OFT, but the convergence is evidence that the subject+predicate unit is a natural reading-chunking boundary across traditions.

## Adversarial history

### The narrow-then-broad arc: a methodological case study

The codification of M4-BoFM-1 proceeded in two audit passes separated by a same-session observation. The arc is worth documenting precisely because it illustrates a discipline lesson about audit scope.

**First audit: correct-but-narrow (commit `fb82c55`).** The initial hostile audit was scoped to: *"does the corpus support a rule for the triad-as-subject + orphan-predicate case?"* The audit was set by the surface signal that triggered the conversation (the patriarch-deity-triad at Alma 29:11). Three corpus instances were found. The audit returned a correct verdict — the triad-as-subject orphan-predicate pattern is real and warrants codification — but the scope was set by the surface feature that prompted the inquiry, not by the underlying principle. The codified sub-clause was a bottom-up patch.

**Stan's catch at 29:12: principle over surface.** Stan immediately observed that Alma 29:12's `did deliver them out of bondage.` exhibited the same failure mode, but with a B1-shape subject rather than the A1 triad. The first audit, scoped to "fixed-formula subject," had treated the triad's formula-status as definitional rather than incidental. Stan's observation made the diagnostic explicit: the operative principle is not "triad is fixed formula" but "subject NP + bare predicate are one ATU." The formula-status of the triad is a separate property (governed by R18a) that happened to be present in the triggering instance; it is not the property that grounds the merge.

**Second audit: broader scope, principle-first (task `aec7492d96ab06a3c`).** The Opus-level audit dispatched for the broader question confirmed: the subject-orphan-predicate pattern recurs across approximately 27 corpus instances spanning six subject shapes and 11 books. This is not a formula-specific edge case; it is a systematic fragmenting pattern arising wherever the editor treats a long subject NP as a complete line. The audit's widened scope produced the closed-list `SUBJECT_SHAPES_M4_BOFM1` and the five exclusion categories, and its findings supported promotion from R18a sub-clause to standalone rule.

**Discipline lesson.** A hostile audit that returns a correct verdict may still have its scope set by the surface signal that prompted the inquiry rather than by the underlying principle. The correct-but-narrow result produces a patch codification; a second pass with principle-first scoping produces the structural rule. The gap between "R18a sub-clause governing triad-as-subject" and "M4-BoFM-1 governing any subject-orphan-predicate" is not a gap in verdict quality — both audits reached correct verdicts — but in scope orientation. The lesson is not "audits were wrong" but "scope of inquiry matters: set it by principle, not by the surface feature that happened to present first."

This arc is a canonical example of how canon construction should respond to scope-blindspot discovery: (1) apply the narrow codification when the narrow scope is what evidence supports, (2) immediately run a broader second pass when adjacent evidence suggests the underlying principle is wider than the surface signal, (3) promote the narrower codification to a principled rule when the broader pass confirms the principle. The R18a sub-clause was not a mistake; it was the honest codification of what the first audit could verify. M4-BoFM-1 is the honest codification of what the second audit could verify.

## Future work

### UD Stage 2 filter for the validator

The current validator (`validate_m4_bofm_1_subject_orphan.py`) operates in surface-pattern mode: it looks for the terminal-comma/semicolon + predicate-lead signals with named exclusions. Stage 2 refinement would add UD-parse confirmation: verify that the line-A terminal token bears `nsubj` dependency to the finite root on line B. This would reduce false positives in edge cases where surface pattern fires but UD structure does not confirm the subject→predicate bond. Stage 2 is deferred until UD-parse coverage of the corpus's extended-NP subject shapes is empirically stable.

### Cross-corpus sweep: M4-GNT-1 and M4-TNK-1

The principle (subject NP + its predicate = one ATU) is universal. The per-corpus closed-list of eligible subject shapes is BoFM-specific. Both sibling corpora are candidates for analogous instantiation:

- **M4-GNT-1 (Greek NT):** Greek's synthetic morphology marks subject-verb agreement on the verb itself (no independent subject NP required); when an explicit subject NP is present, the same subject-orphan-predicate failure mode can arise. The Greek register's characteristic long nominal chains (genitive stacks, participial absolute constructions) are the likely generation sites. Cross-check against readers-gnt canonical source files.
- **M4-TNK-1 (Hebrew Bible):** Biblical Hebrew's verb-subject ordering (VS and SV both attested) and pro-drop morphology mean the failure mode looks different — explicit subject NPs are already marked-constructions, often topicalized or contrastive; the orphan-predicate pattern likely arises in chiastic and parallel-line environments. Cross-check against readers-tanakh canonical source files.

Both sister canons should run corpus-sweep equivalents of the BoFM `SUBJECT_SHAPES_M4_BOFM1` inventory against their own attested subject shapes before codifying.

### Closed-list augmentation protocol

The `PREDICATE_LEAD_LEMMAS` list in the UD signature is explicitly marked "augmented as new instances are observed." As the validator runs against the full corpus over time, new predicate-lead forms may surface. Augmentation is a Category A maintenance task — adding an observed lemma to the list when a corpus instance confirms it is a clean bare-predicate lead requires no per-item editorial judgment.

---

*References:*

- Operational canon entry: `readers-bofm/private/01-method/colometry-canon.md §5 M4-BoFM-1` (codified 2026-05-11, commits `fb82c55` → `e20a4b9` → `45ff06b`)
- Universal framework: [`../../docs/framework.md`](../../docs/framework.md) §1.5 M4 (fragmented atomic thought-unit)
- Sister rule (predicate→complement): [`R17.md`](R17.md)
- Sister rule (triad-formula integrity, post-promotion scope): [`R18a.md`](R18a.md)
- Validator: `readers-bofm/validators/colometry/validate_m4_bofm_1_subject_orphan.py`
- Audit trail: `readers-bofm/private/audit-trail/M4-BoFM-1.md` (audit task id: `aec7492d96ab06a3c`)
