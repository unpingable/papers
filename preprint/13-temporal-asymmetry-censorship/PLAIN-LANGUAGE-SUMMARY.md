# Plain-language summary

**Companion to:** *Temporal Asymmetry in Censorship Systems* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Deep-packet inspection is often discussed as a contest over recognizable bytes: one side finds a signature and the other disguises it. The paper argues that timing and resource limits are just as important. A middlebox must gather enough evidence, classify a flow, and act before the communication passes the relevant commitment point. It cannot wait forever or spend unlimited memory and computation on every connection.

The paper models two clocks: a transport clock for when traffic arrives and an inspection clock for when a defensible classification becomes available. Circumvention can exploit the difference by delaying decisive evidence, disrupting the classifier's timing assumptions, or preserving low-cost options before escalating. Its “Universal Bypass Inequality” states the combined condition: enforcement loses within the model when decisive evidence is late, unavailable, or too costly to process and blocking cannot take effect before communication commits.

This reframes inspection as a bounded decision problem rather than an all-seeing filter. It tells defenders to measure evidence latency, processing budget, enforcement latency, defaults under uncertainty, and acceptable collateral damage. Encrypted ClientHello is important in this geometry because it can remove an observation rather than merely obscure a familiar byte pattern, forcing the censor to accept uncertainty or block more broadly.

## Claim boundary

The paper is a formal systems model, not an operational circumvention guide. It deliberately omits implementation instructions. It reports no measurements from production censorship systems, and its queueing derivation is only sketched. The inequality is necessary and sufficient only relative to the model and its assumptions, not for every real censor. Adaptive classifiers, cascaded middleboxes, and political behavior are simplified. The institutional, language-model, and distributed-consensus comparisons are structural analogies, not empirical validations of equivalence.

## Read the paper

- [Manuscript source](dpi_bypass_control_theory.md)
- [Rendered PDF](dpi_bypass_control_theory.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18235696)
- [Zenodo record](https://zenodo.org/records/18235697)
