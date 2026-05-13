---
name: End-state-first orientation for big projects
description: For multi-phase / cross-corpus / migration work, lead session-orientation with the picture of what the user sees when done — NOT the procedural phase list. Procedural-first orientation enables substrate-hunt rabbitholes; picture-first orientation anchors all sub-decisions to the destination.
type: feedback
---

When planning multi-phase work (migrations, cross-corpus ports, big-feature rollouts) — and especially when handing such work across compaction boundaries — **lead with the end-state picture, not the procedural phase list.**

**Why this memory exists:** 2026-05-12 GNT KJV-migration scoping. Post-compaction pending.md was procedural-first ("Phase 1: acquire PD KJV+Strong's data → Phase 2: build alignment → ..."). The session latched onto Phase 1's substrate problem and rabbitholed for ~30 minutes hunting external tagged-KJV repos — all unnecessary work, because the documented design at `atu-method/docs/apparatus.md` actually uses STEPBible Strong's data + viz.bible MetaV KJV-Strong's tagging as the alignment substrate.

Stan's intervention: *"so let's stop: going down this rabbithole"* + *"the whole point was to leverage the work already done by the stepbible, right?"* — and finally *"describe to me what you think i want to see when this is done on the website."* The moment Stan forced the description of the end-state picture, the substrate question resolved itself.

**Root cause:** procedural-first pending.md + rule-shaped memories ("port the swap-system") + CHECK-IN protocol that prioritizes canon/rules/git-log but not the picture-shaped architectural docs (`apparatus.md`, `architecture.md`). With no anchored picture, "STEPBible doesn't ship Tagged-KJV" → "find external Tagged-KJV" felt like a valid logical chain. With the picture present, the chain is obviously wrong.

**How to apply:**

1. **Picture-first pending.md.** When pending.md holds a multi-phase migration plan, the FIRST section is "End state: what the user sees when this is done" — a paragraph (or two) describing the user-facing display, behavior, and unification across siblings. The phase list comes AFTER. The phase list is the procedural skeleton; the picture is the anchor that says "every phase must terminate at this picture."

2. **Picture-shaped memories.** When saving a "port-X-from-sibling-Y" memory, include a concrete user-facing exemplar (`begat → fathered on toggle`) alongside the verb (`port the swap-system`). Rule-shaped memories pass discipline checks but don't anchor destination. Both rule AND picture.

3. **CHECK-IN read-set extension for migration work.** When CHECK-IN runs and there's active cross-corpus / multi-phase / migration work in pending.md, ADD the picture-shaped architectural docs to the mandatory read set: `atu-method/docs/apparatus.md` + `atu-method/docs/architecture.md`. These are the "what does done look like" docs. Per-repo CLAUDE.md CHECK-IN sections name these explicitly. *(Claude-derived operationalization, not a direct Stan directive — the discipline of pulling back to the picture is Stan's; the specific mechanism of routing through CHECK-IN is Claude's inference. Stan can override the mechanism without overriding the underlying discipline.)*

4. **Picture-test before scoping.** Before scoping a multi-phase plan, ask: "Can I describe what the user sees on the page when this is done, in 1 paragraph, without referencing any phase or substrate?" If no, the picture is unclear — clarify before scoping. If yes, scope each phase as "what step does this take toward the picture."

5. **Pull-back-to-picture on ambiguity.** Stan codified this 2026-05-12: *"if you hit ambiguity/judgment call points, pull back and remind yourself what it is you're doing and why and the answers should become clear."* When mid-work and an architectural fork appears, the right move is NOT to evaluate the fork on its technical merits in isolation — it's to pull back to the end-state picture and ask which fork serves the picture.

6. **Cross-corpus picture unification.** When work spans sibling readers, the picture should include the unification dimension: what's shared across siblings (UX shell, swap behavior, KJV anchoring) and what differs (number of layers, language-specific archaisms). *(Claude-derived inference from the cross-sibling end-state descriptions in this session, not a direct Stan codification — the unified design IS shipped, but the "load-bearing design constraint" framing is mine. Treat as helpful framing during cross-corpus work, not as a meta-rule that auto-fires in non-cross-corpus contexts.)*

**Documented in:** `atu-method/docs/apparatus.md` now has a "What the Reader Sees (end-state per sibling)" section + a "How the KJV-anchored English layer is produced" mechanism diagram, both picture-first. Per-repo CLAUDE.md CHECK-IN sections reference apparatus.md when migration work is active.
