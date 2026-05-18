---
name: architecture-must-match-method
description: "When scaling a methodology into infrastructure, periodically check that the as-built architecture matches what the method actually claims. The ATU framework was cognitive-first (ATUs identified by bidirectional test; rules constrain) but the architecture had drifted to rules-first (validators produced ATU rendering; LLM cleaned up residue). The mismatch produced silent corpus pollution and contested results until empirically surfaced 2026-05-17. Default: re-check architecture-vs-method alignment whenever an experiment reveals unexpected results."
metadata:
  type: feedback
---

**The principle:** When a methodology is scaled into infrastructure, architecture decisions accumulate. Each decision is small, defensible in isolation, often inherited from pre-LLM tooling constraints. Over time the cumulative architecture may diverge from what the method actually claims — silently, because each decision passed local scrutiny. When an experiment produces an unexpected result, before refining the experiment, check whether the result reveals an architecture-vs-method mismatch.

**Why — the ATU example (2026-05-17):**

The framework says ATUs are cognitive units identified by the bidirectional test. Syntactic rules CONSTRAIN ATU well-formedness; they do not CREATE ATU rendering. Parallelism is a poetic-rhetorical feature operating on a separate axis from ATU rendering.

The as-built architecture had drifted into:
1. R/H validators ran FIRST and PRODUCED ATU rendering via procedural rules
2. LLM ran SECOND as residue cleanup
3. Some validators encoded parallelism categories (poetic-rhetorical features mis-located as ATU criteria)
4. The cognitive-unity gate was added to the LLM rubric to make its output match the validator-producer output

Multi-experiment evidence surfaced the mismatch:
- Validators (Legs 1-2-3) caught 0 of 4 needed corrections on Ps 1 — they do not produce correct ATU rendering on this verse-class
- Pure LLM with vs. without cognitive-unity gate: IDENTICAL accuracy. The gate was empirically inert.
- Minimal rubric on Ps 1: 14 of 14 ATUs match manual baseline exactly.

The corrected architecture:
1. LLM + parse-aware bidirectional test → identifies cognitive ATU candidates
2. Hebrew syntactic constraint catalog (yes/no grammatical questions) → audits candidates
3. Editorial review surfaces conflicts
4. Cognitive identification first; syntactic constraints second; parallelism off-axis

Stan verbatim: *"this is possibly that 'huge' breakthrough i have been wanting: the insight is that our architecture did not match the method we proposed."*

**How to apply:**

- When an experiment produces an unexpected result, before refining the experiment, check whether the result reveals an architecture-vs-method mismatch.
- Pattern signals: rules that PROCEDURALLY GENERATE output when the methodology says rules should CONSTRAIN output; LLM rubrics with categories that do not appear in the framework's actual claim; ad-hoc "extension" gates added because the existing rules produce wrong output.
- Periodic re-check: "what does the method actually claim about how X happens?" vs. "what is the architecture actually doing to produce X?"
- Cost of unchecked drift: silent corpus pollution; contested results; cognitive overhead defending an architecture that does not match the theory.

**Anti-pattern:** defending the as-built architecture by adding patches (cognitive-unity gates, FP guards, etc.) when the underlying issue is architecture-method mismatch. Patches accumulate cost without addressing the divergence.

**Pro-pattern:** when a patch is proposed, ask whether the patch is closing a method-vs-architecture gap or whether it is compensating for a method-vs-architecture mismatch. The first is legitimate; the second indicates the architecture needs realignment, not patching.

**See also:** [[feedback_minimal_rubric_validated]] (the empirical validation of the realigned architecture), [[feedback_three_anti_default_factors]] (Factor B / new-rule reflex is one form of patching a method-vs-architecture mismatch), [[feedback_rule_proposal_gates]] (Gate B uniform-application check tends to surface method-vs-architecture mismatches).
