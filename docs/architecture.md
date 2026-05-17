# Architecture — Four Planes

The ATU apparatus separates concerns into four planes, not stacked layers. Each plane is internally coherent (all data, all spec, all tooling, or all delivery); planes interact through defined interfaces.

This document is normative for any project consuming `atu-method`. Drift from this architecture indicates either a documentation gap or a design error.

---

## Plane summary

```
┌─────────────────────────────────────────────────────────────────┐
│ DATA PLANE                                                       │
│   • Source texts (canonical, immutable, per-repo)                │
│   • Parsed corpora (Macula / CoNLL-U — regenerable from source)  │
│   • Rendered corpora (v2-mine / v2-he / v2-greek — committed via │
│     git history)                                                 │
│   • Transaction logs (TxLog files — append-only)                 │
│   • Source-text anchoring (TAHOT, Strong's, Skousen)             │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ SPECIFICATION PLANE                                              │
│   • Framework — shared in atu-method/docs/                       │
│   • Glossary (universal terms) — shared in atu-method/docs/      │
│   • Cross-project discipline memories — shared in atu-method/    │
│   • Constraint catalog — per-repo, language-specific             │
│   • Minimal-rubric prompt — per-repo, language-specific          │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ TOOLING PLANE                                                    │
│   • Source-text anchoring (Macula, TAHOT, Strong's, Skousen)     │
│   • Parse adapters (Macula-lowfat, CoNLL-U)                      │
│   • LLM identification stage (minimal rubric)                    │
│   • Constraint catalog audit stage                               │
│   • Editorial review surface                                     │
│   • KJV-alignment subsystem (atu_method/kjv_alignment/)          │
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
  Audit-then-apply discipline, mandatory-audit triggers, change
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
| Rendered corpus | — | ✓ |
| Transaction logs | — | ✓ |
| Source-text anchoring | (universal infrastructure) | ✓ (per-corpus tables) |
| Framework | ✓ | (referenced, not duplicated) |
| Glossary | ✓ (universal terms) | ✓ (project-specific terms only) |
| Discipline memories | ✓ | (referenced, not duplicated) |
| Constraint catalog | (template + cross-corpus map) | ✓ (language-specific entries) |
| Minimal-rubric prompt | (cross-corpus template) | ✓ (per-language specialization) |
| Parse adapters | ✓ | (consumed) |
| LLM identification stage | ✓ (orchestration) | ✓ (prompt + audit calls) |
| Constraint catalog audit stage | ✓ (orchestration) | ✓ (concrete constraint implementations) |
| Editorial review surface | (pattern) | ✓ (per-repo workflow) |
| KJV-alignment subsystem | ✓ (full implementation) | (consumed via thin wrapper) |
| Audit gates | ✓ | (wired per-repo) |
| Build pipeline | — | ✓ |
| Reader UI | — | ✓ |
| Audio / study overlays | — | ✓ |

The pattern: **infrastructure and methodology framework shared; data and delivery per-repo; constraint detail per-repo with patterns and orchestration shared.**

---

## Interface contracts between planes

### Data plane → Specification plane

The specification plane describes the editorial methodology and constraint catalog; it does not consume data directly. Cross-references from spec to data (e.g., "canonical case: Alma 12:26") are illustrative, not load-bearing.

### Specification plane → Tooling plane

The constraint catalog audit stage in the tooling plane consumes constraint specifications from the specification plane. The interface is:

- **Encoded question** — the yes/no grammatical question the constraint answers (per-rule field in the catalog entry).
- **Closed lists** — Named lemma / category sets cross-referenced from constraint entries. Audit stage loads these at start.
- **Precedence hierarchy** — Per-repo canon section defining order of evaluation when multiple constraints fire on the same break.

Drift between the constraint description in the canon and the actual implementation is a **failure** — detected by `canon-validator-alignment-protocol.md` per-repo script.

### Data plane ↔ Tooling plane

- **LLM identification stage reads** the source text + minimal-rubric prompt; emits a proposed ATU-segmented rendering.
- **Constraint catalog audit stage reads** the proposed rendering + the parsed corpus; emits a violation report per proposed break.
- **Editorial review** consumes both; writes to the rendered corpus via TxLog with rollback support.
- **Build pipeline** (delivery plane) reads the rendered corpus and produces HTML fragments.

### Workflow ↔ all planes

The audit-then-apply discipline operates across planes. It governs:

- When canon changes (specification plane) require audit-evidence in commit messages.
- When constraint audit outputs (tooling plane) are application-ready vs. require manual review.
- When data-plane mutations require baseline-check before commit.

See [`change-protocol.md`](change-protocol.md) for the operational workflow.

---

## Internal structure of the Tooling plane — cognitive-labor partitioning

The four-plane model carves by **where things live** (data / spec / tooling / delivery). It does not by itself describe the internal task-type structure of the Tooling plane. A complementary view is needed: **what kind of cognitive work each tool does**.

The Tooling plane subdivides into three stages, each fit for a different task type:

1. **LLM identification** — applies the minimal rubric (bidirectional test + restrictive-relative binding + small language-specific constraints) to source text; produces ATU-segmented proposal.
2. **Constraint catalog audit** — applies the per-language syntactic constraint catalog to the proposed rendering; emits violation report. Mechanical execution; constraints expressed as yes/no grammatical questions.
3. **Editorial review** — human adjudicates conflicts between proposal and constraint violations; produces final rendering.

These stages differ in cost profile, auditability, discipline requirements, and failure modes — distinctions that matter for system design and that the four-plane model alone does not surface.

For the substantive description of the three stages, the bidirectional test, the coarse-anchor principle, the two-phase processing model, and the meta-discipline layer, see [`toolset-architecture.md`](toolset-architecture.md).

The two documents are complementary: `architecture.md` (this file) is normative for where code and data live; `toolset-architecture.md` is normative for which task type each tool is fit for.

---

## Drift prevention

The four-plane architecture is durable only if drift is controlled:

1. **Constraint specifications live in the canon, not the audit-stage implementation.** When a constraint changes, the canon is the source of truth; the implementation is updated to match. `canon-validator-alignment-protocol.md` provides the mechanical alignment check.

2. **Framework material lives in atu-method/docs/, not in per-repo canons.** Per-repo canons reference framework sections by stable path. They do **not** duplicate framework prose.

3. **Discipline memories live in atu-method/memories/, not in per-repo canons.** Per-repo canons reference memories by name. They do not restate the memory's content.

4. **Cross-project consistency is enforced by the four-plane assignment.** If a piece of content is "shared" it goes in atu-method; if "per-repo" it stays in the respective reader. Mixed ownership (same content in two places) is the failure mode that produces drift.

Plain operational language (constraints, canon, build pipeline, swap system) is preferred over architectural jargon in day-to-day work. Architectural terminology (data plane, specification plane, tooling plane, delivery plane) is reserved for system-design conversations and this document.
