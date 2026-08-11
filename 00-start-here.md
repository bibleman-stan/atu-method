# Start here — the atu-method vault map

**This is the front door.** Everything in the repo is reachable from here in one or two clicks. Organised by *what you are trying to do*, not by where the files happen to sit.

> **If you are opening this to see where things stand, go to [[Current-Tasks.md]].** That is the in-flight board. This file is the map; that one is the state.

---

## The two files that answer "what now?"

| | |
|---|---|
| [[Current-Tasks.md]] | **What is in flight**, organised by what unblocks it: waiting on you / ruled-but-gated / mine / known-broken. |
| [[Pending-Decisions.md]] | **What needs your ruling**, one entry per decision with a recommendation, why that one, and its cons. |

---

## 1-method — the canon

The normative layer. Everything else is downstream of these.

- [[1-method/framework.md|framework.md]] — **the canonical methodology specification.** The bidirectional test (§2.1), the explicit-marker license (§2.2), mechanical-first architecture, the v0→v3 pipeline, and the §7 change discipline that governs edits to itself. **Read first.**
- [[1-method/cross-corpus-principles.md|cross-corpus-principles.md]] — the universal-principles companion. Candidate-ATU substrate, structural justifications J1/J2/J4/J5, merge-overrides M1/M4, application order, the N=2/N=3+ cliff, and the rhetoric-figures-constrain firewall. *Not* a break-licensor — those live in framework §2.1/§2.2.
- [[1-method/binding-rules-hebrew.md|binding-rules-hebrew.md]] — the 14 validated Hebrew rules (B1–B14, B4 retired). Trigger, justification, example, counter-example, evaluation order.
- [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]] — LXX-Greek catalog. **PARKED** (2026-05-27 smoke-test artifact; not wired live).
- [[1-method/glossary.md|glossary.md]] — universal term definitions. ATU, bidirectional test, binding rule, clause-atom.

*Still to be written: EME English catalog (pending BoFM pilot), Latin catalog.*

## 2-evidence — what we have actually measured

Findings live here, filed in the same turn they are produced (standing default #5(c)).

- [[2-evidence/deployment-status.md|deployment-status.md]] — **the single source of truth for what is LIVE per reader edition.** Per-repo CLAUDE.mds and READMEs drift; this file does not. Never assert deployment state from anything else.
- [[2-evidence/framework-claim-inventory.md|framework-claim-inventory.md]] — all 37 framework assertions typed as OURS / SOURCED / CONVERGENT / MEASURED / UNPROVEN / TUNED. The hinge claim — that grammatical closure proxies for thought — is currently unsupported.
- [[2-evidence/finding-isaiah-cross-corpus-divergence.md|finding-isaiah-cross-corpus-divergence.md]] — the same Isaiah, two of our editions, 34% apart. Hebrew breaks more often on identical content; BoFM is coarser in 13 of the 14 verses that differ.
- [[2-evidence/finding-substrate-loop-diagnosis.md|finding-substrate-loop-diagnosis.md]] — the substrate loop is missing a *filter*, not an instrument. The Isaiah gold oracle exists, produced F1 0.561, and has been idle 73 days behind one unbuilt component.
- [[2-evidence/finding-requirements-phase-hole.md|finding-requirements-phase-hole.md]] — the data plane has no gold and the SDLC has no requirements phase; these are one hole, not two. Why validators measure conformance while nothing measures correctness. Three axes — plane, audience, phase — and how they stack.
- [[2-evidence/traceability-tanakh.md|traceability-tanakh.md]] — theory → rule → validator, one row per constraint. 26 constraints all carrying a Joüon/Waltke-O'Connor source; 17 with a validator; 14 validators with no constraint at all. Generated; grounding judgments curated in `traceability-grounding.json`.
- [[2-evidence/reader-observations.md|reader-observations.md]] — Loop 6 capture channel. Your observations against verse references, so n=1 can become n=many.
- [[2-evidence/PROJECT-BRIEF-2026-08-08.md|PROJECT-BRIEF-2026-08-08.md]] — dense machine-facing system brief with provenance tags. Written for another Claude to consume, not for reading.
- [`2-evidence/scholarship/`](2-evidence/scholarship/) — the external literature, indexed at [`scholarship/_index.md`](2-evidence/scholarship/_index.md), with per-corpus subfolders (`bofm/`, `gnt/`, `methodology/`).

## 3-implementation — how it is actually built

- [[3-implementation/substrate.md|substrate.md]] — **the Textual Fabric Doctrine.** Substrate before superstructure; the framework is a Container, not an Originator; fabric quality bounds the claims. The mechanical ceiling and the three past-ceiling levers, fabric-parity tiers per corpus, the GIGO guardrail, the new-corpus START gate.
- [[3-implementation/toolset-architecture.md|toolset-architecture.md]] — pipeline implementation per stage: parse layers, v1.5 binding-rule application, optional v2 LLM adjudication, v3 editorial review.
- [[3-implementation/architecture.md|architecture.md]] — the four-plane technical architecture (data / specification / tooling / delivery) and which plane is shared vs per-repo.
- [[3-implementation/apparatus.md|apparatus.md]] — scope statement: what the apparatus is, what it produces, and the KJV-anchored English layer as a concern separate from ATU segmentation.

## 4-process — how the work governs itself

- [[4-process/improvement-loops.md|improvement-loops.md]] — **the six loops and their measured status.** Four of six are reported broken. Read this before proposing process changes.
- [[4-process/collapsed-maturation-loops.md|collapsed-maturation-loops.md]] — **PROPOSAL.** What the topology looks like with two conversation partners instead of four, drawn loop by loop with what is lost and how to hold it down.
- [[4-process/retraction-log-protocol.md|retraction-log-protocol.md]] — per-repo retraction-log spec: format, the 3-strike promotion threshold, what counts as a retraction.
- [[4-process/draft-promotions-2026-08-07.md|draft-promotions-2026-08-07.md]] — the two drafted promotions (**both denied**), the corrected count, and the protocol defect that fell out of it.
- [[4-process/proposal-2026-08-06-criterion-reconstruction.md|proposal-2026-08-06-criterion-reconstruction.md]] — the §2.1 reconstruction; six allowances tested for derivability. Governs the non-finite-predication ruling.
- [[4-process/methodology-position.md|methodology-position.md]] — relationship to LDHB and discourse-grammar references. Why the apparatus does not depend on LDHB at runtime.

## Navigation and memory

- [[canon-index.md]] — **one row per §-anchor / concept / doc**, with status (live / archived / superseded / CONTESTED / phantom), live-successor, and every consumer. Use it to answer "where does §X.Y live, and who cites it?"
- [[canon-index-receipts.md]] — the raw grep/Read output backing every claim in the index.
- [`memories/`](memories/) — 36 cross-corpus methodology memories, indexed at [`memories/_index.md`](memories/_index.md).
- [`memories/operational/`](memories/operational/) — 70 operational memories: north-star, deferred queue, named arcs, feedback disciplines. **Recovered 2026-08-06** from a deleted namespace; state as of 2026-06-15, so treat entries as possibly stale until re-verified.
- [[CLAUDE.md]] — my operating instructions for this repo: standing behavioral defaults, closed routes, mandatory orientation reads.
- [`README.md`](README.md) · [[CHANGELOG.md]] — repo overview and change history. (`README.md` is a markdown link, not a wikilink: three files share that basename, so a wikilink cannot resolve it.)

## Tooling

Scripts live in [`5-machinery/scripts/`](5-machinery/scripts/). The ones that matter to you:

| Script | What it does |
|---|---|
| `loop_health.py` | Mechanical staleness check across every loop. Runs on session start; warns, never blocks. |
| `check_broken_pointers.py` | Pointer integrity — broken doc paths, broken anchors, broken wikilinks. |
| `add_wikilinks.py` | Turns unlinked `doc.md §N` mentions into clickable wikilinks. Idempotent; dry-run by default. |

Skills live in [`.claude/skills/`](.claude/skills/) — `atu-audit-tier`, `atu-compaction-resume`, `jsonl`. **Project skills belong in this folder**, never the global bucket, so they travel with the repo.

---

## Retired — kept as receipts, not authoritative

[`_old/`](_old/) holds prior versions of every doc, including the 2026-05-18 mechanical-first rewrite under `_old/2026-05-18-mechanical-first-rewrite/`.

Retired in that rewrite, and **deliberately not linked** because they are no longer in the vault: `change-protocol.md` (replaced by framework §7), `canon-validator-alignment-protocol.md` (binding rules *are* the canon), `editorial-review-protocol.md`, `rule-template.md`, `rule-equivalence-map.md`, and the Stage-1 `prompts/`. If you see one of these cited in prose, it is a historical reference, not a live pointer.
