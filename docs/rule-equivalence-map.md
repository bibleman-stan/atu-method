# Rule Equivalence + Non-Equivalence Map

This map identifies which per-corpus rules across the BoFM, GNT, and Tanakh canons are doing the same underlying work (and can be reasoned about as a family), and which rules have no analog in sibling corpora (corpus-unique rules — the load-bearing non-correspondences that must not be force-ported). It is intended for cross-corpus audit work, LXX/Vulgate porting decisions, and framework maintenance. It is NOT a rule catalog — each canon already contains that. Focus here is on clusters and non-correspondences.

Rule IDs follow each canon's own prefix convention (BoFM: R-numbers; GNT: R-numbers in a different namespace; Tanakh: H-numbers). The framework's universal items (J1–J5, M1–M4, §1.1 bidirectional test) are listed separately at the bottom; they are not per-corpus rules and do not appear in the equivalence families.

---

## Cross-corpus rule families (equivalences)

| Family / underlying purpose | BoFM | GNT | Tanakh | Notes |
|---|---|---|---|---|
| **Complement integrity** (matrix verb + obligatory clausal complement stay together) | R17 (six verb classes: causative, aspectual, speech-indirect, cognition, volition, FEF-extraposition; *that/whether/if/WH/inf*) | R10 (cognition/perception/belief verbs + ὅτι merge; declaration/speech verbs + ὅτι split — GNT is the only canon that splits complement integrity by complementizer class) | H7 (cognition, volition, causative, aspectual, verbless-copular classes; *כִּי/אֲשֶׁר* clauses) | All three instantiate framework M2. Key difference: GNT R10 is the one place where the same underlying principle produces a SPLIT (declaration verbs + ὅτι) rather than a merge — because the declaration act is propositionally complete. BoFM and Tanakh handle this via the direct-discourse exclusion inside R17 / H7 respectively, not by splitting the rule. |
| **Adjective/predicate + complement integrity** | R26 (ADJ head + *that*-complement stays together; distinct from R17 which is VERB head only) | (absorbed into R10 / M2 — no separate rule for adj-headed complements) | H7 / H18 covers participial predicates (H18.2) | BoFM is the only corpus with an explicit adj-head complement rule (R26) because Early Modern English frequently surfaces this pattern; GNT and Hebrew handle it through the general complement-integrity principle. |
| **Formula integrity** (lexicalized multi-word frame is one unit) | R1 (AICTP — *And it came to pass* + closed variants); R18 (fixed idioms: *put to death*, *it is expedient that*, etc.); R18a (Patriarch-Deity-Triad) | R6 (fixed phrases — Layer 1); R18a-GNT (Patriarch-Deity-Triad *ὁ θεὸς Ἀβραάμ καὶ Ἰσαάκ καὶ Ἰακώβ*); Amen-formula speech-intro (own-line atomic unit) | H1 (maqqef-group indivisibility — orthographic unit); H16 (wayehi protasis as FEF formula); SOLEMNITY_PREFIXES in H5 (*כֹּה אָמַר יְהוָה*, *נְאֻם־יְהוָה*) | All three instantiate framework §1.2 formula integrity. Key non-equivalence: R1 AICTP is an English-register construction unique to BoFM literary style; H16 wayehi is its closest structural analog (FEF pattern, temporal-frame + main-clause) but operates in Hebrew narrative morphology with wayyiqtol, not a fixed English surface string. GNT has *καὶ ἐγένετο* in Luke/Acts as the Septuagintal parallel but it is not given a named rule in the GNT canon (handled via FEF periodic-frame treatment in §8 and J5 substantive adjunct). |
| **Speech-act announcement** (speech-intro frame ≠ quoted content) | R28 (speech-act announcement after adverbial frame — split is mandatory); R17 exclusion #1 (direct discourse excluded from complement-merge) | R11 / R28-ext (speech-intro verb gets own line; speech content follows; GNT adds Amen-formula and OT-attribution-tag sub-cases) | H5 / H5b (speech-act announcement default: finite speech-act verb + content are separate ATUs regardless of frame length; *לֵאמֹר* complementizer marks speech-onset boundary) | Universal J3 instantiated across all three corpora. Key difference: Tanakh H5 explicitly retired the "short-framing-default" (frames ≤3 prosodic words merging with speech); BoFM and GNT retain some short-frame aggregation exceptions under narrow scope-economy carve-outs. |
| **Vocative integrity** (vocative unit is indivisible) | R15 | R7 (Layer 1); R18 (three-way refined treatment with repeated-vocative and compound-divine-name sub-cases) | H4 (Hebrew lacks morphological vocative case; address-position NP with 2p verbal morphology); repeated-vocative pairs stay together | All three treat vocatives as atomic units. GNT's R18a-GNT (Patriarch-Deity-Triad) is formally a formula-integrity rule but operationally covers the same content as Tanakh's H9 divine-title appositives. Hebrew H4 is more elaborate because Hebrew signals vocative contextually, not morphologically. |
| **Divine-title appositives** | R18a (Patriarch-Deity-Triad: KEEP-WHOLE regardless of internal coordination) | R18a-GNT (same formula: *ὁ θεὸς Ἀβραάμ καὶ θεὸς Ἰσαάκ καὶ θεὸς Ἰακώβ* — 4 surface variants, all KEEP-WHOLE) | H9 (INTRODUCING vs REFERENCING: introducing appositives earn a stack-split on formal anchor; referencing appositives merge as bound name unit) | GNT and BoFM agree on KEEP-WHOLE. Tanakh is structurally richer because Hebrew has a richer divine-title appositive system with first-occurrence revelatory contexts (Gen 14:18 *אֵל עֶלְיוֹן*) that earn their own line. Worth noting: GNT R18a-GNT and BoFM R18a appear to be a direct three-corpus parallel (same OT formula surfacing in all three). |
| **Never end a line on a conjunction / particle seeking its content** | R9 (never end on CCONJ) | R2 (Layer 1 — never dangle conjunction) | H14 (discourse particles lead their content; H3 vav-consecutive own-line policy implicitly covers this for *wayyiqtol*) | Universal Layer 1 pattern across all three. GNT adds discourse-direction nuance for γάρ (supports-backward vs introduces-forward) but the placement rule (never line-final) is identical. |
| **Never end a line on a determiner / article** | R11 | R3 (Layer 1) | H1 / maqqef implicitly; no separate rule (Hebrew article is a prefix clitic, not a separate token) | GNT and BoFM share this as Layer 1. Hebrew doesn't need a separate rule because the definite article *הַ* is prefixed to its noun — the maqqef-group rule (H1) covers orthographic joining where relevant. |
| **Never split auxiliary from main verb** | R12 | R5 (never split periphrastic: εἰμί + participle) | H18.2 (participial predicate integrity: *הָיָה* + predicate participle stays together; verbless predicate analog) | BoFM and GNT handle English/Greek periphrastic constructions. Hebrew H18 covers the structural analog (subject + participial predicate as one verbless-clause unit). |
| **Never split preposition from its object** | R13a | R2 (Layer 1 covers this via conjunction; ADP-seeking-object is in the Layer 1 table) | H1 / H2 (maqqef-group and construct-chain integrity cover this for Hebrew bound structures) | Same underlying principle; different orthographic realizations. Hebrew maqqef-group + construct chain effectively prohibit this split at the orthographic level. |
| **Cross-verse continuity** (atomic thought spanning verse boundary stays intact) | R14 (implied — not found as a named rule in the BoFM §5 list; handled by framework §1.11) | §3.17 cross-verse-continuity-merge | H10 (explicit rule: sense-line stays in earlier verse's block; superscript verse-marker for MT boundary crossing) | All three canons handle this but Tanakh's H10 is the most elaborated (two-direction handling; superscript convention). |
| **No-anchor rule** (every line must carry an atomic-thought anchor) | R20 (named rule) | R1 (core mechanical rule; 860 merges applied corpus-wide) | §5.0 No-Anchor Test (named operational test, not a numbered H-rule) | Functionally identical across all three corpora; the implementation emphasis differs (GNT has the most complete detector; Tanakh names it as an operational test in §5.0). |
| **Parallel-list uniformity** (uniform treatment of list members) | (framework §1.12 applies) | R12 / R28 (editorial rule; authorial asymmetry principle) | H17 (Genealogy / List-Formula Handling — most explicit; triggers Parallel-List Uniformity Principle with Gen 5 / Deut curse-series examples) | Same framework §1.12 principle. Tanakh H17 is the most operationally explicit because Hebrew genealogical formula is highly stereotyped. |

---

## Corpus-unique rules (no cross-corpus analog)

### BoFM-unique

- **R1 — AICTP formula integrity** — The *And it came to pass* surface string is a register-specific feature of Early Modern English scripture style (derived from KJV translation of wayyiqtol / *καὶ ἐγένετο*). GNT has no such fixed English-register formula (GNT operates in Greek). Tanakh has the structural analog (H16 wayehi protasis), but H16 fires on Hebrew morphology (*וַיְהִי* + wayyiqtol clause-head), not on a fixed English surface string. A ported LXX rule would need to identify Greek *καὶ ἐγένετο* as the FEF marker — closer to GNT's FEF periodic-frame treatment than to R1's surface-string model.

- **R5 — Equivalence "or" as appositive** — The *or* = *that is to say* substitution pattern is a stylistic tic of BoFM literary register (Early Modern English reformulation). Greek uses ὅτι / ἤτοι / τουτέστιν for the equivalence-clarification function; Hebrew uses *אוֹ* differently and the specific reformulation pattern is absent. No GNT or Tanakh analog rule exists.

- **R16 — Dangling "that" after AICTP** — Governs break placement at the right edge of the AICTP formula when trailing *that* is present. Purely BoFM-specific: the trailing *that* is an artifact of the English subordinating-complementizer pattern unique to AICTP. GNT/Tanakh have no equivalent (Greek and Hebrew surface their complementizers differently; H5/*לֵאמֹר* is a dedicated speech-onset marker, not a trailing subordinator).

- **R19 — Cataphoric "that" / relative clause treatment** (BoFM R19, distinct from GNT R19) — The BoFM R19 governs content-dependent relative clause break placement (cataphoric *that*-clauses break; anaphoric merge). This is an English-relative-clause behavior pattern specific to the BoFM literary register and its heavy use of restrictive *that*-clauses. GNT and Tanakh have analogous relative-clause rules but they are not similarly numbered and operate through different structural mechanisms (Greek case-marked relative pronouns; Hebrew *אֲשֶׁר*-clauses embedded in construct chains or casus pendens).

- **R23 — Date colophon integrity** — BoFM's year-formula (*in the Xth year of the reign of the judges*) is a corpus-specific colophon pattern. Hebrew has a structurally similar year-formula pattern in Kings/Chronicles/Jeremiah, but Tanakh has not codified it as a named rule (it would fall under H17 list-formula or H16 FEF). GNT has no equivalent.

- **R27 — "Insomuch that" binding** — *Insomuch that* is an EME result-clause marker specific to the BoFM register. GNT R25 (ὥστε consecutive-result binding) is the closest analog, but *insomuch that* and *ὥστε* are independent closed-list items; no mechanical equivalence.

- **R29 — Bare infinitival orphan integrity** — Bare infinitival orphans (*to X*) at line-start without a governing verb on the same line. This is a function of the BoFM's heavy use of purpose-infinitive stacking in EME register. GNT handles infinitivals differently (Greek infinitives are governed by the J5 / M3 framework tools; no dedicated rule). Hebrew infinitive-construct is handled through H7 complement integrity and H5 speech-frame.

### GNT-unique

- **R19 (GNT) — Genitive absolute always own line** — Greek genitive absolutes (participial phrase with subject in the genitive, grammatically independent of the matrix) are a Greek syntactic feature with no Hebrew or English analog. Hebrew has no genitive absolute construction; BoFM English has no participial absolute with subject-case marking. The closest Tanakh analog is the circumstantial clause or casus pendens (H15), but these operate through different syntax. An LXX rule would inherit R19 directly because the LXX is Greek; do not port to Hebrew-translation contexts.

- **R10 — ὅτι complementizer split by verb class** — The cognition-vs-declaration split on ὅτι is GNT-specific because it depends on Greek indirect-discourse syntax (recitative ὅτι for direct speech; complementizer ὅτι for indirect speech / cognition objects). Hebrew handles this through the *כִּי*-clause taxonomy in H7, but the mechanism differs (Hebrew *כִּי* is multivalent — causal, asseverative, complementizer; the cognition/speech distinction is less deterministic). BoFM handles it through the direct-discourse exclusion inside R17 (colon-terminated direct speech exits complement integrity).

- **R25 — ὥστε short-consecutive-result binding** — ὥστε as a result-clause marker is Greek-specific. BoFM R27 (*insomuch that*) is the register-level cousin but they are not equivalent for force-port purposes. Hebrew equivalent would be *עַל־כֵּן* / *לָכֵן* (H14 discourse particles), which operate under a different rule entirely.

- **R23 (GNT) — Dative subject of infinitive** — Greek dative-subject-of-infinitive construction (articular infinitive with dative subject) has no Hebrew or English structural analog. This is a Koine Greek syntax feature (BDF §393-400). Do not port to BoFM or Tanakh.

- **Marked-coordinator climactic emphasis (J1 fifth signal)** — The *ἔτι τε καί / μάλιστα δέ / μᾶλλον δέ / οὐ μόνον...ἀλλὰ καί* climactic-addition family is Greek-specific (Runge §2 marked-coordinator analysis). BoFM polysyndetic series uses *and* alone with no climactic-emphasis morphosyntax; Hebrew has *אַף* / *גַּם* for additive-emphasis but not the same formal climactic-coordinator system.

- **OT-attribution tags inside quotation blocks (merge)** — The Revelation letter-closing *λέγει τὸ πνεῦμα ταῖς ἐκκλησίαις* pattern and Pauline *λέγει κύριος* mid-citation tags are GNT-specific phenomena arising from NT authors quoting the LXX. No BoFM analog (BoFM has no embedded-OT-quotation apparatus). Tanakh does not have quotation-within-quotation attribution in this form. An LXX rule might need this if LXX has similar mid-passage attribution tags, but the pattern is NT-text-specific.

- **R20 (GNT) — Participial phrase test (refined)** — Greek's rich participial system (attributive, circumstantial, genitive absolute, periphrastic) produces participial-phrase editorial decisions that are GNT-specific. BoFM EME has participials but fewer distinct construction types. Tanakh H18.2 covers participial predicates in Hebrew, but the Hebrew participle is a different grammatical beast (it fills the finite-verb slot in verbless clauses; it does not form genitive absolutes; it does not have the Greek circumstantial-participle's freedom of reference).

### Tanakh-unique

- **H1 — Maqqef-group indivisibility** — The maqqef (־) is a Hebrew orthographic feature joining tokens into prosodic words. No English or Greek analog exists. Do not port. LXX does not preserve maqqef-group behavior (LXX is Greek and does not carry the Masoretic accent apparatus).

- **H2 — Construct chain default** — The Hebrew bound *nomen regens + nomen rectum* construct-state chain is a Hebrew morphosyntactic feature (the regens takes construct-state morphology). Greek expresses genitive relationships via case marking on independent tokens; English uses *of*-phrases or compound nouns. Neither has a construct-chain structural analog that warrants a dedicated merge rule. LXX translates construct chains using Greek genitives — the construct-chain merge behavior must be re-evaluated in Greek terms for LXX (it would become a genitive-phrase integrity question, not a construct-chain question).

- **H3 — Vav-consecutive clause-head policy** — Hebrew *wayyiqtol* (vav-consecutive imperfect) is the dominant narrative-prose clause-head marker, carrying sequential-event morphology. English narrative uses finite verbs without marked sequentiality; Greek uses aorist indicative with various conjunctions. Neither BoFM nor GNT has a construction doing the same morphological work. The closest GNT analog is the narrative aorist + *καί* / *δέ* coordination pattern, but no GNT rule gives it a named default-own-line policy at this level of explicit codification.

- **H6 — Ketiv/Qere policy** — The Masoretic Ketiv/Qere apparatus is unique to the Hebrew Bible tradition (written consonants vs. oral reading tradition). No GNT or BoFM analog. The GNT has textual variants (NA28 apparatus) but these are manuscript variants, not a deliberate preservation of two simultaneous reading traditions. LXX has no Ketiv/Qere; the LXX represents one translation layer above the Hebrew base text.

- **H8 (retired) / H11 (retired) — Te'amim rules** — RETIRED 2026-05-05. Te'amim play no canon role. Noted here only because the rule slots exist; they are empty. No force-port question arises.

- **H12 — Petucha/setuma rendering** — The paragraph-marker system (פ / ס in TAHOT) is a Masoretic textual-tradition feature. No GNT or BoFM analog. LXX manuscripts have their own paragraph markers (ekthesis, paragraphos marks in papyri) but they are not equivalent to the Masoretic petucha/setuma system. Do not port.

- **H13 — Special letters** — Suspended letters, inverted nuns, large/small letters are Masoretic graphical anomalies. Entirely corpus-unique with no analog in GNT or BoFM.

- **H14 — Discourse particles** (*הִנֵּה, אָז, עַתָּה, לָכֵן, עַל־כֵּן*) — While the underlying principle (discourse particle leads its content, never trails the prior line) maps to GNT R8 framing devices (*ἰδού, διό, οὖν, ἀλλά, γάρ, πλήν*) and BoFM R8 framing devices, the specific Hebrew particle inventory is typologically distinct. *הִנֵּה* is deictic-presentative with a complex cataphoric/anaphoric behavior (see §1.1 bidirectional test canonical example); *לָכֵן* / *עַל־כֵּן* are inferential particles without a direct English surface analog. The underlying family clusters with GNT R8 / BoFM R8; the closed list does not port.

- **H15 — Casus pendens / left-dislocation** — Hebrew topic-fronting + resumptive-pronoun (casus pendens) is a major Hebrew narrative device (Joüon-Muraoka §156). While Greek and English have left-dislocation constructions, neither GNT nor BoFM has given them a named rule. Hebrew casus pendens is more systematic and more frequent in the corpus. The LXX sometimes preserves the Hebrew topic-fronting in translation; an LXX rule might need to address this if LXX systematically mirrors the Hebrew pattern.

- **H16 — FEF wayehi protasis** — As noted above: closest structural analog to BoFM R1 (AICTP) and GNT's *καὶ ἐγένετο* periodic-frame treatment, but H16 fires on Hebrew morphology (*וַיְהִי* wayyiqtol + temporal/circumstantial protasis) not a surface string. All three share the FEF-family principle; the instantiation is corpus-specific in each case.

- **H18 — Clause-nucleus integrity for verbless clauses** — Hebrew verbless clauses (no overt copula in present-tense nominal/participial predications) are typologically unique to Hebrew among the three corpora. English and Greek always have a copula or finite verb. BoFM has *is/was* copulae; GNT has εἶναι. The subject+predicate split that H18 prevents is a Hebrew-specific over-fragmentation failure mode arising from the te'amim-derived baseline. Do not port to GNT or BoFM (there is no verbless-clause over-fragmentation problem in those corpora).

---

## Universal items (atu-method framework, not per-corpus)

These live in `framework.md` and are NOT re-instantiated per corpus. Per-corpus canons reference them by ID.

- **J1–J5 structural justifications** — Formally-marked parallel series (J1); Portrait accumulation (J2); Speech-act announcement (J3); Classical commata (J4); Substantive adjunct as own focus (J5). GNT adds a fifth J1 compound-list break signal (marked-coordinator climactic emphasis) that is GNT-specific but operates within the J1 framework slot.
- **M1–M4 merge-overrides** — Gorgianic bonded pair (M1); Verb-object clause-nucleus bond / complement integrity (M2); Bare-governor indivisibility (M3); Fragmented atomic thought-unit (M4).
- **Bidirectional atomic-thought test** (§1.1) — Referential self-containment required in both directions (forward grammatical closure + backward anaphoric resolution). Status as of 2026-05-13: informational diagnostic, NOT a precedence override. Tanakh applied full rigor (detector + 34-verse fixture + corpus scan); GNT applied same rigor and elected to KEEP ALL SPLIT. BoFM has not yet run a dedicated sweep.
- **N=2 Adjudication Principle** (§1.9) and **N=3+ cliff** — Universal tie-breakers for coordinate pairs; apply identically across all three corpora.
- **Parallel-List Uniformity Principle** (§1.12) and **Authorial Asymmetry Principle** (§1.13) — Both universal; per-corpus canons cite them without re-stating.

---

## Implications for LXX/Vulgate

### Rules likely to port directly (from cross-corpus families above)

- Complement integrity family (R17 / R10 / H7 → M2 framework) — port the family, re-instantiate the verb-class closed list from the target language
- Speech-act announcement (R28 / R11 / H5b → J3 framework) — port the split-default; the scope-economy carve-out needs re-evaluation in the target register
- Formula integrity — port the *principle*, but the specific formulas (AICTP, *καὶ ἐγένετο*, wayehi) must be re-identified in LXX Greek; LXX will have its own FEF patterns from translating Hebrew narrative
- Vocative integrity (R15 / R7 / H4) — port; Greek vocative case is morphologically explicit in LXX, making this cleaner than Hebrew
- No-anchor rule (R1-GNT / R20-BoFM / No-Anchor Test-Tanakh) — port universally; this is the operational form of the generative principle
- Cross-verse continuity (H10 / §3.17 / §1.11) — port; LXX versification is a separate overlay from the underlying Greek text

### Rules likely to need LXX/Vulgate-specific re-instantiation

- R10 (GNT) ὅτι cognition-vs-declaration split — LXX uses ὅτι in the same way; verb-class closed list needs review against LXX register (LXX sometimes translates Hebrew speech verbs as Greek cognition-class verbs and vice versa)
- R19 (GNT) genitive absolute own-line — LXX has genitive absolutes; the rule ports, but LXX frequency differs from NT (LXX sometimes over-uses gen-abs as a Hebrew circumstantial-clause calque; the anaphoric-gen-abs bidirectional-test question from GNT §1.1 would resurface)
- H16 FEF wayehi → *καὶ ἐγένετο* — LXX renders wayehi as *καὶ ἐγένετο*; a LXX FEF rule would be a hybrid of H16 (Hebrew morphological trigger) and GNT's periodic-frame treatment; instantiate from scratch using LXX data
- Discourse particles (H14 → GNT R8 family) — LXX translates Hebrew discourse particles sometimes mechanically (*הִנֵּה* → *ἰδού*); the LXX closed list will largely match GNT R8 with additions from the translation-Hebrew substrate

### Rules NOT to force-port (typologically inappropriate)

- **H1 Maqqef-group indivisibility** — LXX is Greek; no maqqef apparatus
- **H2 Construct chain default** — LXX uses Greek genitives; evaluate as genitive-phrase integrity using GNT tools, not Hebrew construct-state tools
- **H3 Vav-consecutive own-line policy** — LXX renders *wayyiqtol* chains as aorist+*καί* or aorist+*δέ*; these are not *wayyiqtol* and do not inherit H3's morphological trigger; evaluate as Greek clause-head policy
- **H6 Ketiv/Qere policy** — no Ketiv/Qere in LXX; the LXX chose one reading
- **H12 Petucha/setuma rendering** — LXX MSS have their own paragraph markers; these are not equivalent
- **H18 Verbless-clause nucleus integrity** — LXX has *εἰμί* copula; the Hebrew verbless-clause over-fragmentation failure mode does not exist in LXX Greek
- **R1 AICTP** — English-register formula; irrelevant for Greek LXX or Latin Vulgate
- **R5 Equivalence "or" as appositive** — EME BoFM register feature; not present in LXX/Vulgate
- **R23 (GNT) Dative subject of infinitive** — LXX shares this Greek feature; the rule DOES port to LXX but NOT to Vulgate Latin (Latin uses different infinitive-subject syntax)
