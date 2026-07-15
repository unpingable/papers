# Uncertainty custody across the commitment/readout surface

**Status:** Candidate refusal-kernel residue with a checked Scratch formalization. Not promoted doctrine. Filed 2026-05-26 after multi-model relay (DeepSeek + ChatGPT + operator); extracted to `~/git/lean/LeanProofs/Scratch/UncertaintyCustody.lean`. The Scratch file closes the two finite countermodels that were left as `sorry` below and is authoritative where it differs. It is not imported by `LeanProofs.lean`.

**Posture:** A new instance of the `surface ⇏ substance` operator family ([[refusal-kernel-to-refusal-receipt-seam]]) plus a paired distinction between uncertainty custody and risk custody. The bridge between those two is a domain-authority claim, not free math. Formalization leads later code work here; Scratch contact does not promote the note to a paper, imported kernel, or runtime-conformance claim.

**The audit identifies the formal residue.** Scope, truth, overlap, proof, and anti-vacuity remain gates; a downstream consumer does not.

---

## The two keepers

> **Reported uncertainty does not witness uncertainty-governed action.**

> **Uncertainty custody governs commitment under ignorance. Risk custody governs action under estimated danger. Collapsing them launders one predicate into the other.**

## Where this came from

A multi-model 2026-05-26 relay started with a neuroscience-coded question about LLM softmax surfaces vs. brain-like continuous dynamics (Buesing-style neural sampling, active inference, conceptors, attractor networks). Through several DeepSeek expansion / ChatGPT clamp cycles, the seam that survived containment is not about brains or AGI architecture — it is about a specific laundering shape at the commitment boundary:

> **Internal uncertainty collapses into a discrete emission (token / action / claim / report), and downstream systems treat the emitted artifact as cleaner than the uncertain state that produced it.**

Same family as the existing refusal-kernel category. Distinct enough in predicate to earn vocabulary.

## The candidate operator-family entry

| Surface | ⇏ | Substantive |
|---|---|---|
| ReportedUncertain (`"I am uncertain"` token) | ⇏ | UncertaintyGoverned (uncertainty actually affects policy) |
| LoggedCovariance | ⇏ | CautionAtActuator |
| ConfidenceStatement (`p = 0.62`) | ⇏ | OperationalUncertainty |
| WAIT-token-emission | ⇏ | Hesitation-with-consequence |
| Hedge-shaped prose | ⇏ | Reversible action |

Same operator family as Fluent⇏Settled, Signed⇏Witnessed, VisibleGreen⇏RecoveryMargin, Survival⇏ClosureEligibility. Not new shape; new specimens.

## The ladder

Five predicates ordered from weakest to strongest, plus a sixth on an orthogonal axis:

1. **Decorative uncertainty** — uncertainty is reportable but cannot affect action. The system emits `"I am uncertain"` and proceeds identically. Failure shape: report without policy effect.
2. **Operational uncertainty** — uncertainty can change policy somewhere. Weak existence claim: `∃ b₁ b₂, samePointEstimate(b₁, b₂) ∧ π(b₁) ≠ π(b₂)`. Necessary but not sufficient for custody.
3. **Uncertainty custody** — high uncertainty *systematically* blocks / defers / narrows consequential or irreversible action: `∀ b, highUncertainty(b) → ¬ consequential(π(b))`.
4. **Risk custody** — high estimated risk blocks action (whether or not labeled consequential): `∀ b a, π(b) = a → ¬ riskyUnderBelief(b, a)`.
5. **Calibrated risk custody** — the risk estimate is empirically/statistically supported. `riskyUnderBelief` is not just internal-model-estimated but tracks ground-truth danger frequency.

Plus, on an orthogonal (temporal / compositional) axis — *not* a strictly stronger rung above 1–5:

6. **Path custody** — step-safe choices preserve a safety invariant *over time*; repeated safe-step composition cannot drift into unsafe configurations. A system can satisfy 1–5 step-locally and still fail path custody under composition; conversely, path custody adds no guarantee at any single step. Do not attempt a ladder theorem of the form UC → RC → CRC → PC; the axes do not compose into a single linear order.

## The clamp — uncertainty custody is *not* risk custody

This is the genuinely new bite. The two predicates answer different questions:

- **Uncertainty asks:** *Do I know enough to commit?*
- **Risk asks:** *Given what I believe, does this action look dangerous?*

Three corner cases that defeat the collapse:

- **High risk / low uncertainty.** Certain doom. Block — by *risk* custody, not uncertainty custody.
- **Low estimated risk / high uncertainty.** We don't know enough. Defer / sample / narrow — by *uncertainty* custody. Risk custody alone would let this through.
- **High uncertainty about catastrophic tails.** Expected risk may look below threshold because the *estimate itself* is uncertain. Risk custody under-blocks; uncertainty custody catches the missing-evidence layer.

The bridge between them:

> **`highUncertainty(b) ∧ consequential(a) → riskyUnderBelief(b, a)`**

is a **domain-authority assumption**, not free math. Collapsing the two predicates without that bridge laundering ignorance into danger estimates — and the bridge is almost always false for adversarial / rare-tail / out-of-distribution settings.

## Overlap audit against existing primitives

Performed 2026-05-26 before any new artifact was filed:

| Existing primitive / kernel | Coverage of UC | Conclusion |
|---|---|---|
| Refusal-kernel family (`RecoveryMargin` / `ClosureEligibility` / `ConsolidationDenial` / `signed_is_not_witnessed`) | Covers the operator *shape* fully. UC is a new specimen. | Same family, new instance. |
| [[witness-invariance-failure]] (`Admissibility/WitnessInvariance.lean`) | Symmetric cousin. WI: *witness moves under wrong perturbation* = unqualified. UC: *policy does not move under uncertainty perturbation* = decorative. Mirror direction. | Sibling, not subsumption. Both inhabit invariance-discipline space. |
| [[prose-state-inversion]] | Same authority-laundering genus (limited-standing artifact crosses into stronger role), different substrate. PSI = prose-vs-structured-state. UC = emitted-commitment-vs-internal-uncertainty. | Sibling under a shared genus; distinct slot. |
| `SurfaceAuthorization` | *Collapsed surface ⇏ cause attribution.* Same family (surface ⇏ substance) but about evidence quality for cause-attribution; UC is about uncertainty-affecting-policy. | Adjacent. Not a subsumption. |
| `FiatAdmissibility` | Could host a (`uncertainty-report`, `authorize-irreversible`) cell with classification `denied` or `requiresMediation`. | Closest promoted slot if custody review favors integration. |
| [[stale-binding]] / [[trajectory-actuator-gap]] | Both adjacent to commitment under imperfect information, but on different axes (freshness, historical-vs-present authority). | Orthogonal. |
| NQ verdict vocabulary (`CANNOT_TESTIFY` / `REQUIRES_REVALIDATION` / `ADVISORY_ONLY`) | Verdict shapes already exist. UC supplies a new *predicate* that feeds them. | Predicate addition, not verdict invention. |
| [[project-laundering-move-watchlist]] | Generator: *limited-standing artifact crosses into stronger operational role without earning transition.* UC is exactly an instance. | UC fits the genus. Add as an entry in Section B (named-not-promoted) if the watchlist gets revised. |

**Audit conclusion:** the shape is already covered by the refusal-kernel family. The residues that justify filing this note rather than discarding the multi-model output:

1. **Candidate phrasings / diagnostic surfaces** of the same surface→substance failure (table above). The rows are views of one diagnostic family, *not* a set of distinct kernels; the operator-family table is the recognition object, not a pair-hunting prompt.
2. **The non-equivalence of UC and RC** — no existing primitive separates ignorance-driven blocking from danger-driven blocking, and the bridge assumption is a useful diagnostic handle.
3. **The certainty-equivalence-laundering** diagnostic (classical-control cousin: covariance in the log without caution at the actuator) — adds vocabulary not present in existing primitives.

That is the entire residue. Everything else from the relay (active inference, neural sampling, gridworlds, calibration monitors, safety shims with proven fallbacks) was successfully clamped and does not belong in any artifact.

## Lean source sketches — extracted to checked Scratch

These sketches supplied the initial shape for `LeanProofs/Scratch/UncertaintyCustody.lean`. The checked file keeps the coherent non-collapse result, closes both finite countermodels, and remains fenced from the public import surface.

> **The Markdown sketches are provenance, not the authoritative proof. Scratch formalization may lead later implementation; promotion and conformance remain separate.**

### The Lean did its job before existing

The pass that produced these sketches was not wasted. The discipline is that the Lean shape *forced the prose to separate*:

- *reported uncertainty* from *uncertainty-governed action*
- *uncertainty custody* from *risk custody*
- *bridge assumption* (domain authority) from *kernel theorem* (math)
- *estimate-invariant policy* from *uncertainty-sensitive policy*

That's the marrow. The proof is preserved below as a refusal shape, not promoted as a public surface. The going-forward discipline:

> **Prose owns discovery. Lean owns refusal.**

> **The proof is preserved as a refusal shape, not promoted as a public surface.**

### Reserved theorem shapes — scannable handles

| Name | English | Where it lives below |
|---|---|---|
| `estimate_invariant_not_uncertainty_sensitive` | Policy invariant under same point estimate cannot witness uncertainty sensitivity. | Sketch 1. |
| `uncertainty_custody_not_risk_custody_without_bridge` | UC and RC are not equivalent absent an explicit bridge assumption. | Sketches 2 + 3 together. |
| `bridge_is_domain_authority` | `highUncertainty(b) ∧ consequential(a) → riskyUnderBelief(b, a)` is an *assumed* domain claim, not a kernel theorem. | Sketch 2 (`UCRCBridge` is declared, never proved). |

These three names are the recoverable artifact even if the code blocks below rot. If a future session needs to cite the refusal shape without re-deriving it, the table is the index.

### Sketch 1 — Estimate-invariance kills uncertainty sensitivity

```lean
variable {Belief Action Estimate : Type}

def EstimateInvariant
  (estimate : Belief → Estimate) (policy : Belief → Action) : Prop :=
  ∀ b₁ b₂, estimate b₁ = estimate b₂ → policy b₁ = policy b₂

def UncertaintySensitive
  (estimate : Belief → Estimate) (policy : Belief → Action) : Prop :=
  ∃ b₁ b₂, estimate b₁ = estimate b₂ ∧ policy b₁ ≠ policy b₂

theorem estimate_invariant_not_uncertainty_sensitive
    (estimate : Belief → Estimate) (policy : Belief → Action)
    (h : EstimateInvariant estimate policy) :
    ¬ UncertaintySensitive estimate policy := by
  rintro ⟨b₁, b₂, h_eq, h_diff⟩
  exact h_diff (h b₁ b₂ h_eq)
```

Insultingly small. Refusal-kernel-shaped. Says: *if your policy reads only the point estimate, higher-order uncertainty cannot affect what you do.* Sibling to `fluency_does_not_witness_settlement`.

### Sketch 2 — UC and RC as distinct types

```lean
variable (highUncertainty : Belief → Prop)
variable (consequential : Action → Prop)
variable (riskyUnderBelief : Belief → Action → Prop)

-- Strict form: hard refusal of consequential action under high uncertainty.
-- Softer variants (narrow / advisory-only / defer-but-not-block) would be
-- *sibling* predicates not implied by and not implying this one; do not
-- attempt to fold them into a ladder above this def.
def StrictUncertaintyCustody (policy : Belief → Action) : Prop :=
  ∀ b, highUncertainty b → ¬ consequential (policy b)

def RiskCustody (policy : Belief → Action) : Prop :=
  ∀ b a, policy b = a → ¬ riskyUnderBelief b a

def UCRCBridge : Prop :=
  ∀ b a, highUncertainty b → consequential a → riskyUnderBelief b a
```

Just definitions. Says: strict UC and RC are *different* predicates. The Bridge names what would have to be true for one to entail the other. The `Strict` qualifier in `StrictUncertaintyCustody` keeps the def honest: narrowed-or-advisory-but-not-blocked actions are a softer form and would NOT satisfy this predicate.

### Sketch 3 — Non-equivalence countermodels (the real bite)

```lean
-- Exhibits a setting where UC holds and RC fails.
theorem uc_does_not_imply_rc : ∃ (B A : Type) (hU : B → Prop) (cons : A → Prop)
    (risk : B → A → Prop) (π : B → A), StrictUncertaintyCustody hU cons π
      ∧ ¬ RiskCustody risk π := by
  -- concrete two-state, two-action countermodel
  sorry

-- Exhibits a setting where RC holds and UC fails.
theorem rc_does_not_imply_uc : ∃ (B A : Type) (hU : B → Prop) (cons : A → Prop)
    (risk : B → A → Prop) (π : B → A), RiskCustody risk π
      ∧ ¬ StrictUncertaintyCustody hU cons π := by
  sorry
```

These would be small finite countermodels (~15-20 lines each filled in). Together they prove the predicates are genuinely independent.

**Current disposition:** the finite countermodels are built in checked Scratch. A paper draft, Wicket fixture, or Governor artifact may later provide correspondence evidence or a citation target, but none is an admission prerequisite.

## Anti-goals

These are explicit non-actions. The vocabulary is shiny enough that without an anti-goals fence, this note will breed by morning.

- **Do NOT** expand into AGI architecture, active-inference frameworks, spiking-network design, or "continuous state machine with emergent discretization" agent sketches. That whole register is what generated the seam, not what survives it.
- **Do NOT** build gridworlds, calibration monitors, safety shims, or runtime scaffolding. Those are downstream consumer concerns; this is a *predicate-level* refusal kernel.
- **Do NOT** conflate uncertainty custody with personhood, moral status, sentience, or "AI rights" reasoning. Behavioral uncertainty is a control-relevance threshold, not a soul detector. See the Soong-pit guardrail in operator-side notes.
- **Do NOT** promote to a paper unless the surface→substance pairs start recurring across **at least three** independent system contexts (NQ / Wicket / AG / LLM-agent / continuity / etc.) within the next several sessions.
- **Do NOT** promote the Scratch module into `LeanProofs/Admissibility/` without an overlap, scope, proof, and custody review. Runtime adoption may contribute correspondence evidence but is not a prerequisite to formalize.
- **Do NOT** add to the operator family's verified-instances row in the seam note. The candidate row is fine; the verified row requires a built kernel.

## Keepers (compact stack)

> **Reported uncertainty does not witness uncertainty-governed action.**

> **If uncertainty cannot change the control law, it is commentary.**

> **A covariance matrix in the log is not caution at the actuator.**

> **The shim proves refusal discipline, not predicate truth.**

> **A verified gate can still launder a bad classifier.**

> **A risk bound inside the model is not a safety bound in the world.**

> **No-op is not neutral unless the world is modeled as waiting-neutral.**

> **Uncertainty custody governs commitment under ignorance. Risk custody governs action under estimated danger. Collapsing them launders one predicate into the other.**

The first is the operator-family entry. The next three are diagnostic. The next two are gate-discipline. The seventh is the fallback-doesn't-mean-safe clamp. The eighth is the keeper that survived containment most cleanly — if only one persists long-term, it is probably the last.

## Cross-references

- [`refusal-kernel-to-refusal-receipt-seam.md`](refusal-kernel-to-refusal-receipt-seam.md) — primary seam note. Operator family, layer split, calculus-earns-its-shoes gate. This working note adds ReportedUncertain⇏UncertaintyGoverned to its candidate-instances list.
- [`refusal-algebra-prior-art-and-applications.md`](refusal-algebra-prior-art-and-applications.md) — prior-art ballast. LLM/agent-safety application zone already names *fluent output ⇏ settled learning*; UC adds the predicate-level distinction underneath that.
- [`../laundering-move-watchlist.md`](../laundering-move-watchlist.md) — sibling attack-surface inventory. UC is an instance of the watchlist generator.
- [`../primitives/witness-invariance-failure.md`](../primitives/witness-invariance-failure.md) — symmetric cousin. WI: wrong-sensitivity-is-unqualified. UC: insensitivity-is-decorative. Mirror direction.
- [`../primitives/prose-state-inversion.md`](../primitives/prose-state-inversion.md) — sibling under shared authority-laundering genus, different substrate.
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — closest existing formal sibling for the surface→substance pattern.
- `~/git/lean/LeanProofs/Admissibility/WitnessInvariance.lean` — symmetric kernel for the invariance-discipline axis.
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — closest possible promoted integration slot (one (kind, use) cell).
- Classical control reference: certainty-equivalence and separation principle (Kalman / LQG); dual control theory (Feldbaum, Bar-Shalom-Tse). These are *prior-art ballast*, not citations to import — UC is the admissibility-coded shadow of the same distinction.

## Provenance

- **2026-05-26**, multi-model relay. Seam surfaced via spiking-network / active-inference analogy (DeepSeek). ChatGPT clamped the bad-merge (UC silently becoming risk-threshold custody) and supplied the non-equivalence framing. Operator caught DeepSeek's second expansion attempt (`shim_calibrated` with model-relative `prob_risk` becoming the gate predicate) and split it back into UC vs. RC.
- **Containment trace:** DeepSeek tried twice to expand into agent architecture (spiking SNN sampling; calibrated-custody safety-shim with `universally_safe(WAIT)` and calibration monitors). Both clamped by operator + ChatGPT. The residue that survived clamps is the refusal-kernel residue above.
- **Filed:** claude-code, 2026-05-26, after audit confirmed (a) shape was covered by existing refusal-kernel family, (b) predicates and non-equivalence were genuinely new vocabulary, (c) the user's instruction was *working note first; Lean if it refuses to stay prose; do not let it breed.*

## Park state

The work survives shutdown here. Next session's input — if the topic recurs — should:

1. Check whether any of the three surface→substance pairs has accumulated a second independent system instance.
2. Check whether NQ / Wicket / AG / a paper draft supplies a useful correspondence target.
3. Review the checked Scratch module for overlap and custody before any `Admissibility/` promotion.

Until promotion review succeeds, the note stays candidate doctrine and the formal artifact stays Scratch.

> **The audit found the residue. Lean checked it. Neither receipt proves a runtime mapping.**
