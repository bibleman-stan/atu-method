# canon-index.md — atu-method anchor navigation

**Permanent navigation artifact** for every §-anchor / named sub-clause / concept / doc the atu-method
methodology references. Hand-built first generation, 2026-06-06, established as part of the §-renumber
migration (Track B). Schema is permanent. Future regeneration via `scripts/build_canon_index.py`
(claudit productionization, pending). Until that exists, this file is hand-maintained.

The temporary `proposed_disposition` column exists ONLY for the in-flight §-renumber migration and
drops out of subsequent regenerations once Stan rules + claudit audits + execution lands.

---

## Schema

One row per anchor. Every cell carries a `file:line` receipt or an explicit absence-statement.

| Field | Values |
|---|---|
| **anchor** | The exact §-id or concept name as it appears in cited form (e.g. `§1.9`, `J3`, `M1 asymmetric-modifier`, `camera-angle`). |
| **type** | `section` / `sub-clause` / `concept` / `doc` |
| **authoritative home** | `<file>:<line-range>` of the canonical definition. |
| **status** | `live` (definition lives in unarchived canon) / `archived(_old)` (definition lives only under `_old/`) / `superseded→<anchor>` / `CONTESTED` (live-cited AND archived — needs Stan ruling) / `phantom(nowhere)` (cited but defined nowhere). |
| **live-successor** | The live anchor that substantively does the same work, OR `null` if none, OR `<see migration>` if pending. |
| **ALL consumers** | Every file:line that cites this anchor across `atu-method/docs/`, `atu-method/2-evidence/scholarship/`, `atu-method/memories/`, per-corpus colometry-canons (BoFM/GNT/Tanakh), reader-repo `scripts/` + `validators/` + `retraction-log.md`, workspace `~/CLAUDE.md`, user `~/.claude/CLAUDE.md`. Compact format: `<short-name>:<line>`. |
| **proposed_disposition (TEMP)** | Migration-only column: `supersede→<live anchor>` / `restore-universal→<doc/section>` / `per-corpus` / `fold→<section>` / `loud-CONTESTED-tombstone`. |
| **rationale (TEMP)** | One-sentence justification per the hard constraints below. |

A row reading `status=archived(_old) / live-successor=… / many live consumers` is a §7.3-style **phantom**
made visible. Stage 1 + Stage 2 Track A of the migration drained 45 such rows in the §7.x family + 4 in the
§0.x / §1.10 / §3.x families.

---

## Hard constraints honored

Verified across both claudit audits (`audit-percept-ruling-v1.json` + `audit-percept-ruling-v2-reaudit.json`)
and confirmed in-turn by Lane 1 receipts. Every disposition below honors these:

1. **`framework.md §2.3` DOES NOT EXIST.** Live framework §2 ends at §2.2 (line 117); next heading is §3 at line 118. Any "use §2.3" proposal is non-executable. (`framework.md` heading grep: only §2.1 + §2.2 under §2.)
2. **Complement-integrity / M2 live home is `framework.md:42` (§2.1), NOT §2.2.** §2.2:112 explicitly delegates single-complement binding to §2.1 ("Distinguish from a *single* subordinate complement, which binds under (A)").
3. **J1 → §2.2** (marker-licensed parallel subordinator-stack split, `framework.md:111-112`); **J3 → §2.1** (quotative frame stands as own ATU, `framework.md:42`).
4. **`framework.md:116` firewall EXCLUDES "parallelism class adjudication" as a primary break-license.** A universal §1.12 restoration would directly contradict this firewall — §1.12 IS parallelism-class adjudication.
5. **§1.12 and §1.13 have FULL self-contained per-corpus bodies.** BoFM canon TIER-0 (lines 116-117 + Moroni 10:8-17 sweep at line 45); GNT R28 §3.7 (lines 741-753, cited by R12/R13/R14). Restoring universal duplicates the per-corpus body.
6. **§1.9 (N=2 + N=3+ cliff) IS genuinely universal and missing.** Body at `_old/framework.md:282-297`; collision-adjudicator role, NOT a break-licensor (so the §2.2:116 firewall does not apply); cited 30+ times across BoFM + GNT scholarship.
7. **`_old/framework.md` §1.10 / §1.11 / §1.3a EXIST and are live-cited** (BoFM canon Tier 0 lines 114-115 + multiple memories). Cannot be silently dropped.
8. **Camera-angle §1.3 and M3 are LIVE-CITED in mechanized merge tests** (BoFM R27 condition-3 + GNT R25 condition-3; BoFM canon TIER 7 line 201 + R27 line 1959; BoFM canon TIER 4 line 152 for M3; GNT canon line 245 for M3). The demote-memory says camera-angle "is never the determinant" — directly contradicting the active R27/R25 condition. Supersede-to-memory breaks the rule's cited definition.
9. **Tanakh canon is a thin 55-line stub with NO §-citation reference table.** Only filename-routing prose at lines 11-16. Anything depending on "add to all three reader canon reference tables" must specify a concrete Tanakh mechanism.
10. **Sub-anchor granularity is load-bearing.** Live citers anchor to `§1.2.1` / `§1.2.2` / `§1.2.3` directly (R1.md:106, R13a.md:49, R11.md:47, R16.md:112, R10.md:17, R17.md:19) AND to NAMED-BUT-UNNUMBERED sub-clauses: J1 "compound-list break signals" (GNT canon:56 adds 5th), M1 "asymmetric-modifier sub-clause" (BoFM canon:747), §1.9 "N=3+ cliff SCOPE" predications-vs-objects distinction (R10.md:60). Restoring the umbrella without preserving sub-clauses verbatim strands the sub-cites.
11. **`framework.md §2` (Categories A/B/C) was MOVED to `§7.0` in Stage 1.** Citers to "framework.md §2 (Category B editorial-judgment)" now repoint to `§7.0`. Watch for old §2 conflations in pre-existing scholarship.
12. **Stranded cites span reader-repo `scripts/` + `validators/` + `retraction-log.md` + `atu-method/memories/`.** Migration destination rules must enumerate these, not just docs.
13. **Companion-doc pattern proven viable when indexed.** `binding-rules-hebrew.md` is cited in 28 places across 15 files including per-reader CLAUDE.mds — restoration into a new `atu-method/docs/<companion>.md` works IF added to `00-start-here.md` AND cited from per-corpus canons or their references.
14. **`structural-licenses.md` does NOT YET exist** and would need `00-start-here.md:25-30` per-language section entry to avoid born-orphan status at the docs-index level.

---

## The Index

### Part A — `§0.x` Preamble & Stance

| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| **§0.1** Mission | section | `_old/framework.md:13-23` | archived(_old) | `framework.md §1 Purpose` (lines 9-19) | 2-evidence/scholarship/bofm/R20.md:17,126 (repointed in Batch A1 to §1); BoFM canon:22-28 + GNT canon:25-43 pointer blocks ("§0") | **supersede→§1 Purpose** | Live §1 carries the apparatus-reveals-ATUs + DOES-NOT list verbatim-equivalent. R20 already repointed in Batch A1 (commit 86e1219). Pointer-block update needed: BoFM:22-28 + GNT:25-43 say "framework.md §0" — change to "framework.md §1". |
| **§0.2** Method (mission sense-driven, method syntax-constrained) | section | `_old/framework.md:25-29` | archived(_old) | `null` (PARTIAL: live §2 framing implies "thought" + "grammatical test as proxy" — relate but do NOT carry the mission/method asymmetry explicitly) | BoFM canon:22-28 + GNT canon:25-43 pointer blocks ("§0") | **fold→§1 Purpose** (add one-sentence note: "Mission is sense-driven, method is syntax-constrained — sense proposes, syntax filters") OR **loud-CONTESTED-tombstone** if Stan wants the asymmetry preserved as its own statement | Live §1 doesn't carry the meta-stance; live §2 frames the criterion but is operational. Folding adds ~25 words to §1 Purpose and preserves the working philosophy. Tombstone alternative if Stan wants the asymmetry distinct. |
| **§0.3** Pragmatic stance (no cognitive-theory derivation) | section | `_old/framework.md:31-33` | archived(_old) | `null` (semantic miss; methodology-position.md adjacent but does not state the disclaimer) | atu-method/memories/feedback_rhetoric_bandwagon.md (1 cite); BoFM canon:22-28 + GNT canon:25-43 pointer blocks ("§0") | **fold→§1 Purpose** (add "Stance" paragraph: "The methodology is a set of conventions reflecting what the apparatus reveals; it is not derived from a cognitive theory.") | Concept is alive in feedback_rhetoric_bandwagon and per-corpus pointer blocks. Folding to §1 keeps it framework-anchored. Live §1's prose already disclaims goal-creep ("does NOT" list); the stance addition is one-sentence. |
| **§0.4** Scope | section | `_old/framework.md:35-41` | archived(_old) | `framework.md §1 Purpose` (partial: NOT-list at lines 13-19) + `§2.1:101` (punctuation-zero-force) + `§2.2:116` (te'amim/genre exclusions) | 2-evidence/scholarship/bofm/R23.md:61 (repointed in Batch A1 to §1); BoFM canon:22-28 + GNT canon:25-43 pointer blocks ("§0") | **supersede→§1 Purpose** | R23 already repointed in Batch A1. The "DOES NOT govern punctuation/words/layout/external-overlays" claim is covered by live §1 NOT-list + §2.1 final paragraph + §2.2:116 explicitly. Pointer-block update needed. |

### Part B — `§1.x` Universal-principle scheme

| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| **§1.1** Generative principle (each proposition splits by default; bidirectional atomic-thought test) | section | `_old/framework.md:47-65` | superseded→`cross-corpus-principles.md §1.1` | `cross-corpus-principles.md §1.1` (reconciled-restore: candidate-ATU substrate + live KEEP-AS-IS default + R27/M-series merge-direction + R6/R7/R20/R21 split-license-identification) | 2-evidence/scholarship/bofm/R20.md:126, R21.md:21,130, R27.md:105,172, R6.md:17,30, R7.md:17,81, R5.md:147; atu-method/memories/feedback_atu_test_is_bidirectional.md, feedback_grammar_constrains_not_determines.md, feedback_rhetoric_figures_constrain_atu.md; BoFM canon:34 + GNT canon:48 pointer blocks; readers-gnt/scripts/audit_anaphoric_gen_abs_macula.py:6 | **supersede→`cross-corpus-principles.md §1.1`** (Stan 2026-06-06: option (a)) | Restored as candidate-ATU substrate statement, not as "split-by-default" doctrine. Live KEEP-AS-IS default is upheld; the principle re-frames what R6/R7/R20/R21 (license-identifiers) and R27/M-series (merge-direction-on-candidate-pair) operate on. |
| **§1.2** Syntax forbids splits (three closed-list ways) | section | `_old/framework.md:67-81` | archived(_old) | PARTIAL — see sub-anchors | 2-evidence/scholarship/bofm/R12.md:149, R10.md:132, R5.md:147 ("syntax forbids splits"); BoFM canon:34 + GNT canon:48 pointer blocks; readers-tanakh/scripts/archive/apply_formula_integrity_merge.py:2; atu-method/memories/feedback_grammar_constrains_not_determines.md | **see sub-anchors §1.2.1 / §1.2.2 / §1.2.3** | Umbrella has no body of its own — function lives in the three sub-categories. Disposition is per-sub-anchor. |
| **§1.2.1** Layer 1 mid-phrase prohibitions | sub-clause | `_old/framework.md:71-72` | archived(_old) | `null` (no named live successor; per-corpus break-legality tables host) | 2-evidence/scholarship/bofm/R13a.md:49, R11.md:47, R16.md:112, R10.md:17, R15.md:136 ("Layer 1 mid-phrase prohibitions") | **per-corpus** (canonical home: `readers-<corpus>/data/syntax-reference/<lang>-break-legality.md`) + leave one-line summary in restored `structural-licenses.md §1.2 syntax-as-constraint` | The three closed-list categories operate AS A FAMILY; Layer-1 prohibitions are per-language by definition (per old §1.2 itself: "specific prohibitions are language-specific"). Citers (R13a/R11/R16/R10/R15) cite framework §1.2.1 but rule-content lives per-corpus. Update citers to point at `structural-licenses.md §1.2.1` (one-line per-corpus delegation) PLUS the per-corpus break-legality table. |
| **§1.2.2** Layer 3 complement integrity | sub-clause | `_old/framework.md:73` | archived(_old) | `framework.md §2.1:42` (verbatim: "a verb whose content follows as a clausal complement ... binds its complement into one ATU ... The verb's open valency is filled by the complement; it does not stand alone. So: clausal complement → matrix binds") | 2-evidence/scholarship/bofm/R17.md:19, R26.md:165 ("§1.2.2 syntax forbids splits — complement integrity") | **supersede→§2.1:42** | Live §2.1:42 carries verbatim equivalent. R17/R26 cites repoint to §2.1 valency note. NOTE: claudit v1 + v2 BOTH got this wrong — v1 pointed at §2.1 with no named successor (true at that moment because complement-integrity wasn't named) ; v2 pointed at §2.2 (INVERSION — §2.2 is the productive break-licensor, not the bind-mechanism). The correct target is §2.1:42 verbatim. |
| **§1.2.3** Layer 3 formula integrity | sub-clause | `_old/framework.md:75` | archived(_old) | `null` (no named live successor; per-corpus formula bodies host) | 2-evidence/scholarship/bofm/R1.md:69,106 (sole live citer: "framework.md §1.2.3 formula integrity") | **per-corpus** + restored stub in `structural-licenses.md` pointing per-corpus | "BoFM has *And it came to pass*; Tanakh has wayyiqtol formulae; GNT has *καὶ ἐγένετο*" — closed lists are per-corpus by §1.2's own statement. R1 (BoFM AICTP) is the canonical instance; cite repoints to `BoFM canon §5 R1` directly. |
| **§1.3** Camera-angle test (DEPRECATED 2026-05-13 → EXCISED 2026-06-06) | section | `_old/framework.md:83-89` (archived; not restored) | **excised — corpus-side refactor required** | NO live successor; concept fully retired | 2-evidence/scholarship/bofm/R27.md:105,172, R25.md:131; BoFM canon:34 + GNT canon:48 pointer blocks; BoFM canon:201 (TIER 7), canon:1959 (R27 condition 3); GNT canon:1171,1181 (R25 condition 3); feedback_camera_angle_diagnostic_demote.md | **excise** — drop camera-angle as a heuristic across the entire stack (Stan 2026-06-06: option (b) — "camera angle is NOT a useful nor defensible heuristic"). **Batch B2 work:** remove "no camera shift" condition from R27 (BoFM) + R25 (GNT); audit corpus-wide rule-output deltas; update scholarship + canon + demote-memory to reflect full retirement. | Camera-angle as a heuristic for identifying ATU boundaries is rejected. R27/R25 condition-3 disposition (drop entirely vs. replace with §2.1-bidirectional-test corollary) handled in B2 halt for Stan. |
| **§1.3a** Rhetoric figures constrain (default dispositions per figure) | section | `_old/framework.md:89-104` | archived(_old) | `null` (concept survives in `atu-method/memories/feedback_rhetoric_figures_constrain_atu.md` and per-corpus canon Tier 0 mentions; framework has no successor) | atu-method/memories/feedback_rhetoric_figures_constrain_atu.md (6 cites); feedback_rule_proposal_gates.md, feedback_no_fake_dilemmas.md; BoFM canon Tier 0 mentions | **restore-universal→`structural-licenses.md` §1.3a** (concept is cross-corpus by construction: figures-constrain-not-determine is a methodological asymmetry that applies to any corpus) | The memory is the working home but a memory is not a methodology section — restored §1.3a anchors the concept as canon-level + the memory is its scholarship companion. Companion-doc index entry required. |
| **§1.4** Five Structural Justifications | section | `_old/framework.md:106-164` | archived(_old) | PARTIAL — see J1-J5 sub-anchors | 2-evidence/scholarship/bofm/R20.md:126, R27.md:172 (multiple); BoFM canon:34 + GNT canon:48 pointer blocks ("J1-J5"); BoFM canon:487,1581,2056,2653,2727 (granular J/M references); GNT canon:56-69,130-136,183,227-259 | **see sub-anchors J1–J5** | Umbrella collects 5 distinct justifications; each Ji needs its own disposition. |
| **J1** Formally-marked parallel series | sub-clause (under §1.4) | `_old/framework.md:112-126` | archived(_old) | `framework.md §2.2:111-112` (parallel subordinator-stack split, marker-licensed) — PARTIAL: only the "marked by a repeated subordinator" variant; the broader J1 ("all formally-marked parallel series") has no live successor | 2-evidence/scholarship/bofm/R10.md:132, EP-5.md:174 ("J1"); BoFM canon:487, GNT canon:56-69 (J1 5-signal extension); R20.md:126 | **supersede→§2.2:111-112** for marker-licensed-subordinator-stack variant + **restore-universal→`structural-licenses.md` §1.4 J1** for the broader "formally-marked parallel series" body (covers correlatives, polysyndetic-and, language-specific equivalents) | §2.2 handles the marker-licensed sub-case (the case where the marker IS the license); but J1 in scholarship refers to the broader principle (e.g. R10's "compound-list-break-signals sub-rule" governing coordinate-object exclusion). §2.2:116 firewall blocks parallelism-class as primary license, but J1's compound-list-break-signal sub-clause (4 signals; GNT adds 5th at canon:56) is a sub-clause INSIDE the criterion, not a primary licensor. Preserve verbatim in `structural-licenses.md`. |
| **J1 "compound-list break signals" sub-clause** (4-signal list; GNT extends to 5th) | named-but-unnumbered sub-clause | `_old/framework.md:116-123` | archived(_old) | `null` | BoFM canon:487, GNT canon:56-69 (GNT 5th signal "marked-coordinator climactic emphasis"); 2-evidence/scholarship/bofm/R10.md:132 | **preserve verbatim in `structural-licenses.md §1.4 J1`** | Stan's hard constraint: "Preserve sub-anchors verbatim ... J-signals". GNT's 5th-signal extension proves the body needs per-corpus extension mechanism. |
| **J2** Portrait accumulation | sub-clause (under §1.4) | `_old/framework.md:127-129` | archived(_old) | `null` | No active live citers found across full sweep (concept named-only in §1.6 four-forces summary recap) | **restore-universal→`structural-licenses.md` §1.4 J2** (low-volume but methodology-load-bearing — defines an exception class) OR **loud-CONTESTED-tombstone** if Stan agrees concept can be dropped | J2 isn't actively cited but is part of the closed-list J1-J5 architecture. Dropping J2 leaves an unnumbered hole. Conservative path: restore minimally. |
| **J3** Speech-act announcement | sub-clause (under §1.4) | `_old/framework.md:131-135` | archived(_old) | `framework.md §2.1:42` (verbatim: "a quotative frame introducing distinct direct discourse ('and he said:') ... PASS: the frame is a complete cataphoric announcement and the quoted discourse is its own ATU"); plus `§2.1:44` (first-person performative "I say to you" binds) | 2-evidence/scholarship/bofm/EP-3.md (J3-routes); BoFM canon:40-42 (Verily formula 32 instances; saith-the-Lord parenthetical); GNT canon:130 | **supersede→§2.1:42** | Live §2.1:42 carries verbatim equivalent (quotative-frame-stands + first-person-performative-binds). Citers repoint to §2.1. Per-corpus J3-named-patterns (BoFM Verily formula, GNT R-rules) cite per-corpus canons directly. |
| **J4** Classical commata | sub-clause (under §1.4) | `_old/framework.md:137-139` | archived(_old) | `null` | Minimal live citers (concept named in §1.6 recap only) | **restore-universal→`structural-licenses.md` §1.4 J4** OR **loud-CONTESTED-tombstone** | Same shape as J2. Conservative: restore as part of structural-licenses.md companion. |
| **J5** Substantive adjunct as own focus | sub-clause (under §1.4) | `_old/framework.md:141-164` | archived(_old) | `null` | 2-evidence/scholarship/bofm/EP-1.md:153 (MALFORMED — says "§1.5 J5"; J5 belongs under §1.4 NOT §1.5; repair: "§1.4 J5"); BoFM canon:43 (Alma 52:18 year-formula); GNT canon:132-136 (canonical cases + gen-abs retirement note); R26.md cites | **restore-universal→`structural-licenses.md` §1.4 J5** + **REPAIR `EP-1.md:153` malformed cite "§1.5 J5" → "§1.4 J5"** as part of this batch | Substantial body (24 lines in _old), specific exclusion sub-clauses ("degree quantifiers excluded", "same-slot vs distinct-slot diagnostic"), per-corpus canonical cases. Preserve verbatim. Malformed cite is documented constraint #10 and MUST be repaired. |
| **§1.5** Four Merge-Overrides | section | `_old/framework.md:166-244` | archived(_old) | PARTIAL — see M1-M4 sub-anchors | 2-evidence/scholarship/bofm/R10.md:132, R5.md:147, EP-1.md, R12.md:149, R20.md:126 (multiple); BoFM canon:34 + GNT canon:48 pointer blocks; BoFM canon:148-156 (TIER 4 catalog); GNT canon:111-128,227-259 | **see sub-anchors M1–M4** | Same as §1.4 — umbrella collects 4 distinct overrides. |
| **M1** Gorgianic bonded pair | sub-clause (under §1.5) | `_old/framework.md:176-203` | archived(_old) | `null` (live framework has no named bonded-pair override; §2.1 bidirectional test handles via "single cognitive bite" implicitly but not by name) | 2-evidence/scholarship/bofm/R12.md:149, R5.md:147, EP-5.md (multiple), R22.md:168; BoFM canon:38-39 (verb-pair list), TIER 4 line 148-156; GNT canon:111-128 (75/78 corpus survey) | **restore-universal→`structural-licenses.md` §1.5 M1** + preserve sub-clauses (asymmetric-modifier, N=2-only caveat, tie-breaker with J1) verbatim | Cross-corpus principle with per-corpus bodies BUT framework anchor is needed for the N=2 Adjudication interaction (which IS universal — see §1.9). Companion home keeps M1 ↔ §1.9 ↔ J1 N=3+ cliff legible together. |
| **M1 "asymmetric-modifier sub-clause"** (joint-attachment test) | named-but-unnumbered sub-clause | `_old/framework.md:201` | archived(_old) | `null` | BoFM canon:747 ("M1 asymmetric-modifier sub-clause (framework §1.5 M1)") | **preserve verbatim in `structural-licenses.md §1.5 M1`** | Stan's hard constraint #10. BoFM canon cites by name; sub-clause is load-bearing for R5-like asymmetric-pair cases. |
| **M2** Verb-object clause-nucleus bond | sub-clause (under §1.5) | `_old/framework.md:205-209` | archived(_old) | `framework.md §2.1:42` (clausal complement → matrix binds — the live home claudit v1 + v2 BOTH got wrong) | 2-evidence/scholarship/bofm/R10.md (multiple), R26.md:165; BoFM canon:148-156 ("M2 = R17 alias"); GNT canon:237 ("M2 verb-object bond"); Tanakh H7 | **supersede→§2.1:42** | M2 is explicitly an alias for per-corpus complement-integrity (BoFM R17, GNT R8, Tanakh H7). Live §2.1:42 + §2.2:112 carry the bind mechanism + the §2.2 delegation. Same destination as §1.2.2. |
| **M3** Bare-governor indivisibility | sub-clause (under §1.5) | `_old/framework.md:211-230` (archived; not restored) | **excised — corpus-side refactor required** | NO live successor named M3 (general principle subsumed by §2.1 bidirectional test; bare-trailing-participials extension disposition TBD) | 2-evidence/scholarship/bofm/R19.md; BoFM canon:152 (TIER 4) + canon:1581; GNT canon:237,245; R20.md:126; feedback_atu_test_is_bidirectional.md + feedback_rule_proposal_gates.md | **excise** — drop M3 references across the stack (Stan 2026-06-06: option (b) — "our doctrine should be correct and non-ambiguous, not document evolution"). **Batch B3 work:** general bare-governor subsumed into §2.1; bare-trailing-participials extension (4 carve-outs at _old:223-228) disposition halt for Stan — fold into §2.1 implicit / re-author as per-corpus rule / drop entirely. | The memory's deprecation upheld. Per-corpus M3 references retired. The 4 carve-outs (stack-cap / coord-list member / antecedent-locality fail / fronted-position participial) are genuine operational content that must land somewhere — Stan ruling on B3 decides where. |
| **M4** Fragmented atomic thought-unit | sub-clause (under §1.5) | `_old/framework.md:232-244` | archived(_old) | `null` (live framework has no named fragmented-ATU override; §2.1 bidirectional test implicit but not by name) | 2-evidence/scholarship/bofm/M4-BoFM-1.md, 2-evidence/scholarship/gnt/M4-GNT-1.md (per-corpus full bodies); BoFM canon:148-156 (TIER 4) + canon §5 R-entries; GNT canon:251-259 + §3.18 line 1318 | **restore-universal→`structural-licenses.md` §1.5 M4** (covers M4-precedence-over-J1/J5, prospective-not-retroactive scope) + per-corpus M4-BoFM-1 / M4-GNT-1 cite the universal | Per-corpus instances are full scholarship bodies but the universal SCOPE clauses (M4 doesn't fire on J1 N≥3 series; M4 doesn't fire on J5 cases; M4 is prospective-not-retroactive) are framework-level and cross-corpus. Companion home preserves these scope clauses. |
| **§1.6** Summary "four forces" | section | `_old/framework.md:246-254` | dropped (recap-only, no normative content; followed §1.3 excision) | NO live successor (the underlying §1.1-§1.5 forces have individual dispositions) | BoFM canon:34 + GNT canon:48 pointer blocks; demote-memory:26,35 | **drop entirely** (Stan 2026-06-06: §1.6 followed §1.3 excision; recap-only table with no surviving normative content) | The four-forces table was a recap. With camera-angle excised, the surviving forces (generative §1.1 → restored, syntax §1.2 → per-corpus + §2.1, merge-overrides §1.5 → restored M1/M4, rhetoric §1.3a → restored) each land in their own row in cross-corpus-principles.md. No summary table needed. |
| **§1.7** Decision procedure (5-step) | section | `_old/framework.md:256-266` | archived(_old) — body has STALE step-1 ("Default: merge" vs live KEEP-AS-IS) | `null` (live decision flow is implicit in §2.1 + §2.2 but not numbered as a procedure) | 2-evidence/scholarship/bofm/R28.md (sole rot-list cite); BoFM canon:34 + GNT canon:48 pointer blocks ("the five-step decision procedure") | **supersede→§2.1 + §2.2** with explicit "the live decision flow is §2.1 bidirectional test → §2.2 marker license check" repoint note; remove §1.7 from pointer blocks. R28 cite updated. | Old §1.7's step-1 default is INVERTED against live KEEP-AS-IS — the procedure can't be silently retained. Live §2.1 + §2.2 IS the live decision flow; numbering it 1-5 again would re-state already-canonical content. Single citer (R28) is mechanical. |
| **§1.8** Application order (Step 0 input filter through Step 4 diagnostic) | section | `_old/framework.md:268-280` | archived(_old) | `null` (live framework has no application-order specification; live §2.1+§2.2 ordering is implicit) | BoFM canon:2307,2402,2500,2609 (cite "§1.8 Step 4" by step number); GNT canon:2316; demote-memory ("§1.8 Step 4 — Diagnostic"); §1.8 body internally references §1.9/§1.13/M-series BY STEP NUMBER (binds the whole §1.x architecture) | **restore-universal→`structural-licenses.md` §1.8 application-order** (preserve verbatim) | §1.8 IS the deterministic step-machine — it's the GLUE binding §1.9 + §1.13 + M-series + camera-angle reference. Per-corpus canons cite "Step 4" by number. Demoting to a footnote loses the step-ordering home (claudit v1's correct catch). Companion-doc preservation aligns with §1.9 restoration target. |
| **§1.9** N=2 Adjudication + N=3+ cliff (Helaman 3:16) | section | `_old/framework.md:282-297` | archived(_old) | `null` (collision-adjudicator role, not break-licensor — §2.2:116 firewall does NOT apply; no live §-coverage) | 60+ live citers including: 2-evidence/scholarship/bofm/R5.md:136,147, R10.md:60,132, R12.md:106,111,149, R15.md:136, R17.md, R18.md, R18a.md:56,119, R21.md, R22.md:108,110,168, R28.md, EP-5.md:50,108,174, M4-BoFM-1.md; 2-evidence/scholarship/gnt/M4-GNT-1.md, R25.md, R28-ext.md; BoFM canon:185-194 (TIER 6 N=2 body) + 222-228 (§3.5.2 N=2 vs N=3+ cliff) + 487,560,636,642,898,1172,1718,2199,2553,2604,2605,2607,2634 (granular cross-refs); GNT canon:106-109 (corpus cases), :183 ("§1.4-§1.9"), :2327-2346 (history); atu-method/memories/feedback_rule_proposal_gates.md; readers-bofm/validators/colometry/validate_rule_07_ud.py:161 ("§1.5 M4") + validate_rule_06_ud.py:104 ("R6/R7 yield per §1.5 M4") | **restore-universal→`structural-licenses.md` §1.9** (definitively cross-corpus per Lane 1's "N=2 + N=3+ cliff" verified-constraints; cross-corpus collision-adjudicator with no break-license character — §2.2:116 firewall doesn't apply) | The strongest restore-universal case: high cite density (60+ files), cross-corpus instantiation (BoFM Helaman 3:16, GNT Matt 22:30 / 2 Cor 11:27), function is criterion-layer not break-license-layer (so §2.2:116 firewall is not in play). BoFM TIER 6 body operationalizes; framework anchor states. Per claudit v2 audit: §1.9 stands independently from §1.12/§1.13 (no triad-framing receipts). |
| **§1.9 "N=3+ cliff SCOPE" sub-clause** (predications-vs-objects distinction) | named-but-unnumbered sub-clause | `_old/framework.md:297` | archived(_old) | `null` | 2-evidence/scholarship/bofm/R10.md:60 ("R10's interaction with framework §1.9's N=3+ cliff: cliff is scoped to coordinate PREDICATIONS, NOT to coordinate OBJECTS"); R18a.md:119 | **preserve verbatim in `structural-licenses.md §1.9`** | Stan's hard constraint #10. R10's SCOPE distinction is load-bearing for compound-list-object handling. |
| **§1.10** Punctuation is not a break signal | section | `_old/framework.md:299-309` | archived(_old) | `framework.md §2.1:101` ("Punctuation has ZERO force — including parser decisions conditioned on it") | 2-evidence/scholarship/bofm/R19.md:31,134, EP-1.md:40,71,153 (repointed in Batch A1 commit 86e1219); BoFM canon:34 + GNT canon:48 pointer blocks ("punctuation-not-a-signal stance"); atu-method/memories/feedback_punctuation_not_evidence.md | **supersede→§2.1:101** (citers repointed in Batch A1; pointer-block update outstanding) | Stage 1 / Batch A1 already repointed the 5 scholarship cites. Pointer-block update from BoFM:34 + GNT:48 still needed: change "punctuation-not-a-signal stance ... §1" → "punctuation-zero-force ... §2.1". |
| **§1.11** Versification is not a break signal | section | `_old/framework.md:311-313` | archived(_old) | `framework.md §3 v1.6 cross-verse-continuity` (lines 156-176) covers the concept; v1.6 EXPLICITLY frames versification as overlay, equivalent to §1.10 punctuation framing | BoFM canon:34 + GNT canon:48 pointer blocks ("versification-not-a-signal stance"); no other live citers | **supersede→§3 v1.6** (with pointer-block update) | v1.6 introduces verse boundaries as "versification artifacts, not parse-derivable features" — same conceptual move §1.11 made. Pointer-block update needed (same edit as §1.10's). |
| **§1.12** Parallel-List Uniformity Principle | section | `_old/framework.md:313-323` | **CONTESTED** | `null` (would collide with §2.2:116 firewall if restored universal; BoFM has full live body) | BoFM canon:45 + 117 (TIER-0 body + Moroni 10:8-17 canonical case), :172 (R7 yields), :560,636,642,2607 (granular cross-refs); GNT canon:48 (pointer-only; no body); _old/rule-equivalence-map.md:25 (Tanakh H17 = Parallel-List Uniformity instance — duplication risk includes Tanakh); 2-evidence/scholarship/bofm/R6.md, R7.md, R10.md (yields-to references) | **per-corpus** (canonical home: BoFM canon TIER-0 + Moroni 10:8-17; GNT pointer in canon:48 either rewritten to BoFM-canonical or fold into GNT-local body; Tanakh H17 stays as Tanakh-local instance) — REMOVE §1.12 line from BoFM:34 + GNT:48 pointer blocks per claudit's "Pointer-block claim is the error" finding. NO universal restoration because (a) §2.2:116 firewall ("framework does NOT include ... parallelism class adjudication ... as primary licenses") would collide and (b) BoFM body is full and self-contained. | The cleanest per-corpus case. Hard constraint #4 + #5 directly apply. §1.12 is a WITHIN-LIST UNIFORMITY rule operating AFTER members are split, not a break-licensor — but at universal-companion-doc level it would be CITED CROSS-CORPUS, elevating it to primary status that the firewall excludes. Better: per-corpus instantiation cites the canon-local body. |
| **§1.13** Authorial Asymmetry overrides editorial symmetry | section | `_old/framework.md:331-337` (SUBSTANTIVE body — refutes v1's "never had a body" claim) | **CONTESTED** | `null` (per-corpus bodies exist; no live framework §-coverage) | BoFM canon:44 (canonical case 2 Nephi 9:27-38 wo-series), :116 (TIER 0 reference) — thin instantiation; GNT canon:741-753 (R28 §3.7 FULL self-contained Principle body cited by R12/R13/R14); 2-evidence/scholarship/bofm/R28.md (5 cites + collision with R28 ID), 2-evidence/scholarship/gnt/R28-ext.md; readers-gnt/private/01-method/check_canon_alignment.py:339-348 (R28 rule_type='Principle', validator=None — no per-line check; demoting framework §1.13 cannot break a validator) | **per-corpus** (live homes: GNT canon §3.7 R28 lines 741-753 is the substantive body; BoFM canon TIER 0 is the lighter instantiation). REMOVE §1.13 line from BoFM:34 + GNT:48 pointer blocks. R28 ID-collision (§1 principle vs §5 rule) is a separate per-corpus cleanup task. | Stan's hard constraint #5 directly applies: per-corpus bodies are full and self-contained. Restoring universally creates two homes for one principle (claudit v2 audit caught this). GNT R28 validator is `None` (Principle, not per-line) — no cross-corpus check breaks. The §1.12 ↔ §1.13 pairwise precedence interaction lives in the BoFM TIER 0 wiring + GNT R28 cited-by-R12/R13/R14 — handled at per-corpus layer. |

### Part C — Doc-level rows (selected; full doc inventory deferred to build_canon_index.py first run)

| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| `framework.md` | doc | itself | live | n/a | universal — every per-corpus canon + scholarship + memories + reader CLAUDE.md | n/a | The atu-method canonical methodology spec. |
| `_old/framework.md` | doc | itself | archived | `framework.md` (post-2026-05-18 rewrite) | `_old/` directory + per-concept dispositions above | n/a | Archived 2026-05-18 mechanical-first rewrite. Sole source for §0.x / §1.x bodies until migration completes. |
| `_old/change-protocol.md` | doc | itself | archived | `framework.md §7` (Stage 1 extracted 2026-06-05, commit 93d67f5) | resolved by Stage 1 | n/a | Stage 1 §7.x migration sourced from this archived doc. |
| `binding-rules-hebrew.md` | doc | itself | live | n/a | 28 occurrences across 15 files (proof-of-concept that companion docs survive when indexed) | n/a | Sister catalog precedent for the proposed `structural-licenses.md`. |
| `binding-rules-lxx.md` | doc | itself | **PARKED** (committed 2026-06-06, commit ba04629; smoke-test artifact per Track A4) | n/a | 00-start-here.md:28 (Track A4 fix) | n/a | Smoke-test artifact, pipeline parked 2026-05-27 per banner. |
| `cross-corpus-principles.md` (renamed from "structural-licenses.md" 2026-06-06 per Stan) | doc | `atu-method/1-method/cross-corpus-principles.md` (NEW 2026-06-06, B1; uncommitted on disk pending claudit audit) | **live (uncommitted)** | n/a | `00-start-here.md` lines 19-21 (Methodology specification section, NEW entry); `readers-tanakh/private/01-method/colometry-canon.md:13` (NEW row in filename-routing table — gitignored, local-only); per-corpus canon pointer-block updates pending B4 | n/a (created in B1) | Final name "cross-corpus-principles.md" — more accurate than "structural-licenses" because hosts §1.9 N=2 collision-adjudicator which isn't a license. Hosts §1.1 reconciled, §1.3a, §1.4 J1/J2/J4/J5, §1.5 M1/M4, §1.8 application-order, §1.9 N=2 + N=3+ cliff. EXCLUDES §1.3 camera-angle + §1.5 M3 per Stan 2026-06-06 excision rulings. |
| `glossary.md` | doc | itself | live (stale per forensic audit) | n/a | framework.md, apparatus.md, architecture.md, _index.md | needs `§7.0 Categories A/B/C` reference update (claudit findings 2026-06-05) | Out of §-renumber scope for this halt; flagged for next-cycle. |
| `methodology-position.md` | doc | itself | live | n/a | framework.md L249, apparatus.md, toolset-architecture.md, _index.md | adjacent to §0.3 disposition but NOT the §0.3 host | LDHB / discourse-grammar relationship; not the pragmatic-stance host. |

### Part C-bis — `framework.md §7.x` Change-discipline family (post-Stage 1)

All §7.x sections are LIVE in `framework.md` post-Stage 1 (commit 93d67f5, 2026-06-05). Sourced
verbatim from archived `_old/change-protocol.md:10-103` plus §7.0 from `_old/framework.md:343-361`
(Categories A/B/C) plus §7.9 preserving prior live §7 binding-rule design checklist.

| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| **§7.0** Categories A / B / C | section | `framework.md:237-256` | **live** | n/a (this IS the live anchor) | Repointed from old `framework.md §2` in Stage 1; consumers include 2-evidence/scholarship/bofm/EP-1.md:153 (after Batch A1 edit "§2 (Category B editorial-judgment)" → "§7.0 (Category B editorial-judgment)"); 4 EP-rules + multiple R-rules reference Category A/B/C semantics | n/a | Stage 1 (commit 93d67f5) extracted from `_old/framework.md:343-361` per Amendment 1 to resolve dangling "Category A/B/C" cross-refs in §7.3 #4 / §7.4 first bullet / §7.8 #3. |
| **§7.1** Authority | section | `framework.md:257-260` | **live** | n/a | (no rot-list cites; structural-anchor only) | n/a | Stage 1 extraction from `_old/change-protocol.md:10-12`. |
| **§7.2** Proposal requirements | section | `framework.md:261-277` | **live** | n/a | 2-evidence/scholarship/bofm/R20.md:33 ("adding a connective requires worked corpus evidence per §7.2") + 1 other rot-list cite | n/a | Stage 1 extraction; 7-clause discipline including defensibility-capture mandate (WHY / HOW WE KNOW / SCOPE). |
| **§7.3** Mandatory-audit triggers (12 categories) | section | `framework.md:278-298` | **live** | n/a (this IS the live anchor — corrects pre-Stage-1 phantom status) | 36 cites resolved in Stage 1 across CLAUDE.md, MEMORY.md, scholarship, memories, ~/CLAUDE.md, hard-constraints sections in this canon-index | n/a | Stage 1 extraction. The single most-cited canon anchor (per Lane 1 rot-list); status correction per claudit 2026-06-06: now LIVE not phantom. |
| **§7.4** Audit-skippable categories | section | `framework.md:299-307` | **live** | n/a | retraction-log-protocol.md + Batch A1/A2/A3/A4 commit-message audit-evidence declarations | n/a | Stage 1 extraction; complement to §7.3 (when audit is mandatory vs. skippable). |
| **§7.5** Audit-evidence in commit messages | section | `framework.md:308-316` | **live** | n/a | feedback_claude_commits_and_pushes.md + feedback_never_skip_audit_gate.md + all Stage 1 / Track A commit messages | n/a | Stage 1 extraction; operationalizes §7.3/§7.4 at commit-time discipline. |
| **§7.6** Self-test before commit | section | `framework.md:317-326` | **live** | n/a | (no direct rot-list cites; structural-anchor; consumed by §7.5 commit-message construction) | n/a | Stage 1 extraction; 5-question pre-commit checklist. |
| **§7.7** Self-consistency audit trigger | section | `framework.md:327-336` | **live** | n/a | feedback_compaction_resume_protocol.md (1 cite) | n/a | Stage 1 extraction; fires when ≥2 new canon subsections/rules added in one session. |
| **§7.8** Proposed-rule adoption protocol | section | `framework.md:337-351` | **live** | n/a | 2-evidence/scholarship/bofm/R27.md:172 + R28.md (multiple) + feedback_rule_proposal_gates.md + feedback_three_anti_default_factors.md (4 rot-list cites) | n/a | Stage 1 extraction; ≥80% clean-categorization adoption criterion. Includes Amendment 1 string change "Category A per §2" → "Category A per §7.0". |
| **§7.9** Binding-rule design checklist (per-rule additions) | section | `framework.md:352-362` | **live** | n/a | (no direct cites; preserves prior live `framework.md §7` 4-step checklist — BHSA features / validated chapter set / cold-eye-match / binding-rules-hebrew.md discipline) | n/a | Stage 1 PRESERVED — not extracted from archive; was the prior live `framework.md §7` 10-line section before Stage 1's §7.x expansion. Kept so the binding-rule-specific discipline is not lost in the §7.x migration. |

### Part D — Concept-level rows (named concepts without §-id)

| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| **ATU vs. rhetorical/discourse lens distinction** | concept (methodology principle) | `atu-method/memories/feedback_atu_and_rhetorical_lenses_distinct.md` (NEW 2026-06-06) | live | n/a | `cross-corpus-principles.md §0.1` (lens scope); anchor-paper future use; per-verse audits when rhetorical instinct ≠ ATU disposition (Alma 34:16 anchor case) | **live — co-shipped with B1** | Stan's articulation 2026-06-06: ATU and rhetorical/discourse lenses are different criteria on the same text; naming the distinction is itself a methodology contribution. Memory captures the principle + how-to-apply + Alma 34:16 anchor + future-paper framing against Chafe/Korpel-Oesch/Cresti/Hannay-Kroon/discourse-grammar precedent. Cross-corpus-principles.md §0.1 (lens scope) is the canonical-companion brief surface; the memory is the full statement. |



| anchor | type | authoritative home | status | live-successor | ALL consumers (file:line) | proposed_disposition | rationale |
|---|---|---|---|---|---|---|---|
| **camera-angle test** | concept | `_old/framework.md §1.3:83-89` + `atu-method/memories/feedback_camera_angle_diagnostic_demote.md` (deprecation memo) | **CONTESTED** | see §1.3 row | 2-evidence/scholarship/bofm/R27.md (condition 3); 2-evidence/scholarship/gnt/R25.md (condition 3); BoFM canon TIER 7 line 201 + R27 line 1959; GNT canon:1171/1181 | **loud-CONTESTED-tombstone — joint Stan ruling with §1.3 and §1.6** | See §1.3 + §1.6 entries above. |
| **N=2 Adjudication Principle** | concept (= §1.9 named form) | see §1.9 row | archived(_old) | per §1.9 disposition | per §1.9 consumers | per §1.9 disposition | The named-form alias for §1.9. |
| **N=3+ cliff (Helaman 3:16)** | concept (= §1.9 named form) | see §1.9 row | archived(_old) | per §1.9 disposition | per §1.9 consumers | per §1.9 disposition | The named-form alias for §1.9 second clause. |
| **Parallel-List Uniformity** | concept (= §1.12 named form) | see §1.12 row | live (per-corpus) / CONTESTED at framework level | per §1.12 | per §1.12 | per §1.12 | The full-prose form of §1.12 — same disposition. |
| **Authorial asymmetry / Textual asymmetry** | concept (= §1.13 named form) | see §1.13 row | live (per-corpus) / CONTESTED at framework level | per §1.13 | per §1.13 | per §1.13 | "Textual asymmetry overrides editorial symmetry" is the GNT R28 phrasing — semantically equivalent to "authorial asymmetry overrides editorial symmetry". |
| **Helaman 3:16 cliff precedent** | concept (BoFM-specific instance of §1.9 N=3+ cliff) | BoFM-specific | live | per §1.9 disposition | 2-evidence/scholarship/bofm/R12.md (multiple); per-corpus precedent | n/a | BoFM-only precedent verse for the N=3+ cliff. Cross-corpus extension would name corpus-specific precedents. |
| **Moroni 10:8-17 spiritual-gifts case** | concept (BoFM-specific instance of §1.12) | BoFM-specific | live | per §1.12 disposition | 2-evidence/scholarship/bofm canon:45 ("3 outliers per 2026-04-26 sweep; merge-dominant treatment") | n/a | BoFM-only canonical case for §1.12. |
| **2 Nephi 9:27-38 wo-series** | concept (BoFM-specific instance of §1.13) | BoFM-specific | live | per §1.13 disposition | BoFM canon:44 | n/a | BoFM-only canonical case for §1.13. |
| **§3.21** (claudit-flagged) | phantom anchor | NONE | **phantom(nowhere)** — external Quirk/CGEL citation, NOT internal §-id | n/a | 2-evidence/scholarship/bofm/R10.md:31 ("CGEL Ch. 14 ... coordination-under-shared-predicator") | NO ACTION — claudit hardens scanner per their note | Scanner false-positive over external publication §-id. |

---

## Disposition rationales (extended)

### Stan's rulings (2026-06-06)

| § | Ruling | Disposition |
|---|---|---|
| §1.1 generative principle | (a) supersede with reconciliation | New `cross-corpus-principles.md §1.1`. Candidate-ATU substrate is restored; live KEEP-AS-IS default upheld. |
| §1.3 camera-angle | (b) corpus-side refactor — excise | Camera-angle excised from doctrine; R27/R25 condition-3 disposition halt for Stan in **Batch B2**. |
| §1.5 M3 bare-governor | (b) corpus-side rewrite — excise | M3 framing dropped; bare-trailing-participials carve-outs disposition halt for Stan in **Batch B3**. |
| §1.6 four-forces | drop entirely | Followed §1.3 excision; recap-only table with no surviving normative content. |
| `cross-corpus-principles.md` creation | YES | Doc to be created (B1); index entry + Tanakh canon:11-16 row mitigate born-orphan. |

### The `cross-corpus-principles.md` companion-doc (B1 deliverable)

Doc to be authored at `atu-method/1-method/cross-corpus-principles.md`. **Sections** (per Stan's rulings — §1.3 and §1.5 M3 excluded):

1. **§1.1** Generative principle (reconciled — candidate-ATU substrate, live KEEP-AS-IS default)
2. **§1.3a** Rhetoric figures constrain (default dispositions per figure)
3. **§1.4 J1** Formally-marked parallel series (broader umbrella + 4-signal compound-list-break + GNT 5th)
4. **§1.4 J2** Portrait accumulation
5. **§1.4 J4** Classical commata
6. **§1.4 J5** Substantive adjunct + sub-clauses (degree-quantifier exclusion + same-slot diagnostic)
7. **§1.5 M1** Gorgianic bonded pair + asymmetric-modifier sub-clause
8. **§1.5 M4** Cross-corpus SCOPE (M4 doesn't fire on J1 N≥3 / J5 substantive adjuncts; prospective-not-retroactive)
9. **§1.8** Application order (adjusted — no §1.3 camera-angle Step 4 reference; M3 reference dropped)
10. **§1.9** N=2 Adjudication + N=3+ cliff + SCOPE sub-clause (predications-vs-objects)

**Index entry** to be added to `00-start-here.md` under new "Cross-corpus principles" section. **Tanakh canon:11-16** filename-routing table gets one row added. Subject to §7.3 trigger #1 adversarial audit before commit.

### Per-corpus dispositions (§1.12, §1.13)

Both go per-corpus per hard constraint #5. The pointer-block lines in BoFM canon:34 + GNT canon:48 mentioning "Parallel-List Uniformity Principle" and "Authorial Asymmetry Principle" become the actual ERROR Stan flagged (Error #1 in his correction directive) — they delegate to a now-orphaned framework §1 anchor for principles that already live IN the per-corpus canons. Pointer-block lines are REMOVED for these two concepts.

### Tanakh born-orphan resolution

Tanakh canon has no §-citation reference table (hard constraint #9). Mitigation: if `structural-licenses.md` is created, add a 5th line to Tanakh canon:11-16 prose table:

```
| atu-method/docs/structural-licenses.md | Cross-corpus principles (J-series, M-series, §1.8 application-order, §1.9 N=2 / N=3+ cliff) |
```

This is the only structural location Tanakh has for cross-doc references — repurposing the existing filename-routing table.

### Sub-anchor verbatim preservation (hard constraint #10)

All NAMED-BUT-UNNUMBERED sub-clauses preserve verbatim in their restoration target:
- J1 4-signal compound-list-break list + GNT-extended 5th signal
- M1 asymmetric-modifier sub-clause (joint-attachment test)
- §1.9 N=3+ cliff SCOPE (predications-vs-objects)
- §1.5 M4 precedence-over-J1/J5 and prospective-not-retroactive scope
- §1.4 J5 degree-quantifier exclusion + same-slot-vs-distinct-slot diagnostic

### Mechanical repairs bundled with this migration

- **`EP-1.md:153` malformed cite `§1.5 J5` → `§1.4 J5`** (or successor) — bundle with §1.4 disposition execution.
- **Pointer-block updates**: BoFM canon:22-28 (§0 → §1), BoFM canon:34 (§1 → drop superseded entries, repoint restored to `structural-licenses.md`); GNT canon:25-43 (same); Tanakh canon:11-16 (add structural-licenses.md row IF created).
- **Reader-repo script/validator stranded cites** (validate_rule_06_ud.py:104, validate_rule_07_ud.py:161, audit_anaphoric_gen_abs_macula.py:6, scan_multi_finite_verb_line.py, audit_anaphoric_frame_macula.py, validate_rule_18a_patriarch_triad.py, validate_rule_17_ud.py): repoint per-rule per the disposition of the §-id each cites.

---

## Verification receipts

Per claudit's audit directive: every consumer claim in this index is backed by raw grep/Read output
in the companion **[`canon-index-receipts.md`](canon-index-receipts.md)** (153 KB, 32 anchor
sections, 79 FLAGGED entries surfaced for Stan + claudit adjudication). Workflow `wasutgzgd`
(2026-06-06, 5 parallel verifier lanes, 444k subagent tokens) produced the receipts; main loop
synthesized into the companion file without interpretive intermediation.

A FLAGGED entry in the receipts does NOT indicate a phantom claim — it indicates a verifier-level
observation that warrants Stan + claudit adjudication (e.g., a cite that was already repointed
in Batch A1 — the on-disk text reads `§2.1` not `§1.10`; a cite that consumes the umbrella anchor
not the granular sub-anchor; a cite that presents a semantic tension with the cited anchor). The
appendix at the end of `canon-index-receipts.md` lists all 79 in one place.

## What's NOT in this first generation

This hand-built generation establishes the schema + §0.x / §1.x rows + the docs / concepts immediately
adjacent. Future regeneration via `build_canon_index.py` should additionally enumerate:
- Full doc-level inventory of every file under `atu-method/docs/` + `atu-method/2-evidence/scholarship/` + `atu-method/memories/`
- Per-rule R/M/J/EP/H sub-anchors across all per-corpus canons (currently 80+ rules across BoFM + GNT + Tanakh)
- Reader-repo validator dependency graph (every `framework §X.Y` cite in `validators/` keyed by validator-name)
- The `retraction-log.md` entries per corpus (BoFM has one; check GNT + Tanakh)
- Workspace `~/CLAUDE.md` + user `~/.claude/CLAUDE.md` rule references (currently spot-checked)
- `~/.claude/projects/.../memory/` cross-reference table (currently spot-checked)

The script should regenerate from source so this file cannot go stale; until then this hand-built
first generation is authoritative through 2026-06-06.

---

## Stage 2 Track B execution sequence (post-Stan-ruling 2026-06-06)

Stan ruled all four CONTESTED concepts. Execution plan:

| Batch | Scope | Audit gate | Halt for Stan? |
|---|---|---|---|
| **B1** | Author `cross-corpus-principles.md` + add `00-start-here.md` entry + add Tanakh canon:11-16 row | §7.3 trigger #1 (new canon doc) — adversarial audit required | YES — review doc content + §1.1 reconciliation paragraph before commit |
| **B2** | Excise camera-angle: drop `no camera shift` condition from BoFM R27 + GNT R25 + scholarship + canon (TIER 7 / R27 condition 3 / R25 conditions) + demote-memory cleanup | §7.3 trigger #6 (mechanical signature change under settled rule) | YES — decide condition-3 disposition (drop entirely / replace with §2.1 backward-containment / other) + sanity-check on rule output delta |
| **B3** | Excise M3: drop M3 framing from BoFM canon:152/1581 + GNT canon:237/245 + scholarship; resolve 4-carve-out disposition (fold into §2.1 / per-corpus rename / drop) | §7.3 trigger #6 | YES — decide 4-carve-out disposition |
| **B4** | Pointer-block updates across all three per-corpus canons (BoFM:22-28 §0→§1, BoFM:34 §1 block rewrite, GNT:25-43 + :48 same shape, Tanakh:11-16 add row); clean repoints for §0.x straggler + §1.2.x + §1.4 J3 + §1.5 M2 + §1.7 + §1.11 + §1.12 + §1.13 | §7.4 audit-skippable (cross-reference updates) — partly; some entries are claim repoints that go through §7.3 | Probably NOT (mechanical) |
| **B5** | Stranded cites in reader-repo scripts / validators / memories / retraction-log | §7.4 audit-skippable | NO |
| **Final** | canon-index.md regeneration with `proposed_disposition` column dropped; build_canon_index.py productionization (claudit) | n/a | n/a |

**Next action:** B1 — drafting `cross-corpus-principles.md`.

**Genuinely-clean Track A batches already shipped** for green-gate audit:
- A1 `86e1219` (§0.1, §0.4, §1.10, §2→§7.0 repoints)
- A2 `daa92b8` (atu-method) + `6d8ef1b` (.claude memory) — §3.x family
- A3 `73112e4` — §3.17 + framework.md:170 self-citation surgery
- A4 `ba04629` — binding-rules-lxx.md committed with PARKED banner + `_index.md:28` fix
