# Receipt the Compiler: Propaganda as Hidden Epistemic Policy and the Architecture of Legible Memory

**Author:** James Beck
**Published:** March 2, 2026
**DOI:** 10.5281/zenodo.18841815
**Zenodo Record:** https://zenodo.org/records/18841815

## Abstract

Propaganda is conventionally understood as the injection of false content into public discourse. This framing is insufficiently precise. The primary attack surface of effective propaganda is not the data layer but the policy layer: the rules governing how evidence is integrated into public memory. We formalize this using a receipted semantic factor graph in which event nodes, receipt nodes, frame nodes, policy nodes, and decision nodes are explicitly typed and separately maintained. Retrospective reinterpretation — semantic retrocausality — is shown to be a normal and necessary feature of any belief-revision system operating over time. We define an epistemic governor as a set of typed constraints requiring that all updates to the semantic graph produce auditable receipts. The counter-propaganda move is not better evidence; it is legible epistemic policy.

## Key Contributions

1. Formalizes public memory as a receipted semantic factor graph with explicit event, receipt, frame, policy, and decision nodes.
2. Defines semantic retrocausality as ordinary Bayesian smoothing — normal belief revision, not a pathology.
3. Identifies propaganda as adversarial post-selection over the smoothing process via asymmetric control of policy-layer update rules.
4. Introduces a pathology taxonomy — policy/frame surgery, rationale backfill, hidden policy drift, and sequence laundering — with worked Bayesian examples.
5. Treats summaries as first-class derived artifacts whose compression and omissions must themselves be receipted.

## File Guide

| File | Description |
|------|-------------|
| `receipt-the-compiler-v1.0.md` | Manuscript (markdown source) |
| `receipt-the-compiler-v1.0.pdf` | Rendered PDF (pandoc + xelatex) |
| `metadata.yaml` | Zenodo metadata |

## Build

```bash
pandoc receipt-the-compiler-v1.0.md -o receipt-the-compiler-v1.0.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Libertinus Serif" \
  -V mathfont="Libertinus Math" \
  -V monofont="Libertinus Mono" \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  --toc \
  -V colorlinks=true
```

Requires: pandoc 3.1+, xelatex, Libertinus fonts.

## Citation
```bibtex
@article{beck2026receipt-the-compiler,
  author = {Beck, James},
  title = {Receipt the Compiler: Propaganda as Hidden Epistemic Policy and the Architecture of Legible Memory},
  year = {2026}
}
```

## Related Papers

- [Scalar Reward Collapse](../03-scalar-reward-collapse/README.md) — eigenstructure evaporation as the formal basis for capture in propaganda
- [Representational Invariance](../11-representational-invariance/README.md) — commitment shear across representations; the "enforceable past" as representation-dependent commitment
- [Bounded Lattice Inference](../12-bounded-lattice-inference/README.md) — governor architecture, contradiction ledger, NLAI (language proposes, evidence commits)
- [Cybernetic Fault Domains](../15-cybernetic-fault-domains/README.md) — governor pattern generalized across nine domains; commitment boundary formalism
- [The Gain Geometry of Temporal Mismatch](../16-signed-geometry/README.md) — capture regime and correlator quality vector; propaganda as capture-mode correlator

## Keywords

propaganda, epistemic governance, factor graphs, Bayesian smoothing, belief revision, receipt architecture, policy transparency, institutional memory, classification, content moderation, information integrity
