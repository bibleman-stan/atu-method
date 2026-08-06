---
name: project-fef-aictp-paper
description: "FEF/AICTP paper — research findings from the 2026-05-22 colometric-rules work: the 'and'/'that' translation-artifact stats, the empty-frame definition, and the cross-corpus convergence (thesis, not yet a result)"
metadata:
  node_type: memory
  type: project
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`ca81ff61-4510-437d-8f8c-a539e0a05296/300c348e8c9ceb55@v3`); state as of 2026-05-22 (snapshot mtime); possibly stale — re-verify before relying.

**FEF paper thread** (JBMS-targeted; see [[project-bom-reader]] for the broader BoFM-reader context — note that memory is stale on git workflow). **FEF = Front-End Frame** (not "formulaic episode frame"). The AICTP ("(and) it came to pass") frame is the BoFM instantiation of the Hebrew **wayyiqtol + circumstantial-protasis** (wayhî) narrative frame.

**CANONICAL HOME IS STAN'S VAULT, not this memory.** The paper note is `C:\vaults-nano\my_brain\10_Projects\Article Ideas\'And It Came to Pass' - Front-End Frames in the Book of Mormon.md` (alias "FEF paper"). The and/that finding below is banked as a z/data zettel: `04_Zettels\Data\The 'and' and 'that' forms of 'it came to pass' are one construction.md`. Related vault notes: `04_Zettels\Synthesis\The Book of Mormon is mostly prose not poetry.md`, `…\A genre-neutral colometric criterion might function as an unsupervised genre classifier.md`; working folder `10_Projects\Readers\BoFM\`. This memory is just Claude's operational pointer — write paper content to the vault, not here.

**2026-05-22 — three paper-grade findings from the AICTP colometric rule work:**

1. **The "and"/"that" split is a translation artifact over ONE construction — now quantified.** In BoFM: **367 "that"-form** ("it came to pass THAT X", parsed parataxis) vs **533 "and"-form** ("it came to pass … AND X", parsed conj with own subject). Structural proof they're one construction: both reduce to *frame + displaced main clause = one ATU* once the frame is treated as semantically empty. The conjunction is English surface; the underlying frame is invariant. Re-runnable counts/examples: `~/repos/readers-bofm/scripts/scan_aictp.py`. This is a clean, countable, stage-1-safe claim.

2. **The frame is propositionally empty — that is WHY it binds.** "It came to pass" carries no event; it's episode-boundary scaffolding. So colometrically it cannot be its own thought-unit; it must attach to the clause it frames. Reframes AICTP from "a formula we keep on its own line" → "a frame that *can't* stand alone" (a principled, testable ATU definition). Shipped as the AICTP-and-form binding rule (`bofm_v1_fabric.py`, commit 0ad3873).

3. **Cross-corpus convergence = the spine of the FEF/AICTP idea, but it's a THESIS not a result.** Same frame-binds-forward behavior across: Hebrew wayhî+temporal+waw/kî (rule B5); BoFM "(and) it came to pass [and/that]" (AICTP); Greek narrative frames / genitive-absolute (the GNT R19 audit independently named B5 as the gen-abs's Hebrew twin). **Scope discipline (per [[feedback-staged-paper-scope-discipline]]):** keep the paper's claim narrow — BoFM AICTP frame + the and/that quantification + the empty-frame definition — and treat Hebrew↔BoFM↔Greek convergence as the *motivating frame*, NOT a proven thesis. Three corpora "doing the same thing" needs same-yardstick measurement before it's a result, not an analogy (same trap as the hand-edit-gold-standard reflex, pointed at theory — see [[feedback-conformance-is-not-correctness]]).

**Offered but not yet built:** a one-page parallel-examples evidence sheet (B5 / AICTP / FEF side by side) for writing from. Build on request.
