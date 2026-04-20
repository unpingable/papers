# tools/

Small operational scripts for the papers repo. Not part of any paper's content; here so they have a durable location and don't live in `/tmp/` or scroll out of shell history.

## Quick start

Before pushing papers to Zenodo, run the combined checker:

```bash
tools/check_all.sh
```

It runs all five validators in sequence and exits non-zero if any fail. Individual scripts can also be run directly; each supports `--json` for machine-readable output.

## Validators

## `zenodo_validate.py`

Cross-checks every `preprint/NN-.../metadata.yaml` against the live Zenodo record it points at. Catches the kinds of drift that accumulate across a 20+ paper corpus:

- broken `zenodo_url` record IDs (typos, format inconsistency)
- title mismatch between source and Zenodo
- source `version` string *behind* Zenodo (indicates a push happened without updating source — this is the most dangerous class of drift, because it turns source into a lie-about-published-state)

**Usage:**

```bash
python3 tools/zenodo_validate.py            # summary table, exits non-zero if drift
python3 tools/zenodo_validate.py --json     # full JSON dump of state per paper
```

Papers where source version is *ahead* of Zenodo are marked `←PUSH?` in the summary output. Those are release-candidate drifts (expected during the window between local v1.x candidate edits and the Zenodo push), not defects. The exit code treats them as clean.

**Known limitation (ahead-detection):** The validator can only detect "ahead" reliably when both source and Zenodo have explicit version strings. A large fraction of the corpus's Zenodo records have no `version` field in their metadata (Zenodo hygiene gap), so a paper like P18 with source `version: "1.1"` and Zenodo `version: (none)` won't be flagged as a push candidate here. Track push-candidate status in each paper's `NOTES.md` changelog and README instead. The validator's reliable signal is BEHIND drift (source lagging a pushed Zenodo version), which is the higher-stakes direction anyway.

**When to run:**

- **Before any Zenodo push.** Catches source/Zenodo mismatch so you don't push a `v1.1` whose source still claims `v1.0`.
- **When a memory says something like "DOI reserved" or "pre-release draft"** — those can go stale silently once a paper is published. The validator confirms or refutes the memory.
- **Occasional periodic check.** Once every few weeks is fine for a small corpus.

**What it does not do:**

- It does not push anything. Pure read-only validation. The write-scoped Zenodo token at `~/git/claude/zenodo/deposit-write` is not used by this script.
- It does not fix drift. It reports. Fixes are manual (edit `metadata.yaml`, rebuild PDF, etc.).
- It does not touch PDFs, READMEs, paper body files, or changelog entries. If those drift in sync with `metadata.yaml`, the validator catches the metadata layer only.

**Origin note:**

Written 2026-04-20 during a state-validation pass that found three source-level drifts (P05 version behind Zenodo, P15 zenodo_url typo, P19 URL format inconsistency). Chatty's frame at the time: "paper ecosystem needed its own observability pass." Promoting the script from `/tmp/` to `tools/` institutionalizes the check so the next ops cycle doesn't start from scratch.

## `pdf_freshness.py`

For each paper dir, compares the source `.md` mtime against the built output (`.pdf` or `.docx`). Flags papers where the source has been edited more recently than the build — the canonical "edited source, forgot to rebuild" signal.

```bash
python3 tools/pdf_freshness.py
```

Ignores drafts (`v0.*-*.md`, `*-project.md`, `PROJECT_PLAN.md`), README/NOTES/paper.md, and figure-output PDFs.

## `metadata_schema.py`

Checks every `metadata.yaml` for schema conformance: required fields present, DOI format, zenodo_url format, version format, no duplicate top-level YAML keys. Catches structural metadata defects like the P05 duplicate-`version:` bug that silently lost one of the values to the YAML parser.

```bash
python3 tools/metadata_schema.py
```

## `citation_graph.py`

Parses each paper's body for reference-list entries pointing to other Δt-series papers (`Beck, J. ... Paper N. doi:10.5281/zenodo.NNNN`) and verifies that the cited DOI matches the actual paper's `metadata.yaml`. Hard-fails on DOI mismatches (embarrassing citation errors); soft-warns on Paper-N prose mentions without corresponding reference entries.

```bash
python3 tools/citation_graph.py
```

Caught on first run: P19 [10] and P22 [1,3] citing completely unrelated Zenodo records (a meconium biomarker paper, a service industry paper). Real content-level drift.

## `doi_validate.py`

For every DOI cited in every paper body, resolves it (Zenodo API for `10.5281/zenodo.*`, CrossRef for others) and compares the resolved title against the title text in the citation. Flags hallucinated DOIs — the failure mode where a model-generated number happens to hit a real stranger's paper on Zenodo or DOI.org.

```bash
python3 tools/doi_validate.py             # full sweep (uses ./tools/.doi_cache.json)
python3 tools/doi_validate.py --only 20,21
python3 tools/doi_validate.py --no-cache  # force refresh
```

The tool fills the gap left by `citation_graph.py`, which only audits intra-series references tagged with "Paper N". Hallucinated DOIs to non-series works are invisible to that tool because they have no "Paper N" tag.

Caveats:
- Runs a polite 1 req/sec rate. Full sweep takes a few minutes the first time.
- Cache at `tools/.doi_cache.json` persists resolved metadata across runs.
- The cited-title extractor is heuristic and handles APA / Chicago / arXiv-ish styles. Self-DOIs from each paper's own metadata are suppressed. Complex reference formats may occasionally mis-extract; when that happens, the "cited" text in the complaint looks garbled but the real-hallucination cases look cleanly like "paper X title" vs "totally different paper".

Origin: 2026-04-20. Built after `citation_graph.py` caught 3 hallucinated intra-series DOIs and we wanted protection against the broader class. On first full run, found 8 more hallucinated citations across P03, P04, P06, P12, P20, P21 — exactly the class the tool was built to catch.

## `formalization_crosswalk.py`

Verifies that Lean theorem names cited in `docs/formalization-index.md` and in P18's Appendix A actually exist in the Lean repo at `~/git/lean/LeanProofs/`. Catches "renamed a theorem in Lean, the papers repo now lies" drift.

```bash
python3 tools/formalization_crosswalk.py
```

Scope is narrow on purpose: scanning paper bodies broadly produces too many false positives from JSON schema field names in backticks. Only the canonical crosswalk file and P18's Appendix A are scanned.

## `check_all.sh`

Runs all six validators in sequence and prints a unified summary with per-check ok/FAIL status. Exit code is 1 if any check fails, 0 if all pass.

```bash
tools/check_all.sh
```

Intended as the standard pre-push sanity check.
