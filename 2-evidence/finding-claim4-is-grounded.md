# Finding — claim #4 is grounded; the inventory and the grounding never met

**Date:** 2026-08-11. Prompted by Stan asking whether `[UNPROVEN]` on claim #4 means the method is circular — *"we made a rule, we used the rule to split the lines, we then measured the lines are conforming to the rule."*

## Short answer: not circular, but genuinely disconnected

Claim #4 — *"grammatical closure is a proxy for thought"* — is typed `[UNPROVEN]` in [[2-evidence/framework-claim-inventory.md]] and called *"the single most load-bearing theoretical claim in the document, asserted in one clause."*

**That typing is accurate about `framework.md` and misleading about the program.** The inventory declares its own method: *"a read-only pass over framework.md."* `[UNPROVEN]` there means **this file does not support this claim**. It was never a survey of whether grounding exists elsewhere.

It does exist, in two places, and neither is cited by the framework or the inventory.

## Where the grounding actually lives

**1. Inside this repo.** [[4-process/methodology-position.md]] §3:

> **"Cognitive grounding — Langacker + Givón primary; Chafe a foil."** The "atomic thought" claim grounds primarily in conceptualization-based cognitive linguistics (Langacker: units as conventional packagings of meaning; Givón: information flow, topic continuity), not in Chafe's prosody-anchored idea units. Rationale: the corpora are mediated *written conceptual artifacts*, not speech transcripts, so prosodic chunking under-fits.

And §2: *"The ATU is this apparatus's **operationalization** — via the bidirectional atomic-thought test — of the **conceptual unit already described in the discourse-linguistic literature, not a newly posited theoretical entity**."*

Named sources: Langacker, *Foundations of Cognitive Grammar* (1987/1991) and "Discourse in Cognitive Grammar" (2001); Givón, *Topic Continuity in Discourse* (1983).

**2. In `atu-nlp-wiki`** — which the inventory's own type system names as the receipt store for `[SOURCED]`. `wiki/clause-as-information-unit.md` (updated 2026-07-11) carries the near-exact proposition:

> "The clause ('sentence') is the basic information processing unit in human discourse. A word may have 'meaning', but only the proposition — grammaticalized as clause — carries information." — Givón-1983, p.7

> "the clause is the minimal unit for **accruing new language-coded information into episodic memory**" — Givón-1995, p.379

Plus Givón-1984's one-chunk-per-clause count (≈1.41 chunks per proposition, biased to over-count), and a convergent cluster with Chafe's intonation unit and Lambrecht's information structure.

**"Only the proposition, grammaticalized as clause, carries information" is claim #4 in someone else's words.**

## The measurable disconnect

| Artifact | Cites Givón |
|---|---|
| `1-method/framework.md` | **0** |
| `2-evidence/framework-claim-inventory.md` | **0** |
| `4-process/methodology-position.md` | yes, as primary grounding |
| `atu-nlp-wiki/wiki/clause-as-information-unit.md` | extensively |

The wiki page is dated **2026-07-11**; the inventory calling the claim unsupported is dated **2026-08-06**. **The grounding predates the verdict by four weeks, in a repo the inventory's own type system points at.**

## What this does and does not fix

It moves claim #4 off `[UNPROVEN]`. It does **not** move it to *proven*, and the inventory's own safety rule says why: `[CONVERGENT]` means *"we derived it independently; an external parallel exists. **Cite as comparison, never as warrant.**"* `feedback_rhetoric_bandwagon.md` names misframing convergence as authorization a listed danger. Givón makes the claim non-arbitrary and locates it in a real research tradition. He does not make it true for Hebrew, Greek, or EME English.

The correct retype is `[CONVERGENT]` — possibly `[SOURCED]` if `methodology-position.md` records the framework actually reasoning *from* Langacker/Givón rather than arriving alongside them. That is a documentary question about authorship order, answerable and unanswered.

## The live challenger, which matters more than the support

The same wiki page carries a named opponent. **Scheppers-2011** inverts the clause-as-basic-unit view: for Ancient Greek the elementary unit is the **colon**, "typically much shorter than a clause," with the clause a *post hoc* construct — word-order rules apply to the colon, not the clause.

This cuts both ways and both ways matter:

- It is a **direct threat to the clause grain** that §2.1 and the binding rules are built on.
- It is **support for colometry as the deliverable**, which is exactly the split behind naming the board `colometry-project`.

A grounding pass that cites Givón and omits Scheppers would be advocacy, not scholarship.

## On the circularity worry specifically

Stan's formulation was *"we made a rule, used the rule to split the lines, then measured the lines conform to the rule."* [[2-evidence/finding-licensor-share.md]] is not that — it measured which of two licensors fired, a fact about the framework's internal composition, not about output quality. But the worry behind it stands: **no internal measurement can validate the criterion.**

Escaping requires an external anchor, and there are exactly two kinds:

1. **Theoretical** — does an independent tradition posit this unit? **Yes, and it is unwired.** Langacker, Givón, Chafe, Lambrecht, with Scheppers dissenting.
2. **Empirical** — does the output match something we did not produce? **Missing.** That is the requirements-phase hole in [[2-evidence/finding-requirements-phase-hole.md]]: no gold, no yardstick, no acceptance criteria in the data plane.

So the loop is open, not vicious. Half the closure material exists and is not connected; the other half has never been built.
