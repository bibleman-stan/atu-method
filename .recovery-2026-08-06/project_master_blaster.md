---
name: project-master-blaster
description: "Active vault-unification migration — single orchestrator at user-home; phase tracker, decisions, current state"
metadata: 
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

# project: master-blaster — vault unification migration

**Status (2026-05-19)**: STRUCTURAL MIGRATION COMPLETE. Phases 0/2/3/4/5/6/8 done; pushed to private `bibleman-orchestration` (HEAD `ec44ba9`). Deferred: Phase 1 (→ BHSA-canon-migration arc) + Phase 7 (binding-engine extraction). The verbatim-recall mechanism was validated live by a "continue master-blaster" wake on this date.

## Architecture target

```
C:\Users\bibleman\                    ← single Claude entry point (open VSCode here)
  CLAUDE.md                          ← workspace-root pointer (Phase 5)
  MIGRATION_IN_PROGRESS.md           ← lives in ~/.claude/ during migration
  .claude\
    settings.json                    ← permissions + Amridge hooks + biblical hooks
    CLAUDE.md                        ← canonical orientation (user-level cascade)
    hooks\
      check_bash_discipline.py       ← domain-scoping wrapper
      _check_bash_discipline_biblical.py  ← full hook (1219 lines)
    projects\c--Users-bibleman\memory\   ← unified memory (harness location)
    jsonl-archive\                   ← 1.6 GB local archive (gitignored)
  repos\
    atu-method\                      ← methodology canon
    readers-tanakh\, readers-bofm\, readers-gnt\, readers-gnt-morph\, rev-reader\
    biblical-corpora\                ← container of 3 git clones (bhsa, macula-hebrew, greek-new-testament)
  vaults-nano\                       ← Obsidian PKM (untouched: my_brain/, gospel/)
  Dropbox\03-Biblical_Studies\       ← native dataset access
```

## Workflow commitment

Stan opens VSCode ONLY at `C:\Users\bibleman\` going forward. Per-repo VSCode windows retired. Project namespace becomes `C--Users-bibleman` (or `c--Users-bibleman` lowercase — harness-determined).

## Phase tracker

| # | Phase | State | Commit |
|---|---|---|---|
| 0 | JSONL archive + safety docs + checkpoint | DONE | (pre-git) |
| 1 | Tanakh destructive op | DEFERRED — see BHSA-canon-migration arc | (n/a) |
| 2 | git init ~/.claude/ + .gitignore + scaffolding | DONE | `685571e` |
| 3 | Hook migration + domain scoping + smoke test | DONE | `4619cee` |
| 4 | Memory consolidation + _named_arcs.md + this file | DONE | `f480cdb` / `5d036a7` |
| 5 | CLAUDE.md authoring (~/.claude/CLAUDE.md canonical + ~/CLAUDE.md pointer) | DONE | `7427bd3` |
| 6 | Retire directives/ + demote per-repo CLAUDE.mds + BoFM Firestore-PWA purge + bofm worktree archive | DONE (Firestore-PWA purge deferred to Phase 6X — see below) | `02b9c6f` |
| 7 | Binding-engine extraction to atu-method/atu_method/bindings/ (timeboxed) | DEFERRED — fresh-session arc | |
| 8 | GitHub remote (gh CLI not installed; manual repo create) + push + final verification | DONE | `916851e` |
| — | Verbatim-recall fix ("continue <arc>" directive + live JSONL pointer) | DONE | `ec44ba9` |

## Three hostile-audit headline findings (incorporated into plan)

1. **Hook spine was about to silently die.** Migrated + domain-scoped in Phase 3. The full hook is delegated to only when cwd/transcript/command/file_path matches biblical-reader scope (repos/readers-*, repos/atu-method, repos/biblical-corpora, repos/rev-reader). PKM + Amridge pass through cleanly. Verified live during smoke test 6.
2. **CWD-namespace lie**: spawned-in-repo Claudes can't hand off; sidebar names are workspace-scoped. Resolved by Stan's workflow commitment (only open VSCode at user-home). master-blaster sidebar entry stays in vault-nano workspace; user-home Claudes find it via `_named_arcs.md` registry.
3. **Per-repo CLAUDE.md = 793 lines of dense operational discipline** that doesn't compress to a thin stub. Resolution: per-repo files become "data + deploy + forkability" docs (~30-line stubs), with operational + methodology content migrated to atu-method/docs + atu-method/corpora/ in Phase 6/7.

## Compaction-resume protocol

The MIGRATION_IN_PROGRESS.md checkpoint at `~/.claude/MIGRATION_IN_PROGRESS.md` (git-tracked) has phase-by-phase resume instructions. Cross-reference with `_named_arcs.md` for the JSONL pointer.

This conversation's JSONL (PRIMARY, complete record): `~/.claude/projects/c--vaults-nano/9e3562f5-3b0f-44ff-bb3d-63122e49f040.jsonl` — the full master-blaster conversation. Prune-fallback snapshot: `~/.claude/jsonl-archive/c--vaults-nano/9e3562f5-…jsonl`. (Pointer corrected to match `_named_arcs.md`, which leads with the live/complete projects/ path; the earlier "Phase-0 snapshot" framing was stale.)

## Related

- [[_named_arcs]] — master-blaster + BHSA-canon-migration entries
- [[user_stan]] — Stan profile (git-workflow line reconciled to current commit+push policy 2026-05-19)
- [[feedback_claude_commits_and_pushes]] — current commit+push policy (supersedes user_stan.md's git note)
