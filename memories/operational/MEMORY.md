> **RECOVERED INDEX** (2026-08-06, state as of 2026-06-15 @v44) — namespace-deletion recovery; entries may be stale; provenance in `.archive/recovery-2026-08-06/RECOVERY-MANIFEST.md`.

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/5eee468b0b9a82fd@v44`); state as of 2026-06-15 (snapshot mtime); possibly stale — re-verify before relying.

# Memory index — user-home unified orchestrator

Loaded into every conversation. Keep under 200 lines.

## ⭐ NORTH STAR — read first, RELOAD on every compaction-resume

- [_north_star.md](_north_star.md) — **SETTLED decisions; stop re-litigating them.** Keystone result (manufactured-gold parser route FAILED for BoFM, gate 21–6 → **parser track CLOSED**; BoFM = Stanza TF v0.1 + v2-sprays). Banked real-gold (Hebrew/BHSA, GNT/N1904, Vulgate-NT TF — don't re-prove). Parked (LXX-syntax, Vulgate-OT, cross-corpus query — don't start without real gold). Settled tactical: SUD≠fork, data in per-repo private/substrate, genre is never an ATU criterion, private canon untracked. "Should we" not "can we."

## Named arcs (multi-session design conversations)

- [_named_arcs.md](_named_arcs.md) — registry of named arcs (master-blaster, BHSA-canon-migration) with JSONL pointers for "continue X" recall

## User profile

- [user_stan.md](user_stan.md) — Stan's role, biblical-reader projects, decision-making style *(note: git workflow section is outdated; see feedback_claude_commits_and_pushes)*

## Active projects

- 📋 [_deferred_queue.md](_deferred_queue.md) — **the standing parked-work queue** (named arcs, v2/v3 residuals, cross-corpus TODOs, research). The answer to "what's deferred?" — keep current.

- 🛡️ [project_session_durability.md](project_session_durability.md) — JSONL transcripts were silently hard-deleted by Claude Code's 30-day `cleanupPeriodDays` default; FIXED 2026-06-01 (set to 36500). Tax/house convos unrecoverable. Remaining gaps: transcripts unbacked (git excludes `projects/**`), only biblical memory namespace version-controlled. Federation = per-launch-folder memory namespace; cross-history index at `~/.claude/session-index.json`.
- [project_master_blaster.md](project_master_blaster.md) — vault unification migration (this conversation's arc); phase tracker, decisions, JSONL pointer
- [project_bom_reader.md](project_bom_reader.md) — BoFM Reader: repo structure, research state, FEF paper status *(62+ days stale on git workflow)*
- [project_fef_aictp_paper.md](project_fef_aictp_paper.md) — FEF/AICTP paper findings (2026-05-22): "and"/"that" translation-artifact stats (367 vs 533), empty-frame ATU definition, cross-corpus convergence as thesis-not-result
- [project_bofm_bidirectional_rebuild.md](project_bofm_bidirectional_rebuild.md) — BoFM pure-method rebuilt against bidirectional test (2026-05-22): ~51%->~20% fail validated by agents; bar=idea-unit, punctuation zero force; archaic-morphology parse normalization (lexicon-sourced); named residual classes
- [project_gnt_idea_unit_measurement.md](project_gnt_idea_unit_measurement.md) — 2026-05-24 genre-spread measure of GNT v1.5: ~49% on idea-unit bar (vs prior ~72%); over-split = 90-95% of failures; diagnosis = no binding layer in fabric; drives the Part-3 port
- [project_wallace_summaries.md](project_wallace_summaries.md) — Wallace summary retrofit: format spec, source mapping
- [project_bofm_substrate_quality.md](project_bofm_substrate_quality.md) — BoFM over-merge/over-split root cause = PARSE-SUBSTRATE quality (no gold treebank; Stanza mis-parses EModE), not rule-gaps. **2026-05-27 RESOLUTION: mechanical layer hit its ceiling (3 rule-designs killed at the §7.3 gate); deployed reader is MOSTLY CORRECT (over-split diagnostic was inflated by miscounting parallel cola); CHOSEN FIX = v2 LLM-adjudication of judgment-residuals over v1, NOT more rules. Substrate upgrade = free no-LDC EModE treebank ([[reference_emode_substrate]]).** Doctrine: `atu-method/3-implementation/substrate.md`. **First v2-adjudication DEPLOYED 2026-05-27** (6 interjection-detach overrides; pipeline proven).
- [project_corpus_v1_substitutes.md](project_corpus_v1_substitutes.md) — DEFERRED marker: BoFM/LXX/Vulgate lack a treebank; we'll build our own v1 clause-atom source (now feasible having seen BHSA + PROIEL). Remember when Stan mentions it.
- [project_bofm_discourse_voice_deploy.md](project_bofm_discourse_voice_deploy.md) — 2026-05-27: first 2 SYSTEMATIC ATU class-fixes shipped to bomreader.com — frame|quote BREAK (197) + cognition/speech BIND (6, after 2 adversarial audits killed 9 over-merges) + 1 revert; quality-meter gate closed at 47 improvement/0 regression. Next BoFM class needs the PCEEC parser substrate, NOT more override sprays.

## Reference

- [reference_biblical_studies_folder.md](reference_biblical_studies_folder.md) — Dropbox/03-Biblical_Studies layout (Greek + Hebrew); biblical-corpora repos at `~/repos/biblical-corpora/` (bhsa 2.5GB + macula-hebrew 2.3GB + greek-new-testament 391MB)
- [reference_academic_vault.md](reference_academic_vault.md) — my_brain Obsidian vault: structure, tag system, BOM Reader connections
- [reference_analytics.md](reference_analytics.md) — GA4 ID + dashboard URL for bomreader.com
- [reference_corpus_pipeline_map.md](reference_corpus_pipeline_map.md) — per-repo ATU layer map; live layer per repo = the **v1.5 binding-rule stage** (dir names drift: Tanakh `v2/heb`, GNT `v1.5/grk`, BoFM `v2`); no v4 (retired 2026-05-22). **Authoritative live-state record: `atu-method/2-evidence/deployment-status.md`** — check it, don't infer deploy state from stale per-repo docs
- [reference_zotero_mcp.md](reference_zotero_mcp.md) — Zotero 9 + MCP (lricher7329 plugin, :23120, .mcp.json) so Claude can read/write the library; write-scope safety model, division of labor, pending read/write test
- [reference_greek_datasets.md](reference_greek_datasets.md) — per-dataset capability catalog for GNT work (Macula=RICH: `that-VP`/`sub-CL`, clause role, frame, referent, person; sblgnt-lowfat=THIN live source; LDGNT=calibration; PROIEL=pilot). Check the rich treebank BEFORE declaring a feature "unavailable" — its absence caused the "structurally impossible" error
- [reference_lxx_english_brenton.md](reference_lxx_english_brenton.md) — LXX-reader English layer = Brenton's Septuagint (1844, public domain); NETS rejected (OUP copyright, free-to-read ≠ redistributable)
- [reference_emode_substrate.md](reference_emode_substrate.md) — off-the-shelf BoFM-treebank-build path: PPCEME (gold EModE treebank — **free download GONE, LDC-only**) + benepar-PPCEME (model NOT published) + UDConverter (Penn→UD) + Carmack POS. **Free no-LDC stack: PCEEC + EarlyPrint/MorphAdorner + UD parser.** Minimal recipe; treebank-build > LLM-only (they combine)
- **Substrate acquired 2026-05-27** (new repos `readers-lxx` + `readers-vulgate`, both in the CLAUDE.md repo map): **Vulgate = gold NT dependency treebank** (UD_Latin-PROIEL, all 27 books); **LXX = gold morph corpus-wide + gold syntax Gen+Ruth + CATSS mirrored** (at-risk 1994 server). **Relocated 2026-05-27** into each reader's own gitignored `private/substrate/` ("each project gets its intuitive data" — Stan): LXX → `readers-lxx/private/substrate/`, Latin → `readers-vulgate/private/substrate/`. (bhsa/macula/gnt stay in the `biblical-corpora/` container pending a deliberate path-update — they feed live pipelines.) Text-Fabric = unifying format (BHSA ecosystem); only build step = CoNLL-U→TF converter. Inventories: each repo's `research/SUBSTRATE-INVENTORY.md`. Doctrine: `atu-method/3-implementation/substrate.md`. **Confirms the thesis: the substrate was already out there, scattered.**

## Operational feedback (how Claude works with Stan)

### Anti-parking
- [feedback_no_silent_parking.md](feedback_no_silent_parking.md) — defect identified mid-session that isn't built this turn MUST land in `_deferred_queue.md` via an actual `Edit` BEFORE turn-end. Prose like "added to the queue" / "parked for v2" is vapor and evaporates on compaction. Stan red line, 2026-06-05 (Alma 34:4 cross-verse case).

### Workflow & permission
- [feedback_claude_commits_and_pushes.md](feedback_claude_commits_and_pushes.md) — Claude handles BOTH commits and pushes for reader/method repos; discover convention from git log
- [feedback_just_execute_no_permission_churn.md](feedback_just_execute_no_permission_churn.md) — within authorized scope, just execute; ask only for scope expansion or irreversible actions
- [feedback_broad_shell_no_permission_hang.md](feedback_broad_shell_no_permission_hang.md) — Bash AND PowerShell broadly allowed in settings.json; never let a shell command hang on a per-command permission prompt
- [feedback_scratch_belongs_in_repo.md](feedback_scratch_belongs_in_repo.md) — C:\tmp is DEPRECATED as scratch (grew to 1.2GB unmanaged); reusable dev scripts → repo tracked 5-machinery/scripts//research/, true throwaway → repo gitignored scratch/ (or work\_scratch\); promote keepers immediately
- [feedback_ship_independent_not_coupled.md](feedback_ship_independent_not_coupled.md) — ship each repo the moment it's gated; cross-repo atomicity is ONLY for shared-canon cascades, NOT independent reader sites; parallelize independent tracks
- [feedback_always_recommend_in_options.md](feedback_always_recommend_in_options.md) — when offering Stan a choice, ALWAYS mark a "(Recommended)" option + say why; never a neutral menu
- [feedback_check_in_regularly.md](feedback_check_in_regularly.md) — during long background work, check in at regular intervals (schedule a wakeup); don't go silent until completion
- [feedback_never_handtype_greek_hebrew.md](feedback_never_handtype_greek_hebrew.md) — never hand-type Greek/Hebrew (silent script-mixing); source from clean occurrences + run the mixed-script scanner before committing
- [feedback_workflow.md](feedback_workflow.md) — older operational rules (bash globally allowed, two-AI workflow, research folder symlink); *git workflow section superseded by feedback_claude_commits_and_pushes*
- [feedback_stan_thinks_claude_files.md](feedback_stan_thinks_claude_files.md) — execute routine moves autonomously per durable system rules; reserve Stan's bandwidth for synthesis
- [feedback_do_it_once.md](feedback_do_it_once.md) — when not urgent, do a task once completely; don't add a throwaway quick pass the full job will redo
- [feedback_surface_judgment_calls.md](feedback_surface_judgment_calls.md) — surface non-mandated choices (incl. dates on submissions) as labeled assumptions BEFORE baking into a deliverable; a bare date reads as the authoring date, not a due date
- [feedback_check_prior_corpora.md](feedback_check_prior_corpora.md) — before treating a new-corpus problem as novel, ask "have we already solved this in Tanakh / another built corpus?" — port the proven solution (ties to Stan's cross-corpus ATU-convergence thesis)
- [feedback_no_fly_swatting.md](feedback_no_fly_swatting.md) — on a deployed mechanical edition, don't hand-patch individual verse splits; the residual tail resolves systematically via v2→v4 progression. Fix only single-root-cause-heals-a-class bugs; defer N-rules-for-N-verses
- [feedback_hand_edit_is_a_datapoint.md](feedback_hand_edit_is_a_datapoint.md) — a human hand-edit is ONE triangulation data point, never definitive weight; human may miss grammar/big-picture/consistency. Measure by canon-conformance; divergence = investigate which is right, don't defer to the human
- [feedback_verify_deploy_state_never_assert.md](feedback_verify_deploy_state_never_assert.md) — NEVER assert deploy/architecture state from docs/memory/agent-claim; ground truth = `atu-method/2-evidence/deployment-status.md` + git log of the live dir. All 3 readers run mechanical-first (v1.5 stage) LIVE; hand-edits superseded. The hand-edit-as-oracle reflex is the trigger to STOP and verify
- [feedback_render_path_verification.md](feedback_render_path_verification.md) — deploy-verify for client-side-rendered artifacts = headless Chrome --dump-dom on the RENDERED DOM, never curl+grep; escape data at every innerHTML injection site + audit corpus values for `<>&` BEFORE shipping a renderer. 2026-06-06 tanakh-morph: את's BHSA gloss `<object marker>` swallowed every chapter; "live-verified" via curl missed it

### Quality gates (pre-output, audit, planning)
- [feedback_pre_output_checks.md](feedback_pre_output_checks.md) — 8-gate scan before every response (compaction-resume, permission-ask regex, correction-preamble, doc-rewrite preamble, hand-wavy language, §7.3 audit, external-transcript fidelity, proactive memory-save)
- [feedback_never_skip_audit_gate.md](feedback_never_skip_audit_gate.md) — §7.3 audit gates (new mechanism/closed list/sub-category/rule) dispatch ≥2 parallel adversarial audits BEFORE code, not after
- [feedback_subagent_specs_require_receipts.md](feedback_subagent_specs_require_receipts.md) — every sub-agent/Workflow spec naming a file/module/function/lemma/feature MUST require pasted verification receipts (ls/wc/Grep/query output) in StructuredOutput; the upstream filter for the §7.3 gate. 2026-06-04: 3/13 specs had phantom citations / fabricated modules / `vt=weqt` (a non-existent BHSA feature) because prompts said "verify" without requiring receipts
- [feedback_three_lens_default_for_plans.md](feedback_three_lens_default_for_plans.md) — non-trivial plans get ≥3 parallel adversarial audits (coding/NLP-domain/workflow lenses) before landing in front of Stan
- [feedback_conformance_is_not_correctness.md](feedback_conformance_is_not_correctness.md) — canon-conformance is an upper bound + was confounded (mixed v2-mine/pure-method); measure the real bidirectional-test rate by genre-spread sampling, never report rule-conformance as "% complete"
- [feedback_parallel_default.md](feedback_parallel_default.md) — N independent units → dispatch all N in parallel (single message, multiple tool calls); sequential only with a real dependency
- [feedback_mechanical_first_for_own_review.md](feedback_mechanical_first_for_own_review.md) — mechanical-first governs Claude's OWN adjudication, not just pipeline output: query the richest treebank (Macula `that-VP`/`sub-CL`, role, frame, referent, person) BEFORE hand-reasoning an ATU/Greek call. The slow GNT ὅτι hand-classification was the failure; "structurally impossible, defer to v2" was wrong because Macula tags it mechanically
- [feedback_code_path_diagnoses_require_running_the_code.md](feedback_code_path_diagnoses_require_running_the_code.md) — mechanical-first extends to the SOURCE TREE: code-path diagnoses ("rule R at file F line N is the bug-locus") are state-claims requiring fresh in-turn Read + Grep + Run, same status as rule #8 external-artifact claims. STOP signal: "I think rule R fires here." Encodes standing default #9. 2026-06-04 origin: 4 consecutive §7.3 audits rejected proposals on this shape (wrong line 555/529; wrong parse file ensemble vs v0-cache-conllu; comma-T21 topology invented; parallel detector when _is_copular_independent_predication at 229 existed).
- [feedback_canon_citation_requires_verbatim_read.md](feedback_canon_citation_requires_verbatim_read.md) — canon citations (framework.md §X.Y, binding-rules-*.md, §v1.x) are external-artifact state and require fresh `Read` of cited section + 30 lines downstream + verbatim quote of the firewall in the artifact. 2026-06-05 anchoring failure: Alma 34:7 PP-conj rule cited framework.md:103-111 §2.2 in its comment while §2.2(ii) firewall at lines 113-117 EXPLICITLY forbids the shared-PP elision the rule restored; rule shipped + regen + +30 validator regressions before Workflow §7.3 audit caught it.
- [feedback_time_estimate_as_diagnostic.md](feedback_time_estimate_as_diagnostic.md) — when work feels like multi-day/multi-week for biblical-text engineering, the estimate is itself diagnostic — almost always treating substrate (data-already-produced) as if it were code-to-be-written. 2026-05-30 proof: symmetric-substrate construction was framed as "weeks" then collapsed to 30s of Python execution + ~250 lines of glue once the on-disk substrate (Macula xml:id + MetaV Strong's) was actually consulted. 94.81% mechanical structural agreement across 26,014 verses in under 90s. Phrases like "acquire X" / "Phase 0 acquisition" / "multi-week engineering" are the stop signal.
- [feedback_scrutinize_stan_instincts.md](feedback_scrutinize_stan_instincts.md) — Stan's ATU instincts are starting signals, not finished judgments. Situate against the framework (bidirectional test §2.1, casuistic allowances, complement-vs-quote) before shipping. Endorsed 2026-06-02 after Alma 37:15 dangling-protasis case revealed auto-deference fails the test; auto-pushback wastes the signal; "situate" produces gold.

### Style & framing
- [feedback_no_correction_preamble.md](feedback_no_correction_preamble.md) — no "you're right" / "let me reset" — just deliver corrected substance
- [feedback_doc_rewrite_no_preamble.md](feedback_doc_rewrite_no_preamble.md) — rewriting a methodology/spec doc: present current state cleanly; NO version preambles, NO "what it was before" headers
- [feedback_no_handwave_in_precision_artifacts.md](feedback_no_handwave_in_precision_artifacts.md) — banned in trigger messages / directives / design docs / sub-agent prompts: "or whatever", "or similar", "TBD", "discover from", "figure out"
- [feedback_lean_entry_points.md](feedback_lean_entry_points.md) — CLAUDE.md is read every wake; keep it lean (~150-200 lines); detail goes to atu-method/docs + memories
- [feedback_session_bookend_protocol.md](feedback_session_bookend_protocol.md) — no session-bookend artifacts; JSONL is the verbatim record
- [feedback_simplicity_bias.md](feedback_simplicity_bias.md) — Stan's instincts pull toward complexity; push back; prefer subsuming into existing system
- [feedback_staged_paper_scope_discipline.md](feedback_staged_paper_scope_discipline.md) — stage-1 papers stake nothing; defer named theory + cross-corpus claims
- [feedback_atu_resolution_author_relative.md](feedback_atu_resolution_author_relative.md) — ATU size is author-relative (smallest chunk the author intended; finer for Luke/Paul/John); preserves the rationale behind R19 (gen abs own line); rescued from defunct readers-nt
- [feedback_external_unit_is_not_atu.md](feedback_external_unit_is_not_atu.md) — scholars' cola/IUs/periods (Scheppers/Marschall/Korpel) are NOT our ATU; their criteria may overlap + be useful feedstock but do NOT replace our method — the bidirectional test is sole arbiter, every external criterion is filtered through it, granularity mismatch is expected not error
- [feedback_em_dashes_illustrative_not_text.md](feedback_em_dashes_illustrative_not_text.md) — em-dashes in Skousen/scholarly clausal illustrations are NOT canonical text; punctuation has zero force in our system. The restoration target is the clause-boundary signal (where the parenthetical opens/closes), not the dash marks. Confirmed 2026-06-01 during Alma 37:41 analysis — pushes Skousen-restoration toward option (C) structural-signal layer, not a punctuation-overlay

### Resume / continuity / contamination
- [feedback_compaction_resume_protocol.md](feedback_compaction_resume_protocol.md) — on compaction, FIRST tool call reads last 30-35 user/assistant turns from session JSONL verbatim (the harness summary is degraded)
- [feedback_circling_back_thread_tracking.md](feedback_circling_back_thread_tracking.md) — hold open-threads across topic-shifts; lead with "circling back to X" when re-anchoring
- [feedback_external_transcript_full_fidelity.md](feedback_external_transcript_full_fidelity.md) — brainstorm transcripts Stan shares ARE load-bearing program thinking; full inventory then filter; never skim-and-respond
- [feedback_rhetoric_bandwagon.md](feedback_rhetoric_bandwagon.md) — scrutinize other-LLM-transcript flattery, authority-padded citations, framework-adoption pressure before propagating
- [feedback_stan_writes_claude_edits.md](feedback_stan_writes_claude_edits.md) — orientation docs + papers: Stan writes substantive prose; Claude shows typos/fixes mechanical errors/suggests organization

### Domain-specific (carried over from bibleman-home)
- [feedback_debug_trace_values.md](feedback_debug_trace_values.md) — when a value is visibly wrong, trace its origin first; don't shotgun infrastructure
- [feedback_preserve_formatting.md](feedback_preserve_formatting.md) — don't rebuild entire xlsx from scratch when only tabs changed; preserve column formatting
- [feedback_read_source_carefully.md](feedback_read_source_carefully.md) — careful source reading before changes

## Methodology canon (separate, not auto-loaded here)

The biblical-reader methodology + cross-corpus durable rules live at `~/repos/atu-method/`:

- `~/repos/atu-method/docs/` — methodology specs (framework.md, binding-rules-hebrew.md, toolset-architecture.md, apparatus.md, methodology-position.md)
- `~/repos/atu-method/memories/` — 32 cross-corpus rules (rule_proposal_gates, atu_test_is_bidirectional, principle_vs_mechanical_coverage, etc.) — read on trigger from biblical-reader work

The vault CLAUDE.md (~/.claude/CLAUDE.md, Phase 5) cross-references these on biblical-reader triggers.
