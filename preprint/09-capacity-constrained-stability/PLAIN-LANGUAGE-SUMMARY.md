# Plain-language summary

**Companion to:** *Capacity-Constrained Stability: A Control-Theoretic Framework for Institutional Resilience*

**Artifact:** version 1.0 · preprint

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Hospitals, financial institutions, and infrastructure systems can appear stable until a shock produces sudden failure. Capacity may exist on paper yet be unavailable quickly enough, while emergency reserves are finite and routine work keeps arriving. The paper asks for a simple boundary that makes this hidden exposure visible before buffers are exhausted.

The paper proposes a compact capacity boundary. Incoming demand must not exceed sustainable processing capacity plus the rate at which a finite reserve can cover demand during the response delay: `Δ ≤ C + B/τ`. This separates operation with real margin from a metastable regime that stays functional only by spending down reserves, and from an unstable regime in which unresolved work necessarily accumulates.

The practical value is in what the inequality forces an audit to measure. Published capacity may be ideal rather than sustainable, reserves may be nominal rather than deployable, and “response time” may omit detection or implementation delay. A system can therefore look adequately resourced while its usable buffer is already on a countdown. The paper gives institutions a simple way to expose that hidden dependence before a shock makes it obvious.

## Claim boundary

The inequality is presented as a necessary capacity condition, not a sufficient theory of institutional success. A system below the boundary may still fail through coordination, allocation, interference, or other mechanisms. The case studies show retrospective consistency, not causal necessity or prospective validation; parameter estimation, changing capacity under load, endogenous shocks, dimension choice, ethics, and political feasibility remain open.

The README's current Lean claim is also overstated. The cited two-budget branch-selection specimen is adjacent to this paper's susceptibility story, but it does not prove `Δ ≤ C + B/τ`, the empirical cases, or a universal classification of institutional failure.

## Read the paper

- [Manuscript source](capacity_constrained_stability_complete_paper.md)
- [Paper PDF](capacity_constrained_stability_complete_paper.pdf)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.18019050](https://doi.org/10.5281/zenodo.18019050)
- [Zenodo record](https://zenodo.org/records/18019051)
