#!/usr/bin/env python3
"""Validate source metadata.yaml vs Zenodo record state for each preprint.

Usage: python3 tools/zenodo_validate.py [--json]

Compares, for every paper under preprint/:
  - source metadata.yaml (version, doi, zenodo_url, title)
  - Zenodo record state reached via the zenodo_url

Exits non-zero if drift is detected (except for deliberate v1.x-candidate drift
where source version is AHEAD of Zenodo — those are pre-push candidates, not
defects). Ahead-detection requires BOTH source and Zenodo to have explicit
version strings; see `tools/README.md` for the known limitation.

No API token required for validation (GET /api/records/{id} is public). The
write-scoped token at ~/git/claude/zenodo/deposit-write is used only if we ever
extend this to push operations.

What counts as drift:
  * record_id in zenodo_url doesn't resolve (404 or fetch error)
  * title mismatch between source and Zenodo
  * source version BEHIND Zenodo version (Zenodo got pushed, source never updated)

What doesn't count as drift:
  * source version AHEAD of Zenodo (pre-push candidate; expected during release work)
  * Zenodo version field empty while source has a version (Zenodo hygiene gap, not defect)
  * minor format differences like "1.0" vs "1.0.0"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path


def load_yaml_simple(path: Path) -> dict:
    """Tiny YAML parser good enough for our metadata.yaml format.

    Handles scalar keys, quoted strings, block scalars (| and >), and simple lists.
    Does not handle nested mappings; our metadata.yaml doesn't use them.

    Tracks duplicate top-level keys in `_duplicates` (list of key names that
    appeared more than once at top level). Downstream code is responsible for
    treating duplicates as a hard validation failure — duplicate keys are a
    YAML footgun that let a file look "updated" to a human skimming while
    different parsers read different values. Found in the wild (P05 metadata,
    2026-04-20) where an earlier bump-attempt appended a second `version:` line
    that silently lost to the original.
    """
    out: dict = {}
    seen_keys: list[str] = []  # order of first appearance
    duplicates: list[str] = []
    current_key = None
    in_block = False
    block_lines: list[str] = []
    block_indent: int | None = None
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if in_block:
                if line.startswith(" " * (block_indent or 2)) or not line.strip():
                    block_lines.append(line)
                    continue
                else:
                    out[current_key] = "\n".join(block_lines).strip()
                    in_block = False
                    block_lines = []
            m = re.match(r"^([a-zA-Z_][\w_]*):\s*(.*)$", line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if key in seen_keys and key not in duplicates:
                    duplicates.append(key)
                else:
                    seen_keys.append(key)
                if val in ("|", ">"):
                    current_key = key
                    in_block = True
                    block_indent = 2
                    block_lines = []
                elif val == "":
                    current_key = key
                    out[key] = []
                else:
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    out[key] = val
            elif line.lstrip().startswith("- "):
                if isinstance(out.get(current_key), list):
                    out[current_key].append(line.lstrip()[2:].strip())
    if in_block:
        out[current_key] = "\n".join(block_lines).strip()
    if duplicates:
        out["_duplicates"] = duplicates
    return out


def extract_record_id(zenodo_url: str) -> str:
    m = re.search(r"/records/(\d+)", zenodo_url or "")
    if m:
        return m.group(1)
    # Tolerate doi.org URLs as a fallback; extract trailing zenodo.N
    m = re.search(r"zenodo\.(\d+)", zenodo_url or "")
    return m.group(1) if m else ""


def fetch_record(record_id: str) -> dict:
    url = f"https://zenodo.org/api/records/{record_id}"
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"_error": str(e)}


def version_tuple(v: str) -> tuple:
    """Parse "1.0", "1.1", "1.0.0" into comparable tuples. Non-numeric → empty.

    Trailing zeros are stripped so "1.0" and "1.0.0" compare equal semantically.
    """
    if not v or v in ("(none)", "null"):
        return ()
    parts = []
    for p in v.split("."):
        try:
            parts.append(int(p))
        except ValueError:
            return ()
    # Strip trailing zeros so (1,0) and (1,0,0) both canonicalize to (1,)
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def find_preprint_dir() -> Path:
    """Locate the preprint/ directory relative to this script's repo root."""
    here = Path(__file__).resolve()
    # tools/zenodo_validate.py → ../preprint
    candidate = here.parent.parent / "preprint"
    if candidate.is_dir():
        return candidate
    # Fall back to CWD-relative
    candidate = Path.cwd() / "preprint"
    if candidate.is_dir():
        return candidate
    raise SystemExit("Could not locate preprint/ directory")


def validate() -> tuple[list[dict], list[str]]:
    """Returns (results, drift_messages). drift_messages is empty → clean."""
    results = []
    drifts = []
    preprint_dir = find_preprint_dir()
    dirs = sorted([d for d in preprint_dir.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name)])
    for d in dirs:
        meta_path = d / "metadata.yaml"
        paper_num = d.name.split("-")[0]
        if not meta_path.exists():
            drifts.append(f"P{paper_num}: no metadata.yaml")
            continue
        src = load_yaml_simple(meta_path)
        if src.get("_duplicates"):
            for dup in src["_duplicates"]:
                drifts.append(f"P{paper_num}: duplicate top-level YAML key '{dup}' in metadata.yaml (structurally invalid — different parsers may read different values)")
        zen_url = src.get("zenodo_url", "")
        record_id = extract_record_id(zen_url)
        if not record_id:
            drifts.append(f"P{paper_num}: cannot extract record id from zenodo_url={zen_url!r}")
            results.append({"paper": paper_num, "dir": d.name, "error": "no record id"})
            continue
        rec = fetch_record(record_id)
        if "_error" in rec:
            drifts.append(f"P{paper_num}: record {record_id} fetch failed: {rec['_error']}")
            results.append({"paper": paper_num, "dir": d.name, "record_id": record_id, "error": rec["_error"]})
            continue
        zen_meta = rec.get("metadata", {})
        zen_version = zen_meta.get("version") or "(none)"
        zen_title = zen_meta.get("title", "")
        src_title = src.get("title", "")
        src_version = src.get("version", "(none)")
        # Drift detection
        if src_title and zen_title and src_title.strip() != zen_title.strip():
            drifts.append(f"P{paper_num}: title mismatch (src={src_title[:60]!r} zen={zen_title[:60]!r})")
        st = version_tuple(src_version)
        zt = version_tuple(zen_version)
        if st and zt and st < zt:
            drifts.append(f"P{paper_num}: source version {src_version} is BEHIND Zenodo version {zen_version} (Zenodo pushed without source update)")
        # src > zen is a pre-push candidate; not a drift
        results.append({
            "paper": paper_num,
            "dir": d.name,
            "src_version": src_version,
            "src_doi": src.get("doi", "?"),
            "record_id": record_id,
            "zen_version": zen_version,
            "zen_pub": zen_meta.get("publication_date", ""),
            "zen_concept_doi": rec.get("conceptdoi", ""),
            "ahead_of_zenodo": bool(st and zt and st > zt),
        })
    return results, drifts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="Emit full JSON to stdout")
    args = ap.parse_args()
    results, drifts = validate()
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            if "error" in r:
                print(f"P{r['paper']} | ERROR: {r['error']}")
                continue
            marker = " ←PUSH?" if r.get("ahead_of_zenodo") else ""
            print(f"P{r['paper']} | src:{r['src_version']} | zen:{r['zen_version']} | pub:{r['zen_pub']} | id:{r['record_id']}{marker}")
    if drifts:
        print("\nDRIFT:", file=sys.stderr)
        for d in drifts:
            print(f"  {d}", file=sys.stderr)
        return 1
    print("\nNo drift detected. (Pre-push candidates are marked ←PUSH? and not counted as drift.)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
