# Compartmentalization: the distinguishability axis (doctrine stub)

*Status: UNRATIFIED-CANDIDATE doctrine stub, 2026-07-10. Named early. Not a paper,
not a kernel directory, not a rename of anything.*

*Provenance: operator realization 2026-07-10 (ops need-to-know siloing / HAL failure
modes / NQ+hauntd), ChatGPT synthesis plus two correction passes, Claude kernel-overlap
audit. Forcing consumer: hauntd→NQ (hauntd in skunkworks, likely graduates once
generalized — the disclosure contract is plausibly the generalization interface).*

## The axis

The existing admissibility family governs the **authority axis**: which transitions
may occur (reachability). Compartmentalization governs the **distinguishability
axis**: which worlds an actor can tell apart.

For principal *p*, a view `view_p : World → Obs_p` induces indistinguishability:

    w₁ ∼_p w₂  ↔  view_p(w₁) = view_p(w₂)

**Doctrine sentence:** *Authority governs which traces are permitted;
compartmentalization governs which worlds remain indistinguishable along those
traces.*

Existing kernels remain load-bearing because changing a view is itself a governed
transition. What they do not supply is the **view semantics**: what distinctions a
disclosure makes available to the recipient, especially after local inference and
composition with other observations. That is a different semantic object, not fresh
vocabulary for an old one.

## Two dual obstructions — one variable, two failure directions

    view too fine    → protected distinctions become visible   (mosaic leakage)
    view too coarse  → assigned duty cannot be performed safely (HAL conflict)

**Mosaic leakage.** Composing views intersects indistinguishability classes:
`∼_{A⊕B} = ∼_A ∩ ∼_B`. Individually — even pairwise — non-revealing releases can
jointly determine a protected fact. Every bridge can pass while the composed view
reveals too much; there is no pipeline event for a per-crossing gate to sit on,
because the join happens at the recipient's inference surface.
→ `Scratch/MosaicRelease.lean`.

**HAL conflict.** If one view-equivalence class contains worlds requiring
incompatible safe actions, no total local policy is safe in both; the architecture
has demanded clairvoyance and will label the failure disobedience. Typed non-action
(`hold` / `escalate`) preserves *justification*, not *mission success* —
SafeRefusal ≠ MissionSuccess. The liveness obligation this creates: an admissible
escalation/disclosure path must exist before the deadline, or compartmentalization
has made the assigned duty unrealizable.
→ `Scratch/CompartmentConflict.lean`.

The design problem between the two failure directions is **bounded sufficient
projection**: reveal enough distinctions to make the duty realizable, but none the
compartment exists to protect.

## Bounded sufficient projection (candidate sixth bridge-obligation atom)

Two conditions, conjoined:

- `OperationallySufficient(v, T)` — some policy over view `v` performs task `T`
  safely: `∃ π, ∀ w, Safe_T(w, π(v(w)))`.
- `WithinDisclosureBound(v, B)` — `v` reveals no distinctions outside the approved
  budget `B`.

Minimization (`¬∃ v' ≺ v` still sufficient and permitted) is **optional and later**
— least elements are notoriously inconsiderate about existing; two incomparable
sufficient projections are normal. Do not smuggle minimality into the atom.

**Independence test** against the five atoms in
`working/bridge-obligation-lattice.md`: construct two bridge witnesses that satisfy
all five existing obligations and support the same bounded effect, where one
additionally discloses an irrelevant protected bit. If only the disclosure bound
separates them, the sixth atom is independent rather than non-amplification in a
fake moustache. Gate at NoSilentConversion before admitting.

## Kernel-overlap audit (2026-07-10, corrected wording)

Held — reuse, do not re-mint:

- **Explicit disclosure transport** reuses NoFreeLift. *Epistemic amplification
  through inference and composition remains unmodeled* — that remainder is this
  axis, not a NoFreeLift face.
- MayMaintain⊬MayRead, MayObserve⊬MayRender — readout-arc faces
  (`NoFreeStandingReadout`, readout-is-a-governed-act).
- **Pairwise bridge *authority* is intransitive** (native to paid pairwise bridges).
  *Information-flow noninterference across those bridges is NOT thereby
  established* — open and unclaimed; B's permitted outputs may encode facts learned
  from A without any authorized B→C bridge.
- RevokedRead⊬Forgotten — contraction-asymmetry **prior** (information is Cartesian,
  authority is linear). Conceptual prior only; the information-persistence instance
  (copied / correlated / compressed / already-used-to-update-state) is not yet
  formalized.
- Typed non-action — refusals-need-receipts (mandamus) + existing
  `DeadlockEscalation.lean`, `AuthenticatedDenial.lean`.
- Break-glass — Leased Coercion composite (leased/logged/split/sunset) +
  relaxation-valve. Knowledge irreversibility applies: access control closes the
  door; it cannot make the visitor unsee the room.
- Purpose limitation (Visible⊬UsableFor) — continuous-admissibility-discharge
  (FCRA permissible-purpose prior art).
- hauntd emits typed claims, not metrics — witness-families doctrine + admission
  gate; Need⊬MayDisclose is standing-as-readout register (need is evidence for a
  disclosure request, not disclosure authority).

Genuinely new: **one view-semantics axis, exposed by two dual obstruction
specimens, plus one candidate bridge obligation governing sufficient disclosure.**

## Four gates, kept separate

1. **Scope gate.** No universal compartment lattice; no ten-`May*`-relation build
   (that list is a register — file-now-work-never); no "composition authority" as a
   sovereign kernel; no noninterference claims. The dashboard composition manifest
   is an ordinary governed transition whose *epistemic effect* must be evaluated
   set-level — pairwise checks are provably insufficient (three-bit XOR specimen).
2. **Formalization timing gate.** The bounded countermodels are built NOW, before
   the interfaces settle. Scratch status is how we formalize early without
   prematurely canonizing — it is not a reason to delay construction.
3. **Implementation gate.** No hauntd→NQ ingress until a written (preferably typed)
   disclosure contract exists: the task NQ must perform; the distinctions NQ must
   receive; the distinctions that must remain hidden; freshness/expiry; provenance;
   permitted correlation; typed refusal; what the witness cannot testify to. The
   contract constrains the code, not describes it afterward. Prometheus stays ops
   telemetry about hauntd itself — never the evidentiary bridge.
4. **Promotion gate.** Everything stays fenced scratch until the countermodels
   survive review, the hauntd contract forces the abstractions, and names
   stabilize.

**Timing doctrine (the corrected inversion):** *Overlap audits constrain novelty
and scope, not timing. Once a bounded forcing question exists, scratch
formalization precedes consumer implementation; promotion may wait, specification
should not.* Bluntly: "do not mint a new calculus" does not mean "let the code mint
it implicitly."

## Ladder / status

1. This stub — filed 2026-07-10.
2. `Scratch/MosaicRelease.lean` — individual and pairwise non-revelation not closed
   under composition; intersection lemma.
3. `Scratch/CompartmentConflict.lean` — no safe total local policy under a hidden
   discriminator; hold/escalate justified but non-completing; narrow-disclosure
   restoration model (seed of the sufficient-projection specimen).
4. SufficientProjection independence specimen — after 2–3 settle vocabulary.
5. `HAUNTD_NQ_WITNESS_CONTRACT` — before adapter implementation; NQ/AG lane, not
   papers lane.
6. Runtime implementation — code realizes the already-declared boundary.

`BlindMaintenance` remains a composed demo built from these pieces, not a third
foundational theorem.

## Scope fence

All results are relative to a declared secret and observation language. No
probabilistic leakage, no timing channels, no human priors, no claim that every
composition leaks — only that non-revelation is not closed under composition, and
that totality-under-assigned-ignorance is refusable. No governance composition with
the literal-Gentzen ProofTheory island.
