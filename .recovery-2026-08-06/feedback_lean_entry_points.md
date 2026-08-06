---
name: lean-entry-points
description: "When rewriting docs after a methodology shift, do surgery, not travelogue. CLAUDE.md is read EVERY wake — keep it lean (~150-200 lines max). Per-repo Claudes need a tight entry point that surgically excises deprecated content and points to detailed references elsewhere. Full methodology, empirical justification, performance tables, protocol details belong in atu-method/docs and atu-method/memories (read on-demand, not every wake). Adding comprehensive 'Production tier' or 'New approach' sections to CLAUDE.md bogs down every per-repo Claude on every wake."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/b46b693b4ed8d96c@v2`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** When updating CLAUDE.md or other per-repo wake-time entry points to reflect a methodology shift:

1. **Surgically chop deprecated content.** Identify what's "cancerous didn't-work" — methodology that was empirically falsified or superseded — and excise it. Old framework terminology (J1-J5, M1-M4, three forces, Layer 1/3 etc. as of 2026-05-17) gets removed, not rewritten in place.

2. **Add a short pointer for new state.** One or two lines max in CLAUDE.md saying "see `../atu-method/docs/X.md` for current methodology." Resist the urge to summarize the new state in detail at the entry point.

3. **Full detail lives elsewhere.** Authoritative methodology in `atu-method/docs/`; discipline memories in `atu-method/memories/`; empirical justification + performance tables in dedicated memory files. These are accessed on-demand when relevant.

4. **CLAUDE.md target size: ~150-200 lines.** Longer than that = bloat. Per-repo Claudes read this on every wake; every extra line is a per-wake tax. Reserve the budget for OPERATIONAL discipline that fires on every interaction (audit-then-apply, change protocol, directive queue, compaction-resume, git workflow, model routing). Methodology theory and empirical justification belong in references.

**Why:** Stan verbatim 2026-05-17: *"surgery is the right analogy: we chop out the cancerous 'didn't work'; we have seen less is more when it comes to making sure they don't bog down, so the claude.md isn't the place for your huge travelogue version of this stuff; if you want to describe it elsewhere and tell them to read, great."*

The anti-pattern: adding a comprehensive "Production tier" or "Updated methodology" section to CLAUDE.md with empirical tables, protocol details, and full rationale. The per-repo Claude doesn't need all that on every wake. It needs to know (a) the discipline, (b) where to look up the methodology when needed.

**How to apply:**

- When asked to "cascade an update through docs and memories," default to surgery: remove deprecated; add SHORT pointers; preserve operational discipline.
- For methodology details: write ONE authoritative reference doc (in `atu-method/docs/`); write ONE memory (in `atu-method/memories/`); point CLAUDE.md at both with a one-line each.
- Resist agent instructions that say "add a section with the new approach" — that builds bloat. Instead "surgically excise deprecated terminology; add one-line pointer to the new reference."
- For multi-doc cascades: dispatch agents with explicit "preserve length budget; reference, don't restate" guidance.

**Anti-pattern to watch:** subagents asked to update CLAUDE.md often expand it by adding comprehensive new sections. They mean well but produce travelogue. Spec them tightly with explicit length budget AND explicit "reference, don't restate."

## Aligns with

- [[feedback_doc_rewrite_no_preamble]] — same family: don't preface with history; present the current state cleanly. This memory adds: keep entry points lean, even when presenting current state.
- [[feedback_simplicity_bias]] — reduce noise; reader bandwidth (per-wake context budget) is the scarce resource.
- [[feedback_just_execute_no_permission_churn]] — entry points should enable execution, not gate it with theory.
