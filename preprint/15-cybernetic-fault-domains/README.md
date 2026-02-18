# Cybernetic Fault Domains: When Commitment Outruns Verification

**Author:** James Beck
**Published:** February 2026
**DOI:** 10.5281/zenodo.18686130
**Zenodo Record:** https://zenodo.org/records/1818686130

## Abstract

We hypothesize that when irreversible commitments cross a boundary faster than verification can complete, unverified state transitions accumulate and systems exhibit recurring loss-of-control signatures. We formalize this condition as **cybernetic fault domains** — boundary-relative temporal regimes defined by a commitment boundary (C_k), commitment-verification lag (Δt), and boundary load (σ) — and provide a measurement protocol with nine domain instantiations spanning organizations, language models, censorship systems, security operations, safety tuning, platforms, representational transforms, optimization dynamics, and synthetic coherence. An architectural containment pattern — **governors** that separate proposal from commitment and gate crossings of C_k on evidence — is implemented and mechanically tested in one domain via an enforcement kernel with 37 verifiable claims and a dimensionless risk index (R_t = PD/E) that formalizes the gate as a single inequality. Four falsifiable claims, seven testable predictions, and the strongest adversarial target are specified: a system that sustains high Δt and σ without degradation would kill the framework.

## Key Contributions

1. A boundary-relative definition of cybernetic fault domains in terms of Δt, C_k, H, and σ, with a minimal measurement protocol.
2. Nine domain instantiations mapping these parameters onto heterogeneous systems, each with concrete parameterization, σ operationalization, failure signature, and worked example.
3. An architectural containment pattern — governors — with an existence proof via an enforcement kernel (agent_gov) backed by 37 mechanically verifiable claims, a dimensionless risk index (Appendix C), and a threat model.
4. Four falsifiable claims, seven testable predictions, and the strongest adversarial target that would falsify the core claim.

## File Guide

| File | Description |
|------|-------------|
| `cybernetic-fault-domains-v1.0.md` | Current manuscript (markdown source) |
| `cybernetic-fault-domains-v1.0.pdf` | Rendered PDF (72 pages, pandoc + xelatex) |
| `governor-pattern.png` | Governor pattern diagram (rendered from Mermaid) |
| `governor-pattern.mmd` | Mermaid source for governor diagram |
| `metadata.yaml` | Zenodo metadata |
| `v0.2-draft-instantiations.md` | Draft: domain instantiations |
| `v0.3-draft-governor.md` | Draft: governor pattern + agent_gov |
| `v0.4-draft-risk-index.md` | Draft: dimensionless risk index (Appendix C) |
| `v0.5-draft-falsifiability.md` | Draft: falsifiability + discussion |
| `cybernetic-fault-domains-v0.1.md` | Initial v0.1 draft (superseded) |
| `cybernetic_fault_domains-project.md` | Project planning notes |
| `PROJECT_PLAN.md` | Project plan |
| `puppeteer-config.json` | Build artifact (mermaid-cli config) |

## Build

```bash
pandoc cybernetic-fault-domains-v1.0.md -o cybernetic-fault-domains-v1.0.pdf \
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
@article{beck2026cybernetic-fault-domains,
  author = {Beck, James},
  title = {Cybernetic Fault Domains: When Commitment Outruns Verification},
  year = {2026}
}
```

## Related Papers

- [The Coherence Criterion: A Unified Framework for Stability in Hierarchical Systems](../01-coherence-criterion/README.md)
- [The Second Law of Organizations: How Temporal Lag Drives Irreversible Institutional Decay](../02-second-law-organizations/README.md)
- [Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems](../03-scalar-reward-collapse/README.md)
- [Eigenstructure Collapse in Social Media Platforms: An Application of Scalar Reward Dynamics Theory](../04-eigenstructure-collapse-social-media/README.md)
- [Control Laws for Hierarchical Kinetics: Design Principles and Intervention Strategies for Multi-Timescale Systems](../05-control-laws-hierarchical-kinetics/README.md)
- [Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap](../06-temporal-closure-requirements/README.md)
- [Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems](../07-delta-t-constrained-inference/README.md)
- [Detecting Temporal Debt in Language Models and Software Systems: Applications of Δt-Constrained Inference](../08-detecting-temporal-debt/README.md)
- [Capacity-Constrained Stability: A Control-Theoretic Framework for Institutional Resilience](../09-capacity-constrained-stability/README.md)
- [You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems](../10-invariant-requirements-temporal-coherence/README.md)
- [Representational Invariance and the Observer Problem in Language Model Alignment](../11-representational-invariance/README.md)
- [Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority](../12-bounded-lattice-inference/README.md)
- [Temporal Asymmetry in Censorship Systems](../13-temporal-asymmetry-censorship/README.md)
- [The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems](../14-temporal-attack-surface/README.md)

## Keywords

- cybernetics
- fault containment
- temporal dynamics
- irreversibility
- commitment boundary
- control theory
- dependable computing
- systems engineering
- socio-technical systems
- governance
- computer security
- language models
- AI safety
