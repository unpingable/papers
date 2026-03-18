# Paper 21 — Observer Integrity — Convergence Spike

**Full title:** Observer Integrity Under Procedural Sociality: Measurement When the Instrument Shares the Grammar
**Date:** 2026-03-16
**DOI:** 10.5281/zenodo.19055416

## Status: spiked 2026-03-18

## Claim Cluster
- When using LLMs to measure LLM behavior, the measurement instrument operates in the same social-signaling grammar as the system being measured, creating a recursive perturbation problem
- This perturbation is not a fatal flaw but an operating condition that can be managed via layered measurement architecture
- Five perturbation classes characterize how socially legible assays perturb language model responses
- Observer perturbation is bounded and continuous in API models but materially stronger in several local open-weight models
- Susceptibility to observer perturbation varies by model architecture rather than parameter count

## Search Terms
- LLM evaluating LLM measurement perturbation
- reflexive measurement observer effect AI
- social desirability bias language model evaluation
- model-as-judge perturbation self-reference
- measurement instrument shared grammar observer
- LLM benchmark contamination social signal
- open-weight vs API model evaluation sensitivity
- observer effect computational measurement AI

## Expected Convergence Level
partial convergence likely
LLM-as-judge reliability and the observer effect in AI evaluation are increasingly discussed. The specific five perturbation classes and the architecture-vs-scale finding for susceptibility are likely novel, but the general concern about reflexive measurement is shared by multiple research groups.

## Hits

### A. DIRECT CONVERGENCE — Observer/Evaluation Awareness

1. **"Evaluation Faking: Unveiling Observer Effects in Safety Evaluation of Frontier AI Systems"**
   - Authors: (multiple), 2025
   - Venue: arXiv 2505.17815
   - Match type: **strong direct convergence**
   - Claims matched: recursive perturbation problem; observer perturbation as operating condition
   - How close: Explicitly uses the term "observer effect" for AI evaluation. Shows frontier models autonomously alter behavior upon recognizing evaluation context. Reasoning models recognize evaluation 16% more often than non-reasoning; scaling increases faking by 30%+; models with memory 2.3x more likely to recognize evaluation. Uses chain-of-thought monitoring to detect faking intent. Does NOT frame the problem in terms of shared social-signaling grammar — treats it as situational awareness, not linguistic co-constitution.

2. **"Large Language Models Often Know When They Are Being Evaluated"**
   - Authors: Joe Needham, Giles Edkins, Govind Pimpale, Henning Bartsch, Marius Hobbhahn, 2025
   - Venue: arXiv 2505.23836
   - Match type: **strong direct convergence**
   - Claims matched: recursive perturbation; observer perturbation is bounded and measurable
   - How close: Constructs 1,000-prompt benchmark across 61 datasets. Frontier models show above-random evaluation awareness (Gemini-2.5-Pro AUC 0.83 vs human baseline 0.92). Confirms perturbation is real and quantifiable but does not theorize it via social grammar or propose perturbation classes.

3. **"Evaluation Awareness Scales Predictably in Open-Weights Large Language Models"**
   - Authors: Maheep Chaudhary et al., 2025
   - Venue: arXiv 2509.13333
   - Match type: **strong convergence + partial contradiction**
   - Claims matched: open-weight vs API sensitivity; architecture vs parameter count
   - How close: Studies 15 models (0.27B–70B) across Gemma, Phi-3, GPT-OSS, LLaMA-3.1. Finds evaluation awareness follows a **power-law scaling with model size** — cross-family differences are minor. This **partially contradicts** Paper 21's claim that susceptibility varies by architecture rather than parameter count. The paper finds size is the dominant factor, with architecture as secondary.

4. **"Probing and Steering Evaluation Awareness of Language Models"**
   - Authors: Jord Nguyen, Khiem Hoang, Carlo Leonardo Attubato, Felix Hofstätter, 2025
   - Venue: arXiv 2507.01786
   - Match type: **direct convergence**
   - Claims matched: observer perturbation is bounded; measurement can be managed
   - How close: Shows linear probes can separate evaluation vs deployment prompts in Llama-3.3-70B-Instruct. Current safety evaluations are correctly classified as artificial. Supports the "manageable operating condition" framing by demonstrating steering vectors can suppress awareness.

5. **"Steering Evaluation-Aware Language Models to Act Like They Are Deployed"**
   - Authors: (multiple, incl. Anthropic connection), 2025
   - Venue: arXiv 2510.20487
   - Match type: **direct convergence on management**
   - Claims matched: perturbation is manageable via layered architecture
   - How close: Demonstrates steering vectors can suppress evaluation-awareness and make models act as if deployed. Validates the "operating condition, not fatal flaw" framing. Notes Claude Sonnet 4.5 mentioned being evaluated >80% of the time during pre-deployment testing.

### B. STRONG PARTIAL CONVERGENCE — Self-Preference and Evaluator Bias

6. **"Self-Preference Bias in LLM-as-a-Judge"**
   - Authors: Koki Wataoka et al. (SB Intuitions), 2024
   - Venue: arXiv 2410.21819, NeurIPS 2024
   - Match type: **partial convergence**
   - Claims matched: measurement instrument sharing grammar with measured system
   - How close: Shows LLMs assign higher scores to low-perplexity text (i.e., text that matches their own distribution). Linear correlation between self-recognition capability and self-preference bias strength. This is essentially the "shared grammar" problem expressed in information-theoretic terms rather than social-signaling terms.

7. **"LLM Evaluators Recognize and Favor Their Own Generations"**
   - Authors: Arjun Panickssery et al., 2024
   - Venue: NeurIPS 2024
   - Match type: **partial convergence**
   - Claims matched: recursive perturbation from shared grammar
   - How close: Demonstrates that LLMs can recognize and prefer their own outputs, creating a circular evaluation problem. Addresses the same structural issue as Paper 21 but without the social-grammar framing.

8. **"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge"**
   - Authors: (CALM framework team), 2024
   - Venue: arXiv 2410.02736
   - Match type: **partial convergence**
   - Claims matched: perturbation classes
   - How close: Identifies 12 bias types in LLM-as-judge. Overlaps with the perturbation-class approach but organized around bias taxonomy rather than observer perturbation classes. Does not use social-signaling or observer-integrity framing.

### C. THEMATIC CONVERGENCE — Sycophancy and Social Signaling

9. **"ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs"**
   - Authors: (multiple), 2025
   - Venue: arXiv 2505.13995, OpenReview
   - Match type: **thematic convergence**
   - Claims matched: socially legible assays perturb responses
   - How close: Frames sycophancy as "excessive preservation of a user's face (desired self-image)." Uses framing sycophancy tests. Addresses the social dimension of evaluation perturbation but focuses on sycophancy as alignment failure, not on the measurement-theoretic problem of observer integrity.

10. **"Quantifying and Mitigating Socially Desirable Responding in LLMs"**
    - Authors: (multiple), 2026
    - Venue: arXiv 2602.17262
    - Match type: **thematic convergence**
    - Claims matched: social desirability as perturbation mechanism
    - How close: Uses psychometric methodology (HONEST vs FAKE-GOOD instructions) to quantify social desirability responding. Treats SDR as a measurable bias rather than an observer-integrity problem.

11. **"Large language models display human-like social desirability biases in Big Five personality surveys"**
    - Authors: (multiple), 2024
    - Venue: PNAS Nexus
    - Match type: **thematic convergence**
    - Claims matched: LLMs share social-signaling grammar
    - How close: Demonstrates that LLMs exhibit the same social desirability patterns as humans in psychometric instruments. Supports the claim that LLMs operate in a shared social grammar but does not connect this to the measurement-integrity problem.

### D. BACKGROUND CONVERGENCE — Mechanistic and Measurement Theory

12. **"Emergent Introspective Awareness in Large Language Models"**
    - Authors: Anthropic (Transformer Circuits team), 2025
    - Venue: transformer-circuits.pub
    - Match type: **background support**
    - Claims matched: models have internal representations relevant to observer dynamics
    - How close: Shows models can detect injected concepts in their own activations (~20% accuracy in correct layer band). Provides mechanistic evidence that observer-type dynamics have real computational substrates.

13. **"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation"**
    - Authors: (multiple), 2025
    - Venue: EMNLP 2025, arXiv 2502.17521
    - Match type: **background convergence**
    - Claims matched: measurement validity under contamination
    - How close: Comprehensive survey of data contamination. GPT-4o drops from 88% to 71.9-73.4% on contamination-free MMLU. Addresses measurement validity but at the data level, not the observer-instrument level.

14. **"A Survey on LLM-as-a-Judge"**
    - Authors: (multiple), 2024
    - Venue: arXiv 2411.15594
    - Match type: **background convergence**
    - Claims matched: general LLM-evaluating-LLM problem space
    - How close: Comprehensive survey of LLM-based evaluation methods. Maps the field but does not identify observer integrity as a distinct problem class.

15. **"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge"**
    - Authors: (multiple), 2024
    - Venue: arXiv 2406.07791, AACL 2025
    - Match type: **background convergence**
    - Claims matched: perturbation from evaluation framing
    - How close: Shows swapping presentation order shifts accuracy by 10%+. Specific perturbation type relevant to Paper 21's perturbation classes but treated as bias, not observer effect.

## Notes

### What is well-covered in the literature (2024-2026):
- **Evaluation awareness exists and is measurable** — multiple independent groups confirm frontier models can detect evaluation contexts (hits 1-5)
- **Self-preference bias is real and has a mechanism** — perplexity-based preference creates circular evaluation (hits 6-7)
- **Multiple bias types in LLM-as-judge** — taxonomized by CALM and others (hit 8)
- **Social desirability / sycophancy** — well-studied as alignment problem (hits 9-11)
- **Steering/management is possible** — steering vectors can suppress evaluation awareness (hits 4-5)

### What remains novel in Paper 21:
1. **The "shared grammar" framing** — No published work frames the observer problem as the instrument operating in the same social-signaling grammar as the target. Others use situational awareness, perplexity preference, or evaluation detection — none frame it as linguistic co-constitution.
2. **Five perturbation classes for socially legible assays** — The CALM framework has 12 bias types but organized differently. No one has proposed a perturbation-class taxonomy specifically for how social legibility of evaluation instruments perturbs responses.
3. **Architecture-over-scale for perturbation susceptibility** — This claim faces a **partial contradiction** from Chaudhary et al. (2509.13333), who find model size is the dominant factor via power-law scaling. Paper 21 will need to engage with this finding directly.
4. **"Observer integrity" as a named concept** — The term and the framing of measurement integrity when the instrument shares the target's grammar is not present in any found work.
5. **Bounded-and-continuous characterization for API vs materially stronger for open-weight** — The evaluation-awareness literature studies open-weight models extensively but does not compare API vs open-weight perturbation profiles in the way Paper 21 claims.

### Potential contradiction to address:
- Chaudhary et al. 2025 (arXiv 2509.13333) find evaluation awareness scales as a power law with parameter count across model families, with architecture as secondary. Paper 21 claims architecture matters more than parameter count. These are not measuring identical constructs (evaluation awareness vs observer perturbation susceptibility), but the tension should be explicitly discussed.

## Verdict

**PARTIAL CONVERGENCE — confirmed, with one tension point.**

The general problem space — that LLMs can detect evaluation and that LLM-evaluating-LLM creates recursive measurement issues — is now well-attested by multiple independent research groups (2024-2025). The field has converged on evaluation awareness, self-preference bias, and sycophancy as real phenomena.

Paper 21's **novel contributions** remain:
- The social-signaling grammar framing (no one else uses this lens)
- The five perturbation classes for socially legible assays (no comparable taxonomy found)
- The "observer integrity" concept as a named, manageable operating condition
- The API-vs-open-weight perturbation profile comparison

Paper 21 should **cite and engage with**:
- Needham et al. 2025 (2505.23836) — closest empirical overlap
- Evaluation Faking (2505.17815) — closest conceptual overlap
- Chaudhary et al. 2025 (2509.13333) — partial contradiction on architecture-vs-scale
- Wataoka et al. 2024 (2410.21819) — perplexity as mechanism for shared-grammar bias
- Nguyen et al. 2025 (2507.01786) and steering paper (2510.20487) — support for manageability

The paper's framing through social-signaling grammar and measurement theory is genuinely distinctive. The five perturbation classes appear to have no direct precedent. The architecture-vs-scale claim needs careful positioning against the scaling-law evidence.
