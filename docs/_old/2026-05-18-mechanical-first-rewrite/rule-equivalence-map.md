# Constraint Equivalence + Non-Equivalence Map

This map identifies which per-corpus constraints across the BoFM, GNT, and Tanakh canons are doing the same underlying work (and can be reasoned about as a family), and which constraints have no analog in sibling corpora (corpus-unique constraints — the load-bearing non-correspondences that must not be force-ported). It is intended for cross-corpus audit work, LXX/Vulgate porting decisions, and framework maintenance. It is NOT a constraint catalog — each canon already contains that. Focus here is on clusters and non-correspondences.

Constraint IDs follow each canon's own prefix convention. Universal items (bidirectional test, restrictive-relative binding) are listed separately at the bottom; they are not per-corpus constraints and do not appear in the equivalence families.

---

## Cross-corpus constraint families (equivalences)

| Family / underlying purpose | BoFM | GNT | Tanakh | Notes |
|---|---|---|---|---|
| **Complement integrity** (matrix verb + obligatory clausal complement stay together) | R17 (six verb classes: causative, aspectual, speech-indirect, cognition, volition, FEF-extraposition; *that/whether/if/WH/inf*) | R10 (cognition/perception/belief verbs + ὅτι merge; declaration/speech verbs + ὅτι split) | H7 (cognition, volition, causative, aspectual, verbless-copular classes; `כִּי/אֲשֶׁר` clauses) | All three encode the universal complement-valence question: "is this matrix verb's obligatory complement on the same line?" Key difference: GNT R10 is the one place where the same underlying principle produces a SPLIT-CANDIDATE (declaration verbs + ὅτι) rather than a BIND — because the declaration act is propositionally complete. BoFM and Tanakh handle this via the direct-discourse exclusion inside R17 / H7. |
| **Adjective/predicate + complement integrity** | R26 (ADJ head + *that*-complement stays together; distinct from R17 which is VERB head only) | (absorbed into R10 — no separate constraint for adj-headed complements) | H7 / H18 covers participial predicates | BoFM is the only corpus with an explicit adj-head complement constraint because Early Modern English frequently surfaces this pattern; GNT and Hebrew handle it through the general complement-integrity question. |
| **Formula integrity** (lexicalized multi-word frame is one unit) | R1 (AICTP — *And it came to pass* + closed variants); R18 (fixed idioms); R18a (Patriarch-Deity-Triad) | R6 (fixed phrases); R18a-GNT (Patriarch-Deity-Triad); Amen-formula speech-intro | H1 (maqqef-group indivisibility); H16 (wayehi protasis as FEF formula); SOLEMNITY_PREFIXES in H5 (`כֹּה אָמַר יְהוָה`, `נְאֻם־יְהוָה`) | All three encode the formula-integrity question. Key non-equivalence: R1 AICTP is an English-register construction unique to BoFM literary style; H16 wayehi is its closest structural analog (FEF pattern, temporal-frame + main-clause) but operates in Hebrew narrative morphology with wayyiqtol. GNT has `καὶ ἐγένετο` in Luke/Acts as the Septuagintal parallel but it is not given a named constraint in the GNT canon. |
| **Speech-act announcement** (speech-intro frame ≠ quoted content) | R28; R17 exclusion #1 (direct discourse excluded from complement-merge) | R11 / R28-ext (speech-intro verb gets own line; speech content follows; Amen-formula and OT-attribution-tag sub-cases) | H5 / H5b (speech-act announcement default: finite speech-act verb + content are separate ATUs regardless of frame length; `לֵאמֹר` complementizer marks speech-onset) | Universal speech-frame question instantiated across all three corpora. Key calibration: speech-intro + short particle-led reply (e.g., Hebrew `הִנֵּנִי`, English "behold here am I") binds as one ATU per the discourse-particle-binding extension. |
| **Vocative integrity** (vocative unit is indivisible) | R15 | R7; R18 (three-way refined treatment with repeated-vocative and compound-divine-name sub-cases) | H4 (Hebrew lacks morphological vocative case; address-position NP with 2p verbal morphology); repeated-vocative pairs stay together | All three treat vocatives as atomic units. Hebrew H4 is more elaborate because Hebrew signals vocative contextually, not morphologically. |
| **Divine-title appositives** | R18a (Patriarch-Deity-Triad: KEEP-WHOLE regardless of internal coordination) | R18a-GNT (4 surface variants, all BIND) | H9 (INTRODUCING vs REFERENCING: introducing appositives earn a stack-split on formal anchor; referencing appositives bind as one name unit) | GNT and BoFM agree on BIND. Tanakh is structurally richer because Hebrew has a richer divine-title appositive system with first-occurrence revelatory contexts that earn their own ATU. |
| **Never end a line on a conjunction / particle seeking its content** | R9 (never end on CCONJ) | R2 (never dangle conjunction) | H14 (discourse particles lead their content; H3 vav-consecutive own-line policy implicitly covers this for wayyiqtol) | Universal forward-closure violation. GNT adds discourse-direction nuance for γάρ (supports-backward vs introduces-forward) but the closure question is identical. |
| **Never end a line on a determiner / article** | R11 | R3 | H1 / maqqef implicitly; no separate constraint (Hebrew article is a prefix clitic, not a separate token) | GNT and BoFM share this. Hebrew doesn't need a separate constraint because the definite article `הַ` is prefixed to its noun — the maqqef-group covers orthographic joining. |
| **Never split auxiliary from main verb** | R12 | R5 (never split periphrastic: εἰμί + participle) | H18.2 (participial predicate integrity: `הָיָה` + predicate participle stays together; verbless predicate analog) | BoFM and GNT handle English/Greek periphrastic constructions. Hebrew H18 covers the structural analog (subject + participial predicate as one verbless-clause unit). |
| **Never split preposition from its object** | R13a | R2 (covers via conjunction; ADP-seeking-object table) | H1 / H2 (maqqef-group and construct-chain integrity cover this for Hebrew bound structures) | Same underlying question; different orthographic realizations. Hebrew maqqef-group + construct chain effectively prohibit this split at the orthographic level. |
| **Cross-verse continuity** (atomic thought spanning verse boundary stays intact) | R14 (handled by framework) | §3.17 cross-verse-continuity-merge | H10 (explicit constraint: sense-line stays in earlier verse's block; superscript verse-marker for MT boundary crossing) | All three canons handle this; Tanakh's H10 is the most elaborated. |
| **No-anchor constraint** (every line must carry an atomic-thought anchor) | R20 | R1 (core mechanical constraint) | §5.0 No-Anchor Test | Functionally identical across all three corpora; the implementation emphasis differs. |
| **Parallel-list uniformity** (uniform treatment of list members) | (framework applies) | R12 / R28 (editorial constraint; authorial asymmetry) | H17 (Genealogy / List-Formula Handling — most explicit) | Same underlying question. Tanakh H17 is the most operationally explicit because Hebrew genealogical formula is highly stereotyped. |
| **Restrictive relative clause binding** | R19-cataphoric / R19-anaphoric (restrictive *that*-clauses bind to head noun) | R-restrictive-relative (restrictive ὅς / ὅστις / ὅπου bind to head noun) | H-restrictive-relative (restrictive `אֲשֶׁר` binds to head noun) | Universal restrictive-relative binding. The diagnostic ("would removing the relative leave the head uniquely identified?") is corpus-agnostic. |
| **Gapped-verb tolerance in parallel cola** | (rare in BoFM; handled editorially) | (rare in GNT poetry; handled editorially) | H-gapped-verb (a colon whose finite verb is gapped from the immediately preceding parallel colon counts as forward-closed if recoverable) | Hebrew-specific frequency due to dense parallelism in poetic books; the underlying principle (recoverable gapped verb satisfies forward closure) is universal. |

---

## Corpus-unique constraints (no cross-corpus analog)

### BoFM-unique

- **R1 — AICTP formula integrity** — The *And it came to pass* surface string is a register-specific feature of Early Modern English scripture style. GNT has no such fixed English-register formula. Tanakh has the structural analog (H16 wayehi protasis), but H16 fires on Hebrew morphology, not a fixed English surface string.
- **R5 — Equivalence "or" as appositive** — The *or* = *that is to say* substitution pattern is a stylistic tic of BoFM literary register. No GNT or Tanakh analog constraint exists.
- **R16 — Dangling "that" after AICTP** — Purely BoFM-specific: the trailing *that* is an artifact of the English subordinating-complementizer pattern unique to AICTP.
- **R23 — Date colophon integrity** — BoFM's year-formula (*in the Xth year of the reign of the judges*) is a corpus-specific colophon pattern.
- **R27 — "Insomuch that" binding** — *Insomuch that* is an EME result-clause marker specific to the BoFM register. GNT R25 (ὥστε consecutive-result binding) is the closest analog, but they are independent closed-list items.
- **R29 — Bare infinitival orphan integrity** — Bare infinitival orphans (*to X*) at line-start without a governing verb on the same line. EME register feature.

### GNT-unique

- **R19 (GNT) — Genitive absolute always own line** — Greek genitive absolutes are a Greek syntactic feature with no Hebrew or English analog. An LXX constraint would inherit R19 directly because LXX is Greek; do not port to Hebrew-translation contexts.
- **R10 — ὅτι complementizer split by verb class** — The cognition-vs-declaration split on ὅτι is GNT-specific because it depends on Greek indirect-discourse syntax. Hebrew handles this through the `כִּי`-clause taxonomy in H7, but the mechanism differs.
- **R25 — ὥστε short-consecutive-result binding** — ὥστε as a result-clause marker is Greek-specific. BoFM R27 (*insomuch that*) is the register-level cousin but not equivalent for force-port purposes.
- **R23 (GNT) — Dative subject of infinitive** — Greek dative-subject-of-infinitive construction has no Hebrew or English structural analog. Koine Greek syntax feature (BDF §393–400).
- **Marked-coordinator climactic emphasis** — The `ἔτι τε καί / μάλιστα δέ / μᾶλλον δέ / οὐ μόνον...ἀλλὰ καί` climactic-addition family is Greek-specific.
- **OT-attribution tags inside quotation blocks** — `λέγει τὸ πνεῦμα ταῖς ἐκκλησίαις` and Pauline `λέγει κύριος` mid-citation tags are GNT-specific phenomena arising from NT authors quoting the LXX.
- **R20 (GNT) — Participial phrase test** — Greek's rich participial system (attributive, circumstantial, genitive absolute, periphrastic) produces participial-phrase editorial decisions that are GNT-specific. Hebrew H18.2 covers participial predicates, but the Hebrew participle is a different grammatical beast.
- **Continuative-vs-restrictive `ἐν ᾧ` distinction** — Pauline epistolary `ἐν ᾧ`-clauses can be continuative (descriptive, may stand alone) or restrictive (binding); the distinction is interpretive and Pauline-corpus-specific.

### Tanakh-unique

- **H1 — Maqqef-group indivisibility** — The maqqef (־) is a Hebrew orthographic feature joining tokens into prosodic words. No English or Greek analog. LXX does not preserve maqqef-group behavior.
- **H2 — Construct chain default** — The Hebrew bound *nomen regens + nomen rectum* construct-state chain is a Hebrew morphosyntactic feature. Greek expresses genitive relationships via case marking on independent tokens; English uses *of*-phrases.
- **H3 — Vav-consecutive clause-head policy** — Hebrew *wayyiqtol* (vav-consecutive imperfect) is the dominant narrative-prose clause-head marker. Neither BoFM nor GNT has a construction doing the same morphological work.
- **H6 — Ketiv/Qere policy** — The Masoretic Ketiv/Qere apparatus is unique to the Hebrew Bible tradition.
- **H12 — Petucha/setuma rendering** — The paragraph-marker system (פ / ס in TAHOT) is a Masoretic textual-tradition feature.
- **H13 — Special letters** — Suspended letters, inverted nuns, large/small letters are Masoretic graphical anomalies. Entirely corpus-unique.
- **H14 — Discourse particles** (`הִנֵּה, אָז, עַתָּה, לָכֵן, עַל־כֵּן`) — Underlying principle (discourse particle leads its content, never trails the prior line) maps to GNT R8 framing devices and BoFM R8 framing devices, but the specific Hebrew particle inventory is typologically distinct.
- **H15 — Casus pendens / left-dislocation** — Hebrew topic-fronting + resumptive-pronoun is a major Hebrew narrative device (Joüon-Muraoka §156). The pattern is more systematic and more frequent in the Hebrew corpus.
- **H16 — FEF wayehi protasis** — Closest structural analog to BoFM R1 (AICTP) and GNT's `καὶ ἐγένετο` periodic-frame treatment, but H16 fires on Hebrew morphology not a surface string. The FEF-family principle is universal; the instantiation is corpus-specific.
- **H18 — Clause-nucleus integrity for verbless clauses** — Hebrew verbless clauses (no overt copula in present-tense nominal/participial predications) are typologically unique to Hebrew. English and Greek always have a copula or finite verb.

---

## Universal items (atu-method framework, not per-corpus)

These live in `framework.md` and are NOT re-instantiated per corpus. Per-corpus canons reference them by ID.

- **Bidirectional test** (§1.2) — Forward grammatical closure + backward referential self-containment. The criterion for ATU well-formedness. Asymmetric: anaphoric failure breaks the test; cataphoric introduction does not.
- **Restrictive relative clause binding** (§1.3) — Restrictive relatives bind to head noun regardless of internal completeness; universal across Hebrew `אֲשֶׁר` / Greek `ὅς` / EME English "which" / "who" / "that".
- **Minimal rubric** — The LLM identification stage's operational rubric: bidirectional test + restrictive-relative binding + small set of language-specific syntactic constraints + default KEEP-AS-IS. Excludes cognitive-unity gates, parallelism class adjudication, and genre anchors as primary licenses.
- **Three-stage pipeline** — LLM identification → constraint catalog audit → editorial review. Corpus-agnostic.
- **Coarse-anchor principle** — Mechanical anchor should be the coarsest reliable signal (typically versification); finer signals are informational, not adjudicative.

---

## Implications for LXX/Vulgate

### Constraints likely to port directly (from cross-corpus families above)

- Complement integrity family — port the family, re-instantiate the verb-class closed list from the target language
- Speech-act announcement — port the universal frame question; calibration for short-particle-led replies needs per-corpus testing
- Formula integrity — port the *principle*, but the specific formulas (AICTP, `καὶ ἐγένετο`, wayehi) must be re-identified in LXX Greek; LXX will have its own FEF patterns from translating Hebrew narrative
- Vocative integrity — port; Greek vocative case is morphologically explicit in LXX, making this cleaner than Hebrew
- No-anchor constraint — port universally; this is the operational form of the bidirectional test
- Cross-verse continuity — port; LXX versification is a separate overlay
- Restrictive-relative binding — port directly (universal); LXX uses Greek `ὅς` / `ὅστις` as in GNT
- Gapped-verb tolerance — port to LXX poetic books where Hebrew gapped-verb parallelism is translated; the principle is universal but Greek frequency is lower than Hebrew

### Constraints likely to need LXX/Vulgate-specific re-instantiation

- R10 (GNT) ὅτι cognition-vs-declaration split — LXX uses ὅτι in the same way; verb-class closed list needs review against LXX register (LXX sometimes translates Hebrew speech verbs as Greek cognition-class verbs and vice versa)
- R19 (GNT) genitive absolute own-line — LXX has genitive absolutes; the constraint ports, but LXX frequency differs from NT
- H16 FEF wayehi → `καὶ ἐγένετο` — LXX renders wayehi as `καὶ ἐγένετο`; a LXX FEF constraint would be a hybrid of H16 (Hebrew morphological trigger) and GNT's periodic-frame treatment; instantiate from scratch using LXX data
- Discourse particles (H14 → GNT R8 family) — LXX translates Hebrew discourse particles sometimes mechanically (`הִנֵּה` → `ἰδού`); the LXX closed list will largely match GNT R8 with additions from the translation-Hebrew substrate

### Constraints NOT to force-port (typologically inappropriate)

- **H1 Maqqef-group indivisibility** — LXX is Greek; no maqqef apparatus
- **H2 Construct chain default** — LXX uses Greek genitives; evaluate as genitive-phrase integrity, not construct-chain
- **H3 Vav-consecutive own-line policy** — LXX renders *wayyiqtol* chains as aorist+καί or aorist+δέ; these are not *wayyiqtol* and do not inherit H3's morphological trigger
- **H6 Ketiv/Qere policy** — no Ketiv/Qere in LXX
- **H12 Petucha/setuma rendering** — LXX MSS have their own paragraph markers; not equivalent
- **H18 Verbless-clause nucleus integrity** — LXX has εἰμί copula; the Hebrew verbless-clause failure mode does not exist in LXX Greek
- **R1 AICTP** — English-register formula; irrelevant for Greek LXX or Latin Vulgate
- **R5 Equivalence "or" as appositive** — EME BoFM register feature; not present in LXX/Vulgate
- **R23 (GNT) Dative subject of infinitive** — LXX shares this Greek feature; DOES port to LXX but NOT to Vulgate Latin
