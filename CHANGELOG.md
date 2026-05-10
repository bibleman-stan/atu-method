# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] — 2026-05-10

Initial release: repository scaffold + content extraction from the BoFM
proof-of-concept implementation.

### Added — Repository scaffold

- MIT license for code (`LICENSE`); CC-BY-4.0 for documentation (`LICENSE-DOCS`).
- `CITATION.cff` for machine-readable scholarly citation (Citation File Format 1.2.0).
- `pyproject.toml` configuring the `atu_method` Python package with hatchling backend, Python 3.10+, optional dev dependencies (pytest, ruff, mypy).
- Stub Python package structure: `atu_method/{parsing,adapters,infrastructure,hooks,english}/` with `__init__.py` annotations describing each module's intended contents.
- README with project description, architecture summary, repository structure, installation instructions, and attribution block.
- `.gitignore` covering Python artefacts + project-specific patterns.

### Added — Documentation (extracted content)

- `docs/apparatus.md` — High-level system overview (canonical statement of what the apparatus is, what it produces, what it is NOT).
- `docs/architecture.md` — Four-plane architectural decomposition (Data / Specification / Tooling / Delivery) with interface contracts between planes, ownership table (shared vs per-repo), drift prevention principles, and supersession note for the prior "7-layer" framing.
- `docs/rule-template.md` — MISRA-style operational rule-spec template. Required and forbidden fields specified. RFC 2119 normative-language conventions, Status / Category / Decidability semantics. Worked migration checklist.
- `docs/framework.md` — Universal methodology framework extracted from BoFM canon §0/§1/§2/§7. Includes §0 Purpose and Stance (Mission, Method, Pragmatic stance, Scope), §1 Framework (Generative principle, Syntax forbids splits, Image, J1-J5 structural justifications, M1-M4 merge-overrides, Decision procedure, Application order, N=2 Adjudication, Punctuation/Versification not signals, Parallel-List Uniformity, Authorial Asymmetry), §2 Categories A/B/C, §7 Change Protocol (12 mandatory-audit triggers, audit-skippable categories, commit-msg discipline, self-test, proposed-rule adoption protocol). ~440 lines of operational specification.
- `docs/glossary.md` — Universal defined terms (ATU, J1-J5, M1-M4, N=2 adjudication, char-offset, T1.1 pattern, TxLog, UD signature, etc.) plus pointers to per-corpus specific terms.
- `docs/change-protocol.md` — Scaffold for §7 (content currently consolidated in framework.md §7; this file reserved for future expansion if §7 grows beyond the framework doc's scope).

### Added — Memories (extracted)

- 20 cross-project discipline memory files copied from `~/.claude/projects/c--Users-bibleman-repos-readers-bofm/memory/` to `memories/`:
  - Methodology discipline (8): `feedback_sense_line_mission`, `feedback_goldilocks_refinement`, `feedback_rhetorical_force`, `feedback_rhetoric_bandwagon`, `feedback_principle_vs_mechanical_coverage`, `feedback_punctuation_not_evidence`, `feedback_application_consistency_vs_rule_coverage`, `feedback_over_structuring_disposition`.
  - Operational discipline (6): `feedback_no_fake_dilemmas`, `feedback_no_eyeball_offers`, `feedback_commit_workflow`, `feedback_decisions_in_chat_not_files`, `feedback_dont_over_engineer_orchestration`, `feedback_ask_when_directive_is_ambiguous`.
  - Dispatch and scaling (5): `feedback_parallel_horde_default`, `feedback_scripts_before_agents`, `feedback_check_existing_tooling`, `feedback_agent_sweep_filter`, `feedback_sweep_when_introducing_a_window`.
  - Session management (1): `feedback_compaction_is_session_boundary`.
- `memories/_index.md` — Index organized by category with one-line hooks per memory; format spec; project-specific-memory note (project memories remain per-repo).
- Not migrated: `project_book_specific_constructions.md` (BoFM-corpus-specific; remains in readers-bofm session memory).

### Added — Scholarship (PoC structure)

- `scholarship/_index.md` — Scholarship-companion directory organization, audience, file format (Statement / Rationale / Grammatical grounding / Empirical evidence / Intellectual lineage / Adversarial history / Future work).
- `scholarship/bofm/_index.md` — Per-rule companion index for BoFM rules.
- `scholarship/methodology/_index.md` — Universal methodology essays index (planned essays defending framework, categories, precedence, intellectual lineage, audit discipline).
- `scholarship/bofm/R17.md` — Proof-of-concept scholarship companion for R17 Complement Integrity. ~250 lines: Statement, Rationale, Grammatical grounding (CGEL Ch. 11/14/16), Empirical evidence (Phase-1 audit 2026-04-23: 265:10 merged:split ratio for topic-PP; Wave 6 audit 2026-05-10 defects A/B/C), Intellectual lineage (CGEL / Macula-Greek / Vaticanus / sister instantiations in readers-gnt R8 and readers-tanakh H7), Adversarial history (4 audit cycles + doctrinal-weight enumerated-list retirement), Future work.
- `scholarship/bofm/R17-poc-operational.md` — Proposed restructured operational entry for R17 in the MISRA-without-Rationale template. ~55 operational lines down from current ~75 mixed-content. Demonstrates the migration pattern with full template-conformance checklist.

### Not yet added (deferred to subsequent releases)

- `atu_method/` Python infrastructure — to extract from `readers-bofm/validators/` once BoFM canon migration validates the architectural plan.
- Remaining BoFM scholarship companions (~24 more rules: R1, R5, R6, R7, R10, R15, R16, R18, R19, R20, R21, R22, R23, R26, R27, R28 + EP-1/3/4/5 + M1-M4 universal companions).
- Per-rule audit-trail files in `readers-bofm/private/audit-trail/` (parallel to scholarship migration).
- GNT and Tanakh canon migrations to the operational template.
- Methodology essays in `scholarship/methodology/` (framework defense, categories defense, intellectual-lineage essay, audit-discipline essay).
- GitHub remote + Zenodo DOI minting.

### Status

This release establishes the shared mechanical-layer repository with:
- Operational documentation publication-quality for apparatus, architecture, and rule-template.
- Universal framework (§0/§1/§2/§7) extracted to a single source.
- 20 cross-project discipline memories centralized.
- One worked rule (R17) demonstrating the operational/scholarship split for future migration.

The next phase (0.2.0) waits on user review of the R17 PoC to validate the rule-template before committing to a full BoFM canon migration (~25 rules + ~25 scholarship companions + ~25 audit-trail files).
