# ATU and rhetorical/discourse lenses are distinct

**Principle (Stan, 2026-06-06).** ATUs and discourse/rhetorical structure are different lenses on
the same text. They sometimes overlap, often don't. Naming the lens distinction explicitly —
and choosing ATU as the primary criterion via `framework.md §2.1`/§2.2, with rhetoric a constraint
not a determinant per `cross-corpus-principles.md §1.3a` — is itself a methodology contribution of
the segmentation/delimitation critical method.

## Statement

The apparatus's primary criterion is the **ATU lens**: the smallest cognitive unit the reader can
process before needing the next. ATUs are determined by:

- `framework.md §2.1` — the bidirectional test (forward grammatical closure + backward referential self-containment)
- `framework.md §2.2` — the explicit-marker license (closed per-corpus registry)
- Default per `framework.md §2.2:116`: **KEEP-AS-IS unless (A) or (B) licenses a break.**

The apparatus also recognizes a **rhetorical/discourse lens**: how the author organizes argument,
contrast, climax, parallelism, periodic structure, chiasmus, and other suprasegmental moves.
Rhetorical structure has default ATU dispositions (parallelism predicts SPLIT per J1, hendiadys
predicts MERGE per M1, chiasmus has no force on ATU within members, etc. — see
`cross-corpus-principles.md §1.3a`). These defaults are **hypotheses**, not determinations. The
bidirectional test always wins.

**Sometimes the lenses overlap. Often they don't.** A rhetorical period may be one ATU or several.
A chiastic center may align with an ATU boundary or sit inside an ATU. A parallel triplet may
render as three ATUs (per J1 N≥3 cliff) or as one (when forward closure fails for individual
members). The lenses ask different questions; their answers are independent.

## Why this distinction is a methodology contribution

The segmentation/delimitation-criticism literature historically conflates these lenses. Scheppers'
colometric work, Marschall's period/colon, the intonation-unit / idea-unit literature (Chafe 1994),
Korpel & Oesch's "delimitation criticism," and the BHRG-style discourse grammars (Heimerdinger,
Westbury) all sometimes slide between "this is a rhetorical unit" and "this is a cognitive unit"
without naming the slide. The result is methodology blur: the same observation is cited as one or
the other depending on which serves the argument.

Our method's contribution: name the lenses explicitly, choose ATU as the primary criterion, make
rhetoric a constraint not an alternative determinant. This pays off in three places:

1. **Defensibility against existing CL literature.** Chafe's idea units, Cresti's information units,
   Hannay & Kroon's information packages — each can be related to ATU via the lens distinction
   without collapsing into them.
2. **Per-verse disposition clarity.** When a reader's instinct reads a rhetorical structure (e.g.
   a 3-move pericope), the lens distinction names what's being observed without requiring it to
   become an ATU split.
3. **Audit cleanliness.** A proposed break grounded in "rhetorical reasons" can be rejected at the
   `framework.md §2.2:116` firewall (cognitive-unity gates / parallelism class adjudication / genre
   anchors are NOT primary licensors) without disputing the rhetorical observation. The rhetorical
   reading is real; it just doesn't license an ATU break by itself.

## How to apply

When a reader's instinct (or a per-verse audit) proposes a break:

1. **Name the claim.** Is it "this is a single cognitive bite" (ATU claim) or "these are distinct
   rhetorical moves" (rhetorical claim)?
2. **For ATU claims:** run `framework.md §2.1` bidirectional test + §2.2 marker check. KEEP-AS-IS
   default holds unless §2.1 or §2.2 licenses a break.
3. **For rhetorical claims:** the observation is valid but does not license an ATU split by
   itself. Document separately (scholarship layer, annotation track, periscope index) without
   altering the ATU rendering.
4. **When they conflict:** the framework wins on ATU disposition. Rhetorical structure does NOT
   override §2.1/§2.2. Conversely, an ATU split licensed by §2.1 stands even if it cuts a
   rhetorical period.

## Anchoring example — Alma 34:16 (2026-06-06 walkthrough)

The verse has 3 distinct rhetorical moves:

> [1] mercy resolves justice → [2] contrast with unfaithful via "while" → [3] consequence for faithful via "therefore"

Per `framework.md §2.1`: "And thus..." and "therefore..." fail backward containment per the
asymmetry section (discourse-anaphoric particles named verbatim at line 41); "while..."
subordinates without an independent matrix. Per §2.2: BoFM marker registry lists `yea` and `or
rather`, not `thus` / `therefore`. Net: KEEP-AS-IS, 1 ATU. Live rendering: 1 line.

The rhetorical reading (3 moves) and the ATU reading (1 unit) are BOTH correct — they answer
different questions. The lens distinction is what lets us hold both simultaneously without
confusion.

## Future-paper framing

When the cross-corpus convergence thesis matures into publication, the lens distinction is one of
the cleanest "what's new" framings against existing precedent. Foreground in introductions; relate
to (not against) existing IU / DU / IP literature; demonstrate via cross-corpus convergence that
the ATU lens is corpus-invariant in a way rhetorical lenses are not.

Concretely:

- vs. **Chafe's idea unit** (1994): both are "smallest cognitive bite" claims but Chafe is
  prosody-grounded (intonation contour) while ATU is author-grounded (syntactic test). The
  difference matters for written corpora where prosody is reconstructed; ATU's bidirectional test
  applies to written text directly.
- vs. **Korpel & Oesch's delimitation criticism**: their criteria fold rhetorical and cognitive
  signals together (paragraph markers, te'amim, manuscript layout); our method makes the lens
  explicit and rejects te'amim as a primary licensor (`framework.md §2.2:116`).
- vs. **Cresti's information units / Hannay & Kroon's IP**: related theoretical ancestors;
  ATU specifies the lens precisely (syntactic closure + referential containment) where IU/IP
  remain looser.
- vs. **BHRG-style discourse grammar** (Heimerdinger, Westbury): different abstraction layer;
  discourse grammar describes how arguments cohere across multiple ATUs; ATU describes the
  per-line cognitive content.

## Aligns with

- [[../docs/framework.md §1 Purpose]] (NOT-list already names "Reveal rhetorical parallelism" as a separate scholarly layer; this memory expands on the principle)
- [[../docs/cross-corpus-principles.md §0.1]] (lens scope statement in the canonical companion)
- [[../docs/cross-corpus-principles.md §1.3a]] (rhetoric figures constrain, atomic-thought determines)
- [[../docs/framework.md §2.2:116]] (parallelism class adjudication excluded as primary break-license — the firewall the lens distinction operationalizes)
- [[../docs/framework.md §2.1 final paragraph]] (punctuation has zero force — same shape: editorial overlay is its own lens, not the ATU determinant)
- [[../docs/methodology-position.md]] (LDHB / discourse-grammar relationship — the framing here generalizes the position from a single named precedent to the principle)
