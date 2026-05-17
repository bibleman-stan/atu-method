---
name: Grammar constrains ATU boundaries; it does not determine them
description: Grammar (UD signatures, syntactic categories, syntactic constraints in catalog per Stage 2, complement/formula/relative integrity) constrains where ATU breaks CAN'T go. It does NOT positively determine where breaks SHOULD go. The generative force is atomic-thought (propositional/psycholinguistic), not grammatical.
type: feedback
---

**Asymmetry:** Grammar gives PROHIBITIONS, not PRESCRIPTIONS, for ATU boundaries.

- **Grammar CAN'T-go signals (syntactic constraints in catalog — Stage 2):** "this break is illegal under the target language's grammar" — line-final CCONJ/DET/AUX/ADP prohibitions, V+DO bond, complement integrity (matrix-VERB or matrix-ADJ valence unsatisfied), fixed-idiom integrity, restrictive-relative bonds (closed-list per corpus).
- **Atomic-thought SHOULD-go signals (generative principle + bidirectional test affirmation per `framework.md §1.2`):** "this break is justified because the next line carries a fresh proposition / camera angle / portrait beat / speech-act announcement / classical comma / substantive adjunct as own focus." The generative force is propositional, not grammatical.

**Why this asymmetry matters:** A grammatical pattern's existence does NOT automatically justify a rule. Per-corpus canon SCOPE statements codify this implicitly — e.g., BoFM R17 SCOPE says "NOUN head → out of scope (no R17-equivalent for NOUN-headed ccomp)." The NOUN-head-complement grammatical pattern exists in UD parses; ATU integrity does NOT extend there because content-emptiness (the atomic-thought-failure test), not syntactic completeness, is the principle. Hostile audit α (2026-05-12) correctly rejected a framework-extension attempt that conflated grammatical-pattern-presence with ATU-boundary-determination.

**Why this memory exists:** Stan codified the principle verbatim 2026-05-13: *"grammar doesn't determine ATUs boundaries, but it can constrain them."* The full BoFM 2026-05-12/13 session's discipline failures all map to this asymmetry-violation: treating grammatical-pattern-presence as ATU-boundary-determination instead of merely as constraint on where breaks can sit. Codified at framework §1.2's tail ("Constraint vs. determination — the asymmetry between §1.1 and §1.2").

**How to apply:**

1. **When proposing a new rule:** ask "does this rule encode a CONSTRAINT (prohibition on illegal breaks) or a DETERMINATION (prescription of correct breaks)?" Constraints are Cat A mechanical rules grounded in syntactic constraints in the catalog (Stage 2) or complement/formula/relative integrity. Determinations require the atomic-thought test to fire — and that test is propositional, not grammatical. Grammar can confirm a determination is safe; grammar alone cannot generate it.

2. **When auditing audit outputs (per `feedback_audit_outputs_need_canon_check`):** if an audit recommends a SCOPE-exclusion grounded purely in "grammatical pattern X is present/absent," reject. Constraints get grounded in grammar; determinations get grounded in atomic-thought + camera-angle. The audit's reasoning must trace to the latter for any merge/split decision.

3. **When closing the gap from "framework says split-by-default" to a closed-list merge:** the closed-list is a CONSTRAINT (these specific heads are content-empty, so breaking here violates atomic-thought because no proposition is complete on the head's line). Not a DETERMINATION (we are not saying "merge X+Y because grammar says so" — we are saying "the proposed split here fails the atomic-thought test under the specific structural condition; therefore merge").

4. **When tempted to import an external grammatical framework wholesale** (UD taxonomy, Penn Treebank labels, Hebrew parallelism categories per `feedback_rhetoric_bandwagon`): such frameworks are CONSTRAINT-classifiers, not DETERMINATION-engines. Use their distinctions to sharpen our constraint signatures (e.g., UD's `acl:relcl` vs `acl` is a useful restrictivity flag). Do NOT import them as ATU-boundary-determiners.

5. **For closed-list extensions specifically** (e.g., R19's `R19_OBLIGATORY_REF_NOUN_HEADS` in BoFM canon, analogous constructs in GNT R10/Tanakh H7): the threshold for inclusion is "is the head referentially content-empty without the complement such that breaking here leaves a line with no atomic thought?" — that's the atomic-thought-failure test, applied through the constraint of grammatical head-completion. The closed-list is the OPERATIONALIZATION of where the atomic-thought test fires; it is not a grammatical-pattern catalog.

**Cross-cutting connection:** This is the deeper principle behind `feedback_rhetoric_bandwagon` (don't import external grammatical frameworks as forces), `feedback_audit_outputs_need_canon_check` (audit framings that are grammatical-pattern-only get rejected), and the framework's stance that "the apparatus is NOT a rhetorical-parallelism analyzer" (apparatus.md). All four rest on this asymmetry: grammar constrains where ATU breaks can sit; atomic-thought determines where they should sit.
