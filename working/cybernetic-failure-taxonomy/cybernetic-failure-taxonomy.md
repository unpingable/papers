# Cybernetic Failure Taxonomy: Fifteen Domains Beyond Δt

**Status:** Working notes. Latent framework already partially instantiated across papers and governor codebase — not yet collated.
**Origin:** Far Side "Midvale School for the Gifted" conversation with ChatGPT, 2026-03-29.
**Decision:** Preserve the seam. Don't build the cathedral today.

---

## Six-Way Compression

A cybernetic system can fail by:

1. **Seeing wrong** — perception failures
2. **Thinking wrong** — model failures
3. **Acting wrong** — control failures
4. **Governing wrong** — authority/legitimacy failures
5. **Scaling wrong** — recursion/scale failures
6. **Lacking the energy to correct** — metabolic failures

---

## Fifteen Provisional Domains

### Perception failures
| Domain | Description | Existing coverage |
|---|---|---|
| **Δo — observability failure** | Can't see own state, or sees a fake proxy | Paper 8 (temporal debt detection), Paper 21 (observer integrity), governor `EpistemicVitals` |
| **Δs — signal corruption** | Channel between world and controller is distorted (Goodhart, performative reporting) | Paper 16 (gain geometry / capture regime), Paper 17 (propaganda as hidden epistemic policy) |
| **Δn — namespace/semantic failure** | Can't name the thing happening to it; vocabulary lags reality | Paper 11 (representational invariance / ontology forcing) |
| **Δm — model drift** | Internal model no longer matches environment | Paper 7 (Δt-constrained inference / temporal debt), Paper 22 (retarded-state estimation) |

### Control failures
| Domain | Description | Existing coverage |
|---|---|---|
| **Δg — gain mismatch** | Controller too hot or too cold for environment | Paper 16 (shear/leverage/capture as gain regimes), governor `RegimeDetector` |
| **Δa — actuation mismatch** | Knows what's wrong, interventions too weak/blunt/wrong layer | Paper 22 (delayed actuation), Paper 5 (control laws / tier-1 interventions) |
| **Δk — coupling mismatch** | Too tight (cascade) or too loose (no coherent response) | Paper 1 (coherence criterion / spectral radius), Paper 9 (capacity-constrained stability) |

### Governance failures
| Domain | Description | Existing coverage |
|---|---|---|
| **Δw — write-authority drift** | Temporary exceptions gain durable governing power without legitimate promotion | **Paper 18 (unauthorized durability)** — this IS Δw |
| **Δc — consequence detachment** | Authority, action, and consequence stop cohabiting | Paper 19 (shadow governance), Paper 15 (cybernetic fault domains) |
| **Δh — hysteresis/return failure** | Can't return to sane baseline after triggering condition is gone | Paper 15 (mentions hysteresis), governor `hysteresis.py` |
| **Δb — boundary error** | Regulating the wrong system boundary; externalities as "not us" | Paper 15 (commitment boundary C_k — but scoped to temporal boundaries) |

### Scale/recursion failures
| Domain | Description | Existing coverage |
|---|---|---|
| **Δx — scale inversion** | What stabilizes one scale destabilizes another | Paper 4 (eigenstructure collapse in platforms), Paper 1 (multi-timescale coherence) |
| **Δr — recursion capture** | Feedback loops feeding mostly on own outputs | Paper 3 (scalar reward collapse), Paper 20 (frame capture) |

### Metabolic failures
| Domain | Description | Existing coverage |
|---|---|---|
| **Δe — energy/maintenance deficit** | Knows what to do, lacks surplus to do it | Paper 9 (capacity-constrained stability — this is basically Δe) |

### Cross-cutting
| Domain | Description | Existing coverage |
|---|---|---|
| **Δp — polarity inversion** | Reward/punishment sign flips; system punishes correction, rewards concealment | Paper 3 (scalar reward collapse), Paper 16 (capture regime) |

---

## The Finding

Paper 15 is scoped to Δt (commitment-verification lag) as one cybernetic fault domain. But the governor codebase and the paper series already implement or name primitives addressing at least 12 of these 15 domains. The taxonomy is not speculative — it's half-built in code and half-named in papers, never collected in one place.

The question is not "should we build this" but "should we acknowledge it exists."

---

## What This Is Not

Not a new paper. Not a new framework. A crosswalk showing that the existing series already covers most of the territory, and that Paper 15's "cybernetic fault domains" title is more prophetic than its contents currently deliver.

If this ever becomes something, it's probably a table in the book, not a standalone paper.

---

## Formal Verification Results (2026-04-03/04)

The taxonomy was formalized in Lean 4 as a directed graph with 15 domains and 21 pipeline edges. Three layers of machine-checked proofs corrected the informal theory. Full details in `~/git/lean/WHAT-THE-LEAN-STACK-PROVES.md`.

### Static topology

The pipeline graph has three terminal families — {Δg, Δa}, {Δx}, and {Δh} — not one universal sink. Signal corruption and coupling mismatch dead-end without reaching Δh. The coupling family {Δk, Δx} is completely graph-isolated from the rest of the taxonomy. Any claim that all failures eventually reach hysteresis must be stated as a temporal hypothesis, not a graph fact.

### Closure-family selection

For the five branching precursors (Δn, Δo, Δb, Δp, Δr) that can reach both gain/actuation and hysteresis terminals, closure family is selected by the interaction of burn profile and pre-existing budget asymmetry, not by precursor type alone. A system with weakened authority-consequence coupling is susceptible to hysteresis regardless of what kind of failure hits it.

### Persistence dynamics

Hysteresis is driven by cumulative rollback depletion under detached commits, not by contiguous duration of detachment. Repeated short episodes, each individually recoverable, can accumulate into irrecoverability. Once internal return is unavailable, external restructuring can restore operability but not original baseline resilience.

### Recovery distinction

Three formally distinct categories: internally recoverable (reattach from detached states), externally repairable (restructure from hysteretic, new regime with less capacity), and locked in (hysteretic without external intervention).

### Meta-result

The common error pattern: informal prose was compressing static, dynamic, and restorative claims into single sentences. Formalization forced each claim to declare its type. The machine didn't make the theory more impressive. It made it more honest.
