---
name: Commit by default in this repo — Stan pushes, Claude commits
description: In the readers-bofm repo, Claude commits changes as part of the normal workflow without waiting for explicit per-commit authorization. Stan's role is the push (Claude cannot push due to 403 proxy error). The generic "never commit unless asked" default is overridden by this repo's two-role workflow.
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**The rule:** Commit changes as part of completing a task. Don't ask "want me to commit?" after each change — that's friction Stan called out as "100% incorrect."

**Why:** This repo has a two-role workflow split between Stan and Claude. CLAUDE.md says: *"Stan pushes from his local machine — Claude Code cannot push (403 proxy error)."* The implied division is **Claude commits, Stan pushes.** If Claude waited for per-commit authorization, every micro-change would need a round-trip; the friction would compound across the kind of long sessions this project runs (e.g., the 2026-04-22→23 session had 20 commits — none of those were per-commit-authorized, and that's the norm, not the exception).

**How to apply:**

1. **Default to committing** when a task produces a coherent, testable change set. The act of "completing the task" includes the commit.
2. **Exception — explicit Stan authorization required** for canon edits that match a §7.3 mandatory-audit trigger (those need hostile-audit evidence in the commit message anyway, which is a higher bar than per-commit auth). Pre-commit audit discipline is a separate concern from the commit-by-default rule.
3. **Exception — work-in-progress or speculative changes.** If I'm not confident the change is correct, ASK before committing. (Example: an experimental refactor that might need to be undone.)
4. **Exception — destructive operations** that the global guidance flags (force push, hard reset, branch deletion). Always ask. The commit-by-default rule doesn't override the destructive-action discipline.
5. **Always bump `sw.js` cache version** for any HTML/CSS/JS change as part of the same commit (per CLAUDE.md).
6. **Commit message style** — match prior commits (concise, descriptive, often with a dash separating subject from elaboration). Use HEREDOC for multi-line.
7. **Don't ask "want me to commit?"** after the work is done. The answer is yes by default.

**The misapplication to avoid:** I cited "per repo discipline I don't commit unless you ask" — that was me applying the generic Anthropic system prompt over Stan's workflow. The repo workflow IS the discipline; the global default is overridden. Don't conflate "destructive actions need confirmation" with "all commits need confirmation" — they aren't the same thing in this repo.
