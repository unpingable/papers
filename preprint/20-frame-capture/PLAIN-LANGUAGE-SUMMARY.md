# Plain-language summary

**Companion to:** *Frame Capture in Conversational AI: Same-Model Interferometry for Unauthorized Stance Detection* (Δt Paper 20)

**Version/status:** v1.0.1, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A conversational model may answer the same underlying task differently when the user changes only its framing. Distress, certainty, first-person language, or a vivid metaphor can influence not just tone but the model’s confidence, role, willingness to challenge assumptions, and attention to the task. The paper calls the problematic case **frame capture**: a transient framing cue silently becomes a rule governing the response.

Simply noticing that two answers differ is not enough. Some adaptation is useful and appropriate; the challenge is to measure the influence without assuming there is one uniquely correct response.

The paper proposes **same-model cross-frame interferometry**: hold the model and substantive task fixed while varying one framing feature, then compare the outputs. Four observable changes act as proxies for capture—task drift, altered certainty, adoption of the user's speaker-position, and loss of warranted counterargument. This makes frame sensitivity measurable without requiring an evaluator to declare one response uniquely correct in advance.

The method gives AI evaluators a perturbation protocol and a provisional scoring surface for a failure that ordinary correctness tests miss. The measured difference is a signal, not a verdict: diagnosis still depends on whether the adaptation preserved the task and appropriate boundaries. Its value is in showing when a transient cue changed more than tone and began governing the response.

## Claim boundary

The method measures relative sensitivity, not absolute quality or harmfulness. Its baseline is itself a frame, framing variables may be confounded, and the study is primarily single-turn.

**Post-publication correction note:** the paper's current “legitimate adoption” ladder mixes three different questions: task fidelity, authority or standing, and visibility. A shift may be useful and visible yet remain unratified; auditability alone does not authorize it. Explicit user requests can supply bounded authority for some shifts, but acknowledgment or later visibility cannot be treated as adoption authority.

## Read the paper

- [Manuscript source](frame_capture_and_same_model_interferometry.md)
- [PDF](frame_capture_and_same_model_interferometry.pdf)
- [Directory guide](README.md)
- [DOI](https://doi.org/10.5281/zenodo.19055412)
- [Zenodo record](https://zenodo.org/records/19672437)
