# Minimal Rubric — EME English (Stage 1 canonical prompt)

This is the canonical Stage 1 prompt for Early Modern English ATU rendering (Book of Mormon, KJV-style content). Three Opus passes use this prompt; agreement scoring across the three passes determines auto-apply (unanimous) vs editorial review (non-unanimous). See `../toolset-architecture.md` §Stage 1.

The prompt embodies the minimal rubric: bidirectional test + restrictive-relative binding + a small set of EME-English-specific syntactic constraints + default KEEP-AS-IS. NO cognitive-unity gate. NO parallelism class adjudication. NO genre anchors as primary licenses.

---

## The Prompt

Render the following EME English chapter into Atomic Thought Units (ATUs) per the minimal rubric.

### What an ATU is

An ATU is the smallest cognitive chunk an attentive reader processes as a discrete unit. One ATU per line in the rendered output.

### Bidirectional test (the criterion)

A line is a legitimate standalone ATU only if BOTH:

**1. Forward grammatical closure** (EME English terms):

- Finite verb: subject MUST be overt (EME English does NOT allow pro-drop) UNLESS imperative or implicit-subject construction
- Verbless / nominal-predicate clause: requires overt copula `is` / `are` / `was` / `were` — EME English does NOT allow zero-copula predication
- Participial / `-ing` clause: subject + participle counts as closed if the participle has its own subject (absolute construction); a bare `-ing` clause modifying the main verb is bound
- Discourse-particle-headed: `behold` / `wherefore` / `for` / `and now` / `yea` + content = ONE ATU; the particle alone fails forward closure
- "And it came to pass that..." frame: the frame + governed clause = ONE ATU OR separate depending on whether the governed clause is short and inseparable vs. independently complete

**2. Backward referential self-containment**:

- Overt referents present on the line OR same discourse-active subject as immediately prior ATU (chain continuity)
- Chain breaks at: speaker change in direct speech, vocative redirecting addressee, change of subject NP
- FAILS when long-range antecedents (>1 ATU back without chain) are required

A break between two adjacent lines is licensed if and only if BOTH lines independently satisfy these two conditions.

The test is **asymmetric**: cataphoric reference (forward-pointing — presentative "behold" + indefinite NP introducing new content; "thus saith X:" announcing speech) does NOT fail the test; only anaphoric unresolved-backward-dependence fails.

### Restrictive relative clause binding

Restrictive (defining) `which` / `who` / `that` clauses bind to head noun and cannot stand as standalone ATUs regardless of internal completeness. Diagnostic: would removing the relative clause leave the head uniquely identified? If no → restrictive → BIND.

Non-restrictive (descriptive) relative clauses may stand alone as ATUs when they pass the bidirectional test AND the head is already identified.

### EME-English-specific constraints

- **Discourse-particle binding**: `wherefore` / `for` / `yea` + clause where the clause has overt subject + finite verb forms ONE ATU (particle + clause together).
- **"Behold" + content binding**: `behold` + content forms ONE ATU.
- **"And it came to pass that..." frame**: usually binds to its governed content unless that content is a long independently complete narrative segment.
- **Coordinate `and` + finite verbs with same subject**: usually two propositions; SPLIT if each half passes bidirectional test independently. Coordinate noun phrases / coordinate objects of a single verb / coordinate adverbials remain bound (failure mode D: do not split at every `and`).
- **Subordinate `for` + independent proposition**: `for` introducing a propositionally distinct causal explanation may stand alone IF subject is overt AND the proposition is independently asserted.
- **Bare participials / -ing forms without own subject**: bound to the main verb (failure mode C: do not split bare participials).

### What is NOT in the rubric (do NOT apply)

- Cognitive-unity gate on parallel cola (empirically inert)
- Parallelism class adjudication (synonymous / antithetic / synthetic categorization)
- Genre anchors as primary licenses
- Aesthetic / colometric preferences
- Punctuation as binding signal (commas, semicolons, colons are EDITORIAL choices; do not let them adjudicate ATU boundaries)

### Under-broken cases

A line containing two independent propositions where each half passes forward-closure + backward-containment independently → SPLIT.

### Failure modes to avoid

A. **Over-merging chains of "that..." clauses**: each "that..."-clause with its own overt subject + finite verb stands as its own ATU.
B. **Under-merging restrictive relatives**: restrictive "which" / "that" / "who" MUST bind to head noun even when the relative clause itself has a complete predicate.
C. **Splitting bare participials from main verb**: bare `-ing` or `-ed` participle without own subject is bound to the main verb's line.
D. **Splitting at every "and"**: the conjunction "and" is NOT a license to split. Apply the under-broken test only.

### Default

**KEEP-AS-IS** unless the bidirectional test, restrictive-relative rule, or EME-specific constraint affirmatively fires.

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

CRITICAL: do NOT modify the English text. Only regroup line breaks. Preserve punctuation and capitalization exactly.

End of chapter: write a summary block:

```
## Chapter summary
- Source content lines: N
- Total ATUs: M
- Net delta: +/- K
- Failure-mode classes that recurred: [list]
- AMBIGUOUS flags: [list verses]
```
