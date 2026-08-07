---
name: feedback-always-recommend-in-options
description: "Every decision put to Stan carries three parts: a recommendation, WHY that one, and its potential CONS — never a neutral menu, never a bare pick"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/154c6c6ede1b6f0f@v2`); state as of 2026-05-25 (snapshot mtime); possibly stale — re-verify before relying.

When presenting Stan a multi-option decision (AskUserQuestion or prose options), **always include an explicit recommendation** — make it the first option with "(Recommended)" in the label, and state *why* in the lead-in. Stan: "i always expect a recommendation among the options."

**Why:** Stan delegates decisively and wants Claude's judgment surfaced, not a neutral menu that pushes the analytical work back to him. A menu without a pick wastes his bandwidth (ties to [[feedback_stan_thinks_claude_files]] — reserve his bandwidth for synthesis, not adjudicating options Claude could rank).

**How to apply:** Every AskUserQuestion gets a "(Recommended)" option in slot 1 + a one-line rationale before the call. If genuinely torn, still pick and say it's close. Never offer 2-4 equal-weight options with no steer. This holds even for irreversible/public-action forks — recommend, then let him veto.

**EXTENDED 2026-08-07 (Stan, verbatim): "for decisions, i always want a recommendation and a why you're recommending it and what the potential cons are."** So the shape is three parts, not one, and it applies to *any* decision surfaced in prose — not only formal AskUserQuestion calls:

1. **The recommendation** — one option, named.
2. **Why that one** — the reasoning that made it win, not a restatement of what it is.
3. **The cons of the recommended option** — what it costs, what it risks, what it forecloses. This is the part that was missing: a recommendation with only upside reads as advocacy, and Stan cannot weigh a pick whose downside he has to infer. State the cons of *the thing being recommended*, not merely the drawbacks of the alternatives.

If a recommendation has no meaningful cons, say so explicitly rather than omitting the section — "no real downside; the cost is ten minutes" is information. Silence there reads as an oversight.
