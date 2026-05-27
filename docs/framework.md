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

## §2 The criterion — what licenses a standalone ATU

The unit is the **atomic _thought_ unit**, not the atomic predication. "Thought" is operationalized primarily by a grammatical test (§2.1) — but grammatical closure is a *proxy* for thought, and it under-captures thought at one principled boundary: an explicit authorial marker of a thought-move. So a line is a legitimate standalone ATU if it satisfies **EITHER**:

- **(A) the bidirectional test** (§2.1, primary), OR
- **(B) the explicit-marker license** (§2.2, secondary — a closed registry of author-placed boundary tokens).

(A) is the default and does the overwhelming majority of the work. (B) is a narrow, closed-list **break-license**, not an ATU-from-fragment rule: it does not certify an incomplete fragment as a thought — it permits a break, at an author-placed marker, between cola that are *already* closure-eligible under (A) (often via elision-restoration) but that the KEEP-AS-IS default would otherwise hold merged. See §2.2 for why that keeps the objectivity firewall intact.

### §2.1 The bidirectional test (primary criterion)

A line passes the bidirectional test if and only if BOTH:

1. **Forward grammatical closure** — the line is grammatically complete on its own terms in the target language. Languages with morphologically-encoded subjects (Hebrew finite verbs, Greek finite verbs, Latin finite verbs) license pro-drop. Verbless / nominal-predicate constructions count as closed when subject + predicate are juxtaposed (Hebrew, Greek). EME English requires overt copula. **Elision-restoration is permitted** — when a verb is gapped from a parallel prior clause, the elision-restored clause counts as closed. *Valency note:* a transitive verb whose obligatory complement is absent from the line is NOT forward-closed (a bare assertion/speech verb — "I say to you …" — has an open content slot: "say *what?*"); it closes only via the cataphoric carve-out below, and only as a quotative announcement, not as an assertion-matrix.

2. **Backward referential self-containment** — the line's referents are established in prior discourse (immediately, via chain-continuity) or self-introducing within the line. Long-range antecedent dependencies (more than one ATU back without chain-continuity) fail backward containment.

A break between two adjacent lines is licensed if and only if both lines independently satisfy these two conditions (or one is licensed under §2.2).

**Asymmetry:**

- **Anaphoric failure** (backward-dangling): pronouns without antecedent on the line, deictic demonstratives ("these things," "that day"), discourse-anaphoric particles (`לָכֵן`, `עַל־כֵּן`, causal `כִּי`, "therefore") all fail backward containment.
- **Cataphoric introduction** (forward-pointing) does NOT fail — *but the carve-out is narrow, and the discriminator is **complement-vs-quote, not verb class**.* A presentative (`הִנֵּה` + indefinite NP) and a **quotative frame introducing distinct direct discourse** ("and he said:", `וַיֹּאמֶר`, `ἀμὴν λέγω ὑμῖν` before a quoted pronouncement) PASS: the frame is a complete cataphoric announcement and the quoted discourse is its *own* ATU (often a paragraph — unbindable). But a verb whose content follows as a **clausal complement** — *regardless of whether it is a cognition, perception, or speech verb* — is forward-incomplete ("know/say *what?*") and **binds** its complement into one ATU: `οἶδα ὅτι` / "I know that X", and equally "I say to you [that] it is well…". The verb's open valency is filled by the complement; it does not stand alone. **So: clausal complement → matrix binds; distinct quoted performance (third-party direct discourse, parataxis) → frame stands.** Verb identity (cognition vs. declaration) is *not* the variable — it was a proxy for complement-vs-quote.

  **The performative assertion-matrix is settled by this:** a first-person performative ("I say to you," "Verily I say unto you," "I say to you that …") begs "say *what?*" identically across its surface variants and **binds** its content — it is a complement-taker, not a quotative frame.

  **Quote-status has no independent force — only the bidirectional test decides** (Stan, 2026-05-26: *"our mission is not to reveal quotes, it's to reveal ATUs"*). "It is a quote" is never itself a reason to bind or stand. The bind/stand call rests on two punctuation-invariant *syntactic* tests, both feature-sourced from the Macula Greek treebank (NOT hand-adjudicated by lemma lists — see the dataset catalog in memory):

  1. **Object-slot test (complement vs. causal/adverbial ὅτι).** The complement-vs-quote rule applies ONLY when the ὅτι-clause actually fills the verb's object slot. Macula marks this directly: `rule="that-VP"` / clause `role="o"` = a ὅτι/ἵνα **complement** (bind-eligible); `rule="sub-CL"` / `role="adv"` = a **causal/adverbial** ὅτι, which is neither a complement nor a quoted performance — it is an adverbial adjunct and follows subordinate-clause handling, NOT this rule. This resolves *Janus* verbs (same lemma, both functions): `ὤμοσεν … ὅτι χρόνος οὐκέτι ἔσται` (Rev 10:6, `that-VP` = oath's content → **bind**) vs. `ὀμόσῃς … ὅτι οὐ δύνασαι` (Matt 5:36, `sub-CL` = causal → **stand**); likewise John 2:18, 1Cor 3:13 (`sub-CL` → stand). No lemma list can separate these; the treebank does.

  2. **Deixis test (indirect complement vs. re-performed direct discourse), among `that-VP` complements.** **Bind** when the complement is the matrix's own propositional content — *shared deictic center* (Rom 8:16 `συμμαρτυρεῖ ὅτι ἐσμὲν τέκνα θεοῦ`, 1st-pl, Paul's own assertion). **Stand** when it is a re-performed utterance with its *own* deictic center — a speaker/addressee shift (Rom 9:17 `λέγει ἡ γραφὴ τῷ Φαραὼ ὅτι Εἰς αὐτὸ τοῦτο ἐξήγειρά σε` — God-to-Pharaoh, "I/you"). This is why Gal 3:8's two ὅτι split differently: the first (`ἡ γραφὴ … ὅτι ἐκ πίστεως δικαιοῖ … ὁ θεός`, 3rd-person reported, shared deixis) **binds**; the second (`ὅτι Ἐνευλογηθήσονται ἐν σοί`, 2nd-person address to Abraham) **stands**. A verbatim re-performed citation therefore **stands** on its own deixis — not because it is "a quote," but because by the bidirectional test it is its own ATU. **Person morphology alone cannot carry this** (1st-singular = "stand" in Rom 9:17 but "bind" in 2Thess 2:5); it requires participant tracking — Macula's `subjref`/`referent`. The recitative quote-guard (Mark 5:23 `λέγων ὅτι Τὸ θυγάτριόν μου …` must never be pierced) is the same test: a re-performed quote has a distinct deictic center.

  **Status (2026-05-26):** the earlier hand-counted "citation-attribution COLLAPSE-CLEAN, 14/15 bind" claim is **superseded** — it pre-dated the deixis test and the Macula re-sourcing, and over-bound the re-performed verbatim citations (Rom 9:17, John 15:25) that should stand. The bind/stand rates must be **re-measured mechanically** off Macula's `rule`/`role`/`person`/`referent` features, not eyeballed. Engine implication: the GNT binding decision should source these features from **Macula Greek** (`readers-gnt/research/macula-greek/`), where it currently reads the thinner `sblgnt-lowfat`; the lemma-list generalization of `merge_cognition_hoti` attempted 2026-05-26 produced causal over-binds (Matt 5:36, John 2:18, 1Cor 3:13) precisely because it lacked the `that-VP`/`sub-CL` signal. The one regression-free piece of that attempt — the `_junction_same_verse` guard (no silent cross-verse ὅτι merge, framework §3) — is independently ship-worthy.

**Restrictive relative clause binding** is a corollary: restrictive relatives bind to their head noun regardless of internal completeness, because removing them leaves the head not uniquely identified. Universal across Hebrew `אֲשֶׁר`, Greek `ὅς`/`ὅστις`, EME English "which"/"who"/"that".

**Punctuation has ZERO force — including parser decisions conditioned on it (parse-substrate corollary).** Editorial punctuation (commas, colons, ano-teleia, sof-pasuq) and accentuation (te'amim) are overlay added after the author's thought-structure; they have zero force in ATU decisions. This extends to the **parse substrate** the binding rules run on. Parsers are trained on punctuated text, so a parser's structural label can be *conditioned on punctuation* — e.g. a comma after a verbum dicendi inducing `parataxis` where an overt complementizer would have yielded `ccomp` ("I say to you**,** it is well…" → parataxis; "I say to you **that** it is well…" → ccomp — same grammatical relation, the difference is only the comma). **Such a label is NOT load-bearing.** Binding rules MUST key on **punctuation-invariant features** (lemma, POS, finiteness, head attachment) and MUST treat punctuation-conditioned label-variants as **equivalent** (a finite content clause of a speech verb binds whether tagged `ccomp` or `parataxis`). A binding boundary that flips on a comma is a punctuation-driven decision and is forbidden — even when the punctuation entered the decision indirectly, laundered through the parser.

### §2.2 The explicit-marker license (secondary criterion)

A colon that is **closure-eligible under (A)** — forward-closed (often via the elision-restoration §2.1 permits: a finite verb gapped from the immediately-prior parallel clause) and backward-contained by immediate chain-continuity — but which the **KEEP-AS-IS default holds merged** (the framework does not split parallel cola on its own), may be **broken onto its own line when it opens with an explicit author-placed marker** from the closed **Marker Registry** (per-corpus, audited). The marker does NOT make a fragment into an ATU — the colon is already a legitimate unit under (A); the marker supplies the **break-license** the keep-as-is default otherwise withholds, signalling that this closure-eligible beat is a distinct authorial thought-move (escalation, restatement, enumerated parallel assertion).

**This is the framework's only *productive* (break-generating) licensor, and it is deliberately quarantined.** It is distinguished from the forbidden "producer-style rule" (glossary) *only* by two preconditions, and safety rests on their conjunction — NOT on "the token is on the page" (te'amim are on the page too, and stay banned): **(a)** the colon independently satisfies (A) — closure-eligibility; **(b)** the break is keyed to a **closed list of discrete author lexemes**, never to inferred parallelism, accentuation, or genre. Drop either precondition and it collapses into the banned analyst-overlay category. The marker, in short, is permission to *break* a unit that is already self-standing — not permission to *create* a unit that is not.

**Scope — what needs (B) vs. what (A) already covers.** Clause-level connectives (Hebrew waw-consecutive; Greek δέ/γάρ/μέν/οὖν; English "for") do **NOT** need (B): each heads its own finite predication and already passes (A). (B) is reserved for markers that license a split **below** the level (A) would license:

- **Sub-clausal asseverative / amplificative openers** that subdivide a single predication — e.g. BoFM English `yea`, `or rather`; candidate twins: Hebrew asseverative `אַף` / `כִּי`, Greek `ναί`. ("…without stubbornness of heart, **yea**, without being brought to know the word" — the `yea` clause shares the matrix verb and so fails forward closure, but the marker opens a distinct amplification beat.)
- **Parallel subordinator-stacks** — a stack of ≥2 coordinate indicative complement/appositive clauses, each propositionally complete once its shared subordinator is stripped, marked by a repeated subordinator (English "that … that … that"). The stack splits into enumerated assertion-beats. (Distinguish from a *single* subordinate complement, which binds under (A); and from *adverbial-purpose* "that"/`ἵνα`, which binds forward.)

**Registry discipline.** Each marker is registered per-corpus with its bidirectional-test status and a worked example; adding one is a §7.3 closed-list-extension audit trigger, and the audit tests **firewall-conformance** (do conditions i–iii hold) not merely output quality. A token enters the registry ONLY if: (i) it is a **single discrete author lexeme** — not a repeated/positional pattern, and not an anaphoric element repurposed as a marker; (ii) the colon it heads is **closure-eligible under (A)** — propositionally complete minus the marker, or forward-closed by restoring a **gapped finite verb** from the immediately-prior parallel clause (a shared *finite verb* only — NOT a shared subject / object / prepositional phrase, which would re-admit the parallel-cola splitting §2 forbids); and (iii) the break is not already licensed by (A)'s asymmetry (clause-level connectives already pass — see Scope).

**Default action**: KEEP-AS-IS unless (A) or (B) affirmatively licenses a break. The framework does NOT include cognitive-unity gates on parallel cola, parallelism class adjudication, te'amim hierarchy, or genre anchors as primary licenses — only the bidirectional test and the closed explicit-marker registry license a break.

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
