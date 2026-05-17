# atu-method/docs — Index

Top-level index for the atu-method documentation. Each doc has a distinct operational purpose. Per-repo Claudes consult by purpose, not by browsing all docs every wake.

Companion: [`../memories/_index.md`](../memories/_index.md) indexes the cross-corpus discipline memories. Together, `docs/` (methodology + protocols) and `memories/` (discipline lessons) form the shared cross-corpus knowledge surface for the reader-repo family.

---

## Methodology specification (read for any rule-design or interpretive work)

- [`framework.md`](framework.md) — **The canonical methodology specification.** Bidirectional test, three-stage pipeline (LLM identification → constraint catalog audit → editorial review), per-corpus instantiation pattern. Authoritative cross-corpus body. Per-repo canon is pointer-only to this document. Read for any rule-design or methodology question.
- [`apparatus.md`](apparatus.md) — **Scope statement.** What the apparatus is and is NOT. The mission, the deliberate exclusions ("the apparatus does NOT produce typography / reveal rhetorical parallelism / prescribe oral delivery / adjudicate textual variants"). Read for scope questions or when audit-bandwagon-resistance is in play.
- [`architecture.md`](architecture.md) — **Four-plane technical architecture** (data / specification / tooling / delivery). Plane ownership: shared vs per-repo. Interface contracts. Read for cross-sibling architectural work. Cross-links to `toolset-architecture.md` for task-type structure within the tooling plane.
- [`toolset-architecture.md`](toolset-architecture.md) — **Cognitive-labor partitioning across the toolset.** Three stages: LLM identification (minimal rubric), constraint catalog audit (syntactic yes/no questions), editorial review. Includes the bidirectional test, the coarse-anchor principle, the two-phase processing model, and the meta-discipline layer. Read for toolset-design questions, cross-corpus port planning, or methodology-paper context.
- [`glossary.md`](glossary.md) — **Universal term definitions.** ATU, bidirectional test, minimal rubric, constraint catalog, three-stage pipeline, etc. Project-specific glossaries live in each per-repo canon. Read when a term is ambiguous.

## Per-rule discipline (read when writing or auditing constraint catalog entries)

- [`rule-template.md`](rule-template.md) — **Operational template for constraint-catalog entries.** Field structure (Status / Category / Decidability / Encoded-question / Verdict-family / Source-reference / Diagnostic-examples / Edge-cases / Scope / Precedence / Implementation). Constraint-style framing (yes/no grammatical questions); producer-style framing is forbidden. Read before writing a new catalog entry or migrating an existing one.
- [`rule-equivalence-map.md`](rule-equivalence-map.md) — **Cross-corpus constraint families + corpus-unique non-correspondences.** Catalogue of which constraints across Hebrew / Greek / EME English / Latin catalogs encode the same underlying grammatical phenomenon (e.g., restrictive relative binding, gapped-verb tolerance) and which have no cross-corpus analog. Read before cross-corpus catalog-design decisions or new-corpus porting.

## Change and audit protocols (read for canon-touching work)

- [`change-protocol.md`](change-protocol.md) — **Canon-change discipline.** Framework authority, proposal requirements, the 12 mandatory-audit triggers, audit-skippable categories, audit-evidence in commit messages, self-test before commit, proposed-rule adoption protocol. Read before any canon change.
- [`retraction-log-protocol.md`](retraction-log-protocol.md) — **Per-repo retraction-log specification.** File format, 3-strike promotion threshold, what counts as a retraction, cross-corpus propagation. Read when logging a retraction or running the threshold-promotion check.
- [`canon-validator-alignment-protocol.md`](canon-validator-alignment-protocol.md) — **Structural alignment check specification.** What per-repo `validators/canon/check_canon_alignment.py` scripts implement: validator file presence, closed-list presence, encoded-question field consistency, multi-valued field branches. Verdict taxonomy: ALIGNED / NO_IMPL / DRIFT / PARTIAL / EDITORIAL_ACK. Read when implementing the per-repo script or running the alignment check.

## Legacy reference

- [`_old/`](_old/) — Prior versions of all docs, preserved for consultation. Not authoritative. The current docs in `docs/` root are the methodology.

---

## How to use this index

A fresh Claude orientation cascade:

1. Read this `_index.md` once to know what's available
2. Read the per-repo `CLAUDE.md` for repo-specific operational context
3. Consult specific docs ON TRIGGER per their stated purpose — not pre-emptively

The orthogonal `memories/_index.md` covers discipline lessons (Claude-default anti-patterns, operational discipline, dispatch and scaling discipline, session management). Both indexes together are the entry point; individual docs and memories are read on-demand when their stated purpose fires.

## Updates to this index

When a new document is added to `atu-method/docs/`, add a one-line entry here in the appropriate category. Per `change-protocol.md`, substantial new docs that shape how the apparatus is operated require the same audit scrutiny as canon changes. A pure-navigation index update (this file) is audit-skippable.
