#!/usr/bin/env python3
"""Audit intra-series citations: verify that each paper's references to other
papers in the Δt series resolve to the right DOIs.

Usage: python3 tools/citation_graph.py [--json]

For each paper's body .md, extracts reference-list entries that look like:

    [N] Beck, J. (YYYY). Title. Preprint, Δt Framework Paper M. doi:10.5281/zenodo.NNNN

and checks that:
  - Paper M exists in preprint/
  - The cited DOI matches preprint/MM-.../metadata.yaml's DOI (concept DOI)
  - All "Paper M" mentions in body prose have corresponding reference entries

Exits non-zero on any mismatch.

Caveats:
  - Only intra-series citations are audited. Non-Beck references are ignored.
  - Prose mentions of "Paper M" inside quoted strings, figure captions, etc.
    are still matched; false positives here are tolerated (noise < missed drift).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from zenodo_validate import load_yaml_simple, find_preprint_dir  # type: ignore


# A reference entry linking to another Δt series paper
REF_RE = re.compile(
    r"\[(\d+)\]\s*Beck,?\s*J\..*?Paper\s+(\d+)\.?\s*doi:\s*(10\.5281/zenodo\.\d+)",
    re.IGNORECASE,
)

# Prose mention: "Paper 7", "Paper 15", etc.
PROSE_MENTION_RE = re.compile(r"\bPaper\s+(\d+)\b")

# Non-body .md files
EXCLUDE_MD_NAMES = {"README.md", "NOTES.md", "paper.md"}
DRAFT_STEM = re.compile(r"^v\d+\.\d+|.*-project$|^PROJECT", re.I)


def find_body_md(d: Path) -> Path | None:
    """Pick the canonical body .md for a paper dir.

    Prefer longest non-excluded, non-draft .md by line count, with a preference
    for a stem that matches any existing .pdf in the dir.
    """
    candidates = []
    pdf_stems = {p.stem for p in d.iterdir() if p.suffix == ".pdf"}
    for p in d.iterdir():
        if p.suffix != ".md":
            continue
        if p.name in EXCLUDE_MD_NAMES:
            continue
        if DRAFT_STEM.match(p.stem):
            continue
        try:
            n_lines = sum(1 for _ in open(p))
        except Exception:
            n_lines = 0
        # Boost candidates whose stem matches an existing .pdf
        score = n_lines + (10000 if p.stem in pdf_stems else 0)
        candidates.append((score, p))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def build_paper_doi_index(preprint_dir: Path) -> dict:
    """Map paper number (int) → metadata dict (doi, zenodo_url, title)."""
    idx = {}
    for d in sorted(preprint_dir.iterdir()):
        if not d.is_dir():
            continue
        m = re.match(r"^(\d\d)-", d.name)
        if not m:
            continue
        num = int(m.group(1))
        meta_path = d / "metadata.yaml"
        if not meta_path.exists():
            continue
        meta = load_yaml_simple(meta_path)
        idx[num] = {
            "doi": meta.get("doi", ""),
            "zenodo_url": meta.get("zenodo_url", ""),
            "title": meta.get("title", ""),
            "dir": d.name,
        }
    return idx


def audit_paper(d: Path, paper_idx: dict) -> tuple[list[dict], list[str]]:
    """Returns (findings, complaints)."""
    body = find_body_md(d)
    if not body:
        return [], [f"no body .md found in {d.name}"]
    text = body.read_text(errors="ignore")
    # Separate references from prose — references typically start with "## References" or "References"
    ref_section_match = re.search(r"(?m)^#{1,3}\s*References\s*$", text)
    if ref_section_match:
        prose_text = text[:ref_section_match.start()]
        refs_text = text[ref_section_match.end():]
    else:
        prose_text = text
        refs_text = ""

    # Extract reference entries pointing to other Δt papers
    ref_entries = REF_RE.findall(refs_text or text)
    # ref_entries: list of (ref_num, paper_num, doi)

    complaints = []
    findings = []

    my_num = int(re.match(r"^(\d\d)-", d.name).group(1))

    # Prose mentions: Paper N
    prose_paper_mentions = set(int(n) for n in PROSE_MENTION_RE.findall(prose_text))
    # Exclude self-mention
    prose_paper_mentions.discard(my_num)
    cited_paper_nums = set(int(pn) for (_, pn, _) in ref_entries)

    # Check each reference entry
    for ref_num, paper_num_str, cited_doi in ref_entries:
        paper_num = int(paper_num_str)
        if paper_num not in paper_idx:
            complaints.append(f"[{ref_num}] refers to Paper {paper_num} which doesn't exist in preprint/")
            continue
        expected_doi = paper_idx[paper_num]["doi"]
        if cited_doi != expected_doi:
            complaints.append(
                f"[{ref_num}] Paper {paper_num} cites doi:{cited_doi} but metadata says doi:{expected_doi}"
            )
        findings.append({
            "ref_num": ref_num,
            "cites_paper": paper_num,
            "cited_doi": cited_doi,
            "expected_doi": expected_doi,
            "match": cited_doi == expected_doi,
        })

    # Papers mentioned in prose but not in references — this is "soft" drift:
    # possibly a missing reference entry, possibly the mention is in a passage
    # that doesn't need formal citation. Warn but tolerant.
    orphan_mentions = prose_paper_mentions - cited_paper_nums
    for orphan in sorted(orphan_mentions):
        if orphan not in paper_idx:
            continue  # Paper doesn't exist; might be forward reference or error — but don't complain here
        complaints.append(f"prose mentions Paper {orphan} but no reference entry found (may be informal mention, worth reviewing)")

    return findings, complaints


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="Emit full JSON to stdout")
    args = ap.parse_args()
    preprint_dir = find_preprint_dir()
    paper_idx = build_paper_doi_index(preprint_dir)
    dirs = sorted([d for d in preprint_dir.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name)])
    all_results = []
    fail_count = 0
    for d in dirs:
        paper_num = d.name.split("-")[0]
        findings, complaints = audit_paper(d, paper_idx)
        all_results.append({
            "paper": paper_num,
            "dir": d.name,
            "findings": findings,
            "complaints": complaints,
        })
        # Count only hard complaints (doi mismatches), not the "prose mentions X but no ref" soft warnings
        hard_complaints = [c for c in complaints if "but no reference entry found" not in c]
        if hard_complaints:
            fail_count += 1
    if args.json:
        print(json.dumps(all_results, indent=2))
    else:
        for r in all_results:
            n_refs = len(r["findings"])
            if not r["complaints"]:
                print(f"P{r['paper']} | ok    | {n_refs} intra-series ref(s) verified")
            else:
                # Check if complaints are all soft
                hard = [c for c in r["complaints"] if "but no reference entry found" not in c]
                status = "FAIL" if hard else "warn"
                print(f"P{r['paper']} | {status:5s} | {n_refs} ref(s)")
                for c in r["complaints"]:
                    prefix = "  !" if "but no reference entry found" not in c else "  ~"
                    print(f"{prefix} {c}")
    if fail_count:
        print(f"\n{fail_count} paper(s) with citation DOI mismatches (hard failures).", file=sys.stderr)
        return 1
    print("\nAll intra-series citations verified (soft warnings may still appear above).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
