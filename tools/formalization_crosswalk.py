#!/usr/bin/env python3
"""Verify that theorem names cited in the formalization index actually exist in the Lean repo.

Usage: python3 tools/formalization_crosswalk.py [--json]

Parses papers/docs/formalization-index.md and each paper's README for backtick-
quoted theorem names (e.g., `idle_preserves_capacity`, `persistence_normalizes`).
Then greps the Lean repo at ~/git/lean/LeanProofs/ for those names. Reports any
names cited in the papers repo that can't be found in Lean source — those are
either renamed theorems, removed theorems, or citation typos.

Exits non-zero on any unresolved theorem citation.

Heuristic notes:
  - Only snake_case identifiers of length ≥ 10 are considered, to avoid false
    matches on Lean keywords or short labels like `aligned`, `detach`, etc.
  - Cites that appear in prose inside quotes or discussion (not as formal
    theorem pointers) are still scanned — noise tolerated over missed drift.
  - The Lean repo is expected at ~/git/lean; if not found, the tool skips.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


LEAN_REPO = Path.home() / "git" / "lean"
PAPERS_REPO = Path(__file__).resolve().parent.parent

# Known Lean identifiers we expect to see cited. snake_case, ≥ 10 chars.
# Empty list means: extract all; use length+snake heuristic.
BACKTICK_RE = re.compile(r"`([a-z][a-z0-9_]{9,})`")

# Files in papers repo that reference Lean work.
# Scope is narrow on purpose: these are the canonical crosswalk artifacts, and
# other files (paper bodies, NOTES.md) contain too many false-positive
# backtick-snake_case tokens (JSON schema fields, etc.) for this blunt heuristic.
CANDIDATE_FILES = [
    "docs/formalization-index.md",
]

# Extract identifiers only from sections of P18 that are specifically about the
# Lean formalization. Outside those sections, backtick snake_case tokens are
# overwhelmingly schema fields / pseudocode names, not Lean theorems.
# Key: path relative to papers repo. Value: section heading(s) that bracket
# the region where Lean identifiers are expected.
SCOPED_FILES = {
    "preprint/18-unauthorized-durability/unauthorized_durability.md": {
        "start_heading_re": re.compile(r"^## Appendix A", re.M),
        "end_heading_re": re.compile(r"^## Acknowledgments", re.M),
    },
}

LEAN_KEYWORD_BLACKLIST: set[str] = set()  # Not needed now that scope is narrow


def extract_lean_identifiers(text: str) -> set[str]:
    """Extract plausible Lean theorem/definition identifiers from text.

    Returns the set of backtick-quoted snake_case tokens that aren't
    obviously a non-Lean word.
    """
    ids = set()
    for m in BACKTICK_RE.finditer(text):
        name = m.group(1)
        if "_" not in name:
            # Multi-word snake_case only; this rules out plain words
            continue
        if name in LEAN_KEYWORD_BLACKLIST:
            continue
        ids.add(name)
    return ids


def find_in_lean(identifier: str, lean_files: list[Path]) -> list[Path]:
    """Return list of .lean files containing a definition/theorem with this name."""
    hits = []
    # Match `theorem X`, `lemma X`, `def X`, `axiom X` etc at word boundary
    pattern = re.compile(rf"\b{re.escape(identifier)}\b")
    for f in lean_files:
        try:
            if pattern.search(f.read_text()):
                hits.append(f)
        except Exception:
            continue
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="Emit full JSON to stdout")
    args = ap.parse_args()

    if not LEAN_REPO.exists():
        print(f"Lean repo not found at {LEAN_REPO}; skipping formalization crosswalk.", file=sys.stderr)
        return 0

    # Restrict scanning to author's project sources. Avoid `.lake/` (Lean package
    # cache, mathlib etc — gigabytes of files unrelated to the formalization).
    lean_files = []
    for src_root in [LEAN_REPO / "LeanProofs"]:
        if src_root.exists():
            lean_files += list(src_root.glob("*.lean"))
    # .py files at the top of the lean repo (e.g., dc_dh_persistence.py)
    if LEAN_REPO.exists():
        lean_files += list(LEAN_REPO.glob("*.py"))
    # Also scan babyriver Lean sources if present
    babyriver_lean = Path.home() / "git" / "babyriver" / "lean" / "BabyRiver"
    if babyriver_lean.exists():
        lean_files += list(babyriver_lean.glob("*.lean"))

    all_results = []
    unresolved_count = 0

    # Files scanned in full
    scan_list = [(rel, None) for rel in CANDIDATE_FILES]
    # Files scanned in scoped sections only
    for rel, scope in SCOPED_FILES.items():
        scan_list.append((rel, scope))

    for rel, scope in scan_list:
        path = PAPERS_REPO / rel
        if not path.exists():
            all_results.append({"file": rel, "status": "skipped", "reason": "file not present"})
            continue
        text = path.read_text(errors="ignore")
        if scope:
            start_m = scope["start_heading_re"].search(text)
            end_m = scope["end_heading_re"].search(text)
            if start_m:
                end_pos = end_m.start() if end_m else len(text)
                text = text[start_m.start():end_pos]
            else:
                all_results.append({"file": rel, "status": "skipped", "reason": "scope section not found"})
                continue
        ids = extract_lean_identifiers(text)
        file_result = {"file": rel, "ids_found": sorted(ids), "unresolved": []}
        for identifier in sorted(ids):
            hits = find_in_lean(identifier, lean_files)
            if not hits:
                file_result["unresolved"].append(identifier)
                unresolved_count += 1
        all_results.append(file_result)

    if args.json:
        print(json.dumps(all_results, indent=2))
    else:
        for r in all_results:
            if r.get("status") == "skipped":
                print(f"{r['file']} | skipped: {r['reason']}")
                continue
            n = len(r.get("ids_found", []))
            unres = r.get("unresolved", [])
            if not unres:
                print(f"{r['file']} | ok    | {n} Lean identifier(s), all resolved")
            else:
                print(f"{r['file']} | FAIL  | {n} ident(s), {len(unres)} unresolved:")
                for u in unres:
                    print(f"  ! {u}")

    if unresolved_count:
        print(f"\n{unresolved_count} Lean identifier citation(s) could not be resolved.", file=sys.stderr)
        return 1
    print("\nAll Lean identifier citations resolve to source in the Lean repo.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
