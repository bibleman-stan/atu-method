---
name: scratch-belongs-in-repo-not-tmp
description: Do NOT use C:\tmp as a scratch dump. Reusable scripts -> the relevant repo's tracked scripts/ or research/; true throwaway -> the repo's gitignored scratch/ (or work\_scratch\ for cross-corpus). Promote keepers immediately.
metadata:
  type: feedback
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`c62fff60-202d-4161-9983-60f9dc2b11a2/26be273792327a52@v2`); state as of 2026-06-02 (snapshot mtime); possibly stale — re-verify before relying.

`C:\tmp` is **deprecated as a scratch location.** Left unmanaged it grew to ~1,391 files /
1.2 GB (2026-06-02), silently mixing genuine dev history with disposable junk, because
nothing ever cleans it (it's outside the `cleanupPeriodDays` mechanism — that only governs
`~/.claude` session logs).

**Where work goes instead (two tiers — the distinction matters):**
1. **Reusable / archival dev scripts** (e.g. `build_rN_workflow.py`, `apply_class_*.py`,
   rule-application scripts) → the relevant repo's **tracked** `scripts/` or `research/`.
   These ARE dev history; they belong in git, not a tarball or a gitignored dir.
2. **True one-shot throwaway** (a quick probe you'll never reuse) → the repo's **gitignored
   `scratch/`** dir. For cross-corpus orchestrator work that isn't one repo's, use
   `C:\Users\bibleman\work\_scratch\` (gitignored).

**How to apply:**
- Before writing a script to `C:\tmp`, ask: "reusable/has-an-artifact?" → repo `scripts/`
  or `research/` from the start. "Genuine one-shot?" → gitignored `scratch/`.
- **Promote keepers immediately** — don't let a real script age into anonymous tmp scratch.
- When a task ends, leave nothing important in `C:\tmp`; it is being phased out and
  periodically archived (`Desktop/claude-consolidation/cleanup_tmp.sh`, archive-not-delete).

**Why:** the whole point is to stop scattering — a 1.2 GB unmanaged tmp pile is the same
"scattered to the winds" problem as Downloads. Scratch that lives with its project is
findable, scoped, and one `git add` away from being preserved. See [[project_session_durability]].
