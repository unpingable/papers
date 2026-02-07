# You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems

**Author:** James Beck  
**Published:** December 23, 2025  
**DOI:** 10.5281/zenodo.18039926  
**Zenodo Record:** https://zenodo.org/records/18039927

## Abstract

Current transformer-based AI systems exhibit systematic failures of temporal coherence—the ability to maintain stable meanings, beliefs, and references across inference steps. We argue these failures are best explained by structural constraints of architectures that lack invariant-preserving primitives. Drawing on the Δt framework for temporal dynamics in hierarchical systems, we identify four essential invariants that any coherent inference system must preserve: (1) Temporal Coherence - past claims constrain present outputs, (2) Semantic Conservation - meaning remains stable under transformation, (3) Epistemic Grounding - sources actually constrain claims, and (4) Irreversibility - errors leave learning residue.

We present empirical tests demonstrating that major production language models violate these invariants despite vastly different implementations. Critically, we show these violations are consistent with architectural limitations: they persist across all tested transformer-based systems because transformers lack the necessary primitives (persistent endogenous state, endogenous state evolution operators, temporal coupling controls).

This work establishes invariant requirements as diagnostic infrastructure for evaluating whether systems can maintain coherence, and demonstrates why current approaches cannot satisfy these requirements without fundamental architectural changes.


## Key Contributions

- We present empirical tests demonstrating that major production language models violate these invariants despite vastly different implementations, training approaches, and parameter scales.
- Critically, we show these violations are **consistent with architectural limitations**: they persist across all tested transformer-based systems because transformers lack the necessary primitives (persistent endogenous state, endogenous state evolution operators, temporal coupling controls).
- Current explanations treat these as: - **Semantic errors** (incorrect content requiring better training data) - **Calibration failures** (overconfidence requiring better alignment) - **Grounding deficits** (missing retrieval requiring RAG systems) We propose a different diagnosis: these are **temporal pathologies**—failures to preserve invariant relationships across time.
- Each pattern has been observed consistently across multiple prompt variations, but we present representative cases rather than aggregate statistics.

## Citation
```bibtex
@article{rock2025temporal-coherence,
  author = {Beck, James},
  title = {You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems},
  year = {2025},
  doi = {10.5281/zenodo.18039926},
  url = {https://zenodo.org/records/18039927}
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
- [Representational Invariance and the Observer Problem in Language Model Alignment](../11-representational-invariance/README.md)
- [Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority](../12-bounded-lattice-inference/README.md)
- [Temporal Asymmetry in Censorship Systems](../13-temporal-asymmetry-censorship/README.md)
- [The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems](../14-temporal-attack-surface/README.md)

## Keywords

- temporal coherence
- architectural invariants
- transformer limitations
- epistemic grounding
- semantic stability
- AI systems analysis
- Δt framework
- language models
- hallucination detection
