---
name: lxx-english-brenton
description: "LXX-reader English layer = Brenton's Septuagint (public domain); NETS is rejected (OUP copyright)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`9d9683ed-2bb3-499d-8eb7-715c2bd3a063/66f2678dbc0f12dd@v2`); state as of 2026-05-29 (snapshot mtime); possibly stale — re-verify before relying.

The English layer for the LXX reader (readers-lxx) is **Brenton's Septuagint** (Lancelot C. L. Brenton, 1844) — fully **public domain**, freely redistributable. Decided 2026-05-29.

**Why not NETS:** the New English Translation of the Septuagint (Oxford University Press, eds. Pietersma & Wright) is **copyrighted**. The IOSCS posts a free PDF for personal/academic reading + limited quotation, but that is NOT a redistribution license — embedding it line-by-line as a public reader's English layer is "reproduction" and needs OUP permission. The program's non-commercial nature does not clear it (reproduction-in-a-derivative-work is the issue regardless). Same class as NIV/ESV.

**How to apply:** Brenton keeps the whole program consistently public-domain, matching the pattern — Douay-Rheims for the Vulgate, KJV for GNT/Tanakh. The per-ATU English-alignment pipeline built for the Vulgate DR (LLM-align each translation span to its source ATU sense-line, token-exact; see the Vulgate `build_content.py` + the `vulgate-dr-align` workflow) ports directly to Brenton. Acquire Brenton's PD text when the LXX-reader build begins. Relates to the LXX silver-convergence arc (gold morph corpus-wide + CATSS LXX↔MT alignment + gold Hebrew BHSA ATU projection, validated on the Gen+Ruth gold LXX syntax).
