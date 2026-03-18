# Paper 22 — No Universal Plant Clock — Convergence Spike

**Full title:** No Universal Plant Clock: Temporal Failure Geometry in Distributed Control Systems
**Date:** March 2026
**DOI:** pending

## Status: spiked 2026-03-18

## Claim Cluster
- Distributed control systems inherit four false temporal assumptions: universal plant clock, interchangeable local clocks, direct access to remote current state, and instantaneous control — and each produces a distinct failure mode when violated
- Temporal failure decomposes into four operationally distinct layers: gauge mismatch, clock divergence, retarded-state estimation, and delayed actuation
- The dominant failure mode in a given system is determined by which timescale ratio (T_o/T_p, T_u/T_p, T_s/T_p, T_c/T_contract) exceeds its critical threshold first
- Many coordination failures are temporal failures wearing other labels (communication problems, decision-making problems, responsiveness problems)
- Temporal coherence is a scarce control resource that can be budgeted, allocated, and governed — not a property to be assumed

## Search Terms
- distributed control temporal failure mode classification
- clock synchronization distributed systems failure
- observation latency actuation delay control stability
- age of information distributed control freshness
- timescale ratio analysis control system design
- coordination failure temporal mismatch diagnosis
- retarded state estimation control theory
- temporal coherence resource allocation governance

## Expected Convergence Level
strong convergence likely
Networked control systems, Age of Information, clock synchronization, and delayed control are all mature research areas with extensive literature. The four-layer decomposition and ratio-based triage are likely novel as a unified diagnostic framework, but the individual layers correspond to well-studied problems.

## Hits

### STRONG CONVERGENCE (individual layers are well-studied)

**1. Fischer, Lynch, Paterson (1985). "Impossibility of Distributed Consensus with One Faulty Process." *JACM*.**
- Match type: **strong** (foundational)
- Claims supported: False assumptions #1 (universal plant clock) and #3 (direct access to remote current state)
- Summary: Establishes the impossibility of simultaneity in distributed systems. Does not decompose the resulting failure modes into a four-layer taxonomy.

**2. Deutsch/Joy/Gosling (1994/1997). "Eight Fallacies of Distributed Computing."**
- Match type: **strong** (cultural touchstone)
- Claims supported: False assumptions #3 and #4 ("latency is zero," "the network is reliable")
- Summary: Enumerates assumptions but provides no failure-mode decomposition or timescale ratio analysis.

**3. Lamport (1978). "Time, Clocks, and the Ordering of Events in a Distributed System." *CACM*.**
- Match type: **strong** (foundational)
- Claims supported: False assumptions #1 and #2 (local clocks not interchangeable with global clock)

**4. Hespanha, Naghshtabrizi, Xu (2007). "A Survey of Recent Results in Networked Control Systems." *Proc. IEEE*.**
- Match type: **strong**
- Claims supported: Layers 3 and 4; timescale ratio analysis via MATI
- Summary: NCS four-component model (plant, sensor, controller, actuator) with two delay channels maps closely to retarded-state estimation and delayed actuation. Very close on individual delay channels. Does NOT unify gauge mismatch or clock divergence into the same framework.

**5. Kokotovic et al. (1976-2014). Singular Perturbation and Timescale Separation.**
- Match type: **strong**
- Claims supported: Timescale ratio analysis (T_o/T_p etc.) as design tool
- Summary: Formal methods for decomposing systems with multiple timescales. Provides the mathematical machinery but focuses on model order reduction, not diagnosing coordination failures or treating temporal coherence as a governance resource.

**6. Yates, Sun, Kaul, Gruteser, Modiano (2021). "Age of Information: An Introduction and Survey." *IEEE JSAC*.**
- Match type: **strong**
- Claims supported: Layer 3; freshness as scarce resource; scheduling/budgeting of update timing
- Summary: AoI directly formalizes information staleness — the gap between current time and generation time of latest update. Very close on the observation-staleness layer. AoI treats freshness as a quantity to be scheduled and optimized, directly supporting the "temporal coherence as scarce resource" claim. Does not incorporate gauge mismatch, clock divergence, or actuation delay into a unified framework.

**7. Carnevale, Teel, Nesic (2007). "MATI for Networked Control Systems." *IEEE TAC*.**
- Match type: **strong**
- Claims supported: Timescale ratio threshold; dominant failure mode determination
- Summary: MATI bounds are exactly the paper's concept of a critical threshold on a timescale ratio (T_s/T_p). Very close on the specific mechanism, but MATI analysis is per-channel, not a unified four-layer decomposition.

**8. Xia, Hespanha et al. (2017). "Networked State Estimation With Delayed and Irregularly Spaced Time-Stamped Observations." *IEEE TAC*.**
- Match type: **strong**
- Claims supported: Layer 3 (retarded-state estimation with time-stamping as mitigation)

### MODERATE CONVERGENCE (related frameworks, different scope)

**9. Kopetz & Steiner (2024). "Temporal Consistency of Data and Information in Cyber-Physical Systems." arXiv:2409.19309.**
- Match type: **moderate-high**
- Claims supported: Layers 3 and 4; temporal consistency as design constraint
- Summary: Addresses temporal inconsistency from delays between sensor acquisition and actuation. Proposes time-triggered architecture as solution. Treats temporal consistency as a first-class design concern, paralleling "temporal coherence as governance resource." Focuses on architectural solutions (TTA) rather than diagnostic taxonomy or institutional extension.

**10. Bulusu et al. (2025). "SoK: Resilience and Fault Tolerance in Cyber-Physical Systems." arXiv:2512.20873.**
- Match type: **moderate-high**
- Claims supported: Failure mode taxonomy; timing as under-addressed failure axis
- Summary: Proposes Origin-Layer-Effect (OLE) taxonomy of CPS faults. Notes that timing perturbations are "systematically under-addressed." Explicitly flags timing perturbations as a gap in the literature — which is exactly what Paper 22 fills.

**11. Wilson et al. (2016). "A typology of time-scale mismatches and behavioral interventions." *Conservation Biology*.**
- Match type: **moderate**
- Claims supported: Coordination failures as temporal failures; timescale mismatch diagnosis
- Summary: 15 types of temporal mismatches across decision-maker, social system, and ecological system. Diagnostic framework for timescale mismatch. Supports the claim that temporal mismatch diagnosis generalizes across domains. Different domain (conservation/governance).

**12. Hocherman et al. (2025). "Time lags in environmental governance." *Ambio*.**
- Match type: **moderate**
- Claims supported: Temporal coherence as governance resource; coordination failures wearing temporal labels
- Summary: Temporal DPSIR framework synthesizing time lags across environmental governance. Cross-domain validation that temporal lag analysis is emerging as a governance tool.

**13. Ge et al. (2013). "Modeling of Random Delays in Networked Control Systems." *JCSE*.**
- Match type: **moderate**
- Claims supported: Different temporal failure modes require different analytical treatments

### WEAK CONVERGENCE (tangential or partial)

**14. Institutional Lag / Policy Implementation Lag literature** — supports institutional extension but lacks control-theoretic framing.

**15. RL for Control Systems with Time Delays (arXiv:2602.00399, 2026)** — action delays transform control into non-Markovian decision process.

**16. Cache Coherence / Distributed Shared Memory** — "coherence" as actively maintained property; weak analogy to temporal coherence as resource.

## Notes

**What the literature already covers well (NOT novel):**
- The impossibility of a universal clock (FLP, Lamport, Sheehy)
- Individual delay channels in NCS (Hespanha, MATI research)
- AoI as freshness metric and scheduling resource
- Timescale separation via singular perturbation
- Temporal mismatch typologies in governance/conservation (Wilson, Hocherman)
- Timing perturbations in CPS as under-addressed (Bulusu SoK)

**What appears NOVEL in Paper 22:**
1. The unified four-layer decomposition (gauge mismatch, clock divergence, retarded-state estimation, delayed actuation) as a single diagnostic framework — each layer is well-studied individually but no paper unifies all four
2. Timescale ratio triage — dominant failure mode determined by which ratio exceeds its threshold first; MATI provides one such ratio but multi-ratio triage across all four layers appears new
3. Temporal coherence as a scarce, budgetable governance resource — AoI treats freshness as optimizable, Kopetz treats temporal consistency as design constraint, but the explicit resource framing is distinctive
4. The diagnostic relabeling claim — coordination failures ARE temporal failures wearing other labels

**Strongest prior art to cite and distinguish from:**
- Hespanha (2007) for NCS delay channels
- AoI literature (Yates et al. 2021, Sun et al. 2017) for freshness-as-resource
- Kopetz & Steiner (2024) for temporal consistency in CPS
- Bulusu et al. (2025) for the gap Paper 22 fills
- Wilson et al. (2016) for cross-domain timescale mismatch typology
- Kokotovic for timescale ratio analysis foundations
- Lamport (1978), FLP (1985) for impossibility foundations

## Verdict

**Strong convergence on components; novel as a unified framework.** Every individual layer maps onto mature research literature. The paper's expected convergence assessment ("strong convergence likely") is confirmed. However, the four-layer decomposition as a unified diagnostic taxonomy, multi-ratio triage for identifying dominant failure modes, temporal coherence as governance resource, and the diagnostic relabeling claim together constitute a genuinely novel synthesis.

The Bulusu SoK (Dec 2025) explicitly identifies timing perturbations as a gap in CPS fault taxonomy — Paper 22 directly fills that gap.
