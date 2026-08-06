---
name: subagent-specs-require-receipts
description: "Every sub-agent / Workflow spec that names a file, module, function, lemma, or feature value MUST require the sub-agent to return pasted verification receipts (ls / wc -c / Grep / TF-query output) in its StructuredOutput. Without receipts the §7.3 gate cannot tell a real citation from a fabricated one. 2026-06-04: a cross-corpus sweep produced 3 of 13 specs with phantom citations, fabricated module names, and hallucinated BHSA feature values (vt=weqt does not exist)."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/7d83c8e90b8f3b39@v2`); state as of 2026-06-15 (snapshot mtime); possibly stale — re-verify before relying.


**The rule.** Any spec handed to a sub-agent (hand-spawned `Agent` or, preferably, a `Workflow` script) that names a concrete artifact — a `file:line`, a module, a function, a lemma, a feature value, a TF/treebank query result — MUST require the sub-agent to RETURN VERIFICATION RECEIPTS in its StructuredOutput: the actual output of `ls` / `wc -c` / `Grep` showing the symbol exists, or the actual query output. "Verify X" without "paste the receipt" is unauditable.

**Why:** Without pasted receipts, the §7.3 adjudication gate cannot distinguish a real module/citation from a hallucinated one — they read identically in prose. On 2026-06-04 a cross-corpus sweep produced **3 of 13 specs with phantom citations / fabricated module names / hallucinated BHSA feature values** (`vt=weqt` does not exist in BHSA). The prompts had asked sub-agents to "verify" without requiring pasted receipts, so the fabrications survived to the gate and cost audit tokens to catch.

**How to apply:**
- The sub-agent StructuredOutput schema includes a `receipts` field: the verbatim command + its output for every named artifact.
- A spec that says "confirm the helper exists" is insufficient; it must say "paste the `Grep` output showing the helper definition."
- This is the upstream filter; [[feedback_never_skip_audit_gate]] is the gate itself. A receipt-less spec is rewritten before dispatch, not sent and caught downstream.
- Siblings: [[feedback_code_path_diagnoses_require_running_the_code]] (the orchestrator's own Read+Grep+Run), [[feedback_canon_citation_requires_verbatim_read]] (canon citations need verbatim firewall quotes), [[feedback_no_handwave_in_precision_artifacts]] (no "verify"/"figure out" in sub-agent prompts).
