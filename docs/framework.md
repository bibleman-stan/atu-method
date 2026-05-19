# Framework — Methodology Specification

Canonical specification of the ATU methodology, shared across all reader editions.

Normative keywords (MUST, MUST NOT, SHOULD, MAY) follow RFC 2119.

---

## §1 Purpose

The apparatus produces **colometric reading editions** of canonical texts: each line on the page renders one **atomic thought unit (ATU)** — a span a reader can take in as a single complete unit before needing the next.

The apparatus reveals ATU structure already present in the text. It does NOT:

- Adjudicate textual variants (the source text is a fixed input)
- Produce typography or oral-delivery markup
- Reveal rhetorical parallelism (separate scholarly layer; may overlap but is not the target)
- Add, remove, or alter words

## §2 The bidirectional test (the criterion)

A line is a legitimate standalone ATU if and only if BOTH:

1. **Forward grammatical closure** — the line is grammatically complete on its own terms in the target language. Languages with morphologically-encoded subjects (Hebrew finite verbs, Greek finite verbs, Latin finite verbs) license pro-drop. Verbless / nominal-predicate constructions count as closed when subject + predicate are juxtaposed (Hebrew, Greek). EME English requires overt copula. **Elision-restoration is permitted** — when a verb is gapped from a parallel prior clause, the elision-restored clause counts as closed.

2. **Backward referential self-containment** — the line's referents are established in prior discourse (immediately, via chain-continuity) or self-introducing within the line. Long-range antecedent dependencies (more than one ATU back without chain-continuity) fail backward containment.

A break between two adjacent lines is licensed if and only if both lines independently satisfy these two conditions.

**Asymmetry:**

- **Anaphoric failure** (backward-dangling): pronouns without antecedent on the line, deictic demonstratives ("these things," "that day"), discourse-anaphoric particles (`לָכֵן`, `עַל־כֵּן`, causal `כִּי`, "therefore") all fail backward containment.
- **Cataphoric introduction** (forward-pointing) does NOT fail: presentative `הִנֵּה` + indefinite NP, "thus says X:" announcing speech.

**Restrictive relative clause binding** is a corollary: restrictive relatives bind to their head noun regardless of internal completeness, because removing them leaves the head not uniquely identified. Universal across Hebrew `אֲשֶׁר`, Greek `ὅς`/`ὅστις`, EME English "which"/"who"/"that".

**Default action**: KEEP-AS-IS unless the bidirectional test affirmatively licenses a break. The framework does NOT include cognitive-unity gates on parallel cola, parallelism class adjudication, or genre anchors as primary licenses.

## §3 Architecture — mechanical-first

The pipeline operates in stages on parse-derived clause units, with bindings applied by BHSA-feature-driven rules to produce ATU candidate groups. LLM adjudication is OPTIONAL and narrow-task, applied only where mechanical bindings cannot decide.

```
v0  Source text (with verse markers)
  ↓
v1  Parse-derived clauses (BHSA clause-atoms for Hebrew;
                           Macula Greek for Greek;
                           CoNLL-U for EME English)
  ↓
v1.5  Binding rules applied — ATU candidate groups
  ↓
v2  (Optional) LLM adjudication on residual cases
  ↓
v3  Editorial review of remaining ambiguity
  ↓
Final ATU rendering — committed to data/text-files/v2/
```

### v1 — Parse-derived clauses

Each language uses its own parse layer:
- **Hebrew**: BHSA via Text-Fabric (ETCBC). Unit = `clause_atom`.
- **Greek**: Macula Greek (Clear-Bible). Unit = clause node.
- **EME English** (BoFM): Stanza CoNLL-U. Unit = sentence.
- **Latin** (planned): UD-Latin or LDT.

Output: one parse-derived clause per record, with linguistic features attached (clause type, head verb lemma, relation tags, etc.).

### v1.5 — Binding rules

A small catalog of **binding rules**, each grounded in the bidirectional test, takes the v1 clauses and merges them into ATU candidate groups. Each rule fires based on parse-derived linguistic features (clause type, head lemma, text prefix after pointing-strip).

For Hebrew, the validated catalog is **14 binding rules** (B1-B14 with B4 retired); see [`binding-rules-hebrew.md`](binding-rules-hebrew.md).

All bindings fire only **within a single verse**. The current architecture binds adjacent clauses (it does not split below clause-atom or bind across verse boundaries).

### v2 — LLM adjudication (optional)

For cases the mechanical layer cannot decide (typically length-dependent restrictive ʾăšer, aetiological formulas, dense parallelism), narrow per-group LLM calls answer specific yes/no questions. This is OPTIONAL — the mechanical layer alone produces a publishable draft.

When used, the LLM:
- Receives one clause-group + 2-3 prior groups as context
- Answers a single narrow question (e.g., "how many ATUs in this group?")
- 3 independent passes with agreement scoring

The LLM does NOT do chapter-level rendering. Its scope is narrow per-group adjudication on the mechanical layer's residuals.

### v3 — Editorial review

The editor adjudicates between the mechanical-first output and any v2 LLM verdicts, plus inspects flagged-uncertain cases. Output is the final ATU rendering.

For chapters where the editor produces a hand-validated rendering, v0-v2 serve as cross-check, not replacement.

## §4 Per-corpus instantiation

The framework is corpus-agnostic. Each corpus instantiates:

1. **Data layer**: source text, parse layer (BHSA / Macula Greek / Stanza CoNLL-U / etc.), version-anchoring (TAHOT / Strong's / Skousen)
2. **Binding-rule catalog**: language-specific (Hebrew B1-B14 validated; Greek / EME / Latin TODO)
3. **Pipeline scripts**: chapter-parametric `pilot_config.py` + `v1_extract` + `v1_5_apply_bindings` + `v3_compare`
4. **Editorial review surface**: per-batch review file in `directives/replies/`

**Currently validated**: Hebrew (Tanakh) across 4 genres — narrative+dialogue, wisdom poetic, prophetic poetic, casuistic legal-list.

## §5 Validation status

**Hebrew Tanakh — four chapters tested cross-genre:**

| Chapter | Genre | Pipeline=cold-eye | F1 vs LDHB | Precision | Recall |
|---|---|---|---|---|---|
| Gen 22 | Narrative+dialogue | 83% (20/24) | 91.2% | 92.9% | 89.7% |
| Psalm 1 | Wisdom poetic | 100% (6/6) | 88.9% | 100% | 80.0% |
| Isaiah 53 | Prophetic poetic | 58% (7/12) | 88.3% | 82.9% | 94.4% |
| Lev 11 (v.1-12) | Legal-casuistic | 25% (3/12) | 85.2% | 79.3% | 92.0% |

Boundary F1 is genre-stable (85-91%). Recall is consistently ≥ 80%. Precision varies (79-100%) — pipeline is conservative on prose, over-segments in dense parallelism and legal lists. **The 14-rule mechanical layer produces ATU drafts requiring 5-25% editorial absorption depending on genre.**

**Lexham Discourse Hebrew Bible (LDHB)** is consulted as a calibration reference; the pipeline does not depend on it at runtime. See `methodology-position.md` for the "Lexham-consulted but not utilized" framing.

## §6 Known gaps

Three architectural gaps the v1.5 mechanical layer cannot currently handle:

1. **Sub-clause gapping** — when BHSA puts two ATUs inside one clause-atom via verb-elision in parallel comparatives (Gen 22:17 stars + sand pattern). Requires sub-clause splitter.
2. **BHSA-fine subject-predicate split** — when BHSA puts one ATU across two clause-atoms (subject NP + asyndetic verb predicate, Ps 1:3 vekhol-asher-ya'aseh / yatzliach). B14 handles the common case; some variants remain.
3. **Length-dependent restrictive ʾăšer** — propositionally-weighty asher clauses with internal subject + verb sometimes stand as own ATU (Stan's editorial choice), sometimes bind. Not mechanically decidable.

All three are appropriate cases for optional v2 LLM adjudication or editorial review.

## §7 Change discipline

Adding or modifying a binding rule MUST:

1. Identify the BHSA (or equivalent) features that drive the rule
2. Test against the validated chapter set (Gen 22 / Psalm 1 / Isaiah 53 / Lev 11)
3. Verify no regression in cold-eye-match or F1 on prior chapters
4. Document under [`binding-rules-hebrew.md`](binding-rules-hebrew.md) (or per-language equivalent)

The bidirectional test §2 is the criterion. Any proposed binding must trace back to it. Rules that produce candidate boundaries WITHOUT cognitive-criterion grounding (te'amim hierarchy as primary, parallelism class as primary, aesthetic preference) are forbidden.

---

## Where to read next

- [`toolset-architecture.md`](toolset-architecture.md) — pipeline implementation per stage
- [`binding-rules-hebrew.md`](binding-rules-hebrew.md) — the 14 validated Hebrew binding rules
- [`apparatus.md`](apparatus.md) — scope statement
- [`methodology-position.md`](methodology-position.md) — LDHB / discourse-grammar relationship
- [`../memories/`](../memories/) — discipline lessons
