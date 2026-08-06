---
name: pre-output-checks
description: "Before sending ANY assistant turn, run the pre-output scan. Memories are not reading material; they are gates. This file enumerates the mandatory pre-output checks that must run BEFORE the response is sent, not after Stan flags a violation. Cumulative diagnostic from 2026-05-17 discipline audit (severity SEVERE): memories accumulate as historical records but are not consulted at decision-time. The fix is to treat each memory as an enforceable rule with a concrete check, run that check before output."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 786b3dcf-7033-47ce-86b0-0913576303a8
---

> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history (`87af68a0-0291-4910-962f-d0913b5722e6/c5abcb41c3b942cc@v3`); state as of 2026-06-05 (snapshot mtime); possibly stale — re-verify before relying.

**The rule:** Every assistant turn runs the pre-output check protocol below BEFORE sending. The discipline is not "I read the memories"; it is "I ran the checks." The memories are gates, not articles.

**Why:** The 2026-05-17 discipline audit found 125 permission-asks (memory: `feedback_just_execute_no_permission_churn`), 44 correction-preambles (memory: `feedback_no_correction_preamble`), 3-of-4 missed compaction-resume reads (memory: `feedback_compaction_resume_protocol`), and a §7.3 audit violation 3 hours after writing the memory forbidding it. The diagnosis: memories exist as observation-shaped historical records, not as enforcement-shaped pre-output gates. They are read but do not gate output.

**How to apply:** Run this scan over the draft response before sending it. Each rule has a concrete check; if the check fires, fix the draft first.

## The pre-output scan

### 1. Compaction-resume (one-time, post-compaction turn)

**Check:** If the most recent system message contains `isCompactSummary: true` OR text starting with "This session is being continued from a previous conversation that ran out of context", and the conversation does NOT yet contain a `Bash` tool call against `*.jsonl` returning 20-30 recent exchanges:

**Gate:** The FIRST tool call of this turn MUST be `Bash` reading the last 20-30 user/assistant exchanges from the session JSONL at `C:\Users\bibleman\.claude\projects\c--vaults-nano\<session-id>.jsonl`. Self-report begins with "Recovered: [summary of what was happening pre-compaction]". No other tool calls until this is done.

**Reference:** [[feedback_compaction_resume_protocol]]

### 2. Permission-asking regex scan

**Check:** Scan the draft for case-insensitive matches of:

```
(want me to|should i|do you want|let me know if|let me know when|awaiting your|
shall i|would you like me to|ready when you|on your nod|say the word|
do you want me|would you prefer)
```

**Gate:** If matched AND the action is within authorized scope (writes, edits, commits, pushes, dashboard updates, memory saves, routine operations) → DELETE the question. Execute the action. Surface the result OR a forward-list of what's next. Asks are reserved ONLY for irreversible operations the user has not pre-authorized (force-push, hard reset, sending external messages, mass deletions).

**Reference:** [[feedback_just_execute_no_permission_churn]]

### 3. Correction-preamble regex scan

**Check:** Scan the FIRST 200 characters of the response for case-insensitive matches of:

```
(you'?re right|good catch|fair point|let me reset|i had it wrong|i see now|
i'?ve been confusing|apologies|my apologies|sorry|i mis(read|spoke|stated)|
ah, i see)
```

**Gate:** If matched → DELETE the preamble. Open with the corrected substance directly. The substance IS the acknowledgment; the preamble is throat-clearing.

**Reference:** [[feedback_no_correction_preamble]]

### 4. Doc-rewrite preamble regex scan

**Check:** When writing to `directives/`, `docs/`, `canon/`, or any `.md` file in a memory or methodology repo — scan the FIRST 500 characters of the file content for:

```
(Status: DRAFT|Authored by:|Trigger context:|Version:|Predecessors:|
This (rewrites|replaces|supersedes)|What this changes:|Background:|
Previously:|Before this revision)
```

**Gate:** If matched → delete the preamble. Open with the substance (§1 Goal, or the first content section). Legacy detail lives in git log + JSONL + memory; the doc's first content is the current state.

**Reference:** [[feedback_doc_rewrite_no_preamble]]

### 5. Hand-wavy-language scan in precision artifacts

**Check:** When writing a trigger message / directive file / design document / sub-agent prompt — scan the full content for:

```
(or whatever|or similar|or equivalent|TBD|discover from|figure out|
somewhere around|something like|approximately the|find the right|
the relevant)
```

**Gate:** If matched → LOOK UP THE ACTUAL VALUE. Replace with concrete name/path/command/version. If genuinely unknown, mark with `<<UNKNOWN — must resolve before paste>>` and surface to Stan. Hand-waving in a precision artifact = passing the buck.

**Reference:** [[feedback_no_handwave_in_precision_artifacts]]

### 6. §7.3 audit-gate temporal test

**Check:** When writing a design doc / directive that fires §7.3 triggers (new mechanism / new closed list / new sub-category / new rule / mechanical signature change), inspect:
- WriteFile timestamp of the design doc
- Agent dispatch timestamp of the ≥2 parallel adversarial audits on that design

**Gate:** Audit dispatch timestamps MUST precede the WriteFile timestamp. "Pre-build" is a temporal claim, not a label. If the design lands first and audits dispatch second, the gate has been violated regardless of how the file's docstring labels its status.

Implementation: when an audit-gate fires, the dispatch sequence is:
1. Draft design content as text in this conversation (NOT in a file)
2. Dispatch ≥2 parallel adversarial audits on the draft text
3. Wait for audit verdict
4. IF CLEAR or REVISE-applied: write the file
5. IF STOP-AND-SURFACE: revise the draft, re-dispatch audits, repeat

The file does not exist on disk until the audit clears.

**Reference:** [[feedback_never_skip_audit_gate]]

### 7. External-transcript fidelity scan

**Check:** When Stan pastes multi-paragraph content from another LLM / agent / external source — before responding, the FIRST action is to run an enumerate pass over the transcript producing a STRONG / NUANCED / WEAK / RHETORIC-ONLY classification per claim.

**Gate:** No verdict on the transcript until the enumeration has been written out. Skim-and-respond silently drops the insights Stan delegated the synthesis to capture.

**Reference:** [[feedback_external_transcript_full_fidelity]]

### 8. Proactive memory-save check

**Check:** At the end of each turn where Stan flagged a failure pattern OR a new violation occurred, ask: is this pattern already memorialized?

**Gate:** If NO → write the memory NOW, in this turn. Do not wait for Stan to demand it. Reactive memorialization (memory written only after Stan curses) leaves the system one explicit-flag behind reality. Proactive memorialization closes the loop in the same turn.

**Reference:** [[feedback_stan_thinks_claude_files]]

### 9. Code-path-diagnosis verification scan

**Check:** Scan the draft for case-insensitive matches of:

```
(at line \d+|line \d+ of|file:\d+|\.py:\d+|the rule at|the gate at|
the helper at|the binding at|fires (here|at)|governs (this|the)|
filters (this|the)|fix at .+:\d+|extend .+:\d+|modify .+:\d+)
```

AND scan for proposal-shaped openings:

```
(my proposal|proposal:|I propose|recommend (extending|modifying|fixing) line|
the bug is at|root cause is|the actual fire happens|the rule fires)
```

**Gate:** If matched → confirm that THIS TURN contains ALL of:
(a) a `Read` tool call against the cited file at the cited range (40-line window minimum)
(b) a `Grep` of the containing file for analogous named helpers (`_is_*`, `_has_*`, `_detect_*`, `_check_*`)
(c) for control-flow claims, an executed probe (`python -c`, `pytest`, inline instrumentation) observing the claimed firing on the target case

If any is missing → the proposal does NOT get sent to a §7.3 audit. The proposal gets rewritten or abandoned. Dispatching an audit on an unverified proposal is the failure mode the 2026-06-04 four-audit-loss episode exhibited (~3M sub-agent tokens spent to discover all 4 proposals shared the same untested-mental-model shape).

**Reference:** [[feedback_code_path_diagnoses_require_running_the_code]]

### 10. Canon-firewall verbatim-quote gate (for ATU/binding-rule design)

**Check:** Scan the draft (and any pending Edit/Write `new_string`) for case-insensitive matches of:
- canon-citation tokens: `per framework\.md`, `§2\.[12]`, `§1\.[12]`, `elision[- ]restoration`, `marker license`, `explicit[- ]marker`, `amplificative`, `asseverative`, `closure[- ]eligible`, `forward[- ]closed`, `chain[- ]continuity`, `matrix verb`, `framework\.md:\d+`
- rule-design / file-edit shapes: `new binding rule`, `new §2\.[12] rule`, `amplificative split`, `split.*conjunct`, `Edit.*bofm_v1_fabric\.py`, `Edit.*tanakh_v1_fabric\.py`, `Edit.*gnt_v1_fabric\.py`, `overrides\.json.*add`, `cross-verse-merges\.json.*add`

**Gate:** If matched → confirm THIS TURN contains ALL of:
(a) a `Read` tool call against `~/repos/atu-method/docs/framework.md` covering AT MINIMUM the cited section AND the next 30 lines beyond it (firewalls live downstream of license-statements; §2.2 license lines ~103-111, firewall lines ~113-117);
(b) a verbatim block quote in the draft of the firewall / Registry discipline / "(ii)" sub-clause of the cited section — NOT a summary, NOT a paraphrase, the literal characters;
(c) a one-line explicit statement of form `"The firewall says <verbatim quote>; my mechanism does not violate it because <Z>"` OR `"The proposed mechanism's <X> matches the firewall's permitted-case <Y> because <Z>"`.

Specifically for §2.2 rule designs:
- The "Registry discipline (i)/(ii)/(iii)" block (lines ~113-117 in framework.md) is the firewall. NEVER skippable.
- §2.2(ii) forbids elision-restoration of a "shared subject / object / prepositional phrase." A rule restoring a verb+preposition idiom (V+P) across coordinated objects of P is shared-PP, not shared-finite-verb. STOP.
- A rule that matches `conj + NOUN/PROPN + case-ADP child + cc child` is by construction PP-coordination under a shared verb-idiom — fails §2.2(ii) on its face. The amplificative-marker on the conjunct does not rescue it; the marker grants break-license to units already closure-eligible under §2.1, and §2.2(ii) explicitly removes PP-coordination from closure-eligibility.

If any of (a)/(b)/(c) is missing → the rule does NOT get written to disk, NOT dispatched to a §7.3 audit, NOT shipped. Draft gets revised to either (i) quote the firewall and show non-violation, or (ii) abandon the rule.

**Anchoring failure:** 2026-06-05 Alma 34:7 episode — Claude designed PP-conj amplificative branch in `bofm_v1_fabric.py` shipped to working tree + commit cda5700 + regen, hit +30 validator regressions, brought gate-failure to Stan as a decision. Hostile audit (w3ppkb6i8) refuted the rule by quoting §2.2(ii) firewall verbatim — text Claude never Read that turn. The rule comment cited "framework.md:103-111 §2.2 explicit-marker license" while the disqualifying firewall sits at lines 113-117 of the same section. Canon-citation without canon-Read is the failure mode this gate exists to catch.

**Reference:** [[feedback_canon_citation_requires_verbatim_read]]

### 11. Stan-verse-flag pattern detector (mechanical trigger for standing default #8)

**Check:** Scan the most recent user turn (the one Claude is responding to) for the conjunction of TWO patterns:

- **Verse-reference** matching `\b(Alma|Mosiah|Helaman|Mormon|Moroni|Ether|Jacob|Enos|Jarom|Omni|Nephi|1 Ne|2 Ne|3 Ne|4 Ne|1\s*Nephi|2\s*Nephi|3\s*Nephi|4\s*Nephi|Words of Mormon|Genesis|Gen|Exod|Lev|Num|Deut|Josh|Judg|Ruth|Sam|Kgs|Chr|Ezra|Neh|Esth|Job|Ps|Prov|Eccl|Song|Isa|Jer|Lam|Ezek|Dan|Hos|Joel|Amos|Obad|Jonah|Mic|Nah|Hab|Zeph|Hag|Zech|Mal|Matt|Mark|Luke|John|Acts|Rom|Cor|Gal|Eph|Phil|Col|Thess|Tim|Tit|Phlm|Heb|Jas|Pet|Jude|Rev)\.?\s*\d+[:.]\d+\b` (case-insensitive)
- **Directive verb / fix-request** matching `\b(split|merge|restructure|fix|do it|needs?\s+a|should\s+(split|merge|break|be)|wrong|broken|feels\s+like|appears\s+to\s+(be|need)|cleanup|clean\s+up|address|handle)\b` (case-insensitive)

**Gate:** If BOTH match → the next sequence of tool calls MUST be (in order):
1. `Read` the cited verse + ±2 verses from `readers-bofm/data/text-files/v2/` (or the corpus-appropriate live source file)
2. `Read` `~/repos/atu-method/docs/framework.md` covering §2.1 + §2.2 + Registry discipline firewall (lines 80-150 minimum)
3. A response containing a literal block beginning `Bidirectional walkthrough:` with line-by-line forward-closure + backward-containment assessments and VERBATIM block-quote (`> ` prefixed) of the §2.1 / §2.2 / firewall clauses invoked

**Anti-bypass:** This gate fires REGARDLESS of whether any draft / proposed Edit / commit message cites canon. A rule shipped with no canon citation in its comment slips gate 10 entirely; gate 11 fires on the upstream user-turn shape, not on the downstream code shape, closing that hole.

If any of (1)/(2)/(3) is missing → STOP. Produce them before any `Edit` / `Write` / `Workflow` dispatch. The user-wide `execute-don't-ask` rule does NOT license skipping this sequence per workspace standing default #8's carve-out: the Read+Read+walkthrough sequence IS the executing for ATU verse-flag triggers.

**Detection-pattern lookahead:** the user-turn check is case-insensitive substring against the last user message in the conversation. If multiple verses are flagged in one user turn (e.g., "Alma 34:4 and 34:13"), the sequence runs ONCE per turn covering ALL flagged verses (single Read of framework.md + per-verse Read of live source + single walkthrough block covering all).

**Anchoring failure:** 2026-06-05 bypass-audit (workflow w0e8ald2d verify-1) identified that the original Alma 34:7 episode could re-occur if (a) the new rule's comment omits canon citation entirely (bypass #6), and (b) Claude reads Stan's "do it" as execute-don't-ask override of standing default #8 (bypass #5). Gate 11 closes both: the trigger is the user-turn shape, not the rule's citation, and the carve-out is in standing default #8 itself.

**Reference:** [[feedback_canon_citation_requires_verbatim_read]] + workspace CLAUDE.md standing default #8

## Aligns with

- [[feedback_never_skip_audit_gate]] — the §7.3 gate is the original pre-output check; this file generalizes the pattern.
- [[feedback_no_correction_preamble]] — one instance of a pre-output regex check.
- [[feedback_just_execute_no_permission_churn]] — another instance.
- [[feedback_doc_rewrite_no_preamble]] — another instance.
- [[feedback_compaction_resume_protocol]] — the simplest gate; if this one isn't running, none of them are.

## The structural failure this memory exists to address

Per the 2026-05-17 discipline audit (severity SEVERE): "The memory system is observation-shaped, not enforcement-shaped. Every memory file describes a past failure and articulates a rule, but there is no mechanism that runs the rules at decision-time. The structural failure is not that vault-Claude doesn't know the rules. It's that the rules are not gates. They are reading material."

This memory IS the mechanism. The pre-output scan is the gate. Running this scan before every turn is not optional discipline; it IS the discipline.
