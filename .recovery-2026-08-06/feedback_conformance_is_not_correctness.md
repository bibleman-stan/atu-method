---
name: feedback-conformance-is-not-correctness
description: "Canon-conformance (didn't trip an encoded validator) is NOT the bidirectional-test correctness rate — measure the real yardstick by sampling, never report rule-conformance as a completeness claim"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/a0cca8480420859c@v3`); state as of 2026-06-05 (snapshot mtime); possibly stale — re-verify before relying.

**The trap (2026-05-22):** I reported BoFM pure-method as "~98% complete" on canon-conformance (510 flagged lines / 22,994 = 97.8% not tripping any encoded validator). Stan: *"that also throws your whole '98% complete' premise into question and it needs to be examined at every level."* He was right twice over:

1. **Canon-conformance ≠ correctness — it is only an UPPER BOUND.** A validator only catches what its rule encodes. A line can trip ZERO validators and still fail the bidirectional ATU test (bare "And it came to pass." was the proof — 100% conformant, broken thought). So "97.8% conformant" ⇒ true correctness ≤ 97.8%, gap unmeasured. The number certifies "broke no rule we wrote," never "is a complete thought."

2. **The metric was also CONFOUNDED.** `run_all.py` discovers all `validate_*.py`; ~13 legacy validators hardcode `default=.../v2-mine` and silently scored Stan's HAND-EDITS, while ~23 `_ud` validators (via `book_paths` + `BOFM_V2_DIR`/`BOFM_CONLLU_DIR`) scored pure-method. The "TOTAL: 935" mixed two corpora. This is why my totals swung 523/547/935/1061 across runs — I kept re-citing a confounded number. Clean pure-method = sum of `book_paths` validators only.

**What the REAL yardstick showed (5-genre bidirectional sample, 727 lines, parallel Sonnet agents):** Enos 1 37% fail · 1 Nephi 1 47% · 2 Nephi 8 (Isaiah) 44% · Alma 5 (sermon) 55% · Moroni 7 (epistle) 61%. **~51% of lines fail the bidirectional test** — against 97.8% "conformant." The gap between the two metrics is the whole point. Discourse/expository fails worse than narrative (more subordination/relatives/coordinate chains).

**How to apply — ALWAYS:**
- **Never report rule-conformance as a completeness/"% done" claim.** State it as "didn't trip encoded validators" and pair it with a bidirectional-test sample number, or don't quote a percentage at all.
- **The bidirectional test is measured by SAMPLING actual output across genre clusters** (parallel agents, strict reading), not by counting validator hits. Make it a standing gate, like the Hebrew 4-genre / Greek 3-genre validation designs.
- **Before citing any conformance number, confirm what corpus each validator reads.** Confounded apparatus = meaningless total.
- **Verify a surprising audit finding against the actual file** before relaying it (traced "he saw / and heard much" split to confirm agents weren't hallucinating). Ties to [[feedback_debug_trace_values]].

Ties to [[feedback-hand-edit-is-a-datapoint]] (don't substitute hand-edit granularity for the yardstick either) and [[feedback-check-prior-corpora]] (Tanakh/GNT used genre-spread validation as the real measure — the wheel).


**Validator regressions on a newly-shipped binding rule are NEVER a Stan-decision punt.** +N validator regressions on a §2.2- or §v1.x-citing rule = rule-is-wrong signal until proven otherwise via fresh `Read` of the cited canon section + verbatim firewall quote demonstrating non-violation. Punting to Stan with "validator may encode pre-framework canon" without re-Reading the canon is conformance-flipped-into-its-opposite: using rule-conformance to justify the rule instead of measuring the rule against canon. 2026-06-05 anchoring failure: Alma 34:7 PP-conj rule hit +30 validator regressions; Claude said "validator encodes pre-framework canon" without re-Reading framework.md §2.2(ii) which would have shown the rule violates the firewall. The validator was right; the rule was wrong.
