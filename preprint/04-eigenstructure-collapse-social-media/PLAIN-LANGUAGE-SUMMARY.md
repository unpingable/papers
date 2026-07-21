# Plain-language summary

**Companion to:** *Eigenstructure Collapse in Social Media Platforms: An Application of Scalar Reward Dynamics Theory*

**Artifact:** version 1.0.1 · preprint

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Social platforms repeatedly rank content using engagement signals. Visibility produces new engagement, which then influences later rankings. The paper asks whether this loop structurally favors a shrinking set of high-engagement formats and why small “diversity” adjustments may fail to preserve slower or less immediately rewarding content.

The paper uses the scalar-reward model from P03 as a baseline for examining that feedback loop. Under the model's fixed reward function, content below the maximum loses relative visibility, selection concentrates on the highest-reward modes, and the unchanged operator cannot restore modes it has eliminated. The platform question is whether ranking systems operate close enough to this regime, for long enough, to produce the same concentration pressure.

That shifts the design question from “does the platform value diversity?” to “what part of the system can preserve it independently of engagement?” A small diversity bonus may simply change which content wins the same contest. Protected feed capacity, genuinely plural objectives, slower feedback, or independent curation alter the selection structure itself. The paper gives readers a way to distinguish those structural interventions from adjustments that remain subordinate to the engagement loop.

## Claim boundary

The paper's central platform-to-theorem transport is under editorial correction. The cited theorem assumes one fixed reward function, while the platform loop in this manuscript explicitly derives a new reward function from subsequent engagement. No proof presently shows that time averaging or “quasi-stationary” rewards preserve the theorem's conclusions.

The bounded current claim is therefore conditional: where a specified platform process can be represented over a stated interval by the fixed multiplicative operator, that model predicts concentration. The manuscript does not yet establish that an entire deployed platform is “exactly” that operator. Claims about typical parameters, observed content decay, competitive selection, and business-model necessity also require separate empirical evidence. The paper should be read as an architectural model and hypothesis, not a completed universal theorem about social media.

## Read the paper

- [Manuscript source](platform_scalar_collapse.md)
- [Paper PDF](platform_scalar_collapse.pdf)
- [Directory README](README.md)
- [DOI: 10.5281/zenodo.17803843](https://doi.org/10.5281/zenodo.17803843)
- [Zenodo record](https://zenodo.org/records/19672408)
