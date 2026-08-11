---
cssclasses:
  - wide
---

# Audit — linguistic and computational-linguistic viability

> **Hostile audit** of [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]], commissioned 2026-08-09. Lens: linguistics and computational linguistics. The brief was to find where the proposal breaks on linguistic reality, not to improve it. Every file claim carries a pasted receipt; every scholarly claim carries a citation.
>
> **Status: AUDIT FINDINGS. Nothing adopted, nothing changed.** No commit, no push.

---

## Verdict summary

| # | Finding | Label | Severity |
|---|---|---|---|
| 1 | The 31-shared-lines evidence measures **two HTML renderers**, not two rule engines. Correction A's proof is a category error. | CONFIRMED | **FATAL** |
| 2 | 11 of 13 live Hebrew rules key on **ETCBC clause-type tags that have no equivalent in any other substrate**. There is nothing to parameterise. | CONFIRMED | **FATAL** |
| 3 | The one-rule-many-corpora experiment **was already run** (Hebrew→LXX) and it **failed**, in the project's own recorded numbers. | CONFIRMED | **FATAL** |
| 4a | **Gate 0 / te'amim**: prosodic, not idea-unit; banned by the project's own canon in three places; and *already the generator of the deployed Hebrew text*. Triply disqualified. | CONFIRMED | **FATAL** |
| 4b | **Gate 0 / Skousen**: the sense-lines are **Skousen's own editorial punctuation**, not manuscript lineation. The proposal's description is factually wrong. | CONFIRMED | **FATAL** (as arbiter) |
| 4c | **Gate 0 / Marschall**: syllable-bounded *rhetorical/prosodic* côla; the project's own memory already ruled them non-identical to ATUs. | CONFIRMED | SERIOUS |
| 4d | The LXX evaluation gold (UD-PTNK) is itself **Hebrew-projected** — the LXX validation is circular. | CONFIRMED | **FATAL** |
| 5 | "One engine over UD/TF parses" is a false premise: the five corpora sit on **five different annotation formalisms**, only two of which are UD. | CONFIRMED | SERIOUS |
| 6 | The per-corpus branching **has already happened inside the canon itself** (framework §2.1), not just in the Python. Unifying the code does not unify the criterion. | CONFIRMED | SERIOUS |
| 7 | v0→v1→v1.5→v2 is not a universal shape — **the deployed Tanakh pipeline does not run it**, and the LXX applier no longer exists on disk. | CONFIRMED | SERIOUS |
| 8 | No segmentation-appropriate metrics (WindowDiff / Pk / B / γ), no chance correction, no inter-annotator agreement. `cardinality match` is close to meaningless. | CONFIRMED | SERIOUS |
| 9 | Tokenisation and treebank-interoperability standards are unaddressed. | CONFIRMED | MINOR |
| 10 | Where the linguistics **is** identical (Tanakh vs Tanakh), the code **is** accidentally duplicated at 72%. The proposal is right about a class it never identified. | CONFIRMED | — (survives) |

---

## Method and receipts

All measurements run 2026-08-09 from `C:\Users\bibleman\repos`.

Shared-line measurement script (`scratchpad/shared_lines.py`) — strips blanks, lines under 10 chars, and comment lines; compares the sets of remaining distinct stripped lines. This is my reconstruction of the proposal's "identical non-trivial lines" metric; my counts run slightly lower than its stated 31 (definition-dependent), which does not affect any conclusion below.

---

## Finding 1 — The central evidence measures the wrong layer (CONFIRMED, FATAL)

The proposal's single quantitative claim for its spine is Part 2 row 3 and Correction A:

> `readers-tanakh/scripts/build_books.py` (540 lines) and `readers-gnt/scripts/build_books.py` (462 lines) share **31 identical non-trivial lines** — same name, same job, diverged.
> — [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]]:41
>
> The 31-shared-lines measurement is the proof: two files with the same name doing the same job have almost nothing in common. **A rule must be one artifact, parameterised per corpus, executed by one engine.**
> — [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]]:88

**These two files contain no binding rules.** They are HTML renderers — component 7 in the proposal's own taxonomy, not component 3 or 5.

```
$ sed -n '1,3p' readers-tanakh/scripts/build_books.py
"""
build_books.py - Generate three-layer HTML book fragments from tier sources.

$ sed -n '1,3p' readers-gnt/scripts/build_books.py
"""
build_books.py — Generate HTML book files from colometric text sources.
```

Both read *already-segmented* text off disk and emit markup:

> Reads chapter files from v1.5/grk/*/ (Greek) and v1.5/eng-kjv/*/ (English,
> KJV-verbatim), and writes one HTML fragment per book into books/.
> — `readers-gnt/scripts/build_books.py`:3-4

Grep for any binding logic returns nothing but a rendering tokeniser:

```
$ grep -nE "should_bind|def .*bind|B1[0-4]|binding_rule|merge_|split_" \
    readers-tanakh/scripts/build_books.py readers-gnt/scripts/build_books.py
readers-tanakh/scripts/build_books.py:158:def split_hebrew_cola_to_words(cola_line)
readers-tanakh/scripts/build_books.py:244:            words = split_hebrew_cola_to_words(he_cola)
```

`split_hebrew_cola_to_words` splits an already-decided cola into orthographic words so each can get a `<span>`. It is a renderer utility, not a segmentation rule.

The full function inventories confirm it — every function is parse-a-file, render-a-layer, or discover-books:

```
$ grep -nE "^def " readers-tanakh/scripts/build_books.py
130:def parse_chapter_lines      158:def split_hebrew_cola_to_words   173:def render_he_layer
183:def render_word_layer        208:def _load_ot_swap_pipeline       224:def render_chapter
282:def _files_in                291:def lines_to_lookup              295:def _pick_source
313:def build_book               483:def main

$ grep -nE "^def " readers-gnt/scripts/build_books.py
48:def parse_chapter            102:def build_ylt_lookup             122:def _wrap_verse_markers
136:def build_chapter_html      213:def discover_books               250:def _book_prefix
257:def _find_book_subdir       275:def resolve_greek_path           289:def resolve_english_path
304:def build_book              350:def _run_integrity_check         383:def main
```

**Why this is fatal rather than a citation slip.** The two renderers *should* diverge, and their divergence is linguistically motivated. The Tanakh renderer emits a four-layer right-to-left reader with per-orthographic-word span alignment across Hebrew / transliteration / interlinear / gloss, and carries a maqqef-driven prosodic-joining class:

> The .joined class on a translit/interlinear word means "this Hebrew word
> ends in maqqef and is prosodically joined to the next"
> — `readers-tanakh/scripts/build_books.py`:31-32

The GNT renderer emits a two-layer left-to-right Greek/English reader with a superscript verse-marker mechanism. Maqqef does not exist in Greek. Four-layer word alignment is not wanted in the GNT product. **These are different reading editions, so they are different documents, so they are different renderers.** Measuring their line overlap and concluding "the rules diverged" is a category error twice over: wrong component, and the divergence it detects is a product decision.

I reproduced the measurement and inspected what the shared lines actually *are*:

```
$ python scratchpad/shared_lines.py readers-tanakh/scripts/build_books.py readers-gnt/scripts/build_books.py
  345 nontrivial-unique lines  readers-tanakh/scripts/build_books.py
  268 nontrivial-unique lines  readers-gnt/scripts/build_books.py

SHARED   19
        | OUTPUT_DIR = os.path.join(REPO_ROOT, "books")
        | REPO_ROOT = os.path.dirname(SCRIPT_DIR)
        | SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        | VERSE_REF_RE = re.compile(r"^\d+:\d+$")
        | def main():
        | if __name__ == "__main__":
        | import argparse
```

Every shared line is Python scaffolding. **The metric cannot distinguish "these rules diverged" from "these are two different programs that happen to be written in Python."** It has no discriminating power for the claim it is asked to support.

The real rule engines are elsewhere:

| Corpus | Rule engine | Lines |
|---|---|---|
| Tanakh (research pilot) | `readers-tanakh/research/atu-pilot-mechanical-first/v1_5_apply_bindings.py` | 305 |
| Tanakh (`atu_pipeline_v2`) | `readers-tanakh/scripts/atu_pipeline_v2/binding_rules.py` | 189 |
| GNT | `readers-gnt/scripts/sblgnt_generate.py` | 513 nontrivial |
| BoFM | `readers-bofm/5-machinery/scripts/bofm_generate.py` | 1333 |
| LXX | `C:/tmp/lxx_binding/apply_binding_rules.py` — **does not exist** (see Finding 7) |

Run on the *actual* engines, the metric bottoms out even harder:

```
$ python scratchpad/shared_lines.py \
    readers-tanakh/scripts/atu_pipeline_v2/binding_rules.py \
    readers-bofm/5-machinery/scripts/bofm_generate.py \
    readers-gnt/scripts/sblgnt_generate.py
  100 nontrivial-unique  binding_rules.py
  878 nontrivial-unique  bofm_generate.py
  513 nontrivial-unique  sblgnt_generate.py

SHARED  2  :: binding_rules.py <-> bofm_generate.py      ("return False", "return out")
SHARED  2  :: binding_rules.py <-> sblgnt_generate.py    ("return False", "return out")
SHARED  9  :: bofm_generate.py <-> sblgnt_generate.py    ("import sys", "def main():", ...)
```

**Correction A rests on a measurement of the presentation layer. The specification layer was never measured. The spine of the proposal is unsupported by its own evidence.**

---

## Finding 2 — There is nothing to parameterise (CONFIRMED, FATAL)

The proposal asks for "one artifact, parameterised per corpus." Parameterisation presupposes that the rules differ in their *values* while sharing their *shape*. Read the Hebrew engine and the presupposition collapses.

`readers-tanakh/scripts/atu_pipeline_v2/binding_rules.py`:35-122, verbatim excerpts:

```python
def should_bind(prev: dict, curr: dict) -> tuple[bool, str | None]:
    if prev["verse"] != curr["verse"]:  return False, None
    if curr["typ"] == "Voct":           return True, "B1-vocative"        # B1
    if curr["typ"] == "Defc": ...                                          # B2
    if curr_consonants.startswith("אשר"): return True, "B3-..."            # B3
    if (prev["head_verb_lemma"] == "היה" and prev["typ"] in WAYYIQTOL_TYPES ...) # B5
    if prev["typ"] == "CPen":           return True, "B6-cpen-resumption"  # B6
    if (prev["typ"] == "Way0" and prev_token_count <= 1 ...)               # B7
    if (prev["typ"] == "NmCl" and prev_consonants.startswith(("הנה","והנה"))
        and curr["typ"] == "ZQt0"):                                        # B8
    if (curr["typ"] == "NmCl" and curr_consonants.startswith("נאם")):      # B9
    if curr["typ"] == "InfC":           return True, "B10-purposive-infc"  # B10
    if (prev["head_verb_lemma"] in COGNITION_VERB_LEMMAS
        and curr_consonants.startswith("כי")):                             # B11
    if prev["typ"] == "Reop":           return True, "B12-reop-binding"    # B12
    if curr["typ"] == "Ptcp" and prev["head_verb_lemma"] == "היה":         # B13
    if curr["typ"] in ("ZYq0", "ZQt0"): return True, "B14-..."             # B14
```

**11 of the 13 live rules (B1, B2, B5, B6, B7, B8, B9, B10, B12, B13, B14 — 85%) trigger on `typ`**, the ETCBC/BHSA clause-type tag. Only B3 (a consonant-prefix match on `אשר`) and B11 (lemma set + `כי` prefix) do not.

`typ` is not a general linguistic category with a cross-linguistic realisation. It is a value from a proprietary ETCBC taxonomy that encodes the Biblical Hebrew verbal system directly into the tag: `Way0`/`WayX` (wayyiqtol with/without explicit constituent), `ZQt0`/`ZYq0` (zero-conjunction qatal/yiqtol), `NmCl` (nominal clause), `CPen` (casus pendens), `Voct`, `InfC`, `Ptcp`, `Reop`. **UD has no such layer.** UD gives `upos`, `deprel`, `feats`; it does not give a clause-type ontology, and its designers deliberately did not build one ([Universal Dependencies](https://universaldependencies.org/)).

So "parameterise B12 for Greek" is not a parameter change. `Reop` is an ETCBC editorial diagnosis of discourse re-opening. There is no Greek value to put in the slot, because there is no slot.

**The project already discovered this, rule by rule, and wrote it down.** From [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]], the "Rules NOT ported" table and its per-rule reasoning:

| Hebrew rule | LXX status | Recorded reason (verbatim) |
|---|---|---|
| B2 | **NOT PORTED** | "Greek has no et-marker" (:233) |
| B6 | **NOT PORTED** | "keys on BHSA's `CPen` clause-type tag… **No equivalent tag exists** in the LXX projection" (:199) |
| B12 | **NOT PORTED** | "**BHSA-specific clause-type tag, no Greek analog** and no LXX projection signal" (:238) |
| B14 | **NOT PORTED** | "targets BHSA's clause-type signature… a Greek-surface analog would over-merge paratactic narrative" (:179, :239) |
| B8 | **NOT PORTED** | "the bidirectional test wants the residual cases split" (:237) |
| B1 | ported only by approximation | "**No Greek vocative-case marker.** Hebrew B1 (Voct clause type from BHSA) **does not port**" (:54-56) |

That is 5 of 13 rules explicitly not portable, plus B1 portable only as a re-derived approximation. The stated reason in four of the six cases is *the absence of the BHSA tag*.

**The counter-hypothesis holds.** The Hebrew catalog is not a language-neutral rule set awaiting parameters. It is a set of queries against one treebank's annotation ontology. That is not accidental divergence; it is the correct way to write rules over BHSA, and it is unportable by construction.

### The substrate-capability asymmetry, stated precisely

Compare what each engine must *do* to answer the same linguistic question — "does this segment carry an independent predication?"

Hebrew, from BHSA (one lookup):

```python
if curr["typ"] == "Voct":   return True, "B1-vocative"
```

Early Modern English, from a Stanza UD parse (42 lines, reconstructing what BHSA hands over):

```python
def _seg_independent_predication(seg):
    """... a VERB whose deprel is root/conj/parataxis, not governed by an in-segment
    subordinator ...; OR a COPULAR predicate (ADJ/NOUN/PRON/PROPN with a `cop` child)
    whose deprel is root/conj/parataxis with its OWN subject ...
    Errs toward 'no independent predication' only when EVERY clause is subordinate."""
```
— `readers-bofm/5-machinery/scripts/bofm_generate.py`:299-340

The BoFM engine is 878 non-trivial lines against Tanakh's 100 **for the same job**, because it is reconstructing clause structure that BHSA supplies as a primitive, from a parse the project itself calls weak, over a register (Early Modern English) the parser was not trained on. Note the defensive comments — "Parse-robust", "Errs toward", "the old VERB/AUX-only test skipped `cop` and wrongly called this a frame". That is not divergence for want of an engine. That is the tax on a poor substrate, and one engine does not abolish it; one engine has to *contain* it.

---

## Finding 3 — The experiment has already been run, and it failed (CONFIRMED, FATAL)

This is the strongest evidence available, and it is the project's own. [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]] is a full-dress attempt to do exactly what the proposal proposes: take the Hebrew catalog, re-express each rule for a second corpus, run it, measure it.

**Result, from the catalog's own smoke-test tables (:336-345):**

| Metric | Pre (raw projection, no rules) | Post v1 | Post v2 |
|---|---|---|---|
| Cardinality match (1547 verses) | 682 (44.1%) | 691 (44.7%) | 696 (**45.0%**) |
| Mean per-gold Jaccard | 0.6958 | 0.6879 | 0.6946 (**−0.0012 vs raw**) |

The entire ported catalog, after two refinement rounds and morphological gating, moved cardinality match by **+0.9 percentage points** and left mean Jaccard **slightly worse than applying no rules at all**. The catalog says so plainly:

> v2 hit the +14 card-match-delta target floor (catalog goal was "≥ +20"; we landed at +14 — the +20 target assumed v1's diacritic-collision-driven B2 helps were real, which they mostly weren't).
> — [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:341-345

**And the rules that did the most work were the ones with no Hebrew ancestry at all.**

- **LXX-B0**, rated the highest-confidence rule in the catalog ("**this is the strongest binding signal in the LXX pipeline**", :68), is provenance `LXX-original` and is not a linguistic rule at all — it collapses two output lines when they trace to the same MT clause-atom. It is alignment plumbing.
- **LXX-B6** (genitive absolute) is marked "Greek-original (**NOT a Hebrew port**)" (:145) — a construction the catalog states has "**no Hebrew analog**" (:48-51).

Meanwhile the flagship port, B5 (wayhi temporal frame ↔ καὶ ἐγένετο), was **switched off**:

> **Over-merge risk: HIGH against UD-PTNK gold.** v1 smoke (2026-05-30) had **2 helped / 16 hurt**; gold treats the wayhi-frame as its own ATU even when temporally anchored. … revealed **no Greek-surface pattern that separates helps from hurts cleanly** — the same anchor tokens appear in both groups.
> — [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:109

And B11 (the ὅτι↔ki analogue the proposal cites as its compounding channel) is **also off**:

> **Current default: rule is OFF in the applier (commented out)** pending CenterBLC `that-VP`/`sub-CL` projection.
> — [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:159

### On the ὅτι↔ki and ὅς↔ʾăšer analogies specifically

The proposal cites these as evidence of a real compounding channel. [[memories/feedback_cross_corpus_convergence.md|feedback_cross_corpus_convergence.md]]:5 states it maximally: "**ὅτι *is* ki; ὅς *is* ʾăšer, at the clause-binding level**" — while :9 forbids assuming it.

Linguistically the analogy is **partial and directionally misleading**:

- **ὅτι ↔ כִּי.** Both are polyfunctional complementiser/causal particles, so the surface parallel is real. But the *disambiguation problem is not shared*. Hebrew B11 disambiguates by matrix-verb lemma alone (`COGNITION_VERB_LEMMAS`). Greek cannot: framework §2.1 documents that a lemma-list approach produced causal over-binds at Matt 5:36, John 2:18, 1Cor 3:13, and that the discriminator must come from Macula's `rule="that-VP"` vs `rule="sub-CL"` features (:48). Greek additionally has **recitative ὅτι** — ὅτι introducing verbatim direct discourse — which Hebrew כִּי does not have in the same way, and which framework §2.1 must handle with a separate deixis test and participant-tracking via `subjref`/`referent` (:50). So: same-shaped particle, **different disambiguation machinery, different feature source, different failure modes**. Calling it "one rule with parameters" hides three distinct mechanisms.
- **ὅς ↔ אֲשֶׁר.** Real typological similarity (both head restrictive relatives), and the framework's corollary at §2.1:54 is sound. But the LXX catalog flags a Greek-specific hazard Hebrew does not have: "**Greek often uses ὅς for non-restrictive relatives too, which are NOT bindable**" (:95) — because Greek marks the restrictive/non-restrictive distinction differently from Hebrew, and `אֲשֶׁר` does not carry case-number-gender agreement that opens the same ambiguity. Net measured effect of the ported rule in v2: **6 helped / 5 hurt / +1** (:353).

**Verdict.** The analogies are typologically genuine at the level of *construction type* — restrictive relatives bind, complements bind, vocatives bind. That is a well-attested cross-linguistic tendency and the framework is right to name it. But it is genuine at exactly the altitude where it buys nothing operationally: **the construction generalises, the trigger never does.** Every ported rule needed a new trigger, a new feature source, and a new set of counter-examples, and half of them needed to be switched off. Convergence at the level of "restrictive relatives bind" is a paragraph in a paper, not a parameterised artifact.

---

## Finding 4 — Gate 0: the arbiter question

This is the load-bearing gate. The proposal:

> **Gate 0 — the arbiter question. Nothing is built before this is answered.** Is there an external segmentation witness that our rules did not produce? Candidates: Masoretic **te'amim**, **Skousen's** manuscript-tradition lineation, **Marschall's** syllable bands. If none is adequate, **stop**.
> — [[4-process/master-proposal-rebuild.md|master-proposal-rebuild.md]]:195-196

**My verdict: none of the three is an external witness to *idea-unit* segmentation. All three measure something else. The gate fails.** But it fails informatively, and Finding 4e below says what a real arbiter would have to look like.

Note first that **the project has already answered this**, and the proposal does not cite it. [[memories/operational/feedback_external_unit_is_not_atu.md|feedback_external_unit_is_not_atu.md]]:16-19 — a memory dated 2026-05-26, indexed in [[memories/operational/MEMORY.md|MEMORY.md]]:94 — rules on Marschall and Korpel by name:

> **Why:** each scholar's target object differs from the idea-unit, and the mismatch runs BOTH ways:
> - **Scheppers' colon** = the prosodic *intonation/information unit* — **finer** than the ATU… His "fronting makes a colon" rule = our documented over-split failure mode.
> - **Marschall's côlon** = a *rhetorical/sound-mapping* unit with syllable bounds (7–25, ≤35)… **Syllable thresholds are prosodic.**
> - **Korpel's colon** sits in a 6-level hierarchy… line/strophe are supra-ATU; poetic cola can be sub-ATU.

That memory's ruling — "**The bidirectional ATU test is the sole arbiter.** External criteria are *feedstock* filtered through it" (:14) — is the correct linguistic position, and it is incompatible with Gate 0 as written. Gate 0 asks for an arbiter; the standing canon says there cannot be one, by design.

### 4a — Te'amim: prosodic, canon-banned, and already inside the output (CONFIRMED, FATAL)

**(i) Linguistically, the te'amim are a prosodic system, not a semantic-unit system.** The standard modern linguistic account is Dresher's: the accents are built from units of the prosodic hierarchy and **"deviate from syntactic constituency in ways that are characteristic of prosodic representations"** (B. Elan Dresher, "The Prosodic Basis of the Tiberian Hebrew System of Accents," *Language* 70/1 [1994]: 1–52). Prosodic phrasing is *derived from* syntax but is not isomorphic to it — it is reshaped by phonological weight, eurhythmy, tempo and phrase-length constraints. That is precisely why the accents sometimes agree with syntax and sometimes do not.

The scholarly picture is genuinely contested and I should state the other side fairly: Aronoff (1985, *Language* 61) and Price (*The Syntax of Masoretic Accents in the Hebrew Bible*, 1990) argue for a syntactic basis, and Yeivin's principles of relative accent value are routinely used to read syntax off the accents. De Hoop and Sanders survey the dispute ([JHS 22, 2022](https://jhsonline.org/index.php/jhs/article/view/29622)). But **no position in that debate claims the accents segment idea-units.** Even the maximally syntactic reading gives you a syntactic hierarchy, and the framework's own §2.1 is explicit that grammatical closure is *a proxy for thought, not thought*. The gap between "syntactic constituent" and "atomic thought unit" is the whole methodology; te'amim cannot arbitrate across it.

**(ii) The te'amim are banned by this project's own canon — three times.** [[1-method/framework.md|framework.md]]:

> **Punctuation has ZERO force**… Editorial punctuation (commas, colons, ano-teleia, sof-pasuq) **and accentuation (te'amim)** are overlay added after the author's thought-structure; they have **zero force in ATU decisions**. (§2.1:101)

> safety rests on their conjunction — NOT on "the token is on the page" (**te'amim are on the page too, and stay banned**). (§2.2:107)

> The framework does NOT include cognitive-unity gates on parallel cola, parallelism class adjudication, **te'amim hierarchy**, or genre anchors as primary licenses. (§2.2:116)

> Rules that produce candidate boundaries WITHOUT cognitive-criterion grounding (**te'amim hierarchy as primary**, parallelism class as primary, aesthetic preference) **are forbidden**. (§7.9:361)

There is a defensible distinction the proposal does not draw: banned as a *licensor* (input to rules) ≠ banned as a *witness* (independent evaluation reference). A hostile reading still kills it. If te'amim have zero force by canon, then when the accent hierarchy and our output disagree, **canon forbids us from acting on the disagreement.** An arbiter whose verdicts you are forbidden to act on is not an arbiter. It is a decoration.

**(iii) Fatally, the te'amim are not external to the Tanakh output — they generate it.** `readers-tanakh/scripts/run_full_pipeline.py`:11-16 lists the production pipeline:

```
Steps per book:
  1. ingest_tahot.py    --book <book_key>
  2. parse_teamim.py    --book <book_key>
     Skip: data/text-files/v1/he-baseline/<out_subdir>/ already exists
  3. apply_validators.py --book <out_subdir>
  4. propagate_editorial_layers.py --book <out_subdir>
  5. regenerate_english.py ...
  6. build_books.py ...
```

Step 2 is the segmenter, and it segments on the accents:

> parse_teamim.py - **Te'amim-driven baseline cola generator** (starting draft for v2/heb editorial).
> **Splits at te'amim cola boundaries derived from the Hebrew accents.**
> — `readers-tanakh/scripts/parse_teamim.py`:2-6

And the deployed text is an edit-distance from that baseline:

> **v1 = te'amim baseline draft, v2 = editorial gold standard.** The cascade picks the most-refined version that exists per chapter.
> — `readers-tanakh/scripts/build_books.py`:11-13

> v1-he-baseline is the editor's starting draft (**seeded by te'amim parsing**); v2/heb (editorial) freely adds, removes, or merges line breaks **relative to this baseline**.
> — `readers-tanakh/scripts/parse_teamim.py`:24-26

The project is aware of the tension and has a canon section for it ("The Te'amim Are Not a Structural Prior", Rule H8 "Te'amim as Evidence", cited at `parse_teamim.py`:27-28). That framing does not survive as an *arbiter* argument. Every deployed Hebrew line break started life as an accent-derived break and was then kept or moved by a human editor. Using te'amim to validate that output measures **editorial edit-distance from the seed**, anchored by the seed. This is the exact circularity the proposal warns against at :191 — "**cases are adjudicated by us against our own rules, this is circularity in a nicer container**" — one layer worse, because the seed is upstream of the human too.

**Verdict 4a: te'amim are disqualified on all three counts independently.** Wrong object (prosody), canon-forbidden, and non-independent of the artifact they would judge.

### 4b — Skousen: not a manuscript witness (CONFIRMED, FATAL as arbiter)

The proposal calls this "**Skousen's** manuscript-tradition lineation" (:196) and "Skousen's manuscript lineation" ([[Pending-Decisions.md]]:59). **This is factually wrong, and the error is the whole point.**

Skousen's *The Book of Mormon: The Earliest Text* (Yale University Press, 2009; 2nd ed. 2022) sets the text in sense-lines. But the sense-lines are **Skousen's own editorial apparatus, introduced because the manuscripts have no such structure**:

> The punctuation, sense line breaks, and paragraph breaks are **Skousen's**; the original manuscript had none, and the printer's manuscript didn't have much more.
> — [Times & Seasons, "The Original Text of the Book of Mormon II: The Yale Edition"](https://archive.timesandseasons.org/2011/02/the-original-text-of-the-book-of-mormon-ii-the-yale-edition-of-the-book-of-mormon/index.html)

> The sense-lines format breaks up the lines of the text according to phrases and clauses. Skousen decided to adopt the sense-line format **to reflect how Joseph Smith dictated the text**. His dictation did not indicate punctuation, sentence structure, or paragraphing.
> — [Book notice, ScriptureCentral](https://scripturecentral.org/blog/book-notice-second-edition-of-the-book-of-mormon-the-earliest-text); cf. [BYU Studies review](https://byustudies.byu.edu/article/the-book-of-mormon-the-earliest-text), [Yale UP](https://yalebooks.yale.edu/book/9780300263374/the-book-of-mormon/)

So the object is: **one twenty-first-century scholar's judgment about phrase-and-clause boundaries, motivated by a hypothesis about oral dictation, over a text whose manuscript witnesses supply no lineation evidence at all.** That is a second analyst applying an unstated criterion — valuable as a second opinion, worthless as an external witness, and *definitionally* not "manuscript-tradition."

Two further problems specific to using it as an arbiter here:

1. **Different target object.** "Phrases and clauses" is a syntactic granularity. The ATU is explicitly *not* the atomic predication (framework §2:22). Skousen's cola will be systematically finer than ATUs in the same way Scheppers' are — the granularity mismatch the project's own memory calls "expected, not error" ([[memories/operational/feedback_external_unit_is_not_atu.md|feedback_external_unit_is_not_atu.md]]:24).
2. **Already ingested as input.** `bofm_generate.py` carries `_load_skousen_restorations()` (:158) and `_apply_skousen_restoration()` (:186), and [[memories/operational/MEMORY.md|MEMORY.md]]:95 records a ruling that "em-dashes in Skousen\scholarly clausal illustrations are NOT canonical text; punctuation has zero force in our system." Skousen is already feedstock on the input side of the BoFM pipeline. Using him on the output side as arbiter re-imports the te'amim circularity in English.

**Verdict 4b: disqualified as arbiter.** Usable — and genuinely useful — as an independent *second annotator* for agreement measurement (see 4e), which is a different and lesser thing.

### 4c — Marschall: prosodic bands, already ruled out; but one real asset (CONFIRMED, SERIOUS)

Marschall's côlon is defined with **syllable bounds (7–25, ≤35)**, per [[memories/operational/feedback_external_unit_is_not_atu.md|feedback_external_unit_is_not_atu.md]]:18. A unit defined by syllable count is a **metrical/prosodic** unit by construction. It cannot be an idea-unit witness for the same reason a 14-line constraint does not tell you where the argument of a sonnet turns.

This sits inside the long-running dispute in Hebrew colometry over whether syllable-counting is a legitimate criteriology at all — the field has not settled what a colon *is*, let alone agreed a method for finding one (see the "Colometry of Hebrew Verse and the Masoretic Accents" evaluation, [Part I](https://www.academia.edu/1470534/The_Colometry_of_Hebrew_Verse_and_the_Masoretic_Accents_Evaluation_of_a_Recent_Approach_Part_I) / [ResearchGate](https://www.researchgate.net/publication/311903418_THE_COLOMETRY_OF_HEBREW_VERSE_AND_THE_MASORETIC_ACCENTS_EVALUATION_OF_A_RECENT_APPROACH_PART_1); Park & Price, *Typology in Hebrew Poetic Meter: A Generative Metrical Approach*). Importing an unsettled criteriology as your ground truth imports its instability.

**But there is one genuine asset here that the proposal does not mention and should have.** [[memories/operational/_deferred_queue.md|_deferred_queue.md]]:88:

> **Validation oracles to build** (independent boundary checks): **Korpel's ~92% Masoretic-disjunctive-accent agreement** (Tanakh ATU-vs-te'amim measurement — **corroboration, not a force**); **Marschall's hand-segmented 2 Cor 10–13 as a GNT gold set**; **Scheppers' P1/P2 Wackernagel postpositive position as a Greek-only boundary validator**.

**Marschall's hand-segmented 2 Corinthians 10–13 is a real, external, human-produced segmentation of a Greek text that this project did not produce.** It is small, it is at the wrong granularity, and it answers a different question — but it is the only candidate on the table that is genuinely independent *and* genuinely a segmentation. The Scheppers Wackernagel-position test is better still, because postpositive placement (δέ, γάρ, μέν in P1/P2) is a **hard morphosyntactic fact about Greek clitic placement**, not an analyst's judgment: it identifies where a Greek speaker treated a phonological phrase as beginning. That is the closest thing to an objective boundary signal anywhere in this document's evidence.

The [[memories/operational/_deferred_queue.md|_deferred_queue.md]] framing — "corroboration, not a force" — is exactly right and is the framing Gate 0 should have used.

### 4d — The LXX gold is Hebrew-projected: the existing validation is circular (CONFIRMED, FATAL)

Separate from the three named candidates, the arbiter the project *actually uses* for LXX is UD_Ancient_Greek-PTNK. That gold is not independent of the pipeline it evaluates.

The LXX pipeline is, by the catalog's own description, a Hebrew projection:

> The LXX pipeline is a **Hebrew-projection** pipeline (CATSS-aligned BHSA clause-atoms projected through MT→LXX word alignment onto the CenterBLC Greek word stream).
> — [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:16-18

And UD-PTNK was built the same way:

> This treebank was produced using text extracted from greekdoc.github.io **with initial syntactic relations produced by word-aligning and projecting the relations from the parallel Ancient Hebrew treebank**, before automatically correcting systematic syntactic mismatches and manually correcting other errors.
> — [UD_Ancient_Greek-PTNK](https://github.com/UniversalDependencies/UD_Ancient_Greek-PTNK); method paper: [Producing a Parallel Universal Dependencies Treebank of Ancient Hebrew and Ancient Greek via Cross-Lingual Projection](https://aclanthology.org/2024.lrec-main.1145/) (LREC-COLING 2024)

**Both sides of the LXX evaluation descend from the same Hebrew annotation.** Agreement between them is not cross-linguistic convergence; it is a shared source. Any convergence result computed on Gen+Ruth LXX is uninterpretable as evidence for the program thesis.

And the sting: **even in this maximally favourable setting — Hebrew-projected system evaluated against Hebrew-projected gold — cardinality match is 45.0%.** If shared ancestry cannot get the two to agree on the *number of units* in more than half of verses, the residual is not a rule-engineering problem. It is the granularity gap between "syntactic annotation" and "idea unit," and no architecture closes it.

The catalog half-sees this, calling UD-PTNK "the gold-**segmenter**'s behavior" and "the UD-PTNK **auto-segmenter**" (:109, :366) and invoking `conformance ≠ correctness`. That instinct is right and should be promoted to a finding: **UD-PTNK is a dependency treebank. It has no ATU layer. Its "partition" is a syntactic-annotation artifact.** Measuring ATU output against it measures conformance to UD annotation conventions.

### 4e — What a real arbiter would have to be (PLAUSIBLE)

Since Gate 0 fails as posed, the useful contribution is the spec it should have written. An external witness to idea-unit segmentation must be:

1. **Targeting the same object** — idea units, not cola, not intonation units, not syntactic clauses, not metrical lines. On current evidence **no such published resource exists for these corpora.** Every candidate surveyed (te'amim, Skousen, Marschall, Korpel, Scheppers, LDHB, UD-PTNK) targets a demonstrably different object.
2. **Causally independent of the artifact** — not the seed of it (te'amim/Tanakh), not an input to it (Skousen/BoFM), not projected from the same source (UD-PTNK/LXX).
3. **Produced under a stated criteriology**, so that disagreements are diagnosable rather than merely countable.
4. **Multiply instantiated**, so that the arbiter's own reliability can be measured before it is trusted (see Finding 8).

Condition 4 is the one that changes the answer. **If no external arbiter exists, the available substitute is not a better external source — it is a properly-constructed internal one:** a held-out set segmented independently by two or more annotators under the §2.1 criterion, blind to each other and to the pipeline output, with agreement reported using a unitizing-appropriate coefficient. That is a *reliability* claim rather than a *validity* claim — weaker than what Gate 0 asked for, and honest about being weaker. It also happens to be the only thing that would tell Stan whether the bidirectional test is operationalisable by anyone other than Stan, which is the question actually underneath all of this.

**Note also that Gate 0's own escape hatch is sound and is the likeliest correct outcome**: "If none is adequate, **stop** — the system is additive by nature, and the correct response is to run it as such and skip the rebuild entirely" (:196). On this audit's evidence, that branch is the one that fires.

---

## Finding 5 — "One engine over UD/TF parses" is a false premise (CONFIRMED, SERIOUS)

The proposal's Part 6 target diagram shows one `ENGINE` consuming "corpus data packages · substrates". The commissioning brief describes it as "one engine over UD/TF parses". The five corpora do not sit on two formalisms. They sit on five:

| Corpus | Substrate | Formalism | Unit |
|---|---|---|---|
| Tanakh | BHSA via Text-Fabric (ETCBC) | **ETCBC clause-atom + clause-type ontology** | `clause_atom` |
| GNT | Macula Greek (Clear Bible) lowfat XML | **Macula/lowfat syntax trees** — `cltype`/`rule`/`role`/`subjref` | clause node |
| BoFM | Stanza CoNLL-U | **UD** (out-of-register parse) | sentence |
| LXX | CATSS MT→LXX alignment + CenterBLC TF morph + UD-PTNK | **hand-built alignment projection** | CATSS line |
| Vulgate | UD_Latin-PROIEL → TF v0.1 | **UD** (PROIEL-converted) | — |

Receipts: framework §3:141-144 for the first three; [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:16-18 for LXX; [[CLAUDE.md]]:44,97 for Vulgate/PROIEL.

Only BoFM and Vulgate are UD. Tanakh's ETCBC clause-atom layer and Macula's `rule`/`role`/`referent` layer are **richer than UD in exactly the dimensions the rules depend on**, and are mutually untranslatable. Framework §2.1:48-52 depends on Macula features (`rule="that-VP"` vs `rule="sub-CL"`, `subjref`/`referent`) that exist in no other substrate — the section explicitly says "**No lemma list can separate these; the treebank does**" and that the GNT engine must be re-sourced onto Macula because the thinner `sblgnt-lowfat` lacks them.

A single engine over these five must therefore hold five substrate adapters with **non-overlapping capability sets**, and every rule must declare which capabilities it needs and what it degrades to when they are absent. That is not "a rule parameterised per corpus." That is a capability-negotiation layer plus five backends — the same divergence, relocated into a plugin interface, with an added abstraction tax and a new failure mode (silent capability fallback producing a different segmentation without saying so).

This is precisely the audit question posed in the brief — "the same divergence wearing a new coat" — and the answer is **yes**, with one qualification recorded in Finding 10.

---

## Finding 6 — The criterion itself has already branched per corpus (CONFIRMED, SERIOUS)

Even granting a unified engine, the proposal assumes the *specification* is corpus-neutral and only the triggers vary. Read framework §2.1 and that is not true today.

§2.1 opens with a genuinely universal core (forward closure + backward containment, ~lines 31-42). It then accretes, in the same section, a run of allowances that are corpus-specific in their conditions:

| Allowance | Line | Corpus scoping in the text itself |
|---|---|---|
| Serial circumstantial participial chains | :56 | "**EME English narrative**; cross-corpus parallel to Hebrew waw-prefixed chains" |
| Discrete cognitive-state circumstance chain | :63 | "(**EME English narrative**)" |
| Relative-clause-embedded speech-frame | :70 | Alma 32:17; "extend `_is_multiclause_quote`" |
| Discourse-particle attribution within reported speech | :72 | closed list "yea, behold, verily, lo, amen, yes" |
| Discourse-particle amplification | :81 | 1 Ne 11:1 |
| Cognition-frame participial allowance | :88 | "**Rare in BoFM (1 documented instance — Alma 33:1)**" |
| Object-slot + deixis tests for ὅτι | :48-50 | Macula-feature-sourced; **GNT only** |
| Explicit-marker Registry | §2.2:105-114 | "**registered per-corpus**" |

Six of these are Early Modern English / Book of Mormon allowances written into the shared framework document, two are Greek-only and depend on a Greek-only feature source, and the §2.2 Marker Registry is per-corpus **by design** ("Each marker is registered per-corpus with its bidirectional-test status", :114).

The §2.1:33 closure definition is itself already branched: "Languages with morphologically-encoded subjects (Hebrew finite verbs, Greek finite verbs, Latin finite verbs) license pro-drop… **EME English requires overt copula.**" That is a correct piece of linguistics and it is a per-corpus conditional in the definition of the primary criterion.

**The implication for the proposal is direct.** Its load-bearing relationship is "3 ↔ 4 ↔ 6 — a rule, the cases it decided, and the check that enforces it must be one artifact with three faces" (:31). But per-corpus branching lives at layer 3-and-above: it is in the *criterion*, not only the trigger. Unifying the engine does not unify the criterion; it just moves the `if corpus == "bofm"` from Python into the spec artifact, where it will be less visible, not more.

Worse for the "cases are the test suite" mechanism: the Alma 33:1 allowance is codified on **one documented instance**. Framework §7.3 trigger 3 ("Spot-check-based proposals — any canon claim resting on less than full-corpus-sweep evidence") should have fired on it. A test suite derived from single-instance allowances will encode the instance, not the rule.

---

## Finding 7 — v0→v1→v1.5→v2 is not a universal shape (CONFIRMED, SERIOUS)

The proposal's target diagram gives the engine as `v0→v1→v1.5→v2`. Framework §3:122-136 specifies it. Three problems.

**(i) The deployed Tanakh pipeline does not run it.** `run_full_pipeline.py`:11-16 (quoted in full at 4a-iii) is `ingest_tahot → parse_teamim → apply_validators → propagate_editorial_layers → regenerate_english → build_books`. There is no v1.5 binding stage. The binding rules are **not referenced from `readers-tanakh/scripts/` at all** except inside the separate `atu_pipeline_v2/` tree:

```
$ grep -rn "v1_5_apply_bindings\|apply_bindings" readers-tanakh/scripts/
readers-tanakh/scripts/atu_pipeline_v2/binding_rules.py:125:def apply_bindings(...)
readers-tanakh/scripts/atu_pipeline_v2/run_full_tanakh.py:39:from binding_rules import apply_bindings
readers-tanakh/scripts/atu_pipeline_v2/run_full_tanakh.py:409:  groups_raw = apply_bindings(...)
readers-tanakh/scripts/atu_pipeline_v2/tanakh_overrides.py:12: ...
```

So **Tanakh has two parallel segmentation methods** — an accent-driven production path that ships, and a rule-driven path in `atu_pipeline_v2/`. The canonical Hebrew catalog B1–B14 documented in [[1-method/binding-rules-hebrew.md|binding-rules-hebrew.md]] describes the second one. That is a far more serious architectural finding than anything the proposal identified, and the proposal does not mention it.

**(ii) The LXX applier does not exist.** The catalog names its implementation seven times, including in "Adding a new LXX rule" step 7:

> Applier: `C:/tmp/lxx_binding/apply_binding_rules.py` — [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:289, :411

```
$ ls -la /c/tmp/lxx_binding/
ls: cannot access '/c/tmp/lxx_binding/': No such file or directory
```

Every LXX number quoted in Finding 3 is therefore **unreproducible**. The substrate caches (`full_verse_data.json`, `centerblc_morph.json`, `post_binding_scores_v2.json`) are gone with it. The catalog is honest that it is a "smoke-test artifact" (:3), but a rebuild that treats the LXX port as a validated data point is building on a number nobody can re-derive.

**(iii) The linguistic objection to the shape.** v1 is "parse-derived clauses" and v1.5 merges adjacent clauses upward. Framework §3:154 states the consequence: "**it does not split below clause-atom** or bind across verse boundaries." But framework §6:225 lists sub-clause gapping as an unfixable gap *created by this shape* — "when BHSA puts two ATUs inside one clause-atom via verb-ellipsis in parallel comparatives (Gen 22:17 stars + sand pattern). **Requires sub-clause splitter.**" And §2.2's entire explicit-marker license exists to break units *below* the level (A) licenses (":109-112").

So the pipeline is **merge-only over a substrate whose atoms are sometimes too coarse**, and the framework has had to open two escape hatches (§2.2 markers, §1.6 cross-verse continuity) plus a v2 LLM residual and a v3 editorial residual to work around it. That is not a universal shape; it is one substrate's granularity (ETCBC clause-atoms) promoted to an architecture. For BoFM the natural unit is the Stanza *sentence* — far coarser — which is why `bofm_generate.py` is dominated by *splitting* machinery (`_marker_split`, `_split_one`, `_split_at_stack_leaders`, `_detect_stack_leaders`) rather than binding. **Tanakh merges up; BoFM splits down.** Calling both "v1.5 binding rules" is a naming convention over two opposite operations.

**(iv) Corroborating scale evidence.** `overrides.json` carries 911 hand-adjudicated verses:

```
$ python -c "import json; d=json.load(open('readers-bofm/data/text-files/v2-adjudicated/overrides.json',encoding='utf-8')); print('keys:',len(d)); print('all bare lists:', all(isinstance(v,list) for v in d.values()))"
keys: 911
all bare lists: True
```

The proposal reads this as a missing-warrants problem (component 4). Linguistically it is also a **coverage** signal: 911 verses where the mechanical layer's output was overridden wholesale. And the first entry is a §2.2 parallel-subordinator stack —

```
'moroni 5:2': ['O God, the Eternal Father, we ask thee ... to bless and sanctify this wine ...,',
               'that they may do it in remembrance of the blood of thy Son ...;',
               'that they may witness unto thee ... that they do always remember him,',
               'that they may have his Spirit to be with them.', 'Amen.']
```

— i.e. exactly the construction `_detect_stack_leaders` (:732) exists to handle. Overrides are overlapping with rules the engine already has. That is the "rule and case can disagree and nothing tells you which is wrong" problem the proposal correctly identifies at :31 — but it is a *rule-quality* problem, and one engine does not fix rule quality.

---

## Finding 8 — The evaluation is not measured with segmentation metrics (CONFIRMED, SERIOUS)

This is the finding most directly responsive to Stan's stated concern ("there is no guarantee that the gates and validators are correct"), and the proposal does not touch it. Its Part 7 answer is entirely structural — single source, calibration assertions, cases-as-tests. **None of those is a measurement.**

What the project currently reports:

| Metric in use | Where | Problem |
|---|---|---|
| Boundary F1 vs LDHB | framework §5:210-215 | Not distance-sensitive; near-misses penalised identically to gross errors |
| "Pipeline=cold-eye %" | framework §5:210-215 | Exact-match on a whole chapter; uninterpretable, and it collapses (25% on Lev 11) |
| **Cardinality match** | [[1-method/binding-rules-lxx.md|binding-rules-lxx.md]]:337 | Compares the *count* of units per verse. Two segmentations can share a count and agree on **zero** boundaries. |
| Mean per-gold Jaccard | :337 | Set overlap; ignores boundary position and ordering |

**What is missing, and is standard in this exact task:**

- **Pk** and **WindowDiff** (Pevzner & Hearst, "A Critique and Improvement of an Evaluation Metric for Text Segmentation," *Computational Linguistics* 28/1 [2002]: 19–36 — [MIT Press](https://direct.mit.edu/coli/article/28/1/19/1731/A-Critique-and-Improvement-of-an-Evaluation-Metric), [PDF](https://people.ischool.berkeley.edu/~hearst/papers/pevzner-01.pdf)). WindowDiff slides a window and penalises boundary-count mismatch within it, so a boundary off by one token is scored as a near-miss rather than as one false positive plus one false negative. This is the precise pathology the current F1 hides: the pipeline is described as "conservative on prose, over-segments in dense parallelism" (§5:217), which is a *distance-structured* error profile that F1 is blind to.
- **Boundary Similarity / B** (Fournier & Inkpen, "Segmentation Similarity and Agreement," NAACL 2012 — [ACL Anthology](https://aclanthology.org/N12-1038.pdf)), which handles near-miss and boundary-type distinctions and, unlike WindowDiff, supports a chance-corrected agreement form.
- **γ (gamma)** for unitizing (Mathet, Widlöcher & Métivier, "The Unified and Holistic Method Gamma (γ) for Inter-Annotator Agreement Measure and Alignment," *Computational Linguistics* 41/3 [2015] — [MIT Press](https://direct.mit.edu/coli/article/41/3/437/1524/The-Unified-and-Holistic-Method-Gamma-for-Inter)), which is the right instrument when annotators disagree about *where* units are, not just how to label them.
- **Chance correction of any kind.** No κ, no α, nowhere. Krippendorff's uα family is the segmentation-appropriate choice (Pons Bordería, "Inter-annotator agreement in spoken language annotation: Applying uα-family coefficients to discourse segmentation," [*Russian Journal of Linguistics*](https://journals.rudn.ru/linguistics/article/view/26802)).
- **Inter-annotator agreement at all.** Discourse-level annotation is the low-agreement end of the field — well below POS tagging (~98%) and syntax (~93%) (Artstein & Poesio, [Inter-annotator Agreement](https://apps.dtic.mil/sti/pdfs/AD1158943.pdf)). **We have no idea whether two competent annotators applying §2.1 would agree**, which means we have no upper bound on what any engine could achieve, and no way to tell "the engine is wrong" from "the task is underdetermined."

The general point is now well-established in the segmentation literature: "Macro F1 is not the best primary metric for linear text segmentation because segmentation errors are **structured and distance-sensitive**, while F1 is not… Boundary-only scores can yield **misleading comparisons when annotation granularity varies** across datasets or differs from system behavior" ([When F1 Fails: Granularity-Aware Evaluation for Dialogue Topic Segmentation](https://arxiv.org/pdf/2512.17083)). Granularity variance across annotators is not an edge case for this project — per [[memories/operational/feedback_external_unit_is_not_atu.md|feedback_external_unit_is_not_atu.md]]:24 it is the *expected* condition.

**`cardinality match` deserves a specific callout.** The LXX refinement was steered by it across two rounds, and every headline number in that catalog (44.1% → 44.7% → 45.0%, "+14 card-match-delta target floor") is a count comparison. **A metric that scores `[AB][CD]` and `[A][BCD]` as a perfect match cannot steer a segmenter.** The catalog's own red-line monitor is smarter than its headline metric — it tracks "pure over-merges from card-match" (39 → 11), which is at least directional. But the optimisation target was the wrong number.

**This finding is upstream of the rebuild in the same way Gate 0 is.** If the measurements cannot distinguish a good segmentation from a bad one, then "prove each step before the next" (:198) is unexecutable, "cases are the test suite" (:189) cannot be scored, and the behavioural-snapshot regression baseline (:68) records *changes* without being able to rank them. **Fixing the metrics is cheaper than any part of the rebuild and is a strict prerequisite for all of it.**

---

## Finding 9 — Tokenisation and interoperability are unaddressed (CONFIRMED, MINOR)

A computational linguist would expect these declared before any cross-corpus engine is designed; none appears in the proposal.

- **Token identity across substrates.** Hebrew must decide orthographic word vs prosodic word vs morpheme. The Tanakh renderer already carries this distinction and its maqqef-joining rule (`build_books.py`:31-32, 39-41), and B7 counts tokens (`prev_token_count = len(prev["text"].split())`) — so a *rule verdict* depends on a tokenisation convention that is nowhere specified. Greek must decide crasis and elision; Latin enclitic `-que`; EModE contractions.
- **Stable cross-substrate addressing.** Boundaries are currently expressed as line-splits of rendered text (`overrides.json` stores whole re-segmented strings, not offsets). There is no stand-off annotation model, so a boundary cannot be stated independently of the string it was computed over — which makes both regression diffing and any future annotator-agreement measurement fragile.
- **Diacritic-strip as a rule trigger.** B3 fires on `strip_pointing(text).startswith("אשר")`, and LXX-B2's v1 backstop is a diacritic-stripped surface list that the catalog itself records as broken: "Article `ὁ` collapses to `ο` under diacritic-strip, colliding with relative `ὅ`" — 114 fires in v1 collapsing to 12 once morph-gated (:308, :353). **Surface-string triggers over normalised text are a known-hazardous design** and two of the thirteen Hebrew rules use them.
- **Normalisation standard.** No declared Unicode normalisation form (NFC/NFD) for Hebrew pointing or Greek diacritics, which is a precondition for any of the above being reproducible across machines.

None of this is fatal, and all of it is ordinary practice that would be settled in the first week of a treebank project.

---

## Finding 10 — Where the divergence *is* accidental, and the proposal never looked (CONFIRMED — the strongest thing in it)

I ran the proposal's own metric on two implementations of the **same rules, in the same language, in the same repo**:

```
$ python scratchpad/shared_lines.py \
    readers-tanakh/scripts/atu_pipeline_v2/binding_rules.py \
    readers-tanakh/research/atu-pilot-mechanical-first/v1_5_apply_bindings.py
  100 nontrivial-unique  binding_rules.py
  170 nontrivial-unique  v1_5_apply_bindings.py

SHARED  72
        | """Decide if curr binds to prev. Return (should_bind, rule_name)."""
        | COGNITION_VERB_LEMMAS = {"ידע", "ראה", "שׁמע", "חשׁב", "זכר", "בין", "הכיר"}
        | WAYHI_ANCHOR_CONSONANT_PREFIXES = ("אחר", "ביום", "בהיות", "כאשר", "כי", "ב")
        | WAYYIQTOL_TYPES = {"Way0", "WayX"}
```

**72 shared lines — 72% of the smaller file — including the rule constants themselves.** This is a controlled result, and it is the cleanest thing in this audit:

| Comparison | Linguistics | Shared non-trivial lines |
|---|---|---|
| Tanakh ↔ Tanakh (same rules, same language) | identical | **72** |
| Tanakh ↔ BoFM (different language, different substrate) | different | **2** |
| Tanakh ↔ GNT | different | **2** |
| BoFM ↔ GNT | different | **9** |

**Where the linguistics is the same, the code is duplicated at 72%. Where the linguistics differs, it shares boilerplate and nothing else.** The shared-line metric, applied to the right files, refutes the proposal's cross-corpus thesis and confirms a within-corpus thesis it never stated.

The real duplication problem is therefore **intra-corpus, not inter-corpus**: `COGNITION_VERB_LEMMAS` and `WAYHI_ANCHOR_CONSONANT_PREFIXES` are Hebrew linguistic content copy-pasted into two files that can now drift silently against each other and against [[1-method/binding-rules-hebrew.md|binding-rules-hebrew.md]]. That is a genuine three-way drift surface, it is exactly the defect the proposal describes at :86 ("a rule exists twice per corpus — once as English prose in a catalog, once as Python in a reader"), and it is fixable **without any cross-corpus unification at all**: make the Hebrew rule constants and their catalog entry one artifact, per corpus.

---

## What survives

Stripping out the parts that break on linguistic reality, this much of the proposal holds up:

**1. The compilation-pipeline framing (Part 3 spine).** Naming the work "theory → spec → engine → edition" is correct and useful. What does not follow is that one compilation target serves five source languages.

**2. Correction B — validators are not skills.** Fully sound, and the linguistic reason is stronger than the one given: a segmentation criterion applied non-deterministically produces *unmeasurable* output. You cannot compute agreement, drift, or regression against a judgment that varies by run. This is the argument that should have been made, and it also implies the reverse — the *v2 LLM residual*, which the proposal is content to leave non-deterministic, is exactly where the current metrics are blindest.

**3. Rule ↔ check ↔ case as one artifact (Part 1's "3 ↔ 4 ↔ 6").** Correct, and Finding 10 shows the need is real and measurable. **Scope it per corpus.** One Hebrew artifact holding B1–B14's prose, triggers, and checks would eliminate a live three-way drift surface today.

**4. The behavioural snapshot (Part 2, "what is recoverable even though why is not").** The best idea in the document, and path-independent as claimed. Two amendments: capture boundaries as **stand-off character offsets over a normalised source**, not as re-segmented strings (Finding 9), and score snapshot-to-snapshot deltas with **WindowDiff/B**, not cardinality match (Finding 8).

**5. Presentation and publish unification (Parts 4 and 5).** The one place the "config, not code" claim is true. Script direction, fonts, layer count, and transliteration toggles are genuinely configuration. Note that Finding 1 shows the two renderers are currently *rightly* different products — so this is real work, not a merge — but the target is sound and it is the lowest-risk item on the list.

**6. Part 9's self-criticism was correct and should have been promoted to the verdict.** The proposal wrote:

> **The 31-shared-lines figure I used as evidence of accidental divergence may instead be evidence that the divergence is justified** — and if so, one engine is the wrong shape and this proposal's spine is wrong. (:207)

That is the finding. This audit confirms it — and finds the figure worse than merely ambiguous, since it was measured on the wrong layer entirely.

**7. Gate 0's structure, though not its candidates.** Gating on the arbiter question, and being willing to terminate the whole plan, is the right instinct correctly placed. It fails on all three named candidates (Finding 4), which means the escape hatch the proposal already wrote — *"the system is additive by nature, and the correct response is to run it as such and skip the rebuild entirely"* — is the branch the evidence selects.

### What should be done before anything is built

In dependency order, all cheap, none requiring an architectural commitment:

1. **Fix the metrics** (Finding 8). WindowDiff + B on every existing comparison. Retire cardinality match as a steering target. Cost: days. Everything downstream depends on it, including the ability to evaluate this proposal empirically.
2. **Measure the criterion's reliability** (Finding 4e). Two independent annotators, one held-out chapter per corpus, §2.1 only, blind. Report γ or uα. This tells you the ceiling before you build anything to chase it — and it is the only available answer to Gate 0.
3. **Reconcile the two Tanakh pipelines** (Finding 7-i). One corpus, two live segmentation methods, and the canonical rule catalog documents the one that does not ship. This is a bigger real defect than anything the proposal found.
4. **Collapse the intra-corpus rule duplication** (Finding 10). Per corpus, not across corpora.
5. **Re-examine the LXX result** (Findings 3, 4d, 7-ii) before it is cited again as convergence evidence: the applier is gone, and both sides of its evaluation descend from the same Hebrew annotation.

---

## Sources

- B. Elan Dresher, "The Prosodic Basis of the Tiberian Hebrew System of Accents," *Language* 70/1 (1994): 1–52 — [author's page](https://dresher.artsci.utoronto.ca/)
- Raymond de Hoop & Paul Sanders, "[The System of Masoretic Accentuation: Some Introductory Issues](https://jhsonline.org/index.php/jhs/article/view/29622)," *Journal of Hebrew Scriptures* 22 (2022) — incl. bibliography for Aronoff 1985 (*Language* 61, syntactic basis) and Price 1990 (*The Syntax of Masoretic Accents in the Hebrew Bible*)
- "[The Colometry of Hebrew Verse and the Masoretic Accents: Evaluation of a Recent Approach, Part I](https://www.academia.edu/1470534/The_Colometry_of_Hebrew_Verse_and_the_Masoretic_Accents_Evaluation_of_a_Recent_Approach_Part_I)" — [ResearchGate copy](https://www.researchgate.net/publication/311903418_THE_COLOMETRY_OF_HEBREW_VERSE_AND_THE_MASORETIC_ACCENTS_EVALUATION_OF_A_RECENT_APPROACH_PART_1)
- "[Colometry and Accentuation in Hebrew Prophetic Poetry](https://www.academia.edu/26055094/Colometry_and_Accentuation_in_Hebrew_Prophetic_Poetry)"
- Royal Skousen, ed., *The Book of Mormon: The Earliest Text* (Yale UP, 2009; 2nd ed. 2022) — [Yale UP](https://yalebooks.yale.edu/book/9780300263374/the-book-of-mormon/); [BYU Studies review](https://byustudies.byu.edu/article/the-book-of-mormon-the-earliest-text); [Times & Seasons, "The Original Text of the Book of Mormon II"](https://archive.timesandseasons.org/2011/02/the-original-text-of-the-book-of-mormon-ii-the-yale-edition-of-the-book-of-mormon/index.html); [ScriptureCentral book notice](https://scripturecentral.org/blog/book-notice-second-edition-of-the-book-of-mormon-the-earliest-text)
- Lev Pevzner & Marti Hearst, "[A Critique and Improvement of an Evaluation Metric for Text Segmentation](https://direct.mit.edu/coli/article/28/1/19/1731/A-Critique-and-Improvement-of-an-Evaluation-Metric)," *Computational Linguistics* 28/1 (2002): 19–36 — [PDF](https://people.ischool.berkeley.edu/~hearst/papers/pevzner-01.pdf)
- Chris Fournier & Diana Inkpen, "[Segmentation Similarity and Agreement](https://aclanthology.org/N12-1038.pdf)," NAACL-HLT 2012 — [arXiv](https://arxiv.org/pdf/1204.2847)
- Yann Mathet, Antoine Widlöcher & Jean-Philippe Métivier, "[The Unified and Holistic Method Gamma (γ) for Inter-Annotator Agreement Measure and Alignment](https://direct.mit.edu/coli/article/41/3/437/1524/The-Unified-and-Holistic-Method-Gamma-for-Inter)," *Computational Linguistics* 41/3 (2015): 437–479
- Ron Artstein & Massimo Poesio, "[Inter-annotator Agreement](https://apps.dtic.mil/sti/pdfs/AD1158943.pdf)"
- Salvador Pons Bordería, "[Inter-annotator agreement in spoken language annotation: Applying uα-family coefficients to discourse segmentation](https://journals.rudn.ru/linguistics/article/view/26802)," *Russian Journal of Linguistics*
- "[When F1 Fails: Granularity-Aware Evaluation for Dialogue Topic Segmentation](https://arxiv.org/pdf/2512.17083)," arXiv:2512.17083
- [UD_Ancient_Greek-PTNK](https://github.com/UniversalDependencies/UD_Ancient_Greek-PTNK); [UD_Ancient_Hebrew-PTNK](https://universaldependencies.org/treebanks/hbo_ptnk/index.html); "[Producing a Parallel Universal Dependencies Treebank of Ancient Hebrew and Ancient Greek via Cross-Lingual Projection](https://aclanthology.org/2024.lrec-main.1145/)," LREC-COLING 2024
- [Universal Dependencies](https://universaldependencies.org/)
- Sung Jin Park & James D. Price, *Typology in Hebrew Poetic Meter: A Generative Metrical Approach* — [ETS notice](https://etsjets.org/publication/typology-in-biblical-hebrew-meter-a-generative-approach/)
