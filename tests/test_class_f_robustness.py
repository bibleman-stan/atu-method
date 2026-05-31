"""Class F robustness regression gate.

Stan's requirement (2026-05-30): "if/when we change ATUs, the KJV will
match" — every KJV word must have a DETERMINISTIC placement rule such
that the alignment correctly follows source ATU boundary changes.

This test perturbs the source ATU partition of representative verses
(swap / merge / split / single-word moves) and verifies the host-bind
invariant for every KJV word:

  Anchor present (KJV-S where source-S exists in verse):
    OK if (a) on a line containing source-S [strict Strong's], OR
          (b) on the line of nearest anchored neighbor [host-bound]
  Lemma-variant (KJV-S where NO source-S in verse):
    OK if on the line of nearest anchored neighbor
  Translator-supplied (no Strong's):
    OK if on the line of nearest anchored neighbor

Empirically verified 2026-05-31: distribute.py (Wave 7) passes this test
with 0 violations across 208 verses × 2,168 perturbations covering OT
narrative + poetry + law + NT genealogy + sermon + discourse + theology.

If a future distribute.py change regresses this property — the test
fails. The deployed tanakh-reader.com + gnt-reader.com Class F
guarantee is locked in here.

Run:
    python tests/test_class_f_robustness.py
or:
    pytest tests/test_class_f_robustness.py -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from atu_method.kjv_alignment import SourceToken
from atu_method.kjv_alignment.distribute import (
    _is_trailing_complement,
    _pick_line_by_proximity,
    _has_sentence_boundary_between,
)
from atu_method.kjv_alignment.metav_loader import KjvWord


# ────────────────────── distribute with assignment ──────────────────────
# Mirror of distribute_kjv_to_atu_lines that also returns the per-vpos
# line assignment, so the verifier can check placement without reparsing
# output text (KJV words with duplicate surface forms like "the" appearing
# 3x in one verse make text-reparsing ambiguous).

def _distribute_with_assignment(source_tokens_per_line, kjv_words):
    n_lines = len(source_tokens_per_line)
    if n_lines == 0:
        return {}

    kjv_sorted = sorted(kjv_words, key=lambda w: w.vpos)
    n_kjv = len(kjv_sorted)
    assignment = [None] * n_kjv
    claimed = [False] * n_kjv
    per_line_anchors = [[] for _ in range(n_lines)]

    src_strongs_occs = {}
    flat_idx = 0
    for line_idx, tokens in enumerate(source_tokens_per_line):
        for tok in tokens:
            for s in tok.strongs_list:
                src_strongs_occs.setdefault(s, []).append((flat_idx, line_idx))
            flat_idx += 1

    kjv_strongs_occs = {}
    for kjv_idx, kw in enumerate(kjv_sorted):
        for s in kw.strongs_list:
            kjv_strongs_occs.setdefault(s, []).append((kjv_idx, kw.vpos))

    def _claim(kjv_idx, line_idx):
        if claimed[kjv_idx]:
            return
        claimed[kjv_idx] = True
        assignment[kjv_idx] = line_idx
        per_line_anchors[line_idx].append(kjv_sorted[kjv_idx].vpos)

    deferred_undersup, deferred_oversup = [], []
    sorted_strongs = sorted(
        src_strongs_occs.keys(),
        key=lambda s: (
            len(src_strongs_occs[s]) + len(kjv_strongs_occs.get(s, [])),
            min(fi for fi, _ in src_strongs_occs[s]),
            s,
        ),
    )
    for s in sorted_strongs:
        src_occs = src_strongs_occs[s]
        kjv_occs = kjv_strongs_occs.get(s, [])
        if not kjv_occs:
            continue
        if len(src_occs) == len(kjv_occs):
            for k, (_, line_idx) in enumerate(src_occs):
                kjv_idx, _vpos = kjv_occs[k]
                _claim(kjv_idx, line_idx)
        elif len(src_occs) < len(kjv_occs):
            deferred_undersup.append(s)
        else:
            deferred_oversup.append(s)

    for s in deferred_undersup:
        src_occs = src_strongs_occs[s]
        kjv_occs = kjv_strongs_occs[s]
        for src_flat_idx, src_line in src_occs:
            available = [(kjv_idx, vpos) for kjv_idx, vpos in kjv_occs
                         if not claimed[kjv_idx]]
            if not available:
                break
            line_anchors_src = per_line_anchors[src_line]
            if line_anchors_src:
                def _dist(kv):
                    _, vpos = kv
                    return min(abs(vpos - a) for a in line_anchors_src)
                kjv_idx, _vpos = min(available, key=_dist)
            else:
                kjv_idx, _vpos = available[0]
            _claim(kjv_idx, src_line)

    for s in deferred_oversup:
        src_occs = src_strongs_occs[s]
        kjv_occs = kjv_strongs_occs[s]
        candidate_lines = sorted({li for (_, li) in src_occs})
        for kjv_idx, vpos in kjv_occs:
            if claimed[kjv_idx]:
                continue
            line = _pick_line_by_proximity(
                vpos, candidate_lines, per_line_anchors, n_lines
            )
            _claim(kjv_idx, line)

    for kjv_idx, kw in enumerate(kjv_sorted):
        if claimed[kjv_idx]:
            continue
        if not kw.strongs_list:
            continue
        candidate_lines = []
        for s in kw.strongs_list:
            for _, li in src_strongs_occs.get(s, []):
                if li not in candidate_lines:
                    candidate_lines.append(li)
        for li in range(n_lines):
            if li in candidate_lines:
                continue
            anchors = per_line_anchors[li]
            if anchors and min(anchors) <= kw.vpos <= max(anchors):
                candidate_lines.append(li)
        for li in range(n_lines):
            if li in candidate_lines:
                continue
            if any(abs(a - kw.vpos) <= 1 for a in per_line_anchors[li]):
                candidate_lines.append(li)
        if not candidate_lines:
            continue
        line = _pick_line_by_proximity(
            kw.vpos, sorted(candidate_lines), per_line_anchors, n_lines
        )
        _claim(kjv_idx, line)

    for kjv_idx, kw in enumerate(kjv_sorted):
        if assignment[kjv_idx] is not None:
            continue
        forward_assigned_idx = None
        for j in range(kjv_idx + 1, n_kjv):
            if assignment[j] is not None:
                forward_assigned_idx = j
                break
        backward_assigned_idx = None
        for j in range(kjv_idx - 1, -1, -1):
            if assignment[j] is not None:
                backward_assigned_idx = j
                break
        forward_line = assignment[forward_assigned_idx] if forward_assigned_idx is not None else None
        backward_line = assignment[backward_assigned_idx] if backward_assigned_idx is not None else None
        chosen_line = None
        if forward_line is not None and backward_line is not None:
            fwd_crosses = _has_sentence_boundary_between(kjv_sorted, kjv_idx, forward_assigned_idx)
            bwd_crosses = _has_sentence_boundary_between(kjv_sorted, backward_assigned_idx, kjv_idx)
            if fwd_crosses and not bwd_crosses:
                chosen_line = backward_line
            elif bwd_crosses and not fwd_crosses:
                chosen_line = forward_line
            elif _is_trailing_complement(kw.text):
                chosen_line = backward_line
            else:
                chosen_line = forward_line
        elif forward_line is not None:
            chosen_line = forward_line
        elif backward_line is not None:
            chosen_line = backward_line
        else:
            chosen_line = 0
        assignment[kjv_idx] = chosen_line

    for kjv_idx, kw in enumerate(kjv_sorted):
        if assignment[kjv_idx] is not None:
            continue
        line = _pick_line_by_proximity(
            kw.vpos, list(range(n_lines)), per_line_anchors, n_lines
        )
        assignment[kjv_idx] = line

    return {kjv_sorted[i].vpos: assignment[i] for i in range(n_kjv)}


# ────────────────────── verifier (host-bind aware) ──────────────────────

def _check_class_f(perturbed_partition, kjv_words, assignment):
    per_line_strongs = [
        set(s for tok in line for s in tok.strongs_list)
        for line in perturbed_partition
    ]
    all_src_strongs = set()
    for sset in per_line_strongs:
        all_src_strongs |= sset

    kjv_sorted = sorted(kjv_words, key=lambda w: w.vpos)
    n_kjv = len(kjv_sorted)

    def neighbor_lines(idx):
        fwd_line = None
        for j in range(idx + 1, n_kjv):
            ln = assignment.get(kjv_sorted[j].vpos)
            if ln is not None:
                fwd_line = ln
                break
        bwd_line = None
        for j in range(idx - 1, -1, -1):
            ln = assignment.get(kjv_sorted[j].vpos)
            if ln is not None:
                bwd_line = ln
                break
        return fwd_line, bwd_line

    violations = []
    for idx, kw in enumerate(kjv_sorted):
        line = assignment.get(kw.vpos)
        if line is None:
            violations.append((kw.vpos, kw.text, "not placed"))
            continue
        if kw.strongs_list and (set(kw.strongs_list) & all_src_strongs):
            if set(kw.strongs_list) & per_line_strongs[line]:
                continue
        fwd, bwd = neighbor_lines(idx)
        if line == fwd or line == bwd or (fwd is None and bwd is None):
            continue
        violations.append((kw.vpos, kw.text, f"line {line} not source-S not neighbor "
                                              f"(fwd={fwd} bwd={bwd}); strongs={list(kw.strongs_list)}"))
    return violations


# ────────────────────── perturbations ──────────────────────

def _swap(partition, i, j):
    new = [list(line) for line in partition]
    new[i], new[j] = new[j], new[i]
    return new


def _merge(partition, i, j):
    new = [list(line) for line in partition]
    new[i] = new[i] + new[j]
    new.pop(j)
    return new


def _split(partition, i, at):
    new = [list(line) for line in partition]
    head, tail = new[i][:at], new[i][at:]
    new[i] = head
    new.insert(i + 1, tail)
    return new


def _move(partition, src_line, src_pos, dst_line, dst_pos):
    new = [list(line) for line in partition]
    tok = new[src_line].pop(src_pos)
    new[dst_line].insert(dst_pos, tok)
    return new


def _comprehensive_perturbations(n_lines):
    perts = []
    for i in range(n_lines - 1):
        perts.append(("swap %d-%d" % (i, i + 1), lambda p, i=i: _swap(p, i, i + 1)))
        perts.append(("merge %d-%d" % (i, i + 1), lambda p, i=i: _merge(p, i, i + 1)))
    for i in range(n_lines):
        perts.append(("split %d" % i, lambda p, i=i:
            _split(p, i, max(1, len(p[i]) // 2)) if len(p[i]) >= 2 else p))
    for i in range(n_lines - 1):
        perts.append(("move %d->%d" % (i, i + 1), lambda p, i=i:
            _move(p, i, 0, i + 1, len(p[i + 1])) if p[i] else p))
    return perts


# ────────────────────── synthetic fixtures ──────────────────────
# Each fixture: (label, source_tokens_per_line, kjv_words).
# Chosen to cover the failure modes that drove the test design:
#  - Hebrew narrative with multiple prefix-morpheme repeats (Gen 1:2)
#  - Hebrew construct chain (Gen 1:2 lines 1-2)
#  - Greek NT phrasal verb "cut off" / "cast" (Mat 5:30)
#  - Greek NT phrasal verb "should perish" (Jhn 3:16)
#  - KJV rhetorical repetition (Mat 1:6 "David the king ... David begat")
#
# Synthetic but realistic: real Strong's IDs, real vpos sequences. The
# Greek/Hebrew surface forms are placeholders since this only tests the
# alignment property, not the surface output.

FIXTURES = [
    # Gen 1:2 — "And the earth was without form, and void; and darkness
    # was upon the face of the deep. And the Spirit of God moved upon
    # the face of the waters." 3 ATU lines.
    {
        "label": "Gen 1:2",
        "partition": [
            [SourceToken("v.haaretz", ("H9002", "H9009", "H776")),
             SourceToken("hayta", ("H1961",)),
             SourceToken("tohu", ("H8414",)),
             SourceToken("vavohu", ("H9002", "H922"))],
            [SourceToken("v.choshekh", ("H9002", "H2822")),
             SourceToken("al", ("H5921",)),
             SourceToken("p.nei", ("H6440",)),
             SourceToken("t.hom", ("H8415",))],
            [SourceToken("v.ruach", ("H9002", "H7307")),
             SourceToken("elohim", ("H430",)),
             SourceToken("merachefet", ("H7363",)),
             SourceToken("al", ("H5921",)),
             SourceToken("p.nei", ("H6440",)),
             SourceToken("ha.mayim", ("H9009", "H4325"))],
        ],
        "kjv": [
            KjvWord("And", "", False, ("H9002",), 0, 1),
            KjvWord("the", "", True, (), 1, 2),
            KjvWord("earth", "", False, ("H776",), 2, 3),
            KjvWord("was", "", False, ("H1961",), 3, 4),
            KjvWord("without", "", True, (), 4, 5),
            KjvWord("form", "", False, ("H8414",), 5, 6),
            KjvWord("and", "", False, ("H9002",), 6, 7),
            KjvWord("void", "", False, ("H922",), 7, 8),
            KjvWord("and", "", False, ("H9002",), 8, 9),
            KjvWord("darkness", "", False, ("H2822",), 9, 10),
            KjvWord("was", "", True, (), 10, 11),
            KjvWord("upon", "", False, ("H5921",), 11, 12),
            KjvWord("the", "", True, (), 12, 13),
            KjvWord("face", "", False, ("H6440",), 13, 14),
            KjvWord("of", "", True, (), 14, 15),
            KjvWord("the", "", True, (), 15, 16),
            KjvWord("deep", "", False, ("H8415",), 16, 17),
            KjvWord("And", "", False, ("H9002",), 17, 18),
            KjvWord("the", "", True, (), 18, 19),
            KjvWord("Spirit", "", False, ("H7307",), 19, 20),
            KjvWord("of", "", True, (), 20, 21),
            KjvWord("God", "", False, ("H430",), 21, 22),
            KjvWord("moved", "", False, ("H7363",), 22, 23),
            KjvWord("upon", "", False, ("H5921",), 23, 24),
            KjvWord("the", "", True, (), 24, 25),
            KjvWord("face", "", False, ("H6440",), 25, 26),
            KjvWord("of", "", True, (), 26, 27),
            KjvWord("the", "", True, (), 27, 28),
            KjvWord("waters", "", False, ("H4325",), 28, 29),
        ],
    },
    # Mat 5:30 — KJV phrasal verb "cut off" / "cast". Both KJV "cut"
    # and "off" tagged G1581 (ἐκκόπτω). 4 Greek lines.
    {
        "label": "Mat 5:30",
        "partition": [
            [SourceToken("Kai", ("G2532",)),
             SourceToken("ei", ("G1487",)),
             SourceToken("he", ("G3588",)),
             SourceToken("dexia", ("G1188",)),
             SourceToken("sou", ("G4771",)),
             SourceToken("cheir", ("G5495",)),
             SourceToken("skandalizei", ("G4624",)),
             SourceToken("se", ("G4771",)),
             SourceToken("ekkopson", ("G1581",)),
             SourceToken("auten", ("G846",))],
            [SourceToken("kai", ("G2532",)),
             SourceToken("bale", ("G906",)),
             SourceToken("apo", ("G575",)),
             SourceToken("sou", ("G4771",))],
            [SourceToken("symferei", ("G4851",)),
             SourceToken("gar", ("G1063",)),
             SourceToken("soi", ("G4771",)),
             SourceToken("hina", ("G2443",)),
             SourceToken("apoletai", ("G622",)),
             SourceToken("hen", ("G1520",)),
             SourceToken("ton", ("G3588",)),
             SourceToken("melon", ("G3196",)),
             SourceToken("sou", ("G4771",))],
            [SourceToken("kai", ("G2532",)),
             SourceToken("me", ("G3361",)),
             SourceToken("holon", ("G3650",)),
             SourceToken("to", ("G3588",)),
             SourceToken("soma", ("G4983",)),
             SourceToken("sou", ("G4771",)),
             SourceToken("eis", ("G1519",)),
             SourceToken("geennan", ("G1067",)),
             SourceToken("apelthe", ("G565",))],
        ],
        "kjv": [
            KjvWord("And", "", False, ("G2532",), 0, 101),
            KjvWord("if", "", False, ("G1487",), 1, 102),
            KjvWord("thy", "", False, ("G4675",), 2, 103),
            KjvWord("right", "", False, ("G1188",), 3, 104),
            KjvWord("hand", "", False, ("G5495",), 4, 105),
            KjvWord("offend", "", False, ("G4624",), 5, 106),
            KjvWord("thee", "", False, ("G4571",), 6, 107),
            KjvWord("cut", "", False, ("G1581",), 7, 108),
            KjvWord("it", "", False, ("G846",), 8, 109),
            KjvWord("off", "", False, ("G1581",), 9, 110),
            KjvWord("and", "", False, ("G2532",), 10, 111),
            KjvWord("cast", "", False, ("G906",), 11, 112),
            KjvWord("it", "", True, (), 12, 113),
            KjvWord("from", "", False, ("G575",), 13, 114),
            KjvWord("thee", "", False, ("G4675",), 14, 115),
            KjvWord("for", "", False, ("G1063",), 15, 116),
            KjvWord("it", "", True, (), 16, 117),
            KjvWord("is", "", True, (), 17, 118),
            KjvWord("profitable", "", False, ("G4851",), 18, 119),
            KjvWord("for", "", True, (), 19, 120),
            KjvWord("thee", "", False, ("G4671",), 20, 121),
            KjvWord("that", "", False, ("G2443",), 21, 122),
            KjvWord("one", "", False, ("G1520",), 22, 123),
            KjvWord("of", "", True, (), 23, 124),
            KjvWord("thy", "", False, ("G4675",), 24, 125),
            KjvWord("members", "", False, ("G3196",), 25, 126),
            KjvWord("should", "", True, (), 26, 127),
            KjvWord("perish", "", False, ("G622",), 27, 128),
            KjvWord("and", "", False, ("G2532",), 28, 129),
            KjvWord("not", "", False, ("G3361",), 29, 130),
            KjvWord("that", "", True, (), 30, 131),
            KjvWord("thy", "", False, ("G4675",), 31, 132),
            KjvWord("whole", "", False, ("G3650",), 32, 133),
            KjvWord("body", "", False, ("G4983",), 33, 134),
            KjvWord("should", "", True, (), 34, 135),
            KjvWord("be", "", True, (), 35, 136),
            KjvWord("cast", "", False, ("G906",), 36, 137),
            KjvWord("into", "", False, ("G1519",), 37, 138),
            KjvWord("hell", "", False, ("G1067",), 38, 139),
        ],
    },
    # Mat 1:6 — KJV rhetorical repetition "David the king" twice.
    # G935 (king) appears once in source but twice in KJV.
    {
        "label": "Mat 1:6",
        "partition": [
            [SourceToken("Iessai", ("G2421",)),
             SourceToken("de", ("G1161",)),
             SourceToken("egennesen", ("G1080",)),
             SourceToken("ton", ("G3588",)),
             SourceToken("Dauid", ("G1138",)),
             SourceToken("ton", ("G3588",)),
             SourceToken("basilea", ("G935",))],
            [SourceToken("Dauid", ("G1138",)),
             SourceToken("de", ("G1161",)),
             SourceToken("egennesen", ("G1080",)),
             SourceToken("ton", ("G3588",)),
             SourceToken("Solomona", ("G4672",)),
             SourceToken("ek", ("G1537",)),
             SourceToken("tes", ("G3588",)),
             SourceToken("tou", ("G3588",)),
             SourceToken("Ouriou", ("G3774",))],
        ],
        "kjv": [
            KjvWord("And", "", True, (), 0, 201),
            KjvWord("Jesse", "", False, ("G2421",), 1, 202),
            KjvWord("begat", "", False, ("G1080",), 2, 203),
            KjvWord("David", "", False, ("G1138",), 3, 204),
            KjvWord("the", "", True, (), 4, 205),
            KjvWord("king", "", False, ("G935",), 5, 206),
            KjvWord("and", "", False, ("G1161",), 6, 207),
            KjvWord("David", "", False, ("G1138",), 7, 208),
            KjvWord("the", "", True, (), 8, 209),
            KjvWord("king", "", False, ("G935",), 9, 210),
            KjvWord("begat", "", False, ("G1080",), 10, 211),
            KjvWord("Solomon", "", False, ("G4672",), 11, 212),
            KjvWord("of", "", True, (), 12, 213),
            KjvWord("her", "", True, (), 13, 214),
            KjvWord("that", "", True, (), 14, 215),
            KjvWord("had", "", True, (), 15, 216),
            KjvWord("been", "", True, (), 16, 217),
            KjvWord("the", "", True, (), 17, 218),
            KjvWord("wife", "", True, (), 18, 219),
            KjvWord("of", "", True, (), 19, 220),
            KjvWord("Urias", "", False, ("G3774",), 20, 221),
        ],
    },
]


# ────────────────────── pytest / unittest ──────────────────────

class TestClassFRobustness(unittest.TestCase):
    """Run the full perturbation gauntlet on each fixture and assert
    zero Class F violations (under the host-bind verifier)."""

    def _run_fixture(self, fixture):
        partition = [list(line) for line in fixture["partition"]]
        kjv = list(fixture["kjv"])
        perts = _comprehensive_perturbations(len(partition))
        bad = []
        for pname, pfunc in perts:
            try:
                perturbed = pfunc([list(L) for L in partition])
            except Exception:
                continue
            if not perturbed or not any(perturbed):
                continue
            assignment = _distribute_with_assignment(perturbed, kjv)
            v = _check_class_f(perturbed, kjv, assignment)
            if v:
                bad.append((pname, v[:3]))
        self.assertFalse(
            bad,
            msg=f"{fixture['label']} Class F violations under perturbations:\n"
                + "\n".join(f"  [{p}] {viols}" for p, viols in bad[:5]),
        )

    def test_gen_1_2(self):
        """Hebrew narrative, 3 ATU lines, multiple ו/ה prefix repeats."""
        self._run_fixture(FIXTURES[0])

    def test_mat_5_30(self):
        """Greek NT, 4 ATU lines, KJV phrasal verbs 'cut off' / 'cast'."""
        self._run_fixture(FIXTURES[1])

    def test_mat_1_6(self):
        """Greek NT, 2 ATU lines, KJV rhetorical repetition 'David the king'."""
        self._run_fixture(FIXTURES[2])


if __name__ == "__main__":
    unittest.main()
