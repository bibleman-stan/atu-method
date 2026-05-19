# atu-method/docs — Index

Top-level index for the atu-method documentation. Each doc has a distinct purpose; consult by purpose.

Companion: [`../memories/_index.md`](../memories/_index.md) indexes cross-corpus discipline memories.

---

## Methodology specification

- [`framework.md`](framework.md) — **The canonical methodology specification.** Bidirectional test, mechanical-first architecture, v0→v3 pipeline, validation status across four genres. Authoritative cross-corpus body. Read first.
- [`apparatus.md`](apparatus.md) — **Scope statement.** What the apparatus is and what it produces. The KJV-anchored English layer (a separate concern from ATU segmentation). Cross-sibling end-state UX description.
- [`toolset-architecture.md`](toolset-architecture.md) — **Pipeline implementation per stage.** Per-corpus parse layers, v1.5 binding-rule application, optional v2 LLM adjudication, v3 editorial review. Reference to the pilot scripts at `readers-tanakh/research/atu-pilot-mechanical-first/`.
- [`architecture.md`](architecture.md) — **Four-plane technical architecture** (data / specification / tooling / delivery). Plane ownership: shared vs per-repo. Interface contracts.
- [`glossary.md`](glossary.md) — **Universal term definitions.** ATU, bidirectional test, binding rule, BHSA clause-atom, etc.

## Per-language binding-rule catalogs

- [`binding-rules-hebrew.md`](binding-rules-hebrew.md) — **The 14 validated Hebrew binding rules** (B1-B14 with B4 retired). Each rule: trigger, justification, example, counter-example. Evaluation order and global same-verse guard.
- Greek catalog — TODO (pending GNT pilot)
- EME English catalog — TODO (pending BoFM pilot)
- Latin catalog — TODO (pending LXX/Vulgate consideration)

## Position documents

- [`methodology-position.md`](methodology-position.md) — **Relationship to LDHB / discourse-grammar references.** "Lexham-consulted but not utilized" framing. Why the apparatus does not depend on LDHB at runtime.

## Per-repo discipline

- [`retraction-log-protocol.md`](retraction-log-protocol.md) — Per-repo retraction-log specification. File format, 3-strike promotion threshold, what counts as a retraction.

## Legacy reference

- [`_old/`](_old/) — Prior versions of all docs. Not authoritative. The 2026-05-18 mechanical-first rewrite is preserved under `_old/2026-05-18-mechanical-first-rewrite/`.

---

## What got retired in the 2026-05-18 mechanical-first rewrite

The following were tied to the legacy Stage 1 / Stage 2 / Stage 3 LLM-primary architecture with a 26-entry constraint catalog. Replaced by the mechanical-first pipeline + 14-rule binding catalog:

- `change-protocol.md` — replaced by `framework.md` §7 (shorter, scoped to binding-rule changes)
- `canon-validator-alignment-protocol.md` — no longer needed; binding rules ARE the canon
- `editorial-review-protocol.md` — replaced by the pilot's v3 comparison framework
- `rule-template.md` — replaced by `binding-rules-hebrew.md` format
- `rule-equivalence-map.md` — TODO when Greek/EME/Latin catalogs land
- `prompts/` — Stage 1 LLM rubrics; optional v2 may resurrect a narrow-task variant later
