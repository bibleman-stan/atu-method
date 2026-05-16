# Discipline Memories — Index

This directory holds **cross-project discipline lessons** captured during ATU apparatus development. Each memory is a pattern of failure or success that has been validated across multiple sessions and is generalized beyond any single corpus.

Memories live here (shared across all atu-method consumers) rather than in per-repo canons because the lessons are universal: they apply to any project applying the apparatus to any canonical text.

Per-repo canons reference memories by filename (e.g., "per `feedback_rhetoric_bandwagon`"); they do **not** restate memory content.

Originally accumulated in the readers-bofm session memory directory (`~/.claude/projects/.../memory/`); migrated to this shared location 2026-05-10 as part of the atu-method extraction. Continued discipline lessons learned during ongoing apparatus development should land here.

---

## Methodology discipline

- [`feedback_sense_line_mission.md`](feedback_sense_line_mission.md) — atomic thought trumps poetic structure; the apparatus exposes sense-lines, not rhetorical parallels. Parry / Lowth / Kugel are separate scholarly layers that may overlap with the apparatus but are not its target.
- [`feedback_goldilocks_refinement.md`](feedback_goldilocks_refinement.md) — container-not-originator merge applies to subordinating syntax only; coordinate/parallel members each get their own atomic beat. Run Q1/Q2 diagnostic + adversarial audit before committing merge batches.
- [`feedback_rhetorical_force.md`](feedback_rhetorical_force.md) — rhetorical impact alone never justifies a split. The test is always: own thought? Camera-angle repositioning IS valid; aesthetic force without thought-independence is not.
- [`feedback_rhetoric_bandwagon.md`](feedback_rhetoric_bandwagon.md) — resist wholesale adoption of external formal frameworks (classical rhetoric, Hebrew parallelism theory from Lowth/Watson/Kugel/Berlin/O'Connor). The grounding is psycholinguistic, not parallelism-structural. Adopt specific observations; reject ontological-category imports.
- [`feedback_principle_vs_mechanical_coverage.md`](feedback_principle_vs_mechanical_coverage.md) — principle-soundness ≠ mechanical coverage. If validators repeatedly miss a pattern, "criterion 1 covers it" is not enough — the rule is operationally incomplete until a UD signature is codified.
- [`feedback_punctuation_not_evidence.md`](feedback_punctuation_not_evidence.md) — never use commas, em-dashes, or semicolons as evidence for break/merge. Punctuation is post-canonical editorial overlay. Reasoning must rest on grammar/syntax alone.
- [`feedback_application_consistency_vs_rule_coverage.md`](feedback_application_consistency_vs_rule_coverage.md) — the operate-side twin of over-structuring: failure mode is usually same-rule-applied-inconsistently across instances. Canonical texts' formulaic language is especially vulnerable to sedimented inconsistency; consistency is prior to correctness.
- [`feedback_over_structuring_disposition.md`](feedback_over_structuring_disposition.md) — stable tendency to add structure the text/canon/code doesn't demand. Root cause for rule multiplication, aesthetic reasoning, wavering, default-splitting. ASK the five diagnostic questions BEFORE writing new rules or new code.
- [`feedback_grammar_constrains_not_determines.md`](feedback_grammar_constrains_not_determines.md) — grammar (Layer 1, complement/formula/relative integrity) gives PROHIBITIONS on where ATU breaks CAN'T go, not PRESCRIPTIONS for where they SHOULD go. The generative force is atomic-thought (propositional/psycholinguistic), not grammatical. Closed-list extensions operationalize where the atomic-thought-failure test fires under specific grammatical conditions — they are NOT grammatical-pattern catalogs. Codified at framework §1.2's tail 2026-05-13.
- [`feedback_atu_test_is_bidirectional.md`](feedback_atu_test_is_bidirectional.md) — the atomic-thought test is bidirectional, not just forward. Backward-anaphoric content (deictic demonstratives "these things," unresolved pronouns, discourse-anaphoric particles לָכֵן/עַל־כֵּן/causal כִּי) fails atomic-thought standing alone. Cataphoric reference (presentative הִנֵּה + indefinite NP) does NOT fail. §1.1 test-refinement, not a new §1.5 merge-override. Canonical case: Gen 22:1 — frame + apodosis is one ATU. Codified at framework §1.1 2026-05-13. CRITICAL PRECEDENCE CLARIFICATION (added per gnt-reader sibling lesson): bidirectional is INFORMATIONAL DIAGNOSTIC, not a mechanical PRECEDENCE OVERRIDE. Validators must fire on canon-encoded UD signatures (R/M/EP rules), not on bidirectional-test outcome.
- [`feedback_rhetoric_figures_constrain_atu.md`](feedback_rhetoric_figures_constrain_atu.md) — rhetorical figures (hendiadys, merism, parallelism, chiasm, anaphora, etc.) have DEFAULT ATU dispositions (hendiadys→merge via synonymy-coextension; merism→merge via polar-totality-coextension; parallelism→split each member; chiasm→no force, structural-not-propositional) but never independently DETERMINE ATU boundaries. Each figure CONSTRAINS the candidate space; atomic-thought (per §1.1, bidirectional) determines the answer. Same asymmetry as [[grammar-constrains-not-determines]]. Codified 2026-05-13 from Stan-verbatim "this is a key insight: the interaction of rhetorical devices/figures of speech with ATUs."
- [`feedback_camera_angle_diagnostic_demote.md`](feedback_camera_angle_diagnostic_demote.md) — the "camera-angle shift" diagnostic (framework §1.3) should DROP OUT or be caveated to redundancy with atomic-thought test. Stan-verbatim 2026-05-13: "the more I see it at work, the less confident I am it's helpful." Camera-angle reasoning collapses to either atomic-thought-test paraphrase or aesthetic-bandwagon smuggling; never independently diagnostic. Treat invocations as warning signal. Framework §1.3 + §1.6 edits pending.
- [`feedback_three_anti_default_factors.md`](feedback_three_anti_default_factors.md) — the 7 recurring correction patterns compress to 3 factors plus 1 closed structural blind spot. Factor A: surface-feature pattern-matching substituted for atomic-thought test (patterns 1, 2, 5). Factor B: new-rule reflex over uniform-application (patterns 6, 7). Factor C: sample-size discipline (pattern 4). Compression makes the rule-proposal gates tractable (3 checks instead of 7). Codified 2026-05-16 from the readiness-arc retrospective.
- [`feedback_rule_proposal_gates.md`](feedback_rule_proposal_gates.md) — four-gate checklist run before any rule proposal, closed-list extension, scope claim, or precedence claim. Operationalizes Factors A/B/C plus the bidirectional atomic-thought test as mandatory pre-proposal checks. Catches factor failures before they enter the canon. Cross-references the retraction-log protocol at `atu-method/docs/retraction-log-protocol.md` (the latency-bounding mechanism). Codified 2026-05-16.

## Operational discipline

- [`feedback_directive_protocol.md`](feedback_directive_protocol.md) — per-repo directive queue replaces paste-prompts as default cross-repo coordination. Vault-Claude writes directive files to `directives/pending/`; Stan reviews + triggers per-repo Claudes; per-repo Claudes process in commit order, write replies, move processed directives to archive. Stan retains editorial control at directive-file-review; direct engagement remains available. Codified 2026-05-16.
- [`feedback_no_fake_dilemmas.md`](feedback_no_fake_dilemmas.md) — when the canon's mechanical test resolves a case, apply it. Do NOT route mechanically-resolved cases through "borderline / pending judgment / want me to also" framings. Only genuine canon-gap cases get explicit "rule X doesn't cover Y" framing.
- [`feedback_no_eyeball_offers.md`](feedback_no_eyeball_offers.md) — after audit clears a sweep, apply it. Don't manufacture "stop and let you eyeball" hedges. Specific concerns get specific exemplars, not generic deferral.
- [`feedback_proactive_open_item_examination.md`](feedback_proactive_open_item_examination.md) — every "I held this back because you have to decide" item must be visible (in chat, not deposited in files per `feedback_decisions_in_chat_not_files.md`). As the method matures, periodically re-examine whether held items have become canon/code/precedent-derivable. If yes, surface "I have an answer now" rather than re-defer.
- [`feedback_commit_workflow.md`](feedback_commit_workflow.md) — in two-role workflows (user pushes; agent commits), the generic "never commit unless asked" default is overridden. Don't ask "want me to commit?" after a coherent task.
- [`feedback_decisions_in_chat_not_files.md`](feedback_decisions_in_chat_not_files.md) — session pending files are for carry-forward state only, containing forward-looking items. Transcript / session-notes / decisions narratives are redundant with the JSONL session log. Decisions go in the chat window, not deposited in files.
- [`feedback_dont_over_engineer_orchestration.md`](feedback_dont_over_engineer_orchestration.md) — before writing Python/TS that wraps an SDK, three-question check: runs outside Claude Code? native equivalent? runbook sufficient? Codification ≠ code.
- [`feedback_ask_when_directive_is_ambiguous.md`](feedback_ask_when_directive_is_ambiguous.md) — vague visual directives ("needs a space," "looks ugly," "cleaner") have multiple valid implementations. Ask one direct question before changing code. Multiple-choice options are still guessing. "Everything else was fine" → don't touch surrounding code.

## Dispatch and scaling discipline

- [`feedback_parallel_horde_default.md`](feedback_parallel_horde_default.md) — when work decomposes, dispatch 4-8× the agent count intuition suggests. Per-dimension audits, per-cluster sweeps, pre-spawned next-wave verification.
- [`feedback_scripts_before_agents.md`](feedback_scripts_before_agents.md) — before dispatching agents for a corpus sweep, ask if it can be done with grep/sed/regex/Python. Agents cost seconds and tokens; scripts cost nothing. Agents only when the rule requires per-item judgment the code can't encode.
- [`feedback_check_existing_tooling.md`](feedback_check_existing_tooling.md) — before writing a new scanner/validator, check the existing validator suite, syntax-reference, or a one-line Grep. The validator suite stays focused when extensions go to existing detectors rather than fork to new ones.
- [`feedback_agent_sweep_filter.md`](feedback_agent_sweep_filter.md) — parallel sweep agents return detritus alongside signal. Filter each item through (level / provenance / redundancy) checks before codifying.
- [`feedback_sweep_when_introducing_a_window.md`](feedback_sweep_when_introducing_a_window.md) — when introducing a flag/window with N readers, gate ALL N at once. Same-root-cause symptoms in different code paths are not separate bugs. Third-strike rule.

## Session management discipline

- [`feedback_compaction_is_session_boundary.md`](feedback_compaction_is_session_boundary.md) — when resuming from a compaction summary, still execute the full CLAUDE.md CHECK-IN protocol. Compaction gives context but does not exercise the orientation muscles; silent skip is a check-in failure.
- [`feedback_compaction_resume_protocol.md`](feedback_compaction_resume_protocol.md) — after a compaction event, FIRST action after the mandatory orientation reads is to read the last 20-30 user↔assistant back-and-forth turns from the session JSONL verbatim. Summaries preserve narrative but lose Stan's exact phrasing, minor corrections, tradeoffs weighed. Bluffing continuity from summary-memory alone fails the trust state.
- [`feedback_endstate_first_orientation.md`](feedback_endstate_first_orientation.md) — for multi-phase / cross-corpus / migration work, lead orientation with the user-facing END-STATE picture, NOT the procedural phase list. Procedural-first orientation enables substrate-hunt rabbitholes; picture-first anchors all sub-decisions to the destination. Pull back to picture on ambiguity. (Note: the "add apparatus.md to CHECK-IN" sub-rule is a Claude-derived operationalization, marked explicitly in the memory body.)

---

## Memory format

Each memory file is a single Markdown document with:

- **Title** (short statement of the lesson)
- **Frontmatter** (name / description / type)
- **Body** with:
  - **The principle** (one paragraph stating the rule/discipline)
  - **Why** (the past incident, strong preference, or theoretical basis grounding it)
  - **How to apply** (when/where this guidance fires; concrete operational triggers)

Memories are short (typically 50-100 lines). They are referenced by filename from per-repo canons and agent prompts; their content lives once here.

## Project-specific memories

Some memories are corpus-specific and remain in their respective reader repos. The BoFM project memory `project_book_specific_constructions.md` (per-book EME constructions, ~15 per-book observations) is BoFM-specific and stays in the readers-bofm memory directory. Similar per-project memories may exist in readers-gnt and readers-tanakh; they remain per-repo.

## Updating this directory

When a new cross-project discipline lesson is captured during apparatus development, add it here (not in a per-repo memory directory) IF it generalizes beyond a single corpus. If unsure, default to per-repo memory and promote here once the lesson has demonstrably crossed project boundaries.

Per §7.3 trigger #10 (Discipline-shifting memory file additions), new memories that shape how the apparatus is operated are behaviorally-governing and require the same audit scrutiny as canon. Adding a new memory file is an audit-trigger.
