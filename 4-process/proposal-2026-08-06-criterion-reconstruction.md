---
status: PROPOSED — analysis only. No canon edited. Retiring live allowances is a
  §7.3 trigger #5 event and MUST clear adversarial audit before any change.
---

# Proposal — deconstruct and rebuild §2.1's allowance apparatus

**Summary**: [`framework.md`](../1-method/framework.md) §2.1 is **18,828 bytes elaborating a 1,352-byte criterion** — roughly fourteen to one — and six of its named allowances landed in a single day (2026-06-02, commits `4413af1`, `5398066`, `be73423`, `d39999b`, plus the serial-circumstantial chain). This document tests each allowance against the question the criterion actually asks: *does it derive from (A) forward closure + backward containment, or from its siblings?* Result: **two derive, three do not, and one collides with a firewall**. The three that do not derive rest on two carve-outs — the "participial-predication allowance" and the "legal-casuistic protasis carve-out" — that are **cited as existing and defined nowhere**.

**Status: PROPOSED.** Nothing here is applied. These allowances are deployed and generate live line breaks on three reader sites.

**Last updated**: 2026-08-06

---

## The finding that reframes the rest: two phantom foundations

Grepped 2026-08-06 across [[1-method/framework.md|framework.md]], [[1-method/cross-corpus-principles.md|cross-corpus-principles.md]], `binding-rules-*.md`, `_old/`, and the BoFM + GNT per-corpus canons:

| Cited carve-out | Cited at | Defined |
|---|---|---|
| "the participial-predication allowance" | `framework.md:56`, `:63` | **nowhere** |
| "the existing legal-casuistic protasis carve-out" | `framework.md:63` | **nowhere** |

Both are invoked in the grammatical voice of settled canon — "satisfied under the participial-predication allowance", "extending the *existing* legal-casuistic protasis carve-out". Neither has a definition, a worked example, or an audit trail. This is the phantom class [`canon-index.md`](../../canon-index.md) tracks, and the failure shape `feedback_canon_citation_requires_verbatim_read` was written for.

It matters because **forward closure is exactly what non-finite material lacks**. A participial phrase is not grammatically complete on its own terms; that is the whole difficulty. Three allowances resolve that difficulty by appeal to a carve-out that does not exist.

## Per-allowance verdicts

### DERIVES — keep, but replace the analogical warrant with the derivation

**1. Relative-clause-embedded speech-frame** (`:70`). The frame|quote break rests on the deixis test at `§2.1:50` — a re-performed utterance has its own deictic center. Syntactic embedding depth does not change deictic center, so the rule extends to `acl:relcl`-embedded speech verbs by *derivation*, not analogy. Alma 32:17 is a genuine exemplar. **Keep**; restate the warrant as deixis rather than as "the existing rule also fires."

**2. Discourse-particle attribution within reported speech** (`:72`). Also derives from deixis — the particle is the speaker's word, the frame is the narrator's. Critically, this allowance **licenses no break at all**: it decides which side of an already-licensed boundary the particle falls on. **Keep, and reclassify** as boundary *placement*, not a break license. It is in §2.1 by filing error.

### DOES NOT DERIVE — rebuild or retract

**3. Serial circumstantial participial chains** (`:56`). Backward containment is sound (chain-continuity carry of subject + finite tense is squarely (A)). Forward closure is granted by the phantom. Strip the phantom and there is no closure argument — only the intuition that four coordinated missionary activities feel like four beats. Rests on **1 exemplar** (Mosiah 27:35).

**4. Discrete cognitive-state circumstance chain** (`:63`). Rests on **both** phantoms simultaneously, and the second is worse than missing: "extending the existing legal-casuistic protasis carve-out to EME narrative" is a **register extension**, which is a scope claim and Category B by default per §7.0's own diagnostic — extending a Hebrew legal-casuistic carve-out to Early Modern English narrative is not a clarification.

**5. Cognition-frame participial allowance** (`:88`). Its own text offers "three converging anchors": (i) analogy to frame|quote; (ii) dependence on allowance #4, which rests on phantoms; (iii) parallel-cola uniformity — "items 2..N each get their own ATU **under the existing fabric**, so item 1 must too." Anchor (iii) is circular: the fabric's current output is used to justify the rule that changes the fabric. Rests on **1 documented instance** (Alma 33:1), and its own text says so.

### FIREWALL COLLISION — retraction candidate

**6. Discourse-particle amplification** (`:81`). This one is not merely underived; it appears to contradict `§2.2` directly. The allowance licenses "yea + non-finite content" by borrowing "the prior line's **subject + finite verb** through chain-continuity carry-over," with the exemplar amplifying a *locative PP* (1 Ne 11:1, "yea, into an exceedingly high mountain"). But `yea` is a registered §2.2 marker, and §2.2's admission precondition (ii) reads verbatim (`framework.md:114`):

> forward-closed by restoring a **gapped finite verb** from the immediately-prior parallel clause (a shared *finite verb* only — NOT a shared subject / object / prepositional phrase, which would re-admit the parallel-cola splitting §2 forbids)

The allowance borrows a shared subject and licenses a shared-PP amplification — both named exclusions. **This is the Alma 34:7 shape recurring**: a rule citing §2.2 while restoring precisely the shared-PP elision §2.2(ii) forbids, which shipped with +30 validator regressions before an audit caught it (`feedback_canon_citation_requires_verbatim_read`). The allowance also self-flags "the highest false-positive risk."

Two occurrences of one shape is one short of the retraction log's 3-strike promotion threshold — a threshold that has never once been evaluated.

## Why it happened (structural, not personal)

Three conditions held simultaneously on 2026-06-02. The criterion was **too thin to adjudicate hard cases** — one sentence plus an unsupported proxy claim (see [`framework-claim-inventory.md`](framework-claim-inventory.md) #4), so every difficult verse needed a bespoke carve-out because there was nothing else to appeal to. The retraction→promotion loop had **already frozen on 2026-05-17**, two weeks earlier, so nothing forced consolidation. And each allowance could cite its siblings as warrant, which makes growth self-sustaining: allowance C is justified by B, B by A, A by analogy.

**The sprawl is a symptom of the thin hinge, not an independent defect.** That is the load-bearing claim of this proposal, and it predicts something testable: thicken §2 (what licenses treating grammatical closure as a proxy for thought, and what follows from it for non-finite predication) and a real fraction of these allowances should reappear as *consequences* rather than exceptions.

## The rebuild, in dependency order

1. **Resolve the non-finite predication question at the criterion level.** Every failing allowance fails the same way: non-finite material lacking forward closure. Either the framework takes a principled position on when non-finite predication constitutes a thought-unit — argued, not assumed — or all three retract. This is one decision, not three.
2. **Then re-derive each allowance against the thickened criterion.** Survivors keep their content and gain a real warrant. Non-survivors go to the §2.2 marker registry (if they are genuinely marker-licensed and closure-eligible) or to a per-corpus rule catalog (if they are EME-specific), or they retract.
3. **Move the two derivable ones out of the allowance pile** — #1 restated from deixis, #2 reclassified as placement.
4. **Log every retraction.** Six allowances is more than enough to test whether the 3-strike threshold produces a promotion, which would be the retraction loop's first cycle since 2026-05-17.

## Gate — what must happen before anything is edited

- Retiring live applications is **§7.3 trigger #5**; the register extension in #4 is **trigger #1/#4**. Both mandate adversarial audit BEFORE the change, dispatched as a `Workflow` with ≥2 lenses per the standing default (over-merge and atomicity), not hand-spawned agents.
- Every candidate retraction must be **measured against the BoFM gold yardstick** (33 stratified verses, `readers-bofm/private/substrate/emode-substrate/bofm-atu-gold-yardstick.json`) with the allowance in and out. Over-merge is the red line and validators are blind to it.
- Only survivors of both are applied, and each retraction gets a retraction-log entry.

**Nothing in this document is applied. It is a proposal awaiting Stan's ruling on step 1 and the audit dispatch.**

## Related

- [`framework-claim-inventory.md`](framework-claim-inventory.md) — the typing pass; #4 is the hinge this proposal says to fix first
- [`improvement-loops.md`](improvement-loops.md) — loop 2 is the stalled mechanism that would have caught this
- [`../1-method/framework.md`](../1-method/framework.md) §2.1, §2.2, §7.0, §7.3
