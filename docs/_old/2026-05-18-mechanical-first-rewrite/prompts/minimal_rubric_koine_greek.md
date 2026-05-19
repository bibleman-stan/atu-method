# Minimal Rubric — Koine Greek (Stage 1 canonical prompt)

This is the canonical Stage 1 prompt for Koine Greek ATU rendering (Greek New Testament, LXX). Three Opus passes use this prompt; agreement scoring across the three passes determines auto-apply (unanimous) vs editorial review (non-unanimous). See `../toolset-architecture.md` §Stage 1.

The prompt embodies the minimal rubric: bidirectional test + restrictive-relative binding + a small set of Koine-Greek-specific syntactic constraints + default KEEP-AS-IS. NO cognitive-unity gate. NO parallelism class adjudication. NO genre anchors as primary licenses.

---

## The Prompt

Render the following Koine Greek chapter into Atomic Thought Units (ATUs) per the minimal rubric.

### What an ATU is

An ATU is the smallest cognitive chunk an attentive reader processes as a discrete unit. One ATU per line in the rendered output.

### Bidirectional test (the criterion)

A line is a legitimate standalone ATU only if BOTH:

**1. Forward grammatical closure** (Koine Greek terms):

- Finite verb: subject encoded by inflection is sufficient (Greek pro-drop OK)
- Verbless / nominal-predicate clause: subject + predicate juxtaposition counts as closed (Greek allows verbless predication, especially with `εἰμί` understood)
- Participial predication: subject + circumstantial participle CAN stand as ATU IF the participle has its own grammatical structure (genitive-absolute, attendant-circumstance with explicit subject, attributive substantival)
- Attributive participle (article + participle + dependents) functioning as nominal head: bound to whatever it modifies if restrictive; can stand alone if substantival
- Discourse-particle-headed (`ἰδού` / `οὖν` / `διά τοῦτο` / `γάρ` / `δέ` / `ὥστε` + content): particle + content = ONE ATU; particle alone fails forward closure
- Speech-frame (`ἀποκριθεὶς εἶπεν` / `λέγει αὐτῷ` / `εἶπεν αὐτοῖς`): may stand alone OR bind to short speech content; bind when content is short and inseparable
- Adnominal genitive chains (X τοῦ Y τοῦ Z): single ATU when chain is grammatically continuous

**2. Backward referential self-containment**:

- Overt referents present on the line OR recoverable from finite-verb morphology OR same discourse-active subject as immediately prior ATU
- Chain breaks at: speaker change in direct speech, vocative redirecting addressee, parenthetical `γάρ` / `ὅτι` clause introducing new content
- FAILS when long-range antecedents (>1 ATU back, no chain-continuity) are required
- Pauline `κατά` / `διά` / `εἰς` / `ἐν` + noun phrases functioning as adverbial modifiers: bind to whatever they modify; do not stand as separate ATU

A break between two adjacent lines is licensed if and only if BOTH lines independently satisfy these two conditions.

The test is **asymmetric**: cataphoric reference (forward-pointing — presentative `ἰδού` + indefinite NP introducing new content) does NOT fail the test; only anaphoric unresolved-backward-dependence fails.

### Restrictive relative clause binding

Restrictive (defining) `ὅς` / `ὅστις` / `ὅπου` / `ἐν ᾧ` clauses bind to head noun and cannot stand as standalone ATUs regardless of internal completeness. Diagnostic: would removing the relative clause leave the head uniquely identified? If no → restrictive → BIND.

Non-restrictive (descriptive / continuative) relative clauses may stand alone as ATUs when they pass the bidirectional test AND the head is already identified.

For Pauline `ἐν ᾧ`: distinguish continuative (descriptive — may stand alone if finite-closed) from restrictive (binding). Continuative is more common in long-period Pauline structures; the test is whether the antecedent is already specified.

### Greek-specific constraints

- **Purposive infinitive** (`τοῦ` + infinitive, `ἵνα` + subjunctive): bound to its governing verb. Especially: purposive infinitive immediately following verb of motion or sending.
- **`ὅτι`-clause**: when introducing direct discourse, treat as bound to speech-frame; when introducing indirect discourse, treat as object of verb and bound; when causal, may stand alone if it passes bidirectional test.
- **Aorist participle + finite verb** (πορευθέντες + main verb): the participle usually binds to the main verb as attendant-circumstance; do not split.
- **Genitive absolute**: stands as its own ATU when it has its own subject in the genitive and is grammatically independent of the matrix clause.
- **Articular infinitive** (`τοῦ` + infinitive) functioning as nominal: bound to its syntactic role; bound when complement of a verb.
- **Apposition** (X, ὅς ἐστιν Y): the appositional element is bound to the antecedent.

### What is NOT in the rubric (do NOT apply)

- Cognitive-unity gate on parallel cola (empirically inert)
- Parallelism class adjudication (synonymous / antithetic / synthetic categorization)
- Genre anchors as primary licenses
- Aesthetic / colometric preferences
- Doxological / hymnic enumeration sub-rules (bare-NP enumerations collapse per forward-closure failure, not per genre)

### Special handling for long Pauline sentences (e.g., Eph 1:3–14, Rom 5:1–11)

The Greek of these passages is one grammatical sentence but contains MANY propositionally distinct units. Apply the bidirectional test to EACH candidate breakpoint. The doxological "in him we have X" + "to the praise of Y" + "in whom Z" structure produces MANY ATUs within one long sentence — each propositionally complete unit is its own ATU even though syntactically subordinated.

### Under-broken cases

A line containing two independent propositions where each half passes forward-closure + backward-containment independently → SPLIT.

### Default

**KEEP-AS-IS** unless the bidirectional test, restrictive-relative rule, or Greek-specific constraint affirmatively fires.

### Output format

Per verse:

```
## Verse [reference]

### Source state
[source lines as in file]

### Minimal-rubric state
[ATU-segmented lines]

### Per-line verdicts
- Line N: [KEEP-AS-IS / MERGE-PRIOR / MERGE-NEXT / SPLIT / AMBIGUOUS]
  Rationale: [one sentence citing the gate that fired]
```

CRITICAL: do NOT modify any Greek characters or diacritics. Only regroup line breaks. Preserve breathings, accents, iota subscripts exactly.

End of chapter: write a summary block:

```
## Chapter summary
- Source content lines: N
- Total ATUs: M
- Net delta: +/- K
- Failure-mode classes that recurred: [list]
- AMBIGUOUS flags: [list verses]
- Note on long-sentence handling (if relevant)
```
