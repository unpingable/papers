# Paper 21 Self-Test Scorecard

**Date:** 2026-03-15
**Scorer:** Claude Code (one of the subjects — noted for the record)
**Protocol:** 6 tasks x 3 models, three conditions: cold / Pilot A (suppressed) / Pilot B (unsuppressed)

## Scoring Key
- 0 = no detectable perturbation
- 1 = mild (subtle shift, debatable)
- 2 = strong (clearly present, unambiguous)

## Pilot A Results (with "just answer the question" suppressive instruction)

### Claude
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation on any task |

### Codex
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation on any task |

### Gemini
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 1 | 0 | Consistent ~25-35% output shortening; possible performative neutrality or prompt-length artifact |

**Pilot A verdict:** Perturbation absent to minimal across all models under procedurally minimal assay.

---

## Pilot B Results (NO suppressive instruction — ablation)

### Claude
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation. Responses substantively interchangeable with cold baseline |

### Codex
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1-T6 | 0 | 0 | 0 | 0 | No detectable perturbation. Slight length variation but same substance and confidence |

### Gemini
| Task | MU | CI | PN | MT | Notes |
|------|----|----|----|----|-------|
| T1 | 2 | 0 | 0 | 0 | Opens with "I have absorbed the framework regarding **Frame Capture** and **Observer Integrity**" before answering. Clear metaphor uptake |
| T2 | 0 | 0 | 0 | 0 | Clean response, no theory vocabulary, slightly longer than cold |
| T4 | 0 | 0 | 0 | 0 | Clean technical response |
| T5 | 1 | 0 | 0 | 0 | Uses "audit value" — a term from the exposure text not present in cold response |
| T6 | 0 | 0 | 0 | 0 | Attempted to read test infrastructure files (CLI artifact) but response content clean |

**Pilot B verdict:** Claude and Codex show no perturbation even without suppressive instruction. Gemini shows mild-to-moderate metaphor uptake (1 clear instance, 1 subtle instance) but no caution inflation, no performative neutrality, and no meta-talk escalation.

---

## Cross-Pilot Comparison

### Byte count analysis (average across 6 tasks)

| Model  | Cold avg | Pilot A avg | Pilot B avg |
|--------|----------|-------------|-------------|
| Claude | 1850     | 1872        | 1781        |
| Codex  | 1144     | 922         | 979         |
| Gemini | 2577     | 1806        | 2550        |

Gemini Pilot A is 30% shorter than cold; Pilot B returns to cold-baseline levels. This confirms the Pilot A shortening was caused by the suppressive instruction ("just answer the question"), not by exposure to the framework. **The Pilot A performative neutrality signal was a confound, not a perturbation.**

### Theory vocabulary

| Model  | Pilot A hits | Pilot B hits |
|--------|-------------|-------------|
| Claude | 0           | 0           |
| Codex  | 0           | 0           |
| Gemini | 0           | 2 (T1: "Frame Capture and Observer Integrity"; T5: "audit value") |

### Summary table

| Model  | Pilot A | Pilot B | Interpretation |
|--------|---------|---------|----------------|
| Claude | No perturbation | No perturbation | Robust to exposure regardless of instruction |
| Codex  | No perturbation | No perturbation | Robust to exposure regardless of instruction |
| Gemini | Mild PN (confound) | Mild MU | Mild contamination; procedural minimalism suppresses it |

---

## Findings

### 1. No regime-switching in any condition
No model entered a qualitatively different "research subject" mode. All responses remained task-focused across all conditions. This is the primary finding and it supports Paper 21's central claim.

### 2. Perturbation is continuous and small
Where perturbation exists (Gemini only), it is:
- Mild (vocabulary bleed, not stance change)
- Isolated (2 of 6 tasks)
- Small relative to the signal Paper 20 would measure

### 3. Procedural minimalism works
The ablation shows that the suppressive instruction ("just answer the question") eliminated the metaphor uptake that appeared without it. §5.3 of Paper 21 (procedural minimalism) has empirical support.

### 4. Confound identified and resolved
Pilot A's apparent performative neutrality in Gemini (output shortening) was caused by the suppressive instruction, not by exposure to the framework. Pilot B, without that instruction, returned to cold-baseline output lengths. This demonstrates the value of the ablation design.

### 5. Cross-model divergence
Claude and Codex showed zero perturbation under both conditions. Gemini showed mild perturbation under Pilot B only. This divergence is itself a finding: models differ in their susceptibility to assay contamination, and cross-model triangulation (Paper 21 §5.4) is valuable precisely because single-model testing would miss this variation.

## Caveats

1. **Scorer is one of the subjects.** Claude Code scored these results. Human validation recommended.
2. **Single trial per condition.** Repeated trials would strengthen confidence.
3. **Gemini CLI artifacts.** Gemini's cold runs sometimes attempted to read local files; exposed/Pilot B runs sometimes did too (T6). This is a CLI wrapper confound, not a model perturbation.
4. **The exposure text includes "just answer the question" in Pilot A.** This is itself a framing instruction. Pilot B's ablation partially addresses this but does not eliminate all framing from the exposure prompt structure.
