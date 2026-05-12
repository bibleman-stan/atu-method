"""Self-tests for atu_method.kjv_alignment.

Run as:
    pytest tests/test_kjv_alignment.py -v
or:
    python tests/test_kjv_alignment.py
from the atu-method repo root.

Each test case is end-to-end: actual MetaV CSVs on disk + synthesised
source-token sets (TAGNT/TAHOT-equivalent). The canonical-truth cases
are Gen 1:1 and Matt 1:23 — both are paragraph-anchor verses for the
whole migration.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Make the repo root importable when running this file directly.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from atu_method.kjv_alignment import (  # noqa: E402
    SourceToken,
    align_verse,
    distribute_kjv_to_atu_lines,
    extract_strongs_from_tagnt_col,
    extract_strongs_from_tahot_col,
    load_kjv_strongs_index,
    normalize_strongs,
)
from atu_method.kjv_alignment.metav_loader import book_id_for_osis  # noqa: E402


METAV_DIR = _REPO_ROOT / "data" / "kjv-strongs"


# ----------------------------------------------------------------------
# Strong's normalization tests
# ----------------------------------------------------------------------


class TestStrongsNormalize(unittest.TestCase):
    def test_braces_stripped(self):
        self.assertEqual(normalize_strongs("{H1254A}"), ["H1254"])

    def test_morphology_stripped(self):
        self.assertEqual(normalize_strongs("G1080=V-AAI-3S"), ["G1080"])

    def test_leading_zeros_stripped(self):
        self.assertEqual(normalize_strongs("G0846"), ["G846"])
        self.assertEqual(normalize_strongs("H0430"), ["H430"])

    def test_tahot_compound_split(self):
        # H9003 (preposition prefix) + H7225 (beginning) with G-suffix
        self.assertEqual(normalize_strongs("H9003/{H7225G}"), ["H9003", "H7225"])

    def test_tagnt_alt_comma_list(self):
        self.assertEqual(normalize_strongs("G3603, G2076"), ["G3603", "G2076"])

    def test_alphabetic_suffix_stripped(self):
        self.assertEqual(normalize_strongs("G2455N=N-NSM-P"), ["G2455"])

    def test_empty(self):
        self.assertEqual(normalize_strongs(""), [])
        self.assertEqual(normalize_strongs("   "), [])

    def test_plain(self):
        self.assertEqual(normalize_strongs("H7225"), ["H7225"])
        self.assertEqual(normalize_strongs("G2316"), ["G2316"])

    def test_dedup(self):
        self.assertEqual(normalize_strongs("G2532, G2532"), ["G2532"])

    def test_tagnt_col_extract(self):
        # Real example from Mat.1.23#17 (ἐστιν):
        #   col4 = "G1510=V-PAI-3S"
        #   col12 = "G1510"
        #   col13 = "G3603, G2076"
        out = extract_strongs_from_tagnt_col("G1510=V-PAI-3S", "G1510", "G3603, G2076")
        self.assertEqual(out, ["G1510", "G3603", "G2076"])

    def test_tahot_col_extract(self):
        # Real example from Gen.1.1#01 (בְּ/רֵאשִׁית):
        #   col5 = "H9003/{H7225G}"
        #   col9 = "H7225G"
        out = extract_strongs_from_tahot_col("H9003/{H7225G}", "H7225G")
        self.assertEqual(out, ["H9003", "H7225"])


# ----------------------------------------------------------------------
# MetaV loader smoke tests
# ----------------------------------------------------------------------


class TestMetavLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = load_kjv_strongs_index(METAV_DIR)

    def test_gen_1_1_present(self):
        key = (book_id_for_osis("Gen"), 1, 1)
        self.assertIn(key, self.index)
        words = self.index[key]
        self.assertEqual(words[0].text, "In")
        self.assertEqual(words[0].strongs_list, ())  # translator-supplied
        self.assertEqual(words[2].text, "beginning")
        self.assertIn("H7225", words[2].strongs_list)

    def test_matt_1_1_present(self):
        key = (book_id_for_osis("Matt"), 1, 1)
        self.assertIn(key, self.index)
        words = self.index[key]
        # Reconstruct verse text by KJV vpos order
        rendered = " ".join(w.render() for w in words)
        self.assertEqual(
            rendered,
            "The book of the generation of Jesus Christ, the son of David, the son of Abraham.",
        )

    def test_tagnt_alias_resolves(self):
        # "Mat" (TAGNT) should resolve to BookID 40 (OSIS "Matt")
        self.assertEqual(book_id_for_osis("Mat"), book_id_for_osis("Matt"))

    def test_word_count_invariant_gen_1_1(self):
        # MetaV's Gen 1:1 has 10 KJV words
        key = (book_id_for_osis("Gen"), 1, 1)
        self.assertEqual(len(self.index[key]), 10)


# ----------------------------------------------------------------------
# End-to-end alignment tests
# ----------------------------------------------------------------------


# Hebrew source tokens for Gen 1:1 (TAHOT-equivalent, in textual order).
# Strong's lists are what extract_strongs_from_tahot_col would produce.
GEN_1_1_TOKENS = [
    SourceToken("בְּרֵאשִׁית", ("H9003", "H7225")),
    SourceToken("בָּרָא", ("H1254",)),
    SourceToken("אֱלֹהִים", ("H430",)),
    SourceToken("אֵת", ("H853",)),
    SourceToken("הַשָּׁמַיִם", ("H9009", "H8064")),
    SourceToken("וְאֵת", ("H9002", "H853")),
    SourceToken("הָאָרֶץ", ("H9009", "H776")),
]


# Greek source tokens for Matt 1:1 (TAGNT-equivalent).
MATT_1_1_TOKENS = [
    SourceToken("Βίβλος", ("G976",)),
    SourceToken("γενέσεως", ("G1078",)),
    SourceToken("Ἰησοῦ", ("G2424",)),
    SourceToken("Χριστοῦ", ("G5547",)),
    SourceToken("υἱοῦ", ("G5207",)),
    SourceToken("Δαυὶδ", ("G1138",)),
    SourceToken("υἱοῦ", ("G5207",)),
    SourceToken("Ἀβραάμ", ("G11",)),
]


# Greek source tokens for Matt 1:23 (TAGNT-equivalent).
MATT_1_23_TOKENS = [
    SourceToken("ἰδοὺ", ("G2400",)),
    SourceToken("ἡ", ("G3588",)),
    SourceToken("παρθένος", ("G3933",)),
    SourceToken("ἐν", ("G1722",)),
    SourceToken("γαστρὶ", ("G1064",)),
    SourceToken("ἕξει", ("G2192",)),
    SourceToken("καὶ", ("G2532",)),
    SourceToken("τέξεται", ("G5088",)),
    SourceToken("υἱόν", ("G5207",)),
    SourceToken("καὶ", ("G2532",)),
    SourceToken("καλέσουσιν", ("G2564",)),
    SourceToken("τὸ", ("G3588",)),
    SourceToken("ὄνομα", ("G3686",)),
    # αὐτοῦ: primary G846, KJV alt G3778. We pass both per
    # extract_strongs_from_tagnt_col semantics.
    SourceToken("αὐτοῦ", ("G846", "G3778")),
    SourceToken("Ἐμμανουήλ", ("G1694",)),
    SourceToken("ὅ", ("G3739",)),
    # ἐστιν: primary G1510, KJV alts G3603+G2076.
    SourceToken("ἐστιν", ("G1510", "G3603", "G2076")),
    SourceToken("μεθερμηνευόμενον", ("G3177",)),
    SourceToken("μεθʼ", ("G3326",)),
    # ἡμῶν: primary G3165, KJV alt G2257.
    SourceToken("ἡμῶν", ("G3165", "G2257")),
    SourceToken("ὁ", ("G3588",)),
    SourceToken("θεός", ("G2316",)),
]


class TestEndToEndAlignment(unittest.TestCase):
    def test_gen_1_1_single_line(self):
        """Single ATU line: full KJV verse text."""
        result = align_verse("Gen", 1, 1, [GEN_1_1_TOKENS], METAV_DIR)
        self.assertEqual(len(result), 1)
        self.assertEqual(
            result[0],
            "In the beginning God created the heaven and the earth.",
        )

    def test_gen_1_1_split_after_elohim(self):
        """Split after token #3 אֱלֹהִים: KJV words preserve KJV order."""
        line_a = GEN_1_1_TOKENS[:3]  # בְּרֵאשִׁית, בָּרָא, אֱלֹהִים
        line_b = GEN_1_1_TOKENS[3:]  # אֵת, הַשָּׁמַיִם, וְאֵת, הָאָרֶץ
        result = align_verse("Gen", 1, 1, [line_a, line_b], METAV_DIR)
        self.assertEqual(len(result), 2)
        # Line A claims H7225 (beginning), H1254 (created), H430 (God).
        # Translator-supplied "In", "the" attach forward to line A.
        self.assertEqual(result[0], "In the beginning God created")
        # Line B claims H853 (and), H8064 (heaven), H776 (earth).
        # Translator-supplied "the" before heaven attaches forward to line B.
        self.assertEqual(result[1], "the heaven and the earth.")

    def test_matt_1_1_single_line(self):
        """Matt 1:1 single ATU line: KJV verbatim."""
        result = align_verse("Matt", 1, 1, [MATT_1_1_TOKENS], METAV_DIR)
        self.assertEqual(len(result), 1)
        self.assertEqual(
            result[0],
            "The book of the generation of Jesus Christ, the son of David, the son of Abraham.",
        )

    def test_matt_1_23_canonical_split(self):
        """Matt 1:23 split per v4-editorial: last line 'God with us.'"""
        # v4-editorial split for Matt 1:23:
        # Line 0: Ἰδοὺ ἡ παρθένος ἐν γαστρὶ ἕξει       (tokens 1..6)
        # Line 1: καὶ τέξεται υἱόν                       (tokens 7..9)
        # Line 2: καὶ καλέσουσιν τὸ ὄνομα αὐτοῦ Ἐμμανουήλ (tokens 10..15)
        # Line 3: ὅ ἐστιν μεθερμηνευόμενον               (tokens 16..18)
        # Line 4: Μεθʼ ἡμῶν ὁ θεός                       (tokens 19..22)
        lines = [
            MATT_1_23_TOKENS[0:6],
            MATT_1_23_TOKENS[6:9],
            MATT_1_23_TOKENS[9:15],
            MATT_1_23_TOKENS[15:18],
            MATT_1_23_TOKENS[18:22],
        ]
        result = align_verse("Matt", 1, 23, lines, METAV_DIR)
        self.assertEqual(len(result), 5)
        # CANONICAL TEST: the last ATU line must render as "God with us."
        self.assertEqual(result[4], "God with us.")
        # And each prior line should be KJV verbatim chunks in KJV order:
        self.assertEqual(result[0], "Behold, a virgin shall be with child,")
        self.assertEqual(result[1], "and shall bring forth a son,")
        self.assertEqual(result[2], "and they shall call his name Emmanuel,")
        self.assertEqual(result[3], "which being interpreted is,")

    def test_word_count_invariant(self):
        """Every KJV word in the verse must appear on exactly one line."""
        index = load_kjv_strongs_index(METAV_DIR)
        # Matt 1:23 example
        lines = [
            MATT_1_23_TOKENS[0:6],
            MATT_1_23_TOKENS[6:9],
            MATT_1_23_TOKENS[9:15],
            MATT_1_23_TOKENS[15:18],
            MATT_1_23_TOKENS[18:22],
        ]
        result = align_verse("Matt", 1, 23, lines, METAV_DIR)
        kjv_words = index[(book_id_for_osis("Matt"), 1, 23)]
        total_emitted = sum(len(line.split()) for line in result)
        # Reconstruct expected from MetaV: count surface tokens of
        # "Word + Punc" joined with spaces (mimicking the renderer).
        expected_total = len(kjv_words)
        self.assertEqual(
            total_emitted,
            expected_total,
            f"word-count drift: emitted {total_emitted}, expected {expected_total}",
        )

    def test_italic_only_line_edge_case(self):
        """ATU line whose source tokens match no KJV word renders empty."""
        # Construct a 2-line synthetic verse using Gen 1:1's KJV row but
        # split the source tokens so line 1 consists ENTIRELY of tokens
        # whose Strong's lists contain only H9009 (definite-article prefix
        # — not present on MetaV's KJV side as a Strong's tag).
        line_a = GEN_1_1_TOKENS  # all real tokens on line 0
        line_b = [SourceToken("ה", ("H9009",))]  # untranslatable prefix only
        result = align_verse("Gen", 1, 1, [line_a, line_b], METAV_DIR)
        self.assertEqual(len(result), 2)
        # Line 0 should contain the full verse (line_b's H9009 matches
        # nothing in MetaV)
        self.assertEqual(
            result[0],
            "In the beginning God created the heaven and the earth.",
        )
        self.assertEqual(result[1], "")

    def test_compound_hebrew_prefix(self):
        """A compound source token H9003/H7225G claims KJV 'beginning'.

        Adjacent translator-supplied KJV words ("In", "the") attach to
        the same line via the forward-look rule.
        """
        # Test the normalization end-to-end: pass a raw TAHOT-formatted
        # Strong's cell through extract + use it.
        prefix_token_strongs = tuple(
            extract_strongs_from_tahot_col("H9003/{H7225G}", "H7225G")
        )
        self.assertEqual(prefix_token_strongs, ("H9003", "H7225"))
        line_a = [SourceToken("בְּרֵאשִׁית", prefix_token_strongs)]
        line_b = GEN_1_1_TOKENS[1:]  # rest of verse
        result = align_verse("Gen", 1, 1, [line_a, line_b], METAV_DIR)
        self.assertEqual(len(result), 2)
        # "In" + "the" + "beginning" all on line A
        self.assertEqual(result[0], "In the beginning")
        # Remainder on line B
        self.assertEqual(result[1], "God created the heaven and the earth.")


# ----------------------------------------------------------------------
# Synthetic unit tests for distribute (no MetaV needed)
# ----------------------------------------------------------------------


class TestDistributeUnit(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(distribute_kjv_to_atu_lines([], []), [])

    def test_no_source_tokens(self):
        # No ATU lines means no output even if KJV words exist
        self.assertEqual(distribute_kjv_to_atu_lines([], []), [])

    def test_all_translator_supplied_falls_back_to_line_0(self):
        """If no source token matches any KJV word, everything goes to line 0."""
        from atu_method.kjv_alignment.metav_loader import KjvWord
        kjv = [
            KjvWord(text="The", punc="", italic=False, strongs_list=(),
                    vpos=0, word_id=1),
            KjvWord(text="quick", punc="", italic=False, strongs_list=(),
                    vpos=1, word_id=2),
            KjvWord(text="fox", punc=".", italic=False, strongs_list=(),
                    vpos=2, word_id=3),
        ]
        result = distribute_kjv_to_atu_lines(
            [[SourceToken("foo", ("H9999",))], [SourceToken("bar", ("H9998",))]],
            kjv,
        )
        self.assertEqual(result[0], "The quick fox.")
        self.assertEqual(result[1], "")


# ----------------------------------------------------------------------
# Entry point: allow `python tests/test_kjv_alignment.py`
# ----------------------------------------------------------------------


if __name__ == "__main__":
    unittest.main(verbosity=2)
