# Framing the ATU for scholars: a Text-Fabric node-layer over the grammatical layers

**Stan flagged this as super-helpful for communicating to the scholarly demographic (2026-05-20).** The framing:

> In Text-Fabric terms, an **ATU is a node-layer added to the fabric — a lasso that groups slots by *complete thought* rather than by clause.** The grammatical layers (word / phrase / clause / sentence, e.g. BHSA's nodes) are the scaffold; the ATU is the layer above. This matches the methodology's "grammar constrains, thought determines" claim exactly: the grammar node-layers are the necessary, constraining input; the ATU layer is derived on top by the bidirectional/atomic-thought test.

**Why this framing is valuable (scholarly positioning):**
1. **Credibility by paradigm-fit.** It locates the ATU inside an established, respected infrastructure (Roorda's Text-Fabric, the ETCBC/BHSA tradition) rather than presenting it as a novel fringe construct. The ATU is "the next node-layer," not a new ontology.
2. **A precise, immediately-graspable definition.** ATU = a node grouping slots by complete thought, layered over the grammatical nodes. Scholars who know TF understand it in one sentence.
3. **Reproducible/queryable in their own tools.** An ATU layer can be expressed as a TF feature/node-set added to a dataset — others can inspect, query, and critique it.
4. **Pre-empts the "isn't this just clause-splitting?" objection.** No: it's a *distinct* layer with a *distinct* (psycholinguistic, bidirectional-test) criterion — sometimes coextensive with a clause, sometimes spanning several, sometimes crossing the versification overlay. The overlapping-hierarchy phenomenon TF was built to handle is the very phenomenon the ATU asserts.
5. **Carries the cross-corpus convergence claim.** The ATU node-layer is the *same kind of object* across languages — woven over each language's own grammar-fabric (BHSA for Hebrew, sblgnt-lowfat/MorphGNT for Greek, future fabrics for BoFM/LXX/Vulgate). See [[feedback_cross_corpus_convergence]].

**Caveat to keep honest (do not overclaim):** Text-Fabric itself is *agnostic* infrastructure — it neither privileges nor validates the ATU as the "true" unit; it merely provides a legitimate home for it. What TF's *design motivation* confirms is the deeper premise: meaning-units are real structural objects distinct from versification (the reason overlapping-hierarchy support exists). The ATU's privileged status rests on the atomic-thought test, not on TF.

**Pipeline embodiment:** v1 = read the grammatical node-layer (clauses); v1.5 = derive the ATU node-layer on top. The pipeline literally produces "the ATU layer of the fabric."

## Operationalization (from a Gemini exchange Stan banked, 2026-05-20) — the ATU as a formal node class
Extends the framing above with concrete TF mechanics. Treat the *mechanics* as sound (this is how TF works); treat the proposed *features/taxonomy* as proposals to be earned by our criteria, not as established — and discount the flattery ("epiphany entirely correct"), per [[feedback_rhetoric_bandwagon]].

- **ATU node definition:** an `atu` node is an abstract id (e.g. 900001…) that lassos a contiguous OR non-contiguous set of slots — text-free, like any TF node. So an ATU can subdivide a single sentence into several cognitive units, or span a verse boundary, with zero structural friction (the "grain" + overlapping-hierarchy dilemmas dissolve).
- **Custom features on atu nodes (proposed):** `atu_type` (cognitive function — propositional / parenthetical / connective / modifier), `atu_length` (slots enclosed = an empirical "grain size" / cognitive-density metric), `atu_core` (pointer to the slot/phrase that is the unit's semantic anchor / main assertion). These are useful operationalizations to define rigorously, not yet validated taxonomies.
- **Analytical payload (the real prize):** formalizing ATUs as a node class makes the method *queryable* across a whole corpus, e.g. `atu atu_type=propositional > clause txt=narrative > phrase func=Subj`. It enables systemic research questions: do specific authors use smaller/isolated ATUs in certain clause types? How do our computationally-derived ATU boundaries correlate with ETCBC macro-syntactic units? This queryability is itself a strong argument for eventually building *real* TF datasets for our corpora (esp. the from-scratch BoFM/LXX/Vulgate — see [[feedback_cross_corpus_convergence]] + the project's deferred fabric-building), since it turns the reading edition into a research instrument.
- **Net:** ATUs preserve the primary textual grid and the grammatical layers untouched, adding one independent node layer that maps/measures the text's cognitive rhythm — exactly the use case TF was designed for.
