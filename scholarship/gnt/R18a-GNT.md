# R18a-GNT: Patriarch-Deity-Triad Fixed Formula (Greek) — Scholarship Companion

**Operational entry:** see `readers-gnt/private/01-method/colometry-canon.md §8 Patriarch-deity-triad`.

**Status:** This is the scholarship companion documenting WHY R18a-GNT exists, HOW we know it is correctly framed, and what intellectual and empirical history grounds its current shape. The operational canon entry says WHAT the rule does; this document says why.

---

## Statement

R18a-GNT (Patriarch-Deity-Triad Fixed Formula, Greek instantiation) requires that the deity-formula token sequence *ὁ θεὸς Ἀβραάμ* ... *Ἰσαάκ* ... *Ἰακώβ* — in any of its four attested distributional variants — be kept whole on a single line whenever the spanning sequence appears within a single verse-block. The rule is the Greek sibling of BoFM R18a, which governs the same underlying formula in its KJV-English surface form. Both rules are sisters to R18 (fixed lexicalized idioms), R1 (AICTP formula), and R23 (date-colophon formulas) — each governs a closed-list KEEP_WHOLE span under Tier 2 indivisibility.

## Rationale

The triad *ὁ θεὸς Ἀβραὰμ καὶ ὁ θεὸς Ἰσαὰκ καὶ ὁ θεὸς Ἰακώβ* — and its compressed variants — functions in the NT register as a **single fixed referring expression to YHWH**, not as an enumeration of three distinct patriarch-anchored deities. The formula is a direct LXX-mediated quotation from Exodus 3:6 (Exod 3:6 LXX: *ἐγώ εἰμι ὁ θεὸς τοῦ πατρός σου, θεὸς Ἀβραὰμ καὶ θεὸς Ἰσαὰκ καὶ θεὸς Ἰακώβ*), where YHWH names himself to Moses by reference to the three patriarchs of the covenant. By Jesus's and Stephen's time, the formula was a well-worn christological-apologetic citation — a single appellation with a long history of unitary reference.

Severing the formula across line boundaries fractures a unitary deity-reference into the apparent compositional enumeration of three patriarch-anchored deities — a parsing that the formula's lexicalized status forbids. The principle is identical to BoFM R18a's: a multi-word frozen expression that functions as a single retrieval unit in the reader's mental lexicon should be presented as one visual unit.

What distinguishes R18a-GNT from its BoFM sibling is the surface-form inventory: the Greek's article-distribution space differs from KJV English's possessive-prepositional space. The four attested variants in the NT corpus are:

1. **Fully-distributed** — `ὁ θεὸς Ἀβραὰμ καὶ ὁ θεὸς Ἰσαὰκ καὶ ὁ θεὸς Ἰακώβ` (Matt 22:32, Mark 12:26)
2. **Anchor-shared (articular accusative)** — `τὸν θεὸν Ἀβραὰμ καὶ θεὸν Ἰσαὰκ καὶ θεὸν Ἰακώβ` (Luke 20:37) — article on the anchor only; subsequent members lack the article
3. **Compressed (no article on members)** — `ὁ θεὸς Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακώβ` (Acts 3:13, Acts 7:32) — θεός-lemma governs only the first patriarch; subsequent patriarchs are bare conjuncts
4. **Extended-lead** — `ὁ θεὸς τῶν πατέρων σου, ὁ θεὸς Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακώβ` (Acts 7:32 full formula) — an appositional-lead phrase precedes the triad

The operational matcher therefore uses an in-order spanning-sequence rule rather than exact-string lookup: any verse-block whose tokens contain a `θεός`-lemma governing `Ἀβραάμ`, followed (in order, within the same verse) by `Ἰσαάκ`, followed by `Ἰακώβ`, is treated as the formula.

## Grammatical grounding

Syntactically, the patriarch-deity-triad in Greek is a **fixed coordinate-NP referring expression** functioning as a complex proper noun. The structure is a coordinate compound of three NPs, each with `θεός` as head and a proper-noun genitive (or juxtaposed proper noun in articular-genitive-free constructions) as modifier.

**Article distribution.** Greek coordinate-NP article distribution follows the Granville-Sharp pattern and its extensions: where the same article governs multiple coordinate nouns, they are treated as a single referent-complex; where each noun takes its own article, each is more individuated. The triad's variant forms exploit this continuum:

- *Fully-distributed* (separate article on each member): each member is individuated; the unity is semantic-formulaic, not grammatically mandated by article-sharing.
- *Anchor-shared* (article only on first member): the remaining members are grammatically subsumed under the first article's governance, reinforcing unitary-reference reading.
- *Compressed* (θεός-lemma only once): the remaining patriarchs are bare conjuncts coordinated directly, an extreme compression of the anchor-head.

In all three variants, the **semantic-pragmatic function is invariant**: the sequence is a fixed appellation for YHWH. Greek coordinate syntax permits free distribution of the article and head noun across conjuncts without changing the referential unity of the formula.

BDF §276 on article distribution in coordinate NPs and §266 on proper-noun constructions with genitives provide the grammatical licence for the range of attested surface forms. BDAG entries for *Ἀβραάμ*, *Ἰσαάκ*, *Ἰακώβ* note the NT's formulaic use of the triad as a single messianic-apologetic tag. Smyth §1143–1146 on Greek article syntax with coordinate nouns covers the same distribution mechanics.

The Layer 3 placement (not Layer 1) reflects the same consideration as BoFM R18a: indivisibility here is an editorial recognition of the formula's lexical-bundle status in the LXX-mediated NT register, not a generic Greek-grammatical fact.

## Empirical evidence

### Corpus survey

The patriarch-deity-triad appears at five NT loci:

1. **Matt 22:32** — fully-distributed; *ἐγώ εἰμι ὁ θεὸς Ἀβραὰμ καὶ ὁ θεὸς Ἰσαὰκ καὶ ὁ θεὸς Ἰακώβ*; already compliant pre-codification (triad whole on one line)
2. **Mark 12:26** — fully-distributed; *ἐγὼ ὁ θεὸς Ἀβραὰμ καὶ ὁ θεὸς Ἰσαὰκ καὶ ὁ θεὸς Ἰακώβ*; already compliant pre-codification (triad whole on one line)
3. **Luke 20:37** — anchor-shared variant; triad was **split** across lines 211–212 (R11 speech-intro split caused the break); **mechanical fix applied** in commit `3921a50` — speech-intro `ὡς λέγει` moved to its own prior line per R11, triad consolidated on a single content line
4. **Acts 3:13** — compressed variant; *ὁ θεὸς Ἀβραὰμ καὶ Ἰσαὰκ καὶ Ἰακώβ* preceded by `ὁ θεὸς τῶν πατέρων ἡμῶν` on a separate appositional line (60); triad itself already compliant (whole on one line)
5. **Acts 7:32** — extended-lead variant; triad whole on line 153, but preceding line 152 carries `Ἐγὼ ὁ θεὸς τῶν πατέρων σου,` — **Category B, Stan-review**: boundary judgment on whether the extended-lead phrase is an appositional-head to the triad (merge both onto one line) or a separate prior apposition (current compliant state); the triad line itself is already correct

Post-survey (commit `3921a50`, 2026-05-11): the corpus is compliant on the triad proper at all five loci. The one open question is the Acts 7:32 extended-lead boundary.

### Compliance verification

The validator `validators/colometry/check_r18a_patriarch_triad.py` in readers-gnt reports zero triad-split violations against the post-`3921a50` corpus.

## Intellectual lineage

R18a-GNT derives from the same **lexical-bundle integrity principle** that grounds BoFM R18a and the GNT's broader R18 (fixed lexicalized idioms). Cross-tradition scholarly grounding:

- **LXX manuscript layout traditions.** The triadic deity-formula in Exodus 3:6 and its NT quotations is presented as a single per-cola unit in early codices. Codex Vaticanus's per-cola arrangement of Matthew 22:32 keeps the triad whole — corroborating the unitary-presentation tradition from the earliest Greek manuscript stratum.

- **Targum-tradition translation discipline.** The rabbinic Aramaic targumim consistently render the Hebrew triadic-deity formula (אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב) as a single appellation, never as three separate deity-references. The NT quotations inherit this unitary-reference discipline.

- **TEI Guidelines P5 on multi-word expressions** (`<mwe>`, `<choice>`): the scholarly-editing standard for tagging frozen multi-word formulas as units applies directly. The patriarchal triad is a canonical candidate for `<mwe>` tagging in any TEI-conformant critical apparatus.

- **CGEL** Chapter 12 on coordination-with-ellipsis: the mechanics of *the God of X, the God of Y, the God of Z* → *the God of X, [the God] of Y, [the God] of Z* coordination admit free distribution of the anchor without affecting unitary-reference status. The Greek equivalents follow the same coordination-with-ellipsis mechanics under BDF §276.

R18a-GNT's codification (2026-05-11, commit `3921a50`) was prompted by Stan's directive to port the BoFM R18a principle to the GNT corpus: *"remember the stepbible incorporation; codify the patriarch-triad as a long single-thought reference to the LORD"* (Stan, 2026-05-11). The GNT audit (task `a24e5638aaa0e6434`) surveyed all five NT loci, identified the Luke 20:37 split as a mechanical violation, and flagged Acts 7:32 as Category B.

## Adversarial history

The codification of R18a-GNT was a **port** from BoFM R18a, not an independent derivation. The BoFM rule had already been through two adversarial-audit cycles (see BoFM R18a.md §Adversarial history): the first cycle considered M4-protected-reference framing vs. R18-sibling fixed-formula framing; the second cycle ran a hostile audit on coordinate-object ellipsis-stacking discriminators and returned Verdict H5 (no clean discriminator exists). Both verdicts are inherited by R18a-GNT because the formulaic-status argument and the coordination-mechanics argument are language-independent: they apply to the Greek surface form for the same reasons they apply to the KJV English surface form.

The GNT-specific audit (`a24e5638aaa0e6434`) tested whether any GNT-corpus feature (article distribution, Granville-Sharp patterns, Greek coordination syntax) required modifying the BoFM rule's framing. Verdict: no modification warranted. The four Greek distributional variants (fully-distributed, anchor-shared, compressed, extended-lead) are all covered by the same in-order spanning-sequence matcher, parallel to the BoFM rule's variant-matching mechanism.

One genuine GNT-specific complexity: the **extended-lead variant** at Acts 7:32 (`Ἐγὼ ὁ θεὸς τῶν πατέρων σου,` as line 152, triad as line 153). This boundary was not present in the BoFM corpus. The BoFM rule's SCOPE-exclusion #3 covers *lead-in title phrases on separate lines* as a legitimate appositional continuation staying on its own line — the same principle applies here. The triad proper remains whole (line 153 compliant); whether line 152 should merge into line 153 is an editorial boundary-of-formula question (Category B) rather than a triad-split violation. Deferred to Stan-review.

## Future work

### Acts 7:32 extended-lead boundary (Stan-review)

The open Category B item: `Ἐγὼ ὁ θεὸς τῶν πατέρων σου,` (line 152) + triad (line 153). Two defensible positions:
- **Split (current):** appositional lead is a separate prior apposition; SCOPE-exclusion #3 applies. Compliant.
- **Merge:** the full formula including the appositional lead is the YHWH self-identification unit; a single line carries the whole. Category B judgment.

Stan's decision determines whether extended-lead becomes a fifth closed-list variant or remains excluded under SCOPE-exclusion #3.

### Cross-corpus alignment (Tanakh)

The source formula אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב appears in Exodus 3:6, 3:15, 3:16, 4:5, with additional patriarch-deity formula loci in Genesis and 1 Chronicles. A Tanakh-specific rule would be needed; the framework (Tier 2 KEEP_WHOLE for unitary deity-formulas) is universal, the Hebrew surface matchers are not. BoFM R18a and R18a-GNT together establish the cross-corpus precedent that Tanakh R18a would inherit.

### Hebrews 11 patriarchal survey

Hebrews 11:8–22 surveys the patriarchs by name in a *pistis*-catalogue that does not use the θεός-lemma anchor. Those loci are governed by SCOPE-exclusion #1 (personal-name list without θεός anchor) and R18a-GNT does not fire. A future survey could verify that no θεός-anchor triad is embedded in the Hebrews 11 catalogue.

---

*References:*

- Operational canon entry: `readers-gnt/private/01-method/colometry-canon.md §8 Patriarch-deity-triad` (codified 2026-05-11, commit `3921a50`)
- Universal framework: `atu-method/docs/framework.md §1.5` (fixed-idiom integrity / formula integrity)
- Sister rule (BoFM): [`../bofm/R18a.md`](../bofm/R18a.md)
- Validator: `readers-gnt/validators/colometry/check_r18a_patriarch_triad.py`
- Audit task: `a24e5638aaa0e6434`
- GNT commit: `3921a50` (readers-gnt, 2026-05-11)
- BDF §276 (article distribution in coordinate NPs); BDF §266 (proper-noun constructions)
- CGEL Chapter 12 (coordination-with-ellipsis)
- BDAG s.v. *Ἀβραάμ*, *Ἰσαάκ*, *Ἰακώβ*
