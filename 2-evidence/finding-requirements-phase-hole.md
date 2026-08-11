# Finding — the data plane and the requirements phase are the same hole

**Date:** 2026-08-11. Arrived at from the question *"are the rules grounded in scholarship, or are they a self-licking ice cream cone?"*

## Three axes, not one taxonomy

The project describes itself with two four-part models, and they were being read as competitors. They are orthogonal, and a third axis joins them:

| Axis | Values | Answers |
|---|---|---|
| **Plane** ([[3-implementation/architecture.md]]) | data · specification · tooling · delivery | *Where does this artifact live?* |
| **Audience** ([[2-evidence/scholarship/_index.md]]) | scholar (human) · robot | *Who reads it?* |
| **Phase** (board `Phase` field) | requirements · design · implementation · deployment | *What state is the work in?* |

Plane and audience are properties of **artifacts**. Phase is a property of **work items**. That is why the board carries Phase and not Plane, and why a single binding rule can sit in the specification plane permanently while moving through all four phases.

**Audience subdivides exactly one plane.** Data is data, tooling is code, delivery is UI — none has a rationale layer. Specification is the only plane holding both *the rule* and *why the rule*. So the human/robot split is not a rival to the plane model; it cuts the specification plane in two.

## The near-mapping, and where it breaks

Three planes line up with three phases closely enough to mislead:

| Plane | SDLC phase |
|---|---|
| Specification | design |
| Tooling | implementation |
| Delivery | deployment |
| **Data** | **— none —** |
| **— none —** | **requirements** |

The two gaps are not two problems. **The requirements phase is the phase that operates on the data plane** — it defines what correct output *is*, measured against gold. The architecture document's DATA plane lists source texts, parsed corpora, rendered corpora, transaction logs, and source-text anchoring. It lists **no gold, no yardstick, no acceptance criteria**. The BoFM gold yardstick exists on disk and is registered nowhere.

So the requirements phase has no home because the data plane has no acceptance-criteria component. One hole, seen from two sides.

## What the hole cost, measured the same day

Three independent findings, all the same shape — **validators measuring conformance to a rule, with nothing measuring whether the rule produces good colometry**:

1. `constraint_catalog_v1.md` is `Status: DRAFT — pending corpus-fixture validation`. Those fixtures are requirements-phase artifacts. They were never built, so 26 constraints have sat unvalidated since 2026-05-17.
2. `validate_short_orphan_line` emits **4,422** findings, the largest single source in the Tanakh suite. Nothing can say whether that is correct, because nothing defines correct. It also has no catalog entry and no scholarly source.
3. Tanakh baseline totals **2,036** against an actual **13,635**. A clean stashed `HEAD` reproduces 13,635 exactly, so the gap is not recent drift — but nothing establishes which number *should* be right.

This is [[memories/operational/feedback_conformance_is_not_correctness.md]] restated structurally: the missing requirements phase is the machinery that principle has always lacked.

## Consequence for the "circularity" worry

The rules are not circular so much as **unanchored at the acceptance end**. They descend from a criterion (the §2.1 bidirectional test) that is itself typed `[UNPROVEN]` in [[2-evidence/framework-claim-inventory.md]] claim #4, and they are checked against baselines that record whatever the code happened to emit.

Naming the board `colometry-project` made requirements *possible* — "is this colometry good, measured against Skousen, Marschall, the Masoretic tradition, and reader use" is answerable, where "is this an atomic thought unit" is not. It did not make requirements *exist*.

## The cheapest first requirements artifact

Claim #6 is typed `[UNPROVEN] — no ratio given anywhere; trivially measurable and never measured`. Counting what fraction of line decisions the §2.1 bidirectional test makes, versus the §2.2 explicit-marker license, is roughly a day's work.

It is worth doing **first** because it can redirect everything else. If the bidirectional test decides most lines, the framework is load-bearing and grounding the rules is worth the effort. If the marker license does most of the work, then "the bidirectional test is sole arbiter" is false as practised, and the grounding effort would be aimed at the wrong object.

## Related

- [[2-evidence/traceability-tanakh.md]] — theory → rule → validator, per row
- [[4-process/lessons.md]] — the probe-calibration lesson captured the same day
- [[3-implementation/architecture.md]] — needs the specification-plane split registered; its own ownership table already contradicts where `binding-rules-hebrew.md` lives
