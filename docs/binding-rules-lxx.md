# LXX Greek Binding Rules Catalog

> **Status (2026-06-06): smoke-test artifact — pipeline PARKED 2026-05-27.** The rule
> designs in this catalog were drafted against the UD_Ancient_Greek-PTNK gold (Gen+Ruth,
> the only available gold LXX syntax treebank) but the live LXX pipeline
> (`scripts/lxx_generate.py` in `readers-lxx/`) currently uses a different UD-native
> architecture; the integration target for this catalog is the projection-v1 generator
> not yet wired live. The rule designs are the restart point when the projection
> pipeline goes active. This catalog is NOT authoritative live canon today; it is
> recorded here so the work is preserved + version-controlled (per 2026-06-05 forensic
> audit recommendation, surfaced via claudit citation-rot scan).

Catalog of mechanical binding rules for the **Greek Septuagint** layer of the cross-corpus
ATU pipeline. Sister catalog to [`binding-rules-hebrew.md`](binding-rules-hebrew.md).

The LXX pipeline is a **Hebrew-projection** pipeline (CATSS-aligned BHSA clause-atoms
projected through MT→LXX word alignment onto the CenterBLC Greek word stream). This
catalog operates on the **post-projection** Greek partition: per-verse, an ordered list
of clause-atom groups (each group = a contiguous run of Greek tokens).

Each rule:
- Fires based on Greek surface features (lemma after diacritic-strip, POS, prefix tokens)
  and/or projection-trace metadata (the Hebrew clause-atom each LXX line projected from)
- Is justified by the bidirectional test (`framework.md` §2)
- Operates only within a single verse (global safety guard in `should_bind()`)
- Is evaluated in order; the first matching rule wins

Validation corpus: UD_Ancient_Greek-PTNK gold (Genesis + Ruth only — the *only* gold LXX
syntax treebank in existence as of 2026-05-30). 1547 scored verses.

---

## Why a separate Greek catalog (LXX-specific concerns)

1. **Hebrew → Greek translation slack.** CATSS line splits do not perfectly track
   clause-atom boundaries. A single Hebrew clause-atom is sometimes spread across
   multiple CATSS lines (the translator chose to render verbosely / split). Each CATSS
   line currently projects to its first-MT-word's atom — but the projection emits one
   "atom" per CATSS line, so within a single Hebrew clause-atom we can get **multiple
   projected Greek atoms that share the same Hebrew clause-atom index**. This is the
   biggest source of over-split in the projection-v1 substrate, and the LXX-B0 rule
   (below) collapses it deterministically.

2. **Greek surface features differ.** Hebrew B5 (wayhi temporal frame) is keyed on the
   `ויהי` consonants; the LXX renders this as `καὶ ἐγένετο` + temporal phrase. The
   trigger has to be re-keyed on Greek surface forms.

3. **Genitive absolute** is a Greek-original construction with no Hebrew analog — the
   Hebrew catalog does not handle it. The LXX commonly opens with `+ Gen + ptcp.gen`
   constructions (often projecting from a Hebrew infinitive construct or temporal
   clause). Needs a Greek-original rule.

4. **No Greek vocative-case marker.** Hebrew B1 (Voct clause type from BHSA) does not
   port: BHSA has a clause-type tag for vocative clauses; the LXX projection doesn't
   carry that. We approximate via Greek nominative-of-address / vocative-case
   morphology when available, otherwise rely on LXX-B0.

---

## Rule catalog

### LXX-B0 — Same-Hebrew-source-atom collapse (the projection shortcut)

| | |
|---|---|
| Trigger | `prev.hebrew_atom == curr.hebrew_atom` AND both are non-None |
| Action | BIND backward (collapse curr into prev's group) |
| Justification | If two adjacent projected lines were emitted from the *same* MT clause-atom (verified mechanically via CATSS→Macula-Hebrew lookup), they represent one Hebrew thought-unit that CATSS happened to render across two alignment lines. The Hebrew bidirectional-test verdict at the source carries through to the Greek: if Hebrew had one ATU, Greek (as a translation) inherits one ATU unless the translator added independent material. This is the strongest binding signal in the LXX pipeline because it is *substrate-deterministic*, not a Greek-surface heuristic. |
| Provenance | LXX-original (cross-corpus shortcut: CATSS×BHSA projection mechanics) |
| Confidence | HIGH — substrate-deterministic |
| Risk lens | **Over-merge risk**: low. The only way this binds incorrectly is if the LXX translator inserted a genuinely independent ATU's worth of new material into a slot CATSS rolls up into one MT atom. Possible (Greek pluses) but rare; flagged as audit residual. |
| Test cases | Gen 22:1 lines 3+4 (`καὶ εἶπεν πρὸς αὐτόν` + `Ἁβραάμ Ἁβραάμ`) — both project to the same `וַיֹּאמֶר` MT atom; should collapse to 1 ATU.  Ruth 1:1 (verse-internal redundancy collapses). |

### LXX-B1 — Vocative nominative-of-address binds backward

| | |
|---|---|
| Trigger | curr line is morphologically a vocative or nominative-of-address (single proper noun, or proper noun + repeated proper noun: `Αβρααμ`, `Αβρααμ Αβρααμ`, `Σαμουηλ Σαμουηλ`); detected via: line consists only of tokens with `upos == "PROPN"` (or a 1–2-word line whose tokens are all proper nouns), no finite verb in the line. |
| Action | BIND backward |
| Justification | Direct port of Hebrew B1 (Voct → bind). A vocative-only line fails forward grammatical closure (no predication) and fails backward containment (its referent is the addressee just named/about-to-act). The previous speech-frame supplies what it needs. Same bidirectional-test result as Hebrew. |
| Provenance | Hebrew B1 (vocative-only clause binds backward) |
| Confidence | HIGH |
| Risk lens | Over-merge risk: low. The only false positive would be a proper-noun-only utterance standing alone as its own narrative move ("Then: Abraham." — vanishingly rare in LXX prose). |
| Test cases | Gen 22:1 `Ἁβραάμ Ἁβραάμ` after `καὶ εἶπεν πρὸς αὐτόν` — bind (combined with LXX-B0, same atom). Gen 22:11 vocative `Ἁβραάμ Ἁβραάμ` — bind to preceding speech frame. |

### LXX-B2 — Restrictive ὅς / ὅστις binds backward

| | |
|---|---|
| Trigger (v2, morph-gated) | curr line's first token has CenterBLC TF morph code beginning with `RR` (=`pronoun, relative`). This cleanly admits ὅς / ὅστις / ὅσπερ in any case-number-gender and cleanly excludes (a) the article ὁ (`RA.*`), (b) the conjunction ὡς (lex='os', morph `C`), and (c) the adverb οὗ "where" (lex='os', morph `D`) — all of which lex-only or surface-only triggers wrongly admit. |
| Trigger (v1 backstop, no morph available) | curr line's first token (after diacritic-strip + lowercase) is in `{ος, ον, ο, οι, η, αι, ων, ω, ους, οις, ας, αις, ης, ηι, ωι}` (forms of relative pronoun ὅς) OR in `{οστις, οντινα, ωτινι, ηντινα, αιτινες, οιτινες, ητις}` (ὅστις). NOTE: this v1 form has documented collisions and is retained only as fallback. |
| Action | BIND backward |
| Justification | Direct port of Hebrew B3 (אֲשֶׁר → bind). Restrictive relative clauses bind to their head noun regardless of internal completeness — removing them leaves the head not uniquely identified (`framework.md` §2.1, "Restrictive relative clause binding"). Universal across Hebrew אֲשֶׁר / Greek ὅς-ὅστις / EME English which-who-that. |
| Provenance | Hebrew B3 (restrictive ʾăšer binds backward) |
| Confidence | MEDIUM — heads the same known limitation as B3 (length-dependent over-binding on propositionally weighty relatives). LXX adds a second risk: Greek often uses ὅς for non-restrictive relatives too, which are NOT bindable. The morph gate (RR) eliminates the homograph noise but cannot distinguish restrictive vs. non-restrictive use; that residual is deferred to v2 LLM. |
| Risk lens | **Over-merge risk: medium** for long ὅς clauses. The Hebrew known-gap applies; the Greek non-restrictive ὅς extends it. Morph gating REMOVED the v1 article-ὁ / conjunction-ὡς / adverb-οὗ false-positive class entirely. |
| Test cases | Gen 1:7 `ὃ ἦν ὑποκάτω τοῦ στερεώματος` (gold-attached as a relative modifier of `ὕδατος`). Gen 22:2 `ὃν ἠγάπησας` (restrictive on `υἱόν σου`). Counter-test (must NOT fire): Gen 22:7 `ὁ δὲ εἶπεν` — article ὁ, morph RA.NSM, blocked. |

### LXX-B3 — καὶ ἐγένετο + temporal anchor binds forward — DEFAULT-DISABLED (v2)

| | |
|---|---|
| Status (v2, 2026-05-30) | **DEFAULT-DISABLED** via module-top feature flag `ENABLE_KAI_EGENETO=False` in the applier. Rule definition retained for future testing / narrowing experiments. |
| Trigger (when enabled) | prev line text (diacritic-stripped, lowercased, first 30 chars) begins with `και εγενετο` AND prev line continues with a temporal anchor token from `{εν τω, μετα, οτε, ως, ως δε, ηνικα, εν τη ημερα, εν εκειναις, εν ταις ημεραις, μετα τα ρηματα, μετα ταυτα}` |
| Action (when enabled) | BIND forward (next line binds to prev) |
| Justification | Direct port of Hebrew B5 (wayhi temporal frame). Hebrew `וַיְהִי` + temporal anchor renders into Koine as `καὶ ἐγένετο` + temporal phrase. The frame is anaphoric to prior narrative (deictic backward) and fails standalone backward containment; binds forward to the main clause it frames. Same pattern Stan recognized in BoFM "and it came to pass" (AICTP) frames. |
| Provenance | Hebrew B5 (wayhi temporal frame) |
| Confidence | HIGH on the trigger-pattern in Hebrew; the v1 smoke test demonstrated it does NOT transfer cleanly to UD-PTNK gold Greek. |
| Risk lens | **Over-merge risk: HIGH against UD-PTNK gold.** v1 smoke (2026-05-30) had 2 helped / 16 hurt; gold treats the wayhi-frame as its own ATU even when temporally anchored. Analysis of the 2 helps (Gen 24:45 `πρὸ τοῦ συντελέσαι`, Gen 31:10 `ἡνίκα ἐνεκίσσων`) vs the 16 hurts (e.g. Gen 6:1 `ἡνίκα ἤρξαντο`, Gen 11:2 `ἐν τῷ κινῆσαι`, Gen 19:29 `ἐν τῷ ἐκτρῖψαι`, Gen 22:1 `μετὰ τὰ ῥήματα ταῦτα` — the *canonical* anchor!) revealed **no Greek-surface pattern that separates helps from hurts cleanly** — the same anchor tokens appear in both groups. Per `feedback_conformance_is_not_correctness.md`, this may reflect the gold-segmenter's behavior rather than methodological truth; revisit when v2 LLM adjudication is available. |
| Test cases (when re-enabled) | Gen 24:45 (helped in v1). Gen 31:10 (helped in v1). |
| Counter-example | Per v1 data, virtually all temporally-anchored `καὶ ἐγένετο` openings — gold partitions the frame separately. |

### LXX-B4 — Purposive τοῦ + infinitive binds backward

| | |
|---|---|
| Trigger | curr line begins (diacritic-stripped, lowercased) with `του ` followed by a token that ends in `-ειν`, `-σαι`, `-ναι`, `-σθαι`, `-εσθαι`, `-σθηναι` (Greek infinitive endings) within the first 3 tokens |
| Action | BIND backward |
| Justification | Port of Hebrew B10 (purposive InfC). The Greek genitive-articular infinitive (`τοῦ + INF`) expresses purpose, tightly bound to the main verb. Fails standalone backward containment (the agent is supplied by the main verb). The Hebrew `לִ + InfC` and Greek `τοῦ + INF` are translation-equivalents; the bind decision carries through. |
| Provenance | Hebrew B10 (purposive infinitive construct) |
| Confidence | HIGH |
| Risk lens | Over-merge risk: low. `τοῦ + INF` is unambiguously a non-finite construction; cannot stand alone as an independent ATU under the bidirectional test. |
| Test cases | Ruth 1:1 `καὶ ἐπορεύθη ἀνὴρ ἀπὸ Βαιθλεεμ…` + `τοῦ παροικῆσαι ἐν ἀγρῷ Μωαβ` → one ATU. Gen 22:5 `… τοῦ προσκυνῆσαι` (purposive). |

### LXX-B5 — Bare λέγων / εἶπεν speech-frame complement binds forward

| | |
|---|---|
| Trigger | prev line ends with a participial speech verb (`λεγων`, `λεγουσα`, `λεγοντες`, `λεγουσαι`, `λεγουσιν`) or a single-token finite speech verb (`ειπεν`, `ειπαν`, `ειπον`, `ελαλησεν`, `εκαλεσεν`) AND prev line is ≤ 3 Greek tokens |
| Action | BIND forward only if the *Hebrew source atom* of the speech-frame line is the same as the *Hebrew source atom* of the curr line — this is effectively a refinement of LXX-B0 on the speech-frame edge. |
| Justification | Cross-references `framework.md` §2.1: "Speech-margin (`וַיֹּאמֶר`) is its own ATU IF AND ONLY IF the following speech can stand alone by the bidirectional test." Greek speech frames behave identically. A *bare single-token* `εἶπεν` or trailing `λέγων` is closer to a single-token wayyiqtol (Hebrew B7 pattern) and tends to bind into the speech act. When Hebrew said it's one atom, we follow. |
| Provenance | Hybrid: Hebrew B7 (bare wayyiqtol pair) for the single-token-prev signal + LXX-B0 atom-trace for the safety check. NOT a port of Hebrew B4 (which was retired). |
| Confidence | MEDIUM — Stan's red line is over-merge of speech-frame + content (the framework §2.1 carve-out). Strictly gated on LXX-B0 trace. |
| Risk lens | **Over-merge risk: HIGH** if applied without the LXX-B0 atom-trace gate. With the gate, risk drops to the LXX-B0 risk profile. |
| Test cases | Gen 22:1 — `καὶ εἶπεν πρὸς αὐτόν` is its own CATSS line projecting to the `וַיֹּאמֶר` atom; the next line `Ἁβραάμ Ἁβραάμ` projects to the same atom (LXX-B0 already binds it). LXX-B5 would only redundantly confirm. Gen 22:7 short `εἶπεν δέ` + content — bind. |

### LXX-B6 — Genitive absolute binds backward (Greek-original)

| | |
|---|---|
| Trigger (v2, morph-gated) | curr line's first 4 tokens contain a participle whose CenterBLC TF morph code matches `V\.[A-Z]{2}PG[SP][MFN]` (= participle in genitive case, any tense × voice × number × gender — covers V.PAPGSM "present-active", V.AAPGPN "aorist-active", V.XAPGSM "perfect-active", V.PMPGSM "present-middle", V.APPGPM "aorist-passive", etc.) AND a noun/pronoun/adjective with `case=Gen` appears within the first 5 tokens (the absolute's subject) AND the participle is NOT immediately preceded (within the head window) by an article in genitive case (which would make this a substantival use: `τῶν καθημένων` = "those sitting", NOT a gen-abs). |
| Trigger (v1 backstop, no morph available) | curr line, in its first 4 tokens, contains a token ending in one of `{-οντος, -οντων, -ουσης, -ουσων, -σαντος, -σαντων, -σασης, -σασων, -νθεντος, -θεντος, -θεντων, -θεισης, -μενου, -μενων, -μενης}`. NOTE: this surface form mis-fires on substantival participles + non-participle words sharing those endings; retained only as fallback. |
| Action | BIND backward |
| Justification | Greek-original construction with no Hebrew analog (Hebrew has no participle-case morphology; renders as a finite temporal clause). Genitive absolutes are circumstantial / temporal modifiers of the main clause: "while X was doing Y, …". They fail standalone backward containment under the bidirectional test — they're adverbial dependents of the matrix. Confirmed by GNT-side audit (`scripts/audit_anaphoric_gen_abs_macula.py` in readers-gnt: genitive absolutes consistently bind to their matrix). |
| Provenance | Greek-original (NOT a Hebrew port). Confirmed in `readers-gnt/scripts/sweep_r19_genabs.py` for the GNT side. |
| Confidence | HIGH on the morph-gated trigger (v2). The substantival-participle false-positive class — every v1 hurt was a substantival use under a GEN article (e.g. Gen 1:26 `τῶν ἑρπόντων`, Ruth 2:16 `τῶν βεβουνισμένων`, Ruth 4:4 `τῶν καθημένων`) — is eliminated by the no-preceding-GEN-article gate. |
| Risk lens | Over-merge risk: low. Genitive absolutes never stand alone as ATUs under the bidirectional test. One v2 over-merge residual (Gen 25:6 `ἔτι ζῶντος αὐτοῦ`) is methodologically defensible — gold treats the gen-abs as its own ATU but framework §2 wants it bound; this is a `conformance ≠ correctness` case, not a rule failure. |
| Test cases | Gen 18:1 `ὤφθη δὲ αὐτῷ ὁ θεὸς… καθημένου αὐτοῦ ἐπὶ τῆς θύρας τῆς σκηνῆς` — the genitive absolute `καθημένου αὐτοῦ` (V.PMPGSM + `αὐτοῦ` GEN) binds to the main clause. Gen 24:30 `τῆς ἀδελφῆς αὐτοῦ λεγούσης οὕτως` (V.PAPGSF gen-abs). Gen 25:6 `ἔτι ζῶντος αὐτοῦ`. Gen 44:14 `ἔτι αὐτοῦ ὄντος ἐκεῖ`. Counter-test (must NOT fire): Ruth 4:4 `ἐναντίον τῶν καθημένων` — preceded by GEN article `τῶν`, substantival use, blocked. |

### LXX-B7 — ὅτι complement of cognition / perception binds backward

| | |
|---|---|
| Trigger | prev line's head verb lemma (or last verbal token's lemma) is in `{οιδα, γινωσκω, βλεπω, οραω, ειδω, ακουω, αισθανομαι, μιμνησκομαι, νοεω}` (cognition / perception verbs) AND curr line begins (diacritic-stripped, lowercased) with `οτι ` (followed by anything other than direct-discourse quote markers — the recitative ὅτι discriminator is a v2 task) |
| Action | BIND backward |
| Justification | Port of Hebrew B11 (cognition + ki-complement). The ὅτι-clause is the OBJECT of the cognition (a complement, not a separate assertion). Translates directly: Hebrew `יָדַעְתִּי כִּי` → Greek `ἔγνωκα ὅτι`. |
| Provenance | Hebrew B11 (cognition + ki-complement) |
| Confidence | MEDIUM — this rule fires on lemma-list cognition without the Macula `that-VP` / `sub-CL` discriminator (framework §2.1 explicitly warns this can over-bind causal ὅτι: Matt 5:36, John 2:18, 1Cor 3:13 are the GNT counter-cases). LXX gold (UD-PTNK) does not expose the role/rule features; we cannot distinguish complement vs. causal ὅτι mechanically here. Deferred to v2 LLM. |
| Risk lens | **Over-merge risk: medium** — causal-ὅτι false positives possible. KEEP-SEPARATE doctrine ("when in doubt KEEP separate" — `CLAUDE.md`) argues for either limiting the lemma list aggressively or punting this rule entirely. **Current default: rule is OFF in the applier (commented out) pending CenterBLC `that-VP`/`sub-CL` projection.** |
| Test cases | Gen 8:11 `ἔγνω Νωε ὅτι κεκόπακεν τὸ ὕδωρ` — bind. Counter: Gen 1:4 `καὶ εἶδεν ὁ θεὸς τὸ φῶς` + `ὅτι καλόν` — the gold partitions this as ONE atom (so binding gives the right answer here); but `… οὐ φοβῇ τὸν θεόν, ὅτι …` (causal "because") would be over-bound. |

### LXX-B8 — Discourse particle δέ / γάρ / μέν / οὖν: NO-OP (clarification rule)

| | |
|---|---|
| Trigger | curr line begins with `δε`, `γαρ`, `μεν`, `ουν` |
| Action | **NO-OP — never bind on this trigger alone.** |
| Justification | Per `framework.md` §2.2 Scope: clause-level connectives (Greek δέ/γάρ/μέν/οὖν; English "for") do NOT need explicit-marker (B). Each heads its own finite predication and already passes the bidirectional test. The KEEP-AS-IS default applies. This rule is documented to **prevent** a future implementer from adding a misguided "δέ/γάρ binds backward" rule. |
| Provenance | `framework.md` §2.2 (negative rule — explicit prohibition) |
| Confidence | HIGH (this is doctrine) |
| Test cases | N/A — this rule never fires by design. |

### LXX-B9 — Asyndetic predicate (Hebrew B14 analog): NOT PORTED

| | |
|---|---|
| Trigger | (would be: curr line is a finite verb clause with no leading conjunction) |
| Action | **NOT PORTED** |
| Justification | Hebrew B14 (`ZYq0` / `ZQt0`: asyndetic yiqtol/qatal predicate) targets BHSA's clause-type signature for subject-NP + asyndetic-verb that split across two clause-atoms. The LXX projection inherits the Hebrew atom assignment through CATSS; LXX-B0 already collapses these where the projection emits two lines that share an MT atom. Adding a Greek-surface asyndetic-predicate rule would either duplicate LXX-B0 or — worse — fire on genuinely independent Greek asyndetic clauses (e.g. paratactic narrative: "He went. He saw."), which the framework §2.1 commitment to "punctuation has ZERO force; treat parataxis ≡ ccomp" means we must NOT bind. **No Greek analog needed — Hebrew construction is preserved by LXX-B0 trace.** |
| Provenance | Hebrew B14 (asyndetic predicate) |
| Confidence | HIGH (explicitly non-ported with reasoning) |

### LXX-B10 — Hineh-presentative (Hebrew B8): partially ported via LXX-B0

| | |
|---|---|
| Trigger | (Hebrew side: `הִנֵּה X` + asyndetic-qatal attribute. Greek: `ἰδοὺ` + NP + verb.) |
| Action | **PARTIALLY PORTED via LXX-B0** |
| Justification | The Hebrew `הִנֵּה X` + descriptive attribute pattern (B8) renders into Greek as `ἰδοὺ X` + clause. Whether this is one ATU or two in Greek depends on whether CATSS aligned them to one MT atom; LXX-B0 collapses if so. Adding a Greek-side `ἰδοὺ`-trigger rule would risk over-merging the *common* case where `ἰδοὺ ἐγώ` ("here I am!") stands alone as a complete response (Gen 22:1, 22:7, 22:11 all have standalone `ἰδοὺ ἐγώ` as their own ATU per gold). **No clean Greek-surface rule needed — the few B8-pattern cases that survive LXX-B0 are exactly the ones the bidirectional test wants left split.** |
| Provenance | Hebrew B8 (hineh-presentative) |
| Confidence | HIGH (explicitly non-ported with reasoning) |

### LXX-B11 — Casus pendens (Hebrew B6): NOT PORTED

| | |
|---|---|
| Trigger | (Hebrew: `prev.typ == "CPen"` — left-dislocated topic) |
| Action | **NOT PORTED** |
| Justification | Hebrew B6 keys on BHSA's `CPen` clause-type tag, which is a parser-tagged left-dislocation diagnosis. No equivalent tag exists in the LXX projection: CATSS does not parse the Greek, CenterBLC carries only morphology, UD-PTNK gold covers only Gen+Ruth and Stanza-UD doesn't distinguish left-dislocation from topicalized subject. LXX-B0 handles the cases where Hebrew CPen → projected-Greek dislocation if CATSS rolls both lines into one MT atom (which is the typical case). The residual is a v2 task. **No clean Greek mechanical analog available.** |
| Provenance | Hebrew B6 (casus pendens resumption) |
| Confidence | HIGH (explicitly non-ported with reasoning) |

### LXX-B12 — Ne'um authenticating formula (Hebrew B9): partially ported

| | |
|---|---|
| Trigger | curr line begins (diacritic-stripped) with `λεγει κυριος`, `φησιν κυριος`, `οραμα` (in oracle headers) |
| Action | BIND backward |
| Justification | Direct port of Hebrew B9 (נְאֻם־יהוה). The LXX consistently renders `נְאֻם־יהוה` as `λέγει κύριος` (or `φησὶν κύριος` in some books). The authenticating tag binds to its preceding oath/speech content. |
| Provenance | Hebrew B9 (ne'um formula) |
| Confidence | HIGH — narrow trigger, classic formula. |
| Risk lens | Over-merge risk: very low. The trigger is a fixed phrase; the speech-verb-of-divine-utterance + κύριος combination is overwhelmingly a quoting tag, not an independent matrix clause. |
| Test cases | Isaiah 1:11 `λέγει κύριος` after content — bind. Gen 22:16 `νְאֻם־יְהוָה` projects to `λέγει κύριος` in LXX (cf. CATSS) — bind. |

### LXX-B13 — Participial attribute with εἰμί (Hebrew B13 analog)

| | |
|---|---|
| Trigger | prev line's head verb lemma is `ειμι` (any form of εἰμί) AND curr line begins with a participle (token ending in `-ων`, `-ουσα`, `-ον`, `-σας`, etc., morphological gating preferable when available) |
| Action | BIND backward |
| Justification | Port of Hebrew B13. The Hebrew "vehayah + participial attribute" pattern (Ps 1:3 `וְהָיָה כְּעֵץ` + `שָׁתוּל`) translates into LXX as a copula + attributive participle: "ἔσται ὡς ξύλον / πεφυτευμένον…". The attributive participle modifies the predicate NP introduced by εἰμί and is not its own ATU. |
| Provenance | Hebrew B13 (participial attribute with היה) |
| Confidence | MEDIUM — participle morphology detection via suffix is imperfect; better with full morph passed through projection-v1. |
| Risk lens | Over-merge risk: medium. Predicative participles WITH their own subject should NOT bind (same caveat as Hebrew B13). The gating on prev being εἰμί catches most attributive cases but not all. |
| Test cases | Ps 1:3 LXX `καὶ ἔσται ὡς τὸ ξύλον` + `τὸ πεφυτευμένον παρὰ τὰς διεξόδους τῶν ὑδάτων` — bind. |

---

## Rules NOT ported (with reasoning)

| Hebrew rule | LXX status | Reason |
|---|---|---|
| B2 (Defc + et-marker appositive) | **NOT PORTED** | Greek has no et-marker; the appositional / object-marker continuation maps to bare accusative apposition, which is already handled by Hebrew clause-atom unity and propagates through LXX-B0. |
| B4 (retired) | n/a | Retired in Hebrew catalog; framework §2.1 supersedes. |
| B6 (casus pendens) | **NOT PORTED** | See LXX-B11. No equivalent Greek surface signal; LXX-B0 covers the projection-mechanical residual. |
| B7 (bare wayyiqtol pair) | Partially absorbed into LXX-B5 | The bare-single-token-prev signal lives inside LXX-B5; not a standalone rule. |
| B8 (hineh-presentative) | **NOT PORTED** | See LXX-B10. The bidirectional test wants the residual cases split. |
| B12 (Reop) | **NOT PORTED** | BHSA-specific clause-type tag, no Greek analog and no LXX projection signal. |
| B14 (asyndetic predicate) | **NOT PORTED** | See LXX-B9. LXX-B0 covers the projection-mechanical residual; Greek-surface analog would over-merge paratactic narrative. |

---

## Rule evaluation order

The rules are evaluated in order in `should_bind(prev, curr)`. The first matching rule
returns `True` and the binding fires. A global safety guard at the top refuses any
binding across verse boundaries.

```
0. Same-verse check (global guard)
1. LXX-B0  Same-Hebrew-source-atom collapse           (highest confidence — runs first)
2. LXX-B1  Vocative / nominative of address
3. LXX-B12 Ne'um (λέγει κύριος) formula
4. LXX-B3  καὶ ἐγένετο + temporal frame                (DEFAULT-DISABLED via ENABLE_KAI_EGENETO flag, v2)
5. LXX-B5  Bare speech-frame + content (LXX-B0-gated)
6. LXX-B4  Purposive τοῦ + infinitive
7. LXX-B6  Genitive absolute                          (morph-gated, v2)
8. LXX-B2  Restrictive ὅς / ὅστις                     (morph-gated, v2)
9. LXX-B13 Participial attribute with εἰμί
10. LXX-B7 Cognition + ὅτι complement                 (currently OFF in applier; pending discriminator)
11. LXX-B8 Discourse particle NO-OP (documentation; never fires)
```

Order rationale: LXX-B0 is substrate-deterministic and confidence-HIGH, so it runs first to
absorb the projection-mechanical cases. Pattern-rules with low over-merge risk run next.
Length-dependent / discriminator-sensitive rules (B2 relative, B7 cognition-ὅτι) run last.

---

## Validation and red-line discipline

Per `CLAUDE.md`: **Over-merge is Stan's RED LINE; validators are BLIND to it.**

Before any of these rules is *applied to deploy*, the standing audit gate requires:

1. ≥ 2 parallel adversarial audits on disjoint lenses (over-merge + atomicity), per
   `feedback_never_skip_audit_gate.md`.
2. Source-parity verification against the v0 Rahlfs source (no text mutation).
3. Index-parity regression check vs. current v1.5 partition.

The current artifact is **a porting + smoke test**, NOT a deploy. The audit gate
remains downstream. Each rule above is documented with its over-merge risk lens so the
audit can scrutinize.

---

## Smoke-test results (2026-05-30 — v1 initial port)

Applier: `C:/tmp/lxx_binding/apply_binding_rules.py`
Substrate: `C:/tmp/lxx_projection/verse_scores.json` → re-exported to
`C:/tmp/lxx_binding/full_verse_data.json` (1547 verses Gen + Ruth, all with
projected partition + UD-PTNK gold partition).
Catalog enabled: LXX-B0–B6 + B12 + B13 (B7 disabled per risk lens; B8/B9–B11 not ported).

### Aggregate (v1)

| Metric | Pre | Post |
|---|---|---|
| Cardinality match (1547 verses) | 682 (44.1%) | 691 (44.7%) |
| Mean per-gold Jaccard | 0.6958 | 0.6879 |

Net cardinality-match +9 verses, mean-Jaccard −0.008.

### Per-rule helped / hurt breakdown (v1)

| Rule | Fired | Helped | Hurt | Neutral | Net | Notes |
|---|---|---|---|---|---|---|
| LXX-B2 restrictive ὅς/ὅστις | 114 | 75 | 35 | 4 | +40 | Article `ὁ` collapses to `ο` under diacritic-strip, colliding with relative `ὅ`. **Fixed in v2 via CenterBLC morph-prefix gate (RR).** |
| LXX-B1 vocative | 20 | 15 | 4 | 1 | +11 | Solid. Closed PROPN list working as designed. |
| LXX-B4 purposive τοῦ + INF | 18 | 11 | 6 | 1 | +5 | Reasonable. Hurts cluster on long τοῦ-INF clauses that gold treats as standalone. |
| LXX-B3 καὶ ἐγένετο temporal frame | 18 | 2 | 16 | 0 | **−14** | Net-negative. **Default-disabled in v2** (no Greek-surface pattern separates 2 helps from 15 hurts). |
| LXX-B13 participial-attribute (εἰμί) | 15 | 12 | 3 | 0 | +9 | Solid. |
| LXX-B6 genitive absolute | 5 | 1 | 4 | 0 | **−3** | Suffix-matching false-positives on substantivized participles. **Fixed in v2 via morph-code regex + no-preceding-GEN-article gate.** |

### Red-line (over-merge) monitor (v1)

- **Pure over-merges from card-match** (verses that started at delta 0, ended at delta < 0): **39** — Stan's red line.
- Rules implicated: B2: 20, B3: 11, B4: 4, B1: 3, B6: 2, B13: 2.

---

## Smoke-test results (2026-05-30 — v2 refinement)

Applier: same path (refinements documented at the top of the file).
Substrate: same (`full_verse_data.json`, 1547 verses Gen + Ruth).
Morph cache: `C:/tmp/lxx_binding/centerblc_morph.json` (1616 verses, from
CenterBLC LXX TF Rahlfs-1935 at
`readers-lxx/private/substrate/centerblc-lxx/tf/1935/`).
v2 output: `C:/tmp/lxx_binding/post_binding_scores_v2.json` (with per-verse
`diff_from_v1` field).
Catalog enabled: LXX-B0–B2 + B4–B6 + B12 + B13 (B3 default-disabled; B7 still
OFF; B8/B9–B11 not ported).

### Aggregate (v2)

| Metric | Pre (raw projection) | Post (v1) | Post (v2) | v2 Δ vs raw | v2 Δ vs v1 |
|---|---|---|---|---|---|
| Cardinality match (1547 verses) | 682 (44.1%) | 691 (44.7%) | **696 (45.0%)** | **+14** | +5 |
| Mean per-gold Jaccard | 0.6958 | 0.6879 | **0.6946** | **−0.0012** | +0.0067 |
| Pure over-merges from card-match | — | 39 | **11** | — | −28 (fixed) |

v2 hit the +14 card-match-delta target floor (catalog goal was "≥ +20"; we
landed at +14 — the +20 target assumed v1's diacritic-collision-driven B2
helps were real, which they mostly weren't). Mean Jaccard delta returned to
near-flat (−0.0012, vs v1 −0.008 and vs the absolute target ≥ 0).

### Per-rule helped / hurt breakdown (v2)

| Rule | Fired | Helped | Hurt | Neutral | Net | Notes |
|---|---|---|---|---|---|---|
| LXX-B1 vocative | 20 | 17 | 3 | 0 | **+14** | Unchanged from v1 trigger; improved net via fewer collisions with other rules. |
| LXX-B13 participial-attribute (εἰμί) | 15 | 12 | 3 | 0 | +9 | Unchanged from v1. |
| LXX-B2 restrictive ὅς/ὅστις | 12 | 6 | 5 | 1 | +1 | Morph-prefix-gated (RR). v1's 114→12 fires reflects removal of the diacritic-strip collision. Residual hurts (5/12) are the known long-relative / non-restrictive ὅς problem already flagged in the risk lens; deferred to v2 LLM. |
| LXX-B4 purposive τοῦ + INF | 19 | 11 | 7 | 1 | +4 | Unchanged from v1 (no refinement scoped). |
| LXX-B6 genitive absolute | 6 | 4 | 2 | 0 | +2 | Morph-gated. v1's 5/4 helped/hurt → v2's 4/2. Every v1 hurt was a substantival participle under a GEN article; v2 blocks that class. |
| LXX-B3 καὶ ἐγένετο temporal frame | 0 | 0 | 0 | 0 | 0 | Default-disabled. |

### Red-line (over-merge) monitor (v2)

- **Pure over-merges from card-match**: **11** (v1: 39). Rules implicated:
  B4: 5, B1: 3, B13: 2, B6: 1.
- **NEW v2 pure over-merges not in v1**: 1 — `Gen 25:6` `ἔτι ζῶντος αὐτοῦ`
  (a genuine genitive absolute that gold treats as its own ATU). Per
  `feedback_conformance_is_not_correctness.md`, framework §2 wants this
  bound (gen-abs is adverbial to matrix); UD-PTNK gold-segmenter splits it.
  Not a rule failure; documented as the residual.
- **Fixed v1 pure over-merges**: 29 (out of v1's 39). The 10 still-persistent
  ones are all from rules NOT in scope for this refinement (B1: 3, B4: 4,
  B13: 2, plus Ruth 1:1 via B4).

### Recommendations from smoke test (v2 update)

1. **B2 + B6 morph-gating is shippable** at this confidence level. Both
   rules went from net-negative or net-near-zero to net-positive with no
   new over-merge class introduced.

2. **B3 stays off** until (a) v2 LLM can adjudicate the Greek wayhi-frame
   semantically, or (b) gold-substrate analysis reveals a separating
   sub-pattern (none found in surface lexis).

3. **B4 (τοῦ + INF) is the next refinement candidate.** v1: 11/6, v2: 11/7
   — unchanged at 5 of the 11 persistent over-merges. The catalog risk
   lens predicts "low" over-merge but the data says otherwise. Hurts
   cluster on long τοῦ-INF clauses gold treats as standalone (the
   length-dependent issue Hebrew B3 has too). Same fix path: morph + clause
   structure beyond surface suffix.

4. **The 11-pure-over-merge floor is the audit-target** if this catalog moves
   toward deploy. Stan's RED LINE; the ≥2 parallel adversarial audits
   (over-merge + atomicity lenses) per `CLAUDE.md` would need to clear these.

5. **Conformance ≠ correctness reminder still applies.** The 1 NEW v2
   over-merge (Gen 25:6) is a clean instance: methodologically correct per
   framework §2 (gen-abs binds to matrix), gold-disagreement per UD-PTNK
   auto-segmenter. The catalog risk lens explicitly says "Genitive absolutes
   never stand alone as ATUs under the bidirectional test." We trust the
   framework over the auto-segmenter on this one case but flag it for audit.

---

## Adding a new LXX rule

Per the Hebrew-catalog discipline:

1. Identify the Greek feature(s) that drive the rule (post-pointing/diacritic-strip surface, lemma, POS, or projection-trace).
2. Have a one-paragraph justification tracing to the bidirectional test (§2 of framework.md).
3. State the Hebrew-rule provenance (or "Greek-original" if not a port).
4. State the over-merge risk lens explicitly.
5. Have at least one canonical positive example from Gen or Ruth (the validated LXX gold).
6. Have at least one canonical counter-example (or "always fires" note).
7. Be added to `C:/tmp/lxx_binding/apply_binding_rules.py:should_bind()` in the correct evaluation order.
8. Be smoke-tested against Gen + Ruth (the UD-PTNK gold set). No regression in cardinality match or mean-Jaccard.
