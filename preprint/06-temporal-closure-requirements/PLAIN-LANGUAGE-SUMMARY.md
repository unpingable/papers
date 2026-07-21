# Plain-language summary

**Companion to:** *Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap*

**Version/status:** current repository source with the necessity-side correction; the published DOI record v1.0 retains the broader abstract.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A system can produce a convincing description of continuity without itself continuing as an autonomous process. A language model can reason over a supplied history, for example, while the history and the timing of each invocation are maintained elsewhere. The paper asks what architecture is required for identity to persist through time and perturbation, rather than merely be reconstructed on demand.

The paper identifies three roles that such an architecture needs: separated timescales, internal state that evolves under the system's own dynamics, and regulation that responds when coherence approaches a boundary. Its central distinction—the “simulator gap”—separates a component that maps supplied inputs to outputs from a system that owns an ongoing trajectory. Giving a model a longer context preserves more input, but it does not by itself create state evolution between invocations.

This is also a systems-boundary argument, not a claim that transformers can never participate in coherent systems. Durable state and regulation may live in other components. The practical contribution is a set of questions for locating continuity in the actual architecture: which component owns the transition law, what changes when no new prompt arrives, and what mechanism detects and corrects drift? It prevents memory, stored history, and endogenous state from being treated as interchangeable.

## Claim boundary

The current bounded claim is necessity-side. An earlier type-boundary specimen distinguished finite external context from endogenous trajectory, but its cited scratch path is not a current stable Lean identifier. A separate Baby River environment kernel establishes bounded environment semantics rather than learning convergence or empirical superiority. Neither artifact proves that the three proposed roles are jointly sufficient for identity-preserving coherence under perturbation. Temporal separation and adaptive control remain less formally developed, and the institutional analogies are first-order constraints rather than a complete organizational theory. The published metadata abstract still contains retired “necessary and sufficient” wording; the README and current repository manuscript state the narrower position.

## Read the paper

- [Manuscript source](Paper6_Temporal_Closure_v1.0.md)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.17849277](https://doi.org/10.5281/zenodo.17849277)
- [Zenodo record](https://zenodo.org/records/17849278)
