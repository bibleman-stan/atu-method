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

**2. In `atu-nlp-wiki`** — which the inventory's own type system names as the receipt store for `[SOURCED]`. `wiki/clause-as-information-unit.md` (updated 2026-07-11) carries the near-exact proposition.

> **VERIFIED AGAINST THE PRIMARY SOURCE, 2026-08-11.** The Givón-1983 quote below was checked against `atu-nlp-wiki/raw/Givon-1983.pdf`, book page 7 (PDF page 3 — the scan carries a 4-page front-matter offset), section *"2. The 'paragraph' strand: Macro traditions"*. It matches verbatim, page number included. The wiki's paraphrase of pp.7–8 is also accurate: p.8 has *"the grammar/syntax, which is primarily (though not exclusively) a clause-level coding instrument."*
>
> This check was run because a quote relayed from a wiki page is a second-hand citation, and second-hand citations are where hallucination hides. **The receipt store makes the check cheap: 77 PDFs in `raw/`, including Givón 1975/1983/1984/1995, Chafe ×2, Lambrecht, Scheppers, Quirk, Shopen, Jurafsky, Louw.** Of the nine sources cited on the clause page, eight have a receipt; only Hiippala does not.

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

## The citation protocol this establishes

Stan, 2026-08-11: *"we need to anchor these theoretical foundations in a footnote citation/quote that can be checked so as to make sure you are not hallucinating."*

The infrastructure for that already exists and was unused. `atu-nlp-wiki/raw/` holds 77 source PDFs, and the inventory's `[SOURCED]` type already says *"a receipt into `atu-nlp-wiki/raw/` should exist."* The gap was never the receipts — it was that nothing required opening them.

**Rule, from here: no grounding claim without all four of —**

1. the **verbatim quote**, not a paraphrase;
2. the **page number** as printed in the source, not the PDF page;
3. the **receipt path** under `raw/`;
4. a **checked-on date**, recording that someone opened the PDF this turn.

A citation relayed from a wiki page is second-hand, and second-hand is exactly where a fabricated page number survives unchallenged. The check costs one `Read` call. **The Givón quote above went through it; every row in the traceability tables should too.**

Where no receipt exists — Hiippala on the clause page, and every Joüon/Waltke-O'Connor citation in `constraint_catalog_v1.md`, none of which have a PDF in `raw/` — the claim is **unverified**, and should be labelled that way rather than silently trusted because it looks like a citation.

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
## Citation errors found in constraint_catalog_v1.md, 2026-08-11

Checked the catalog's Joüon section numbers against the printed table of
contents of Joüon–Muraoka, *A Grammar of Biblical Hebrew* (Rome: Pontificio
Istituto Biblico, 2006), pp. xxi–xxxvi. No PDF required — the TOC alone
produces five discrepancies.

> **EDITION CAVEAT, added 2026-08-11 after Stan pointed it out.** That TOC is
> the **revised English edition of 2006** (Subsidia Biblica 27) — its front
> matter lists four separate prefaces: original French, English, corrected
> second printing, revised English. **Joüon–Muraoka renumbers across editions**;
> the 2006 TOC is visibly full of `aa` / `ba` / `fa` / `nb` sub-letters that are
> revision-era insertions.
>
> So the five rows below are discrepancies **against the 2006 edition**, not
> proven errors. If the catalog was written against the 1991 two-volume English
> edition or the 1993 corrected printing, some may be correct there.
>
> **And that ambiguity is itself the finding.** `constraint_catalog_v1.md`
> names no edition anywhere — every citation reads "Joüon §129" with nothing to
> resolve it against. A section number without an edition is under-specified for
> a work that renumbers, so these citations are *unresolvable* independently of
> whether they are *wrong*. Waltke–O'Connor (1990) has a single edition and is
> unaffected.
>
> **Consequence for the protocol:** the four required elements are now five —
> verbatim quote, printed page, **edition**, receipt path, checked-on date.

| Constraint | Cited as | §  actually covers | Probable correct § |
|---|---|---|---|
| `JM-oath-formula` | Joüon §147 "oaths and adjurations" | **Pronominal substitutions** | **§165** Clause of curse and oath |
| `JM147-vocative-extraclausal` | Joüon §147 "vocative and extra-clausal elements" | **Pronominal substitutions** | **§137g** Vocative |
| `JM103-proclitic-stranding` | §137 "conjunction waw" | **Determination / the article** | **§104** Conjunction |
| `JM174-gapped-verb` | Joüon §174 "gapping" | **Comparative clause** | **§125x** "Omission of the object from a second verb" |
| `JM159e-conditional-protasis` | Joüon §159e | **§159 = Circumstantial clause** | **§167** Conditional clause |

Note `JM-oath-formula` and `JM165` both appear: the catalog already cites §165
correctly elsewhere, so §147 there is a transcription slip rather than a
misunderstanding.

**What this establishes.** "26/26 constraints carry a Source" was never a
measure of grounding — it counted citation-shaped strings. Five of the section
numbers do not survive contact with the table of contents, and no receipt was
needed to discover that. The traceability table needs a value distinguishing
*citation present* from *citation checked*.

**Verified correct against the same TOC**: §13 Maqqef · §103 Preposition ·
§121 Participle (§121c "Used as predicate") · §123 Infinitive absolute ·
§125 Direct accusative · §129 Genitive and construct state (§129c "Length of a
construct chain") · §133 Prepositions in particular · §154 Nominal clause ·
§155 Verbal clause · §156 Casus pendens · §157 Substantival clause (§157ca
"Genuine indirect speech") · §158 Relative clause (§158p "אֲשֶׁר cannot be used
as non-restrictive relative pronoun") · §160 Negative clause · §161
Interrogative sentence · §164 Asseverative clause · §165 Curse and oath ·
§168 Final clause · §177 Syndesis and asyndesis.
