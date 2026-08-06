"""Sweep Claude Code file-history for the lost C--Users-bibleman memory namespace.

Method (per RECOVERY-MANIFEST.md): the namespace's ~55 files (enumerated by the
recovered MEMORY.md index) exist only as content snapshots under
~/.claude/file-history/<session>/<hash>@vN. There is no hash->path index, so files
are identified by frontmatter (name:/description:/type:) and matched against the
target list. Highest @vN per hash wins. Candidates whose frontmatter name matches
a file still live in a surviving namespace are excluded (not lost).

Output: stages matched files into .recovery-2026-08-06/ under their index filename,
with a provenance line injected into frontmatter metadata. Prints a coverage report.
"""
import os, re, sys, glob, io
from collections import defaultdict
from datetime import datetime

HOME = os.path.expanduser("~")
FH = os.path.join(HOME, ".claude", "file-history")
STAGE = os.path.dirname(os.path.abspath(__file__))

# Full target list from recovered MEMORY.md (@v42, 2026-06-05).
TARGETS = [
    "_north_star.md", "_named_arcs.md", "user_stan.md", "_deferred_queue.md",
    "project_session_durability.md", "project_master_blaster.md",
    "project_bom_reader.md", "project_fef_aictp_paper.md",
    "project_bofm_bidirectional_rebuild.md", "project_gnt_idea_unit_measurement.md",
    "project_wallace_summaries.md", "project_bofm_substrate_quality.md",
    "project_corpus_v1_substitutes.md", "project_bofm_discourse_voice_deploy.md",
    "reference_biblical_studies_folder.md", "reference_academic_vault.md",
    "reference_analytics.md", "reference_corpus_pipeline_map.md",
    "reference_zotero_mcp.md", "reference_greek_datasets.md",
    "reference_lxx_english_brenton.md", "reference_emode_substrate.md",
    "feedback_no_silent_parking.md", "feedback_claude_commits_and_pushes.md",
    "feedback_just_execute_no_permission_churn.md",
    "feedback_broad_shell_no_permission_hang.md",
    "feedback_scratch_belongs_in_repo.md", "feedback_ship_independent_not_coupled.md",
    "feedback_always_recommend_in_options.md", "feedback_check_in_regularly.md",
    "feedback_never_handtype_greek_hebrew.md", "feedback_workflow.md",
    "feedback_stan_thinks_claude_files.md", "feedback_do_it_once.md",
    "feedback_surface_judgment_calls.md", "feedback_check_prior_corpora.md",
    "feedback_no_fly_swatting.md", "feedback_hand_edit_is_a_datapoint.md",
    "feedback_verify_deploy_state_never_assert.md", "feedback_pre_output_checks.md",
    "feedback_never_skip_audit_gate.md", "feedback_three_lens_default_for_plans.md",
    "feedback_conformance_is_not_correctness.md", "feedback_parallel_default.md",
    "feedback_mechanical_first_for_own_review.md",
    "feedback_code_path_diagnoses_require_running_the_code.md",
    "feedback_canon_citation_requires_verbatim_read.md",
    "feedback_time_estimate_as_diagnostic.md", "feedback_scrutinize_stan_instincts.md",
    "feedback_no_correction_preamble.md", "feedback_doc_rewrite_no_preamble.md",
    "feedback_no_handwave_in_precision_artifacts.md", "feedback_lean_entry_points.md",
    "feedback_session_bookend_protocol.md", "feedback_simplicity_bias.md",
    "feedback_staged_paper_scope_discipline.md",
    "feedback_atu_resolution_author_relative.md",
    "feedback_external_unit_is_not_atu.md",
    "feedback_em_dashes_illustrative_not_text.md",
    "feedback_compaction_resume_protocol.md",
    "feedback_circling_back_thread_tracking.md",
    "feedback_external_transcript_full_fidelity.md",
    "feedback_rhetoric_bandwagon.md", "feedback_stan_writes_claude_edits.md",
    "feedback_debug_trace_values.md", "feedback_preserve_formatting.md",
    "feedback_read_source_carefully.md",
]

# Already staged 2026-08-06 (first pass by meta-wiki session); index-name mapping.
ALREADY_STAGED = {
    "_north_star.md", "_deferred_queue.md", "project_master_blaster.md",
    "project_bofm_substrate_quality.md", "project_bofm_discourse_voice_deploy.md",
    "reference_emode_substrate.md",
}

def norm(s):
    return re.sub(r"[-_]", "", s.lower())

# slug variants for matching frontmatter name: to target filename
TARGET_KEYS = {}
for t in TARGETS:
    stem = t[:-3].lstrip("_")
    TARGET_KEYS[norm(stem)] = t
    # also without category prefix (north_star -> north-star-settled-decisions won't
    # exact-match; handled by prefix/containment check below)

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)

# frontmatter names of memory files still alive in surviving namespaces -> not lost
def live_names():
    names = set()
    pats = [
        os.path.join(HOME, ".claude", "projects", "*", "memory", "*.md"),
        os.path.join(HOME, "repos", "atu-method", "memories", "*.md"),
    ]
    for pat in pats:
        for p in glob.glob(pat):
            try:
                head = io.open(p, encoding="utf-8", errors="replace").read(2000)
            except OSError:
                continue
            m = FM_RE.match(head)
            if m:
                nm = NAME_RE.search(m.group(1))
                if nm:
                    names.add(norm(nm.group(1)))
    return names

def main():
    live = live_names()
    # collect candidates: highest vN per (session, hash)
    best = {}  # (session, hash) -> (vnum, path)
    for sess in os.listdir(FH):
        sdir = os.path.join(FH, sess)
        if not os.path.isdir(sdir):
            continue
        for fn in os.listdir(sdir):
            m = re.match(r"([0-9a-f]{16})@v(\d+)$", fn)
            if not m:
                continue
            key = (sess, m.group(1))
            v = int(m.group(2))
            if key not in best or v > best[key][0]:
                best[key] = (v, os.path.join(sdir, fn))

    # candidate memory files
    cands = []  # (target_or_None, name, desc, path, mtime, size)
    for (sess, h), (v, path) in best.items():
        try:
            sz = os.path.getsize(path)
            if sz > 200_000:
                continue
            text = io.open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        m = FM_RE.match(text)
        if not m:
            continue
        fm = m.group(1)
        if "node_type: memory" not in fm and not re.search(
            r"^\s*type:\s*(user|feedback|project|reference)\s*$", fm, re.MULTILINE
        ):
            continue
        nm = NAME_RE.search(fm)
        name = nm.group(1) if nm else ""
        dm = DESC_RE.search(fm)
        desc = dm.group(1)[:100] if dm else ""
        cands.append((name, desc, path, os.path.getmtime(path), sz, text))

    # match candidates to targets by name-slug
    matches = defaultdict(list)  # target -> [(mtime, path, name, size, text)]
    unmatched = []
    for name, desc, path, mt, sz, text in cands:
        n = norm(name)
        hit = None
        if n in TARGET_KEYS:
            hit = TARGET_KEYS[n]
        else:
            # containment: e.g. name north-star-settled-decisions vs target north_star
            for k, t in TARGET_KEYS.items():
                if k and (k in n or n in k):
                    hit = t
                    break
        if hit:
            matches[hit].append((mt, path, name, sz, text))
        else:
            if n not in live:
                unmatched.append((name, desc, path, mt, sz))

    # stage: newest snapshot per target
    staged, dupes = [], []
    for target, lst in sorted(matches.items()):
        lst.sort(reverse=True)
        mt, path, name, sz, text = lst[0]
        if target in ALREADY_STAGED or target == "MEMORY.md":
            continue
        d = datetime.fromtimestamp(mt).strftime("%Y-%m-%d")
        prov = ("> **PROVENANCE**: recovered 2026-08-06 from Claude Code file-history "
                "(`" + os.path.relpath(path, FH).replace(os.sep, "/") + "`); state as of "
                + d + " (snapshot mtime); possibly stale — re-verify before relying.\n\n")
        m = FM_RE.match(text)
        out = text[: m.end()] + prov + text[m.end():] if m else prov + text
        dest = os.path.join(STAGE, target)
        io.open(dest, "w", encoding="utf-8", newline="\n").write(out)
        staged.append((target, name, d, sz, os.path.relpath(path, FH)))
        for mt2, p2, n2, s2, _ in lst[1:3]:
            dupes.append((target, os.path.relpath(p2, FH)))

    found = set(matches.keys())
    missing = [t for t in TARGETS if t not in found and t not in ALREADY_STAGED]

    print("=== STAGED THIS PASS (%d) ===" % len(staged))
    for t, name, d, sz, src in staged:
        print("  %-55s %-8s %6dB  %s" % (t, d, sz, src.replace(os.sep, "/")))
    print("\n=== ALREADY STAGED, SKIPPED (%d) ===" % len(ALREADY_STAGED))
    print("\n=== STILL MISSING (%d) ===" % len(missing))
    for t in missing:
        print("  " + t)
    print("\n=== UNMATCHED MEMORY-SHAPED CANDIDATES not in any live namespace (%d) ===" % len(unmatched))
    for name, desc, path, mt, sz in sorted(unmatched)[:40]:
        d = datetime.fromtimestamp(mt).strftime("%Y-%m-%d")
        print("  %-45s %s %6dB  %s" % (name[:45], d, sz, os.path.relpath(path, FH).replace(os.sep, "/")))

if __name__ == "__main__":
    main()
