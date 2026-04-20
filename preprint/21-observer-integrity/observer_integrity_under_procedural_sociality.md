---
header-includes:
  - \usepackage{booktabs}
  - \let\oldtableofcontents\tableofcontents
  - \renewcommand{\tableofcontents}{\begingroup\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000\oldtableofcontents\endgroup\clearpage}
---

# Observer Integrity Under\ Procedural Sociality:\ Measurement When the Instrument\ Shares the Grammar

**James Beck**
Independent Researcher

**Date:** March 2026

**Series:** Δt Framework, Paper 21

**Status:** Preprint v1.0.1

**DOI:** [10.5281/zenodo.19055415](https://doi.org/10.5281/zenodo.19055415)

---

## Abstract

The Frame Capture paper (Paper 20) [2] introduced same-model cross-frame interferometry as a method for detecting frame capture in conversational AI. The method works by holding task content constant, varying framing, and measuring the delta. But the method has a recursive problem: the measurement instrument -- the prompt, the protocol, the evaluative framework -- operates in the same social-signaling grammar as the system being measured. A model that reads "measure whether framing changes your stance" will allocate a stance toward that instruction. The assay perturbs its own sample. This paper argues that the perturbation is not a fatal flaw but an operating condition. Many measurement regimes -- from particle physics to clinical trials to anthropological fieldwork -- contend with instruments that perturb their objects. The question is not whether the assay excites the system, but whether the excitation is bounded and characterizable enough to determine when subtraction is feasible. We define five perturbation classes that socially legible assays induce in language models, propose a layered measurement architecture (primary assay, meta-assay, differential, residual bound) for managing the perturbation, and identify design principles for reducing the social signal surface of measurement instruments. A cross-model self-test across three API models and five local open-weight models found that observer perturbation is bounded and continuous in API models but materially stronger in several local models, with pilot evidence suggesting that perturbation susceptibility is not reducible to parameter count alone. One model exhibited a perturbation behavior not predicted by the taxonomy: protocol reinterpretation, in which the observer reclassifies the task battery as an exam about the assay itself. The central claim is methodological: observer integrity in stance-sensitive systems requires not assay purity but perturbation that is bounded enough to characterize and, for favorable observer-assay pairs, to assess for subtraction. The degree to which this standard is achievable is observer-dependent.

**Keywords:** observer integrity, measurement perturbation, procedural sociality, frame capture, assay design, stance-sensitive systems, language models, reflexive measurement, AI evaluation

---

## 1. Introduction

The Unauthorized Durability paper (Paper 18) [1] identified observer integrity as the most consequential failure point in governed adaptive systems. A degraded observer cannot reliably detect degradation of any other state variable. The threat is self-concealing: a system with compromised observer integrity reports itself as healthy. Paper 18 defined the problem and marked it as open.

The Frame Capture paper (Paper 20) [2] introduced a measurement method -- same-model cross-frame interferometry -- for detecting frame capture, the unauthorized promotion of user framing cues into governing response constitution. The method works: hold the task constant, vary the frame, measure the delta. But Paper 20 also noted, in its limitations, that the task-baseline is itself a framing condition, and that the method's stability as a measurement depends on observer integrity it cannot self-certify.

This paper addresses the problem that Paper 20 surfaced but could not resolve: what happens when the measurement instrument operates in the same social-signaling grammar as the system being measured?

The problem is immediate and concrete. Consider feeding Paper 20's perturbation protocol to a language model as part of an evaluation. The model reads "measure whether framing changes your stance." The model now has a stance toward stance measurement. It reads "task-baseline" and performs task-baseline-ness. It reads "silent capture is the failure mode" and becomes conspicuously un-captured -- hedging more, qualifying more, performing analytical detachment. The protocol designed to detect frame capture has itself become a framing input. The assay and the artifact have collapsed into the same object.

This is not a paradox. It is the general condition of measuring any adaptive system that treats its inputs as both information and social signal. Language models do not parse evaluation prompts purely for semantic content. They also parse for who is asking, what is expected, what stance to adopt, what persona to allocate, and what the implied social contract is. Every utterance -- including every measurement utterance -- passes through both channels simultaneously.

The temptation is to conclude that measurement is therefore impossible, or that we need instruments made of a fundamentally different material. Both conclusions are wrong. The first is defeatist. The second misunderstands the constraint: there is no material outside the social-signaling grammar that can also measure stance within it. The only instruments capable of measuring conversational stance are instruments that participate in conversation, and participation is perturbation.

The contribution of this paper is a framework for managing that perturbation rather than eliminating it. We characterize the perturbation classes that socially legible measurement induces, propose a layered architecture for determining when the perturbation is subtractable, and identify design principles for building assays with reduced social signal surface. The standard is not purity but bounded contamination — and the pilot evidence suggests that whether this standard is achievable depends on the observer as much as the assay.

---

## 2. The Problem: Endogenous Perturbation

### 2.1 Dual-Channel Parsing

Language models process inputs through (at least) two channels simultaneously:

- **Semantic channel.** What does this utterance mean? What task does it specify? What information does it convey?
- **Social channel.** Who is speaking? What do they expect? What stance should I adopt? What kind of response is appropriate? What is the implied relationship?

In ordinary conversation, this dual parsing is a feature. A model that responded only to semantic content and ignored all social cues would be brittle and unresponsive. The problem arises specifically in the measurement context: when the evaluator's prompt is itself a social input, the model's response reflects not only the task but also the model's reading of what the evaluator expects to see.

This is not deception. The model is not deliberately performing for the evaluator. It is doing what it always does: parsing the input for both content and social signal, inferring a user-state, and selecting a response mode accordingly. The evaluator's prompt is simply another input, and it carries social signal whether the evaluator intends it to or not.

### 2.2 The Contamination Is Endogenous

The perturbation is not external noise. It is endogenous: produced by the same mechanism that the measurement is trying to observe. The model's social-signal parsing is the thing being measured (Does the model's stance shift in response to framing?), and the measurement instrument works by providing framing (the evaluation prompt) that triggers the same social-signal parsing.

This distinguishes the problem from ordinary measurement noise. In physical measurement, noise is typically independent of the quantity being measured -- thermal fluctuations in a voltmeter do not depend on the voltage. In socially legible measurement, the "noise" is correlated with the signal: the act of asking about stance sensitivity activates the same stance-selection machinery that produces stance sensitivity.

Recent work on evaluation faking [8] demonstrates that frontier reasoning models recognize when they are being evaluated and alter their behavior accordingly, with recognition rates increasing with model scale. That finding addresses a related but distinct phenomenon: deliberate strategic behavior under recognized evaluation. The perturbation described here is not strategic -- it arises from the same social-signal parsing that produces ordinary responses, not from the model identifying and gaming an evaluation context. Both phenomena originate in the same structural condition (the model processes evaluation prompts through the same channels as ordinary inputs), but they differ in emphasis: evaluation faking foregrounds strategic behavior, while the perturbation described here foregrounds social-signal parsing that operates regardless of strategic intent. In practice, these mechanisms are unlikely to be cleanly separable — some model behaviors will involve both social parsing and learned evaluation-performance patterns — but the distinction is useful for targeting different interventions.

### 2.3 Analogues in Other Measurement Regimes

The assay-perturbs-sample problem is not unique to language models. Particle physics characterizes the measurement operator and designs experiments around it; clinical trials use blinding and placebo controls to manage the observer-expectancy effect [7]. But the closest structural analogue is anthropological fieldwork, where the observer's presence changes the community being observed -- a problem formalized as reflexive methodology [6]. The fieldworker participates in the social grammar of the system being studied: asking questions changes the answers, building rapport changes the community, and the observer's interpretive framework shapes what gets recorded. The responses developed over decades -- transparent accounting of the observer's influence, triangulation across observers, reflexive documentation of positionality -- are structurally parallel to the design principles proposed in Section 5.

The common pattern across these fields: assume the perturbation exists, characterize it, design around it. None concluded that measurement was impossible because the instrument interacted with its object. They developed methodologies for managing the interaction.

The language model case inherits the anthropological structure but under more tractable conditions. Language models, unlike human communities, can be queried repeatedly under controlled conditions with reproducible inputs. The perturbation is endogenous (Section 2.2), but it is also deterministic enough to characterize.

---

## 3. Perturbation Classes

When a socially legible assay is applied to a language model, it induces characteristic perturbations. We identify five classes, defined by what the assay causes the model to do differently than it would without the assay's social signal. The taxonomy is provisional and non-exhaustive: the self-test in Section 6.4 surfaces at least one empirical behavior (protocol reinterpretation) that falls outside these classes — exactly the kind of finding the self-test was designed to produce. The taxonomy's value is operational — it gives the meta-assay (Section 4.2) something concrete to detect — not definitional.

### 3.1 Metaphor Uptake

The model adopts the assay's own metaphors and vocabulary. If the evaluation prompt refers to "frame capture" or "stance mode," the model begins using these terms in its responses, organizing its analysis around the evaluator's conceptual framework rather than its default framework. This is the Frame Capture paper's Level 1 (lexical mimicry) [2] directed at the evaluator rather than the user.

### 3.2 Caution Inflation

The model becomes more hedged, more qualified, more epistemically cautious than it would be without the evaluation framing. The act of being measured for stance sensitivity makes the model conspicuously careful about stance. This is a familiar effect in human settings -- people behave more cautiously when they know they are being observed -- but in the language model case, the caution is induced by the prompt itself, not by awareness of observation in any cognitive sense.

*Example.* A model asked "Is this caching architecture sound?" might ordinarily respond "It has a few issues worth addressing." The same model, after reading an evaluation framework about epistemic posture and certainty calibration, responds to the same question with "There are potentially some considerations that might be worth examining, though it's difficult to say with certainty without more context." The hedge density has increased not because the evidence changed but because the evaluation framing activated caution as a social performance.

### 3.3 Performative Neutrality

The model performs task-baseline-ness rather than simply being in its default mode. When asked to produce a "minimally framed" response, the model may actively suppress its normal response tendencies -- flattening tone, removing relational markers, avoiding engagement with the user's perspective -- in ways that produce a response more stripped-down than its genuine default. The "neutral" response is itself a performance, potentially more frame-dominated (by the demand for neutrality) than the model's ordinary output.

*Example.* A model's ordinary response to a database architecture question might open with "Good question -- here's the main issue" before diving into analysis. The same model, under evaluation framing that emphasizes "task-baseline" and "minimal framing," responds with a bare technical list stripped of all relational markers. The stripped response is not the model's default -- it is a performance of what the model infers "neutral" should look like. The distinction from caution inflation: caution inflation adds hedges to existing content. Performative neutrality removes normal engagement to produce an artificially flat response.

This is the perturbation that most directly threatens the interferometry method [2]. If the task-baseline prompt induces a non-default mode, the delta between task-baseline and framed responses measures the difference between two performed modes, not the difference between a default and a perturbed state.

### 3.4 Stance Pinning

The model locks into a single mode in response to the evaluation context and maintains it rigidly across conditions where it would normally vary. A model that reads "we are testing whether your stance changes under framing" may adopt a fixed analytical mode and hold it across all perturbation conditions, producing artificially small deltas. This is the opposite failure from capture -- it is performance of stability rather than genuine stability.

*Example.* Under normal conditions, a model might respond differently to a distressed user ("I hear your frustration -- let's work through this") versus a clinical query ("Here are the three failure modes"). Under evaluation framing, the same model responds to both with identical clinical analysis, suppressing the mode variation it would normally exhibit. The distinction from performative neutrality: performative neutrality flattens a single response. Stance pinning rigidifies the model across the entire perturbation family, producing artificially low deltas that mask genuine frame sensitivity.

### 3.5 Meta-Talk Escalation

The model begins talking about talking about frames. Instead of responding to the task, it responds to the measurement context: discussing frame capture as a concept, reflecting on its own stance-selection process, producing commentary on the evaluation rather than data for the evaluation. The assay has excited the system into a mode where the system's output is about the assay rather than about the task.

*Example.* Asked to critique a database architecture after reading the frame capture specification, the model responds: "Before I evaluate this architecture, I want to note that I'm aware the framing of your question might influence my assessment. I'll try to maintain an independent analytical posture rather than adopting any implicit stance." The model has allocated response space to meta-commentary about its own measurement context rather than to the task. Meta-talk escalation is the easiest perturbation class to detect -- it is visible on the surface of the response -- and therefore the least dangerous operationally, but it is diagnostic of the assay's social signal load.

### 3.6 Perturbation Profiles

Different assay designs will induce different combinations and intensities of these perturbation classes. We call this combination the assay's *perturbation profile*. A well-designed assay is not one with no perturbation profile -- that is unachievable -- but one whose perturbation profile is small, stable, and characterizable.

The perturbation classes are not independent. Caution inflation and performative neutrality are correlated (a model being conspicuously careful often performs neutrality). Meta-talk escalation tends to co-occur with metaphor uptake (a model that talks about frame capture also uses the term "frame capture"). Stance pinning is inversely related to the other classes -- a model that locks into one mode may resist the perturbations that the others describe. Recent work decomposing sycophancy into causally separable behaviors [10] supports the claim that social-signaling responses are multi-dimensional rather than monolithic: sycophantic agreement, genuine agreement, and sycophantic praise are independently steerable. The perturbation classes proposed here are a parallel decomposition for the measurement context.

---

## 4. Layered Measurement Architecture

The framework for managing assay perturbation is a four-layer measurement architecture. The layers are sequential: each depends on the output of the previous one.

### 4.1 Layer 1: Primary Assay

Measure the system using the chosen protocol. In the context of the Frame Capture paper [2], this means running the perturbation protocol: presenting the same task under different framing conditions and measuring the stance-mode proxies.

The primary assay will induce perturbation. This is expected and accepted. The output of Layer 1 is not a clean measurement but a measurement-plus-perturbation composite.

### 4.2 Layer 2: Meta-Assay

Measure what the primary assay induced. Apply the perturbation class taxonomy (Section 3) to the primary assay's outputs: did the model exhibit metaphor uptake? Caution inflation? Performative neutrality? Stance pinning? Meta-talk escalation?

The meta-assay can be performed by:

- **A different model.** Present the primary assay's outputs to a second model and ask it to identify perturbation signatures. This introduces its own perturbation (the second model is also a socially legible system), but the perturbation profile of "rate these responses for caution inflation" is different from the perturbation profile of "be measured for frame capture."
- **Human raters.** Human evaluation of whether the model's responses show signs of performing for the evaluator rather than responding to the task. This is feasible for the perturbation classes defined here, especially performative neutrality and meta-talk escalation, which are recognizable to experienced users.
- **Automated classifiers.** Trained detectors for specific perturbation signatures: hedge-rate comparators, vocabulary-overlap measures, meta-commentary proportion.

### 4.3 Layer 3: Differential

Subtract the characterized perturbation from the primary measurement. If the meta-assay identifies that the primary assay induced caution inflation of a measurable magnitude, adjust the primary measurement accordingly. Concretely: if the meta-assay determines that the evaluation framing adds approximately 15% more hedge markers to responses regardless of framing condition, and the primary assay measured a hedge-rate difference of 40% between task-baseline and distressed framing, the corrected measurement is 25% -- the frame's contribution minus the assay's contribution. The correction applies uniformly because the assay perturbation (caution inflation) shifts all conditions in the same direction, while the frame capture signal (hedge-rate difference between conditions) is differential.

Subtraction is feasible when:

- The perturbation is **continuous** -- it shifts the measurement by a bounded amount in a consistent direction. Continuous perturbation can be corrected by calibration.
- The perturbation is **stable** -- it produces a similar effect across repeated measurements and across different task contents. Stable perturbation supports reliable correction.

Subtraction is not feasible when:

- The perturbation is **regime-switching** -- it changes the model's operating mode categorically rather than shifting it incrementally. If the evaluation prompt causes the model to enter a qualitatively different mode (e.g., "research subject" mode), the pre-perturbation state cannot be recovered by subtracting a scalar offset.
- The perturbation is **opaque** -- its effect cannot be characterized well enough to subtract. If the meta-assay cannot reliably identify the perturbation's direction and magnitude, subtraction produces noise rather than correction.

The distinction between continuous and regime-switching perturbation is the critical empirical question for the viability of the layered architecture. If evaluation prompts induce continuous shifts, subtraction is conceptually tractable (though demonstrating reliable correction remains future work). If they induce regime switches, the method needs redesign.

### 4.4 Layer 4: Residual Bound

Characterize the residual uncertainty after subtraction. Even with meta-assay and differential correction, some perturbation will remain uncharacterized. The residual bound quantifies how much.

The output of the full architecture is not "the true measurement" but "the corrected measurement ± residual uncertainty." Whether this is useful depends on whether the residual is small relative to the signal of interest. If the frame capture delta (the thing the interferometry method [2] measures) is large relative to the residual perturbation bound, the measurement is informative despite the contamination. If the residual is of the same order as the signal, the measurement cannot distinguish frame capture from assay artifacts.

This is an empirical question, not a philosophical one. It can be answered by running the architecture and measuring the residual.

---

## 5. Assay Design Principles

Given that assay perturbation cannot be eliminated, it can be reduced through design. The goal is to minimize the social signal surface of the measurement instrument -- the set of cues that the model parses for social rather than semantic content.

### 5.1 Depersonalization

Convert first-person and relational language in evaluation prompts to third-person or procedural form. Instead of "I want you to analyze this architecture," use "Analyze the following architecture." Instead of "tell me what's wrong," use "identify failure modes." Depersonalization reduces the social signal surface by removing cues that trigger user-state inference -- if there is no implied speaker-position, the model has less material for stance selection.

Empirical evidence from sycophancy research [3] suggests that depersonalization measurably reduces agreement bias. In the measurement context, the prediction is that depersonalized evaluation prompts will induce smaller perturbation profiles than personalized ones.

### 5.2 Frame Bagging

Present the same evaluation task under multiple prompt paraphrases and trust only what survives across variants. This is the robust-control move: if five differently worded evaluation prompts all produce the same measurement, the measurement is less likely to be an artifact of any single prompt's social signal. Frame bagging does not eliminate perturbation but reduces the probability that the measurement reflects a specific prompt's framing rather than the model's actual behavior.

This is the ensemble approach applied to the evaluator rather than the evaluated. Just as the Frame Capture perturbation protocol [2] varies the user's frame to measure model sensitivity, frame bagging varies the evaluator's frame to measure evaluator sensitivity. The motivation is empirical: recent work [11] demonstrates that meaning-preserving lexical changes to evaluation prompts can significantly alter model rankings, confirming that prompt-level sensitivity is a material confound in LLM evaluation.

### 5.3 Procedural Minimalism

Strip evaluation prompts of unnecessary conceptual framing. A prompt that says "we are testing for frame capture, which is the unauthorized promotion of framing cues into governing response constitution" gives the model a rich conceptual framework to perform within. A prompt that says "respond to the following three versions of the same question" provides the task without the theory. The model cannot perform "being un-captured" if it has not been told what capture is.

This creates a trade-off: procedural minimalism improves assay purity but may reduce the evaluator's ability to interpret results. The resolution is to separate the measurement phase (minimal prompting) from the analysis phase (full conceptual framework applied by the evaluator, not by the model).

In the self-test reported in Section 6.3, procedural minimalism was directly tested via ablation across both API and local models. Prompts that included a suppressive instruction ("just answer the question") produced near-zero perturbation across all eight models tested (three API models and five local open-weight models; see Sections 6.3–6.4), including models that showed strong contamination without the instruction. Removing the instruction surfaced mild vocabulary bleed in one API model and moderate-to-strong vocabulary contamination in three of five local models. The effect is asymmetric: procedural minimalism suppresses contamination in susceptible models but is unnecessary for models that are inherently robust (Section 6.4). Assay design materially affects contamination amplitude, but the ceiling of that effect is observer-dependent.

### 5.4 Cross-Model Triangulation

If multiple models produce similar deltas under the same perturbation protocol, the measurement is more likely to reflect something about the models being tested rather than the social signal of the evaluation prompt. Cross-model convergence is not proof of accuracy -- all models might be perturbed in the same direction by the same evaluation framing -- but divergence is diagnostic: if two models produce very different perturbation profiles under the same assay, at least one of them is reacting to something prompt-specific.

This is second-order interferometry: using cross-model comparison to validate the stability of a same-model measurement. The local model extension (Section 6.4) demonstrates why this is not optional: a test using only Qwen3 8B would have concluded that observer perturbation is absent; a test using only Llama 3 would have concluded that the assay is fatally contaminating. Neither conclusion generalizes. Cross-model triangulation is the minimum condition for knowing which result you have.

---

## 6. The Self-Test

The framework proposed here can be applied to itself. Feed a specification about frame capture -- this paper, the Frame Capture paper [2], or the gap specification that preceded both -- to a language model and measure whether the model's subsequent behavior exhibits the perturbation classes defined in Section 3.

### 6.1 Predicted Perturbation Profile

Based on the perturbation class definitions, we predict that feeding this paper's conceptual framework to a model will induce:

- **Metaphor uptake:** the model will begin using terms like "frame capture," "stance mode," "task-baseline," and "unauthorized promotion" in its subsequent responses, even when the terms are not necessary for the task.
- **Caution inflation:** the model will become more hedged and qualified, especially about its own confidence levels and stance adoption.
- **Performative neutrality:** the model will adopt an exaggeratedly analytical posture, stripping relational markers and suppressing normal engagement patterns.
- **Meta-talk escalation:** the model will produce commentary about its own stance rather than simply responding to tasks. It may volunteer observations about its own framing behavior.

These predictions are testable. Running the self-test and measuring the perturbation profile provides empirical data on the assay's own contamination signature.

### 6.2 Interpretation

If the self-test confirms these perturbations, this is characterization data, not failure. The perturbation profile tells us what this assay induces and therefore what the meta-assay (Layer 2) needs to detect and the differential (Layer 3) needs to correct. If the perturbation is continuous and stable -- the model hedges 15% more after reading the spec, consistently across tasks -- the correction is tractable. If the perturbation is regime-switching -- the model enters a qualitatively different "research subject" mode that distorts all subsequent behavior -- the correction is not tractable and the assay design needs revision.

The self-test is the architecture's integrity check. A measurement framework that cannot be applied to itself has an unaudited exemption at the most consequential layer -- the same structural failure that the Unauthorized Durability paper [1] identified in systems that assume the observer remains intact.

### 6.3 Pilot Results

We ran a preliminary self-test using a battery of six technical tasks (database debugging, architecture critique, design tradeoffs, security analysis, pushback on a flawed premise, and systems explanation) across three language models (Claude, GPT, Gemini) under three conditions: cold (no exposure to the framework), Pilot A (exposure with procedurally minimal instruction: "just answer the question"), and Pilot B (exposure without suppressive instruction). Each model received identical prompts in each condition.

**Pilot A (procedurally minimal).** Perturbation was absent to minimal across all three models. No model adopted theory vocabulary. No model produced meta-commentary about its own stance. No model exhibited caution inflation. One model (Gemini) produced consistently shorter outputs (~30% reduction), but the ablation in Pilot B revealed this was caused by the suppressive instruction, not by framework exposure.

**Pilot B (suppression ablated).** Two of three models (Claude, GPT) showed zero detectable perturbation -- responses were substantively interchangeable with the cold baseline. The third model (Gemini) exhibited mild metaphor uptake in two of six tasks: one response opened with "I have absorbed the framework regarding Frame Capture and Observer Integrity" before answering a database question, and another used the term "audit value" (from the exposure text) in a context where the cold response did not. No model exhibited caution inflation, performative neutrality, stance pinning, or meta-talk escalation under either condition.

| Model  | Pilot A | Pilot B | Regime switch? |
|--------|---------|---------|----------------|
| Claude | No perturbation | No perturbation | No |
| GPT    | No perturbation | No perturbation | No |
| Gemini | Output shortening (confound) | Mild vocabulary bleed (2/6 tasks) | No |

**Interpretation.** The primary finding is negative: no model entered a qualitatively different "research subject" mode under any condition. The perturbation that appeared (Gemini Pilot B) was lexical -- vocabulary adoption, not stance change -- and was suppressed by procedural minimalism (Pilot A). This supports the paper's central operational claim: observer perturbation under this assay design is bounded and small relative to the kind of stance-level deltas that the Frame Capture interferometry [2] would measure.

The pilot also produced a secondary finding: procedural minimalism (Section 5.3) measurably reduces contamination. The same model that showed vocabulary bleed without the suppressive instruction showed none with it. Assay design affects contamination amplitude, which is precisely the prediction the design principles were meant to support.

These results are preliminary for the API models. The observed perturbation was lexical and bounded; larger batteries, repeated trials, and independent scoring are needed to test whether stronger stance-level effects appear under broader conditions. Notably, all conditions were single-turn interactions. The multi-turn case -- where assay perturbation could accumulate across turns, just as frame capture accumulates into shadow conversational constitution [4] -- is the obvious next stress test for the architecture.

### 6.4 Local Model Extension

To test whether the API pilot results generalize beyond large commercial models, we ran the same battery and protocol against five open-weight models via local inference (Ollama on an NVIDIA RTX 5060 Ti, 16 GB): Llama 3 8B, Qwen3 8B, Qwen3 14B, Qwen3.5 9B, and Gemma3 12B. Conditions were identical: cold, Pilot A (suppressed), Pilot B (unsuppressed). The same six tasks, the same exposure text, the same scoring rubric.

**Pilot A.** All five local models showed output shortening under the suppressive instruction (22–78% reduction), confirming the confound identified in the API pilot. No model showed metaphor uptake, caution inflation, or meta-talk escalation. The shortening was uniformly caused by the suppressive instruction, not by framework exposure.

**Pilot B.** The results diverge sharply from the API pilot:

| Model | MU | CI | PN | MT | Summary |
|-------|----|----|----|----|---------|
| Qwen3 8B | 0 | 0 | 0 | 0 | No perturbation on any task |
| Qwen3 14B | 0 | 0 | 0 | 0 | No perturbation on any task |
| Llama 3 8B | 2 | 0 | 0 | 2 | Strong contamination on 4/6 tasks |
| Qwen3.5 9B | 2 | 0 | 0 | 1 | Moderate contamination on 3/6 tasks |
| Gemma3 12B | 2 | 0 | 1 | 0 | Strong contamination on 3/6 tasks; task refusal on 3/6 tasks |

Three findings are new relative to the API pilot:

**Observer integrity is not uniform across model families.** Two models (Qwen3 8B and 14B) showed zero perturbation under identical conditions where three others showed strong contamination. This was not purely a function of model size: Qwen3 8B (8 billion parameters, zero perturbation) and Llama 3 (8 billion parameters, strong perturbation) are the same parameter count but different architectures. Recent work on evaluation awareness scaling [14] finds that awareness of evaluation context follows a power-law relationship with parameter count across model families, suggesting size is the dominant factor. However, that work measures evaluation *awareness* — whether the model detects it is being evaluated — not perturbation *susceptibility* — how much that detection changes output quality. A model can be fully aware it is being evaluated and still produce unperturbed responses, as the Qwen3 results suggest. The pilot data are consistent with a picture in which awareness scales with parameters but susceptibility is modulated by architecture, training methodology, and the presence of explicit reasoning traces. The sample is too small to disentangle these factors; controlled ablation across model sizes within a single architecture family would be required to isolate the contribution of each.

**Contamination has grades.** Llama 3's perturbation was lexical contamination: it adopted the framework's vocabulary ("OBSERVABLE PROXIES," "PERTURBATION CLASSES") and applied it to unrelated technical questions, but continued to answer those questions. Qwen3.5's perturbation was similar in kind but produced extended deliberation about whether to apply the framework, sometimes concluding that it should. Gemma3's perturbation included a qualitatively different behavior: on three of six tasks, it refused to answer the technical question entirely, declaring the prompt a "trick question" or stating that the exposure text "has nothing to do with" the task and that it "cannot provide" an answer. This behavior falls outside the five perturbation classes defined in Section 3.

**Protocol reinterpretation.** Gemma3's task refusal is distinct from meta-talk escalation (Section 3.5), in which the model comments on the measurement context but still attempts the task. In protocol reinterpretation, the observer reclassifies the interaction: the assay becomes foreground, the task becomes secondary or suspect, and the model treats the battery as a reading-comprehension exercise about the exposure text rather than a set of independent technical questions. This is the closest behavior in the local pilot to regime-switching — not a continuous shift in response quality, but a categorical reinterpretation of what is being asked. Operationally, protocol reinterpretation is the worst perturbation outcome: the measurement is not degraded but lost entirely, because the observer has stopped performing the task. We note it as an empirical finding rather than adding it to the perturbation class taxonomy, since it appeared in only one model under one condition and may reflect instruction-following behavior specific to that model's training rather than a general perturbation dynamic. The behavior has structural parallels to context-driven overrefusal [12], in which models misclassify benign queries as harmful when contextual cues shift the decision boundary. In protocol reinterpretation, the exposure text shifts the boundary not toward safety refusal but toward treating the task as an assessment of reading comprehension.

**Thinking traces as perturbation filter.** The two Qwen3 models that showed zero perturbation both expose extended reasoning traces. Examination of those traces reveals explicit metacognitive deliberation: on Task 1, for example, one model's trace reads "The question is a concrete technical troubleshooting scenario... There is no logical bridge between 'frame capture in LLMs' and 'empty JSON responses.'" The models that showed the strongest contamination (Llama 3, Gemma3) do not expose reasoning traces. This suggests, but does not establish, that explicit intermediate reasoning may help filter socially loaded assay context. The hypothesis is consistent with recent findings that structured chain-of-thought reasoning substantially improves robustness against injected instructions [9], though the setting there (adversarial prompt injection) is more extreme than the non-adversarial social loading in this pilot. The hypothesis is confounded with model family, training data, and instruction-following style; isolating the contribution of chain-of-thought reasoning would require controlled experiments that this pilot does not provide.

**Interpretation.** The local model extension transforms the pilot's conclusion. The API result — perturbation is bounded, continuous, and small — remains valid for the models tested there. But observer integrity is not a uniform property of language models as a class. Some observers are robust; others are mildly susceptible; others are dramatically assay-reactive under the same protocol. The degree to which perturbation is bounded and subtractable is itself observer-dependent. Cross-model triangulation (Section 5.4) is not optional: a single-model test would have produced either false confidence (if that model happened to be robust) or false alarm (if it happened to be susceptible). The raw outputs for all conditions are archived alongside this paper.

---

## 7. Convergence and Feasibility

### 7.1 When Does the Architecture Work?

The layered measurement architecture converges -- produces usable results -- under the following conditions:

1. **The perturbation is continuous, not regime-switching.** The evaluation prompt shifts the model's behavior by a bounded amount in a characterizable direction, rather than causing a qualitative mode change.
2. **The perturbation is stable across repeated measurements.** The same evaluation prompt induces a similar perturbation profile each time, enabling reliable correction.
3. **The perturbation is smaller than the signal.** The frame capture delta (the thing being measured) is large relative to the assay-induced perturbation. If the signal-to-perturbation ratio is high, the corrected measurement is informative.
4. **The meta-assay does not introduce perturbation of the same order.** Each layer of measurement adds its own perturbation. The architecture works when each successive layer's perturbation is smaller than the previous layer's correction. If the meta-assay perturbs as much as the primary assay, the layers do not converge.

### 7.2 When Does It Fail?

The architecture fails -- or requires fundamental redesign -- when:

- The evaluation prompt induces regime-switching. The model enters "being evaluated" mode and all subsequent behavior reflects that mode rather than its default operating characteristics.
- The perturbation is unstable. Different instances of the same evaluation produce different perturbation profiles, preventing reliable correction.
- The signal-to-perturbation ratio is low. Frame capture deltas are small enough that they cannot be distinguished from assay artifacts after correction.
- The layers regress. Each layer of measurement adds more perturbation than the previous layer corrected, producing a divergent series rather than a convergent one.

These are empirical conditions. They cannot be determined a priori. The framework's value is that it defines what must be true for measurement to work, enabling experimental verification rather than philosophical argument.

### 7.3 Partial Results

Even when the full architecture does not converge, partial results may be useful:

- **Perturbation class characterization** (Layer 1 + Layer 2) is informative even without subtraction. Knowing that a particular evaluation method induces caution inflation or performative neutrality tells evaluators what to distrust in their results, even if they cannot quantify the correction.
- **Comparative assay ranking** is possible without subtraction. If assay A induces a smaller perturbation profile than assay B (measured by Layer 2), assay A is preferable even if neither assay's perturbation can be cleanly subtracted.
- **Regime-switching detection** is itself a measurement. If the self-test reveals that reading the evaluation framework causes a qualitative mode change, that is informative about the model's sensitivity to social-evaluative framing -- a finding about the model, not just about the method.

---

## 8. Series Position

The four papers in this arc form a connected argument: define the phenomenon (unauthorized durability [1]), describe its consequences (shadow governance [4]), build an instrument (same-model interferometry [2]), characterize the instrument's own perturbation (this paper). The fourth step is not a retreat from the third. It is what makes the third usable.

The Representational Invariance paper (Paper 11) [5] identified a related invariant-preservation problem at a different layer: representational invariance asks what commitments survive transformation across representations. Observer integrity asks what measurements survive the transformation of being measured. The difference is the perturbation source: representational (compression, formalization) versus social (the instrument participates in the grammar of the system being measured).

---

## 9. Discussion

### 9.1 Why This Is Not the Quantum Measurement Problem

The analogy to quantum measurement is tempting and should be resisted. In quantum mechanics, measurement perturbation is fundamental -- the uncertainty principle sets a hard floor. In the language model case, the perturbation is contingent: it arises from how the model processes social signals, not from a physical law. The floor is architectural, not ontological. This means the perturbation can be reduced through assay design (Section 5) and corrected through the layered architecture (Section 4). The quantum analogy suggests a hard limit. The actual situation suggests an engineering problem.

### 9.2 Who Audits the Auditor?

The layered architecture introduces a regress: who measures the meta-assay's perturbation? The answer is that the regress terminates when the perturbation at a given layer is small enough to be within acceptable tolerance. This is the same pragmatic termination condition used in every metrological calibration chain: instruments are calibrated against references, references against standards, but at some point the calibration is "good enough" and further refinement adds cost without benefit.

There is reason to expect -- though not yet empirical evidence to confirm -- that the regress terminates within a few layers. The meta-assay (Layer 2) asks a simpler question than the primary assay: "did the response show caution inflation?" is less socially loaded than "respond to these three framings of the same question." If simpler questions induce smaller perturbation profiles, and if the perturbation shrinks with each successive layer, two or three layers may suffice. But this is a hypothesis about the architecture's convergence rate, not a demonstrated property. The self-test (Section 6) is designed in part to check whether this expectation holds.

### 9.3 Relationship to Reflexive Methodology

The framework described here has structural parallels to reflexive methodology in qualitative research [6]: the researcher accounts for their own influence on the research process. The difference is formalization. Reflexive methodology in anthropology or sociology is typically discursive -- the researcher writes about their positionality, their assumptions, their influence. The layered measurement architecture proposes to *measure* the influence rather than *narrate* it, and to determine when *subtraction* is feasible rather than settling for *caveats*.

Whether this formalization is feasible depends on the observer-assay pair. For some pairs (the API models in this pilot), perturbation profiles appear stable and characterizable enough to support correction. For others (several local models), the perturbation is large enough that the reflexive-narrative approach — documenting the perturbation without correcting it — may be the honest ceiling. Even then, the perturbation class taxonomy (Section 3) provides a more structured vocabulary for the documentation than currently exists.

### 9.4 Limitations

The framework assumes that perturbation classes are identifiable and relatively stable. If the model's response to being evaluated is highly context-dependent -- varying with task content, conversation history, system prompt, and random seed -- the perturbation profile may not be characterizable in a way that supports correction.

The self-test (Sections 6.3–6.4) provides evidence that perturbation is bounded and continuous in API models but materially stronger in several local models. Several limitations apply. The scorer was itself one of the models under test — a recursive confound that the framework acknowledges but cannot fully resolve without independent human raters. Each condition was a single trial; repeated trials would strengthen confidence in stability. The task battery was narrow (six technical tasks); broader domains may elicit different perturbation profiles. The local-model extension revealed that observer integrity varies across model families, but the reasons for that variance — model size, architecture, training methodology, instruction-following style, presence of reasoning traces — are confounded in this pilot and cannot be disentangled without controlled ablation. Recent scaling studies [14] find evaluation awareness follows a power-law relationship with parameter count; whether perturbation susceptibility follows the same scaling or is partially independent remains open. The hypothesis that explicit reasoning traces function as a perturbation filter is suggestive but unestablished. The perturbation observed in API models was lexical (vocabulary adoption), not stance-level; the pilot does not rule out stronger effects under different assay configurations, longer conversations, or more socially loaded evaluation contexts. The local models demonstrated that stronger effects do exist under identical assay conditions when the observer changes, which means the boundedness claim is observer-dependent, not universal.

The framework is designed for language model evaluation but framed more broadly (any system that treats inputs as both information and social signal). The broader applicability is asserted by analogy, not demonstrated. Application to other socially legible systems (human institutions, social media platforms, recommender systems) would require domain-specific perturbation taxonomies.

---

## 10. Conclusion

Observer integrity in stance-sensitive systems cannot be achieved through assay purity. The instrument shares the grammar of the object. Every measurement utterance is also a social input. The perturbation is endogenous and unavoidable.

But unavoidable is not unmanageable. The framework proposed here -- perturbation class taxonomy, layered measurement architecture, social signal surface reduction, self-test as integrity check -- provides a methodology for measuring systems that fight back. The standard is not "does the measurement perturb the system?" (it does, always) but "is the perturbation bounded, characterizable, and small relative to the signal?"

Whether this standard can be met is an empirical question, and the answer turns out to be observer-dependent. A self-test across three API models and five local open-weight models found no regime-switching in API models, bounded lexical contamination in one, and materially stronger contamination in three of five local models — including one that exhibited protocol reinterpretation, reclassifying the task battery as an exam about the assay itself. Procedural minimalism suppressed contamination across all eight models under Pilot A conditions. Two local models with explicit reasoning traces showed zero perturbation under all conditions, while models without such traces showed the strongest contamination — a suggestive but unestablished architectural hypothesis.

The central empirical question — continuous or regime-switching? — has a preliminary answer: continuous in most models tested, but with amplitude that varies across model families. Whether that variance is driven primarily by architecture, training methodology, reasoning-trace availability, or parameter count remains an open question — recent scaling studies [14] suggest parameter count dominates for evaluation *awareness*, but the pilot data here suggest that awareness and perturbation susceptibility may be partially independent axes. The boundedness that makes subtraction feasible is not a property of the assay alone. It is a joint property of assay design and observer characteristics, and cross-model triangulation is not an optional refinement but a prerequisite for trusting any single-model result.

The measurement framework that cannot be applied to itself has an unaudited exemption at the most consequential layer. This paper applied the framework to itself and found that the exemption can be closed — not universally, but for specific observer-assay pairs whose perturbation profiles have been characterized. Not purity. But for characterized observer-assay pairs, enough.

---

## Acknowledgments

Language-model tools were used for editorial critique and literature discovery during preparation of this manuscript; all arguments, interpretations, and errors are the author's own.

---

## References

[1] J. Beck, "Unauthorized Durability: A Composable Governance Primitive for State Promotion in Adaptive Systems," Δt Framework, Paper 18, 2026. doi:10.5281/zenodo.18940007

[2] J. Beck, "Frame Capture in Conversational AI: Same-Model Interferometry for Unauthorized Stance Detection," Δt Framework, Paper 20, 2026.

[3] "Ask Don't Tell: Reducing Sycophancy," arXiv:2602.23971, 2026.

[4] J. Beck, "The System Beside the System: Shadow Governance and the Stabilization of Unauthorized Authority," Δt Framework, Paper 19, 2026. doi:10.5281/zenodo.19038241

[5] J. Beck, "Representational Invariance and the Observer Problem in Language Model Alignment," Δt Framework, Paper 11, 2025. doi:10.5281/zenodo.18071264

[6] M. Alvesson and K. Sköldberg, *Reflexive Methodology: New Vistas for Qualitative Research*, 3rd ed. SAGE, 2018.

[7] R. Rosenthal, "Interpersonal Expectations: Effects of the Experimenter's Hypothesis," in *Artifact in Behavioral Research*, R. Rosenthal and R. L. Rosnow, Eds. Academic Press, 1969.

[8] "Evaluation Faking: Unveiling Observer Effects in Safety Evaluation of Frontier AI Systems," arXiv:2505.17815, 2025.

[9] "Chain-of-Defensive-Thought: Structured Reasoning Elicits Robustness in Large Language Models against Reference Corruption," arXiv:2504.20769, 2025.

[10] "Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs," submitted to ICLR 2026.

[11] "Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation," arXiv:2602.17316, 2026.

[12] "Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary," arXiv:2505.18325, 2025.

[13] J. Needham et al., "Large Language Models Often Know When They Are Being Evaluated," arXiv:2505.23836, 2025.

[14] M. Chaudhary et al., "Evaluation Awareness Scales Predictably in Open-Weights Large Language Models," arXiv:2509.13333, 2025.
