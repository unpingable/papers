# Attack #02 — BoundaryTransit × feedback quarantine

**Filed:** 2026-06-05. **Status:** vector-mining pilot output. **Vector ID:** attack-02. **Confidence:** high.

## Question

> Can the corpus's existing freshness / type-fidelity / non-amplification atoms already prevent feedback-loop self-validation, or does the system need an explicit `BoundaryIntegrity` / provenance-preservation primitive as the relay proposed?

## Sources audited

- `working/loop-capture.md` (2026-05-09 origin, 2026-05-10 filed): adversarial-mechanism paper candidate. Five capture surfaces (sensor / estimator / objective / admissibility / reporting). **Witness Necessity Claim** explicit. Lean strategy already sketched.
- `working/causality-control-plane.md` (2026-03-17): admissibility = temporal standing of a signal within a decision architecture. Three failure classes (latency / observability / ordering) + CBPI + admissibility regime + capture.
- `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md`: substrate-side companion to BoundaryTransit. Seven-row refusal invariant table — row 6 is post-hoc laundering with `antiRetroactive` as substrate neighbor.
- `LeanProofs/Admissibility/StaleEvidenceMerge.lean` (UNRATIFIED-CANDIDATE): operationalizes freshness atom. `no_safeStep_from_stale_merged` is the action-time-freshness-does-not-survive-composition theorem.
- `LeanProofs/Admissibility/BoundaryWitness.lean` (SCRATCH/EXPOSITORY): forgetful-map / no-section schema; Axis 1 + Axis 2 boundary-witness obstructions. (Adjacent but different — about whether bridging happened, not about feedback loops.)
- `working/bridge-obligation-lattice.md`: five obligation atoms; static vs dynamic kernel split.

## What the relay claimed (Slice 4 of the multi-agent dump)

```text
DownstreamOf : Evidence → Effect → Prop
IndependentCustody : Evidence → Effect → Prop
NoSelfValidatingLoop : downstream evidence without independent custody
                       cannot discharge the effect that produced it
+ BoundaryIntegrity (provenance preservation) as enabling precondition
```

## Three-altitude verdict

The relay's claim is **DUPLICATE at three altitudes**, with the corpus's choice to leave each altitude's piece *separately named* being the federation doctrine working as intended, not a gap.

### Altitude 1: Lean substrate

| Relay piece | Corpus location | Verdict |
|---|---|---|
| `DownstreamOf` (causal lineage) | `StaleEvidenceMerge.lean` operates on action-time-fresh evidence at reconciliation time; the temporal-lineage shape is precisely what `evidenceFresh` on the merged state computes | DUPLICATE on shape |
| `IndependentCustody` | Already implicit in `SafeStep` carrying `bridged` — a `Prop` field carrying the freshness + value-preservation pair. `no_safeStep_from_stale_merged` shows that downstream `SafeStep`s cannot be reconstructed from upstream stale evidence | DUPLICATE |
| `NoSelfValidatingLoop` Lean theorem | `no_safeStep_from_stale_merged : ¬ Nonempty (SafeStep timedEnv merged)` — *the action-time-freshness atom already provides the loop-breaking refusal* | DUPLICATE |
| `BoundaryIntegrity` / provenance preservation | BoundaryTransit's `antiRetroactive` field (per witness-carrier-model § 6 row 6 cross-reference) | DUPLICATE |

### Altitude 2: Substrate discipline doctrine

The witness carrier model § 6 (refusal invariant table) names seven refusal cases. The relay's NoSelfValidatingLoop + BoundaryIntegrity bundle maps to rows 4 + 5 + 6:

| Carrier-model row | Required invariant | Maps to relay claim |
|---|---|---|
| Row 4: **stale** | `now ∈ valid_window` checked against verifier clock | freshness atom; loop quarantine via time |
| Row 5: **widened-after-issue** | child caveats only narrow parent's authority | non-amplification atom; loop quarantine via authority |
| Row 6: **post-hoc laundering** | `issued_at` cannot follow a transition that itself required prior authority; *the witness post-dates what it claims to have authorized* | exact substrate-level statement of NoSelfValidatingLoop + BoundaryIntegrity |

The corpus's substrate doctrine already names what the relay called BoundaryIntegrity, with `antiRetroactive` as the substrate neighbor. **One-day priority for the corpus, 2026-06-06 vs the relay's 2026-06-05.**

### Altitude 3: Paper-candidate synthesis

`working/loop-capture.md` is the corpus's adversarial-mechanism paper candidate. The exact relay claim maps to:

| Loop-capture element | Relay element | Verdict |
|---|---|---|
| Sensor / estimator / objective / admissibility / reporting capture | The relay's "feedback quarantine" target | DUPLICATE; loop capture has the five-surface decomposition the relay collapsed to a single rule |
| **Witness Necessity Claim**: "A loop whose detectors consume only captured reports cannot reliably detect capture. Detection requires at least one channel not co-captured by the same transformation." | Relay's "evidence downstream of effect cannot discharge that effect without independent custody" | DUPLICATE; mirror polarity (quarantine vs witness necessity); same content |
| "A witness need not be pure. It must fail differently." | Relay's "IndependentCustody" | ALIAS-RISK; corpus phrasing is sharper |
| Anti-Boyd theorem candidate: "A fast OODA loop around false state is just high-frequency self-harm." | Relay has no analog | Corpus is strictly stronger |
| Connection to P25 Theorem 1 (observation-equivalent states force policy-equivalence) | Relay has no analog | Corpus is connected to existing series |
| Connection to WIF-composition's audited failure-surface orthogonality | Relay has no analog | Corpus is connected to existing witness-discipline doctrine |

The paper-altitude synthesis is **already filed and named** as Loop Capture. The relay's `NoSelfValidatingLoop` is the corpus's Witness Necessity Claim with the polarity flipped (quarantine = inverse-image of detection) and the surface decomposition collapsed.

## The federation-doctrine angle

Apply the BRIDGE-CANDIDATE gate per [[project-no-unifier-without-laundering]]:

- The corpus has THREE separate atoms (freshness / non-amplification / type-fidelity) that together compose the loop-quarantine effect.
- The relay proposes a single NoSelfValidatingLoop + BoundaryIntegrity bundle that absorbs all three.
- This is *exactly* Outcome 2 (laundering) again: erasing three refusal surfaces into a single judgment form.

**The corpus chose this on purpose.** The federation doctrine says: keep the atoms separate; name the cross-atom failure mode in the adversarial vocabulary (loop capture); operationalize substrate-level discipline in the witness carrier model. The composition gap *is* the federation doctrine — it's not a gap, it's the architecture.

Gate verdict: relay's BoundaryIntegrity → BRIDGE-CANDIDATE → reclassified to LAUNDERING. Same gate as attack-05, fired again, same disposition.

## Cross-reference gap (the only genuine micro-finding)

`working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` cross-references the bridge-obligation-lattice, admissibility-related-work-map, and the Lean BoundaryTransit file. It does **not** cross-reference `working/loop-capture.md`.

`working/loop-capture.md` cross-references P22 / P25 / P27 / admissibility family / WIF-composition / the Lean kernel files. It does **not** cross-reference the witness-carrier-model candidate.

Both files address the same shape — independent witness / non-co-captured channel / antiRetroactive carrier — at different altitudes (paper-candidate vs substrate-candidate). The cross-link absence is a corpus housekeeping miss, not a missing theorem. **Recommended action: one-line cross-ref each direction, NOT a new file, NOT a bridge theorem.** Auditable, ~5 min, no new structure.

## Verdict summary

- **DUPLICATE** at three altitudes (Lean substrate / substrate-discipline doctrine / paper-candidate synthesis).
- **ALIAS-RISK** on vocabulary (quarantine ↔ witness necessity; IndependentCustody ↔ "fail differently"; BoundaryIntegrity ↔ antiRetroactive + post-hoc laundering refusal).
- **LAUNDERING** if promoted as single primitive across three atoms (federation doctrine).
- **NOT a MISSING-PRECONDITION**: the three atoms compose via the federation's chosen architecture (separate atoms + loop-capture adversarial dual + witness-carrier substrate discipline).
- **NOT a BRIDGE-CANDIDATE**: the gate fires; the paper-altitude synthesis is already filed.
- **Cross-reference micro-gap** between loop-capture and witness-carrier-model worth ~5 min closing as housekeeping.

## Survivors

**Survivor 1: the cross-reference patch.** Add bidirectional link between `working/loop-capture.md` § Witness/defense concepts and `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` § 6 row 6. Concrete, mechanical, no doctrine change.

**Survivor 2: a question for future loop-capture Lean staging.** When loop-capture earns a Lean spike, the Witness Necessity Theorem (lifted from P25 Theorem 1) is a candidate target. The relay's `IndependentCustody` framing could inform the *predicate name*, not the *theorem content*. Carry as a vocabulary candidate for that future spike — NOT authorized to build now.

## Recommended next action

- **Do not** mint `BoundaryIntegrity` as a new obligation atom. Use `antiRetroactive` + the three existing atoms.
- **Do not** mint `NoSelfValidatingLoop.lean` as a SCRATCH file. The Lean substrate (StaleEvidenceMerge) already operationalizes the freshness-side; the paper-altitude synthesis (loop capture) is the doctrine home.
- **Do** consider the bidirectional cross-reference patch between loop-capture.md and witness-carrier-model-candidate-2026-06-06.md — Survivor 1 above.
- **Do** carry IndependentCustody as a vocabulary candidate for a future loop-capture Lean spike. **Not authorized to build until loop-capture earns Lean staging via its own forcing case.**

## Method validation (cumulative, 2-pilot)

The vector-mining method continues to behave correctly:

- **Attack-05** (relay's effect-partial-order vs bridge-obligation-set): DUPLICATE + ALIAS-RISK + LAUNDERING. Gate fired.
- **Attack-02** (relay's feedback quarantine vs corpus's atoms): DUPLICATE at three altitudes + LAUNDERING (single-bundle absorption of three atoms). Gate fired. One genuine cross-reference micro-gap surfaced as housekeeping.

**Pattern:** the relay's contribution at each altitude is a re-derivation of corpus material under fresh vocabulary, with the relay-shape attack on multiple altitudes simultaneously masking individual altitude duplication. Single-altitude review (just Lean, or just doctrine, or just paper) might have missed the multi-altitude pattern; vector mining catches it because the corpus index is multi-altitude by design.

**Refinement for next pilot:** the multi-altitude check is now a method primitive — always check all three altitudes (substrate Lean / substrate doctrine / paper candidate) before classifying. Attack-02 demonstrates that a relay claim can be DUPLICATE at one altitude while looking novel at another; only the cross-altitude scan catches the full pattern.

**Common-mode immunity continues to hold.** The relay was Claude-web-shaped; the corpus check rejected it independently across three altitudes simultaneously.

## Cross-references

- `working/loop-capture.md` — the corpus paper-candidate that does what the relay claims to discover.
- `working/causality-control-plane.md` — admissibility as temporal-standing doctrine.
- `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` § 6 row 6 — substrate-level post-hoc-laundering refusal.
- `LeanProofs/Admissibility/StaleEvidenceMerge.lean` — freshness atom operationalized.
- `working/bridge-obligation-lattice.md` — the five-atom obligation grid.
- [[project-no-unifier-without-laundering]] — the federation doctrine the relay would violate.
- [[project-witness-carrier-model]] — substrate-side BoundaryTransit memory.
- [[feedback-claude-common-mode-synthesis]] — the methodology check that continues to validate.
- `working/vector-mining/2026-06-05-attack-05-effect-vs-obligation.md` — previous pilot.

## Provenance

Pilot run 2026-06-05 of the corpus-archaeology vector-mining method. Attack #2 selected per attack-05 follow-up recommendation as second test of method polarity (narrower scope, possibly a real gap). Result: no gap at the substrate, doctrine, or paper-candidate altitudes; one cross-reference micro-gap surfaces as legitimate housekeeping. Method validated for cross-altitude scanning; pattern of multi-altitude DUPLICATE in a single relay claim now recognized as a recurring relay-shape.
