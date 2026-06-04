# Substrate Feature Catalog

**Location:** `~/repos/atu-method/docs/substrate/feature-catalog.md`
**Status:** Living registry. Updated whenever a substrate feature lands, is revised, or is retired.
**Doctrine source:** `atu-method/docs/substrate.md` + this file's §7.3 audit-gate references.

---

## 0. Why this file exists

We are in the business of making our apparatuses **as optimized as possible for ATU revelation** — and, as a direct consequence, optimized for *other* reveal-by-reading lenses that the same substrate can power.

The substrate **is** the apparatus. ATU is **one lens**, not the only one. A mature Text-Fabric (TF) substrate decouples two things that the v1.5 binding-rule stage has historically conflated:

1. **WHAT-IS-THERE** — rich per-token / per-clause / per-period features (morphology, dependency role, agreement, equational status, postpositive class, te'am rank, parenthetical-signal, matrix-finiteness, shared-antecedent edges, prosodic phrase id, …).
2. **HOW-IT-IS-SEGMENTED** — the deterministic function `f(substrate) -> rendered-text` that produces a viewable layer.

Each lens (ATU, Korpel-colometric, Wackernagel, Marschall, Skousen-parenthetical, Wallace-diagrammatic, cantillation-prosody, Croft/Scheppers full-grammatical-unit, KJV-verse) is one such `f`. They draw from the **same** substrate, lit differently. A pill-button toggle in the reader UI switches `f` over the same verse range.

This catalog is the registry that prevents loss of these insights — features are documented at the point of extraction, with every consumer-lens hook named, so no lens-power gets stranded the next time the conversation compacts.

---

## 1. Per-feature entry schema

Every substrate feature MUST be catalogued with the following fields. Missing fields = the feature is not registered and cannot be relied on by any lens.

```
### <feature_name>

- **repo:** <which reader repo / substrate location owns extraction>
- **status:** proposed | under-revision | in-flight | shipped | retired
- **extraction_recipe_summary:** <1-3 sentences: what data source, what query/computation, what output node-type or edge-type in TF>
- **truth_set:** <path to gold/yardstick file used to validate extraction; required for shipped>
- **§7.3_audit_gate:** <date passed | pending | n/a-substrate-consumption>
- **multi_lens_consumers:** <per-lens hook table — see §2>
- **insertion_point:** <where in pipeline: v0-source | v0.5-tf-build | v1-treebank | v1.5-binding | v2-llm | v3-editorial>
- **downstream_consumers:** <named binding rules, lens renderers, validators, paper-claims that depend on this feature>
- **owner_notes:** <known limits, edge cases, ports across corpora>
```

### Lens-consumer hook format

For `multi_lens_consumers`, use a table. The hook column says *how the lens consumes the feature* (gate, signal, rank-input, edge-traversal, rendering-trigger). A lens that does not consume the feature is omitted; `n/a` is reserved for "considered and rejected" with a one-line reason.

```
| lens                          | consumer? | hook                                              |
|-------------------------------|-----------|---------------------------------------------------|
| ATU                           | yes       | gate for B<NN> bind/break                         |
| Korpel-colometric             | n/a       | <reason this Hebrew lens does not consume>        |
| Wackernagel-periods           | yes       | P1/P2 position re-rank input                      |
| Marschall-periods             | yes       | period-boundary candidate signal                  |
| Skousen-parenthetical         | no        | —                                                 |
| Wallace-diagrammatic          | yes       | clause-role rendering                             |
| Cantillation-prosody          | n/a       | <reason>                                          |
| Croft/Scheppers-FGU           | yes       | full-grammatical-unit closure test                |
| KJV-verse                     | no        | —                                                 |
```

---

## 2. Lens catalog (reference)

Cross-corpus lenses currently in scope. Each lens has its own `f(substrate) -> lens-rendered-text-file` renderer; this catalog tracks **which substrate features each `f` reads**.

| lens | corpus scope | maturity | one-line definition |
|---|---|---|---|
| ATU | Tanakh + GNT + BoFM + LXX + Vulgate | DEPLOYED (v1.5) | bidirectional-test smallest author-intended idea unit |
| Korpel/Masoretic-colometric | Hebrew | research | te'amim disjunctive hierarchy → colometric lines |
| Wackernagel-periods | Greek | research | period boundaries via P1/P2 postpositive position |
| Marschall hand-segmented periods | Greek (2 Cor 10-13 gold) | gold-anchored | Marschall's published period segmentation |
| Skousen parenthetical structure | BoFM | research | structural-signal layer (NOT punctuation-overlay; see `feedback_em_dashes_illustrative_not_text`) |
| Wallace diagrammatic | GNT | research | didactic clause-structure visualization |
| Cantillation-prosody | Hebrew | research | te'amim melodic phrase units (prosodic, not syntactic) |
| Croft/Scheppers full-grammatical-unit | cross-corpus (FEF/AICTP) | thesis-anchor | full-grammatical-unit closure (Croft) / clausal IU (Scheppers) |
| KJV-verse | all (legacy compare) | shipped | verse boundary as fall-through reference layer |

Lens-renderer code lives per reader repo at `tools/lenses/<lens_name>.py` (TBD path; pin once first non-ATU lens lands).

---

## 3. Seed entries — pipeline-A features (STATUS: under-revision-in-pipeline-A-revision)

These five features were extracted under pipeline-A and are currently under revision. Each must be re-audited against §7.3 before any new lens consumes them.

### tanakh-is-bare

- **repo:** `readers-tanakh`
- **status:** under-revision (pipeline-A revision)
- **extraction_recipe_summary:** Per-clause flag marking clauses with no overt subject NP (verb-only / null-subject). Derived from BHSA `function=Subj` absence at the clause node; cross-checked against Stanza fallback only where BHSA clause boundaries differ.
- **truth_set:** `readers-tanakh/private/substrate/yardstick/is-bare.json` (regen target; current file is pre-revision)
- **§7.3_audit_gate:** pending (revision invalidates prior pass)
- **multi_lens_consumers:**

  | lens | consumer? | hook |
  |---|---|---|
  | ATU | yes | gate for B-class bind on bare-clause continuation |
  | Korpel-colometric | yes | bare-clause often colon-internal, never colon-terminal |
  | Wackernagel-periods | n/a | Hebrew lens; Greek-only feature scope |
  | Marschall-periods | n/a | Greek-only |
  | Skousen-parenthetical | n/a | BoFM-only |
  | Wallace-diagrammatic | n/a | GNT-only |
  | Cantillation-prosody | yes | bare-clause prosodic-phrase-id constraint |
  | Croft/Scheppers-FGU | yes | bare-clause is FGU-internal by default |
  | KJV-verse | no | — |

- **insertion_point:** v0.5-tf-build (annotate at TF clause node)
- **downstream_consumers:** Hebrew binding rules B3, B7, B11 (per `binding-rules-hebrew.md`); Tanakh validator; LXX projection-v1 (Hebrew-source).
- **owner_notes:** Distinguish "bare" (null subject) from "elided-subject" (recoverable from prior clause); pipeline-A conflated them.

### tanakh-agreement

- **repo:** `readers-tanakh`
- **status:** under-revision (pipeline-A revision)
- **extraction_recipe_summary:** Per-clause record of person/number/gender agreement between finite verb and overt-or-recovered subject. Drawn from BHSA `ps`/`nu`/`gn` features.
- **truth_set:** `readers-tanakh/private/substrate/yardstick/agreement.json` (regen target)
- **§7.3_audit_gate:** pending
- **multi_lens_consumers:**

  | lens | consumer? | hook |
  |---|---|---|
  | ATU | yes | gate for shared-subject BIND across coordinated clauses |
  | Korpel-colometric | no | — |
  | Wackernagel-periods | n/a | Hebrew-only feature |
  | Marschall-periods | n/a | Greek-only |
  | Skousen-parenthetical | n/a | BoFM-only |
  | Wallace-diagrammatic | n/a | GNT-only |
  | Cantillation-prosody | no | — |
  | Croft/Scheppers-FGU | yes | agreement-continuity is FGU-cohesion signal |
  | KJV-verse | no | — |

- **insertion_point:** v0.5-tf-build (clause-node feature)
- **downstream_consumers:** Hebrew binding rules B5, B9; cross-corpus shared-subject heuristics ported to BoFM v1.5.
- **owner_notes:** Pipeline-A treated agreement-mismatch as automatic BREAK; revision should treat as one signal among several (see §7.3 audit).

### gnt-matrix-finite

- **repo:** `readers-gnt`
- **status:** under-revision (pipeline-A revision)
- **extraction_recipe_summary:** Per-clause flag marking the clause whose finite verb is the matrix predicate of its sentence (vs. embedded finite verbs in ὅτι-clauses, ἵνα-purpose, relative, etc.). Sourced from Macula `clause` + `that-VP` + `sub-CL` features (per `reference_greek_datasets.md`).
- **truth_set:** `readers-gnt/private/substrate/yardstick/matrix-finite.json` (regen target)
- **§7.3_audit_gate:** pending
- **multi_lens_consumers:**

  | lens | consumer? | hook |
  |---|---|---|
  | ATU | yes | matrix-finite is BIND-anchor for embedded complement |
  | Korpel-colometric | n/a | Hebrew-only lens |
  | Wackernagel-periods | yes | matrix-finite establishes period domain for P1/P2 search |
  | Marschall-periods | yes | period-closure candidate at matrix-finite return |
  | Skousen-parenthetical | n/a | BoFM-only |
  | Wallace-diagrammatic | yes | matrix is diagram root |
  | Cantillation-prosody | n/a | Hebrew-only |
  | Croft/Scheppers-FGU | yes | matrix-finite anchors FGU |
  | KJV-verse | no | — |

- **insertion_point:** v0.5-tf-build (clause-node feature, Macula-sourced)
- **downstream_consumers:** GNT binding rules (ὅτι complement-vs-quote handling per `feedback_mechanical_first_for_own_review`); FEF/AICTP empty-frame analysis (`project_fef_aictp_paper`); LXX-NT projection (where applicable).
- **owner_notes:** Pipeline-A under-used Macula's `that-VP` discrimination — the "structurally impossible, defer to v2" error documented in `feedback_mechanical_first_for_own_review`. Revision MUST consume `that-VP` + `sub-CL` before declaring a ὅτι-clause indeterminate.

### gnt-equational-cola

- **repo:** `readers-gnt`
- **status:** under-revision (pipeline-A revision)
- **extraction_recipe_summary:** Per-clause flag for copular / equational constructions (εἰμί + predicate nominative/adjective; verbless equationals in conditional protases). Sourced from Macula clause-role + lemma + part-of-speech.
- **truth_set:** `readers-gnt/private/substrate/yardstick/equational-cola.json` (regen target)
- **§7.3_audit_gate:** pending
- **multi_lens_consumers:**

  | lens | consumer? | hook |
  |---|---|---|
  | ATU | yes | equational-cola are atomic — bidirectional test passes minimally |
  | Korpel-colometric | n/a | Hebrew-only lens |
  | Wackernagel-periods | yes | equational clauses constrain P2 placement |
  | Marschall-periods | yes | rarely a period-boundary candidate |
  | Skousen-parenthetical | n/a | BoFM-only |
  | Wallace-diagrammatic | yes | equational is a distinct diagram shape |
  | Cantillation-prosody | n/a | Hebrew-only |
  | Croft/Scheppers-FGU | yes | equationals are minimal FGUs |
  | KJV-verse | no | — |

- **insertion_point:** v0.5-tf-build (clause-node feature)
- **downstream_consumers:** GNT binding rules for predicate-nominative BIND; Vulgate-NT (PROIEL) parallel feature; LXX-Greek equational handling.
- **owner_notes:** Verbless protases were under-counted in pipeline-A; revision should annotate even when no overt copula present.

### gnt-shared-matrix-antecedent

- **repo:** `readers-gnt`
- **status:** under-revision (pipeline-A revision)
- **extraction_recipe_summary:** Cross-clause edge: linking each embedded / coordinated clause to the matrix-finite clause whose subject/antecedent it shares. Derived from Macula `referent` feature + clause-role + person/number agreement.
- **truth_set:** `readers-gnt/private/substrate/yardstick/shared-matrix-antecedent.json` (regen target)
- **§7.3_audit_gate:** pending
- **multi_lens_consumers:**

  | lens | consumer? | hook |
  |---|---|---|
  | ATU | yes | shared-antecedent is BIND-candidate gate (over-merge red-line: REQUIRES adversarial audit per default decisions) |
  | Korpel-colometric | n/a | Hebrew-only lens |
  | Wackernagel-periods | yes | shared antecedent extends period domain |
  | Marschall-periods | yes | shared antecedent argues against period closure |
  | Skousen-parenthetical | n/a | BoFM-only |
  | Wallace-diagrammatic | yes | edge in the diagram |
  | Cantillation-prosody | n/a | Hebrew-only |
  | Croft/Scheppers-FGU | yes | shared antecedent extends FGU |
  | KJV-verse | no | — |

- **insertion_point:** v0.5-tf-build (TF edge-feature between clause nodes)
- **downstream_consumers:** GNT binding rules for ellipsis/coordination BIND; FEF/AICTP shared-frame analysis.
- **owner_notes:** Highest over-merge risk among the five — Stan's red-line per CLAUDE.md. Every consumer-lens that uses this edge as a BIND signal must be gated through the §3-default ≥2-parallel-adversarial-audit `Workflow`.

---

## 4. Seed entries — pipeline-B features (STATUS: in-flight-pipeline-B)

Thirteen features currently in flight under pipeline-B. Stub-level catalog entries; each MUST be filled in (extraction recipe + truth set + §7.3 audit + lens-consumer table) before merging into substrate.

| # | feature_name | repo | one-line scope |
|---|---|---|---|
| B-01 | (pending name) | (pending) | (pending) |
| B-02 | (pending name) | (pending) | (pending) |
| B-03 | (pending name) | (pending) | (pending) |
| B-04 | (pending name) | (pending) | (pending) |
| B-05 | (pending name) | (pending) | (pending) |
| B-06 | (pending name) | (pending) | (pending) |
| B-07 | (pending name) | (pending) | (pending) |
| B-08 | (pending name) | (pending) | (pending) |
| B-09 | (pending name) | (pending) | (pending) |
| B-10 | (pending name) | (pending) | (pending) |
| B-11 | (pending name) | (pending) | (pending) |
| B-12 | (pending name) | (pending) | (pending) |
| B-13 | (pending name) | (pending) | (pending) |

> **Action item:** Pipeline-B is in-flight at the time of this catalog's creation; the 13 feature names + recipes are tracked in the pipeline-B working files but have not yet been frozen for catalog entry. Each entry MUST be promoted to a full §1-schema record before the feature ships to substrate. **Do not let pipeline-B features land in substrate without populating this catalog** — that is the loss-of-insight failure mode this file exists to prevent.

A pipeline-B promotion checklist per feature:

1. Name fixed (`<corpus>-<feature-noun>` convention).
2. Repo + extraction recipe + truth-set path filled.
3. §7.3 audit gate passed (≥2 parallel adversarial audits per `feedback_never_skip_audit_gate`).
4. `multi_lens_consumers` table filled — every lens in §2 either has a hook or has an explicit `n/a` with reason.
5. `insertion_point` + `downstream_consumers` named.
6. Entry committed to this file in the same atomic ship as the substrate code change (per `feedback_workflow` atomic-ship doctrine).

---

## 5. Adding a new substrate feature — required workflow

A new feature does NOT enter substrate by being extracted. It enters by clearing this gate:

### 5.1 §7.3 audit gate — REQUIRED

Per CLAUDE.md standing default #7 + `feedback_never_skip_audit_gate`:

> New mechanism / new integration / new env-flag / new guard structure triggers the §7.3 audit gate BEFORE code, not after. Substrate consumption (reading existing data on disk) is exempt; building a new code-integration shape over substrate is NOT.

A new substrate feature is, by definition, a new code-integration shape. It is NOT exempt. Before extraction code is written:

- Dispatch ≥2 parallel adversarial audits via a `Workflow` script (NOT hand-spawned `Agent` calls — per standing default #2).
- Lens A: over-merge / over-extraction (does this feature falsely collapse distinctions?).
- Lens B: atomicity / under-extraction (does this feature falsely split or miss cases?).
- A third lens (NLP-domain or workflow per `feedback_three_lens_default_for_plans`) where the feature is non-trivial.
- Survivors of all lenses proceed; non-survivors halt the workflow and return findings.

### 5.2 multi_lens_consumers — REQUIRED

Every lens in §2 must appear in the new feature's consumer table — either with a named hook, or with an explicit `n/a` + one-line reason. Silent omission is forbidden, because silent omission is how lens-power gets lost.

Rule of thumb: if you can name the hook in <10 words, the feature is mature enough to ship. If the hook is hand-wavy ("might help with prosody"), the feature is not ready — sharpen or omit.

### 5.3 truth_set — REQUIRED

Per CLAUDE.md standing default #7 + `feedback_conformance_is_not_correctness`:

> Conformance ≠ correctness. Source-parity is the correctness gate; index-parity is regression-only.

Every feature ships with a gold/yardstick file used to validate extraction against ground truth, NOT just internal consistency. Reuse existing yardsticks where possible (BHSA, Macula, BoFM gold yardstick, UD_Latin-PROIEL, LXX Gen+Ruth gold). Build a new yardstick only when no existing one covers the feature.

The truth-set lives in `<repo>/private/substrate/yardstick/<feature-name>.json` and is referenced from this catalog.

### 5.4 Atomic-ship requirement

Per `feedback_workflow` atomic-ship doctrine: catalog entry + extraction code + truth set + validator hook ship as ONE commit. A merged feature without a catalog entry is a regression and must be reverted (per CLAUDE.md default decision "Apply causes regression → Revert → root-cause → fix → re-apply").

### 5.5 Worked example — adding `gnt-postpositive-class`

(Illustrative; not yet in flight.)

1. **§7.3 audit:** `Workflow` dispatches Opus-lens-over-merge + Opus-lens-atomicity + Sonnet-lens-NLP-domain. Question: does the categorical scheme {true-postpositive, conditional-postpositive, never-postpositive} cleanly cover δέ, γάρ, μέν, οὖν, τε, ἄν, …? Survivors return refined scheme.
2. **Extraction:** Per-token feature on TF word node; computed from lemma + Wackernagel positional analysis in Macula.
3. **Truth set:** `readers-gnt/private/substrate/yardstick/postpositive-class.json` — hand-checked sample of 200 instances across Gospels + Paul + General Epistles + Revelation.
4. **multi_lens_consumers:**

   | lens | consumer? | hook |
   |---|---|---|
   | ATU | yes | postpositive cannot host a BIND/BREAK boundary |
   | Korpel-colometric | n/a | Hebrew-only |
   | Wackernagel-periods | yes | core signal — defines P1/P2 search |
   | Marschall-periods | yes | period-internal-only constraint |
   | Skousen-parenthetical | n/a | BoFM-only |
   | Wallace-diagrammatic | yes | rendered inline with host |
   | Cantillation-prosody | n/a | Hebrew-only |
   | Croft/Scheppers-FGU | yes | postpositive is FGU-internal by default |
   | KJV-verse | no | — |

5. **insertion_point:** v0.5-tf-build (word-node feature).
6. **downstream_consumers:** Wackernagel-period lens renderer; Marschall comparison; GNT binding rule revision (boundary-host constraint).
7. **Atomic ship:** catalog entry + extraction code + yardstick + Wackernagel renderer hook in one commit.

---

## 6. Catalog hygiene

- This file is loaded on trigger when working on substrate / lens / pipeline-B work (per CLAUDE.md consult-on-trigger).
- Pair every status change (proposed → in-flight → shipped → retired) with a commit to this file.
- When a feature is retired, leave the entry with `status: retired` + one-line reason — do NOT delete. Retired entries are the institutional memory that prevents re-litigating closed routes (per CLAUDE.md "Closed routes" doctrine).
- Cross-link from `atu-method/docs/substrate.md` (doctrine) → here (registry) → per-repo `private/substrate/yardstick/*.json` (truth sets).
- When a lens reaches "shipped" status in a reader's pill-button toggle UI, add the deployment date to its §2 row.

---

## 7. Open threads

- **Pipeline-B feature names** — fill in §4 table as soon as the 13 names freeze.
- **Lens renderer path convention** — pin `tools/lenses/<lens_name>.py` once first non-ATU lens lands; update §2 footnote.
- **Cross-corpus feature ports** — when a feature proves itself in one corpus (e.g., `tanakh-agreement`), check `feedback_check_prior_corpora` discipline before re-implementing in another; port via shared TF feature where possible.
- **Pill-button toggle UX** — UI shell for lens switching is separately tracked in the reader repos; this catalog supplies the data contract that the UI consumes.