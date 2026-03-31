# Spike: Hysteresis / Return Failure (Δh)

**Status:** Spike — receipts, not architecture
**Domain:** Can't return to sane baseline after triggering condition is removed
**Compression:** Can't get back out once the failure normalizes
**Sequence:** Second spike (hardest, but yields a reusable discrimination criterion)

---

## The Failure

A system enters a state in response to a trigger. The trigger is removed. The system does not return. The question is whether that non-return is pathological or adaptive.

Not every "new normal" is a failure. Scar tissue that makes you stronger is learning. Emergency powers that never sunset are capture. The domain needs a discrimination criterion, not just examples.

---

## Candidate Discrimination Criterion

Four questions:

1. **Baseline**: What was the prior operating regime?
2. **Trigger removal**: Has the condition that caused the shift actually been removed?
3. **Legitimate transformed equilibrium**: Did the system learn something real — is the new state a better fit for the actual environment?
4. **Pathological non-return**: Is the system stuck in the emergency state because the emergency state has become self-reinforcing?

**Δh is pathological when the persistence mechanism is self-referential rather than environment-referential.** The system stays in the state because being in the state maintains the state — not because the environment still warrants it.

Emergency powers that justify themselves by the emergency they create. Scope absorption that generates the workload that justifies the absorption. Normalized exception that produces the conditions that make the exception feel normal.

Contrast: a company that restructured during a crisis and kept the new structure because it actually works better. That's adaptation, not Δh. The new state is maintained by environmental fit, not by self-reinforcing lock-in.

---

## Symptom Pattern

- "New normal" language when the triggering condition has passed
- Emergency measures that generate their own justification for continuance
- Inability to articulate what "return to baseline" would even look like
- The system's memory of the prior state has been overwritten by the current one
- Reversal attempts are treated as threats rather than corrections

---

## Where It Already Shows Up

### Papers
- **Paper 15** — mentions hysteresis as a property of cybernetic fault domains, but doesn't develop the standalone question
- **Paper 18** — unauthorized durability (Δw) is adjacent. Temporary exceptions gaining permanent governing power is a specific case of Δh where the non-return is in authority structure.
- **Paper 22** — retarded-state estimation means the controller is always working from stale data, which can prevent it from recognizing that the trigger has been removed

### Governor
- `hysteresis.py` — implements hysteresis as a stabilization mechanism (deliberate non-return to prevent oscillation). This is hysteresis-as-tool, not hysteresis-as-failure. The governor uses Δh therapeutically without modeling it as a failure mode.

### Substack / Public Writing
- Scope absorption that never reverses — the person/team/institution takes on emergency load, the emergency ends, the load stays
- "Your own job, frankly" — personal Δh as lived experience

---

## The Hard Distinction

**Hysteresis-as-stabilization** vs. **hysteresis-as-capture**:

| | Stabilization (healthy) | Capture (Δh failure) |
|---|---|---|
| Persistence driver | Environmental fit | Self-reinforcing lock-in |
| Reversal response | Open to review | Treats reversal as threat |
| Baseline memory | Retained, compared against | Overwritten or inaccessible |
| Justification | Points to external conditions | Points to own continuation |

The governor already uses healthy hysteresis (don't oscillate between regimes on noise). The failure mode is when the system can't distinguish between "we're staying here because it's correct" and "we're staying here because we're stuck."

---

## Relationship to Other Domains

- **Δw → Δh**: Unauthorized durability (Δw) is Δh in the authority layer specifically
- **Δh → Δn**: Sometimes the system can't return because it can't name the prior state anymore (vocabulary has shifted to normalize the current one)
- **Δh → Δb**: A boundary error can become permanent via Δh — the wrong perimeter normalizes and becomes "how we've always done it"

---

## What Would "Thickening" Look Like?

The discrimination criterion is the real deliverable. If it holds, it's reusable across every paper where hysteresis appears. Probably:
- A formal criterion in the book (when is non-return pathological?)
- An upgrade to the governor: distinguish stabilization-hysteresis from capture-hysteresis
- Possibly a short paper if the criterion is sharp enough to stand alone
