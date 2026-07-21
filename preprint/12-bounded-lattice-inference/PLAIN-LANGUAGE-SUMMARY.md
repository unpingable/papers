# Plain-language summary

**Companion to:** *Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Language models can propose explanations and actions fluently, but fluency is a poor basis for deciding what becomes durable system state. Prompt-only memory is easy to rewrite, contradictions can disappear through paraphrase, and a model can effectively certify its own assertions. Adding persistent state without governing its write path can turn inconsistency into durable inconsistency—or create an agent with new goals and risks.

Bounded Lattice Inference separates proposal from commitment. Language may open a claim, but only an external evidence object may close it and change authoritative state. A governor checks typed evidence, keeps claims and contradictions in a ledger, applies budgets to state transitions, and can refuse a persuasive proposal. The resulting architecture lets a model reason freely without letting it certify its own assertions.

The implementation tests whether identical inputs can produce different outputs because of traceable internal state—the paper's operational meaning of “interiority”—and explores two failure regimes. Under resource starvation, repair cannot proceed; under contradiction accumulation, unresolved conflict arrives faster than it can be serviced. The key capability is therefore not merely persistent memory. It is persistent state whose meaning and write path are governed by something other than the language model.

## Claim boundary

The paper does not claim consciousness, intentional agency, value alignment, production-scale performance, or adversarial robustness. Its guarantees are conditional on claim extraction: the current extractor is probabilistic and can miss or invent claims. Evidence is typed and externally sourced, but the reference implementation simplifies authentication and cannot make a wrong or compromised source true. The experiments cover a research-scale implementation and limited control-surface sweeps; they do not establish runtime conformance for other systems.

## Read the paper

- [Manuscript source](bounded_lattice_inference.md)
- [Rendered PDF](bounded_lattice_inference.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18145346)
- [Zenodo record](https://zenodo.org/records/18145347)
