# Architecture — Four Planes

The ATU apparatus separates concerns into **four planes**, not stacked layers. Each plane is internally coherent (all data, all spec, all tooling, or all delivery); planes interact through defined interfaces.

This document is normative for any project consuming `atu-method`. Drift from this architecture indicates either a documentation gap or a design error.

---

## Plane summary

```
┌─────────────────────────────────────────────────────────────────┐
│ DATA PLANE                                                       │
│   • Source texts (canonical, immutable, per-repo)                │
│   • Parsed corpora (Macula / CoNLL-U — regenerable from source)  │
│   • Edited corpora (v2-mine / v2-he / v2-greek — append-only via │
│     git history)                                                 │
│   • Transaction logs (TxLog files — append-only)                 │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ SPECIFICATION PLANE                                              │
│   • Framework (§0/§1/§2/§7) — shared in atu-method/docs/         │
│   • Glossary (universal terms) — shared in atu-method/docs/      │
│   • Cross-project discipline memories — shared in atu-method/    │
│   • Rule detail (§5) — per-repo, MISRA-style operational template│
│   • Layer 1 syntax-floor tables — per-repo, language-specific    │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ TOOLING PLANE                                                    │
│   • Query interface (Token/Sentence primitives)                  │
│   • Parse adapters (Macula-lowfat, CoNLL-U)                      │
│   • Detectors (UD-query validators reading data + spec)          │
│   • Appliers (char-offset-precise mutators with TxLog)           │
│   • Dashboard / parity-test / review-queue runners               │
│   • Audit gates (commit hooks, baseline checks)                  │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ DELIVERY PLANE                                                   │
│   • Build pipeline (corpus → HTML fragments) — per-repo          │
│   • Reader UI (web app, swap system, study layers) — per-repo   │
│   • Audio / morpheme / study overlays — per-repo                 │
└─────────────────────────────────────────────────────────────────┘

ORTHOGONAL: WORKFLOW
  Audit-then-apply discipline, §7.3 mandatory-audit triggers, change
  protocol. Describes how operators use the tooling plane on the spec
  plane against the data plane. Lives in atu-method/docs/change-protocol.md
  plus per-repo CLAUDE.md operational sections.
```

---

## Plane ownership: shared vs. per-repo

| Plane component | Shared in atu-method | Per-repo (readers-{bofm,gnt,tanakh}) |
|---|---|---|
| Source text | — | ✓ |
| Parsed corpus | — | ✓ |
| Edited corpus | — | ✓ |
| Transaction logs | — | ✓ |
| Framework (§0/§1/§2/§7) | ✓ | (referenced, not duplicated) |
| Glossary | ✓ (universal terms) | ✓ (project-specific terms only) |
| Discipline memories | ✓ | (referenced, not duplicated) |
| Rule detail (§5) | — | ✓ |
| Layer 1 syntax-floor | — | ✓ (language-specific) |
| Query interface (parsing) | ✓ | (consumed) |
| Parse adapters | ✓ | (consumed) |
| Detectors | (base classes / patterns) | ✓ (concrete implementations) |
| Appliers | (base class) | ✓ (concrete implementations) |
| Dashboard / parity / review-queue | ✓ | (consumed) |
| Audit gates | ✓ | (wired per-repo) |
| Build pipeline | — | ✓ |
| Reader UI | — | ✓ |
| Audio / study overlays | — | ✓ |

The pattern: **infrastructure and methodology framework shared; data and delivery per-repo; rule detail and detector implementations per-repo with patterns shared.**

---

## Interface contracts between planes

### Data plane → Specification plane

The specification plane describes the editorial methodology and rule set; it does not consume data directly. Cross-references from spec to data (e.g., "canonical case: Alma 12:26") are illustrative, not load-bearing.

### Specification plane → Tooling plane

Detectors in the tooling plane consume rule specifications from the specification plane. The interface is:

- **Rule signature** — YAML in each rule's §5 entry, describing the UD pattern that triggers the rule and the action to take.
- **Closed lists** — Named lemma / category sets cross-referenced from rule signatures. Detectors load these at start.
- **Precedence hierarchy** — §3.5 of each per-repo canon. Detectors must filter candidates that match higher-tier rules out of lower-tier buckets.

Drift between the rule signature in the canon and the actual detector implementation is a **failure** — detected manually for now; future versions will validate machine-checkable.

### Data plane ↔ Tooling plane

- Detectors **read** the parsed corpus (Layer 2 of the data plane) and emit verdicts (`STRONG-MERGE-CANDIDATE`, `STRONG-SPLIT-CANDIDATE`, `REVIEW-REQUIRED`, etc.).
- Appliers **write** to the edited corpus (v2-* files) via the TxLog, supporting rollback on regression.
- The build pipeline (delivery plane) **reads** the edited corpus and produces HTML fragments.

### Workflow ↔ all planes

The audit-then-apply discipline operates **across** planes. It governs:

- When canon changes (specification plane) require audit-evidence in commit messages.
- When detector outputs (tooling plane) are application-ready vs. require manual review.
- When data-plane mutations require baseline-check before commit.

See [`change-protocol.md`](change-protocol.md) for the operational workflow.

---

## Internal structure of the Tooling plane — cognitive-labor partitioning

The four-plane model carves by **where things live** (data / spec / tooling / delivery). It does not by itself describe the internal task-type structure of the Tooling plane. As LLM-augmented operations have become load-bearing in the apparatus (R19 resolver; passage-level audit; future v1→v2 generative pass), a complementary view is needed: **what kind of cognitive work each tool does**.

The Tooling plane subdivides internally into four **legs**, each fit for a different task type:

1. **Mechanical floor** — UD parsing, Layer-1 prohibitions, source-text anchoring, coarse candidate-break generation. Deterministic; cheap; scales freely.
2. **Point-rule validators (R/H stack)** — pattern-specific break-legality. Mechanical execution; §7.3-audit-gated for proposal of new rules / closed lists / sub-categories.
3. **LLM resolver for validator-flagged residue** — per-instance judgment within bounded rule scope. Operates on REVIEW outputs; agreement-scored across runs.
4. **LLM passage-level audit over rendered output** — holistic "is this rendering over-broken?" check. Operates over rendered v2 (not parse input). Catches what point-rules structurally cannot see.

These legs differ in cost profile, auditability, discipline requirements, and failure modes — distinctions that matter for system design and that the four-plane model alone does not surface.

**For the substantive description** of the four legs, the extended bidirectional test (with the cognitive-unity gate for parallel poetry), the coarse-anchor principle, the two-phase candidate-vs-adjudication processing model, and what is still missing from the toolset, see [`toolset-architecture.md`](toolset-architecture.md).

The two documents are complementary, not redundant: `architecture.md` (this file) is normative for where code and data live; `toolset-architecture.md` is normative for which task type each tool is fit for.

---

## Drift prevention

The four-plane architecture is durable only if drift is controlled:

1. **Rule signatures live in the canon, not the detector.** When a rule changes, the canon is the source of truth; the detector is updated to match. Future versions of `atu-method` will provide a mechanical alignment check.

2. **Framework material lives in atu-method/docs/, not in per-repo canons.** Per-repo canons reference framework sections by stable ID (e.g., "see atu-method/docs/framework.md §1.4 N=2 Adjudication"). They do **not** duplicate framework prose.

3. **Discipline memories live in atu-method/memories/, not in per-repo canons.** Per-repo canons reference memories by name (e.g., "per `feedback_rhetoric_bandwagon`"). They do not restate the memory's content.

4. **Cross-project consistency is enforced by the four-plane assignment.** If a piece of content is "shared" it goes in atu-method; if "per-repo" it stays in the respective reader. Mixed ownership (same content in two places) is the failure mode that produced the original drift.

---

## What this architecture replaces

This four-plane decomposition supersedes earlier informal descriptions of the apparatus as "a 7-layer mechanical apparatus" or similar stacked-layer framings. The 7-layer enumeration was useful as memorable shorthand but technically misleading — its "layers" mixed data, spec, tooling, workflow, and delivery as peers. Four planes, each internally coherent and externally interfaced, matches standard software architecture practice (Clean Architecture, Hexagonal Architecture, Domain-Driven Design) and standard digital-scholarly-editing practice (TEI / CTS / OHCO).

Plain operational language (validators, canon, build pipeline, swap system) is preferred over architectural jargon in day-to-day work. Architectural terminology (data plane, specification plane, tooling plane, delivery plane) is reserved for system-design conversations and this document.
