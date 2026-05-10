---
name: Check existing tooling before building new scanners
description: Before writing a new BofM scanner or validator, check whether existing validators in validators/, the ud-taxonomy reference, or a simple Grep already surface the pattern. Scanner proliferation creates a forest of can't-scale tools; extend existing tooling instead.
type: feedback
originSessionId: 5e934fd5-32e0-4958-9b1e-00dd9f0e6d19
---
**Rule.** Before writing a new scanner / validator / script for a BofM pattern, check:

1. **Existing validators** — `validators/` directory (see `validators/README.md`). Does one already cover the pattern?
2. **UD taxonomy reference** — `data/syntax-reference/ud-taxonomy.md` §7 Break Legality. Documents generic break-legality decisions.
3. **Grep over the v2-mine corpus** — often a one-line pattern resolves "find all instances of X" without a dedicated scanner.

Only build a new scanner if none of these covers the pattern AND the pattern is important enough to deserve its own validator (i.e., will be re-run across sessions).

**Why:** Scanner proliferation bloats the tooling tree, creates inconsistencies between similar scanners, and obscures which one is authoritative. BofM currently has a focused validators/ suite — keep it focused. The architectural preference is rule-application validators (apply the rule's actual logic) rather than shape-specific scanners.

**How to apply:**
- "I want to find all X" → first try `Grep` over `data/text-files/v2-mine/`. If one line of regex gives you X, don't build anything.
- "I want to audit rule Y" → check `validators/` for an existing Y validator. If yes, run it and extend; don't fork.
- If you're about to write a scanner > 50 lines of Python and the pattern is shape-matchable, stop and try Grep first.
- If building is genuinely necessary, extend an existing validator rather than creating a parallel file.
