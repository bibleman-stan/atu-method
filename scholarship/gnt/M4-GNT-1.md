# M4-GNT-1: Subject-Orphan Predicate Completion (Greek Instantiation) — Scholarship Companion

**Operational entry:** see `readers-gnt/private/01-method/colometry-canon.md §3.18 M4-GNT-1`.

**Codification date:** 2026-05-11. Commits: `001604d` (initial GNT canon §3.18 entry + 11 Cat A corpus merges; audit task `a0d7d74092a145179`).

**Status:** This is the scholarship companion documenting WHY M4-GNT-1 exists, HOW we know it is correctly framed, and what intellectual and empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

M4-GNT-1 (Subject-Orphan Predicate Completion, Greek Instantiation) requires that a v4-editorial line whose content is a subject NP of one of the closed-list-eligible shapes be merged with the bare finite predicate on the immediately-following line. A subject NP terminating at a line boundary — with its matrix predicate exiled to the next line — fails the atomic-thought test: the subject-line is not a proposition (no predication), the predicate-line is not a proposition (no anchor), and the merged subject+predicate is one proposition (one image, one cognitive frame). Merge is therefore mandatory.

The rule is the **predicate-side dual of R10** (Complement Integrity) in the GNT canon. R10 protects the predicate→complement bond (ὅτι-clauses and their equivalents); M4-GNT-1 protects the subject→predicate bond. Together they close the subject–predicate–complement triad that constitutes a complete syntactic clause. The rule is the Greek-corpus instantiation of the same principle that drives M4-BoFM-1 in the BoFM apparatus, adapted for Koine Greek's distinct morphosyntax: synthetic verb agreement, pro-drop, and the household-code parenesis genre that generates the rule's densest cluster.

## Rationale

### The architectural gap

Before 2026-05-11, the GNT operational canon contained rules that were predominantly **prohibitive** (Layer 1 vetoes) and **protective** (formula integrity; complement integrity R10; participial discipline R20; genitive-absolute R19). The apparatus had been refined primarily by applying these subtractive and boundary-preservation constraints. What it lacked was a corresponding affirmative rule codifying the positive direction of the merge-override principle: *when splitting a span produces fragments that individually fail the atomic-thought test, merge*.

Framework §1.5 M4 (Fragmented atomic thought-unit) stated this principle at the universal level. Per-corpus instantiation of M4 as a mechanical rule with a validator had not been done for the GNT. The principle was enforced editorially — by Stan's eye catching orphaned predicates on review — but not by the apparatus's mechanical pipeline. This created a gap between the framework's stated merge-override and its operational teeth.

The gap was not random. The GNT's household-code parenesis genre (Colossians 3, Ephesians 5–6, 1 Peter 5) employs a highly regular syntactic template that consistently generates the orphan-predicate failure mode: each directive opens with a nominative address NP (`Αἱ γυναῖκες,`, `οἱ ἄνδρες,`, `Τὰ τέκνα,`, `οἱ δοῦλοι,`) that is simultaneously the grammatical subject and the group being addressed, then places the imperative predicate on the next line. Split, each line fails the No-Anchor test. Merged, each is one clear ATU: identity + directive. This genre-systematic generation made the gap both predictable and correctable once the pattern was named.

### The predicate→complement dual

R10's protective logic is symmetrical: a matrix verb governing an obligatory ὅτι-clausal complement must keep that complement resolvable within the ATU, because the matrix without its complement is propositionally incomplete. The same logic applies one layer out: a subject NP that requires a matrix predicate for propositional completeness must keep that predicate on the same line, because the subject alone is not a proposition.

The parallelism is exact:

| Relation | Fragment A alone | Fragment B alone | Merged |
|---|---|---|---|
| Subject → Predicate (M4-GNT-1) | Subject NP (no predication) | Bare predicate (no subject) | One proposition |
| Predicate → Complement (R10) | Matrix verb (no complement) | Complement clause (no matrix) | One proposition |

In both cases, splitting a bond that the atomic-thought test requires to remain whole produces two non-atomic fragments. In both cases, the apparatus's answer is the same: the bond is the ATU.

## Grammatical grounding

### Subject NP shapes in Koine

Greek's synthetic morphology marks subject-verb agreement on the finite verb itself — nominal subjects are grammatically optional, which means that when an explicit subject NP *is* present, it carries pragmatic weight: it is marked, often topicalized, contrastive, or genre-required. This makes explicit subject NPs in the GNT a more restricted and semantically dense class than their English counterparts in BoFM text, and it shapes the closed-list `SUBJECT_SHAPES_M4_GNT1`:

- **C1 — Vocative-address NP in nominative subject position**: the household-code genre's characteristic subject form. The nominative plural (`Αἱ γυναῖκες`, `οἱ ἄνδρες`, `Τὰ τέκνα`) is simultaneously the grammatical subject of the following imperative and the addressed group. The double function — subject + vocative — creates the surface ambiguity that makes this class the most instructive for the G-exclusion architecture.
- **C2 — NP-with-appositive**: deity NPs and title NPs with genitival or appositional elaboration (`ὁ κύριος, ὁ θεὸς τῶν πνευμάτων τῶν προφητῶν,`). The appositive extends the NP rightward, making it surface as a "complete" line, masking the missing predicate.
- **C3 — NP-with-participial modifier**: a subject NP bearing an attributive or circumstantial participle that occupies a line by itself (`Ἰωσὴφ δὲ ὁ ἀνὴρ αὐτῆς, δίκαιος ὢν καὶ μὴ θέλων αὐτὴν δειγματίσαι,`). G5 override governs: the participial verbs on line A are non-finite and do not constitute a complete clause.
- **C4 — NP-with-relative-clause**: a subject NP extended by a relative clause, placing its finite predicate on the next line.
- **C5 — Biographical-introduction NP**: the `καί τις X ὀνόματι Y, [appositive,] [participle,]` template common in Acts and narrative contexts (Acts 16:14, Lydia).

### Household-code parenesis

The household-code (Haustafeln) genre in Pauline and deutero-Pauline letters and 1 Peter follows a tightly structured syntactic template: (1) addressee in nominative NP, (2) behavioral directive in imperative or equivalent, (3) motivational subordinate clause. The genre's structural regularity means that a single rule — merge the nominative addressee-NP with its imperative predicate — is genre-systematic rather than case-by-case. The eight household-code merges applied in commit `001604d` are not eight separate editorial decisions; they are one rule's uniform application across a genre.

### Biographical-introduction conventions

The `καί τις ... ὀνόματι ...` biographical-introduction formula in Acts and parallel narrative contexts regularly produces multi-token subject NPs followed by a verb of perception or action on the next line (Acts 16:14: `καί τις γυνὴ ὀνόματι Λυδία, πορφυρόπωλις πόλεως Θυατείρων, σεβομένη τὸν θεόν,` / `ἤκουεν`). The appositional and participial elaboration extends the NP to a natural line-break point, and the following simple finite verb is left stranded. C5 captures this convention.

### Deity-NP formulas

Revelatory and epistolary literature employs deity NPs with elaborate appositional chains (`αὐτὸς ὁ κύριος ἐν κελεύσματι, ἐν φωνῇ ἀρχαγγέλου καὶ ἐν σάλπιγγι θεοῦ,`). The elaboration is doxological — it expands the subject's identity — but the elaborated subject NP still requires a finite predicate for propositional completion. C2 captures this class; G4 separately carves out the edge case where a doxological *predicate* formula (`Ἄξιος εἶ`) is followed by an infinitival complement rather than a subject-less orphan predicate.

## Empirical evidence

### Corpus distribution

Sweep audit task `a0d7d74092a145179` (2026-05-11) processed all 27 NT books for the surface-pattern trigger (line A terminating in `,` or `·` with no finite verb, followed by line B with a bare finite predicate and no leading connective). Approximately 149 surface candidates were identified. After applying all 5 G-exclusions and 6 universal exclusions:

- **~15–20 clean Cat A cases** remained after full exclusion filtering
- **~130 correctly-excluded cases** where the surface trigger fired but a G-exclusion or universal exclusion blocked merge

The ~11 clean Cat A merges applied in commit `001604d` represent the highest-confidence subset of the 15–20 clean cases:

| Cluster | Count | Books |
|---|---|---|
| Household-code (C1) | 8 | Col 3:18, 3:19, 3:20, 3:22; Eph 5:25, 6:1, 6:5; 1 Pet 5:5 |
| Biographical-introduction (C5) | 1 | Acts 16:14 (Lydia) |
| NP-with-participial / G5 override (C3) | 1 | Matt 1:19 (Joseph) |
| Deity-NP (C2) | 1 | 1 Thess 4:16 |

**Skipped / excluded (4 of 15):**

- Acts 19:24 — G1 exclusion (line B starts with attributive participle `ποιῶν`, modifier of `ἀργυροκόπος` on line A, not a bare predicate)
- Luke 1:38 — G2 exclusion (`Ἰδοὺ ἡ δούλη κυρίου·` is a complete verbless clause by Greek ellipsis; `γένοιτό μοι` is a separate predication)
- Rev 22:6 — already merged (single line pre-existing; no action required)
- Heb 3:1 — already merged (single line pre-existing; no action required)

### G-exclusion validation

The five Greek-specific G-exclusions correctly discriminated non-firing cases in every audited instance:

- **G1 (attributive participle on line B)**: Acts 19:24 `ποιῶν ναοὺς ἀργυροῦς` — confirmed attributive modifier of `ἀργυροκόπος` by Greek participial syntax. Merging would attach a modifier chain as a predicate, producing a semantic distortion.
- **G2 (verbless nominal sentence)**: Luke 1:38 — `Ἰδοὺ ἡ δούλη κυρίου·` ends in `·` (Greek high stop = sentence boundary), confirming a complete verbless clause by Greek copula ellipsis. The following `γένοιτό μοι κατὰ τὸ ῥῆμά σου.` is Mary's response as a separate proposition.
- **G3 (periphrastic)**: no corpus instances requiring G3 exclusion emerged in the sweep; the exclusion is pre-emptive for constructions identifiable at Stage 2 UD parse.
- **G4 (doxological vocative + infinitival complement)**: Revelation `Ἄξιος εἶ` constructions correctly excluded; the doxological address units are complete predicative formulas, not orphaned subjects.
- **G5 (participial-only line A)**: Matt 1:19 — confirmed that `δίκαιος ὢν καὶ μὴ θέλων` are circumstantial participles, not finite predicates; the subject NP `Ἰωσὴφ δὲ ὁ ἀνὴρ αὐτῆς` is genuinely orphaned from its finite predicate `ἐβουλήθη`. G5 override correctly fires M4-GNT-1 here.

Zero false-negative exclusions were found: no case was excluded that should have merged, and no case was merged that should have been excluded.

## Intellectual lineage

### Framework M4 as the universal anchor

Framework §1.5 M4 (Fragmented atomic thought-unit) states: if splitting would produce fragments that individually fail the atomic-thought test, merge. M4-GNT-1 is the corpus-specific instantiation of this universal principle for the GNT's attested subject-shape inventory. The framework principle is abstract; the per-corpus rule is what gives it mechanical teeth in the GNT editorial apparatus.

### M4-BoFM-1 as the sister codification

M4-BoFM-1 (BoFM instantiation, codified 2026-05-11, commit `45ff06b`) is the closest precedent and structural template for M4-GNT-1. Both rules operationalize the same underlying principle (subject NP + bare predicate = one ATU) and share the same R10/R17 dual framing, the same closed-list architecture, and the same length-backstop heuristic. The key structural differences between the two instantiations are entirely corpus-driven:

| Dimension | M4-BoFM-1 | M4-GNT-1 |
|---|---|---|
| Subject shapes | A1 triad, A2 AICTP-head-NP, B1–B5 | C1 vocative-address NP, C2 NP-with-appositive, C3 NP-with-participial, C4 NP-with-relcl, C5 biographical-intro |
| Greek-specific exclusions | None (English morphology) | G1–G5 (Greek participle morphology, verbless-nominal ellipsis, periphrastic) |
| Primary genre cluster | Alma narrative; prophetic citation chains | Pauline household-code parenesis (Col, Eph, 1 Pet) |
| Corpus size | ~27 pre-codification violations / 11 books | ~11 clean Cat A / 27 books (denser exclusion filtering required) |

The G-exclusion architecture is M4-GNT-1's principal architectural contribution beyond M4-BoFM-1: five Greek-specific patterns had to be explicitly enumerated and closed because Koine Greek's morphosyntax generates surface lookalikes that English does not. This required a finer-grained exclusion apparatus and motivates the MorphGNT-aware Stage 2 filter in the validator.

### Pauline household-code parenesis tradition

The household-code genre (Haustafeln) is a well-documented NT form, studied in NT scholarship as a distinct literary-social genre (Balch 1981, Crouch 1972, Yoder Neufeld 1997). Its syntactic regularity — nominative addressee NP → imperative directive → motivational clause — is precisely what made the household-code cluster the most systematic and highest-confidence application of M4-GNT-1. The genre's structure is not the reason the rule applies (the atomic-thought test is), but it explains why the rule's application is genre-systematic rather than dispersed across idiosyncratic occurrences.

### R10 as the predicate→complement dual

R10 (Complement Integrity) in the GNT canon is the operational analog of R17 in the BoFM canon. Its logic: a matrix verb and its obligatory clausal complement form one cognitive frame. M4-GNT-1 instantiates the structurally symmetric logic one level up: subject NP + matrix predicate = one cognitive frame (the proposition). The apparatus now has both halves of the clause-integrity principle:

- **Subjectward (M4-GNT-1):** subject + predicate = one ATU
- **Complementward (R10):** predicate + complement = one ATU

### Cross-corpus tri-finding: the Tanakh asymmetry

The sweep audit that produced M4-GNT-1 was designed as a cross-corpus comparison: does the subject-orphan-predicate failure mode arise in the Hebrew Bible in a way requiring an analogous M4-TNK-1 rule? The answer is **no**, and the reason is architecturally significant:

Biblical Hebrew's verb-subject (VS) and subject-verb (SV) ordering options, combined with extensive pro-drop morphology, make the explicit-subject-NP-then-orphaned-predicate failure mode structurally rare. In Hebrew:
- Finite verbs carry person/number/gender agreement, effectively encoding the subject in the morphology; explicit subject NPs are already marked-constructions (topicalization, contrast, emphasis).
- When a subject NP does appear explicitly, it tends to follow the verb in VS order (rather than preceding it as a potential orphan-line), or to appear in casus-pendens construction (left-dislocation with a resumptive pronoun in the predicate clause).
- The VSO default means that any post-verbal NP is not typically mistakable for a predicate-less subject.

The audit task `a535fcbcc01012e3c` (Tanakh M4 audit, 2026-05-11) confirmed: **no M4-TNK-1 needed**. The VSO word order, pro-drop, and casus-pendens construction together make the GNT's orphan-predicate failure mode a cross-linguistic structural asymmetry, not a universal. This validates the principle's cross-corpus boundary: the atomic-thought test is universal; the morphosyntactic conditions that produce the subject-orphan failure mode are corpus-specific; per-corpus instantiation is therefore the correct architecture.

The tri-finding:
- BoFM (English-archaic SVO, explicit subjects): M4-BoFM-1 required, codified.
- GNT (Koine Greek SVO-flexible, explicit subjects present as marked constructions): M4-GNT-1 required, codified.
- Tanakh (Biblical Hebrew VSO+pro-drop+casus-pendens): M4-TNK-1 **not required** — the structural conditions for the failure mode are absent.

## Adversarial history

### Sweep audit task `a0d7d74092a145179`

The audit was dispatched 2026-05-11 as a corpus-wide sweep with explicit scope: *classify all ~149 surface candidates across 27 NT books, confirm or reject each G-exclusion, and identify the closed-list of eligible subject shapes and exclusion categories*.

**Methodology.** The audit applied a two-stage filter:
1. **Stage 1 (surface):** identify all line-pairs where line A terminates in `,` or `·` with no finite verb, and line B begins with a bare finite predicate and no leading connective.
2. **Stage 2 (structural):** apply all 5 G-exclusions and 6 universal exclusions to each Stage 1 hit; classify as Cat A (MERGE), Cat B (REVIEW), or Excluded (STAY-SPLIT).

**Findings.** The household-code cluster emerged as the highest-confidence subgroup: 8 cases across Col 3 and Eph 5–6 and 1 Pet 5 sharing the identical C1-vocative-subject + imperative-predicate template. The biographical-introduction cluster (Acts 16:14, Matt 1:19 via G5 override, and two pre-merged cases) and deity-NP cases (1 Thess 4:16, Rev 22:6 pre-merged) confirmed the principle's extension across genre.

**Critical exclusion verifications.** The audit's most important individual findings were the two non-obvious exclusions:
- Acts 19:24 (G1): `ποιῶν` was initially flagged as a potential bare-predicate lead. Structural analysis confirmed it is an attributive participle in a post-posed modifier construction common in Greek relative-clause equivalents. Merge would have misread a modifier as a predicate — a semantically harmful error. G1 exclusion correctly catches this class.
- Luke 1:38 (G2): `Ἰδοὺ ἡ δούλη κυρίου·` was initially flagged. The high-stop `·` marker and the verbless nominal structure (`ἡ δούλη` as predicate nominative with implied `εἰμί`) confirm a complete verbless clause. G2 exclusion correctly catches the Greek-ellipsis completeness pattern.

**Cross-corpus Tanakh audit (task `a535fcbcc01012e3c`).** A parallel audit of the Tanakh corpus confirmed the VSO/pro-drop asymmetry. The audit's negative result — no M4-TNK-1 needed — is itself evidence for the correct framing of M4-GNT-1: it validates that the subject-orphan failure mode is a property of the GNT's morphosyntax, not a universal feature of all corpora the ATU apparatus processes.

**Verdict.** The audit confirmed the five Greek-specific G-exclusion categories, the five closed-list subject shapes, the 11 non-overlapping exclusion conditions, and the 11 clean Cat A merges. Zero hostile counter-examples were found that required rule revision after audit. The rule proceeds to application-ready status without revision.

## Future work

### Phase B candidates (~140 surface, narrow with UD/MorphGNT-aware filters)

Approximately 130–138 of the 149 initial surface candidates were correctly excluded by the G-exclusions + universal exclusions. However, Stage 2 MorphGNT-aware filtering for G1 (attributive-participle-on-line-B) and G3 (periphrastic) required manual inspection for ambiguous cases. A MorphGNT-aware Stage 2 filter in `check_m4_gnt_1_subject_orphan.py` would automate this disambiguation by:
- Querying the MorphGNT parse for line B's lead token to confirm finite vs. participial morphology (G1 gate)
- Confirming finite mood (indicative/subjunctive/imperative) vs. infinitival or participial for G3/G5 classification

This would allow the validator to reliably narrow the Phase B candidates to clean Cat A merges without manual structural inspection of each instance.

### Cross-corpus harmonization

The BoFM and GNT instantiations of M4 now share a common structural template (closed-list subject shapes, exclusion-list architecture, length backstop, framework anchor). Future harmonization should ensure:
- The validator interfaces (`validate_m4_bofm_1_subject_orphan.py` and `check_m4_gnt_1_subject_orphan.py`) share a common atu-method infrastructure module for the merge-forward action, enabling cross-corpus regression testing.
- The `SUBJECT_SHAPES` and `EXCLUSION_LIST` closed lists in both validators are maintained in a machine-readable format in the atu-method repo for future cross-corpus analysis.

Any future corpus added to the ATU apparatus (a readers-LXX, a readers-Josephus, a readers-Mishnah) should run a corpus-sweep analogous to task `a0d7d74092a145179` before codifying its own M4 instantiation, following the tri-finding precedent that the Tanakh's structural asymmetry established.

---

*References:*

- Operational canon entry: `readers-gnt/private/01-method/colometry-canon.md §3.18 M4-GNT-1` (codified 2026-05-11, commit `001604d`)
- Universal framework: [`../../docs/framework.md`](../../docs/framework.md) §1.5 M4 (fragmented atomic thought-unit)
- Sister rule (predicate→complement): GNT canon §3.5 R10 (Complement Integrity / ὅτι-clause integrity)
- Sister corpus rule: [`../bofm/M4-BoFM-1.md`](../bofm/M4-BoFM-1.md) (BoFM instantiation, codified 2026-05-11)
- M4-TNK-1 deliberately NOT codified: Tanakh audit task `a535fcbcc01012e3c` confirmed Hebrew VSO+pro-drop+casus-pendens makes the subject-orphan failure mode structurally rare; no rule needed.
- Validator: `readers-gnt/validators/colometry/check_m4_gnt_1_subject_orphan.py`
- Audit trail: task `a0d7d74092a145179` (sweep audit completed 2026-05-11; ~149 surface candidates → ~11 clean Cat A after G-exclusions)
