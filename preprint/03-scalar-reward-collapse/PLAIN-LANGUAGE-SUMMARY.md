# Plain-language summary

**Companion to:** *Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems*

**Artifact:** version 1.0.1 · preprint

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Many systems repeatedly score alternatives with one number and give more weight to whatever scores best. Recommendation systems promote engaging content, training loops favor highly rewarded outputs, and markets favor successful strategies. The paper asks what repeated selection of this kind does to alternatives that never achieve the maximum score.

The paper isolates the simplest version of that loop: a finite set of alternatives, one fixed reward for each, and repeated multiplicative reweighting toward higher reward. In this model, every alternative below the maximum loses relative weight exponentially. Eventually the distribution concentrates on the reward-maximizing set, and the same unchanged process cannot restore an alternative whose weight has reached zero. Recovery requires an outside source, a changed objective, or a different update rule.

The paper calls this loss of non-maximal modes “eigenstructure evaporation.” The useful result is sharper than the general observation that optimization creates winners: it shows that, for this operator, reducing the learning rate only slows the concentration. It does not change its direction. Anyone designing for durable diversity therefore has to protect alternatives structurally rather than assume that a carefully tuned scalar score will preserve every distinction that matters.

## Claim boundary

The theorem is exact for the stated finite-state, fixed-reward multiplicative operator. It does not automatically cover changing rewards, arbitrary reinforcement-learning algorithms, platforms, markets, or institutions; each application needs an explicit mapping and assumptions. The discussion of continuous spaces and rapidly changing rewards is prospective rather than part of the proved result. Likewise, later governance formalization does not prove this paper or imply that every scalar objective launders authority. A useful successor specimen may examine when scalar scoring erases distinct judgments, but that is new work.

## Read the paper

- [Manuscript source](scalar_reward_collapse.md)
- [Paper PDF](scalar_reward_collapse.pdf)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.17791872](https://doi.org/10.5281/zenodo.17791872)
- [Zenodo record](https://zenodo.org/records/19672401)
