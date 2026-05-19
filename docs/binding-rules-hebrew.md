# Hebrew Binding Rules Catalog

Catalog of the 14 mechanical binding rules that transform BHSA clause-atoms into ATU candidate groups for Hebrew (Tanakh).

Each rule:
- Fires based on BHSA-derived features (clause type, head verb lemma, text-prefix after pointing-strip)
- Is justified by the bidirectional test (`framework.md` §2)
- Operates only within a single verse (global safety guard in `should_bind()`)
- Is evaluated in order; the first matching rule wins

The catalog was validated across four chapters spanning four genres (Gen 22 / Psalm 1 / Isaiah 53 / Lev 11). See `framework.md` §5 for validation numbers.

---

## B1 — Vocative binds backward

| Trigger | `curr.typ == "Voct"` |
| Justification | Vocative-only clauses fail the bidirectional test on their own (no predication, no closure). MUST bind to preceding speech-margin or NP. |
| Example | Gen 22:1 `וַיֹּאמֶר אֵלָיו` + `אַבְרָהָם` → one ATU |

## B2 — Appositive (object-marker check)

| Trigger | `curr.typ == "Defc"` AND `curr` text (consonants only) starts with `את` or `ואת` |
| Justification | BHSA's `Defc` covers BOTH appositive (object-marker continuation) AND fronted-subject NP. Only the object-marker-headed flavor is appositive; the other starts a new ATU. |
| Example | Gen 22:2 `אֶת־בִּנְךָ אֶת־יְחִידְךָ` + `אֶת־יִצְחָק` → one ATU |
| Counter-example (does NOT fire) | Ps 1:3 `וְכֹל` (Defc, no `את`) — fronted subject of following predicate, starts new ATU |

## B3 — Restrictive ʾăšer binds backward

| Trigger | `curr` text (consonants only, pointing stripped) starts with `אשר` |
| Justification | Restrictive relative clauses bind to their head noun regardless of internal completeness; removing them leaves the head not uniquely identified. |
| Excluded by construction | Causal `יַעַן אֲשֶׁר` / `עֵקֶב אֲשֶׁר` (don't start with `אשר`) |
| Example | Gen 22:2 `אֶת־יְחִידְךָ` + `אֲשֶׁר־אָהַבְתָּ` → one ATU |
| Known limitation | Length-dependent over-binding. Long propositionally-weighty ʾăšer clauses with internal subject + verb sometimes should stand alone (LDHB SUB-POINT pattern). Not mechanically distinguishable from short modifiers; remains a known gap for v2 LLM. |

## B4 — REMOVED

Was: speech-frame + any non-wayyiqtol → bind. **Replaced by the bidirectional-test principle.** Speech-margin (`וַיֹּאמֶר`) is its own ATU IF AND ONLY IF the following speech can stand alone by the bidirectional test:
- Speech-margin + vocative-only (`אַבְרָהָם`) → bind (handled by B1)
- Speech-margin + complete-clause speech (`הִנֵּנִי`) → split (each passes the test independently)

## B5 — Wayhi temporal frame binds forward

| Trigger | `prev.head_verb_lemma == "היה"` AND `prev.typ in {Way0, WayX}` AND `prev` text (consonants) starts with `ויהי` AND contains a temporal anchor prefix (`אחר` / `ביום` / `בהיות` / `כאשר` / `כי` / `ב`) within first 30 chars |
| Justification | Wayhi-temporal-frame is the canonical Hebrew narrative "and it came to pass that..." opening, anaphoric to prior narrative (`hadevarim ha'eleh` = "these things" = deictic backward). The frame fails standalone backward containment; binds to the main clause it frames. Same pattern as BoFM "and it came to pass" (AICTP) frames. |
| Example | Gen 22:1 `וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה` + `וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם` → one ATU |

## B6 — Casus pendens resumption

| Trigger | `prev.typ == "CPen"` |
| Justification | Casus pendens (dislocated topic / left-dislocation) introduces a topic that the following clause resumes. The dislocated NP fails forward closure alone (no predication); the resumption clause completes it. |
| Example | Gen 22:4 `בַּיֹּום הַשְּׁלִישִׁי` + `וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו` → one ATU |

## B7 — Bare wayyiqtol pair (hendiadys-like)

| Trigger | `prev.typ == "Way0"` AND prev text is a single token AND `curr.typ in {Way0, WayX}` |
| Justification | A bare single-token wayyiqtol verb followed by another wayyiqtol typically expresses coupled motion or preparation (hendiadys-like): "and he arose and went." The single-token preparation verb fails the closure intuition of a full predication. |
| Example | Gen 22:3 `וַיָּקָם` + `וַיֵּלֶךְ אֶל־הַמָּקֹום` → one ATU |

## B8 — Hineh-presentative + asyndetic-qatal attribute

| Trigger | `prev.typ == "NmCl"` AND prev text (consonants) starts with `הנה` or `והנה` AND `curr.typ == "ZQt0"` |
| Justification | Deictic-presentative `הִנֵּה X` ("behold X") introduces a new entity; an immediately-following asyndetic qatal clause is a descriptive attribute of that entity (typically a passive participle expressed via qatal form). The two together form one presentational ATU. |
| Example | Gen 22:13 `וְהִנֵּה־אַיִל אַחַר` + `נֶאֱחַז בַּסְּבַךְ בְּקַרְנָיו` → one ATU ("behold a ram caught in the thicket by his horns") |

## B9 — Ne'um authenticating formula

| Trigger | `curr.typ == "NmCl"` AND `curr` text (consonants) starts with `נאם` |
| Justification | The `נְאֻם־יהוה` formula ("oracle of YHWH") is an authenticating tag that binds to its preceding oath/speech content. Universal pattern in prophetic and oath texts. |
| Example | Gen 22:16 `בִּי נִשְׁבַּעְתִּי` + `נְאֻם־יְהוָה` → one ATU |

## B10 — Purposive infinitive construct

| Trigger | `curr.typ == "InfC"` |
| Justification | Infinitive construct clauses (typically `לְ` + InfC) express purpose or speech-introduction tightly bound to a main verb. Fails standalone backward containment (the main verb supplies the agent). Covers both `לֵאמֹר` ("saying") after speech verbs and `לִשְׁחֹט` ("to slaughter") after action verbs. |
| Example | Gen 22:20 `וַיֻּגַּד לְאַבְרָהָם` + `לֵאמֹר` → one ATU. Gen 22:10 `וַיִּקַּח אֶת־הַמַּאֲכֶלֶת` + `לִשְׁחֹט אֶת־בְּנוֹ` → one ATU. |

## B11 — Verb-of-cognition + ki-complement

| Trigger | `prev.head_verb_lemma in {ידע, ראה, שׁמע, חשׁב, זכר, בין, הכיר}` AND `curr` text (consonants) starts with `כי` |
| Justification | A `כִּי`-complement clause after a verb of cognition is the SUBJECT or OBJECT of the cognition (a complement, not a separate assertion). The `כי` introduces the content of what is known/seen/heard. |
| Example | Gen 22:12 `כִּי עַתָּה יָדַעְתִּי` + `כִּי־יְרֵא אֱלֹהִים אַתָּה` → one ATU |

## B12 — Reop forward-binding

| Trigger | `prev.typ == "Reop"` |
| Justification | BHSA's `Reop` (re-opening / discourse-resumption) tag marks a bare conjunction (typically standalone `כִּי` in oath contexts) that opens the following clause. The conjunction is the head of the content that follows; bind forward. |
| Example | Gen 22:16 `כִּי` (Reop) + `יַעַן אֲשֶׁר עָשִׂיתָ אֶת־הַדָּבָר הַזֶּה` → one ATU |

## B13 — Participial attribute (refined)

| Trigger | `curr.typ == "Ptcp"` AND `prev.head_verb_lemma == "היה"` |
| Justification | BHSA's `Ptcp` tag covers both attributive participles (modify prior NP, no own subject) and predicative participles (with own subject). Only the attributive flavor binds. Heuristic: bind only when prev clause's head is `היה` (the canonical "vehayah ke-X + attribute" pattern). |
| Example | Ps 1:3 `וְהָיָה כְּעֵץ` + `שָׁתוּל עַל־פַּלְגֵי מָיִם` → one ATU |
| Counter-example (does NOT fire) | Ps 1:6 `כִּי־יוֹדֵעַ יְהוָה דֶּרֶךְ צַדִּיקִים` — Ptcp but prev is from prior verse and no `היה`; predicative participle stays its own ATU |

## B14 — Asyndetic predicate (yiqtol / qatal without waw)

| Trigger | `curr.typ in {"ZYq0", "ZQt0"}` |
| Justification | Asyndetic verb clauses (no waw-conjunction prefix) are typically predicates of a fronted subject NP from a prior clause. Bind to prev so the subject + predicate forms one ATU. The B8 hineh-pattern is a more specific case handled earlier. |
| Example | Ps 1:3 `וְכֹל אֲשֶׁר־יַעֲשֶׂה` (Defc + xYq0 relative) + `יַצְלִיחַ` (ZYq0) → one ATU ("all that he does prospers") |

---

## Rule evaluation order

The rules are evaluated in order in `should_bind(prev, curr)`. The first matching rule returns `True` and the binding fires. A global safety guard at the top refuses any binding across verse boundaries.

```
0. Same-verse check (global guard)
1. B1 Vocative
2. B2 Appositive (object-marker)
3. B3 Restrictive ʾăšer
4. B5 Wayhi temporal frame
5. B6 Casus pendens resumption
6. B7 Bare wayyiqtol pair
7. B8 Hineh-presentative + ZQt0
8. B9 Ne'um formula
9. B10 Purposive InfC
10. B11 Cognition + ki-complement
11. B12 Reop forward-binding
12. B13 Participial attribute (with היה)
13. B14 Asyndetic predicate
```

Order matters when multiple rules could fire on the same clause pair. The current order is empirically chosen; B8 precedes B14 to avoid the asyndetic-predicate rule swallowing the hineh-presentative pattern.

---

## Validation results

Per `framework.md` §5: 85-91% boundary F1 vs LDHB across four chapters / four genres. Pipeline catches ≥ 80% of LDHB boundaries (recall) and draws boundaries that are present in LDHB ≥ 79% of the time (precision). The specific failure modes (length-dependent ʾăšer, sub-clause gapping, BHSA-fine subject-predicate split) are documented in `framework.md` §6.

## Adding a rule

A new binding rule MUST:

1. Identify the BHSA feature(s) that drive the rule
2. Have a one-paragraph justification tracing to the bidirectional test
3. Have at least one canonical positive example
4. Have at least one canonical counter-example (or "always fires" note)
5. Be added to `v1_5_apply_bindings.py:should_bind()` in the correct evaluation order
6. Be retested against the validated chapter set (Gen 22 / Psalm 1 / Isaiah 53 / Lev 11). No regression in cold-eye match or boundary F1 on prior chapters.

A new rule that produces a regression on one of the validated chapters MUST be either revised or rejected, not committed.

## Retiring a rule

A rule may be retired (like B4 was) when:
- Its function is subsumed by another rule operating on a more principled feature
- Its firing is empirically incorrect on more chapters than it's correct on
- It was a heuristic that the bidirectional test directly contradicts

Retired rules stay numbered (B4 retains its slot; new rules use B15+) so the numbering is stable.
