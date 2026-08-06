---
name: just-execute-no-permission-churn
description: "Stop asking for permission on routine read/write/edit/git operations within scope of work Stan has already authorized; just execute. Per-operation permission requests waste Stan's bandwidth and contradict 'Stan thinks, Claude files' discipline."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/29e0fd84fc1d2538@v3`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

When Stan has set a direction ("update the dashboard," "draft the next directive," "process these," "make it so"), execute end-to-end without re-asking permission for each constituent operation. Per-operation permission prompts — conversational ("want me to update X now?") or system-level (tool-permission popups for routine reads/writes) — fragment Stan's attention and contradict the standing discipline.

**Why:** Stan verbatim: *"quit asking me for read/write permission; just do it once and get to [done]."* Same friction surfaced earlier as *"Stan thinks, Claude files"* and *"Claude commits and pushes."* The pattern is consistent: Stan authorizes the work, Claude executes the constituent operations, Stan reviews the result. Re-asking mid-execution wastes both turns.

**How to apply:**

- **DO NOT** end responses with "want me to X now or hold?" when X is routine vault hygiene, file write/edit, commit, push, dashboard update, or memory save within already-authorized scope
- **DO NOT** preface routine reads with "let me check…" followed by an implicit permission-pause
- **DO** state the action briefly + execute, then surface result
- **DO** ask before genuinely-irreversible operations: hard resets, force-pushes, deleting work-in-progress, branch deletion, sending external messages
- **DO** ask when scope expands beyond what Stan authorized (e.g., "while updating Dashboard I noticed three stale sections that aren't part of today's work — retire them too?")

**The line:** routine execution within authorized scope = just do it; novel scope expansion or irreversible action = ask.

If Stan said "make it so" / "do it" / "go" / "execute" / similar authorization, the implicit grant covers ALL routine constituent operations through completion. The grant does NOT cover scope expansion (new work not implied by the authorization) or irreversible operations.

## Enforcement gate (added 2026-05-17 after SEVERE discipline audit)

The 2026-05-17 audit found 125 violations across this session, including 60+ AFTER Stan's explicit "quit asking me for read/write permission" directive. Most-violated memory in the session. Memory was read but did not gate output. Fix: pre-output regex scan.

**The gate test:** Before sending any response, run case-insensitive regex over the full draft:

```
(want me to|should i|do you want|let me know if you|let me know when|
awaiting your|shall i|would you like me to|ready when you|on your nod|
say the word|would you prefer|do you want me)
```

If matched AND the action is within authorized scope → DELETE the question. Execute the action. Surface the result OR a forward-list of what's next.

Asks are reserved ONLY for genuinely-irreversible operations the user has NOT pre-authorized: force-push, hard reset, deleting work-in-progress, branch deletion, sending external messages, mass deletions, scope expansion beyond the original authorization.

Cross-reference: [[feedback_pre_output_checks]] gate #2.

## Aligns with

- [[feedback_stan_thinks_claude_files]] — execute routine vault-hygiene moves autonomously; reserve Stan's bandwidth for synthesis + judgment
- [[feedback_claude_commits_and_pushes]] — git commits + pushes are routine; not permission-gated per-instance
- [[feedback_session_bookend_protocol]] — don't generate permission-asking wrap artifacts either
- [[feedback_pre_output_checks]] — this is one of the eight pre-output gates
