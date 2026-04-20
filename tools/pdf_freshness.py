#!/usr/bin/env python3
"""Flag papers whose source .md is newer than their built output (.pdf or .docx).

Usage: python3 tools/pdf_freshness.py [--json]

For each paper dir under preprint/, pairs each paper-body .md against its built
output and reports staleness. Exits non-zero if any paired .md is newer than
its built counterpart. Unpaired .md files (drafts, project plans, supplementary
prose without a built artifact) are reported as info, not as drift.

Some papers (P06, P07, P08) publish as .docx rather than .pdf; both are treated
as valid built outputs.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


# Non-body markdown files — never pair these
EXCLUDE_MD_NAMES = {"README.md", "NOTES.md", "paper.md"}

# .md files whose stem matches these patterns are drafts/project notes, not paper bodies
DRAFT_STEM_PATTERNS = [
    re.compile(r"^v\d+\.\d+"),           # v0.1-..., v1.0-...
    re.compile(r".*-project$"),          # *-project
    re.compile(r"^PROJECT", re.I),       # PROJECT_PLAN
]

# Build-output extensions (both treated as valid paired output)
BUILT_EXTS = {".pdf", ".docx"}

# Artifact-output prefixes that aren't papers
EXCLUDE_BUILT_PREFIXES = ("figure", "fig_", "tier_", "governor-pattern")


def find_preprint_dir() -> Path:
    here = Path(__file__).resolve()
    candidate = here.parent.parent / "preprint"
    if candidate.is_dir():
        return candidate
    candidate = Path.cwd() / "preprint"
    if candidate.is_dir():
        return candidate
    raise SystemExit("Could not locate preprint/ directory")


def is_draft_stem(stem: str) -> bool:
    return any(pat.match(stem) for pat in DRAFT_STEM_PATTERNS)


def check_dir(d: Path) -> list[dict]:
    """Return list of (md, built, stale_bool, reason) for each body-md found."""
    findings = []
    mds = [p for p in d.iterdir()
           if p.suffix == ".md"
           and p.name not in EXCLUDE_MD_NAMES
           and not is_draft_stem(p.stem)]
    built = [p for p in d.iterdir()
             if p.suffix in BUILT_EXTS
             and not any(p.name.startswith(pre) for pre in EXCLUDE_BUILT_PREFIXES)
             and "figures" not in p.parts]
    # Drop drafts from built outputs too (v0.1 PDFs etc exist but aren't canonical)
    built = [p for p in built if not is_draft_stem(p.stem)]
    for md in mds:
        # Prefer same-stem match regardless of extension
        same_stem = [p for p in built if p.stem == md.stem]
        if same_stem:
            pair = same_stem[0]
        elif len(built) == 1:
            pair = built[0]
        else:
            # Pick the most-specific same-extension-family match if any; else report unpaired
            findings.append({
                "md": md.name,
                "built": None,
                "stale": False,
                "reason": f"no unambiguous build pair (built files: {sorted(p.name for p in built) or 'none'})",
            })
            continue
        md_mtime = md.stat().st_mtime
        built_mtime = pair.stat().st_mtime
        stale = md_mtime > built_mtime
        findings.append({
            "md": md.name,
            "built": pair.name,
            "md_mtime": md_mtime,
            "built_mtime": built_mtime,
            "delta_seconds": round(md_mtime - built_mtime, 1),
            "stale": stale,
        })
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="Emit full JSON to stdout")
    args = ap.parse_args()
    preprint_dir = find_preprint_dir()
    dirs = sorted([d for d in preprint_dir.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name)])
    results = []
    stale_count = 0
    for d in dirs:
        paper_num = d.name.split("-")[0]
        findings = check_dir(d)
        for f in findings:
            f["paper"] = paper_num
            f["dir"] = d.name
            if f.get("stale"):
                stale_count += 1
            results.append(f)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            if "reason" in r:
                print(f"P{r['paper']} | info  | {r['md']} | {r['reason']}")
            elif r.get("stale"):
                delta = r["delta_seconds"]
                days = delta / 86400
                print(f"P{r['paper']} | STALE | {r['md']} is {days:.1f}d newer than {r['built']} — rebuild needed")
            else:
                print(f"P{r['paper']} | ok    | {r['md']} ← {r['built']}")
    if stale_count:
        print(f"\n{stale_count} stale build(s). Rebuild before upload.", file=sys.stderr)
        return 1
    print("\nAll built outputs fresh.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
