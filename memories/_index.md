# Discipline Memories — Index

This directory holds **cross-project discipline lessons** learned during the development of the ATU apparatus. Each memory captures a pattern of failure or success that has crossed multiple sessions and multiple projects (readers-bofm, readers-gnt, readers-tanakh).

Memories live here (shared across all atu-method consumers) rather than in per-repo canons because the lessons are universal: they apply to any project applying the apparatus to any corpus.

Per-repo canons reference memories by filename (e.g., "per `feedback_rhetoric_bandwagon`"); they do **not** restate the memory's content.

---

**Status: SCAFFOLD** — to be populated by extraction from `~/.claude/projects/c--Users-bibleman-repos-readers-bofm/memory/` (the 17 captured feedback memories accumulated during BoFM development).

Initial memory list (filenames will match those in the original memory directory):

## Methodology discipline

- `feedback_sense_line_mission.md` — atomic thought trumps poetic structure; we expose sense-lines, not parallels; Parry is a separate layer.
- `feedback_goldilocks_refinement.md` — container-not-originator merge applies to subordinating syntax only; coordinate/parallel members each get their own atomic beat.
- `feedback_rhetorical_force.md` — rhetorical impact alone never justifies a split; criterion 1 (own thought?) is the test.
- `feedback_rhetoric_bandwagon.md` — resist wholesale adoption of external formal frameworks (classical rhetoric, Hebrew parallelism); we are psycholinguistic-grounded, not parallelism-structural.
- `feedback_principle_vs_mechanical_coverage.md` — principle-soundness ≠ mechanical coverage; if validators repeatedly miss a pattern, rule is operationally incomplete.
- `feedback_punctuation_not_evidence.md` — punctuation is inherited overlay, not adjudication evidence.
- `feedback_application_consistency_vs_rule_coverage.md` — consistency is prior to correctness; same-rule-applied-inconsistently is the BoFM-style failure mode.

## Operational discipline

- `feedback_no_fake_dilemmas.md` — when canon's mechanical test resolves a case, apply it; do not route mechanically-resolved cases through "borderline / pending judgment" framings.
- `feedback_no_eyeball_offers.md` — after audit clears a sweep, apply it; do not manufacture "stop and let you eyeball" hedges.
- `feedback_commit_workflow.md` — commit by default in repos with two-role workflow; Stan pushes, agent commits.
- `feedback_decisions_in_chat_not_files.md` — pending.md is for carry-forward state only; decisions go in chat, not deposited in files.
- `feedback_dont_over_engineer_orchestration.md` — three-question check before writing orchestration code: runs outside Claude Code? native equivalent? runbook sufficient?
- `feedback_over_structuring_disposition.md` — stable tendency to add structure the text/canon/code doesn't demand; ask five diagnostic questions before writing new rules or code.
- `feedback_ask_when_directive_is_ambiguous.md` — vague visual directives have multiple valid implementations; ask one direct question before changing code.

## Dispatch / scaling discipline

- `feedback_parallel_horde_default.md` — when work decomposes, dispatch 4–8x the agent count intuition suggests; per-dimension audits, per-cluster sweeps.
- `feedback_scripts_before_agents.md` — before dispatching agents for a corpus sweep, check if grep/sed/regex/Python can do it.
- `feedback_check_existing_tooling.md` — before writing a new scanner/validator, check existing tooling.
- `feedback_agent_sweep_filter.md` — parallel sweep agents return detritus alongside signal; filter each item through level/provenance/redundancy checks before codifying.
- `feedback_sweep_when_introducing_a_window.md` — when adding a flag/window with N readers, gate ALL N at once; same-root-cause symptoms in different paths are not separate bugs.

## Session-management discipline

- `feedback_compaction_is_session_boundary.md` — compaction is a session boundary; execute full CLAUDE.md CHECK-IN protocol on resume.

---

## Memory format

Each memory file is a single Markdown document with:

- **Title** (short statement of the lesson)
- **Trigger context** (what session or pattern produced the lesson)
- **The principle** (one paragraph)
- **Why** (the past incident or strong preference that grounded it)
- **How to apply** (when/where this guidance fires)

Memories are short (~50–100 lines each). They are referenced by filename from per-repo canons and agent prompts.
