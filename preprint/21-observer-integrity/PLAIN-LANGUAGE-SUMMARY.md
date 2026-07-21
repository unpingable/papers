# Plain-language summary

**Companion to:** *Observer Integrity Under Procedural Sociality: Measurement When the Instrument Shares the Grammar* (Δt Paper 21)

**Version/status:** v1.0.1, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Evaluating a conversational model requires communicating with it. But an evaluation prompt is itself a social signal: it tells the model what is being measured, what stance seems desirable, and how an evaluator expects it to behave. A test for frame sensitivity can therefore change the very behavior it is trying to observe.

This is not ordinary independent noise. The disturbance is produced by the same social interpretation mechanism under examination.

The paper treats this disturbance as part of the measurement rather than evidence that measurement is impossible. It identifies recognizable contamination patterns—adopting the assay's vocabulary, artificial caution or neutrality, holding one stance across every condition, and discussing the test instead of doing the task. Its layered architecture runs the primary assay, uses a meta-assay to characterize what the first assay induced, estimates the difference, and retains a bound for what remains unresolved.

This changes what “observer integrity” means. The goal is not a magically unperturbed observation, but evidence that the perturbation is stable, bounded, and small enough for a particular observer–assay pair. A pilot across three API models and five local models found materially different susceptibility, making cross-model comparison part of the measurement itself rather than a decorative replication check.

## Claim boundary

The pilot used a narrow technical task battery, mostly single trials, and a scorer that was itself among the tested models. The proposed subtraction procedure is not generally validated, and large or regime-switching perturbations may make correction impossible. Results from the tested models do not establish a universal relationship with model size, architecture, or visible reasoning traces. The broader application beyond language models remains analogical.

## Read the paper

- [Manuscript source](observer_integrity_under_procedural_sociality.md)
- [PDF](observer_integrity_under_procedural_sociality.pdf)
- [Directory guide](README.md)
- [DOI](https://doi.org/10.5281/zenodo.19055415)
- [Zenodo record](https://zenodo.org/records/19672438)
