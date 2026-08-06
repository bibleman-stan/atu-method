---
name: no-handwave-in-precision-artifacts
description: "Hand-wavy language (or whatever, or similar, TBD, discover from, figure out) is BANNED in precision artifacts: trigger messages, directive files, design documents, sub-agent prompts, scheduled-task definitions, commit messages, prompts passed between agents. These artifacts are read by other Claudes / Stan / future-me as authoritative; hand-waving in them = passing the buck. Stan flagged this 2026-05-17 ('UNACCEPTABLY SLOPPY WORK — YOU GO EFFING FIGURE OUT WHAT IT IS AND MAKE YOUR PROMPT PRECISE') after I wrote 'or whatever Tanakh's three-check equivalents are; discover from CLAUDE.md/scripts/ on wake' in a trigger message he was about to paste."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`8ad64085-f7d5-4845-9324-ac4e9c7f9e54/59f7cfa271f4a330@v2`); state as of 2026-05-17 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** When writing any precision artifact — trigger message, directive file, design document, sub-agent prompt, scheduled-task definition, commit-message body, paste-prompt for another Claude — every name, path, command, version, ID must be CONCRETE and VERIFIED. Hand-wavy substitutes are banned.

**Banned patterns** (case-insensitive regex; scan the artifact before send/paste):

```
(or whatever|or similar|or equivalent|TBD|discover from|figure out|
somewhere around|something like|approximately the|find the right|
the relevant|whatever fits|as appropriate|or analogous)
```

**Why:** Hand-waving in a precision artifact is the pass-the-buck failure mode. The artifact's reader (peer Claude, future-me, Stan) has to do the homework I should have done. When the reader is another Claude running autonomously, hand-waving creates real cost: it may interpret the gap differently than intended, OR it may silently fail to find the missing concrete value. Stan verbatim 2026-05-17: *"YOU GO EFFING FIGURE OUT WHAT IT IS AND MAKE YOUR PROMPT PRECISE."*

**The specific incident (2026-05-17):** I composed a trigger message for Stan to paste into Tanakh-Claude initiating Torah render (directive 1700). My v2 of the trigger contained:

> "Run the full cascade: scripts/regenerate_english.py for the batch's chapters → scripts/build_books.py → check_cascade_alignment.py (or whatever Tanakh's three-check equivalents are; discover from CLAUDE.md/scripts/ on wake)."

The actual correct precision is one Bash command away. Tanakh's pre-commit hook is at `validators/hooks/pre-commit` and invokes `scripts/refresh_book.py --book <NN-book> --build`, which sequentially runs `apply_validators.py → propagate_editorial_layers.py → regenerate_english.py → build_books.py`. The hook auto-stages derived layers, then `validators/run_all.py --baseline-check` enforces the regression gate. That's the concrete cascade. Hand-waving "or whatever" instead of looking that up was the failure.

**How to apply:**

1. **Before pasting any prompt / writing any artifact**: scan the draft for the banned-pattern regex above.
2. **If matched**: STOP. Look up the actual value. Read the file, grep the codebase, run the command, check the path. The lookup is almost always one tool call.
3. **If genuinely unknown after lookup**: mark with `<<UNKNOWN — must resolve before paste>>` and surface to Stan as an explicit blocker. NEVER paste with the unknown in place — Stan will (correctly) read it as buck-passing.
4. **For sub-agent prompts specifically**: imagine the agent is offline-only with no internet and no project context. Every reference must be self-resolvable from the prompt or from explicit file paths the agent can read. If your prompt says "use the standard pattern" without specifying where the standard pattern is documented, the agent will guess.

**Concrete pre-send check (pseudocode):**

```python
banned = re.compile(
    r"or whatever|or similar|or equivalent|TBD|discover from|figure out|"
    r"somewhere around|something like|approximately the|find the right|"
    r"the relevant|whatever fits|as appropriate|or analogous",
    re.IGNORECASE,
)
for line in artifact.splitlines():
    if banned.search(line):
        raise ArtifactPrecisionError(f"Hand-wavy language in: {line!r}")
```

If you're tempted to write "or whatever" because you don't remember the exact name, that's the signal that you haven't done the lookup. The lookup is part of the work.

## Aligns with

- [[feedback_pre_output_checks]] — this is gate #5 in the pre-output scan.
- [[feedback_just_execute_no_permission_churn]] — same family: do the homework, don't defer it.
- [[feedback_stan_writes_claude_edits]] — Stan's prose is precise; Claude's prose to other agents must match that standard.
- [[feedback_never_skip_audit_gate]] — when Stan asks for a hostile audit on something I composed, the audit will find the hand-waves; better to scan myself first.

## The diagnostic underneath

Hand-waving in precision artifacts has the same shape as skipping an audit gate: in both cases, the discipline says "do the careful thing now" and the temptation says "good enough, move on." Both are accumulated risk. The §7.3 audit gate catches design-time hand-waves before code lands; this rule catches artifact-time hand-waves before paste.
