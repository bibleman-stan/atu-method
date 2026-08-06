# atu-method/docs — Index

Top-level index for the atu-method documentation. Each doc has a distinct purpose; consult by purpose.

Companion: [`../memories/_index.md`](00-start-here.md) indexes cross-corpus discipline memories.

---

## Deployment state of record (read before asserting what's live)

- [`deployment-status.md`](05-status/deployment-status.md) — **THE single source of truth for what is LIVE per reader edition** (which layer is deployed, on what method, anchoring commits; the source-text-sacred vs segmentation-regenerable distinction). Per-repo `CLAUDE.md`/READMEs drift stale and must NOT be trusted over this file.

## Doctrine (read with framework.md)

- [`substrate.md`](03-implementation/substrate.md) — **The Textual Fabric Doctrine (substrate before superstructure).** Established 2026-05-27. The framework is a Container, not an Originator; fabric quality bounds the claims. The **mechanical ceiling** (judgment-residuals — complement-vs-quote, parallel-cola — are not rule-decidable over a weak parse → use better substrate or v2 LLM-adjudication). Fabric-parity tiers per corpus, the GIGO guardrail, the hybrid annotation pipeline, the new-corpus START gate. BoFM is the worked example (v2-adjudication chosen).

## Methodology specification

- [`framework.md`](01-normative/framework.md) — **The canonical methodology specification.** Bidirectional test, mechanical-first architecture, v0→v3 pipeline, validation status across four genres. Authoritative cross-corpus body. Read first.
- [`cross-corpus-principles.md`](01-normative/cross-corpus-principles.md) — **Cross-corpus universal principles companion.** Candidate-ATU substrate (§1.1), structural justifications J1/J2/J4/J5, merge-overrides M1/M4, application order (§1.8), N=2 Adjudication + N=3+ cliff (§1.9), rhetoric-figures-constrain (§1.3a). NOT break-licensors (those live at `[framework.md §2.1](<01-normative/framework.md#§2.1 The bidirectional test (primary criterion)>)`/§2.2); this is the methodology layer above per-corpus rule catalogs.
- [`apparatus.md`](03-implementation/apparatus.md) — **Scope statement.** What the apparatus is and what it produces. The KJV-anchored English layer (a separate concern from ATU segmentation). Cross-sibling end-state UX description.
- [`toolset-architecture.md`](03-implementation/toolset-architecture.md) — **Pipeline implementation per stage.** Per-corpus parse layers, v1.5 binding-rule application, optional v2 LLM adjudication, v3 editorial review. Reference to the pilot scripts at `readers-tanakh/research/atu-pilot-mechanical-first/`.
- [`architecture.md`](03-implementation/architecture.md) — **Four-plane technical architecture** (data / specification / tooling / delivery). Plane ownership: shared vs per-repo. Interface contracts.
- [`glossary.md`](01-normative/glossary.md) — **Universal term definitions.** ATU, bidirectional test, binding rule, BHSA clause-atom, etc.

- [`../canon-index.md`](../canon-index.md) — **Canon-anchor navigation index.** One row per §-anchor / sub-clause / concept / doc; status (live/archived/superseded/CONTESTED/phantom) + live-successor + ALL consumers + (for in-flight migrations) proposed_disposition. Hand-built first generation; future regeneration via `build_canon_index.py`. Use to find "where does §X.Y live + who cites it."

## Per-language binding-rule catalogs

- [`binding-rules-hebrew.md`](02-registries/binding-rules-hebrew.md) — **The 14 validated Hebrew binding rules** (B1-B14 with B4 retired). Each rule: trigger, justification, example, counter-example. Evaluation order and global same-verse guard.
- [`binding-rules-lxx.md`](02-registries/binding-rules-lxx.md) — **LXX-Greek catalog** (parked smoke-test artifact, 2026-05-27; integration target is the projection-v1 generator not yet wired live). GNT catalog still TODO (pending GNT pilot).
- EME English catalog — TODO (pending BoFM pilot)
- Latin catalog — TODO (pending LXX/Vulgate consideration)

## Position documents

- [`methodology-position.md`](05-status/methodology-position.md) — **Relationship to LDHB / discourse-grammar references.** "Lexham-consulted but not utilized" framing. Why the apparatus does not depend on LDHB at runtime.

## Per-repo discipline

- [`retraction-log-protocol.md`](04-process/retraction-log-protocol.md) — Per-repo retraction-log specification. File format, 3-strike promotion threshold, what counts as a retraction.

## Legacy reference

- [`_old/`](_old/) — Prior versions of all docs. Not authoritative. The 2026-05-18 mechanical-first rewrite is preserved under `_old/2026-05-18-mechanical-first-rewrite/`.

---

## What got retired in the 2026-05-18 mechanical-first rewrite

The following were tied to the legacy Stage 1 / Stage 2 / Stage 3 LLM-primary architecture with a 26-entry constraint catalog. Replaced by the mechanical-first pipeline + 14-rule binding catalog:

- `change-protocol.md` — replaced by [`framework.md` §7](<01-normative/framework.md#§7 Change discipline>) (shorter, scoped to binding-rule changes)
- `canon-validator-alignment-protocol.md` — no longer needed; binding rules ARE the canon
- `editorial-review-protocol.md` — replaced by the pilot's v3 comparison framework
- `rule-template.md` — replaced by [`binding-rules-hebrew.md`](02-registries/binding-rules-hebrew.md) format
- `rule-equivalence-map.md` — TODO when Greek/EME/Latin catalogs land
- `prompts/` — Stage 1 LLM rubrics; optional v2 may resurrect a narrow-task variant later
