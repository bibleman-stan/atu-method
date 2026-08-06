---
name: three-lens-default-for-plans
description: "When proposing ANY non-trivial plan, design, trigger message, paste-prompt, directive, or methodology decision — BEFORE finalizing and putting it in front of Stan — dispatch ≥3 parallel adversarial audits from coding / NLP-domain / workflow lenses. Each lens finds holes the other two miss. This is the plan-level gate; the existing pre-output regex/temporal gates are the response-level gate; the §7.3 audit gate is the code-change gate. All three layers must run. Memorialized 2026-05-17 after Stan flagged that not running the three lenses by default has produced repeated Stan-time waste + near-misses (86-decision review surface, API-key trigger, Stage-3 write-to-v2/heb cascade, hand-wavy paste-prompts, over-claimed accuracy numbers)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`786b3dcf-7033-47ce-86b0-0913576303a8/20679e152c30e194@v2`); state as of 2026-05-18 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** Before any non-trivial plan / design / trigger / directive / methodology proposal lands in front of Stan, dispatch ≥3 parallel adversarial audits from these three independent lenses:

1. **Coding / engineering best practices** — modularity, abstraction boundaries, test coverage, error handling, concurrency, branch + rollback strategy, dependency management, code smells, technical debt, cascade safety, hook discipline, single-source-of-truth violations.

2. **NLP / corpus linguistics / domain quality** — empirical validation rigor, sample size, genre coverage, theoretical grounding, literature consistency, linguistic correctness of constraints, IR-layer assumptions, cross-corpus claims, over-claims vs evidence.

3. **Project workflow / Stan-bandwidth / sustainability** — Stan-time realism, cadence sustainability, multi-Claude coordination, failure-recovery latency, scope discipline, exit criteria, single-point-of-failure risk, cost model realism, methodology vs text-shipping balance.

Each lens gets independent context + a hostile prompt instructed to find holes, identify what was missed, poke for what's still wrong. Run all three in parallel via Agent dispatch (one message, three Agent calls).

**Why:** The 2026-05-17 session produced a sequence of Stan-flagged failures that any of the three lenses would have caught pre-emptively:

| Failure | Which lens would have caught it |
|---|---|
| 86-decision per-batch review surface | Workflow |
| API-key reference in Tanakh-Claude trigger | Coding |
| Stage-3 instruction to write to v2/heb pre-adjudication | Coding |
| "Or whatever Tanakh's three-check equivalents are" hand-wave | Workflow / Coding |
| 73% UNANIMOUS treated as auto-applicable (correlated-errors blind spot) | NLP |
| 5-chapter 94%/100% accuracy as production validation | NLP |
| 26-entry catalog treated as grammar-derivation when empirically grown | NLP |
| Stan-bandwidth budget of 40-60 hours for Tanakh | Workflow |
| `_CLUSTER_DIRECT_REGISTRATIONS` dual-source-of-truth silent-skip bug | Coding |
| Pre-commit auto-stage glob picking up unrelated working-tree state | Coding |
| Memories-as-articles vs memories-as-gates structural failure | Workflow (meta) |

Each of these wasted Stan-time + introduced near-miss damage. The structural pattern: I was reasoning in one lens at a time (usually engineering, occasionally methodology, rarely workflow) and never subjecting my own proposal to the other two. Self-audit only happened after Stan explicitly flagged the failure.

**Stan verbatim 2026-05-17:** *"it troubles me you don't say yes — THESE are the dimensions you should be thinking through carefully before wasting my time and potentially ruining my project."*

**How to apply:**

1. **Identify the trigger.** Any of:
   - Trigger message / paste-prompt for another Claude (Tanakh-Claude, GNT-Claude, future repo-Claudes)
   - Directive draft for `directives/pending/`
   - Multi-step plan ≥3 steps
   - Design proposal touching architecture, catalog, pipeline, cascade
   - Methodology decision (new gate, new criterion, new closed list, retraction)
   - Cost / cadence / Stan-bandwidth claim
   - Anything proposing autonomous-run behavior

2. **Compose the three lens prompts.** Each prompt:
   - Names the lens explicitly
   - Lists the files/repos the agent must read to ground critique
   - Inlines the proposal verbatim (do not paraphrase)
   - Lists 10-15 specific questions the lens should hunt for
   - Requests format: severity-tagged findings + top-3 actions

3. **Dispatch parallel** (one message, three Agent calls, `run_in_background: true`).

4. **Wait for all three.** Do NOT pre-emptively revise the proposal based on one audit's findings before the others return. Cross-lens patterns (where multiple audits converge on the same hole from different angles) are the highest-signal findings.

5. **Integrate findings into v2 proposal.** Surface to Stan as: original proposal + audit verdicts + integrated v2. Don't ask permission to integrate; do it.

6. **Don't ship until findings are integrated.** "Audit found MUST-FIX, plan continues unchanged" is not a defensible position.

**Cost:** ~$6-15 per plan-cycle (3 Sonnet agents × ~10-15 min wall-time × ~$2-5 each). Cheap insurance compared to a Stan-flagged failure that wastes hours.

**When this does NOT apply** (trivial-fix carve-out):
- Single-line bug fix with obvious diagnosis
- Doc rewording / typo correction
- Memory update with no behavioral change
- Routine constituent operation within already-audited scope (writes, edits, commits within Stan-authorized work)
- Response to a direct Stan question that doesn't propose new infrastructure or workflow

**When in doubt: dispatch the audits.** False-positive cost (3 audits on something simple) is ~$10 + 15 min. False-negative cost (skipping audits on something non-trivial) is Stan-frustration + project damage. Asymmetric — favor the audits.

## Aligns with

- [[feedback_pre_output_checks]] — response-level regex/temporal gates (8 checks per turn). This memory is the plan-level analog: 3 parallel-audit gates per proposal.
- [[feedback_never_skip_audit_gate]] — code-change gate (§7.3 audit before any code touching constraint mechanism / closed list / sub-category / rule). This memory is the broader proposal-validation gate, fires on proposals BEFORE they reach the code-change stage.
- [[feedback_parallel_default]] — three lenses dispatch in parallel, one message, not sequential.
- [[feedback_just_execute_no_permission_churn]] — do not ask Stan permission to run the audits; running them is the discipline, not a decision point.
- [[feedback_no_handwave_in_precision_artifacts]] — each lens prompt must itself be precise (no "or whatever / or similar" in audit prompts).

## The structural diagnosis

Pre-output checks (response level) + three-lens audits (plan level) + §7.3 audits (code level) form a defense-in-depth pattern. None alone catches everything; each catches what the others miss. The recurring 2026-05-17 failure mode was operating with only the third layer (and inconsistently). Running all three layers by default is the discipline. The cost is bounded; the savings on Stan-time and project-trajectory damage are not.
