# Lean Formalization Summary

Draft paragraph for paper/book integration. Source: machine-checked proofs in `~/git/lean/LeanProofs/`.

---

## Paper-facing paragraph

The cybernetic failure taxonomy was formalized in Lean 4 as a directed graph with 15 domains and 21 pipeline edges. Three results corrected the informal theory.

First, the static pipeline graph has three terminal families — {Δg, Δa} (gain/actuation), {Δx} (scale inversion), and {Δh} (hysteresis) — not one universal sink. Signal corruption and coupling mismatch dead-end without reaching Δh. Any claim that all failures eventually reach hysteresis must be stated as a temporal hypothesis about persistence dynamics, not as a graph-topological fact.

Second, for the five branching precursors that can reach both gain/actuation and hysteresis terminals (Δn, Δo, Δb, Δp, Δr), closure family is selected by the interaction of precursor burn profile and pre-existing budget asymmetry, not by precursor type alone. A system with weakened authority-consequence coupling is susceptible to hysteresis regardless of what kind of failure hits it. Conversely, a system with degraded model quality is susceptible to gain/actuation closure even under governance-heavy failures.

Third, hysteresis is driven by cumulative rollback depletion under detached commits, not by contiguous duration of detachment. Repeated short detachment episodes, each individually recoverable, can accumulate into irrecoverability — episode recoverability does not imply lifetime recoverability. Once internal return is unavailable, external restructuring can restore operability but not original baseline resilience: the repaired system is operable in a new regime with reduced rollback margin, and can fail again, typically faster.

The common error pattern across all three corrections: the informal prose was compressing static, dynamic, and restorative claims into single sentences. The formalization forced each claim to declare its type and then proved or falsified it on those terms.

---

## Key sentences for inline use

**On terminal families:**
Static topology yields multiple terminal families; any universalization of Δh must be stated as a temporal hypothesis, not a graph fact.

**On closure selection:**
For branching precursors, closure family is selected by the interaction of burn profile and pre-existing budget asymmetry, not by precursor type alone.

**On persistence:**
Reset failure is driven by cumulative rollback depletion under detached commits; prolonged contiguous detachment is sufficient but not necessary.

**On recovery:**
A system can be internally irrecoverable yet externally repairable, and external repair restores operability without restoring baseline resilience.

**On the meta-pattern:**
Formalization did not confirm the informal theory. It forced the informal theory to stop compressing distinct claim types into single sentences.
