---
name: Scripts before agents for mechanical corpus sweeps
description: Before dispatching agents for a corpus-wide pattern, ask "can this be done with grep, sed, or a short Python script?" If yes, script it. Agents take minutes and tokens; scripts run in milliseconds. Dispatch agents only when the rule requires per-item judgment the script can't encode.
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**Rule.** Before dispatching agents for a corpus-wide pattern, ask:

- Can this be resolved with `grep` / `Grep` / `re.sub` / a short Python script?
- If yes → write the script, run it, commit.
- If no (requires reading comprehension, per-item editorial judgment, context-sensitive decisions the rule can't encode) → dispatch agents.

**Why:** Agents take 60-300 seconds each and consume context + tokens. Scripts run in milliseconds at zero context cost. The BofM-specific trap: many "sweeps" that feel judgment-heavy are actually deterministic once the rule is articulated (e.g., Rule 17 complement-integrity, Rule 19 predicative-identifier, Rule 9 dangling conjunctions). Those are Python territory, not agent territory.

**How to apply:**
- Word/phrase replacement → Python `str.replace` with safety check (contextual grep before + after).
- Regex-matchable pattern → Python `re.sub` or `Grep` tool.
- Rule with unambiguous mechanical trigger (per `CLAUDE.md` §Source Rules "rule-derivative changes are Category A") → script it.
- Agents → only when the rule requires contextual judgment the code can't encode.

**Diagnostic.** If the agent prompt is "for each item, do X" and X is deterministic, you wanted a script. If X is "decide whether to do the thing," dispatch.
