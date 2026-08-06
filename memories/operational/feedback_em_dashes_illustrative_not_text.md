---
name: em-dashes-illustrative-not-text
description: "Em-dashes in Skousen/scholarly clausal-structure illustrations are not real text — they're a typographic device showing where the clausal boundary sits. In our system (punctuation has zero force), the restoration target is the clausal-boundary signal, NOT the dash marks themselves."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/936fea27f9d9476d@v2`); state as of 2026-06-01 (snapshot mtime); possibly stale — re-verify before relying.

When Skousen (or any analyst) uses em-dashes around a parenthetical to expose the true clause structure obscured by later editorial punctuation, the em-dashes themselves are **illustrative**, not canonical text. They are doing the work of showing the clause — but the clause is what's real, the dashes are not.

**Why:** This came up 2026-05-29 during Alma 37:41 Skousen-restoration analysis. The original 1830 reading was "Nevertheless, because those miracles were worked by small means, nevertheless it did show unto them marvelous works; they were slothful…" The post-1837 deletion of the second "nevertheless" collapsed a parenthetical aside into a false apodosis. Skousen-style restoration would set off the parenthetical with em-dashes — but in our system punctuation has zero force (see `feedback_external_unit_is_not_atu.md` + the no-split-on-punctuation rule). Em-dashes don't survive into v0 and have no effect on the binding engine.

**How to apply:**
- When restoring a textual variant with clausal implications, encode the **clause-boundary signal** (where the parenthetical opens / closes, the true apodosis attachment), NOT the dash marks.
- The Skousen-restoration architecture (option C, deferred 2026-05-29) is a `data/text-files/v0-skousen-restorations.json` layer that supplies the missing structural signal — likely as a token-insertion ("nevertheless" added back) or an explicit clause-boundary annotation consumed by the fabric, not as a punctuation-style overlay.
- For our purposes, em-dashes in scholarly prose are diagnostic: they tell us *where* the binding/break belongs, and we encode that structural fact through whatever non-punctuation mechanism the fabric supports (frame-mark insertion, sub-clause annotation, etc.).
- Generalizes beyond Skousen: any analyst's punctuation in their analysis is illustrative-of-structure, never the target of restoration.

Related: [[feedback_external_unit_is_not_atu]] (scholars' criteria are feedstock, not verdict — the bidirectional ATU test is the sole arbiter).
