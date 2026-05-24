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
│   • Binding-rule catalog — per-repo, language-specific           │
│   • (optional) v2 adjudication prompts — per-repo, narrow-task   │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│ TOOLING PLANE                                                    │
│   • Source-text anchoring (Macula, TAHOT, Strong's, Skousen)     │
│   • Parse adapters (BHSA / Macula-lowfat / CoNLL-U)             │
│   • v1.5 binding-rule engine (feature-driven ATU grouping)       │
│   • Optional v2 LLM adjudication (narrow-task, on residuals)     │
│   • v3 editorial review surface                                  │
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
  plane against the data plane. Lives in atu-method/docs/framework.md §7
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
| Binding-rule catalog | (template + cross-corpus map) | ✓ (language-specific rules) |
| v2 adjudication prompts (optional) | (cross-corpus template) | ✓ (per-language, narrow-task) |
| Parse adapters | ✓ | (consumed) |
| v1.5 binding-rule engine | ✓ (orchestration) | ✓ (rule implementations) |
| v2 LLM adjudication (optional) | ✓ (orchestration) | ✓ (per-language adjudication calls) |
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

The specification plane describes the editorial methodology and binding-rule catalog; it does not consume data directly. Cross-references from spec to data (e.g., "canonical case: Alma 12:26") are illustrative, not load-bearing.

### Specification plane → Tooling plane

The v1.5 binding-rule engine in the tooling plane consumes the binding-rule catalog from the specification plane. The interface is:

- **Trigger** — the parse-derived feature condition (clause type, head lemma, relation, text prefix) under which a binding rule fires (per-rule field in the catalog entry).
- **Closed lists** — Named lemma / category sets cross-referenced from rule entries. The engine loads these at start.
- **Evaluation order + same-verse guard** — Per-repo catalog section defining rule precedence and the within-verse binding boundary.

Drift between a binding rule as documented in the canon and its `should_bind()` implementation is a **failure** — detected by the per-repo validator baseline-check (the binding rules ARE the canon; cf. `framework.md` §7).

### Data plane ↔ Tooling plane

- **v1 parse extraction reads** the source text + parse layer; emits parse-derived clause units.
- **v1.5 binding-rule engine reads** the clause units; emits ATU candidate groups (a publishable draft on its own).
- **v2 LLM adjudication (optional)** reads a residual clause-group + context; emits a yes/no verdict for that group only.
- **Editorial review (v3)** consumes the mechanical output + any v2 verdicts; writes to the rendered corpus via TxLog with rollback support.
- **Build pipeline** (delivery plane) reads the rendered corpus and produces HTML fragments.

### Workflow ↔ all planes

The audit-then-apply discipline operates across planes. It governs:

- When canon changes (specification plane) require audit-evidence in commit messages.
- When constraint audit outputs (tooling plane) are application-ready vs. require manual review.
- When data-plane mutations require baseline-check before commit.

See [`framework.md`](framework.md) §7 for the operational workflow (change discipline scoped to binding-rule changes).

---

## Internal structure of the Tooling plane — cognitive-labor partitioning

The four-plane model carves by **where things live** (data / spec / tooling / delivery). It does not by itself describe the internal task-type structure of the Tooling plane. A complementary view is needed: **what kind of cognitive work each tool does**.

The Tooling plane subdivides into the mechanical-first pipeline stages, each fit for a different task type:

1. **v1 — parse extraction** — reads the per-corpus parse layer (BHSA clause-atoms / Macula clause nodes / CoNLL-U sentences) into parse-derived clause units with their linguistic features. Deterministic.
2. **v1.5 — binding rules** — feature-driven binding rules merge the v1 clause units into ATU candidate groups. Mechanical execution; each rule grounded in the bidirectional test, firing on parse-derived features. This is the primary segmenter — it produces a publishable draft on its own.
3. **v2 — optional LLM adjudication** — for the narrow residual cases the mechanical layer cannot decide, per-group LLM calls answer a single yes/no question (3 passes, agreement-scored). OPTIONAL and narrow; the LLM does NOT do chapter-level rendering.
4. **v3 — editorial review** — human adjudicates between the mechanical output and any v2 verdicts, plus flagged-uncertain cases; produces the final rendering.

These stages differ in cost profile, auditability, discipline requirements, and failure modes — distinctions that matter for system design and that the four-plane model alone does not surface.

> **Note (2026-05-18 reconciliation):** a short-lived 2026-05-17 design made Stage 1 an *LLM-primary* identifier (LLM proposes the whole rendering; a constraint catalog audits it). That was retired the next day in favor of the mechanical-first pipeline above (see `_index.md` and `framework.md` §3). The LLM is now an *optional, narrow-task adjudicator on residuals*, not the primary identifier.

For the substantive description of the stages, the bidirectional test, and the binding-rule catalog, see [`framework.md`](framework.md) §3 and [`toolset-architecture.md`](toolset-architecture.md).

The two documents are complementary: `architecture.md` (this file) is normative for where code and data live; `toolset-architecture.md` is normative for which task type each tool is fit for.

---

## Drift prevention

The four-plane architecture is durable only if drift is controlled:

1. **Binding rules live in the canon, not in a separate audit-stage implementation** (the binding rules ARE the canon). When a rule changes, the canon catalog is the source of truth; the `should_bind()` implementation is updated to match, and the per-repo validator baseline-check provides the mechanical alignment check.

2. **Framework material lives in atu-method/docs/, not in per-repo canons.** Per-repo canons reference framework sections by stable path. They do **not** duplicate framework prose.

3. **Discipline memories live in atu-method/memories/, not in per-repo canons.** Per-repo canons reference memories by name. They do not restate the memory's content.

4. **Cross-project consistency is enforced by the four-plane assignment.** If a piece of content is "shared" it goes in atu-method; if "per-repo" it stays in the respective reader. Mixed ownership (same content in two places) is the failure mode that produces drift.

Plain operational language (constraints, canon, build pipeline, swap system) is preferred over architectural jargon in day-to-day work. Architectural terminology (data plane, specification plane, tooling plane, delivery plane) is reserved for system-design conversations and this document.
