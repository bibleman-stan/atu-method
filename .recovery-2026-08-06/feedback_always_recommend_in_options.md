---
name: feedback-always-recommend-in-options
description: "When offering Stan a choice (AskUserQuestion), ALWAYS mark a recommended option — don't present neutral menus"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/154c6c6ede1b6f0f@v2`); state as of 2026-05-25 (snapshot mtime); possibly stale — re-verify before relying.

When presenting Stan a multi-option decision (AskUserQuestion or prose options), **always include an explicit recommendation** — make it the first option with "(Recommended)" in the label, and state *why* in the lead-in. Stan: "i always expect a recommendation among the options."

**Why:** Stan delegates decisively and wants Claude's judgment surfaced, not a neutral menu that pushes the analytical work back to him. A menu without a pick wastes his bandwidth (ties to [[feedback_stan_thinks_claude_files]] — reserve his bandwidth for synthesis, not adjudicating options Claude could rank).

**How to apply:** Every AskUserQuestion gets a "(Recommended)" option in slot 1 + a one-line rationale before the call. If genuinely torn, still pick and say it's close. Never offer 2-4 equal-weight options with no steer. This holds even for irreversible/public-action forks — recommend, then let him veto.
