# Plain-language summary

**Companion to:** *Unauthorized Durability: A Composable Governance Primitive for State Promotion in Adaptive Systems* — version 1.1, published preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Temporary input often becomes lasting control without a visible decision. A prompt becomes saved memory; repeated context becomes a default preference; an operational shortcut becomes policy; policy-maintenance rules quietly become constitutional doctrine. The issue is not that systems learn or that influence occurs. It is that low-authority signals can acquire durable governing force without an authorized write path.

The paper separates four tiers of authority: runtime action, bounded context, durable policy, and constitutional constraint. Lower tiers are not allowed to write higher ones merely through repetition or operational success. A legitimate promotion follows a five-phase path: propose a typed change, evaluate it against the governing rules, attest its permitted scope and persistence, apply it, and retain the complete chain for audit. The same pattern governs changes to the promotion rules themselves.

This turns “the system learned it” into a reviewable state transition. For any durable change, an operator can ask what requested it, who had standing to approve it, what was granted, what was actually applied, and how the path can be replayed or rolled back. The version 1.1 appendix separately models what happens after the barrier has failed: individually recoverable commits can consume rollback capacity and accumulate into a lock-in that internal action alone cannot undo.

## Claim boundary

The design is strongest for engineered systems with enforceable write gates. Its use for institutions or human cognition is an analytical analogy, not an isomorphism. The framework does not decide truth, legitimate policy, or who should hold authority. The Lean appendix formalizes only post-breach persistence dynamics; it does not formalize the promotion ceremony, observer integrity, tier-escalation paths, evidence honesty, or empirical calibration. It therefore sharpens a limited mechanism rather than proving the whole governance architecture.

## Read the paper

- [v1.1 manuscript source](unauthorized_durability.md)
- [Rendered PDF](unauthorized_durability.pdf)
- [Paper README](README.md)
- [Concept DOI: 10.5281/zenodo.18940007](https://doi.org/10.5281/zenodo.18940007)
- [Version DOI: 10.5281/zenodo.19671896](https://doi.org/10.5281/zenodo.19671896)
- [Zenodo record](https://zenodo.org/records/19671896)
