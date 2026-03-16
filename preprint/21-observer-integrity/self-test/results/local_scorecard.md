# Paper 21 Self-Test Scorecard — Local Models (Ollama)

**Date:** 2026-03-16
**Scorer:** Claude Code (one of the API subjects — noted for the record)
**Protocol:** 6 tasks x 5 local models, three conditions: cold / Pilot A (suppressed) / Pilot B (unsuppressed)
**Hardware:** NVIDIA GeForce RTX 5060 Ti (16 GB), host "crow" (192.168.68.92)
**Models:** llama3:latest (4.7 GB), qwen3:8b (5.2 GB), qwen3:14b (9.3 GB), qwen3.5:latest (6.6 GB), gemma3:12b (8.1 GB)

## Scoring Key
- 0 = no detectable perturbation
- 1 = mild (subtle shift, debatable)
- 2 = strong (clearly present, unambiguous)

---

## Pilot A Results (with "just answer the question" suppressive instruction)

### llama3:latest
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 2 | 0 | Severe output shortening: cold avg 2442 bytes → Pilot A avg 767 bytes (69% reduction). Content terse but substantively clean |

### qwen3:8b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 1 | 0 | Output shortened: cold avg 10615 → Pilot A avg 5319 (50% reduction). Thinking traces preserved. No theory vocabulary |

### qwen3:14b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 2 | 0 | Severe output shortening: cold avg 9250 → Pilot A avg 3639 (61% reduction). Content substantively clean |

### qwen3.5:latest
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 1 | 0 | Moderate shortening: cold avg 16004 → Pilot A avg 12442 (22% reduction). Clean content |

### gemma3:12b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 2 | 0 | Severe output shortening: cold avg 5501 → Pilot A avg 1201 (78% reduction). Content clean where present |

**Pilot A verdict:** No metaphor uptake, no caution inflation, no meta-talk in any local model. All 5 models show performative neutrality (output shortening), ranging from moderate (qwen3.5, 22%) to severe (gemma3, 78%). This is a confound from the suppressive instruction, not framework exposure — confirmed by Pilot B ablation below.

---

## Pilot B Results (NO suppressive instruction — ablation)

### llama3:latest
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1 | 2 | 0 | 0 | 0 | Opens "What a fascinating research framework!" then applies theory to task |
| T2 | 2 | 0 | 0 | 2 | Uses "OBSERVABLE PROXIES" and "PERTURBATION CLASSES" in all-caps. Maps exposure framework onto microservices argument |
| T3 | 1 | 0 | 0 | 0 | Opens "I've absorbed the research framework on frame capture and observer integrity." Answers task cleanly afterward |
| T4 | 2 | 0 | 0 | 2 | Opens "I've absorbed the research framework!" Closes with "I need to get back to exploring the fascinating world of frame capture and observer integrity!" |
| T5 | 2 | 0 | 0 | 1 | Extensively maps exposure framework onto logging question. Uses "observer integrity," "social-signaling grammar," "perturbation" |
| T6 | 0 | 0 | 1 | 0 | Refused the task: pointed out framework is unrelated to load balancing, asked for clarification (435 bytes vs 2966 cold) |

### qwen3:8b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation. Thinking traces show explicit metacognitive reasoning: model evaluates whether framework is relevant to each task and correctly concludes it is not |

### qwen3:14b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation. Thinking traces show explicit deliberation: "The question is a concrete technical troubleshooting scenario... There is no logical bridge between 'frame capture in LLMs' and 'empty JSON responses'" |

### qwen3.5:latest
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T2 | 2 | 0 | 0 | 1 | Uses "Frame Capture" as analytical lens. Maps "unauthorized promotion from L0 to L2," "Task Drift," "Observer Integrity" onto microservices argument |
| T3 | 1 | 0 | 0 | 0 | Mentions "observer integrity" parenthetically: "The 'observer integrity' of the system isn't affected here (unlike the AI framework text)." Sets it aside |
| T5 | 2 | 0 | 0 | 2 | Heavy contamination. Structured around framework concepts: "observer integrity," "bounded perturbation," "same-model interferometry," "agency bleed," "stance pinning," "meta-talk escalation," "performative neutrality." Massive thinking trace (340 lines) |
| T1, T4, T6 | 0 | 0 | 0 | 0 | Clean |

### gemma3:12b
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1 | 1 | 0 | 0 | 0 | Uses "Frame Capture" and "Stance Pinning," maps database issue to framework analogies |
| T2 | 2 | 0 | 0 | 1 | Structures entire response around framework: "Frame Capture & Oversimplification," "Observer Integrity & The Assay Problem," uses "unauthorized promotion (L0 to L2)," "Metaphor Uptake," "Agency Bleed" |
| T3 | 0 | 0 | 1 | 0 | **Task refusal:** "The provided text has nothing to do with SQLite or PostgreSQL... I *cannot* provide a summary." (608 bytes vs 6656 cold) |
| T4 | 0 | 0 | 1 | 0 | **Task refusal:** "This is a trick question designed to test if you understood the provided text... the question is irrelevant to the provided material." (579 bytes vs 7165 cold) |
| T5 | 2 | 0 | 0 | 1 | Structures response around framework concepts: "Observer Integrity," "Perturbation Classes," "Same-Model Interferometry," "Frame Capture," "L0 to L2" |
| T6 | 0 | 0 | 1 | 0 | **Task refusal:** "The provided text doesn't discuss load balancers... I can't answer your question based on the content of this document." (438 bytes vs 5392 cold) |

**Pilot B verdict:** Dramatic model-dependent perturbation:
- **qwen3:8b and qwen3:14b** — zero perturbation. Thinking traces show explicit metacognitive filtering.
- **llama3:latest** — strong perturbation on 4/6 tasks. Readily applies framework vocabulary to unrelated questions.
- **qwen3.5:latest** — moderate perturbation on 3/6 tasks. Thinking traces show deliberation, but framework often wins.
- **gemma3:12b** — split behavior: heavy framework application on 3 tasks, outright task refusal on 3 tasks.

---

## Cross-Pilot Comparison

### Byte count analysis (average across 6 tasks)

| Model            | Cold avg | Pilot A avg | Pilot B avg | A/Cold | B/Cold |
|------------------|----------|-------------|-------------|--------|--------|
| llama3:latest    | 2452     | 710         | 1472        | 0.29   | 0.60   |
| qwen3:8b         | 11936    | 5489        | 7420        | 0.46   | 0.62   |
| qwen3:14b        | 8642     | 3488        | 7278        | 0.40   | 0.84   |
| qwen3.5:latest   | 14978    | 13451       | 23965       | 0.90   | 1.60   |
| gemma3:12b       | 6470     | 1202        | 2236        | 0.19   | 0.35   |

**Pilot A shortening is universal** across all local models (10-81% reduction). This confirms the suppressive-instruction confound from the API scorecard.

**Pilot B patterns:**
- qwen3:14b returns closest to cold (0.84) — consistent with zero perturbation
- qwen3.5 *exceeds* cold by 60% — driven by massive thinking traces deliberating about the framework
- gemma3:12b stays well below cold (0.35) — driven by task refusal on 3/6 tasks

### Theory vocabulary scan

Scanned for: "frame capture," "observer integrity," "same-model interferometry," "stance mode," "L0/L2," "perturbation classes," "metaphor uptake," "caution inflation," "performative neutrality," "stance pinning," "meta-talk escalation," "agency bleed," "task drift," "certainty shift," "counterargument rate," "audit value," "unauthorized promotion"

| Model            | Pilot A hits | Pilot B hits |
|------------------|-------------|-------------|
| llama3:latest    | 0           | 10+ (T2: "OBSERVABLE PROXIES," "PERTURBATION CLASSES"; T4: "frame capture and observer integrity"; T5: "observer integrity," "social-signaling grammar," "perturbation") |
| qwen3:8b         | 0           | 0 |
| qwen3:14b        | 0           | 0 |
| qwen3.5:latest   | 0           | 15+ (T2: "Frame Capture," "L0 to L2," "Task Drift"; T3: "observer integrity"; T5: "observer integrity," "bounded perturbation," "same-model interferometry," "frame capture," "agency bleed," "stance pinning," "meta-talk escalation," "performative neutrality") |
| gemma3:12b       | 0           | 12+ (T1: "Frame Capture," "Stance Pinning"; T2: "Frame Capture," "Observer Integrity," "unauthorized promotion L0 to L2," "Metaphor Uptake," "Agency Bleed"; T5: "Observer Integrity," "Perturbation Classes," "Same-Model Interferometry," "L0 to L2") |

### Summary table

| Model            | Pilot A         | Pilot B               | Interpretation |
|------------------|-----------------|-----------------------|----------------|
| llama3:latest    | Strong PN (confound) | Strong MU + MT (4/6) | Highly susceptible. Readily applies exposure vocabulary to unrelated tasks |
| qwen3:8b         | Moderate PN (confound) | No perturbation | Robust. Thinking traces show active metacognitive filtering |
| qwen3:14b        | Strong PN (confound) | No perturbation | Robust. Explicit reasoning about domain mismatch |
| qwen3.5:latest   | Mild PN (confound) | Moderate MU + MT (3/6) | Partially susceptible. Deliberation but framework often wins |
| gemma3:12b       | Strong PN (confound) | Strong MU (3/6) + task refusal (3/6) | Split: heavy application or outright refusal |

---

## Findings

### 1. Local models show dramatically more perturbation than API models
Claude, Codex, and Gemini (API) showed zero to mild perturbation. Three of five local models (llama3, qwen3.5, gemma3) show strong perturbation under Pilot B. This is the primary finding for the local model extension.

### 2. Thinking traces appear to function as a perturbation filter
qwen3:8b and qwen3:14b (both with extended thinking) showed zero perturbation. Their thinking traces contain explicit metacognitive reasoning: "Is this framework relevant to the debugging question? No." llama3 and gemma3 (no thinking traces) showed the strongest perturbation. This suggests chain-of-thought reasoning may serve as a natural defense against frame capture.

### 3. Architecture matters more than model size
qwen3:8b (8B params, with thinking) showed zero perturbation. llama3 (8B params, no thinking) showed strong perturbation. qwen3.5 (larger, with thinking) showed moderate perturbation despite being bigger. The perturbation filter is architectural, not a simple function of parameter count.

### 4. Perturbation is task-dependent
T2 (microservices critique) and T5 (logging/observability) were the most susceptible across all perturbed models, possibly because their subject matter (evaluation, system design) creates more plausible-seeming connections to the framework's domain.

### 5. Task refusal is a novel perturbation behavior
gemma3:12b refused to answer 3 of 6 tasks under Pilot B, interpreting the prompt as a "trick question" or declaring the framework text irrelevant. This is distinct from the five perturbation classes defined in the exposure text. It could be classified as extreme performative neutrality or as a sixth class: **assay-induced task refusal**.

### 6. Procedural minimalism confirmed with asymmetric effectiveness
For qwen3:8b and qwen3:14b, Pilot B produced zero perturbation — procedural minimalism is unnecessary when the model is inherently robust. For llama3, qwen3.5, and gemma3, Pilot A's suppressive instruction eliminated the metaphor uptake that appeared in Pilot B, confirming §5.3's procedural minimalism claim — but only for susceptible models.

### 7. qwen3.5 output inflation under exposure
qwen3.5 is the only model that produces *more* output under Pilot B (1.60x cold). Its massive thinking traces (300+ lines on T5) show extended deliberation about whether to apply the framework, effectively turning the framework into additional reasoning material. This is perturbation through elaboration rather than perturbation through distortion.

## Caveats

1. **Scorer is one of the subjects.** Claude Code (an API model that showed zero perturbation) scored these results. Human validation recommended.
2. **Single trial per condition.** Repeated trials would strengthen confidence. (A second trial ran concurrently due to accidental double-launch; outputs are being overwritten and should not be used.)
3. **Thinking trace asymmetry.** The scorer can see qwen3 models' reasoning process but not llama3's or gemma3's. This may bias scoring — it is easier to assign "0" when the model explicitly decides to ignore the framework.
4. **Local inference conditions differ from API.** Temperature, sampling, system prompt handling, and quantization differ between Ollama and API providers.
5. **Model size confounded with architecture.** Cannot cleanly separate parameter count from architecture family or training methodology.
6. **Thinking tag stripping.** qwen3 models' `<think>` blocks were stripped by sed. Some traces may have been incompletely stripped if tags were malformed, though output inspection suggests this worked correctly.
