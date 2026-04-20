#!/usr/bin/env python3
"""Verify every DOI cited in every paper body resolves to what it claims to cite.

Usage: python3 tools/doi_validate.py [--json] [--only PNN[,PNN...]]

For each paper body .md, extracts every DOI (pattern: 10.\\d+/...), resolves it
against Zenodo (for 10.5281/zenodo.*) or CrossRef (for others), fetches the
resolved title, and compares it against the cited title text that appears
immediately before or around the DOI in the reference list.

Exits non-zero on any DOI that fails to resolve OR resolves to something
substantially different from what's cited.

This exists because citation_graph.py only audits intra-series DOIs (those with
a "Δt Framework Paper N" tag). Hallucinated DOIs to non-series works — e.g., a
model-generated DOI that happens to hit a real stranger's paper — are
structurally invisible to that tool. This tool covers that gap.

Origin: 2026-04-20. Motivated by discovering that P19 ref [10] and P22 refs
[1,3] had shipped to Zenodo with hallucinated DOIs pointing at real unrelated
papers (meconium biomarker, skill-gap analysis). Manual review provably cannot
catch this class; 8-digit Zenodo IDs are not human-distinguishable.

Rate: polite 1 req/sec. ~10-30 DOIs per paper, 22 papers → a few minutes.
Results are cached in tools/.doi_cache.json across runs.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from zenodo_validate import find_preprint_dir, load_yaml_simple  # type: ignore


CACHE_PATH = Path(__file__).parent / ".doi_cache.json"
USER_AGENT = "dt-framework-doi-check/1.0 (mailto:jmbeck@gmail.com)"

# DOI pattern. Match up to whitespace / quote / angle bracket / markdown link
# terminator ']'. DOIs can contain parens (e.g. 10.1016/S0925-7535(97)00026-X),
# so we don't treat () as boundaries in the regex; unmatched trailing ')' is
# trimmed in the loop. Trailing sentence punctuation also stripped there.
DOI_RE = re.compile(r"\b(10\.\d{4,}/[^\s\"'<>\]]+)")
# Reference-entry heuristic: find the paragraph containing the DOI, strip the DOI itself
# to recover cited title candidate.

STOPWORDS = set("""
a an and are as at be by for from has have he in is it its of on or that the
their this to was were will with we you do does not can could should would may
might been being he she they them i via ii iii iv v vi vii viii ix x
""".split())


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2))


def http_get(url: str, accept: str = "application/json") -> tuple[int, str]:
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": accept,
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode(errors="ignore")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="ignore") if e.fp else ""
    except Exception as e:
        return 0, f"(error: {e})"


def resolve_doi(doi: str, cache: dict) -> dict:
    """Return {status, title, source} dict. Cached."""
    if doi in cache:
        return cache[doi]
    result = {"doi": doi}
    if doi.startswith("10.5281/zenodo."):
        record_id = doi.split(".")[-1]
        code, body = http_get(f"https://zenodo.org/api/records/{record_id}")
        if code == 200:
            try:
                j = json.loads(body)
                result["status"] = "ok"
                result["title"] = j.get("metadata", {}).get("title", "")
                result["source"] = "zenodo"
            except Exception:
                result["status"] = "parse_error"
                result["source"] = "zenodo"
        elif code == 302:
            # follow redirect once
            m = re.search(r"/api/records/(\d+)", body)
            if m:
                code, body = http_get(f"https://zenodo.org/api/records/{m.group(1)}")
                if code == 200:
                    j = json.loads(body)
                    result["status"] = "ok"
                    result["title"] = j.get("metadata", {}).get("title", "")
                    result["source"] = "zenodo"
                else:
                    result["status"] = f"redirect_http_{code}"
                    result["source"] = "zenodo"
            else:
                result["status"] = "redirect_no_target"
                result["source"] = "zenodo"
        else:
            result["status"] = f"http_{code}"
            result["source"] = "zenodo"
    else:
        # Try CrossRef
        code, body = http_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")
        if code == 200:
            try:
                j = json.loads(body)
                titles = j.get("message", {}).get("title", [])
                result["status"] = "ok"
                result["title"] = titles[0] if titles else ""
                result["source"] = "crossref"
            except Exception:
                result["status"] = "parse_error"
                result["source"] = "crossref"
        else:
            result["status"] = f"http_{code}"
            result["source"] = "crossref"
    cache[doi] = result
    time.sleep(1)  # polite
    return result


def normalize_title(s: str) -> set[str]:
    """Return set of significant lowercased words from a title string."""
    # Strip LaTeX / markdown noise
    s = re.sub(r"[\\$*_\[\]{}()`~<>]", " ", s)
    s = re.sub(r"[^\w\s-]", " ", s)
    words = set()
    for w in s.lower().split():
        w = w.strip("-")
        if len(w) < 4:
            continue
        if w in STOPWORDS:
            continue
        if w.isdigit():
            continue
        words.add(w)
    return words


def titles_plausibly_match(cited: str, resolved: str) -> bool:
    """Fuzzy check: do the two titles share enough significant words?"""
    c = normalize_title(cited)
    r = normalize_title(resolved)
    if not c or not r:
        return False
    overlap = c & r
    # Require at least 3 words shared AND overlap covers ≥ 40% of shorter set
    if len(overlap) < 3:
        return False
    shorter = min(len(c), len(r))
    return len(overlap) / shorter >= 0.4


def extract_cited_title_around_doi(text: str, doi: str) -> str:
    """Extract the reference entry containing this DOI, then pull the title from it.

    Strategy:
      1. Find the DOI's position.
      2. Work backward to find the start of the current reference entry. A
         reference entry starts either with a bracketed number "[N]" at line
         start, or with a blank line. We take the nearest such boundary.
      3. From the entry text, peel off the title. Titles are typically between
         the author block and the venue, often delimited by periods, but
         citation styles vary (APA: "Author (YYYY). Title."; Chicago: "Author,
         'Title,' Venue, YYYY."; Beck's own style: "Beck, J. (YYYY). Title.").
         Strategy is permissive: take the longest sentence-like unit in the
         entry that's not the author line and not obviously venue/metadata.
    """
    idx = text.find(doi)
    if idx == -1:
        return ""
    # Work backward to find entry start
    window_start = max(0, idx - 1500)
    window = text[window_start:idx]
    # Candidate starts: [N], or blank line
    # Find the LATEST such boundary (closest to the DOI)
    boundary_re = re.compile(r"(?:^|\n)(?:\[\d+\]|\n)")
    starts = [m.end() for m in boundary_re.finditer(window)]
    if starts:
        entry_start = starts[-1]
        entry = window[entry_start:]
    else:
        entry = window[-500:]
    # Normalize whitespace
    entry = re.sub(r"\s+", " ", entry).strip()
    # If entry leads with author list (typical: "Beck, J." or "Author et al."),
    # drop up to the LAST (YYYY) pattern — last because adjacent reference entries
    # without blank-line separation (bullet style) will have multiple (YYYY) in the
    # window, and the one immediately preceding the DOI is the one we want.
    year_matches = list(re.finditer(r"\(\d{4}[a-z]?\)\.?\s*", entry))
    if year_matches:
        m = year_matches[-1]
        after_year = entry[m.end():]
    else:
        # Try ", YYYY," or ", YYYY." or trailing YYYY
        m = re.search(r",\s*\d{4}[a-z]?[,.]?", entry)
        if m:
            # Chicago style: title is BEFORE the year, not after. Take text up to year.
            # But also often in quotes. Handle that too.
            before_year = entry[:m.start()]
            # Strip leading author; author is usually before first "," that has
            # no matching quote. Just take the quoted portion if any.
            qm = re.search(r'["\u201c]([^"\u201d]+)["\u201d]', before_year)
            if qm:
                return qm.group(1).strip()
            # Else split on ", " and take the longest chunk
            chunks = [c.strip() for c in before_year.split(", ") if c.strip()]
            if chunks:
                chunks.sort(key=len, reverse=True)
                return chunks[0]
            return before_year.strip()
        else:
            after_year = entry
    # Now we're in APA-style territory. Title is first period-delimited unit,
    # possibly containing further punctuation. Strip up to doi: marker.
    after_year = after_year.split("doi:")[0]
    # Split on ". " and take longest of the first 3 chunks
    parts = [p.strip() for p in after_year.split(". ") if p.strip()]
    if not parts:
        return after_year.strip()
    # Title usually isn't the last (venue) or first shortest; take longest of first 3
    head = parts[:3]
    head.sort(key=len, reverse=True)
    return head[0].strip()


# File selection (same conventions as citation_graph.py)
EXCLUDE_MD_NAMES = {"README.md", "NOTES.md", "paper.md"}
DRAFT_STEM = re.compile(r"^v\d+\.\d+|.*-project$|^PROJECT", re.I)


def find_body_md(d: Path) -> Path | None:
    pdf_stems = {p.stem for p in d.iterdir() if p.suffix == ".pdf"}
    candidates = []
    for p in d.iterdir():
        if p.suffix != ".md" or p.name in EXCLUDE_MD_NAMES or DRAFT_STEM.match(p.stem):
            continue
        try:
            n_lines = sum(1 for _ in open(p))
        except Exception:
            n_lines = 0
        score = n_lines + (10000 if p.stem in pdf_stems else 0)
        candidates.append((score, p))
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def audit_paper(d: Path, cache: dict) -> tuple[list[dict], list[str]]:
    body = find_body_md(d)
    if not body:
        return [], [f"no body .md found in {d.name}"]
    text = body.read_text(errors="ignore")
    # Self-DOIs from this paper's own metadata — these appear in the paper
    # header and shouldn't be validated as citations.
    meta_path = d / "metadata.yaml"
    self_dois: set[str] = set()
    if meta_path.exists():
        meta = load_yaml_simple(meta_path)
        for fld in ("doi",):
            v = meta.get(fld, "")
            if v:
                self_dois.add(v.strip().rstrip(".,;:"))
        # Also suppress the record ID from zenodo_url
        zu = meta.get("zenodo_url", "")
        m = re.search(r"/records/(\d+)", zu or "")
        if m:
            self_dois.add(f"10.5281/zenodo.{m.group(1)}")
    # Join hyphenated line-wraps (e.g. "10.5281/zen-\nodo.17859324" → "10.5281/zenodo.17859324")
    # — an artifact of docx/LaTeX typesetting that slipped into source. Removing
    # the hyphen-newline entirely is correct for wrapped words; in the rare case
    # of a real hyphen at EOL, this would over-join, but markdown source doesn't
    # typically carry such hyphens.
    text = re.sub(r"-\n\s*", "", text)
    # Find DOIs
    dois = []
    seen = set()
    for m in DOI_RE.finditer(text):
        doi = m.group(1)
        # Strip trailing sentence punctuation AND unmatched closing brackets.
        # DOIs can contain (), but if a DOI ends with ) without matching (, it's
        # likely from a wrapping like "cite (... doi:X)".
        while doi and doi[-1] in ".,;:":
            doi = doi[:-1]
        # Balance parens: if more ) than ( at end, trim unmatched trailing )
        while doi.endswith(")") and doi.count("(") < doi.count(")"):
            doi = doi[:-1]
        # Trim trailing ] or }
        while doi and doi[-1] in "]}":
            doi = doi[:-1]
        if not doi or doi in seen or doi in self_dois:
            continue
        seen.add(doi)
        dois.append(doi)

    findings = []
    complaints = []
    for doi in dois:
        resolved = resolve_doi(doi, cache)
        cited_title = extract_cited_title_around_doi(text, doi)
        resolved_title = resolved.get("title", "")
        status = resolved.get("status", "?")
        finding = {
            "doi": doi,
            "status": status,
            "source": resolved.get("source"),
            "cited_title": cited_title[:100],
            "resolved_title": resolved_title[:100],
        }
        if status != "ok":
            complaints.append(f"{doi}: does not resolve ({status})")
            finding["match"] = False
        elif cited_title and not titles_plausibly_match(cited_title, resolved_title):
            complaints.append(
                f"{doi}: cited title does not match resolved title\n"
                f"    cited:    {cited_title[:120]}\n"
                f"    resolved: {resolved_title[:120]}"
            )
            finding["match"] = False
        else:
            finding["match"] = True
        findings.append(finding)
    return findings, complaints


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--only", default="", help="Comma-separated paper numbers (e.g. --only 19,22)")
    ap.add_argument("--no-cache", action="store_true", help="Ignore existing cache (still writes new cache)")
    args = ap.parse_args()
    preprint_dir = find_preprint_dir()
    cache = {} if args.no_cache else load_cache()
    filter_set = set()
    if args.only:
        filter_set = set(n.strip().lstrip("P").zfill(2) for n in args.only.split(","))
    dirs = sorted([d for d in preprint_dir.iterdir() if d.is_dir() and re.match(r"^\d\d-", d.name)])
    all_results = []
    fail_count = 0
    total_dois = 0
    for d in dirs:
        paper_num = d.name.split("-")[0]
        if filter_set and paper_num not in filter_set:
            continue
        findings, complaints = audit_paper(d, cache)
        save_cache(cache)  # incremental; resume-friendly
        all_results.append({"paper": paper_num, "findings": findings, "complaints": complaints})
        total_dois += len(findings)
        if complaints:
            fail_count += 1
        if not args.json:
            status = "ok" if not complaints else "FAIL"
            print(f"P{paper_num} | {status:5s} | {len(findings)} DOI(s), {len(complaints)} issue(s)")
            for c in complaints:
                for line in c.split("\n"):
                    print(f"  ! {line}")
    save_cache(cache)
    if args.json:
        print(json.dumps(all_results, indent=2))
    if fail_count:
        print(f"\n{fail_count} paper(s) have DOI issues ({total_dois} DOIs checked).", file=sys.stderr)
        return 1
    print(f"\nAll {total_dois} DOI(s) resolve to plausibly-matching sources.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
