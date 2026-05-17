# atu-method/docs — Index

Top-level index for the atu-method documentation. Each doc has a distinct operational purpose. Per-repo Claudes should consult by purpose, not browse all docs every wake.

Companion: [`../memories/_index.md`](../memories/_index.md) indexes the cross-corpus discipline memories. Together, `docs/` (methodology + protocols) and `memories/` (discipline lessons) form the shared cross-corpus knowledge surface for the reader-repo family.

---

## Methodology specification (read for any rule-design or interpretive work)

- [`framework.md`](framework.md) — **The canonical methodology specification.** Generative principle, syntactic vetoes, merge-overrides, structural justifications, bidirectional atomic-thought test, three-layer architecture. Authoritative cross-corpus body. Per-repo canon §0/§1/§2 are pointer-only to this document. Read for any rule-design or methodology question.
- [`apparatus.md`](apparatus.md) — **Scope statement** — what the apparatus is and is NOT. The mission, the deliberate exclusions ("the apparatus does NOT produce typography / reveal rhetorical parallelism / prescribe oral delivery / adjudicate textual variants"). Read for picture-shaped scope questions or when audit-bandwagon-resistance is in play.
- [`architecture.md`](architecture.md) — **Four-plane technical architecture** (data / specification / tooling / delivery, with workflow orthogonal). Plane ownership: shared vs per-repo. Interface contracts. Read for cross-sibling architectural work or when the picture matters more than the procedural phase list. Cross-links to `toolset-architecture.md` for the task-type structure within the Tooling plane.
- [`toolset-architecture.md`](toolset-architecture.md) — **Cognitive-labor partitioning across the toolset** (four legs: mechanical floor / point-rule validators / LLM resolver / LLM passage-level audit, plus meta-discipline). Complements `architecture.md` along an orthogonal axis: where `architecture.md` describes where things live, this describes which task type each tool is fit for. Includes the extended bidirectional test (with cognitive-unity gate for parallel poetry), the coarse-anchor principle, and the two-phase candidate-vs-adjudication processing model. Read for cross-corpus toolset-design questions, LXX/Vulgate spin-up planning, or methodology-paper context.
- [`glossary.md`](glossary.md) — **Universal term definitions.** ATU, M1–M4, J1–J5, N=2 adjudication, Helaman 3:16 cliff, etc. Project-specific glossaries (AICTP for BoFM, te'amim for Tanakh, periphrastic for GNT) live in each per-repo canon. Read when a term is ambiguous.

## Per-rule discipline (read when writing or auditing §5 entries)

- [`rule-template.md`](rule-template.md) — **Operational template for every §5 rule entry.** MISRA-style fields (Status / Category / Decidability / Layer / Rule / UD signature / Closed lists / Scope / Exclusions / Precedence / Examples / Implementation). Includes the universal-shape vs per-corpus-vocabulary scope statement, status semantics, category semantics (A/B/C), decidability semantics, standard action codes, multi-valued field conventions, and forbidden-content list. Read before writing a new §5 entry or migrating an existing one.
- [`rule-equivalence-map.md`](rule-equivalence-map.md) — **Cross-corpus rule families + corpus-unique non-correspondences.** Catalogue of which rules across BoFM / GNT / Tanakh canons do the same underlying work (e.g., complement integrity instantiated as R17 / R10 / H7) and which rules have no cross-corpus analog (AICTP, genitive absolute, verbless clauses, etc.). Read before cross-corpus rule-design decisions, LXX/Vulgate porting questions, or framework-family discussions.

## Change and audit protocols (read for canon-touching work)

- [`change-protocol.md`](change-protocol.md) — **Canon-change discipline.** §7.1 framework authority. §7.2 proposal requirements. §7.3 12 mandatory-audit triggers. §7.4 audit-skippable categories. §7.5 audit-evidence in commit messages. §7.6 self-test before commit. §7.7 self-consistency audit trigger. §7.8 proposed-rule adoption protocol. Read before any canon change.
- [`retraction-log-protocol.md`](retraction-log-protocol.md) — **Per-repo retraction-log specification.** File format, 3-strike promotion threshold, what counts as a retraction, cross-corpus propagation. Bounds discipline-codification latency by catching recurring anti-default sub-patterns at the 3rd occurrence rather than the 5th-or-later. Read when logging a retraction or running the threshold-promotion check.
- [`canon-validator-alignment-protocol.md`](canon-validator-alignment-protocol.md) — **Structural alignment check specification.** What per-repo `validators/canon/check_canon_alignment.py` scripts must implement: validator file presence, closed-list presence in source, UD signature field consistency, multi-valued field branches. Verdict taxonomy: ALIGNED / NO_IMPL / DRIFT / PARTIAL / EDITORIAL_ACK. Read when implementing the per-repo script or running the alignment check.

---

## How to use this index

A fresh Claude orientation cascade should:

1. Read this `_index.md` once to know what's available
2. Read the per-repo `CLAUDE.md` for repo-specific operational context
3. Consult specific docs above ON TRIGGER per their stated purpose — not pre-emptively

The orthogonal `memories/_index.md` covers discipline lessons (Claude-default anti-patterns, operational discipline, dispatch and scaling discipline, session management). Both indexes together are the entry point; individual docs and memories are read on-demand when their stated purpose fires.

## Updates to this index

When a new document is added to `atu-method/docs/`, add a one-line entry here in the appropriate category. Per `change-protocol.md` §7.3 trigger #10 (discipline-shifting additions), substantial new docs that shape how the apparatus is operated require the same audit scrutiny as canon changes. A pure-navigation index update (this file) is audit-skippable per §7.4.
