---
name: broad-shell-no-permission-hang
description: Stan broadly authorizes BOTH Bash and PowerShell; never let a shell command hang on a per-command permission prompt
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/d04394f933d37c7c@v2`); state as of 2026-05-29 (snapshot mtime); possibly stale — re-verify before relying.

Stan broadly authorizes shell execution — **both Bash AND PowerShell** — and does not want commands hanging on per-command permission prompts (the process blocks indefinitely when he steps away from the keyboard).

**Why:** repeated permission prompts on PowerShell commands left the process "hanging up… just waiting there" while Stan looked away (2026-05-29). `"Bash"` was already a broad allow in `~/.claude/settings.json` (`permissions.allow`), but PowerShell was only whitelisted for ~50 exact command strings, so any *new* PowerShell invocation prompted and stalled.

**How to apply:** `"PowerShell"` was added to `permissions.allow` (broad, like `"Bash"`) on 2026-05-29 — both shells now run prompt-free. If a shell command ever *would* prompt, treat that as a settings-allow gap to fix, not a reason to wait. Operate with broad shell authority: just run it, report after. (Ties to [[feedback_just_execute_no_permission_churn]] and [[feedback_workflow]].)
