# R28-ext: Speech-Act Announcement After Frame — GNT Scholarship Companion

**Operational entry:** see `readers-gnt/private/01-method/colometry-canon.md §3.6 R28-ext` (current).

**Status:** This is the scholarship companion documenting WHY R28-ext exists, HOW we know it is correctly framed, and what intellectual/empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

R28-ext (Speech-Act Announcement After Frame, split direction) requires that when a finite speech verb introducing direct speech co-occurs on the same v4-editorial line with a *substantive* preceding adverbial frame — temporal clause (ὡς/ὅτε/ὅταν + finite verb), causal clause, or participial absolute frame — the line MUST be split. The frame occupies line 1; the finite speech verb and its dative-object address (if any) occupy line 2, closed with the ano teleia (·) or colon (:) per R11.

R28-ext is the split-direction complement of §3.6 frame-aggregation (which handles merge direction). Frame-aggregation absorbs a *structurally trivial* qualifier (bare ἐάν/ὅταν + single subjunctive, no own finite-clause body) onto the speech-verb line. R28-ext splits the reverse case: a *substantive* frame (own subject, verb, object content) that is falsely co-lineated with the speech verb that follows it.

Two Greek-specific exclusions are critical and absolute: (1) ἀπεκρίθη + ὅτι is R10-governed declarative-verb complement — R28-ext does not fire; (2) ἀπεκρίθη + λέγων is a Semitic pleonasm — a Hebraism treated as a fused speech-intro unit under R11, not a split candidate.

## Rationale

The frame and the speech-act are two distinct cognitive frames, each encoding one complete predication.

The adverbial frame sets the scene — when, where, or under what conditions speech occurred. It contains its own finite verb, subject, and often object content. The reader must process it as a completed clause before reaching the speech announcement. The speech announcement ("he said to Simon:" / "he says:") is a separate complete communicative predication: subject + finite verb + dative address, closing with the direct-speech marker.

Co-lineating two complete predications violates the one-predication-per-line generative principle. The reader encounters both the scene-setup and the announcement within a single ATU, compressing what should be two cognitive frames into one. The split externalizes structure already latent in the text's own grammar.

This rule is the speech-intro-context instantiation of the same split-discipline already operative for genitive absolutes (R19) and adverbial subordinate clauses (R9). It is not a new principle; it is the application of an existing principle to the specific subclass in which the subordinate clause is immediately followed by a direct-speech introduction verb.

## Grammatical grounding

### Greek frame types attested in the corpus

**Temporal ὡς-clause + εἶπεν (Luke 5:4).** `ὡς δὲ ἐπαύσατο λαλῶν` — "when he stopped speaking" — is a finite temporal clause with subject (Ἰησοῦς, recovered from context), verb (ἐπαύσατο), and complementary infinitive (λαλῶν). It is a complete peripheral constituent in Smyth §2411 terms (temporal ἐπεί/ὡς clauses as frame-setting adverbials in narrative). `εἶπεν πρὸς τὸν Σίμωνα·` — subject recovered, finite aorist, dative addressee — is a complete speech-predication.

**ὅταν-temporal + λέγει (Heb 1:6).** `ὅταν δὲ πάλιν εἰσαγάγῃ τὸν πρωτότοκον εἰς τὴν οἰκουμένην` is a substantive ὅταν-clause with its own verb (εἰσαγάγῃ, aorist subjunctive) and accusative object (τὸν πρωτότοκον). `λέγει·` is the OT-citation speech-intro. Per BDF §382 and Wallace, ὅταν + subjunctive forms the protasis of a conditional temporal clause — a full adverbial predication, not a trivial qualifier.

**Participial frame + εἶπεν (Luke 14:15; Luke 5:20; Luke 14:21; Heb 8:8; Heb 10:5).** Participial frames with their own overt objects or substantial NP clusters function as adverbial circumstantial clauses (Smyth §2062–2070, "circumstantial participle"). When the frame has ≥3 non-punctuation tokens in the participle's NP cluster and is followed by a finite speech verb, two complete predications occupy one line.

- Luke 5:20: `καὶ ἰδὼν τὴν πίστιν αὐτῶν` (perception-frame, accusative object) + `εἶπεν·`
- Luke 14:21: `τότε ὀργισθεὶς ὁ οἰκοδεσπότης` (emotion-frame with overt subject) + `εἶπεν τῷ δούλῳ αὐτοῦ·`
- Heb 8:8: `μεμφόμενος γὰρ αὐτοὺς` (causal-participle frame, accusative object) + `λέγει·`
- Heb 10:5: `διὸ εἰσερχόμενος εἰς τὸν κόσμον` (inferential-participle frame, directional phrase) + `λέγει·`

The per-cola manuscript tradition is relevant: Codex Vaticanus and Codex Sinaiticus per-cola scribal layouts routinely give speech-tag matrix predications their own cola, distinct from preceding temporal/causal frames. The split is not an editorial innovation; it surfaces a presentation convention with deep manuscript precedent.

### Exclusion grounding

**Exclusion 1 — ἀπεκρίθη + ὅτι (R10-governed).** When ὅτι immediately follows a speech verb, the construction is a cognition/declaration-verb complement governed by R10. `ὅτι` here introduces indirect speech content — it is the complement of the speech act, not a preceding frame. R28-ext requires the adverbial to *precede* the speech verb and be *structurally peripheral*; ὅτι following the verb is the verb's own complement. R10 governs; R28-ext is out of scope. The canonical John 3:28 ὅτι-clause pattern illustrates this cleanly.

**Exclusion 2 — ἀπεκρίθη + λέγων Hebraism.** The double-verb construction `ἀπεκρίθη ... λέγων·` is a Semitic idiom pervasive in the Synoptic tradition, where λέγων is a redundant manner marker — a pleonastic participle functioning as a semantically empty speech-intro intensifier (BDF §420.1; Moule, *Idiom Book of NT Greek*, pp. 99–100). The λέγων does not introduce a second cognitive frame; it is fused with ἀπεκρίθη into a single speech-intro unit. R11 collapses the entire `ἀπεκρίθη ... λέγων·` onto one line; R28-ext does not fire because there is no autonomous preceding *frame* — ἀπεκρίθη itself is the speech announcement. Canonical cases: Matt 11:25, Matt 12:38, Mark 9:5, Luke 17:17.

## Empirical evidence

### Phase A — Initial codification (commits 06e32df + f2a3676, 2026-05-11)

Three STRONG-SPLIT-CANDIDATE applications established the rule's operational shape:

| Locus | Frame type | Split produced |
|-------|-----------|----------------|
| Luke 5:4 | Temporal ὡς-clause (finite verb ἐπαύσατο + complement λαλῶν) | `ὡς δὲ ἐπαύσατο λαλῶν,` / `εἶπεν πρὸς τὸν Σίμωνα·` |
| Heb 1:6 | ὅταν-temporal + subjunctive (εἰσαγάγῃ + full NP) | `ὅταν δὲ πάλιν εἰσαγάγῃ τὸν πρωτότοκον εἰς τὴν οἰκουμένην,` / `λέγει·` |
| Luke 14:15 | Participial frame (ἀκούσας + object) | `Ἀκούσας δέ τις τῶν συνανακειμένων ταῦτα` / `εἶπεν αὐτῷ·` |

Note: Heb 1:6 overrode a prior §3.6 merge example that had treated the ὅταν-clause as a short qualifier. The R28-ext canon entry's scope-boundary criterion (structural minimum frame vs. substantive finite-clause) correctly distinguishes these: the Heb 1:6 ὅταν-clause has its own verb + NP, disqualifying it as a trivial qualifier.

### Phase B — Validator surface (commit 0706314, 2026-05-11)

The validator (`check_r28_speech_act_frame.py`) surfaced 4 additional STRONG-SPLIT-CANDIDATE instances beyond the original 3. All 4 were cat-A mechanical hits applied without per-item review:

| Locus | Frame type | Split produced |
|-------|-----------|----------------|
| Luke 5:20 | Participial perception-frame (ἰδών + τὴν πίστιν αὐτῶν) | `καὶ ἰδὼν τὴν πίστιν αὐτῶν` / `εἶπεν·` |
| Luke 14:21 | Participial emotion-frame with overt subject (ὀργισθεὶς ὁ οἰκοδεσπότης) | `τότε ὀργισθεὶς ὁ οἰκοδεσπότης` / `εἶπεν τῷ δούλῳ αὐτοῦ·` |
| Heb 8:8 | Causal-participle frame (μεμφόμενος γὰρ αὐτοὺς) | `μεμφόμενος γὰρ αὐτοὺς` / `λέγει·` |
| Heb 10:5 | Inferential-participle frame (διὸ εἰσερχόμενος εἰς τὸν κόσμον) | `διὸ εἰσερχόμενος εἰς τὸν κόσμον` / `λέγει·` |

**Total corpus-wide:** 7 STRONG-SPLIT-CANDIDATE applications. Distribution: Luke 4 (5:4, 5:20, 14:15, 14:21), Hebrews 3 (1:6, 8:8, 10:5).

### REVIEW cases (5 outstanding)

The validator also surfaces cases that require per-instance Stan judgment:

1. **Interposed participles** (e.g., John 8:7 `ἀνακύψας εἶπεν αὐτοῖς`, Luke 19:5 `ἀναβλέψας ... εἶπεν`): single-word circumstantial participle with no own object or substantial NP cluster — short-frame minimum question. Does a 1–2 token participial frame earn its own line, or does the substantive-frame threshold (≥3 tokens per canon scope) correctly exclude it?

2. **Short 1–2 token frames** (John 11:4 and analogues): the ≥3 token threshold in the scope definition screens these out from STRONG-SPLIT; they surface as REVIEW-REQUIRED.

These 5 cases require Stan's judgment on the short-frame minimum threshold before they can be mechanically applied.

## Intellectual lineage

R28-ext is a GNT-corpus port of BoFM R28 (Speech-Act Announcement After Frame), the operational instantiation of the universal J3 (speech-act announcement) sub-principle at matrix-predication level. The BoFM rule governs the same structural condition — substantive adverbial frame + finite speech verb on the same colometric line — in the archaic KJV-register English of the Book of Mormon text. R28-ext re-calibrates the same rule to the Greek NT target corpus, replacing the BoFM closed lists with GNT equivalents:

| Dimension | BoFM R28 | GNT R28-ext |
|-----------|---------|-------------|
| Speech lemmas | *say, speak, declare, cry, answer* | λέγω, εἶπον, φημί |
| Frame marks | *after, when, while, before, since* etc. | ὡς, ὅτε, ὅταν, ἐπεί, ἐπειδή, participial frames |
| Participial-continuation exclusion | *, saying:* (archaic continuation marker) | λέγων Hebraism (ἀπεκρίθη+λέγων) |
| Result-direction filter | *that, insomuch, until* following speech verb | ὅτι immediately following speech verb (R10-governed) |

The rule is the **split-direction complement of §3.6 frame-aggregation**. §3.6 frame-aggregation handles the merge direction: when a trivial qualifier (bare ἐάν + single subjunctive) precedes a speech verb, it merges onto the speech-verb line because the qualifier lacks the predication-weight to stand alone. R28-ext handles the opposite case: when the qualifying frame IS predication-weight-sufficient (own verb + object + subject), it earns its own line and forces a split. Together the two rules bracket the boundary between trivial qualifier (aggregate) and substantive frame (split).

The **Lukan narrative** and **Pauline-transition** pattern appear most prominently in the corpus: Luke uses participial perception and emotion frames before speech verbs as a narrative style device (ἰδών, ἀκούσας, ὀργισθείς). Hebrews uses participial and inferential frames before OT-citation speech intros (μεμφόμενος, εἰσερχόμενος). Both patterns are high-frequency and structurally clean R28-ext triggers.

## Adversarial history

The audit that established R28-ext was task `a80b9f5b92c7f1125`, with audit evidence present in commit `f2a3676`.

### 1. Port from BoFM R28

The GNT adaptation required identifying the two Greek-specific exclusions absent from the BoFM version. BoFM R28's participial-continuation exclusion covered *, saying:* — a uniquely archaic-English construction. The Greek equivalent is structurally different: the ἀπεκρίθη + λέγων Hebraism is not merely a participial continuation marker but a fully fused double-verb idiom with Semitic roots. A naïve port of the BoFM exclusion (excluding participial speech verbs) would have caught λέγων, but the adversarial audit established that the *reason* for exclusion is different — it's a Semitic idiom, not merely a participial form — and the exclusion must be defined on the specific lexical pair (ἀπεκρίθη + λέγων), not on participiality in general.

The ὅτι-complement exclusion (Exclusion 1) was added specifically for Greek: BoFM English has no structural equivalent of the verb-plus-ὅτι direct-complement pattern. R10 governs these cases in the GNT corpus; adding the exclusion ensured R28-ext would not misfire on John 3:28-style constructions.

### 2. Heb 1:6 override of prior §3.6 merge example

The initial §3.6 frame-aggregation section had cited Heb 1:6 as a canonical merge example — the ὅταν-clause was treated as a short qualifier aggregating onto the speech verb. The adversarial audit challenged this: the Heb 1:6 ὅταν-clause contains its own verb (εἰσαγάγῃ), accusative object (τὸν πρωτότοκον εἰς τὴν οἰκουμένην), and conjunction (δέ) — it is not a bare ὅταν + single-word subjunctive. The audit concluded it met the R28-ext substantive-frame threshold and that the prior §3.6 merge example was wrong. The §3.6 scope boundary was refined to specify "bare ἐάν/ὅταν + single-word subjunctive with no substantial finite-clause body," and Heb 1:6 was moved from §3.6 merge examples to R28-ext split examples. The canon is now internally consistent on this boundary.

### 3. Short-frame minimum question (open)

The ≥3-token threshold in the scope definition (participial frames with own subject/object content ≥3 non-punctuation tokens) was set to exclude single-word frames (e.g., `ἀνακύψας εἶπεν` where ἀνακύψας is a bare 1-token participle with no object). The threshold was an adversarial-audit recommendation to prevent R28-ext from over-applying to bare circumstantial participles. However, the 5 REVIEW cases above test its boundary; the threshold needs Stan confirmation before the REVIEW cases can be resolved mechanically.

## Future work

1. **REVIEW cases (5):** Stan judgment needed on interposed-participle and short-frame minimum cases before the ≥3-token threshold can be confirmed or revised. Once confirmed, the REVIEW cases either apply mechanically (if threshold lowered) or remain excluded (if threshold confirmed).

2. **Heb 1:6 split confirmation:** The override of the prior §3.6 merge example deserves Stan verification of the split preference (`ὅταν δὲ πάλιν εἰσαγάγῃ τὸν πρωτότοκον εἰς τὴν οἰκουμένην,` / `λέγει·`).

3. **Speech-lemma closed list:** The current `SPEECH_LEMMAS_R28EXT` (λέγω, εἶπον, φημί) reflects the most common direct-speech verbs. Corpus-frequency audits may surface additional verbs (e.g., ἀποκρίνομαι in non-Hebraism constructions, κράζω, βοάω). Future expansion should be driven by REVIEW-case surfacing, not prospective enumeration.

4. **Acts pattern:** `μετὰ + articular-infinitive + ἀπεκρίθη` (Acts 15:13 type) was cited in the codification context as a related temporal-frame pattern. Acts corpus-wide scan against this construction may surface additional R28-ext candidates.

5. **Cross-corpus consistency:** The readers-tanakh sibling (Hebrew *wayyomer* + temporal/causal frame patterns) and the BoFM R28 share the same J3 sub-principle lineage. Aligning the three operational canons' exclusion structures — especially the participial-continuation-marker exclusion — is future harmonization work.

---

*Cross-references:*

- Operational canon entry: `readers-gnt/private/01-method/colometry-canon.md §3.6 R28-ext` (current state)
- Sister rule (BoFM): [`../bofm/R28.md`](../bofm/R28.md) — Speech-Act Announcement After Frame (BoFM corpus instantiation)
- Validator: `readers-gnt/validators/colometry/check_r28_speech_act_frame.py`
- Framework anchor: [`../../docs/framework.md`](../../docs/framework.md) §1.4 J3 (speech-act announcement structural justification)
- Audit task: `a80b9f5b92c7f1125`; audit evidence in commit `f2a3676`
- §3.6 split-direction complement: §3.6 frame-aggregation (merge direction, same section)
- Precedence rules: R9 (general subordinate-clause break), R10 (ὅτι complement), R11 (speech-intro own line), R19 (genitive absolute)
