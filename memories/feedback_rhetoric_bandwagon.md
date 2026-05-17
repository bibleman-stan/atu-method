---
name: Rhetoric bandwagon — maintain critical distance from external rhetorical frameworks
description: When you encounter external scholarly work articulating rule systems grounded in classical rhetorical theory or Hebrew-poetry parallelism systems (Lowth, Watson, Kugel, Berlin, O'Connor), resist wholesale adoption. Our theoretical ground is psycholinguistic, not rhetorical. Adopt specific observations; reject ontological-category imports
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**The pattern to resist:** when trench Claudes encounter external scholarly work articulating formal rule systems (classical rhetorical theory, Hebrew-parallelism theory from Lowth / Watson / Kugel / Berlin / O'Connor, or future theoretical frameworks), the tendency is toward **enthusiastic wholesale adoption** — treating the external framework as authoritative scaffolding to import rather than as a comparison target to learn from selectively.

Stan named this the "rhetoric bandwagon" and has had to correct it multiple times in the GNT sibling. The same pattern can fire here — parallelism theory is the obvious BofM attractor.

## Why it's dangerous

Our theoretical foundation is **psycholinguistic / cognitive**, not rhetorical or parallelism-structural. See `feedback_sense_line_mission.md` for the grounding principle: atomic thought trumps poetic structure; we expose sense-lines, not parallels; Parry is a separate layer we may overlap with but do not target.

Importing external frameworks wholesale:

1. Dilutes the project's distinctive contribution
2. Imports theoretical assumptions we don't share
3. Creates failure modes that don't fit the BofM text
4. Misframes convergence as authorization

## Recognition signals — watch for these phrases/instincts

- *"Adopting her framework (with attribution) would give us a citable formal lineage"*
- *"This is cleaner / more disciplined than our current methodology"*
- *"We stand in [X]'s explicit tradition"*
- *"Promote our practice to a named law, citing [external source] as the typology source"*
- *"When her analysis matches ours, we should follow her method"*
- Reframing our rules as instances of their rule system
- Adopting ontological categories wholesale (periods, bicola, line-versification schemes as "fundamental structure")
- **Named-category carve-out (added 2026-04-23)** — Under pressure to codify a judgment call where a mechanical rule fires but editorial instinct balks, reaching for a named category ("doctrinal weight," "register," "cadence," "formulaic weight," "named BofM pairs") to rationalize dodging the merge. This shape-matches rhetoric-bandwagon even when the named category isn't imported from external theory — the instinct to invent a named sub-class rather than invoke existing §2 Category A/B/C discretion IS the failure mode. Two catches in 48 hours: Stab-commata register + Semantic Grouping Principle (2026-04-22, deleted in f883eab); doctrinal-weight Category-B bump (2026-04-23 AM, withdrawn in 1ea0d68).

## Safe to adopt

- **Specific empirical observations as linguistic facts**
- **Rules that are deflationary-reinterpretable**
- **External work as validation benchmark** (output convergence is evidence, not authorization)
- **Terminology as clarification**

## The pragmatic test

> **Is this rule grounded in how humans cognize, or in how trained scribes/poets were taught to compose?**
>
> First kind = safe to adopt. Second kind = ghost-chasing.

## How to apply

When enthusiastic about a new external framework: pause, apply the pragmatic test, flag the tension to Stan before adopting. Output-convergence (both methods capture something real) ≠ method-adoption (commits to their theoretical assumptions). The former is fine; the latter requires Stan's explicit sign-off.

**For the named-category carve-out sub-pattern (added 2026-04-23):** before adding any new named sub-clause, sub-class, or category label to the canon, ask: *does §2 Category A/B/C already cover this concern?* Specifically §2's closing instruction — "when uncertain between A and B/C on editorial/rhetorical grounds, treat as Category B." If yes, don't add named categories; invoke §2. If no, the new sub-clause needs a mechanical trigger (UD signature, corpus count, closed list of forms) — not a feel-test. Suspect any proposed sub-clause that relies on words like *recognized, formulaic, cadence, register, weight, rhythm, domain*.

**For the biased-spot-check sub-pattern (added 2026-04-23):** do NOT propose canon codification based on spot-check confirmation alone (e.g., "a 30-case spot-check shows uniform pattern"). Spot-checks are subject to confirmation bias — the cases I look at first tend to confirm my hypothesis; the counterexamples cluster in the cases I don't look at. **Require a full-corpus sweep against the proposed rule before codification.** If the corpus is too large for full manual sweep, dispatch an agent to classify every instance and report the disposition distribution (e.g., 98/147 own-line, 40/147 inline). The counterexample rate is the acceptance criterion — if >20% of corpus instances contradict the rule, the rule is not yet codifiable (per canon §7's ≥80% clean-categorization threshold). Example catch: 2026-04-23 PM EP-6 Exception/Save clause proposal — my 30-case spot-check showed apparent uniformity; hostile-audit full-corpus sweep found 98 of 147 *save it were/be/is* cases were LINE-START not inline, contradicting the proposal's "short-form → merge" prediction 70% of the time.

**Systematic audit discipline (added 2026-04-23, after 5 catches in one session):**

Canon §7.3 now specifies 11 mandatory-audit triggers and §2 has a scope/precedence/closed-list/carve-out diagnostic that defaults such additions to Category B. CLAUDE.md has a pre-commit audit discipline with a self-test. Those are the authoritative refs; this memory captures the BEHAVIORAL sub-pattern.

The disposition to watch for: **I construct a canon change, frame it internally as "Low-tier clarification" or "documenting existing practice" or "scope refinement," and propose codification without audit.** The framing is often wrong. Gap 1-A was framed as "documenting" but was actually a precedence claim. Rule 17 topic-PP was framed as "refinement" but was actually a closed-list extension. Doctrinal-weight bump was framed as "SCOPE sharpening" but was actually a new enumerated-list category.

Operational discipline before any `git add -f private/01-method/colometry-canon.md`:
1. Does the change include a scope claim, precedence claim, closed-list extension, or named-category carve-out? (If yes → audit.)
2. Does the change rest on spot-check evidence rather than full-corpus classification? (If yes → audit.)
3. Does the change reclassify or delete previously-settled canon? (If yes → audit.)

**Parallelize audits by default.** When triggered, dispatch multiple audit dimensions in parallel (one message, multiple Agent tool calls). Sequential only when audit A's verdict determines whether audit B should run.

**Five catches precedent** (treat as training examples, not as dismissible one-offs):
- Stab-commata deletion (f883eab) — named category that failed SCOPE test after exclusions
- Doctrinal-weight bump withdrawal (1ea0d68) — enumerated list of "recognized formulas," 4 of 5 feel-tests
- EP-6 Exception/Save rejection (13f8859) — spot-check hid 70% counterexample rate
- 1 Ne 19:5 reclass catch (d8fd16f) — Category B reclassified as A via different rule-framing
- R28 import (cf2f755) — provisional reject overturned; corpus evidence I had missed

Each failure has a named shape. When I find myself proposing something shape-matching one of the 5, audit first.

**Sixth catch (2026-05-10) — external-reviewer classical-rhetoric proposal:** Gemini reviewed the canon and proposed adding **Justification 6 — Syntactic Rupture (Anacoluthon)** to the closed-list of structural justifications. Hostile-audit dispatched (Opus, single message); REJECTED with 7 arguments — most decisive: (a) direct collision with prior M4 mechanism (Justification 6 splits ruptured fragments; M4 merged them — direct negation; M4 itself is deprecated 2026-05-17 under the bidirectional test framework, but the structural conflict with any merge-default remains), (b) fails extensibility test (a) — anacoluthon is the ABSENCE of formal structure, opposite generating principle from justifications 1-5, (c) corpus-fit: WoM 1:1 (textbook BoFM anacoluthon) already resolves cleanly under existing Rule 21 / Justification 5 + the generative principle. **The recognition signal: external reviewer proposing a new closed-list extension named after a classical rhetorical figure ("Anacoluthon," "Zeugma/Gapping").** The proposal had surface plausibility (ancient texts DO use anacoluthon) but the cure was wrong — the corpus already handles every BoFM case. Default response when external reviewers propose closed-list extensions named after classical rhetorical categories: skepticism + hostile-audit before any consideration. The ATU framework is grounded in cognitive recovery, not classical-rhetoric taxonomy.

## Cross-reference

- `feedback_over_structuring_disposition.md` (umbrella) — rhetoric-bandwagon is the "external-authority" sub-pattern
- `feedback_sense_line_mission.md` — the psycholinguistic grounding principle we maintain against external frames
- `feedback_rhetorical_force.md` — rhetorical force alone never justifies a split (related anti-external-frame discipline)
