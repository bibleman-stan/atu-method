---
name: atu-resolution-is-author-relative
description: ATU size is not fixed — it's the smallest chunk the AUTHOR intended; sophisticated authors build at finer resolution, so the colometric grid tracks authorial sophistication, not a lowest-common-denominator rule.
metadata:
  type: feedback
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`c62fff60-202d-4161-9983-60f9dc2b11a2/a219fd396bca686d@v3`); state as of 2026-06-01 (snapshot mtime); possibly stale — re-verify before relying.

The "atomic thought" criterion is NOT a fixed unit size. It is the smallest chunk
the author intended to be processed as one. Sophisticated authors (Luke, Paul, John
at their most crafted) build at a finer resolution than plainer narrators (Mark in
simpler scenes); the colometric grid must track the AUTHOR'S sophistication, not
impose a lowest-common-denominator rule. Finer-grained atomic units are licensed when
the intended audience has higher processing capacity (first-century hearers of
Luke-Acts could track interjectory beats as distinct units).

**Why:** Identified reviewing Acts 1:9, where a session had merged
"καὶ ταῦτα εἰπὼν βλεπόντων αὐτῶν ἐπήρθη" as a "double FEF." The real structure is
three beats: εἰπών (FEF frame) + βλεπόντων αὐτῶν (genitive absolute — interjectory
camera-shift to the disciples' POV) + ἐπήρθη (main verb). Merging absorbed the gen abs
and flattened Luke's three-beat rhythm. The point of the apparatus is *revealing*
rather than obscuring the author's voice.

**How to apply:** Track resolution to the author, not a flat rule. When merging FEF
chains, check each participle's CASE: nominative participles may merge with their main
verb; **genitive absolutes may NOT be merged into the chain** — they stand alone. The
concrete mechanical consequence — genitive absolutes always get their own line — is
already codified as **R19 (genitive absolute own line)** in
`atu-method/atu_method/infrastructure/validator_output.py` and as **LXX-B6** in
`atu-method/1-method/binding-rules-lxx.md`. This note preserves the *rationale* behind
R19, not the rule itself. Connects to [[feedback_external_unit_is_not_atu]] (gold/
external units are candidate-sources, never ATU criteria).

_Origin: rescued from the defunct `readers-nt` project memory during the
claude-consolidation cleanup (2026-06-01). readers-nt was the first GNT colometric
reader, since renamed/superseded to readers-gnt (the GitHub repo
`bibleman-stan/readers-nt` 301-redirects to `readers-gnt`); its in-repo method handoff
doc was removed in the transition, so this rationale survived only in that orphaned
note. Ideal long-term home is `atu-method/1-method/framework.md` §ATU definition._
