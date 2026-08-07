---
name: atu-compaction-resume
description: Recover working state after a compaction or a session resume in atu-method or a reader repo. Use whenever the session opens with "This session is being continued", an isCompactSummary marker, a degraded/summarized context, or a request to resume a named arc such as "continue master-blaster". Reconstructs state from the session JSONL and from git rather than from the harness summary.
---

# Compaction-resume — the summary is degraded, the JSONL is not

On compaction the harness summary is **lossy**; the on-disk session transcript is not. What is lost is the context window, never the JSONL. So resume by reading the record, not by trusting the recap.

## 1. Dump the real transcript first

Before any substantive response, read the last 30–35 user/assistant exchanges **verbatim** from the session JSONL. Newest file under:

```
~/.claude/projects/<cwd-slug>/*.jsonl
```

The slug for this repo is `c--Users-bibleman-repos-atu-method`. The full command form lives in `memories/operational/feedback_compaction_resume_protocol.md`.

Do this even when the summary looks complete — the failure mode is a summary that reads coherently while having dropped the specific decision you are about to contradict.

## 2. Re-enumerate state from ground truth, never from recall

- **Deploy state** → `2-evidence/deployment-status.md` plus the git log of the live directory. Never infer it from a per-repo README or from memory; those drift.
- **In-flight work** → `git status --short` and `git log --oneline -10` in the repo *and* in the relevant reader repo.
- **Parked work** → `memories/operational/_deferred_queue.md`.
- **Never recall a pre-compaction comparative number** (an F1, a pass rate, a diff count) without re-running the gate that produced it. If re-running is impractical, say the number is unverified rather than repeating it.

## 3. Do not re-litigate settled decisions

`memories/operational/_north_star.md` and the "Closed routes / banked-gold / settled tactical" section of `CLAUDE.md` are the settled layer. Post-compaction Claude has historically re-opened exactly these — run-vs-close, SUD-fork, data placement, genre holds. Treat everything there as closed unless Stan reopens it.

**Caveat as of 2026-08-06:** the recovered operational memory reflects state from 2026-06-01 to 2026-06-15 (the namespace was deleted and restored from file-history). Anything decided between mid-June and August is not in it. Treat those files as "current as of mid-June" and verify against git before relying on them.

## 4. Named arcs

To resume "continue master-blaster" or any named arc: `memories/operational/_named_arcs.md` holds the registry with JSONL pointers into `~/.claude/jsonl-archive/<namespace>/<session-id>.jsonl`. Sessions between mid-June 2026 and the 2026-08-06 recovery are not registered there.

## 5. Then continue the cascade, don't restart it

Compaction-resume means **continue the in-flight work**, not re-plan it. Enumerate state, state what was in flight, and pick it up.
