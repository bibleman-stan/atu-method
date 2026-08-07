# canon-index-receipts.md — verification receipts for canon-index.md

**Companion to `canon-index.md`** — produced 2026-06-06 in response to claudit's audit directive:
*"VERIFICATION RECEIPTS, not assertions: every home + every consumer backed by actual grep/read
output."* This file backs every claim in `canon-index.md` with raw verbatim grep/Read output from
fresh in-turn verification. Receipts are organized per concept-family lane, matching the verifier
workflow's five parallel scopes.

## Schema (per row)

```
## <anchor>

**Home:** <file:line>
> <verbatim Read excerpt>

**Live-successor:** <where, or "null">
> <verbatim excerpt, if applicable>

**Consumers (verified):**
- <file:line>: `<grep output line, verbatim>`
- ...

**Consumers (FLAGGED):**
- <file:line>: <reason the ground-truth check failed or returned a tension>
```

## Audit-trail notes

- Workflow `wasutgzgd` (5 parallel verifier lanes, 444k subagent tokens, 365 tool uses).
- "FLAGGED" entries are NOT errors per se — they include cases where:
  - The cite was already repointed (Batch A1 §1.10 cites now read `§2.1`, not `§1.10`)
  - The cite consumes the umbrella anchor not the granular sub-anchor (e.g. BoFM canon:26 cites `framework.md §0` covering §0.1/§0.2/§0.3/§0.4 collectively)
  - The cite presents a semantic tension with the cited anchor (e.g. `feedback_rhetoric_bandwagon.md:13` framing "psycholinguistic / cognitive" is in tension with §0.3's "not derived from a cognitive theory")
  - Each FLAGGED entry surfaces something Stan + claudit should adjudicate; collected at the end of this file.
- No FLAGGED entry indicates an unverifiable claim that should auto-fail the audit.
- Workflow ran with prohibition: "NO interpretive work — agents return raw grep output structured by row. Main loop synthesizes."

---


# Lane 1 — Part A (§0.x) + Part C-bis (§7.x)

```
## §0.1 Mission

**Home:** `_old/framework.md:13-23` (i.e. `docs/_old/framework.md`)
> ## §0.1 Mission
>
> The apparatus reveals **atomic thought units (ATUs)** — units of meaning a reader can process discretely. Each line on the page renders one ATU; each ATU is a span the reader can take in before needing the next.

**Live-successor:** `docs/01-normative/framework.md §1 Purpose` (lines 9-19)
> ## §1 Purpose
>
> The apparatus produces **colometric reading editions** of canonical texts: each line on the page renders one **atomic thought unit (ATU)** — a span a reader can take in as a single complete unit before needing the next.
>
> The apparatus reveals ATU structure already present in the text. It does NOT:
>
> - Adjudicate textual variants (the source text is a fixed input)
> - Produce typography or oral-delivery markup
> - Reveal rhetorical parallelism (separate scholarly layer; may overlap but is not the target)
> - Add, remove, or alter words

**Consumers (verified):**
- `scholarship/bofm/R20.md:17`: `The apparatus's mission is to render each line as one atomic thought unit (`framework.md §1`). The atomic-thought test, applied at the line level, presupposes that the line carries predicative content the reader can take in as a complete cognitive bite. A line with zero anchors is, by construction, not a thought — it is a fragment dependent on its neighbors for completion.`
  → Already repointed to `§1` in Batch A1; no `§0.1` token at this line.
- `scholarship/bofm/R20.md:126`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1 (atomic-thought mission), §1.1 (generative principle — each proposition splits by default), §1.4 J1-J5 (the five structural justifications — referenced by Exemption 4), §1.5 M3 (bare-governor indivisibility — related "fragment fails atomic-thought" failure mode)`
  → Already repointed to `§1`; no `§0.1` token at this line.
- `readers-bofm/1-method/colometry-canon.md:26` (the §0 pointer-block, spanning canon-index's referenced :22-28): `**Pointer to framework.** Universal mission, method (sense-driven mission + syntax-constrained method), pragmatic stance, and scope statements are codified at [`atu-method/docs/01-normative/framework.md §0`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- `readers-gnt/private/01-method/colometry-canon.md:29` (the §0 pointer-block, spanning canon-index's referenced :25-43): `**Pointer to framework.** Universal mission, method (sense-driven mission + syntax-constrained method), pragmatic stance, and scope statements are codified at [`atu-method/docs/01-normative/framework.md §0`](docs/01-normative/framework.md). This canon does not duplicate that prose.`

**Consumers (FLAGGED):**
- `scholarship/bofm/R20.md:17,126` — canon-index lists these as §0.1 consumers but they cite `§1`, not `§0.1`. This is correct per the canon-index annotation "(repointed in Batch A1 to §1)". The cells are NOT phantom; they are post-repoint live successors. Verifier note: the row is faithful (the §-citation was rewritten before the index was hand-built) — flagged because the post-repoint cite is what's on disk, not the pre-repoint `§0.1`.
- BoFM canon range `22-28` and GNT range `25-43` — `§0` is cited at BoFM:26 and GNT:29 (single-line cites). The "ranges" in the canon-index represent the surrounding §0 pointer block. No verbatim `§0.1` token at the cited ranges in either canon; both cite `§0` umbrella.

## §0.2 Method

**Home:** `_old/framework.md:25-29`
> ## §0.2 Method
>
> **The mission is sense-driven. The method is syntax-constrained.** A break that violates the target language's syntax is always wrong regardless of how strong the sense argument; a sense judgment within the permitted space is editorially recoverable. Leading with syntax preserves the discipline that lets sense work — it does not demote the mission.
>
> Novel rules MAY originate from sense-driven observation. The method accommodates this: sense proposes, syntax filters, the combination becomes a rule. But every break that survives to the corpus MUST be affirmable by the target language's syntax.

**Live-successor:** null — `docs/01-normative/framework.md` has no `§0.2` heading (verified by grep for `^## §0\.|^### §0\.` against full live framework.md returning no matches). Live §2 introduces "thought operationalized by a grammatical test … grammatical closure is a proxy for thought" (framework.md:22) but does NOT carry the sense-driven mission vs syntax-constrained method asymmetry explicitly. Canon-index disposition `fold→§1 Purpose` is consistent with the absence.

**Consumers (verified):**
- `readers-bofm/1-method/colometry-canon.md:26` (pointer block within :22-28): same `§0` cite line as §0.1 above (the pointer block covers mission + method + stance + scope as a single `framework.md §0` reference).
- `readers-gnt/private/01-method/colometry-canon.md:29` (pointer block within :25-43): same `§0` cite line as above.

**Consumers (FLAGGED):**
- No verbatim `§0.2` token exists in the BoFM or GNT canon files (Grep `§0` matches lines BoFM:5, BoFM:26 and GNT:8, GNT:29, GNT:41, GNT:177, GNT:2302, GNT:2310, GNT:2313, GNT:2314, GNT:2369; none use `§0.2`). The §0.2 sub-anchor is consumed only via the umbrella `§0` pointer. Cite-by-umbrella is a real consumption pattern but does NOT give a verbatim §0.2 receipt.

## §0.3 Pragmatic stance

**Home:** `_old/framework.md:31-33`
> ## §0.3 Pragmatic stance
>
> This methodology is a set of conventions reflecting what the apparatus is trying to reveal. It is not derived from a cognitive theory; no such claim is asserted. The apparatus operates as what it is: a consistently-applied editorial practice grounded in target-language syntax, tested against the corpus, and refined by validator sweeps.

**Live-successor:** null — verified by grep across live `docs/01-normative/framework.md` for `pragmatic stance` / `cognitive theory` returning no matches in live file. `methodology-position.md` exists adjacent but does not state the cognitive-theory disclaimer at any matched line (no §0.3 token).

**Consumers (verified):**
- `atu-method/memories/feedback_rhetoric_bandwagon.md:13`: `Our theoretical foundation is **psycholinguistic / cognitive**, not rhetorical or parallelism-structural. See `feedback_sense_line_mission.md` for the grounding principle: atomic thought trumps poetic structure; we expose sense-lines, not parallels; Parry is a separate layer we may overlap with but do not target.`
  → Conceptual cite — does NOT use `§0.3` token. Most thematically-aligned line; same family but it asserts the OPPOSITE framing ("psycholinguistic / cognitive" = a theoretical foundation, vs §0.3's "not derived from a cognitive theory; no such claim is asserted"). Flagged below.
- `readers-bofm/1-method/colometry-canon.md:26` and `readers-gnt/private/01-method/colometry-canon.md:29` — same umbrella `§0` pointer-block lines verified under §0.1 above (these are the "BoFM canon:22-28 + GNT canon:25-43 pointer blocks" cited by canon-index).

**Consumers (FLAGGED):**
- `atu-method/memories/feedback_rhetoric_bandwagon.md` — canon-index says "(1 cite)" but a `§0.3` Grep returns no matches in this file. The conceptual link goes through `feedback_sense_line_mission.md` referenced at line 13. **More importantly:** the memory's framing ("Our theoretical foundation is psycholinguistic / cognitive") is in semantic *tension* with §0.3's "not derived from a cognitive theory; no such claim is asserted" — the canon-index disposition `fold→§1 Purpose` glosses this tension. Surface to Stan.
- BoFM/GNT canon pointer-block — same FLAG as §0.2: §0.3 sub-anchor is consumed only via umbrella `§0`; no verbatim §0.3 token in either canon.

## §0.4 Scope

**Home:** `_old/framework.md:35-41`
> ## §0.4 Scope
>
> Each per-corpus instantiation of this framework governs **where lines break** in its source texts. It does NOT govern:
> - Punctuation (inherited from the source; preserved unchanged)
> - Words (never added, removed, or altered)
> - Layout beyond break positions
> - External editorial overlays (te'amim, NA28 paragraph structure, ancient codex colometric arrangements, etc. — see §1.10 and §1.11)

**Live-successor:** `docs/01-normative/framework.md §1 Purpose` (partial: NOT-list at lines 13-19) + `§2.1:101` (punctuation-zero-force) + `§2.2:116` (te'amim/genre exclusions). §1 Purpose NOT-list verified above under §0.1 successor.

**Consumers (verified):**
- `scholarship/bofm/R23.md:61`: `The BoFM's distinctive *"forty and second"* / *"twenty and seventh"* compound-ordinal pattern (number-word + *and* + ordinal) is preserved as part of the formula's lexicalized form. The UD validator (`validate_rule_23_ud.py` lines 99-117) explicitly allows the compound-ordinal sub-pattern inside the formula's anchor span. The compound form is not editorially modernized to *"forty-second"* — punctuation and word-content are inherited from the source per the universal preservation principle (`framework.md §1`).`
  → Already repointed to `§1` (Batch A1); no `§0.4` token at this line.
- `readers-bofm/1-method/colometry-canon.md:26` and `readers-gnt/private/01-method/colometry-canon.md:29` — same umbrella `§0` pointer-block lines as above.

**Consumers (FLAGGED):**
- `scholarship/bofm/R23.md:61` — same shape as R20: cites `§1`, not `§0.4`. Post-repoint state; the canon-index annotation "(repointed in Batch A1 to §1)" is faithful. No live `§0.4` token on disk in any consumer.

## §7.0 Categories A / B / C

**Home:** `docs/01-normative/framework.md:237-256` (live)
> ### §7.0 Categories A / B / C
>
> Every proposed change falls into one of three categories:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:237`: `### §7.0 Categories A / B / C` (definition)
- `docs/01-normative/framework.md:346`: `3. If clean ≥80% → apply clean decisions mechanically (Category A per §7.0), remove "proposed" label; capture the adoption evidence (sweep counts, audit verdicts) in the commit message.`
- `docs/01-normative/cross-corpus-principles.md:55`: `- Categories A/B/C: `framework.md §7.0``
- `scholarship/bofm/EP-1.md:153`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §2.1 (punctuation has zero force) + §7.0 (Category B editorial-judgment) + §1.5 J5 (substantive adjunct as own focus — interaction)`
- `canon-index.md:49`: hard-constraint #11 documenting the §2→§7.0 move.
- `canon-index.md:111`: glossary stale-cite next-cycle flag.
- `canon-index.md:117`: row-introduction explaining §7.0 was sourced from `_old/framework.md:343-361`.
- `canon-index.md:247`: Batch A1 commit reference.

**Consumers (FLAGGED):**
- None at the §7.0 ID level. (Glossary stale-cite at canon-index:111 is itself documented as out-of-scope and flagged for next-cycle, so it is a tracked-flag not a hidden-flag.)

## §7.1 Authority

**Home:** `docs/01-normative/framework.md:257-260` (live)
> ### §7.1 Authority
>
> This document is the authoritative specification of the framework, categories, and change protocol. Per-corpus canons reference this document by stable section ID. They MUST NOT inline framework prose.

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:257`: `### §7.1 Authority` (definition)
- `docs/_old/_index.md:24`: `- [`change-protocol.md`](change-protocol.md) — **Canon-change discipline.** §7.1 framework authority. §7.2 proposal requirements. §7.3 12 mandatory-audit triggers. ...` (archived index cite)
- `docs/_old/change-protocol.md:10`: `## §7.1 Authority` (archived home)
- `docs/_old/framework.md:367`: `The change protocol (§7.1 Authority through §7.8 Proposed-rule adoption protocol) has been extracted to its own canonical document: ...` (archived reference)
- `canon-index.md:123`: row entry self-citing `framework.md:257-260`.

**Consumers (FLAGGED):**
- Canon-index row reports "(no rot-list cites; structural-anchor only)" — consistent with absence of live consumer §7.1 citations in `scholarship/` / `memories/` / per-corpus canon files. Live structural-anchor with no operational consumers. Not a defect.

## §7.2 Proposal requirements

**Home:** `docs/01-normative/framework.md:261-277` (live)
> ### §7.2 Proposal requirements
>
> Proposals to change an existing rule, add a new rule, or retire a rule MUST:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:261`: `### §7.2 Proposal requirements` (definition)
- `docs/01-normative/framework.md:333`: `- All three defensibility elements (WHY / HOW WE KNOW / SCOPE per §7.2) are captured for each addition (in the scholarship companion, not the canon).`
- `scholarship/bofm/R20.md:33`: `The BoFM-archaic register preserves KJV-style discourse-connective usage (*Wherefore*, *And now*, *Therefore*, *Yea*, *Behold*) as standalone-line beats. The closed list in the operational entry is corpus-attested and conservative — adding a connective requires worked corpus evidence per §7.2.`
- `docs/_old/_index.md:24`: archived index cite (same line as §7.1 above).
- `docs/_old/change-protocol.md:14`: `## §7.2 Proposal requirements` (archived home).
- `docs/_old/change-protocol.md:86`: `- All three defensibility elements (WHY / HOW WE KNOW / SCOPE per §7.2) are captured ...` (archived self-ref).
- `docs/_old/framework.md:367`: same archived reference cited under §7.1.
- `canon-index.md:124`: row entry.

**Consumers (FLAGGED):**
- Canon-index says "scholarship/bofm/R20.md:33 + 1 other rot-list cite" — the "1 other" is unnamed. Live grep finds only R20.md:33 across `atu-method/`. Possible second cite was the `change-protocol.md` archived self-ref (now `_old/`) and dropped from rot-list as Stage 1 resolved it. Flag for canon-index author confirmation.

## §7.3 Mandatory-audit triggers

**Home:** `docs/01-normative/framework.md:278-298` (live)
> ### §7.3 Mandatory-audit triggers (12 categories)
>
> For proposals matching ANY of the following triggers, an adversarial audit (hostile-agent dispatch or equivalent external skeptical review) MUST be dispatched and its findings reflected in the commit. Skipping audit on a triggered proposal is a protocol violation.

**Live-successor:** n/a (this IS the live anchor — corrects pre-Stage-1 phantom status).

**Consumers (verified) — live §7.3 cites grouped by file:**

*atu-method/docs:*
- `docs/01-normative/framework.md:267`: `3. **Survive adversarial audit** (when any mandatory-audit trigger fires; see §7.3).`
- `docs/01-normative/framework.md:278`: `### §7.3 Mandatory-audit triggers (12 categories)` (definition)
- `docs/01-normative/framework.md:312`: `- `Audit-skippable per §7.3 ([reason])` with the reason citing one of §7.4 categories; OR`
- `docs/01-normative/cross-corpus-principles.md:130`: `§7.3`. A proposed sixth justification MUST demonstrate (a) that it is a genuinely distinct instance`
- `docs/01-normative/cross-corpus-principles.md:238`: `§7.3`.`
- `docs/01-normative/glossary.md:44`: `... Adding a marker is a §7.3 closed-list-extension audit trigger. See `framework.md §2.2`.`
- `docs/03-implementation/substrate.md:23`: `... were all reshaped/killed at the §7.3 audit gate *before* code).`
- `docs/05-status/deployment-status.md:21`: (line omitted by truncation)

*atu-method/scholarship:*
- `scholarship/_index.md:60`: `- `methodology/audit-discipline.md` — the WHY behind §7.3 mandatory-audit triggers.`
- `scholarship/methodology/_index.md:19`: `- `audit-discipline.md` — WHY the §7.3 mandatory-audit triggers. ...`
- `scholarship/methodology/_index.md:23`: `... (§7.3 trigger #1 if a new methodology essay is added; lower triggers for edits within existing essays).`
- `scholarship/bofm/R28.md:63`: `Both refinements were post-codification audit findings (§7.3 trigger #6 — mechanical-signature changes under a settled rule) ...`
- `scholarship/bofm/R28.md:107`: `... Both were §7.3 trigger #6 changes (mechanical-signature changes under a settled rule). ...`
- `scholarship/bofm/R15.md:44`: `... triggered the corpus-wide vocative sweep under §7.3 trigger #12-b ...`
- `scholarship/bofm/R15.md:97`: `... corpus-wide vocative sweep that followed (under §7.3 trigger #12-b post-detection) ...`
- `scholarship/bofm/R21.md:93`: `Per §Action-Codes "new action codes require a meta-template change (§7.3 trigger #9)," ...`
- `scholarship/bofm/R21.md:105`: `... awaits the validator's first corpus sweep (§7.3 trigger #12-a — post-codification goal-fit audit).`
- `scholarship/bofm/R20.md:93`: `... New exemptions would require §7.3 trigger #1 mandatory-audit dispatch with worked corpus example. ...`
- `scholarship/bofm/R20.md:117`: `... Pending corpus-attestation audit and §7.3 trigger #1 mandatory-audit dispatch.`
- `scholarship/bofm/EP-5.md:52`: `... Pending tasks for EP-5 corpus-fit work are tracked in BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-5.md:128`: `... Per BoFM canon §7.3 trigger #12 (post-codification corpus-fit verification) ...`
- `scholarship/bofm/EP-4.md:75`: `... Per BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-4.md:127`: `... Per BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-1.md:61`: `... Pending tasks for EP-1 corpus-fit work are tracked in BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-1.md:115`: `... Per BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-3.md:58`: `... Pending tasks for EP-3 corpus-fit work are tracked in BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/EP-3.md:135`: `... Per BoFM canon §7.3 trigger #12 ...`
- `scholarship/bofm/R18a.md:81`: `... Building a rule on a singleton fails canon §7.3's biased-spot-check guard.`
- `scholarship/bofm/R6.md:129`: (line omitted by truncation)

*atu-method/memories:*
- `memories/_index.md:81`: `Per §7.3 trigger #10 (Discipline-shifting memory file additions), new memories ... are behaviorally-governing and require the same audit scrutiny as canon.`
- `memories/feedback_three_anti_default_factors.md:25`: `Source: `change-protocol.md` §7.3 trigger #3 (spot-check-based proposals) + §7.8 (≥80% adoption threshold).`
- `memories/feedback_rule_proposal_gates.md:31`: `- <50 cases → spot-check; not adoption-ready (per `change-protocol.md` §7.3 trigger #3)`
- `memories/feedback_rule_proposal_gates.md:47`: `Proposal is ready for `change-protocol.md` §7.3 mandatory-audit dispatch ...`
- `memories/feedback_rule_proposal_gates.md:55`: `... When dispatching adversarial audits per §7.3, include the gate-status of the proposal in the dispatch prompt ...`
- `memories/feedback_rule_proposal_gates.md:57`: `... `change-protocol.md` §7.3 / §7.8 (audit triggers + adoption threshold).`
- `memories/feedback_rhetoric_bandwagon.md:56`: `Canon §7.3 now specifies 11 mandatory-audit triggers and §2 has a scope/precedence/closed-list/carve-out diagnostic ...`
- `memories/feedback_no_fake_dilemmas.md:19`: `2. **§7.3 skip-safe means skip.** Typo fixes, cross-reference updates without precedence claims, mechanical Category-A applications: don't ask. Apply.`
- `memories/feedback_no_eyeball_offers.md:9` and `:11`: cites including `... The audit was the obvious next step (codified in canon §7.3); ...`
- `memories/feedback_directive_protocol.md:45`: `- **Audit triggers** — if any items trip §7.3 mandatory-audit triggers, the directive flags them`
- `memories/feedback_commit_workflow.md:14`: `2. **Exception — explicit Stan authorization required** for canon edits that match a §7.3 mandatory-audit trigger ...`

*atu-method/atu_method:*
- `atu_method/hooks/__init__.py:3`: `- check_canon_extensions: detects §7.3 mandatory-audit-trigger patterns in`

*atu-method root:*
- `README.md:88`: `│   └── change-protocol.md   §7.3 mandatory-audit triggers, audit-evidence rules`
- `canon-index.md:28,49,111,117,125,182,237,238,239,240,247`: multiple self-references (row entry + hard-constraints + Stage-1 batch table).

*Workspace + global CLAUDE.md cites:*
- `C:/Users/bibleman/CLAUDE.md:33`: `... Without receipts, the spec is unaudit-able — the §7.3 gate cannot tell fabricated module names from real ones. ...`
- `C:/Users/bibleman/CLAUDE.md:35`: `... dispatch the §7.3 audit ONLY on the surviving variant(s). ...`
- `C:/Users/bibleman/CLAUDE.md:41`: `... The §7.3 gate has caught parallel-detector designs at least twice in the 2026-06-04 session ...`
- `C:/Users/bibleman/CLAUDE.md:43`: `... New mechanism / new integration / new env-flag / new guard structure triggers the §7.3 audit gate BEFORE code, not after. ... Citing canon without Reading canon THIS TURN = automatic §7.3 trigger ... BEFORE dispatching the §7.3 adversarial audit on a code-touching proposal ...`
- `C:/Users/bibleman/CLAUDE.md:45`: `... 4 consecutive §7.3 audits rejected proposals on this same shape ...`
- `C:/Users/bibleman/.claude/CLAUDE.md`: no §7.3 cites (Grep returned no matches — the user-wide file does NOT cite §7.3 directly).
- `repos/readers-bofm/CLAUDE.md:21`: `... Three rule-designs ... were each reshaped/killed at the §7.3 adversarial-audit gate on 2026-05-27 ...`
- `repos/readers-bofm/CLAUDE.md:38`: `Audit-skippable per §7.3 (master-blaster Phase 6 — ...)` (commit-message template)
- `repos/readers-gnt/CLAUDE.md:28`: `Audit-skippable per §7.3 (master-blaster Phase 6 — ...)` (template)
- `repos/readers-tanakh/CLAUDE.md:40`: `Audit-skippable per §7.3 (master-blaster Phase 6 — ...)` (template)

*Per-project memory:*
- `.claude/projects/C--Users-bibleman/memory/feedback_code_path_diagnoses_require_running_the_code.md:25,46,48,57,61`: multiple §7.3 cites.
- `.claude/projects/C--Users-bibleman/memory/feedback_claude_commits_and_pushes.md:33`: `... Every commit touching canon must declare `Audit-skippable per §7.3 (<reason>)` ...`
- `.claude/projects/C--Users-bibleman/memory/feedback_canon_citation_requires_verbatim_read.md:20,37`: §7.3 audit-gate cross-refs.
- `.claude/projects/C--Users-bibleman/memory/feedback_pre_output_checks.md:12,82,84,139,159,189`: multiple §7.3 cites.
- `.claude/projects/C--Users-bibleman/memory/_deferred_queue.md:23,43,45,47`: §7.3 cites (PARKED items).
- `.claude/projects/C--Users-bibleman/memory/feedback_no_handwave_in_precision_artifacts.md:60`: `... The §7.3 audit gate catches design-time hand-waves before code lands ...`
- `.claude/projects/C--Users-bibleman/memory/feedback_never_skip_audit_gate.md:3,10,16,18,20,24,27,31,36,43,45,47,62,69,73`: many §7.3 cites (the dedicated audit-gate memory).
- `.claude/projects/C--Users-bibleman/memory/feedback_three_lens_default_for_plans.md:3,80,87`: §7.3 cites.
- `.claude/projects/C--Users-bibleman/memory/project_bofm_discourse_voice_deploy.md:18`: `... only the 6 surviving BOTH audits shipped. This is the §7.3 gate working: ...`
- `.claude/projects/C--Users-bibleman/memory/project_bofm_substrate_quality.md:10`: cite (line truncated).
- `.claude/projects/C--Users-bibleman/memory/MEMORY.md:28,68,69,74,75`: §7.3 cites (MEMORY index entries).

*Reader-repo non-md (Python validators):*
- Not found via this grep cycle (extension filter limited to md). Canon-index claim of validator cites is for `readers-bofm/validators/colometry/validate_rule_07_ud.py:161` and `validate_rule_06_ud.py:104` — these cite "§1.5 M4", NOT §7.3. The §7.3 row's "36 cites resolved" claim is the framework-md-cite count, not validator count.

*Archived (`_old/`) — for completeness; not "live consumers":*
- `docs/_old/_index.md:24,42`; `docs/_old/change-protocol.md:31,65`; `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:32,66`, `editorial-review-protocol.md:144`; `docs/_old/toolset-architecture.md:27,30,157,190,196,208,229`; `docs/_old/architecture.md:48,124`; `docs/_old/rule-template.md:204`; `docs/_old/2026-05-18-mechanical-first-rewrite/rule-template.md:111` — all archived; tombstoned with the `_old/` move.

**Consumers (FLAGGED):**
- Canon-index says "36 cites resolved in Stage 1". Total LIVE §7.3 cites enumerated above is approximately 60+ unique lines across atu-method live + workspace CLAUDE.md + memory. The "36" count is for the rot-list, not for all live cites — flag terminology precision: "36 cites resolved" ≠ "36 cites exist". Cite-density is higher than the row implies; the row's claim is faithful in spirit (the rot-list-bounded subset) but might mislead.
- `docs/05-status/deployment-status.md:21` matched in Grep but content omitted by truncation flag. Verifier could not paste verbatim line. Re-read needed to confirm §7.3 usage. Flagged.
- `scholarship/bofm/R6.md:129` matched in Grep but content omitted by truncation flag. Same — re-read needed.
- `project_bofm_substrate_quality.md:10` truncated, same flag.
- `docs/01-normative/framework.md:114` matched in Grep but content was omitted by `[Omitted long matching line]`. This is the §2.2:114 line area, possibly a §7.3 footnote/cross-ref. Re-read needed to confirm.
- The user-wide file `~/.claude/CLAUDE.md` has NO `§7.3` cites — canon-index row says "across CLAUDE.md, MEMORY.md, scholarship, memories, ~/CLAUDE.md". The "~/CLAUDE.md" component is the user-home-workspace `C:/Users/bibleman/CLAUDE.md` (5 cites), NOT the user-wide `C:/Users/bibleman/.claude/CLAUDE.md` (0 cites). The row's wording "~/CLAUDE.md" is ambiguous between the two CLAUDE.mds in Stan's stack; the user-wide file is empty for §7.3, the user-home file is rich. Flag for Stan's terminology disambiguation.

## §7.4 Audit-skippable categories

**Home:** `docs/01-normative/framework.md:299-307` (live)
> ### §7.4 Audit-skippable categories
>
> All of the following MUST hold for a proposal to bypass audit:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:299`: `### §7.4 Audit-skippable categories` (definition)
- `docs/01-normative/framework.md:312`: `- `Audit-skippable per §7.3 ([reason])` with the reason citing one of §7.4 categories; OR`
- `docs/04-process/retraction-log-protocol.md:56`: `- Logging a retraction is itself audit-skippable per `change-protocol.md` §7.4 (defensibility-capture; the retraction event was prior).`
- `canon-index.md:126`: row entry.
- `canon-index.md:240`: `... §7.4 audit-skippable (cross-reference updates) — partly; some entries are claim repoints that go through §7.3 ...`
- `canon-index.md:241`: `... §7.4 audit-skippable ...`
- `docs/_old/_index.md:42`: `... A pure-navigation index update (this file) is audit-skippable per §7.4.` (archived)
- `docs/_old/change-protocol.md:52`: `## §7.4 Audit-skippable categories` (archived home)
- `docs/_old/change-protocol.md:65`: `- `Audit-skippable per §7.3 ([reason])` with the reason citing one of §7.4 categories; OR` (archived)
- `docs/_old/retraction-log-protocol.md:63`: `... audit-skippable Category A operation (per `change-protocol.md` §7.4) ...` (archived)
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:53,66`: archived.

**Consumers (FLAGGED):**
- Canon-index says "retraction-log-protocol.md + Batch A1/A2/A3/A4 commit-message audit-evidence declarations". The "Batch A1/A2/A3/A4 commit-message" claim is in git-log space and not greppable from disk. Verifier cannot ground-truth these without `git log`. Flag for Stan/audit-runner: receipt of commit-message §7.4 declarations not provided by this disk-only verification. NOT a disposition defect, but a verification-completeness flag.

## §7.5 Audit-evidence in commit messages

**Home:** `docs/01-normative/framework.md:308-316` (live)
> ### §7.5 Audit-evidence in commit messages
>
> Every commit message that touches a per-corpus canon MUST declare audit-status explicitly:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:308`: `### §7.5 Audit-evidence in commit messages` (definition)
- `.claude/projects/C--Users-bibleman/memory/feedback_claude_commits_and_pushes.md:33`: `- **Audit-evidence keyword** — atu-method enforces this via change-protocol.md §7.5. Every commit touching canon must declare `Audit-skippable per §7.3 (<reason>)` or `Audit dispatched: <evidence>`. readers-bofm has a commit-msg hook that enforces the keyword for canon-extension patterns; check `.git/hooks/commit-msg` before assuming you can skip.`
- `.claude/projects/C--Users-bibleman/memory/feedback_claude_commits_and_pushes.md:40`: `3. **Compose the commit message** following the repo's pattern (title format, body, audit-evidence, co-author footer). For atu-method specifically, audit-evidence is mandatory per §7.5.`
- `.claude/projects/C--Users-bibleman/memory/feedback_never_skip_audit_gate.md:37`: `7. Commit with §7.5 audit-evidence in the message.`
- `canon-index.md:127`: row entry.
- `docs/_old/change-protocol.md:61`: `## §7.5 Audit-evidence in commit messages` (archived)
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:62`: archived.

**Consumers (FLAGGED):**
- Canon-index claims "all Stage 1 / Track A commit messages" — same shape as §7.4: git-log-only assertion not ground-truthed by disk grep. Verification-completeness flag.
- Canon-index also names `feedback_claude_commits_and_pushes.md` + `feedback_never_skip_audit_gate.md`. Both confirmed above. Faithful.

## §7.6 Self-test before commit

**Home:** `docs/01-normative/framework.md:317-326` (live)
> ### §7.6 Self-test before commit
>
> Before committing a canon change, run the five-question self-test:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:317`: `### §7.6 Self-test before commit` (definition)
- `canon-index.md:128`: row entry.
- `docs/_old/_index.md:24`: archived index cite (includes "§7.6 self-test before commit").
- `docs/_old/change-protocol.md:70`: `## §7.6 Self-test before commit` (archived).
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:71`: archived.
- `work/claudit/citation-rot-list-post-stage1.md:71`: enumerated in the rot-list-post-stage1 token list (no individual cite line).

**Consumers (FLAGGED):**
- Canon-index says "(no direct rot-list cites; structural-anchor; consumed by §7.5 commit-message construction)". Confirmed — no live §7.6 cites in `scholarship/`, `memories/`, or reader CLAUDE.mds outside the archived `_old/` paths. Faithful.

## §7.7 Self-consistency audit trigger

**Home:** `docs/01-normative/framework.md:327-336` (live)
> ### §7.7 Self-consistency audit trigger
>
> When a session adds ≥2 new canon subsections, rules, or merge-overrides, run a light self-consistency audit before wrap:

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:327`: `### §7.7 Self-consistency audit trigger` (definition)
- `.claude/projects/C--Users-bibleman/memory/feedback_compaction_resume_protocol.md:54`: `5. **Self-report briefly before responding.** One short paragraph confirming what was recovered (e.g., "Recovered: SSC three-tier promotion just landed; cognitive-ur-text framing under careful-scope discipline; bidirectional ATU test codified in atu-method §1.1; in-flight: rhetorical-structure §7.7 just added"). Do not pad — the report exists to confirm context-recovery, not to summarize.`
- `canon-index.md:129`: row entry.
- `docs/_old/_index.md:24`: archived index cite.
- `docs/_old/change-protocol.md:80`: `## §7.7 Self-consistency audit trigger` (archived).
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:82`: archived.

**Consumers (FLAGGED):**
- The `feedback_compaction_resume_protocol.md:54` cite is an **example string inside a self-report illustration** — it is not a regulative cite of §7.7 ("apply this trigger") but a pretend-quote of past recovery prose mentioning §7.7. The canon-index "(1 cite)" is technically correct on token count but semantically thin. The row faithfully describes this as the sole cite; flagged for completeness — there is no operational consumer of §7.7 in live scholarship/memories.

## §7.8 Proposed-rule adoption protocol

**Home:** `docs/01-normative/framework.md:337-351` (live)
> ### §7.8 Proposed-rule adoption protocol
>
> A rule labeled *proposed* is a rule awaiting corpus verification. "Proposed" is a testable state, not a hedging license.

**Live-successor:** n/a (this IS the live anchor).

**Consumers (verified):**
- `docs/01-normative/framework.md:337`: `### §7.8 Proposed-rule adoption protocol` (definition)
- `scholarship/bofm/R28.md:53`: `Adoption per §7.8: 27/28 clean (96.4%) — well above the 80% adoption threshold. ...`
- `scholarship/bofm/R28.md:87`: `R28 was proposed on 2026-04-19 and adopted to Active status on 2026-05-10 via a 27-instance corpus sweep (§7.8). ...`
- `scholarship/bofm/R28.md:115`: `... Adoption per §7.8 cleared the 80% threshold (96.4% clean). Status moved from Proposed to Active.`
- `scholarship/bofm/R28.md:151`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.4 J3 (speech-act announcement structural justification), §1.7 (decision procedure), §7.8 (proposed-rule adoption protocol)`
- `scholarship/bofm/R27.md:49`: `The 71/29 distribution at codification time was not yet a clean adoption signal per framework §7.8 (≥80% clean categorization required). ...`
- `scholarship/bofm/R27.md:105`: `... The rule was codified as **proposed** pending corpus-wide sweep verification (framework §7.8 — adoption requires ≥80% clean categorization).`
- `scholarship/bofm/R27.md:135`: `... but the formal status-promotion (proposed → active) per §7.8 awaits documented ≥80% clean-categorization evidence in the commit record.`
- `scholarship/bofm/R27.md:139`: `### Adoption per framework §7.8`
- `scholarship/bofm/R27.md:141`: `The rule remains **proposed**. Framework §7.8 requires the first corpus sweep to produce ≥80% clean categorization ...`
- `scholarship/bofm/R27.md:172`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle), §1.3 (camera-angle test), §1.4 (J1, J5), §7.8 (proposed-rule adoption protocol); ...`
- `memories/feedback_three_anti_default_factors.md:25`: `Source: `change-protocol.md` §7.3 trigger #3 (spot-check-based proposals) + §7.8 (≥80% adoption threshold).`
- `memories/feedback_rule_proposal_gates.md:33`: `- Full corpus with ≥80% clean categorization → adoption threshold met (per §7.8)`
- `memories/feedback_rule_proposal_gates.md:57`: `... `change-protocol.md` §7.3 / §7.8 (audit triggers + adoption threshold).`
- `canon-index.md:130`: row entry.
- `docs/_old/_index.md:24`: archived index cite.
- `docs/_old/change-protocol.md:90`: `## §7.8 Proposed-rule adoption protocol` (archived).
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:92`: `## §7.8 Proposed-constraint adoption protocol` (archived; semantic drift "rule"→"constraint" but same anchor).
- `docs/_old/framework.md:367`: archived reference.

**Consumers (FLAGGED):**
- Canon-index "(4 rot-list cites)" — live grep shows ≥8 live cites across R27/R28/feedback files (R28.md ×4, R27.md ×6, feedback_three_anti_default_factors.md ×1, feedback_rule_proposal_gates.md ×2). Same shape as §7.3 flag: "rot-list cites" is a constrained subset; live cite count is higher. Row content is faithful in spirit (the rot-list-bounded subset) but underplays live density. Flag for terminological precision.

## §7.9 Binding-rule design checklist

**Home:** `docs/01-normative/framework.md:352-362` (live)
> ### §7.9 Binding-rule design checklist (per-rule additions)
>
> Adding or modifying a binding rule MUST also:

**Live-successor:** n/a (this IS the live anchor; PRESERVED from prior live `framework.md §7`).

**Consumers (verified):**
- `docs/01-normative/framework.md:352`: `### §7.9 Binding-rule design checklist (per-rule additions)` (definition)
- `canon-index.md:118`: `(Categories A/B/C) plus §7.9 preserving prior live §7 binding-rule design checklist.`
- `canon-index.md:131`: row entry.
- `work/claudit/citation-rot-list-post-stage1.md:71`: enumerated in token list.
- `docs/_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:110`: `## §7.9 Architecture-method alignment check` (archived — DIFFERENT semantic content; archived §7.9 was an "architecture-method alignment check", live §7.9 is "binding-rule design checklist"). Same anchor ID, repurposed body in Stage 1.
- `docs/_old/2026-05-18-mechanical-first-rewrite/canon-validator-alignment-protocol.md:49`: `- **Producer-vs-constraint framing.** ... covered by the periodic architecture-method alignment check (`change-protocol.md` §7.9).` (archived; cites the OLD §7.9 semantics, not the live one).

**Consumers (FLAGGED):**
- **Anchor reuse — live §7.9 semantic ≠ archived §7.9 semantic.** Archived `_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:110` defined §7.9 as "Architecture-method alignment check"; live `docs/01-normative/framework.md:352` defines §7.9 as "Binding-rule design checklist". Any consumer pointer to "§7.9" written against the archived semantics is **silently semantically broken** in the live world. The `_old/canon-validator-alignment-protocol.md:49` cite is the demonstration: it cites §7.9 expecting the architecture-method-alignment-check semantics, which is no longer at §7.9. Canon-index row says "(no direct cites; preserves prior live `framework.md §7`)" — but it does NOT flag the §7.9 semantic-collision against the rewrite-stage archived §7.9. Surface to Stan: archived `_old/2026-05-18-mechanical-first-rewrite/` material reads as "current" to a naive grep, and §7.9's anchor was repurposed across the rewrite-stage. The `canon-validator-alignment-protocol.md` is archived and tombstoned, so the impact is contained, but the canon-index row's "(no direct cites)" claim glosses the archived-but-still-on-disk citer.
- Canon-index says §7.9 has no direct cites — confirmed for `scholarship/` and `memories/` live grep. Faithful in scope.

---

**Verifier summary (delivered as part of the receipt schema):**

- Part A (§0.x): 4 rows verified. All four §0.x sub-anchors archived in `_old/framework.md`; consumers cite via the umbrella `§0` token at BoFM:26 + GNT:29 (the "pointer-block" lines), NOT via verbatim `§0.1` / `§0.2` / `§0.3` / `§0.4` tokens. R20.md and R23.md cites were repointed to `§1` in Batch A1 and no longer carry §0.x tokens. feedback_rhetoric_bandwagon's connection to §0.3 is thematic (line 13) and in semantic *tension* (psycholinguistic-cognitive vs §0.3's not-derived-from-cognitive-theory), not a §-token cite.
- Part C-bis (§7.x): 10 rows verified. All live in `docs/01-normative/framework.md:237-362`. Cite density audit:
  - §7.0 — multiple live cites confirmed (framework, cross-corpus-principles, EP-1, canon-index hard-constraints).
  - §7.1 — structural anchor, zero operational consumers (faithful to row).
  - §7.2 — R20.md:33 confirmed; "1 other rot-list cite" not located on disk via Grep.
  - §7.3 — extensive cite forest: ≥60 unique live lines across atu-method/{docs,scholarship,memories,atu_method/hooks,README}, workspace `C:/Users/bibleman/CLAUDE.md` (5 cites), reader-repo CLAUDE.mds (3 cites), and `.claude/projects/.../memory/` (40+ cites). Row's "36 cites" reflects rot-list bound, not live cite count.
  - §7.4 — `retraction-log-protocol.md:56` confirmed; commit-message Batch A1-A4 declarations not ground-truthable from disk (git-log space).
  - §7.5 — `feedback_claude_commits_and_pushes.md:33,40` and `feedback_never_skip_audit_gate.md:37` confirmed; commit-message Stage-1 declarations same git-log flag as §7.4.
  - §7.6 — no operational consumers; structural-anchor only. Faithful.
  - §7.7 — sole consumer is a pretend-quote example string in `feedback_compaction_resume_protocol.md:54`, not a regulative cite. Effectively zero operational consumers.
  - §7.8 — ≥8 live cites across R27.md, R28.md, feedback_three_anti_default_factors.md, feedback_rule_proposal_gates.md. Row's "4 rot-list cites" underplays live density (same shape as §7.3 flag).
  - §7.9 — **semantic-collision flag**: live §7.9 = binding-rule design checklist; archived rewrite-stage §7.9 = architecture-method alignment check. Same anchor, different body. Archived `canon-validator-alignment-protocol.md:49` cites the OLD semantics. Contained-impact (archived path) but row does not flag this.

Cross-cutting flags surfaced for the audit:
1. §0.1/§0.4 consumer claims at R20/R23 are POST-repoint (now `§1`) — row's notation "(repointed in Batch A1)" is faithful; verifier confirms.
2. §0.x cites in BoFM/GNT canons go through umbrella `§0` only; no verbatim §0.1/§0.2/§0.3/§0.4 tokens on disk.
3. §0.3's only "consumer" in feedback_rhetoric_bandwagon is in *semantic tension* with the §0.3 claim, not aligned with it.
4. §7.x "rot-list cite" counts (§7.2, §7.3, §7.8) consistently underplay live cite density — row terminology could mislead a reader skimming for total impact.
5. §7.4 and §7.5 "commit-message" cite claims are git-log-space and not ground-truthed by disk grep.
6. §7.7's "1 cite" is a self-report example string, not a regulative consumer.
7. §7.9 anchor was repurposed in Stage 1; archived material at `_old/2026-05-18-mechanical-first-rewrite/canon-validator-alignment-protocol.md:49` carries a now-semantically-stale §7.9 cite.
8. `docs/05-status/deployment-status.md:21`, `scholarship/bofm/R6.md:129`, `project_bofm_substrate_quality.md:10`, `docs/01-normative/framework.md:114` matched §7.3 grep but content was elided by the truncation flag — these lines are §7.3 hits but verifier could not paste verbatim from this verification cycle.


# Lane 2 — §1.1 + §1.2 family

All §1.2.x consumers verified. Now I have all the receipts needed. Let me produce the structured output:

## §1.1 Generative principle

**Home:** `docs/_old/framework.md:47-65`
> `## §1.1 Generative principle`
> ``
> `**Each proposition splits by default.**`

**Live-successor:** `docs/01-normative/cross-corpus-principles.md §1.1` (line 63)
> `## §1.1 Generative principle — candidate-ATU substrate`

**Consumers (verified):**
- `scholarship/bofm/R20.md:126`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1 (atomic-thought mission), §1.1 (generative principle — each proposition splits by default), §1.4 J1-J5 (the five structural justifications — referenced by Exemption 4), §1.5 M3 (bare-governor indivisibility — related "fragment fails atomic-thought" failure mode)`
- `scholarship/bofm/R21.md:21`: `This is one of the framework's "non-predicated unit that functions as atomic thought via formal-structural recoverability" cases — except here the unit IS predicated, just non-finitely. R21 is therefore not a Structural Justification (J1–J5) extension of the generative principle; it is a direct application of the generative principle (§1.1: *each proposition splits by default*) to a participial proposition whose subject and predication are both morphologically present.` (NOTE: canon-index cites `:19`; actual hit is line 21 — off-by-2)
- `scholarship/bofm/R21.md:130`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle — each proposition splits by default), §1.5 M3 (bare-governor indivisibility — partner-partition with R21 over the participial space)`
- `scholarship/bofm/R27.md:172`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle), §1.3 (camera-angle test), §1.4 (J1, J5), §7.8 (proposed-rule adoption protocol); BoFM canon §3.5 Tier 5 (R7 yields-to R27), §3.5.1 (*that*-cluster precedence)`
- `scholarship/bofm/R27.md:105`: FLAGGED — Grep for §1.1 returned only lines 172 in R27.md. No §1.1 token at line 105.
- `scholarship/bofm/R6.md:17`: `The break is grammatical-structural rather than rhetorical: the *because*-clause has its own finite verbal nucleus (a finite verb under its embedded subject), its own subject (often co-referential with the matrix subject, but a fresh syntactic subject under the embedded predication), and its own complement structure. Each finite verbal nucleus is a candidate predication per the §1.1 generative principle; the *because* subordinator confirms the embedded clause's adverbial-causal function.`
- `scholarship/bofm/R6.md:30`: `R6 sits in the broader **finite-clausal-adverbial split** family with R7 (Purpose Clauses Break — *that* + MODAL) and the framework's §1.1 generative principle. The differentiation between R6 (causal) and R7 (purposive) is the mark inventory and the cognitive function (cause vs. telos), not a deeper structural difference. Both finite adverbial clauses earn their own atomic frame.`
- `scholarship/bofm/R7.md:17`: `The break is grammatical-structural rather than rhetorical: the *that*-clause has its own finite verbal nucleus (the modal aux + main verb), its own subject (often co-referential with the matrix subject, but a fresh syntactic subject under the embedded predication), and its own complement structure. Each finite verbal nucleus is a candidate predication per the §1.1 generative principle; the modal-auxiliary signature confirms finite predication.`
- `scholarship/bofm/R7.md:81`: `R7 sits in the broader **finite-clausal-adverrbial split** family with R6 (Causal Clauses Break — *because*) and the framework's §1.1 generative principle. Each finite adverbial clause earns its own atomic frame; the differentiation between R6 (causal) and R7 (purposive) is the mark inventory and the cognitive function (cause vs. telos), not a deeper structural difference.`
- `memories/feedback_atu_test_is_bidirectional.md:7`: `**Principle:** "Single cognitive bite" (framework §1.1) requires the line to stand on its own **referentially**, not just **grammatically**. ...`
- `memories/feedback_atu_test_is_bidirectional.md:25`: `1. **When evaluating a proposed line break:** run the bidirectional test, not just the forward one. Ask both (a) "is the proposition forward-closed on this line?" (existing §1.1) AND (b) "is this line referentially self-contained against upstream?" Both must pass for standalone-ATU status.`
- `memories/feedback_atu_test_is_bidirectional.md:43`: `6. **Cite §1.1 when invoking, not a merge-override mechanism.** A merge decision grounded in backward-anaphoric failure cites the bidirectional atomic-thought test at §1.1. ...`
- `memories/feedback_atu_test_is_bidirectional.md:49`: `- Codified at framework §1.1's tail (2026-05-13). All canons (BoFM, GNT, Tanakh) inherit this test through the §1.1 generative principle...`
- `memories/feedback_grammar_constrains_not_determines.md:14`: `**Why this memory exists:** Stan codified the principle verbatim 2026-05-13: ... Codified at framework §1.2's tail ("Constraint vs. determination — the asymmetry between §1.1 and §1.2").`
- `memories/feedback_rhetoric_figures_constrain_atu.md:8`: `**Principle.** Rhetorical figures of speech are CONSTRAINTS on the candidate-space of ATU breaks, NOT DETERMINANTS. Each figure has a default disposition that flows from its referential structure, but the atomic-thought test (§1.1, bidirectional) is the determination engine. ...`
- `memories/feedback_rhetoric_figures_constrain_atu.md:45`: `- Symmetric counterpart to [[grammar-constrains-not-determines]]: ... The §1.1 generative principle is the determination engine; §1.2 (grammar/formula integrity) and rhetoric-figures (this memory) are the two constraint layers.`
- `readers-bofm/1-method/colometry-canon.md:34` (BoFM pointer block): `**Pointer to framework.** The framework specification — generative principle (each proposition splits by default); three closed-list ways syntax forbids splits ...` — verified, pointer block at line 34.
- `readers-gnt/private/01-method/colometry-canon.md:48` (GNT pointer block): `**Pointer to framework.** The framework specification — generative principle (each proposition splits by default); ...` — verified, pointer block at line 48.
- `readers-gnt/scripts/audit_anaphoric_gen_abs_macula.py:6`: `bidirectional ATU test (framework §1.1, GNT canon §1).`

**Consumers (FLAGGED):**
- `scholarship/bofm/R27.md:105`: §1.1 token not present at line 105. Full-file grep for `§1.1` in R27.md returns only line 172. The canon-index citation `R27.md:105` is wrong for §1.1.
- `scholarship/bofm/R21.md:21`: Canon-index cites `R21.md:21`. Actual §1.1 hit is line 21 (verified — the "is therefore not a Structural Justification" line). Confirmed correct.
- `scholarship/bofm/R5.md:147`: Canon-index lists `R5.md:147` under §1.1 consumers. Line 147 reads: `- Universal framework: [...] §1.5 (merge-overrides — R5 is structurally parallel to M1 on the *or* coordinator), §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C — R5 is principled Category B)`. §1.1 token NOT present. Cite is wrong; R5.md contains no §1.1 reference (full-file grep returned no matches).

---

## §1.2 Syntax forbids splits (umbrella)

**Home:** `docs/_old/framework.md:67-81`
> `## §1.2 Syntax forbids splits (three closed-list ways)`
> ``
> `Syntax does not generate breaks. Syntax only vetoes them. A split that the generative principle would otherwise produce is forbidden when one of these three applies:`

**Live-successor:** null — `framework.md §1.2` does not exist as an umbrella section in live framework.md; per-sub-anchor dispositions only (per canon-index "see sub-anchors"). PARTIAL successor framing in `cross-corpus-principles.md §0.2` ("HOSTS: ... §1.3a (rhetoric figures constrain)") but §1.2 umbrella itself is null.

**Consumers (verified):**
- `scholarship/bofm/R12.md:149`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits), §1.5 M1 (Gorgianic bonded pair / verb-synonymy test), §1.9 (N=2 Adjudication Principle)`
- `scholarship/bofm/R10.md:132`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits — Layer 1 mid-phrase prohibitions), §1.4 J1 (compound-list-break-signals sub-rule — governs coordinate-object exclusion), §1.5 M1 (asymmetric-modifier sub-clause — governs Mosiah 18:7 third-item modifier), §1.9 (N=2 Adjudication / N=3+ cliff scope to predications, not objects)`
- `memories/feedback_grammar_constrains_not_determines.md:10`: `- **Atomic-thought SHOULD-go signals (generative principle + bidirectional test affirmation per `framework.md §1.2`):** "this break is justified because the next line carries a fresh proposition / camera angle / portrait beat / speech-act announcement / classical comma / substantive adjunct as own focus." The generative force is propositional, not grammatical.`
- `memories/feedback_grammar_constrains_not_determines.md:14`: `**Why this memory exists:** ... Codified at framework §1.2's tail ("Constraint vs. determination — the asymmetry between §1.1 and §1.2").`
- `readers-bofm/1-method/colometry-canon.md:34` (BoFM pointer block): verified — pointer block at line 34 enumerates "three closed-list ways syntax forbids splits (Layer 1 mid-phrase prohibitions, complement integrity, formula integrity)".
- `readers-gnt/private/01-method/colometry-canon.md:48` (GNT pointer block): verified — same pointer block prose at line 48.
- `readers-tanakh/scripts/archive/apply_formula_integrity_merge.py:2`: line 2 reads `# -*- coding: utf-8 -*-`. The §1.2 token does not appear there; the file content (formula-integrity merge) is conceptually §1.2.3-aligned but the canon-index citation `:2` is the file's encoding declaration, not a §1.2 reference. FLAGGED (line-number wrong OR conceptual-only cite without literal §-token).

**Consumers (FLAGGED):**
- `scholarship/bofm/R5.md:147`: Canon-index lists `R5.md:147` under §1.2 consumers ("syntax forbids splits"). Verified line 147: `§1.5 (merge-overrides...), §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C ...)`. §1.2 token NOT present. Full-file grep for `§1.2` in R5.md returns no matches. Cite is wrong.
- `readers-tanakh/scripts/archive/apply_formula_integrity_merge.py:2`: line 2 is the file encoding shebang-adjacent line (`# -*- coding: utf-8 -*-`); the file's docstring (lines 3-4) describes M1 bonded-pair/formula-integrity work but does not literally cite `§1.2`. Cite is conceptual, not literal — flag as line-number-target-not-a-§-token-bearing-line.

---

## §1.2.1 Layer 1 mid-phrase prohibitions

**Home:** `docs/_old/framework.md:71-72`
> `1. **Layer 1 mid-phrase prohibitions.** Splits mid-predication, mid-phrase, or mid-lexical-unit. The specific prohibitions are language-specific and live in each per-corpus repo's Layer 1 break-legality table (`data/syntax-reference/<language>-break-legality.md`). Universal pattern: line-final CCONJ seeking next member, DET seeking head, AUX seeking V, ADP seeking object, transitive V seeking DO, mid-vocative split, mid-fixed-unit split.`

**Live-successor:** null — no live §1.2.1 anchor in framework.md (per canon-index row: "no named live successor; per-corpus break-legality tables host").

**Consumers (verified):**
- `scholarship/bofm/R13a.md:49`: `- Universal framework: `atu-method/docs/01-normative/framework.md §1.2.1` (Layer 1 mid-phrase prohibitions)`
- `scholarship/bofm/R11.md:47`: `- Universal framework: `atu-method/docs/01-normative/framework.md §1.2.1` (Layer 1 mid-phrase prohibitions)`
- `scholarship/bofm/R16.md:112`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2.1 (Layer 1 mid-phrase prohibitions; line-final subordinator dangles forward), §1.2.3 (formula integrity)`
- `scholarship/bofm/R10.md:17`: `This is not preference. The object is an **obligatory argument** of the transitive verb's syntactic frame. Without the object NP, the transitive verb is not predicating anything complete. The framework treats this case under §1.2.1 (Layer 1 mid-phrase prohibitions): syntax does not generate breaks but vetoes them, and the verb-object bond is the canonical case where the veto fires absolutely.`
- `scholarship/bofm/R15.md:136`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2.1 (Layer 1 mid-phrase prohibitions — vocative integrity), §1.9 (N=2 Adjudication does NOT apply to appositional constructions including vocative+close-appositive)`

**Consumers (FLAGGED):**
- (none — all five sub-clause cites for §1.2.1 ground-truth on the exact lines named)

Additional unsolicited evidence: §1.2.1 also appears at `R16.md:19` (`The rule is one of the framework's Tier-2 indivisibility/formula/vocative cases (framework.md §1.2.1...`) and `R10.md:69` — not in canon-index but live in scholarship.

---

## §1.2.2 Layer 3 complement integrity

**Home:** `docs/_old/framework.md:73`
> `2. **Layer 3 complement integrity.** When a matrix verb's or adjective's valence is unsatisfied without its clausal complement (e.g., *he said that X*, *it is expedient that X*), the matrix is grammatically incomplete on its own; the complement must merge. Per-corpus rules implementing this principle are language-specific (see each canon's §5 — the verb classes that require complement-integrity merging differ by language).`

**Live-successor:** `framework.md §2.1:42`
> `... a verb whose content follows as a **clausal complement** — *regardless of whether it is a cognition, perception, or speech verb* — is forward-incomplete ("know/say *what?*") and **binds** its complement into one ATU: `οἶδα ὅτι` / "I know that X", and equally "I say to you [that] it is well…". The verb's open valency is filled by the complement; it does not stand alone. **So: clausal complement → matrix binds; distinct quoted performance (third-party direct discourse, parataxis) → frame stands.**`

**Consumers (verified):**
- `scholarship/bofm/R17.md:19`: `The apparatus's atomic-thought test, applied at the matrix-clause level, therefore mandates merge when the complement and matrix are on different lines. The rule is one of the framework's "syntax forbids splits" cases (`framework.md §1.2.2`): the matrix's valence is unsatisfied without its clausal complement, and a split that fragments the matrix from its complement violates the syntactic floor.`
- `scholarship/bofm/R26.md:165`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2.2 (syntax forbids splits — complement integrity), §1.5 M2 (verb-object clause-nucleus bond, alias of complement-integrity); BoFM canon §3.5 Tier 3 (Complement integrity), §3.5.1 (the *that*-cluster sub-hierarchy)`

**Consumers (FLAGGED):**
- (none — both cites ground-truth on the named lines)

Additional unsolicited: §1.2.2 also at `R26.md:19` (parallel framing line) — not enumerated in canon-index.

---

## §1.2.3 Layer 3 formula integrity

**Home:** `docs/_old/framework.md:75`
> `3. **Layer 3 formula integrity.** Lexicalized multi-word frames function as single units. Per-corpus rules implementing this principle are language-specific (formula content varies — BoFM has *And it came to pass*; Tanakh has wayyiqtol formulae; GNT has *καὶ ἐγένετο*).`

**Live-successor:** null — no live §1.2.3 anchor in framework.md (per canon-index row: "no named live successor; per-corpus formula bodies host").

**Consumers (verified):**
- `scholarship/bofm/R1.md:69`: `The sibling GNT canon's rule on *καὶ ἐγένετο* formula integrity, and Tanakh's rule on wayyiqtol narrative formulas, are sister instantiations of the same universal formula-integrity principle (see `framework.md §1.2.3`). Each per-corpus canon enumerates its own formula inventory because formulas are language-specific lexical bundles; the universal principle is consistent across canons.`
- `scholarship/bofm/R1.md:106`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2.3 (formula integrity)`

**Consumers (FLAGGED):**
- (none — both cites ground-truth on the named lines)

Additional unsolicited: §1.2.3 also at `R1.md:17` ("syntax-veto case under framework.md §1.2.3") and `R1.md:99` (speculative future), `R16.md:19` and `R16.md:112` (joint with §1.2.1) — not all enumerated in canon-index but live.

---

## Summary of gap flags

1. **`R27.md:105` for §1.1** — §1.1 token NOT present at line 105 (full-file grep returns only line 172). Canon-index cite is wrong.
2. **`R5.md:147` for §1.1** — line 147 cites §1.5, §1.9, §2 (no §1.1). Full-file grep for §1.1 in R5.md returns no matches. Canon-index cite is wrong.
3. **`R5.md:147` for §1.2** — same line 147 has no §1.2 token. Full-file grep for §1.2 in R5.md returns no matches. Canon-index cite is wrong.
4. **`readers-tanakh/scripts/archive/apply_formula_integrity_merge.py:2` for §1.2** — line 2 is the encoding shebang (`# -*- coding: utf-8 -*-`); no literal §1.2 token at or near line 2. The docstring at lines 3-4 describes M1/formula-integrity work conceptually but does not cite §1.2 literally. Either the line number is wrong or the cite is "conceptual citation, not literal §-token presence" — flag for claudit ruling.
5. **`R21.md:21` consumer cited as `R21.md:21`** — verified correct (line 21 carries the §1.1 cite). Mentioned for completeness; not a gap.


# Lane 3 — §1.3 + §1.3a + §1.4 (J1-J5 + sub-clauses)

```
## §1.3 camera-angle

**Home:** docs/_old/framework.md:83-89
> 83: `## §1.3 Image sharpens ambiguous proposition boundaries`
> 85: `**Camera-angle test (DEPRECATED — see caveat).** When proposition-first is ambiguous, ask: does the mind's eye reposition between candidate frames? Camera-angle shift → SPLIT. No shift → MERGE.`
> 87: `**Caveat (added 2026-05-13).** The camera-angle diagnostic is DEPRECATED in favor of the bidirectional atomic-thought test (§1.1 refinement; …)` [continues]

**Live-successor:** null — verified by Grep across `docs/01-normative/framework.md` for `J1|J5|camera|1\.3|1\.4` returning zero hits. Live framework.md uses a new structure (§1 Purpose / §2 The criterion w/ §2.1 bidirectional + §2.2 explicit-marker) with NO J1-J5 or camera-angle content.

**Consumers (verified):**
- `scholarship/bofm/R27.md:105`: `Three-condition merge test (word count ≤8, subject continuity, no camera-angle shift), with the default direction SPLIT. The rule was codified as **proposed** pending corpus-wide sweep verification (framework §7.8 — adoption requires ≥80% clean categorization).`
- `scholarship/bofm/R27.md:172`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle), §1.3 (camera-angle test), §1.4 (J1, J5), §7.8 (proposed-rule adoption protocol); BoFM canon §3.5 Tier 5 (R7 yields-to R27), §3.5.1 (*that*-cluster precedence)`
- `scholarship/gnt/R25.md:131`: `The 3-condition merge test itself, the word-count threshold (≤8), the subject-continuity condition, and the camera-angle condition were all verified adversarially against Phase A candidates before application. No additional carve-outs or threshold adjustments were required by the audit.`
- `readers-bofm/1-method/colometry-canon.md:34`: `**Pointer to framework.** The framework specification … image diagnostic (camera-angle test); five structural justifications J1–J5 …` [full line at offset 34]
- `readers-bofm/1-method/colometry-canon.md:201`: `- Single-image / camera-angle diagnostic (image-test)`
- `readers-bofm/1-method/colometry-canon.md:1959`: `**Rule.** A consecutive-result clause … (3) no camera-angle shift occurs across the boundary (single-image diagnostic passes). …`
- `readers-gnt/private/01-method/colometry-canon.md:48`: `**Pointer to framework.** … image diagnostic (camera-angle test); five structural justifications J1–J5 …`
- `readers-gnt/private/01-method/colometry-canon.md:1171`: `3. **No camera shift** — no new scene participant or viewpoint pivot is introduced by the result clause.`
- `readers-gnt/private/01-method/colometry-canon.md:1181`: `    no_camera_shift: true`
- `atu-method/memories/feedback_camera_angle_diagnostic_demote.md:8`: `**Principle.** The "camera-angle shift" diagnostic — described in framework §1.3 as a TIEBREAKER alongside single-image (and listed in §1.6 precedence tier-matrix as DIAGNOSTIC) — has been used in session to JUSTIFY splits that would otherwise fail the atomic-thought test. …`
- `atu-method/memories/feedback_camera_angle_diagnostic_demote.md:26`: `4. **Framework-edit (this memory's load-bearing artifact):** framework §1.3 should be updated to caveat camera-angle as "deprecated; redundant with bidirectional atomic-thought test under §1.1 refinement …`
- `atu-method/memories/feedback_camera_angle_diagnostic_demote.md:35`: `(Codified 2026-05-13 from Stan-verbatim observation during R7 motion-verb purpose-INF audit wave. Framework §1.3 + §1.6 edit pending.)`

**Consumers (FLAGGED):**
- `scholarship/bofm/R28.md (multiple)`: NO matches for `camera-angle` OR `§1.3` in R28.md. Closest is `R28.md:21` and `:151` which cite §1.4 J3, NOT §1.3 camera-angle. The audit row's claim that R28.md is a §1.3 consumer fails ground-truth — R28.md cites §1.4 J3 only.

---

## §1.3a rhetoric figures constrain

**Home:** docs/_old/framework.md:89-104
> 89: `## §1.3a Rhetoric and ATU — figures constrain, atomic-thought determines`
> 91: `**Principle (added 2026-05-13).** Rhetorical figures (hendiadys, merism, parallelism, chiasm, anaphora, climax, etc.) have DEFAULT ATU dispositions that flow from their referential structure — but they never independently DETERMINE ATU boundaries. …`
> 93-101: list of figure → default dispositions (hendiadys / merism / parallelism / chiasm / anaphora / climax)

**Live-successor:** null — Grep across `docs/01-normative/framework.md` returned zero hits for rhetoric/figures content; live framework restructure has no §1.3a successor.

**Consumers (verified):**
- (none of the audit-claimed consumers ground-truthed)

**Consumers (FLAGGED):**
- `atu-method/memories/feedback_rhetoric_figures_constrain_atu.md` (audit row claims **6 cites** to §1.3a): full file Read returns ZERO occurrences of `§1.3a`. The file cites `framework.md §1.1` (line 8 references §1.1) and `framework.md §1.2` (lines 12, 13, 16) — never §1.3a. Six §1.2 / §1.1 cites exist; the audit row appears to misattribute these to §1.3a.
- `atu-method/memories/feedback_rule_proposal_gates.md`: NO match for `§1.3a`. Closest content (line 11): `Am I citing a surface feature (UD signature, rhetorical figure, punctuation, lexical pattern) as evidence?` — a generic rhetoric-as-surface-feature mention, NOT a §1.3a cite.
- `atu-method/memories/feedback_no_fake_dilemmas.md`: NO match for `§1.3a`. Closest (line 36): `- `feedback_rhetoric_bandwagon.md` — meta-audit failure mode (judgment-handoff smuggling section)` — pointer to the bandwagon memory, NOT a §1.3a cite.
- `readers-bofm/1-method/colometry-canon.md` Tier 0 mentions: not located by direct Grep within the offsets exercised; flagged as not ground-truthed in this verification pass (no specific line was supplied for the Tier 0 claim, and a Grep for `§1.3a` against the canon would be required to confirm).

---

## §1.4 umbrella (Five Structural Justifications closed list)

**Home:** docs/_old/framework.md:106-164
> 106: `## §1.4 The Five Structural Justifications (closed list)`
> 108: `Non-predicated units that function as atomic thoughts via formal-structural recoverability. The reader reconstructs "who did what" because formal markers in the text make the missing predicate recoverable.`
> 110: `The list is extensible only by worked corpus example + adversarial validation. A proposed sixth justification MUST demonstrate (a) that it is a genuinely distinct instance of the same generating principle, and (b) that it survives an adversarial challenge.`

**Live-successor:** null — no J1-J5 / §1.4 token in live `docs/01-normative/framework.md`.

**Consumers (verified):**
- `scholarship/bofm/R20.md:126`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1 (atomic-thought mission), §1.1 (generative principle — each proposition splits by default), §1.4 J1-J5 (the five structural justifications — referenced by Exemption 4), §1.5 M3 (bare-governor indivisibility — related "fragment fails atomic-thought" failure mode)`
- `scholarship/bofm/R27.md:172`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle), §1.3 (camera-angle test), §1.4 (J1, J5), §7.8 (proposed-rule adoption protocol); BoFM canon §3.5 Tier 5 (R7 yields-to R27), §3.5.1 (*that*-cluster precedence)`
- `readers-bofm/1-method/colometry-canon.md:34`: `**Pointer to framework.** … five structural justifications J1–J5 (formally-marked parallel series, portrait accumulation, speech-act announcement, classical commata, substantive adjunct) …`
- `readers-gnt/private/01-method/colometry-canon.md:48`: `**Pointer to framework.** … five structural justifications J1–J5 …`
- `readers-bofm/1-method/colometry-canon.md:487`: `4. *Or*-coordinations functioning as compound objects under a shared verb or preposition (J1 compound-list members) → §1.4 J1 governs the head-and-object analysis; if the compound list reads as J1 series, R5 yields. The N=3+ cliff (§1.9) does not engage R5 because R5 fires only on N=2 *or*-pairs.`
- `readers-bofm/1-method/colometry-canon.md:1581`: `1. Bare participial without its own subject (subject-inheriting from matrix) — out of scope; routes to M3 (bare-governor indivisibility, framework §1.5 M3) including M3's bare-trailing-participial extension.` — NOTE: this line cites §1.5 M3, NOT §1.4. The audit's BoFM-canon:1581 cite as §1.4 consumer is mis-attributed.
- `readers-bofm/1-method/colometry-canon.md:2056`: `3. Result-clause internal structure firing J5 substantive adjunct or J1 parallel series — those breaks fire INSIDE the merged unit and are NOT excluded from R27; R27's outer-boundary verdict (merge) stands → framework `§1.4``
- `readers-bofm/1-method/colometry-canon.md:2653`: `**Framework anchor:** Corpus-specific operational instantiation of framework M4 (fragmented atomic thought-unit; see [`atu-method/docs/01-normative/framework.md §1.5`](docs/01-normative/framework.md)).` — NOTE: cites §1.5 M4, NOT §1.4. Mis-attributed in audit row.
- `readers-bofm/1-method/colometry-canon.md:2727`: `2. **J1 stacked-coordinate-subject tail.** When line A is the final element of a parallel-series stack of coordinate subjects (per framework J1), the parallel-series convention wins. M4-BoFM-1 yields per the §1.5 M4 scope discipline (M4 is prospective, not retroactive against J1 series).`
- `readers-gnt/private/01-method/colometry-canon.md:56`: `- **J1 compound-list break signals — GNT extension: marked-coordinator climactic emphasis (5th signal).** Framework §1.4 J1 lists four compound-list-break signals …`
- `readers-gnt/private/01-method/colometry-canon.md:130`: `- **J3 named patterns (speech-act announcement) — GNT instantiations.** Direct speech introduction: `καὶ ἔλεγεν αὐτοῖς:` / `καὶ εἶπεν αὐτῷ:` — each is a complete speech-act predication. See §3.6 (R11) for the full treatment.`
- `readers-gnt/private/01-method/colometry-canon.md:132`: `- **J5 substantive adjunct — GNT canonical cases.**`
- `readers-gnt/private/01-method/colometry-canon.md:183`: `**Pointer to framework.** The five structural justifications (J1–J5) and four merge-override conditions (M1–M4), their generating principles, two-prong exception test, complete decision procedure, and the N=2 Adjudication Principle are codified at [`atu-method/docs/01-normative/framework.md §1.4–§1.9`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- `readers-gnt/private/01-method/colometry-canon.md:227-259`: this range spans the M1/M2/M3/M4 GNT-cases blocks (lines 227-258 captured above). These cite §1.5 M-overrides, NOT §1.4 J-justifications — verbatim line 227: `### M1 — Gorgianic Bonded Pair: GNT Cases`. The audit row's claim that 227-259 are a §1.4 consumer block is mis-attributed (this is the §1.5 M-override block).

**Consumers (FLAGGED):**
- `readers-bofm/1-method/colometry-canon.md:1581`: cites §1.5 M3, not §1.4. Mis-attributed.
- `readers-bofm/1-method/colometry-canon.md:2653`: cites §1.5 M4, not §1.4. Mis-attributed.
- `readers-gnt/private/01-method/colometry-canon.md:227-259`: this is the M1-M4 GNT-cases block (§1.5 territory), not §1.4. Mis-attributed.

---

## J1 — Formally-marked parallel series

**Home:** docs/_old/framework.md:112-126
> 112: `### J1 — Formally-marked parallel series`
> 114: `Members connected by formal markers (*and also*, *nor*, correlative particles, polysyndetic *and*, language-specific equivalents) where the shared predicate is recoverable from the parallel structure. Each member earns its own beat.`
> 116: `**Compound list break signals.** In a compound list governed by one preposition or verb, bare coordinate items (e.g., *"and [noun]"*) are compound objects and stay merged. A break inside a compound list is justified only when one of these signals is present:`

**Live-successor:** null (live framework.md has no J1 token).

**Consumers (verified):**
- `scholarship/bofm/R10.md:132`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits — Layer 1 mid-phrase prohibitions), §1.4 J1 (compound-list-break-signals sub-rule — governs coordinate-object exclusion), §1.5 M1 (asymmetric-modifier sub-clause — governs Mosiah 18:7 third-item modifier), §1.9 (N=2 Adjudication / N=3+ cliff scope to predications, not objects)`
- `scholarship/bofm/EP-5.md:174`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.4 J1 (formally-marked parallel series — the parallel-stacking interaction) + §1.9 N=2 Adjudication Principle and N=3+ cliff + §2 (Category B editorial-judgment)`
- `readers-bofm/1-method/colometry-canon.md:487`: `4. *Or*-coordinations functioning as compound objects under a shared verb or preposition (J1 compound-list members) → §1.4 J1 governs the head-and-object analysis; if the compound list reads as J1 series, R5 yields. The N=3+ cliff (§1.9) does not engage R5 because R5 fires only on N=2 *or*-pairs.`
- `readers-gnt/private/01-method/colometry-canon.md:56`: `- **J1 compound-list break signals — GNT extension: marked-coordinator climactic emphasis (5th signal).** Framework §1.4 J1 lists four compound-list-break signals (elided auxiliary + stacked participles / possessive restart / new demonstrative / attached relative clause). GNT adds a **fifth: marked-coordinator climactic emphasis on a final list-member**. …`
- `scholarship/bofm/R20.md:126`: (same line cited under §1.4 umbrella above) — verified.

**Consumers (FLAGGED):**
- None for J1 specifically.

---

## J1 4-signal sub-clause

**Home:** docs/_old/framework.md:116-123
> 116: `**Compound list break signals.** In a compound list governed by one preposition or verb, bare coordinate items (e.g., *"and [noun]"*) are compound objects and stay merged. A break inside a compound list is justified only when one of these signals is present:`
> 118-121: enumerated 4 signals: `1. **Elided auxiliary + stacked participles** … 2. **Possessive restart** … 3. **Demonstrative** … 4. **Attached relative clause** …`
> 123: `Without one of these signals, bare coordinate items merge.`

**Live-successor:** null.

**Consumers (verified):**
- `readers-bofm/1-method/colometry-canon.md:487`: cited verbatim above — appeals to J1 compound-list governance (does not enumerate the 4 signals at this line, but invokes the rule).
- `readers-gnt/private/01-method/colometry-canon.md:56`: enumerates the 4 signals verbatim then adds a 5th: `Framework §1.4 J1 lists four compound-list-break signals (elided auxiliary + stacked participles / possessive restart / new demonstrative / attached relative clause). GNT adds a **fifth: marked-coordinator climactic emphasis on a final list-member** …`
- `scholarship/bofm/R10.md:132`: cited verbatim above — `§1.4 J1 (compound-list-break-signals sub-rule — governs coordinate-object exclusion)`.

**Consumers (FLAGGED):**
- None.

---

## J2 — Portrait accumulation

**Home:** docs/_old/framework.md:127-129
> 127: `### J2 — Portrait accumulation`
> 129: `A set of attributes building one mental picture, sharing a copular or attributive frame from context. Applies only when the stack IS the portrait, not when it is a catalogue.`

**Live-successor:** null.

**Consumers (verified):**
- (none in audit scope)

**Consumers (FLAGGED):**
- None — no consumers were claimed for J2 in the row.

---

## J3 — Speech-act announcement

**Home:** docs/_old/framework.md:131-135
> 131: `### J3 — Speech-act announcement`
> 133: `Complete communicative predication introducing direct discourse. Announcement and quoted content are separate cognitive frames.`
> 135: `Per-corpus instantiations of this justification may name specific formula patterns (e.g., recurring speech-tag formulae in the language's literary register). Those named patterns are operational sub-clauses of J3 and are documented in the respective per-corpus canon §5.`

**Live-successor:** null.

**Consumers (verified):**
- `readers-bofm/1-method/colometry-canon.md:40`: `- **J3 named patterns** (operational sub-rules under speech-act announcement):` [followed by Verily-formula + saith-the-Lord sub-bullets at :41-42]
- `readers-gnt/private/01-method/colometry-canon.md:130`: `- **J3 named patterns (speech-act announcement) — GNT instantiations.** Direct speech introduction: `καὶ ἔλεγεν αὐτοῖς:` / `καὶ εἶπεν αὐτῷ:` — each is a complete speech-act predication. See §3.6 (R11) for the full treatment.`

**Consumers (FLAGGED):**
- `scholarship/bofm/EP-3.md (J3-routes)`: Grep for `J3` / `J1` / `J5` / `speech-act` / `route` (case-insensitive) returns ZERO `J3` matches in EP-3.md. The only J-token hits are J1 (lines 51, 70, 72, 74, 127, 178). The audit row's claim of EP-3.md as a J3-routes consumer fails ground-truth.

---

## J4 — Classical commata

**Home:** docs/_old/framework.md:137-139
> 137: `### J4 — Classical commata`
> 139: `Short fragmentary utterances carrying full communicative weight (typically 1-3 words). Brevity + isolation = deliberate emphasis.`

**Live-successor:** null.

**Consumers (verified):**
- (none in audit scope)

**Consumers (FLAGGED):**
- None — no consumers were claimed for J4.

---

## J5 — Substantive adjunct as own focus

**Home:** docs/_old/framework.md:141-164
> 141: `### J5 — Substantive adjunct as own focus`
> 143: `A fronted or trailing adjunct (temporal PP, locative PP, causal PP, etc.) that (a) is grammatically peripheral to the matrix predication's core truth AND (b) carries substantial content earns its own line.`
> 145: `**Grammatical grounding.** The target language treats peripheral adjuncts as syntactically detachable …`

**Live-successor:** null.

**Consumers (verified):**
- `readers-bofm/1-method/colometry-canon.md:43`: `- **J5 substantive-adjunct canonical case:** Alma 52:18 year-formula temporal PP (15-word filling of AICTP "when" slot). See §5 R23 (Date Colophon) for the year-formula operational signature.`
- `readers-gnt/private/01-method/colometry-canon.md:132`: `- **J5 substantive adjunct — GNT canonical cases.**`
- `readers-gnt/private/01-method/colometry-canon.md:133`: `  - *(Genitive absolute REMOVED from J5 — REVISED 2026-05-20: a gen abs is half an ATU and binds forward to its governing matrix per R19 §3.10a; it is not a J5 own-focus adjunct. Acts 1:9 `βλεπόντων αὐτῶν` binds into `ἐπήρθη`.)*`
- `readers-gnt/private/01-method/colometry-canon.md:134-136`: prep-catena / FEF periodic frame / John 1:1 fronted-temporal — all are J5 GNT instantiations.

**Consumers (FLAGGED):**
- `scholarship/bofm/EP-1.md:153`: cites `§1.5 J5` (line 153 verbatim: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §2.1 (punctuation has zero force) + §7.0 (Category B editorial-judgment) + §1.5 J5 (substantive adjunct as own focus — interaction)`). The audit row already flags this as MALFORMED — confirmed: J5 is in §1.4 of the home (line 141), not §1.5. EP-1.md cite mis-numbered.
- `scholarship/bofm/R26.md`: NO match for `§1.4` OR `J5` (case-sensitive) in R26.md. R26.md cites only `§1.2.2`, `§1.5 M2`, and BoFM canon §3.5 Tier 3 / §3.5.1. The audit row's claim of R26.md as a J5 consumer fails ground-truth — R26 is complement-integrity / M2 territory, not J5.

---

## J5 sub-clauses: degree-quantifier exclusion + same-slot diagnostic

**Home:** docs/_old/framework.md:148-152
> 148: `**Exclusion: degree quantifiers.** Short PPs that modify the *degree* of a predicate do NOT pass the slot-paraphrase test — they modify how-much, not when/where/why. Treat as predicate modifiers, not slot-fillers.`
> 150: `**Same-slot vs distinct-slot diagnostic (matrix-cumulation disambiguation).** When a short matrix predicate (≤10 words with finite verb) is followed by N≥3 adjunct lines each leading with a preposition / fixed MWPP (e.g., `even from`, `notwithstanding`, `according to`) / participial frame (`having…`, `being…`) / infinitival lead (`to declare…`), J5 surface-form risks colliding with J1 (formally-marked parallel series). The discriminator:`
> 152: continuation (uniform-type vs mixed-type bullets at 153-154).

**Live-successor:** null.

**Consumers (verified):**
- (no specific consumer cites supplied in the audit row for these sub-clauses)

**Consumers (FLAGGED):**
- None claimed; not flag-able.
```

---

**Summary of FLAGS surfaced for claudit:**

1. **§1.3 row — R28.md mis-cite:** R28.md cites §1.4 J3, NOT §1.3 camera-angle. The "R28.md (multiple)" entry in the §1.3 consumer list is mis-attributed.

2. **§1.3a row — feedback_rhetoric_figures_constrain_atu.md mis-cite (6 cites claim):** Full Read of the file returns zero `§1.3a` references. The file cites `framework.md §1.1` and `framework.md §1.2` (4 hits at lines 8/12/13/16). The "6 cites" appears to count §1.1/§1.2 citations and re-attribute them to §1.3a.

3. **§1.3a row — feedback_rule_proposal_gates.md and feedback_no_fake_dilemmas.md:** Neither file contains `§1.3a`. Generic "rhetorical figure" surface-mentions exist but are not §1.3a cites.

4. **§1.4 umbrella — three mis-attributions:** BoFM canon:1581 (cites §1.5 M3), BoFM canon:2653 (cites §1.5 M4), GNT canon:227-259 (M1-M4 GNT-cases block, §1.5 territory). All three are §1.5 M-override consumers, NOT §1.4 J-justification consumers.

5. **J3 row — EP-3.md J3-routes mis-cite:** EP-3.md has zero `J3` matches; its J-token consumers are all J1 (line 51 etc.). The "EP-3.md (J3-routes)" claim fails ground-truth.

6. **J5 row — EP-1.md:153 MALFORMED (audit already flagged):** confirmed — line 153 cites `§1.5 J5` but J5 lives in §1.4 of the home. The cross-cite is mis-numbered.

7. **J5 row — R26.md mis-cite:** R26.md contains zero `J5` and zero `§1.4` references. R26 is §1.2.2 / §1.5 M2 territory (complement integrity), not J5.

8. **Live successor across all rows:** confirmed null — live `docs/01-normative/framework.md` Greps for `J1|J5|camera|1\.3|1\.4` return ZERO hits. Live framework restructured to §1 Purpose / §2 The criterion (§2.1 bidirectional + §2.2 explicit-marker); J1-J5 / camera-angle / §1.3 / §1.4 anchors do not survive into the live canon.


# Lane 4 — §1.5 (M1-M4 + sub-clauses) + §1.6 + §1.7 + §1.8

## §1.5 umbrella — Four Merge-Override Conditions

**Home:** _old/framework.md:166-244 (actual path: `docs/_old/framework.md:166-244`)
> `## §1.5 The Four Merge-Override Conditions (closed list)`
> `**Symmetric counterpart to structural justifications.** Where structural justifications describe cases where the default (merge under propositions-first) is overridden to produce a split, merge-overrides describe cases where an apparent split-trigger is itself overridden...`

**Live-successor:** null — no live successor (verified by Grep across live `docs/01-normative/framework.md`: `§1\.5|§1\.6|§1\.7|§1\.8|Four Merge-Override|Decision procedure|Application order|four forces` → No matches found). The live `framework.md` has been rewritten without numbered §1.x sections that match these anchors.

**Consumers (verified):**
- `scholarship/bofm/R10.md:132`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits — Layer 1 mid-phrase prohibitions), §1.4 J1 (compound-list-break-signals sub-rule — governs coordinate-object exclusion), §1.5 M1 (asymmetric-modifier sub-clause — governs Mosiah 18:7 third-item modifier), §1.9 (N=2 Adjudication / N=3+ cliff scope to predications, not objects)`
- `scholarship/bofm/R5.md:147`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.5 (merge-overrides — R5 is structurally parallel to M1 on the *or* coordinator), §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C — R5 is principled Category B)`
- `scholarship/bofm/EP-1.md:153`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §2.1 (punctuation has zero force) + §7.0 (Category B editorial-judgment) + §1.5 J5 (substantive adjunct as own focus — interaction)` — **NOTE: cites "§1.5 J5" but J5 is in §1.4, not §1.5** (likely a typo / cross-section reference)
- `scholarship/bofm/R12.md:149`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits), §1.5 M1 (Gorgianic bonded pair / verb-synonymy test), §1.9 (N=2 Adjudication Principle)`
- `scholarship/bofm/R20.md:126`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1 (atomic-thought mission), §1.1 (generative principle — each proposition splits by default), §1.4 J1-J5 (the five structural justifications — referenced by Exemption 4), §1.5 M3 (bare-governor indivisibility — related "fragment fails atomic-thought" failure mode)`
- BoFM canon:34 pointer block: `readers-bofm/1-method/colometry-canon.md:34` → `**Pointer to framework.** The framework specification — generative principle...; four merge-overrides M1–M4 (Gorgianic bonded pair, verb-object clause-nucleus bond, bare-governor indivisibility, fragmented atomic thought-unit)...is codified at [`atu-method/docs/01-normative/framework.md §1`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- GNT canon:48 pointer block: `readers-gnt/private/01-method/colometry-canon.md:48` → `**Pointer to framework.** The framework specification...four merge-overrides M1–M4...is codified at [`atu-method/docs/01-normative/framework.md §1`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- BoFM canon:148-156 (TIER 4 block): `readers-bofm/1-method/colometry-canon.md:148` → `**TIER 4 — Default-merge precedence over split-triggers (M-overrides)**` (followed by M1-M4 enumeration through line 156)
- GNT canon:111-128 (M1 paraphrase-test scope block at 113-128): `readers-gnt/private/01-method/colometry-canon.md:113` → `- **M1 paraphrase-test scope: hendiadys AND merism (codified 2026-05-13).** Framework §1.5 M1 defines a bonded pair as N=2 coordinate members where the pair functions as "a single unified hendiadys or bonded rhetorical image."...`
- GNT canon:227-259 (M1/M2/M3/M4 cases blocks): `readers-gnt/private/01-method/colometry-canon.md:227` → `### M1 — Gorgianic Bonded Pair: GNT Cases` (sections through M4 at 251-258)

**Consumers (FLAGGED):**
- `scholarship/bofm/EP-1.md:153` cites "§1.5 J5" — but J5 is part of §1.4 (five structural justifications), not §1.5 (four merge-overrides). Section number mismatch.

---

## M1 — Gorgianic bonded pair

**Home:** _old/framework.md:176-203 (actual path: `docs/_old/framework.md:176-203`)
> `### M1 — Gorgianic bonded pair`
> `**Definition.** N=2 coordinate members joined by a coordinating particle where the pair functions as a single unified hendiadys or bonded rhetorical image — not two independent propositions...`

**Live-successor:** null — no live successor in `docs/01-normative/framework.md` (verified via Grep `M1|M2|M3|M4|merge-override` — only 2 hits, both meta-references about "merge-overrides" as concept).

**Consumers (verified):**
- `scholarship/bofm/R12.md:149`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2 (syntax forbids splits), §1.5 M1 (Gorgianic bonded pair / verb-synonymy test), §1.9 (N=2 Adjudication Principle)`
- `scholarship/bofm/R5.md:147`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.5 (merge-overrides — R5 is structurally parallel to M1 on the *or* coordinator)...`
- `scholarship/bofm/EP-5.md:50`: `- **N=2 virtue pairs** — *faith and hope*, *meek and lowly*, *chastity and virtue*, *faith and patience*. ~20-30 instances corpus-wide. N=2 routes to §1.9 N=2 Adjudication Principle (M1 synonymy test) before reaching EP-5; most resolve to M1 merge as cognate / bonded pairs.`
- `scholarship/bofm/EP-5.md:108`: `- **Risk: the rule could over-fire on N=2 cognate pairs.** Resolution: explicit interaction with §1.9 N=2 Adjudication Principle — N=2 pairs route to M1 synonymy test before EP-5 is consulted; EP-5 fires only on N≥3 stacks or on N=2 cases that M1 leaves unresolved.`
- `scholarship/bofm/R22.md:168`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.5 M1 (appositional constructions explicitly outside M1's N=2 scope), §1.9 (N=2 Adjudication Principle explicitly excludes appositives)`
- BoFM canon:38-39: `readers-bofm/1-method/colometry-canon.md:38` → `- **M1 bonded-pair list (verb pairs, corpus-attested):** ...M1 verb-pair protection fires only on N=2 verb-coordination per the N=2-only caveat in atu-method/docs/01-normative/framework.md §1.5. Detector reference: ...` and line 39 → `- **M1 nominal-pair canonical cases:** *grace and mercy*, *heaven and earth*, *dust and ashes*, ...`
- BoFM canon:148-156 (M1 listed in TIER 4): line 149 → `- **M1** Gorgianic Bonded Pair (N=2 synonymy/cognate/hendiadys merge)`
- GNT canon:111-128 (M1 paraphrase-test scope) — verified above; line 113 explicit `Framework §1.5 M1`

**Consumers (FLAGGED):** none for this row.

---

## M1 asymmetric-modifier sub-clause

**Home:** _old/framework.md:201 (actual: `docs/_old/framework.md:201`)
> `**Asymmetric-modifier sub-clause.** When an M1-candidate pair has one member carrying a PP modifier or relative clause the other lacks, M1 still wins → MERGE if the modifier attaches semantically to the pair AS A UNIT...`

**Live-successor:** null — no live successor (verified above).

**Consumers (verified):**
- BoFM canon:747: `readers-bofm/1-method/colometry-canon.md:747` → `4. The third (or final) item in a compound object list carrying a trailing PP modifier — when the modifier attaches semantically to the joint object-set, M1 asymmetric-modifier sub-clause (framework §1.5 M1) keeps the modified item bonded with its co-objects; R10 still merges the entire object-set with the shared verb`
- Additional consumer found: `scholarship/bofm/R10.md:56`: `- M1 asymmetric-modifier sub-clause (framework §1.5) treats the trailing PP *on the Lord* as semantically attaching to the joint object-set; the third item remains bonded with its co-objects.`

**Consumers (FLAGGED):** none.

---

## M2 — Verb-object clause-nucleus bond

**Home:** _old/framework.md:205-209 (actual: `docs/_old/framework.md:205-209`)
> `### M2 — Verb-object clause-nucleus bond`
> `This merge-override is an alias for the per-corpus complement-integrity rule (in BoFM canon, Rule 17; in GNT canon, Rule 8; in Tanakh canon, Rule H7)...`

**Live-successor:** null — no live successor.

**Consumers (verified):**
- `scholarship/bofm/R10.md` multiple §1.5 hits — but the M2 reference there is structural-citation only (line 132 just says §1.5 M1, no M2). Grepping for "M2" in R10.md:
- `scholarship/bofm/R26.md:165`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.2.2 (syntax forbids splits — complement integrity), §1.5 M2 (verb-object clause-nucleus bond, alias of complement-integrity); BoFM canon §3.5 Tier 3 (Complement integrity), §3.5.1 (the *that*-cluster sub-hierarchy)`
- BoFM canon:148-156 (M2 entry at line 151): `readers-bofm/1-method/colometry-canon.md:151` → `- **M2** = R17 (alias)`
- GNT canon:237 (M2 strict-application caveat at 237, but M2 section header at 239): `readers-gnt/private/01-method/colometry-canon.md:237` → `**M1 strict-application caveat:** When M1's bonded-pair grounds are withdrawn ("different semantic domains"), that does NOT by itself license a split. Before flipping to SPLIT, check: M2 (verb-object bond), M3 (bare-governor), M4 (fragmented atomic thought), R11 (speech-intro)...` — the M2 reference is at line 237, but the dedicated `### M2 — Verb-Object Clause-Nucleus Bond: GNT Cases` header is at line 239.
- Tanakh H7 — **does NOT exist in the live tanakh canon** (`readers-tanakh/private/01-method/colometry-canon.md` grep for `H7` → No matches found). H7 only exists in the archived legacy canon at `readers-tanakh/_archive/2026-05-18-mechanical-first-rewrite/colometry-canon.md:161`: `2. **Layer 3 complement integrity.** When the matrix verb's or adjective's valence is unsatisfied without its clausal complement — e.g., אָמַר ... כִּי / לֵאמֹר + speech content; יָדַע ... כִּי + content; צִוָּה ... אֲשֶׁר + complement — the matrix is grammatically incomplete on its own; the complement must merge unless one of the long-complement exceptions in §5 Rule H7 fires.`

**Consumers (FLAGGED):**
- "R10.md (multiple)" — Grep of R10.md for §1.5 hits found only line 56 (M1 asymmetric-modifier) and line 132 (§1.5 M1). **No M2 reference in R10.md.** Row's claim "R10.md (multiple)" for M2 is unsupported.
- "Tanakh H7" — H7 is **not in the live Tanakh canon**; only exists in the archived legacy canon (`_archive/2026-05-18-mechanical-first-rewrite/colometry-canon.md`). The framework §1.5 M2 home text at `_old/framework.md:207` still references "Tanakh canon, Rule H7" as the alias, but the live tanakh canon was mechanical-first-rewritten 2026-05-18 and no longer contains H7.
- "GNT canon:237" — line 237 is the M1 strict-application caveat that mentions M2 in passing. The actual M2 section header is at line 239. Off-by-2 on the cite.

---

## M3 — Bare-governor indivisibility

**Home:** _old/framework.md:211-230 (actual: `docs/_old/framework.md:211-230`)
> `### M3 — Bare-governor indivisibility`
> `**Definition.** A head word that cannot stand on its own line without at least one complement, object, or dependent — participial adjective functioning predicatively, governing participle awaiting content, discourse particle standing alone...`

**Live-successor:** null — no live successor.

**Consumers (verified):**
- `scholarship/bofm/R19.md:134`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.1 (generative principle — cataphoric splits), §1.5 M3 (bare-governor indivisibility — anaphoric merges), §2.1 (punctuation has zero force — motivates UPOS-gated proxy)`
- BoFM canon:152: `readers-bofm/1-method/colometry-canon.md:152` → `- **M3** Bare-Governor Indivisibility (extension: bare trailing participials)`
- BoFM canon:1581: `readers-bofm/1-method/colometry-canon.md:1581` → `1. Bare participial without its own subject (subject-inheriting from matrix) — out of scope; routes to M3 (bare-governor indivisibility, framework §1.5 M3) including M3's bare-trailing-participial extension.`
- GNT canon:237 (M3 referenced in M1 strict-application caveat) → `..., check: M2 (verb-object bond), M3 (bare-governor), M4 (fragmented atomic thought)...`
- GNT canon:245: `readers-gnt/private/01-method/colometry-canon.md:245` → `### M3 — Bare-Governor Indivisibility: GNT Cases`
- `scholarship/bofm/R20.md:126`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1 (atomic-thought mission), §1.1 (generative principle — each proposition splits by default), §1.4 J1-J5 (the five structural justifications — referenced by Exemption 4), §1.5 M3 (bare-governor indivisibility — related "fragment fails atomic-thought" failure mode)`
- `atu-method/memories/feedback_atu_test_is_bidirectional.md:43`: `6. **Cite §1.1 when invoking, not a merge-override mechanism.** A merge decision grounded in backward-anaphoric failure cites the bidirectional atomic-thought test at §1.1. Prior M3 (forward-dangling) and M4 (symmetric) merge-override mechanisms are deprecated under the bidirectional test framework (2026-05-17); backward-anaphoric is upstream of those, at the test itself.` — **NOTE: this memory explicitly marks M3/M4 as DEPRECATED under the bidirectional test framework, 2026-05-17.**
- `atu-method/memories/feedback_rule_proposal_gates.md:43`: `Anaphoric reference FAILS. Cataphoric reference (presentative + indefinite NP, "thus says X:") PASSES. Cite `framework.md §1.1` (not a merge-override mechanism — M3/M4 are deprecated under the bidirectional test framework, 2026-05-17) when invoking. The bidirectional test is INFORMATIONAL DIAGNOSTIC, not precedence override...`

**Consumers (FLAGGED):**
- Both memory files (`feedback_atu_test_is_bidirectional.md:43` and `feedback_rule_proposal_gates.md:43`) explicitly state **M3 and M4 are deprecated** under the bidirectional test framework (2026-05-17). This is a status mismatch with the home definition in `_old/framework.md` which still treats them as live.

---

## M4 — Fragmented atomic thought-unit

**Home:** _old/framework.md:232-244 (actual: `docs/_old/framework.md:232-244`)
> `### M4 — Fragmented atomic thought-unit`
> `**Definition.** If splitting a line would produce fragments that individually fail the atomic-thought test, merge...`

**Live-successor:** null — no live successor.

**Consumers (verified):**
- `scholarship/bofm/M4-BoFM-1.md:146`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.5 M4 (fragmented atomic thought-unit)`
- `scholarship/gnt/M4-GNT-1.md:190`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.5 M4 (fragmented atomic thought-unit)`
- M4-BoFM-1.md file body verified — full-bodied scholarship companion exists (line 1: `# M4-BoFM-1: Subject-Orphan Predicate Completion — Scholarship Companion`; line 13 statement of rule; ties to framework M4).
- M4-GNT-1.md file body verified — full-bodied scholarship companion exists (line 1: `# M4-GNT-1: Subject-Orphan Predicate Completion (Greek Instantiation) — Scholarship Companion`; line 13 statement; ties to framework M4 via BoFM apparatus).
- BoFM canon:148-156 (M4 at 153-154): `readers-bofm/1-method/colometry-canon.md:153` → `- **M4** Fragmented atomic thought-unit` + line 154 → `  - Does NOT fire on members of justification-1 series at N≥3 or justification-5 substantive adjuncts (§1 M4 SCOPE)`
- BoFM canon §5 reference: `readers-bofm/1-method/colometry-canon.md:2653` → `**Framework anchor:** Corpus-specific operational instantiation of framework M4 (fragmented atomic thought-unit; see [`atu-method/docs/01-normative/framework.md §1.5`](docs/01-normative/framework.md)).` (this is the §5 M4-BoFM-1 entry header context at lines 2646-2653)
- GNT canon:251-259: `readers-gnt/private/01-method/colometry-canon.md:251` → `### M4 — Fragmented Atomic Thought-Unit: GNT Cases` (block runs through 258).
- GNT canon §3.18 line 1318: `readers-gnt/private/01-method/colometry-canon.md:1318` → `### 3.18 M4-GNT-1: Subject-Orphan Predicate Completion (Greek Instantiation)`

**Consumers (FLAGGED):**
- M4 also flagged as **deprecated 2026-05-17** in `feedback_atu_test_is_bidirectional.md:43` and `feedback_rule_proposal_gates.md:43` (same deprecation status as M3) — but the row did not list these as M4 consumers; flagging here as an unreferenced relevant consumer.

---

## §1.6 four-forces

**Home:** _old/framework.md:246-254 (actual: `docs/_old/framework.md:246-254`)
> `## §1.6 Summary — the four forces`
> `| Force | Direction | Role |`
> `|---|---|---|`
> `| Propositions + 5 structural justifications | GENERATIVE | Default split at every proposition or justified non-proposition boundary |`

**Live-successor:** null — no live successor (verified via Grep on live `framework.md`).

**Consumers (verified):**
- BoFM canon:34 pointer block: `readers-bofm/1-method/colometry-canon.md:34` → `...the four forces summary; the five-step decision procedure; the application-order step-by-step...is codified at [`atu-method/docs/01-normative/framework.md §1`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- GNT canon:48 pointer block: `readers-gnt/private/01-method/colometry-canon.md:48` → `...the four forces summary; the five-step decision procedure; the application-order step-by-step...is codified at [`atu-method/docs/01-normative/framework.md §1`](docs/01-normative/framework.md). This canon does not duplicate that prose.`
- demote-memory:26: `atu-method/memories/feedback_camera_angle_diagnostic_demote.md:26` → `4. **Framework-edit (this memory's load-bearing artifact):** framework §1.3 should be updated to caveat camera-angle as "deprecated; redundant with bidirectional atomic-thought test under §1.1 refinement (see [[atu-test-is-bidirectional]]). Invocation is a warning signal for bandwagon/aesthetic reasoning." §1.6 precedence tier-matrix should likewise demote image-diagnostic row or annotate it as deprecated.`
- demote-memory:35: `atu-method/memories/feedback_camera_angle_diagnostic_demote.md:35` → `(Codified 2026-05-13 from Stan-verbatim observation during R7 motion-verb purpose-INF audit wave. Framework §1.3 + §1.6 edit pending.)`

**Consumers (FLAGGED):** none — all cites verified at claimed line numbers.

---

## §1.7 decision procedure

**Home:** _old/framework.md:256-266 (actual: `docs/_old/framework.md:256-266`)
> `## §1.7 Decision procedure`
> `At every candidate boundary:`
> `1. **Default:** merge (propositions share one predicate; atomic-thought test applies at the predication level).`

**Live-successor:** null — no live successor.

**Consumers (verified):**
- `scholarship/bofm/R28.md:151`: `- Universal framework: [`../../docs/01-normative/framework.md`](docs/01-normative/framework.md) §1.4 J3 (speech-act announcement structural justification), §1.7 (decision procedure), §7.8 (proposed-rule adoption protocol)`
- BoFM canon:34 pointer block (already cited above — explicitly references "the five-step decision procedure")
- GNT canon:48 pointer block (already cited above — explicitly references "the five-step decision procedure")

**Consumers (FLAGGED):** none.

---

## §1.8 application order

**Home:** _old/framework.md:268-280 (actual: `docs/_old/framework.md:268-280`)
> `## §1.8 Application order — explicit step-by-step`
> `The Decision Procedure above gives the high-level 5-step ordering. This subsection makes the step-internal ordering explicit so rule application is provably deterministic...`

**Live-successor:** null — no live successor.

**Consumers (verified):**
- BoFM canon:2307: `**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-1 cross-rule precedence is asserted within Tier 7; EP-1 and the other EP-rules / image-test are co-equal tiebreakers within the tier.`
- BoFM canon:2402: `**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-3 cross-rule precedence is asserted within Tier 7; EP-3 and the other EP-rules / image-test are co-equal tiebreakers within the tier.`
- BoFM canon:2500: `**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). No EP-4 cross-rule precedence is asserted within Tier 7; EP-4 and the other EP-rules / image-test are co-equal tiebreakers within the tier.`
- BoFM canon:2609: `**Precedence.** §3.5 Tier 7. Fires only after Tiers 1-6 settle. Yields to all higher tiers without exception (Tier 7 is post-hoc by construction — see §3.5 and §1.8 Step 4). When a parallel pattern is detected at N≥3, J1 (Tier 5) has already settled the outcome via the N=3+ cliff (§1.9); EP-5 confirms rather than generates...`
- GNT canon:2316: `readers-gnt/private/01-method/colometry-canon.md:2316` → `- `## Section 2: The Unless Conditions` → pointer to `framework.md §1.4–§1.9`; all GNT-corpus worked examples preserved in §2.` — **NOTE: this is the GNT canon's framework-pointer table; the cite "§1.4–§1.9" includes §1.8 in the range but does NOT name §1.8 explicitly.**
- demote-memory — Grep of `feedback_camera_angle_diagnostic_demote.md` for §1.8 → no §1.8 reference found in that file (only §1.3 and §1.6 cited). **Row's claim "demote-memory" lists §1.8 consumer is unsupported.**

**Consumers (FLAGGED):**
- GNT canon:2316 cites range `§1.4–§1.9` not §1.8 by name; the cite is in a re-homing/pointer table for the GNT canon Section 2 rewrite, and the §1.8 inclusion is range-based rather than explicit.
- demote-memory consumer claim for §1.8 — **not verified**; `feedback_camera_angle_diagnostic_demote.md` references §1.3 (line 26) and §1.6 (lines 26, 35) but **no §1.8 reference exists in the file**. Grep `§1\.8` against the file: no matches.


# Lane 5 — §1.9 + §1.10 + §1.11 + §1.12 + §1.13 + Part C docs + Part D concepts

```
## §1.9 — N=2 Adjudication Principle

**Home:** `atu-method/docs/_old/framework.md:282-297`
> `## §1.9 N=2 Adjudication Principle`
> `**The problem this solves.** Several rules mandate MERGE for N=2 coordinate constructions (M1, complement-integrity two-member that-series, etc.). Simultaneously, J1 mandates SPLIT when each member earns its own atomic beat. At N=2 both rules can fire on the same construction.`
> `**The principle.** When a merge-mandating rule and a split-mandating rule (J1) both fire on the same N=2 coordinate construction:`

**Live-successor:** null — `Grep "§1\.9\b"` over live `atu-method/docs/01-normative/framework.md` returned no matches; live framework.md sections are §1-§7 architecture (no §1.x sub-numbering below §1). However the SUBSTANCE is hosted at `atu-method/docs/01-normative/cross-corpus-principles.md §1.9` per its §0.2 manifest ("This document HOSTS: ... §1.9 (N=2 adjudication + N=3+ cliff)").
> `cross-corpus-principles.md:44: - The cross-cutting principles §1.3a (rhetoric figures constrain), §1.8 (application order), §1.9 (N=2 adjudication + N=3+ cliff)`

**Consumers (verified):**
- `atu-method/scholarship/bofm/EP-5.md:50`: `- **N=2 virtue pairs** — *faith and hope*, *meek and lowly*, *chastity and virtue*, *faith and patience*. ~20-30 instances corpus-wide. N=2 routes to §1.9 N=2 Adjudication Principle (M1 synonymy test) before reaching EP-5; most resolve to M1 merge as cognate / bonded pairs.`
- `atu-method/scholarship/bofm/EP-5.md:108`: `- **Risk: the rule could over-fire on N=2 cognate pairs.** Resolution: explicit interaction with §1.9 N=2 Adjudication Principle — N=2 pairs route to M1 synonymy test before EP-5 is consulted; EP-5 fires only on N≥3 stacks or on N=2 cases that M1 leaves unresolved.`
- `atu-method/scholarship/bofm/EP-5.md:174`: `- Universal framework: ... §1.4 J1 ... + §1.9 N=2 Adjudication Principle and N=3+ cliff + §2 (Category B editorial-judgment)`
- `atu-method/scholarship/bofm/R10.md:60`: `This case demonstrates R10's interaction with framework §1.9's N=3+ cliff: the cliff is scoped to coordinate **predications** ..., NOT to coordinate **objects** under a single shared verb.`
- `atu-method/scholarship/bofm/R10.md:132`: `- Universal framework: ... §1.9 (N=2 Adjudication / N=3+ cliff scope to predications, not objects)`
- `atu-method/scholarship/bofm/R12.md:106`: `Resolution: incorporate the §1.9 N=2 Adjudication Principle as a sub-rule, with M1 verb-synonymy as the diagnostic.`
- `atu-method/scholarship/bofm/R12.md:111`: `the framework promoted the diagnostic to a named cross-cutting principle (§1.9). ... R12's N=2 sub-rule now references §1.9 directly`
- `atu-method/scholarship/bofm/R12.md:149`: `- Universal framework: ... §1.9 (N=2 Adjudication Principle)`
- `atu-method/scholarship/bofm/R15.md:136`: `- Universal framework: ... §1.9 (N=2 Adjudication does NOT apply to appositional constructions including vocative+close-appositive)`
- `atu-method/scholarship/bofm/R18a.md:56`: `default-merge per canon §1.9 (coordinate predications only earn N≥3 stacking).`
- `atu-method/scholarship/bofm/R18a.md:119`: `- Adjacent rule (coordinate-object scope): canon §1.9 (N≥3 cliff predication-only scope), R10 sub-rule 3, R5 sub-rule 4`
- `atu-method/scholarship/bofm/R22.md:108`: `The §1.9 N=2 Adjudication Principle (M1 synonymy test) was reviewed for applicability to divine-title appositives. Verdict: explicitly excluded.`
- `atu-method/scholarship/bofm/R22.md:110`: `The exclusion is recorded in §1.9 ("Does NOT apply to appositional constructions") and in BoFM canon §3.5 Tier 6`
- `atu-method/scholarship/bofm/R22.md:168`: `- Universal framework: ... §1.9 (N=2 Adjudication Principle explicitly excludes appositives)`
- `atu-method/scholarship/bofm/R5.md:136`: `The N=3+ cliff (§1.9) suggests that at N=3+ the structure would default to J1 series treatment`
- `atu-method/scholarship/bofm/R5.md:147`: `- Universal framework: ... §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C — R5 is principled Category B)`
- `readers-bofm/validators/colometry/validate_rule_18a_patriarch_triad.py:13`: `coordinate-NP-object merge per canon §1.9 scope).`
- `readers-tanakh/scripts/scan_multi_finite_verb_line.py:242`: `    # one cola exceed the M1 N=2 bonded-pair bound and per §1.9 N=3+`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:487`: `... The N=3+ cliff (§1.9) does not engage R5 because R5 fires only on N=2 *or*-pairs.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:898`: `apply the §1.9 N=2 Adjudication Principle / M1 verb-synonymy test:`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:1172`: `apply the M1 synonymy test (§1.9 N=2 Adjudication Principle):`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:1718`: `Does NOT engage the §1.9 N=2 Adjudication Principle — appositional constructions are explicitly excluded from §1.9`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2199`: `the series is J1 territory (formally-marked parallel series) / §1.9 N=2 adjudication.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2200`: `stays split entirely per the §1.9 N≥3 cliff. → J1.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2214`: `coordinate N=2 infinitival pair; §1.9 adjudication, not auto-merge.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2553`: `apply the §1.9 N=2 Adjudication Principle before reaching EP-5`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2604`: `The N=3+ cliff (§1.9) makes this unconditional.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2605`: `Virtue/vice N=2 pair governed by §1.9 N=2 Adjudication`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2609`: `J1 (Tier 5) has already settled the outcome via the N=3+ cliff (§1.9); EP-5 confirms rather than generates.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2634`: `*Excluded by §1.9 N=2:* "having faith and hope" (N=2 cognate pair; §1.9 routes to M1 synonymy test before EP-5 fires`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:185-194`: BoFM canon "TIER 6 — N=2 adjudication" block — verified inline (substance, not §1.9 token): `**TIER 6 — N=2 adjudication** (cross-cuts Tier 4 vs Tier 5)` / `Applies to: M1 pairs, R12 N=2 compound-verb under shared AUX, R17 N=2 that-series.` / `At **N≥3** the test is moot — Justification 1 wins over merge-rules unconditionally (Helaman 3:16 cliff).`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:222-228`: `### 3.5.2 N=2 vs N=3+ cliff` / `... load-bearing across M1, R12, R17, and the polysyndetic-verb-chain detector.`
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:106-109`: `- **N=2 Adjudication Principle — GNT canonical cases.**` / 3 worked examples (John 10:20, 2 Cor 11:27, Matt 22:30).
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:183`: `**Pointer to framework.** The five structural justifications ... and the N=2 Adjudication Principle are codified at [`atu-method/docs/01-normative/framework.md §1.4–§1.9`]`
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:2327-2346`: `### 2026-05-02 — N=2 Adjudication Principle named in §1` + full body (Tanakh-Reader ported 2026-04-26; GNT-Reader codifies 2026-05-02; cross-project provenance verified inline).

**Consumers (FLAGGED):**
- `atu-method/scholarship/bofm/R21.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R21.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/R28.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R28.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/R18.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R18.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/M4-BoFM-1.md`: audit row claims §1.9 consumer, `Grep "§1\.9" M4-BoFM-1.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/R25.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R25.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/R28-ext.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R28-ext.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/M4-GNT-1.md`: audit row claims §1.9 consumer, `Grep "§1\.9" M4-GNT-1.md` returns NO matches. PHANTOM CITE.
- `atu-method/memories/feedback_rule_proposal_gates.md`: audit row claims §1.9 consumer, `Grep "§1\.9" feedback_rule_proposal_gates.md` returns NO matches. PHANTOM CITE. (Broader `Grep "§1\.9" atu-method/memories/` returned NO matching files in scope.)
- `readers-bofm/validators/colometry/validate_rule_07_ud.py:161`: cite is for `§1.5 M4`, NOT §1.9. (Line 161 reads `if is_elided_this_matrix(sent, head, line_map): continue` — the surrounding comment at lines 161-162 cites `§1.5 M4`.) WRONG ANCHOR.
- `readers-bofm/validators/colometry/validate_rule_06_ud.py:104`: cite is for `§1.5 M4`, NOT §1.9. (Line 104 reads `fragment that R6/R7 yield to per §1.5 M4 (fragmented-atomic-thought-unit).`) WRONG ANCHOR.
- `readers-gnt/scripts` + `readers-tanakh/validators` + `.claude/projects/.../memory`: audit row implied broad consumer presence; `Grep "§1\.9\b"` over readers-gnt returned NO matches; over .claude/projects returned NO matches. Live §1.9 footprint is bofm-only.
- 60+ files claim from audit row is OVERSTATED. Actual ground-truthed consumers: 7 atu-method/scholarship/bofm files + 1 BoFM canon (Dropbox) + 1 GNT canon (Dropbox) + 1 BoFM validator + 1 Tanakh script = ~11 distinct files containing §1.9 citations (not "60+").

---

## §1.9 N=3+ cliff SCOPE sub-clause (predications-vs-objects)

**Home:** `atu-method/docs/_old/framework.md:297`
> `**Scope of the N=3+ cliff.** Applies to coordinate **predications** (compound verbs under shared auxiliary, coordinate that-clauses, coordinate finite clauses). Does NOT apply to coordinate **objects** under a single shared verb — those are governed by J1's compound-list-break-signals sub-rule.`

**Live-successor:** null — no live successor for the SCOPE sub-clause specifically (the §1.9 umbrella has no live home; the sub-clause is a named-but-unnumbered sub-anchor under it).

**Consumers (verified):**
- `atu-method/scholarship/bofm/R10.md:60`: `This case demonstrates R10's interaction with framework §1.9's N=3+ cliff: the cliff is scoped to coordinate **predications** (compound verbs, coordinate *that*-clauses, coordinate finite clauses), NOT to coordinate **objects** under a single shared verb. Three coordinate objects under one verb do not invoke J1's win-over-merge mandate; they remain part of one predication.`
- `atu-method/scholarship/bofm/R18a.md:119`: `- Adjacent rule (coordinate-object scope): canon §1.9 (N≥3 cliff predication-only scope), R10 sub-rule 3, R5 sub-rule 4`

**Consumers (FLAGGED):** none.

---

## §1.10 — Punctuation is not a break signal

**Home:** `atu-method/docs/_old/framework.md:299-309`
> `## §1.10 Punctuation is not a break signal`
> (followed by 11 lines elaborating "no deterministic role"; "Test."; "every punctuation mark from the source text stays in place")

**Live-successor:** SUBSTANCE migrated to `atu-method/docs/01-normative/framework.md §2.1` ("Punctuation has ZERO force"). Verified via consumer cites in R19/EP-1 below ("framework §2.1, 'Punctuation has ZERO force'"). No live `§1.10` section exists in live framework.md (`Grep "§1\.10"` over live framework.md returned no matches).
> Cross-corpus-principles.md:51 lists this delegation explicitly: `- Punctuation-not-a-signal: \`framework.md §2.1\` final paragraph`

**Consumers (verified — Batch A1 repointed to §2.1 per commit 86e1219):**
- `atu-method/scholarship/bofm/R19.md:31`: `The methodology forbids punctuation as a break signal (framework §2.1, "Punctuation has ZERO force"). The apparatus therefore needs an alternative proxy ...` — REPOINTED to §2.1 (no §1.10 token).
- `atu-method/scholarship/bofm/R19.md:134`: `- Universal framework: ... §2.1 (punctuation has zero force — motivates UPOS-gated proxy)` — REPOINTED to §2.1.
- `atu-method/scholarship/bofm/EP-1.md:40`: `... now formalized as \`framework.md\` §2.1, "Punctuation has ZERO force", and BoFM canon §1 Punctuation is not a break signal).` — REPOINTED.
- `atu-method/scholarship/bofm/EP-1.md:71`: `The principle was generalized from EP-1's specific case ... (now \`framework.md\` §2.1, "Punctuation has ZERO force", and BoFM canon §1 Punctuation is not a break signal).` — REPOINTED.
- `atu-method/scholarship/bofm/EP-1.md:153`: `- Universal framework: ... §2.1 (punctuation has zero force) + §7.0 (Category B editorial-judgment) + §1.5 J5 ...` — REPOINTED.
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:34`: pointer block (BoFM canon §1) — substance preserved: `the punctuation-not-a-signal and versification-not-a-signal stances ... is codified at [\`atu-method/docs/01-normative/framework.md §1\`]` (note: still cites `framework.md §1` umbrella, not §2.1 — POSSIBLE STALE POINTER).
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:114`: TIER 0 entry `- Punctuation is not a break signal (see §1)` (per-corpus body; no §1.10 token).
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:48`: pointer block (GNT canon §1) — analogous to BoFM:34; still cites `framework.md §1` umbrella, not §2.1.
- `atu-method/memories/feedback_punctuation_not_evidence.md`: file exists (Glob verified); is the named feedback memory carrying the same principle.

**Consumers (FLAGGED):**
- BoFM canon:34 + GNT canon:48 pointer blocks still cite `framework.md §1` umbrella rather than `framework.md §2.1` — content survives via umbrella, but if §1 umbrella is later restructured these pointers will rot.

---

## §1.11 — Versification is not a break signal

**Home:** `atu-method/docs/_old/framework.md:311-313`
> `## §1.11 Versification is not a break signal`
> `Verse divisions in canonical texts are editorial overlay (same status as punctuation). No break versification imposes is canonical. If a cross-verse merge case is identified, flag per the applicable Category (§2).`

**Live-successor:** SUBSTANCE migrated to `atu-method/docs/01-normative/framework.md §3` v1.6 cross-verse continuity per cross-corpus-principles.md:52: `- Versification-not-a-signal: \`framework.md §3\` v1.6 cross-verse continuity`. No live `§1.11` section exists in live framework.md (`Grep "§1\.11"` over live framework.md returned no matches).

**Consumers (verified):**
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:34`: pointer block — `punctuation-not-a-signal and versification-not-a-signal stances ... is codified at [\`atu-method/docs/01-normative/framework.md §1\`]`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:115`: TIER 0 entry `- Versification is not a break signal (see §1)` (per-corpus body).
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:48`: pointer block (same structure as BoFM:34).
- `atu-method/docs/_old/rule-equivalence-map.md:23`: `Cross-verse continuity (atomic thought spanning verse boundary stays intact) | R14 (implied ... handled by framework §1.11) | §3.17 cross-verse-continuity-merge | H10 (explicit rule ...)`
- `atu-method/docs/_old/rule-equivalence-map.md:110`: `- Cross-verse continuity (H10 / §3.17 / §1.11) — port`

**Consumers (FLAGGED):**
- BoFM:34 and GNT:48 pointer blocks cite `framework.md §1` umbrella (not §1.11 token directly, not §3 v1.6 successor).
- Live consumer footprint is THIN — only pointer-block + the _old/rule-equivalence-map. The "§1.11 cited" by audit row in atu-method/memories returned no Grep matches.

---

## §1.12 — Parallel-List Uniformity Principle

**Home:** `atu-method/docs/_old/framework.md:313-323`
> `## §1.12 Parallel-List Uniformity Principle`
> `When a multi-verse list of parallel members exists with a shared explicit frame, list members receive uniform line-treatment regardless of their individual syntactic shape. Per-construction rules yield to the list-uniformity principle within the list's scope.`
> (plus 4-condition trigger + default direction; full body extends to line 323)

**Live-successor:** PARKED AT PER-CORPUS LEVEL per cross-corpus-principles.md:54: `- Parallel-List Uniformity (§1.12 old): per-corpus — \`BoFM canon §1\` Tier 0 (Moroni 10:8-17 canonical case)`. NO live framework.md home (`Grep "§1\.12"` returned no matches in live framework.md). canon-index.md:146 calls this "CONTESTED at framework level" because `framework.md §2.2:116` firewall would exclude parallelism-class adjudication as a primary break-license.

**Consumers (verified):**
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:45`: `**Parallel-List Uniformity canonical case:** Moroni 10:8-17 spiritual-gifts list (9 members; 3 outliers per 2026-04-26 sweep; merge-dominant treatment).` — BoFM pointer block entry.
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:117`: TIER 0 entry `- **Parallel-List Uniformity** — multi-verse list with shared frame settles uniform treatment (see §1; e.g., Moroni 10:8-17 spiritual gifts)`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:172`: `Yields to **Parallel-List Uniformity** within multi-verse lists (e.g., Moroni 10:8-17)`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:560`: `Yields to ... §1.12 Parallel-List Uniformity (within multi-verse parallel lists), and to M4`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:636`: `5. Multi-verse list with parallel-list uniformity scope (e.g., Moroni 10:8-17) → §1.12 Parallel-List Uniformity wins`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:642`: `Yields to ... §1.12 Parallel-List Uniformity (multi-verse parallel lists).`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:2607`: `Virtue/vice stack appearing in a multi-verse parallel list with a shared explicit frame (Parallel-List Uniformity Principle, §1.12) → list-uniformity governs`
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:48`: pointer block — substance ("Parallel-List Uniformity Principle") referenced in the umbrella pointer.
- `atu-method/docs/_old/rule-equivalence-map.md:25`: `**Parallel-list uniformity** ... (framework §1.12 applies) ... | (Same framework §1.12 principle.)`
- `atu-method/scholarship/bofm/R6.md:140`: `- Universal framework: ... §1.12 (Parallel-List Uniformity); BoFM canon §3.5 Tier 5`
- `atu-method/scholarship/bofm/R7.md:138`: `- Universal framework: ... §1.12 (Parallel-List Uniformity); BoFM canon §3.5 Tier 5 (yields-to relationships)`

**Consumers (FLAGGED):**
- `atu-method/scholarship/bofm/R10.md`: audit row asserted R10 as §1.12 consumer; `Grep "§1\.12" R10.md` returns NO matches (R10's §1.12 row in audit is a PHANTOM CITE — R10 cites §1.9, §1.2, §1.4, §1.5, NOT §1.12).
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:560` and `:636` and `:642`: cite §1.12 token directly — but the framework.md §1.12 has been ARCHIVED. These cites land on a section that no longer exists in the live spec; they survive only because cross-corpus-principles.md hosts the substance.

---

## §1.13 — Authorial asymmetry overrides editorial symmetry

**Home:** `atu-method/docs/_old/framework.md:331-337`
> `## §1.13 Authorial asymmetry overrides editorial symmetry`
> `When a passage contains a serial construction (wo/blessed series, positive/negative conditional pair, beatitude chain, interrogative chain) and the author treats members asymmetrically — expanded mechanism for some, compact for others — **preserve the authorial asymmetry**. Do not pressure compact members to expand, or expanded members to compress, in order to achieve uniform line-treatment across the series.`

**Live-successor:** PARKED AT PER-CORPUS LEVEL per cross-corpus-principles.md:53: `- Authorial asymmetry (§1.13 old): per-corpus — \`BoFM canon §1\` Tier 0 + \`GNT canon §3.7\` R28`. NO live framework.md home (`Grep "§1\.13"` returned no matches in live framework.md).

**Consumers (verified):**
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:44`: `**Authorial Asymmetry corpus precedents:** 2 Nephi 9:27-38 wo-series (9:30 expanded; 9:31-37 compact; 9:38 closes with embedded triad); 3 Nephi 12:1-12 Sermon-at-the-Temple expansions vs Matthean parallels.`
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:116`: TIER 0 entry `- **R28 Authorial Asymmetry** — preserves asymmetric series before any uniformity sweep (see §1)`
- `Dropbox/gnt-reader-private/01-method/colometry-canon.md:741-753`: GNT `#### R28 — Textual Asymmetry Overrides Editorial Symmetry (Principle entry)` (full body present with Matt 25:35–36 / 25:43 worked example; R28 status Active; cited by R12/R13/R14 as bounding constraint).
- `atu-method/scholarship/bofm/R28.md:132`: `Recommendation: rename the §1 Authorial Asymmetry Principle to a structural-principle ID (e.g., a §1.13 stable section ID without the R28 designation, since structural principles in §1 are not per-rule entries in §5).` — meta-reference (proposing rename, not asserting current §1.13 as live).
- `readers-gnt/validators/canon/check_canon_alignment.py:339-348`: R28 entry (`"rule_id": "R28"`, `"name": "Textual asymmetry overrides editorial symmetry"`, `"rule_type": "Principle"`) — substance present; NO `§1.13` token in the file (Grep returned 0 matches).

**Consumers (FLAGGED):**
- `readers-gnt/validators/canon/check_canon_alignment.py:339-348` cite by audit row was at `readers-gnt/private/01-method/check_canon_alignment.py:339-348` — WRONG PATH; actual location is `readers-gnt/validators/canon/check_canon_alignment.py`. Substance matches, path wrong.
- `atu-method/scholarship/gnt/R28-ext.md`: audit claims §1.13 consumer; `Grep "§1\.13" R28-ext.md` returns NO matches. PHANTOM CITE for §1.13 specifically (R28-ext.md may discuss R28 substance but does not cite the §1.13 token).
- `atu-method/scholarship/bofm/R28.md`: only ONE §1.13 reference (line 132), and it's a META-PROPOSAL to rename — not a substantive consumer of §1.13's normative text.

---

## Part C — Doc-level verification

### `framework.md` (universal)
**Receipts:** `Grep "framework\.md"` over `C:/Users/bibleman/repos` returns 77 files (see file list above). Confirmed as the universally-cited canonical doc. Live at `atu-method/docs/01-normative/framework.md` (Glob verified).

### `_old/framework.md` (archived)
**Receipt:** Glob `**/framework.md` returned `repos\atu-method\docs\_old\framework.md` (the archived copy) + `repos\atu-method\docs\framework.md` (live). Archived copy hosts §1.9, §1.10, §1.11, §1.12, §1.13 bodies — all home receipts pasted above came from this file.

### `_old/change-protocol.md` (resolved Stage 1)
**Receipt:** Glob returned `repos\atu-method\docs\_old\change-protocol.md` (archived) + `repos\atu-method\docs\_old\2026-05-18-mechanical-first-rewrite\change-protocol.md`. First 10 lines verified:
> `# Change Protocol — §7 (Operational)`
> `**This document is the canonical statement of the change protocol for ATU canons.** It supersedes per-repo §7 sections, which become one-line pointers to this document. Sections below are the authoritative specification; framework.md §7 is now a one-line pointer here.`

### `binding-rules-hebrew.md` (28 cites / 15 files claim)
**Receipt:** `Grep "binding-rules-hebrew"` over `C:/Users/bibleman/repos` returned 13 files (NOT 15). Audit claim of 28 cites / 15 files is OFF BY 2 FILES. Actual file list:
1. atu-method/canon-index.md
2. atu-method/docs/01-normative/cross-corpus-principles.md
3. atu-method/docs/00-start-here.md
4. atu-method/docs/02-registries/binding-rules-lxx.md
5. atu-method/docs/01-normative/framework.md
6. atu-method/docs/03-implementation/apparatus.md
7. atu-method/docs/01-normative/glossary.md
8. atu-method/docs/05-status/methodology-position.md
9. readers-gnt/_archive/2026-05-19-pre-unification/directives/README-SUPERSESSION-NOTE.md
10. readers-tanakh/data/text-files/v2-pipeline-draft/_OPERATION_IN_PROGRESS.md
11. readers-tanakh/_archive/2026-05-19-pre-unification/CLAUDE.md
12. readers-tanakh/scripts/atu_pipeline_v2/README.md
13. atu-method/docs/03-implementation/toolset-architecture.md

### `binding-rules-lxx.md` (PARKED)
**Receipt:** File exists. First 12 lines confirm PARKED banner:
> `# LXX Greek Binding Rules Catalog`
> `> **Status (2026-06-06): smoke-test artifact — pipeline PARKED 2026-05-27.** The rule designs in this catalog were drafted against the UD_Ancient_Greek-PTNK gold (Gen+Ruth, the only available gold LXX syntax treebank) but the live LXX pipeline ... currently uses a different UD-native architecture; the integration target for this catalog is the projection-v1 generator not yet wired live. The rule designs are the restart point ... This catalog is NOT authoritative live canon today; it is recorded here so the work is preserved + version-controlled (per 2026-06-05 forensic audit recommendation, surfaced via claudit citation-rot scan).`

### `cross-corpus-principles.md` (NEW B1)
**Receipts:**
- File exists on disk (Glob `repos\atu-method\docs\cross-corpus-principles.md`).
- `_index.md` entry at lines 19-21: line 20 reads `- [\`cross-corpus-principles.md\`](docs/01-normative/cross-corpus-principles.md) — **Cross-corpus universal principles companion.** Candidate-ATU substrate (§1.1), structural justifications J1/J2/J4/J5, merge-overrides M1/M4, application order (§1.8), N=2 Adjudication + N=3+ cliff (§1.9), rhetoric-figures-constrain (§1.3a). NOT break-licensors (those live at \`framework.md §2.1\`/§2.2); this is the methodology layer above per-corpus rule catalogs.` VERIFIED at line 20 (not 19-21 exactly — single-line entry).
- Tanakh canon row: audit claim was "line 13"; actual content at `readers-tanakh/private/01-method/colometry-canon.md:14` reads `| \`atu-method/docs/01-normative/cross-corpus-principles.md\` | Cross-corpus universal principles (J1/J2/J4/J5, M1/M4, §1.9 N=2 + N=3+ cliff, §1.8 application order); Tanakh H17 (parallel-list) inherits from §1 framework + per-corpus instantiation |`. **Off by 1 line** (cited 13, actual 14).

**Consumers (FLAGGED):**
- Tanakh canon row OFF BY 1: audit cited line 13, actual at line 14.
- `_index.md` entry: audit cited "lines 19-21"; actually a single line at line 20 (line 19 is the framework.md row above it).

---

## Part D — Concept-level verification

### Camera-angle concept (same scope as §1.3)
**Receipt:** cross-corpus-principles.md:58 retires it explicitly:
> `- Camera-angle test (§1.3 old) — RETIRED. See \`canon-index.md\` Stan's rulings.`
(Per assignment scope this is "same as §1.3" — §1.3 row owned by sibling verifier; here only confirm the retirement line is on disk.)

### ATU vs. rhetorical/discourse lens distinction (NEW 2026-06-06)
**Receipts:**
- `atu-method/memories/feedback_atu_and_rhetorical_lenses_distinct.md`: Glob CONFIRMED exists on disk.
- `cross-corpus-principles.md §0.1` mentions it: `Grep "feedback_atu_and_rhetorical_lenses_distinct"` returned line 35: `[\`../memories/feedback_atu_and_rhetorical_lenses_distinct.md\`](../memories/feedback_atu_and_rhetorical_lenses_distinct.md)` — appears in §0.1 body. §0.1 header at line 18 verified: `### §0.1 Lens scope — ATU vs. rhetorical/discourse structure`.

### Helaman 3:16 cliff precedent (BoFM-specific)
**Receipts:** `Grep "Helaman 3:16"` over `C:/Users/bibleman/repos` returned 5 files:
- `repos\atu-method\canon-index.md`
- `repos\atu-method\docs\cross-corpus-principles.md`
- `repos\atu-method\docs\_old\_index.md`
- `repos\atu-method\scholarship\bofm\R12.md`
- `repos\atu-method\docs\_old\glossary.md`
Also: BoFM canon §3.5 Tier 6 ("At N≥3 the test is moot — Justification 1 wins over merge-rules unconditionally (Helaman 3:16 cliff)." at colometry-canon.md:194 — verified above in §1.9 receipts).

### Moroni 10:8-17 spiritual-gifts case (BoFM-specific)
**Receipts:** `Grep "Moroni 10:8-17|Moroni 10:8"` over `repos/atu-method` returned 2 files:
- `repos\atu-method\canon-index.md`
- `repos\atu-method\docs\cross-corpus-principles.md`
BoFM canon hits (Dropbox/bom-reader-private/01-method/colometry-canon.md): lines 45, 117, 172, 636 — all verified above.

### 2 Nephi 9:27-38 wo-series (BoFM-specific)
**Receipts:**
- `repos/atu-method`: 1 file (`repos\atu-method\canon-index.md`).
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:44`: `**Authorial Asymmetry corpus precedents:** 2 Nephi 9:27-38 wo-series (9:30 expanded; 9:31-37 compact; 9:38 closes with embedded triad)`

**Consumers (FLAGGED):**
- Light footprint — only canon-index.md and the one BoFM canon line. Audit "BoFM-specific concept" framing accurate but scope is genuinely narrow.

### §3.21 scanner false-positive
**Receipts:**
- `Grep "§3\.21"` over `atu-method/docs` returned NO matches.
- `Grep "§3\.21"` over `_old/framework.md` returned NO matches.
- `Grep "§3\.21"` over live `framework.md` returned NO matches.
- R10.md:31 CGEL Ch. 14 cite VERIFIED: `The compound-list-break-signals sub-rule of §1.4 J1 implements this coordination treatment ... This is CGEL Ch. 14's coordination-under-shared-predicator pattern instantiated as a colometric merge.`
- R10.md:29 also contains the CGEL Ch. 14 §2 substantive cite: `- **CGEL Ch. 14 §2** on coordination — when a transitive verb takes a coordinate object series ...`
- Confirms: any scanner hit for `§3.21` is a FALSE POSITIVE (the only `§...` token near R10.md:31 is `§1.4 J1`; CGEL `Ch. 14 §2` is a citation to the Cambridge Grammar of the English Language, NOT an atu-method §-anchor).

**Consumers (FLAGGED):** none — verified zero internal §3.21 hits.


---

# Appendix — FLAGGED entries (synthesis)

79 FLAGGED items surfaced by the verifier workflow across 32 anchors. These are NOT auto-fail items — they surface decisions Stan + claudit should adjudicate. Grouped by anchor.

## §0.1 Mission

- `scholarship/bofm/R20.md:17,126` — canon-index lists these as §0.1 consumers but they cite `§1`, not `§0.1`. This is correct per the canon-index annotation "(repointed in Batch A1 to §1)". The cells are NOT phantom; they are post-repoint live successors. Verifier note: the row is faithful (the §-citation was rewritten before the index was hand-built) — flagged because the post-repoint cite is what's on disk, not the pre-repoint `§0.1`.
- BoFM canon range `22-28` and GNT range `25-43` — `§0` is cited at BoFM:26 and GNT:29 (single-line cites). The "ranges" in the canon-index represent the surrounding §0 pointer block. No verbatim `§0.1` token at the cited ranges in either canon; both cite `§0` umbrella.

## §0.2 Method

- No verbatim `§0.2` token exists in the BoFM or GNT canon files (Grep `§0` matches lines BoFM:5, BoFM:26 and GNT:8, GNT:29, GNT:41, GNT:177, GNT:2302, GNT:2310, GNT:2313, GNT:2314, GNT:2369; none use `§0.2`). The §0.2 sub-anchor is consumed only via the umbrella `§0` pointer. Cite-by-umbrella is a real consumption pattern but does NOT give a verbatim §0.2 receipt.

## §0.3 Pragmatic stance

- `atu-method/memories/feedback_rhetoric_bandwagon.md` — canon-index says "(1 cite)" but a `§0.3` Grep returns no matches in this file. The conceptual link goes through `feedback_sense_line_mission.md` referenced at line 13. **More importantly:** the memory's framing ("Our theoretical foundation is psycholinguistic / cognitive") is in semantic *tension* with §0.3's "not derived from a cognitive theory; no such claim is asserted" — the canon-index disposition `fold→§1 Purpose` glosses this tension. Surface to Stan.
- BoFM/GNT canon pointer-block — same FLAG as §0.2: §0.3 sub-anchor is consumed only via umbrella `§0`; no verbatim §0.3 token in either canon.

## §0.4 Scope

- `scholarship/bofm/R23.md:61` — same shape as R20: cites `§1`, not `§0.4`. Post-repoint state; the canon-index annotation "(repointed in Batch A1 to §1)" is faithful. No live `§0.4` token on disk in any consumer.

## §7.0 Categories A / B / C

- None at the §7.0 ID level. (Glossary stale-cite at canon-index:111 is itself documented as out-of-scope and flagged for next-cycle, so it is a tracked-flag not a hidden-flag.)

## §7.1 Authority

- Canon-index row reports "(no rot-list cites; structural-anchor only)" — consistent with absence of live consumer §7.1 citations in `scholarship/` / `memories/` / per-corpus canon files. Live structural-anchor with no operational consumers. Not a defect.

## §7.2 Proposal requirements

- Canon-index says "scholarship/bofm/R20.md:33 + 1 other rot-list cite" — the "1 other" is unnamed. Live grep finds only R20.md:33 across `atu-method/`. Possible second cite was the `change-protocol.md` archived self-ref (now `_old/`) and dropped from rot-list as Stage 1 resolved it. Flag for canon-index author confirmation.

## §7.3 Mandatory-audit triggers

- Canon-index says "36 cites resolved in Stage 1". Total LIVE §7.3 cites enumerated above is approximately 60+ unique lines across atu-method live + workspace CLAUDE.md + memory. The "36" count is for the rot-list, not for all live cites — flag terminology precision: "36 cites resolved" ≠ "36 cites exist". Cite-density is higher than the row implies; the row's claim is faithful in spirit (the rot-list-bounded subset) but might mislead.
- `docs/05-status/deployment-status.md:21` matched in Grep but content omitted by truncation flag. Verifier could not paste verbatim line. Re-read needed to confirm §7.3 usage. Flagged.
- `scholarship/bofm/R6.md:129` matched in Grep but content omitted by truncation flag. Same — re-read needed.
- `project_bofm_substrate_quality.md:10` truncated, same flag.
- `docs/01-normative/framework.md:114` matched in Grep but content was omitted by `[Omitted long matching line]`. This is the §2.2:114 line area, possibly a §7.3 footnote/cross-ref. Re-read needed to confirm.
- The user-wide file `~/.claude/CLAUDE.md` has NO `§7.3` cites — canon-index row says "across CLAUDE.md, MEMORY.md, scholarship, memories, ~/CLAUDE.md". The "~/CLAUDE.md" component is the user-home-workspace `C:/Users/bibleman/CLAUDE.md` (5 cites), NOT the user-wide `C:/Users/bibleman/.claude/CLAUDE.md` (0 cites). The row's wording "~/CLAUDE.md" is ambiguous between the two CLAUDE.mds in Stan's stack; the user-wide file is empty for §7.3, the user-home file is rich. Flag for Stan's terminology disambiguation.

## §7.4 Audit-skippable categories

- Canon-index says "retraction-log-protocol.md + Batch A1/A2/A3/A4 commit-message audit-evidence declarations". The "Batch A1/A2/A3/A4 commit-message" claim is in git-log space and not greppable from disk. Verifier cannot ground-truth these without `git log`. Flag for Stan/audit-runner: receipt of commit-message §7.4 declarations not provided by this disk-only verification. NOT a disposition defect, but a verification-completeness flag.

## §7.5 Audit-evidence in commit messages

- Canon-index claims "all Stage 1 / Track A commit messages" — same shape as §7.4: git-log-only assertion not ground-truthed by disk grep. Verification-completeness flag.
- Canon-index also names `feedback_claude_commits_and_pushes.md` + `feedback_never_skip_audit_gate.md`. Both confirmed above. Faithful.

## §7.6 Self-test before commit

- Canon-index says "(no direct rot-list cites; structural-anchor; consumed by §7.5 commit-message construction)". Confirmed — no live §7.6 cites in `scholarship/`, `memories/`, or reader CLAUDE.mds outside the archived `_old/` paths. Faithful.

## §7.7 Self-consistency audit trigger

- The `feedback_compaction_resume_protocol.md:54` cite is an **example string inside a self-report illustration** — it is not a regulative cite of §7.7 ("apply this trigger") but a pretend-quote of past recovery prose mentioning §7.7. The canon-index "(1 cite)" is technically correct on token count but semantically thin. The row faithfully describes this as the sole cite; flagged for completeness — there is no operational consumer of §7.7 in live scholarship/memories.

## §7.8 Proposed-rule adoption protocol

- Canon-index "(4 rot-list cites)" — live grep shows ≥8 live cites across R27/R28/feedback files (R28.md ×4, R27.md ×6, feedback_three_anti_default_factors.md ×1, feedback_rule_proposal_gates.md ×2). Same shape as §7.3 flag: "rot-list cites" is a constrained subset; live cite count is higher. Row content is faithful in spirit (the rot-list-bounded subset) but underplays live density. Flag for terminological precision.

## §7.9 Binding-rule design checklist

- **Anchor reuse — live §7.9 semantic ≠ archived §7.9 semantic.** Archived `_old/2026-05-18-mechanical-first-rewrite/change-protocol.md:110` defined §7.9 as "Architecture-method alignment check"; live `docs/01-normative/framework.md:352` defines §7.9 as "Binding-rule design checklist". Any consumer pointer to "§7.9" written against the archived semantics is **silently semantically broken** in the live world. The `_old/canon-validator-alignment-protocol.md:49` cite is the demonstration: it cites §7.9 expecting the architecture-method-alignment-check semantics, which is no longer at §7.9. Canon-index row says "(no direct cites; preserves prior live `framework.md §7`)" — but it does NOT flag the §7.9 semantic-collision against the rewrite-stage archived §7.9. Surface to Stan: archived `_old/2026-05-18-mechanical-first-rewrite/` material reads as "current" to a naive grep, and §7.9's anchor was repurposed across the rewrite-stage. The `canon-validator-alignment-protocol.md` is archived and tombstoned, so the impact is contained, but the canon-index row's "(no direct cites)" claim glosses the archived-but-still-on-disk citer.
- Canon-index says §7.9 has no direct cites — confirmed for `scholarship/` and `memories/` live grep. Faithful in scope.

## §1.1 Generative principle

- `scholarship/bofm/R27.md:105`: §1.1 token not present at line 105. Full-file grep for `§1.1` in R27.md returns only line 172. The canon-index citation `R27.md:105` is wrong for §1.1.
- `scholarship/bofm/R21.md:21`: Canon-index cites `R21.md:21`. Actual §1.1 hit is line 21 (verified — the "is therefore not a Structural Justification" line). Confirmed correct.
- `scholarship/bofm/R5.md:147`: Canon-index lists `R5.md:147` under §1.1 consumers. Line 147 reads: `- Universal framework: [...] §1.5 (merge-overrides — R5 is structurally parallel to M1 on the *or* coordinator), §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C — R5 is principled Category B)`. §1.1 token NOT present. Cite is wrong; R5.md contains no §1.1 reference (full-file grep returned no matches).

## §1.2 Syntax forbids splits (umbrella)

- `scholarship/bofm/R5.md:147`: Canon-index lists `R5.md:147` under §1.2 consumers ("syntax forbids splits"). Verified line 147: `§1.5 (merge-overrides...), §1.9 (N=2 Adjudication Principle), §2 (Categories A/B/C ...)`. §1.2 token NOT present. Full-file grep for `§1.2` in R5.md returns no matches. Cite is wrong.
- `readers-tanakh/scripts/archive/apply_formula_integrity_merge.py:2`: line 2 is the file encoding shebang-adjacent line (`# -*- coding: utf-8 -*-`); the file's docstring (lines 3-4) describes M1 bonded-pair/formula-integrity work but does not literally cite `§1.2`. Cite is conceptual, not literal — flag as line-number-target-not-a-§-token-bearing-line.

## §1.2.1 Layer 1 mid-phrase prohibitions

- (none — all five sub-clause cites for §1.2.1 ground-truth on the exact lines named)

## §1.2.2 Layer 3 complement integrity

- (none — both cites ground-truth on the named lines)

## §1.2.3 Layer 3 formula integrity

- (none — both cites ground-truth on the named lines)

## §1.3 camera-angle

- `scholarship/bofm/R28.md (multiple)`: NO matches for `camera-angle` OR `§1.3` in R28.md. Closest is `R28.md:21` and `:151` which cite §1.4 J3, NOT §1.3 camera-angle. The audit row's claim that R28.md is a §1.3 consumer fails ground-truth — R28.md cites §1.4 J3 only.

## §1.3a rhetoric figures constrain

- `atu-method/memories/feedback_rhetoric_figures_constrain_atu.md` (audit row claims **6 cites** to §1.3a): full file Read returns ZERO occurrences of `§1.3a`. The file cites `framework.md §1.1` (line 8 references §1.1) and `framework.md §1.2` (lines 12, 13, 16) — never §1.3a. Six §1.2 / §1.1 cites exist; the audit row appears to misattribute these to §1.3a.
- `atu-method/memories/feedback_rule_proposal_gates.md`: NO match for `§1.3a`. Closest content (line 11): `Am I citing a surface feature (UD signature, rhetorical figure, punctuation, lexical pattern) as evidence?` — a generic rhetoric-as-surface-feature mention, NOT a §1.3a cite.
- `atu-method/memories/feedback_no_fake_dilemmas.md`: NO match for `§1.3a`. Closest (line 36): `- `feedback_rhetoric_bandwagon.md` — meta-audit failure mode (judgment-handoff smuggling section)` — pointer to the bandwagon memory, NOT a §1.3a cite.
- `readers-bofm/1-method/colometry-canon.md` Tier 0 mentions: not located by direct Grep within the offsets exercised; flagged as not ground-truthed in this verification pass (no specific line was supplied for the Tier 0 claim, and a Grep for `§1.3a` against the canon would be required to confirm).

## §1.4 umbrella (Five Structural Justifications closed list)

- `readers-bofm/1-method/colometry-canon.md:1581`: cites §1.5 M3, not §1.4. Mis-attributed.
- `readers-bofm/1-method/colometry-canon.md:2653`: cites §1.5 M4, not §1.4. Mis-attributed.
- `readers-gnt/private/01-method/colometry-canon.md:227-259`: this is the M1-M4 GNT-cases block (§1.5 territory), not §1.4. Mis-attributed.

## §1.5 umbrella — Four Merge-Override Conditions

- `scholarship/bofm/EP-1.md:153` cites "§1.5 J5" — but J5 is part of §1.4 (five structural justifications), not §1.5 (four merge-overrides). Section number mismatch.

## §1.8 application order

- GNT canon:2316 cites range `§1.4–§1.9` not §1.8 by name; the cite is in a re-homing/pointer table for the GNT canon Section 2 rewrite, and the §1.8 inclusion is range-based rather than explicit.
- demote-memory consumer claim for §1.8 — **not verified**; `feedback_camera_angle_diagnostic_demote.md` references §1.3 (line 26) and §1.6 (lines 26, 35) but **no §1.8 reference exists in the file**. Grep `§1\.8` against the file: no matches.

## §1.9 — N=2 Adjudication Principle

- `atu-method/scholarship/bofm/R21.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R21.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/R28.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R28.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/R18.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R18.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/bofm/M4-BoFM-1.md`: audit row claims §1.9 consumer, `Grep "§1\.9" M4-BoFM-1.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/R25.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R25.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/R28-ext.md`: audit row claims §1.9 consumer, `Grep "§1\.9" R28-ext.md` returns NO matches. PHANTOM CITE.
- `atu-method/scholarship/gnt/M4-GNT-1.md`: audit row claims §1.9 consumer, `Grep "§1\.9" M4-GNT-1.md` returns NO matches. PHANTOM CITE.
- `atu-method/memories/feedback_rule_proposal_gates.md`: audit row claims §1.9 consumer, `Grep "§1\.9" feedback_rule_proposal_gates.md` returns NO matches. PHANTOM CITE. (Broader `Grep "§1\.9" atu-method/memories/` returned NO matching files in scope.)
- `readers-bofm/validators/colometry/validate_rule_07_ud.py:161`: cite is for `§1.5 M4`, NOT §1.9. (Line 161 reads `if is_elided_this_matrix(sent, head, line_map): continue` — the surrounding comment at lines 161-162 cites `§1.5 M4`.) WRONG ANCHOR.
- `readers-bofm/validators/colometry/validate_rule_06_ud.py:104`: cite is for `§1.5 M4`, NOT §1.9. (Line 104 reads `fragment that R6/R7 yield to per §1.5 M4 (fragmented-atomic-thought-unit).`) WRONG ANCHOR.
- `readers-gnt/scripts` + `readers-tanakh/validators` + `.claude/projects/.../memory`: audit row implied broad consumer presence; `Grep "§1\.9\b"` over readers-gnt returned NO matches; over .claude/projects returned NO matches. Live §1.9 footprint is bofm-only.
- 60+ files claim from audit row is OVERSTATED. Actual ground-truthed consumers: 7 atu-method/scholarship/bofm files + 1 BoFM canon (Dropbox) + 1 GNT canon (Dropbox) + 1 BoFM validator + 1 Tanakh script = ~11 distinct files containing §1.9 citations (not "60+").

## §1.10 — Punctuation is not a break signal

- BoFM canon:34 + GNT canon:48 pointer blocks still cite `framework.md §1` umbrella rather than `framework.md §2.1` — content survives via umbrella, but if §1 umbrella is later restructured these pointers will rot.

## §1.11 — Versification is not a break signal

- BoFM:34 and GNT:48 pointer blocks cite `framework.md §1` umbrella (not §1.11 token directly, not §3 v1.6 successor).
- Live consumer footprint is THIN — only pointer-block + the _old/rule-equivalence-map. The "§1.11 cited" by audit row in atu-method/memories returned no Grep matches.

## §1.12 — Parallel-List Uniformity Principle

- `atu-method/scholarship/bofm/R10.md`: audit row asserted R10 as §1.12 consumer; `Grep "§1\.12" R10.md` returns NO matches (R10's §1.12 row in audit is a PHANTOM CITE — R10 cites §1.9, §1.2, §1.4, §1.5, NOT §1.12).
- `Dropbox/bom-reader-private/01-method/colometry-canon.md:560` and `:636` and `:642`: cite §1.12 token directly — but the framework.md §1.12 has been ARCHIVED. These cites land on a section that no longer exists in the live spec; they survive only because cross-corpus-principles.md hosts the substance.

## §1.13 — Authorial asymmetry overrides editorial symmetry

- `readers-gnt/validators/canon/check_canon_alignment.py:339-348` cite by audit row was at `readers-gnt/private/01-method/check_canon_alignment.py:339-348` — WRONG PATH; actual location is `readers-gnt/validators/canon/check_canon_alignment.py`. Substance matches, path wrong.
- `atu-method/scholarship/gnt/R28-ext.md`: audit claims §1.13 consumer; `Grep "§1\.13" R28-ext.md` returns NO matches. PHANTOM CITE for §1.13 specifically (R28-ext.md may discuss R28 substance but does not cite the §1.13 token).
- `atu-method/scholarship/bofm/R28.md`: only ONE §1.13 reference (line 132), and it's a META-PROPOSAL to rename — not a substantive consumer of §1.13's normative text.

