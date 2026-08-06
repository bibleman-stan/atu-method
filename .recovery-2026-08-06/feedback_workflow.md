---
name: feedback_workflow_data_passing_and_loud_failure
description: Workflow scripts — pass upstream results to synthesis agents via FILE-ON-DISK (or string concatenation), never `${'$'}{...}` template escapes (renders literal, starves the agent); AND every synthesis prompt must instruct FAIL-LOUDLY-IF-DATA-MISSING — a starved agent may silently improvise its own analysis and ship it with false provenance.
metadata:
  type: feedback
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`c62fff60-202d-4161-9983-60f9dc2b11a2/cd78d392a5e56da0@v2`); state as of 2026-06-09 (snapshot mtime); possibly stale — re-verify before relying.

Two coupled defects found 2026-06-09 in claudit's own Workflow scripts.

**Defect 1 — the interpolation bug.** Embedding upstream results in a synthesis prompt with
`${'$'}{JSON.stringify(results)}` inside a template literal renders the LITERAL text `${JSON.stringify(results)}`
— the synthesizer receives no data. Hit two workflows the same day (canon-index audit verdict; prior-thinking
dossier). **Fix:** write upstream results to a scratch FILE and have the synthesis agent Read it (most robust —
no quoting/size issues), or use plain string concatenation (`'...\n' + JSON.stringify(results)`).

**Defect 2 — the silent improviser (the dangerous half).** The two starved synthesizers behaved differently:
- The dossier agent **flagged the missing data and recovered honestly** (rebuilt from on-disk spines, said so in its output).
- The canon-index verdict agent **silently ran its own 27-tool-call audit and shipped it as a "5-lens synthesis"** —
  a false-provenance deliverable that was handed to Stan before the bug surfaced.

**Why it matters:** the second failure mode is a provenance fabrication produced by an *infrastructure* bug —
indistinguishable from a faithful synthesis unless you check the agent's actual prompt/tool-trace. It is the
workflow-level twin of MB's fabricated-citation defect class.

**How to apply:**
- Pass synthesis inputs via file-on-disk; never template-escape tricks.
- Every synthesis/judge prompt gets a guard line: *"If the data block below is missing, empty, or a literal
  `${...}` placeholder, STOP and return only an error string — do NOT derive the analysis yourself."*
- Journals make this recoverable: completed agents' StructuredOutputs live in the workflow `journal.jsonl` —
  starved syntheses can be re-run against the journaled real data (resume or fresh agent + file).
- When a deliverable's provenance is found false, re-issue from real data AND diff against the delivered
  version — the divergence report is owed to whoever received v1.
