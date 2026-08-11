---
name: feedback-never-handtype-greek-hebrew
description: Never hand-type Greek/Hebrew into canon/engine files; source tokens from clean occurrences and run the mixed-script scanner before committing
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87af68a0-0291-4910-962f-d0913b5722e6
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`bdb0f65c-d87a-4887-94b8-0f8e6422aa6d/fd46d550c221470e@v2`); state as of 2026-05-26 (snapshot mtime); possibly stale — re-verify before relying.

When editing files that contain Greek or Hebrew (atu-method/docs, per-corpus colometry-canon.md, the generator engines, commit messages), **never hand-type the non-Latin script**. Typing it character-by-character silently mixes 5-machinery/scripts — a Greek `ν` for Hebrew `נ`, a Latin `E` for Greek `ε` — producing corrupt tokens (`וַיֹּאμεр`, `ὥστE`). Stan: "that's unacceptable." In a fidelity-governing apparatus this is the cardinal error; in an **engine closed-list** a mixed-script lemma silently fails to match and breaks the rule with no error.

**Why:** the whole apparatus exists to preserve source-text fidelity. Hand-typing defeats it invisibly. (2026-05-26: three corruptions introduced this session — one shipped in a commit before being caught.)

**How to apply:**
1. **Source tokens from a clean in-corpus occurrence** (copy the existing string), or build from explicit codepoints — do not retype.
2. **Run the mixed-script scanner before any commit touching Greek/Hebrew:** `C:\tmp\scan_mixed_script.py <files>` — it flags any contiguous letter-run spanning >1 script (Greek/Hebrew/Latin/Cyrillic). Legit `δέ-headed` compounds are not flagged (hyphen breaks the run).
3. Repair corruptions programmatically (replace with a clean-sourced token), then re-scan to verify 0 — never hand-fix.

Ties to [[feedback_always_recommend_in_options]] and the source-text rules in ~/.claude/CLAUDE.md (NEVER modify vendored sources / preserve consonants+niqqud).
