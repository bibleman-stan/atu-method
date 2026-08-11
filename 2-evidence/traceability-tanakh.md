# Traceability — Tanakh: theory → rule → validator

**Generated** by `5-machinery/scripts/build_traceability_index.py`. Regenerate rather than hand-edit the table; the Grounding column is the exception and is curated by hand.

- Constraints in catalog: **26**
- With a scholarly `Source`: **26/26**
- With a name-matched validator: **17/26**
- Validators with no matching constraint: **14**

> The catalog is at `readers-tanakh/_archive/2026-05-18-mechanical-first-rewrite/`.
> It is **archived**, marked `Status: DRAFT`, and the six live files in
> `1-method/canon/constraints/` still point to it as their master index.

## Grounding vocabulary

| Value | Means |
|---|---|
| `GROUNDED` | Source asserts the unit coheres **and** that this bears on segmentation |
| `DESCRIBED` | Source establishes the phenomenon; the segmentation inference is ours |
| `PROJECT` | No external source — a deliberate engineering decision |
| `UNGROUNDED` | Neither source nor rationale — candidate for retirement |
| `UNVERIFIED` | Not yet judged by a human. The generator never guesses. |

## Constraints

*Grounding judged: **1/26**. Curated in `2-evidence/traceability-grounding.json`, merged at build time so regenerating never discards it.*

| Constraint | Source (scholarship) | Validator | Grounding |
|---|---|---|---|
| [[JM13-maqqef-group]] | Joüon §13; Layer 1 hebrew-break-legality.md row H1 | `validate_maqqef_integrity` | `UNVERIFIED` |
| [[JM103-proclitic-stranding]] | Joüon §103 (prepositions), §137 (conjunction waw), §125 (object marker), §160 (negation) | **— none —** | `UNVERIFIED` |
| [[JM103e-compound-prep-object]] | Joüon §103e | `validate_compound_preposition_object` | `UNVERIFIED` |
| [[JM129-construct-chain]] | Joüon §129; WO §9.3, §9.5; canon H2 | `validate_construct_chain`<br>`validate_bare_construct_head` | `UNVERIFIED` |
| [[JM125-verb-object-bond]] | Joüon §125; WO §10.2.1; canon M2 | `validate_verb_object_bond` | `UNVERIFIED` |
| [[JM125-coordinated-objects]] | Joüon §125; WO §10.2.1; canon M2 + SJ1 | `validate_coordinated_object` | `UNVERIFIED` |
| [[JM157-complement-integrity]] | Joüon §157; WO §38.3; canon H7 | `validate_complement_integrity` | `UNVERIFIED` |
| [[JM177-bonded-pair]] | Joüon §177; WO §4.6.5; canon M1 | `validate_bonded_pair` | `UNVERIFIED` |
| [[JM154-verbless-clause-nucleus]] | Joüon §154; WO §8.4; canon H18.1 | `validate_clause_nucleus_split` | `UNVERIFIED` |
| [[JM121-participial-predicate]] | Joüon §121; WO §37.6; canon H18.2 | `validate_participial_speech_frame` | `UNVERIFIED` |
| [[JM133-verb-pp-complement]] | Joüon §133; WO §11.4.1; canon H18.3 / M2 | `validate_verb_object_bond`<br>`validate_complement_integrity` | `UNVERIFIED` |
| [[JM155-discourse-particle]] | Joüon §155; AC §4.5; canon H14 + M3 | `validate_bare_discourse_particle` | `UNVERIFIED` |
| [[JM161-interrogative-particle]] | Joüon §161; canon M3 | `validate_interrogative_clause`<br>`validate_bare_discourse_particle` | `UNVERIFIED` |
| [[JM156-casus-pendens]] | Joüon §156; WO §4.7; canon H15 | **— none —** | `UNVERIFIED` |
| [[JM-oath-formula]] | Joüon §147 (oaths and adjurations); canon M4 + §1 formula integrity | `validate_oath_formula` | `UNVERIFIED` |
| [[JM-cross-verse-continuity]] | Canon H10; §1 versification-is-not-a-break-signal | `validate_cross_verse_continuity` | `PROJECT` — cites only Canon H10 and our own §1; the JM prefix implies Joüon but no section is given |
| [[JM-wayehi-fef-protasis]] | Joüon §155 / WO §33.1.1c; canon H16 | `validate_wayehi_protasis` | `UNVERIFIED` |
| [[JM158-restrictive-relative]] | Joüon §158; WO §19.1 | **— none —** | `UNVERIFIED` |
| [[JM158-nonrestrictive-relative]] | Joüon §158; WO §19.3 | **— none —** | `UNVERIFIED` |
| [[JM168-purpose-clause]] | Joüon §168; WO §36.2.2; canon H7 extension | **— none —** | `UNVERIFIED` |
| [[JM159e-conditional-protasis]] | Joüon §159e; WO §38.1 | `validate_wayehi_protasis` | `UNVERIFIED` |
| [[JM174-gapped-verb]] | Joüon §174 (gapping); WO §8.3.2 | `validate_verb_object_bond` | `UNVERIFIED` |
| [[JM157-ki-recitativum]] | Joüon §157.3; WO §39.3.4; canon H7 complement integrity | **— none —** | `UNVERIFIED` |
| [[JM123-inf-abs-predicate]] | Joüon §123; WO §35.3 | **— none —** | `UNVERIFIED` |
| [[JM147-vocative-extraclausal]] | Joüon §147 (vocative and extra-clausal elements); WO §4.7; canon H4 | **— none —** | `UNVERIFIED` |
| [[JM160-negation-scope]] | Joüon §160 (לֹא / אַל / אֵין); WO §39.3.3 | **— none —** | `UNVERIFIED` |

## Validators with no matching constraint

Each is either implementing a rule absent from the catalog, or implementing nothing the catalog knows about. Both are defects.

- `check_canon_alignment`
- `check_canon_extensions`
- `validate_blessed_cursed_chain`
- `validate_canon_retirement_residue`
- `validate_causal_ki`
- `validate_doc_pointers`
- `validate_genealogy_uniformity`
- `validate_line_final_tokens`
- `validate_list_formula_uniformity`
- `validate_parallel_clause_split`
- `validate_parallel_series_uniformity`
- `validate_short_orphan_line`
- `validate_short_verse_fronting`
- `validate_speech_intro_framing`
