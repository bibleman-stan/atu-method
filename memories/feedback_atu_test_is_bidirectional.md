---
name: ATU test is bidirectional
description: The atomic-thought test ("can the reader take this in as a single complete unit of meaning?") is bidirectional, not just forward. ANAPHORIC unresolved-backward-dependence (deictic demonstratives like "these things", unresolved pronouns, discourse-anaphoric particles לָכֵן/עַל־כֵּן/causal כִּי) fails atomic-thought standing. CATAPHORIC forward-pointing reference (presentative הִנֵּה + indefinite NP) does NOT fail. This is a refinement of §1.1, not a new §1.5 merge-override.
type: feedback
---

**Principle:** "Single cognitive bite" (framework §1.1) requires the line to stand on its own **referentially**, not just **grammatically**. A line whose content is anaphoric to prior context — pronouns without on-line antecedent, deictic demonstratives (*these things*, *that day*, *the same*), discourse-anaphoric particles (*therefore*, *thus*, *לָכֵן*, *עַל־כֵּן*, causal *כִּי*) — fails the atomic-thought test, even when it passes forward grammatical closure.

**The asymmetry:**
- **Anaphoric failure (BLOCKS standalone-ATU status):** the line *requires* upstream content to be cognitively complete. Reading the line in isolation leaves a referential hole. Example: Gen 22:1 *wayehi achar ha-devarim ha-eleh* ("and it came to pass after these things") — *ha-devarim ha-eleh* points to undefined antecedent narrative; without the preceding chapters loaded, the line is content-incomplete.
- **Cataphoric standing (ALLOWED):** the line introduces new content with forward-pointing apparatus. Example: presentative *הִנֵּה* + indefinite NP. The line is propositionally complete on its own — the cataphoric reach is a feature of what follows, not a deficit of what's here.

The reason the asymmetry holds: ATU integrity is about what the reader CAN process at this line independently. Anaphoric reference imposes an UPSTREAM dependency (must have already loaded prior context); cataphoric reference creates a DOWNSTREAM expectation (the reader is set up for what's coming, but the current line is propositionally whole).

**Why this memory exists:** Codified 2026-05-13 from cross-conversation refinement. Stan reviewed a separate Claude conversation analyzing Hebrew temporal/framing constructions and corrected: *"I would say [Gen 22:1] is not [an ATU on its own] because, 'and after these things...' by definition requires an 'after these... what?' in a person's mind."* The transcript surfaced a gap in framework §1.1: the generative principle was stated as forward-only (does this line complete a thought?) without the bidirectional referential-self-containment test.

**Relationship to prior merge-override mechanisms (not a parallel mechanism):**
This is a refinement of the §1.1 atomic-thought test itself, NOT a new merge-override under the minimal rubric. Prior framework mechanisms M3 and M4 (deprecated 2026-05-17 under the bidirectional test framework) were triggered by specific structural conditions (forward-dangling heads, symmetric fragmentation). Backward-anaphoric failure is caught upstream of those — at §1.1 — by the atomic-thought test stated bidirectionally. A line that fails the bidirectional test fails atomic-thought, full stop; the merge is the consequence, not a separate rule. Do NOT analogize backward-anaphoric as a "third failure mode" under any override mechanism — that confuses test-refinement (§1.1 level) with override-mechanism logic. The cleaner statement: §1.1 has always implied bidirectional self-containment; this codification just makes the backward direction explicit.

**Status — informational diagnostic, not precedence override (gnt-reader correction 2026-05-13):**
The bidirectional test is **not** a precedence override. It does NOT adjudicate between competing rules in per-corpus application-order machinery, and it is NOT invoked to resolve intra-constraint-catalog conflicts (those go through per-corpus precedence hierarchies). It is an *informational diagnostic* at canon §1: it tells you whether a candidate line stands as an ATU at all, *before* the constraint-catalog audit steps run (Stage 2). Treating it as a precedence override — "the bidirectional test trumps rule X" used to resolve a rule conflict — is a category error: precedence resolves conflicts among rules in the constraint catalog and per-corpus canon; the bidirectional test resolves whether the line is an ATU. Lesson surfaced by gnt-reader the hard way; codify wherever per-corpus canons describe their precedence hierarchies so the distinction is visible.

**How to apply:**

1. **When evaluating a proposed line break:** run the bidirectional test, not just the forward one. Ask both (a) "is the proposition forward-closed on this line?" (existing §1.1) AND (b) "is this line referentially self-contained against upstream?" Both must pass for standalone-ATU status.

2. **Diagnostic markers for anaphoric failure (Hebrew):**
   - *הָאֵלֶּה* / *הַזֶּה* / *הַהוּא* (deictic demonstratives) on the line referencing offline antecedent
   - 3-person pronouns / pronominal suffixes whose antecedent is upstream
   - *לָכֵן* / *עַל־כֵּן* / *כִּי* (causal) / *אָז* (sequential-anaphoric) opening the line
   - Construct chains like *אַחַר הַדְּבָרִים הָאֵלֶּה* where the head genitive is deictic

3. **Cataphoric structures that PASS the test (do not falsely flag):**
   - Presentative *הִנֵּה* + indefinite NP introducing fresh participants
   - *זֶה* / *זֹאת* in cataphoric apposition ("this is the thing that...")
   - First-mention construct chains where the head is the new content
   - Distinguishing: cataphoric points FORWARD into content on the *same or next line*; anaphoric points BACKWARD into content presupposed BEFORE the line

4. **Interaction with FEF/AICTP constructions:** AICTP openers (*wayehi* + temporal frame) are often anaphoric — they require the preceding narrative to make the frame referentially full. This is a STRUCTURAL reason such openers merge into the apodosis: not just "short opening clause" (length is not a criterion), but "the *wayehi* + anaphoric-frame is not propositionally complete on its own line because the frame deictically references upstream narrative." This grounds the AICTP-merge intuition in the bidirectional ATU test rather than in length.

5. **Do NOT use length as a proxy.** Backward-anaphoric failure can occur on long lines too (a fully-formed clause whose subject pronoun has no on-line antecedent still fails the test). Conversely, short cataphoric lines (presentative + name) can stand. The criterion is REFERENTIAL SELF-CONTAINMENT, not word count.

6. **Cite §1.1 when invoking, not a merge-override mechanism.** A merge decision grounded in backward-anaphoric failure cites the bidirectional atomic-thought test at §1.1. Prior M3 (forward-dangling) and M4 (symmetric) merge-override mechanisms are deprecated under the bidirectional test framework (2026-05-17); backward-anaphoric is upstream of those, at the test itself.

**Cross-cutting connections:**
- Relates to [[feedback_grammar_constrains_not_determines]]: grammatical closure is necessary-but-not-sufficient; bidirectional referential self-containment is the broader atomic-thought principle that grammar serves.
- Sharpens the **anti-English-anchor** principle (CLAUDE.md "Anchor in Hebrew syntax, not English-translation surface"): KJV's English-driven smoothing of *wayehi* frames into "and it came to pass that" or "now when" obscures the Hebrew anaphoric structure. The test must run against the Hebrew referential mechanism, not the English smoothed gloss.
- Relates to the substantive-adjunct test (bidirectional test affirmation per `framework.md §1.2`): a Hebrew-marked fronted constituent that introduces *new* topical content is cataphoric and can stand; a fronted constituent that is anaphoric to prior topic does not.
- Codified at framework §1.1's tail (2026-05-13). All canons (BoFM, GNT, Tanakh) inherit this test through the §1.1 generative principle; cross-corpus per-corpus refinements can elaborate the diagnostic markers but the principle is shared.
