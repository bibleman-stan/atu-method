---
name: Goldilocks refinement — subordinate vs coordinate syntax
description: Container-not-originator merge heuristic applies only to SUBORDINATING syntax (modifier→head), NOT to coordinating/parallel syntax where each member is its own atomic beat
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
When running merge passes on BoM sense-lines, do NOT apply container-not-originator reasoning blindly. The load-bearing refinement (ported from readers-gnt/handoffs/02-colometry-method.md §Goldilocks, 2026-04-13):

**Container-not-originator applies to SUBORDINATING syntax (modifier → head) only. It does NOT apply to COORDINATING or PARALLEL syntax. Parallel members are each their own atomic thought.**

**Why:** During the 2026-04-13 session I merged 138 lines across classes A/B/C/E/F/G/H. An adversarial audit of every merge flagged 33 as over-merges (24% of the batch). The worst class was F (participial absolutes) at 63% FP rate, because "he being X" in BoM archaic English functions prosodically as a full predication ("he was X"), not as a dangling modifier. Class H ("or" parallel naming) was second worst at 41% FP. Classes B/C/G held up at 100% because they target genuinely subordinating stranding.

**How to apply:** Before applying any merge, run the Q1/Q2 diagnostic:
- Q1: Can line N be read as a standalone prosodic predication (with implicit "was/had")?
- Q2: Does line N+1 open with a rhetorical pivot ("therefore/thus/wherefore"), a resumptive subject pronoun (he/she/they/it/I/we), a new grammatical subject NP, or a parallel conjunction?

If Q1=YES and Q2=YES → COORDINATE, do NOT merge.
If Q1=NO or Q2=NO → SUBORDINATE, merge is correct.

Stan's breath-unit intuition is the same principle from a different angle: if a proposed merge produces an unspeakably long line, coordination is almost certainly at work and the merge is wrong.

**Protocol:** Dispatch an adversarial audit agent on every merge batch before committing (or at most one commit later). If the audit flags ≥30% for revert, the scanner itself is too broad — add filters before re-running.

The scanners themselves are fine. The bug was trusting them without the Q1/Q2 gate.
