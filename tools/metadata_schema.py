#!/usr/bin/env python3
"""Verify metadata.yaml files across preprints share a consistent field schema.

Usage: python3 tools/metadata_schema.py [--json]

Checks:
  - required fields present (title, author, date, doi, zenodo_url, version, keywords, abstract)
  - DOI format resembles a Zenodo DOI (10.5281/zenodo.NNNN)
  - zenodo_url format is canonical (https://zenodo.org/records/NNNN)
  - version is non-empty and looks like a semver fragment
  - no duplicate top-level YAML keys (structural invalid; see zenodo_validate.load_yaml_simple)
  - title non-empty
  - keywords is a list with at least one entry
  - abstract is non-empty

Exits non-zero if any paper fails any check.

This validator focuses on cross-paper consistency. It doesn't enforce a single
"right" schema beyond what the corpus already uses; it flags outliers.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Import the shared YAML loader from the sibling zenodo_validate module
sys.path.insert(0, str(Path(__file__).parent))
from zenodo_validate import load_yaml_simple, find_preprint_dir  # type: ignore


REQUIRED_FIELDS = [
    "title",
    "author",
    "date",
    "doi",
    "zenodo_url",
    "version",
    "keywords",
    "abstract",
]

DOI_RE = re.compile(r"^10\.5281/zenodo\.\d+$")
ZENODO_URL_RE = re.compile(r"^https://zenodo\.org/records/\d+$")
VERSION_RE = re.compile(r"^\d+(\.\d+){0,2}$")


def check_paper(meta_path: Path) -> list[str]:
    """Return list of human-readable complaint strings. Empty list = clean."""
    complaints = []
    try:
        meta = load_yaml_simple(meta_path)
    except Exception as e:
        return [f"parse error: {e}"]

    if meta.get("_duplicates"):
        for dup in meta["_duplicates"]:
            complaints.append(f"duplicate top-level YAML key: '{dup}'")

    # Required fields
    for fld in REQUIRED_FIELDS:
        val = meta.get(fld)
        if val is None or val == "" or val == []:
            complaints.append(f"missing required field: '{fld}'")

    # DOI format
    doi = meta.get("doi", "")
    if doi and not DOI_RE.match(doi):
        complaints.append(f"doi format unexpected: {doi!r} (expected 10.5281/zenodo.NNNN)")

    # zenodo_url format
    zu = meta.get("zenodo_url", "")
    if zu and not ZENODO_URL_RE.match(zu):
        complaints.append(f"zenodo_url format non-canonical: {zu!r} (expected https://zenodo.org/records/NNNN)")

    # Version format
    ver = meta.get("version", "")
    if ver and not VERSION_RE.match(str(ver)):
        complaints.append(f"version format unexpected: {ver!r} (expected N or N.N or N.N.N)")

    # Keywords should be a list
    kw = meta.get("keywords", [])
    if kw and not isinstance(kw, list):
        complaints.append(f"keywords is not a list: {type(kw).__name__}")

    return complaints


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="Emit full JSON to stdout")
    args = ap.parse_args()
    preprint_dir = find_preprint_dir()
    dirs = sorted([d for d in preprint_dir.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name)])
    results = []
    fail_count = 0
    for d in dirs:
        paper_num = d.name.split("-")[0]
        meta_path = d / "metadata.yaml"
        if not meta_path.exists():
            complaints = ["no metadata.yaml"]
        else:
            complaints = check_paper(meta_path)
        results.append({"paper": paper_num, "dir": d.name, "complaints": complaints})
        if complaints:
            fail_count += 1
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            if r["complaints"]:
                print(f"P{r['paper']} | FAIL")
                for c in r["complaints"]:
                    print(f"  - {c}")
            else:
                print(f"P{r['paper']} | ok")
    if fail_count:
        print(f"\n{fail_count} paper(s) failed schema check.", file=sys.stderr)
        return 1
    print("\nAll metadata.yaml files conform to schema.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
