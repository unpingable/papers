# Plain-language summary

**Companion to:** *The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A security control can be correctly configured and still act too late. Logs may be complete, an alert may eventually be accurate, and an operator may make the right decision after the protected action has already become irreversible. As systems separate detection, decision, and enforcement into different services or human queues, they create race windows that ordinary inventories of vulnerabilities and permissions do not show.

The paper calls these race windows the temporal attack surface. It separates the clocks for detection, decision, and response, then compares them with the point at which an attacker's objective becomes committed. It also makes timeout behavior part of the threat model: when evidence is incomplete, does the system fail open or fail closed, and what disruption can that choice impose?

Worked examples in monitoring, CI/CD, authentication, rate limiting, and human approval turn the model into a defender audit. Map the latency distributions, commitment points, defaults, and response times; then decide whether to detect faster, delay commitment, enforce inline, narrow the duration or scope of authority, or choose a safer default under uncertainty. The paper's central capability is to reveal security failures that permission reviews and eventual observability miss: evidence that arrives after it can still matter.

## Claim boundary

This is a defender-oriented framework and audit method, not a measured study of deployed systems. Its cross-domain cases are analytical demonstrations; no production latency distributions or before-and-after mitigation results are reported. Real systems have adaptive adversaries, interacting controls, queue dependencies, and organizational constraints that the simplified model does not capture. The paper’s broad statements about asynchronous systems and human review should therefore be read as hypotheses and design warnings, not universal empirical laws. It does not supply operational attack instructions.

## Read the paper

- [Manuscript source](temporal_attack_surface.md)
- [Rendered PDF](temporal_attack_surface.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18236164)
- [Zenodo record](https://zenodo.org/records/18236165)
