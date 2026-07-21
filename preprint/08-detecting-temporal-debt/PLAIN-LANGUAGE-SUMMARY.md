# Plain-language summary

**Companion to:** *Detecting Temporal Debt in Language Models and Software Systems: Applications of Δt-Constrained Inference*

**Artifact:** version 1.0 · preprint

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Language models can sound certain when their answers are unstable, and software dashboards can remain green while delivery evidence becomes erratic. The paper asks whether both situations can be screened by comparing expressed confidence with a proxy for evidential support.

The paper turns the mismatch proposed in P07 into two prototype detectors. For language-model responses, it uses repeated-output consistency and, where available, an estimate of how well represented the query is in training data. For software delivery, it combines velocity stability with time remaining. Each prototype compares claimed confidence with measured support and assigns a risk band that can trigger verification, retrieval, replanning, or closer review.

Its contribution is an instrumentation pattern rather than an automated judge. Fluent output and green dashboards are presentation surfaces; neither shows whether the underlying evidence is keeping pace with the commitment being made. By exposing that gap, the detector gives an operator a reason to investigate and preserves a basis for review. The paper is useful to readers designing observability around epistemic or planning risk, even when the proxies cannot decide truth or safety.

## Claim boundary

The manuscript's labels and deployment claims are under substantive correction. The prototype result currently called `Justified (Safe)` is only low measured mismatch under heuristic proxies; it is not a safety verdict. Its thresholds are unvalidated, training-data density is usually unavailable, and the presented observations are neither longitudinal nor a live deployment. The response-level calculation is also `confidence - support`, not the cumulative `D(t)` defined in P07.

Accordingly, this detector should not silently acquire authority to gate, refuse, retrain, or declare a claim correct. Any operational use needs a separately justified threshold, provenance, a stored decision, an identified decision-maker with standing, and a refusal path when basis or authority is missing. The implementation is an experimental risk signal, not a faithful judge.

## Read the paper

- [Manuscript source](delta_t_applications_paper_with_figure.md)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.17859323](https://doi.org/10.5281/zenodo.17859323)
- [Zenodo record](https://zenodo.org/records/17859324)
