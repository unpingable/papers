# Trajectory canonicalization — substrate fix (2026-05-30)

**Status:** Decision record + acid-test evidence. Closes the trajectory-design divergence debt named in [calculus-2-tier-map-2026-05-28.md](calculus-2-tier-map-2026-05-28.md) §"Known debt." Source-of-truth is the Lean stack at `~/git/lean/LeanProofs/Admissibility/`; this is the record of the patch and the reasoning behind its scope.

**Provenance:** Multi-model conversation 2026-05-30 (Claude Code main thread, ChatGPT-conservative). ChatGPT's read elevated the documented debt ("trajectory shape wrinkle, backport per-hop actor into the witness types") to a *substrate* divergence (`SafetyBridge.SafeStep` itself baked actor into the type, so the ledger model had to fork from the substrate to express per-hop actors). The patch scope follows that elevation; the deferred phases follow the explicit instruction not to drag the SafetyPath / forgetful-map / anti-laundering stack into this slice.

---

## What landed

**Substrate (`~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean`).**

- `AuthStep E st` — per-hop-actor authorized step (actor as **field**, not type parameter).
- `SafeStep E st` — same, plus bridge witness; `actor` field, not type parameter.
- `SafeStep.toAuthStep` — projection.
- `AuthorizedTraj E s s'` and `BridgedTraj E s s'` — generic per-hop-actor trajectory inductives over any `SafetyEnv E`; state-threaded via `E.run s hop.act`; the trajectory type binds no actor.
- `BridgedTraj.toAuthorizedTraj` — forgetful map.
- `bridgedTraj_preserves` — generic preservation theorem; structural recursion folding `E.preserves` through `Nat.le_trans`.

**Verdict-layer (`AuthorizedStepNotSafeWitness.lean`).** `AuthorizedStepC` and `SafeAuthorizedStepC` now carry `actor` as a field on `AuthorizedStepC`. `Authorizable st a x := ∃ s : AuthorizedStepC st, s.actor = a ∧ s.step = x`. `.toSafeStep` adapter supplies `actor := s.auth.actor`. Consumers (`poisonAuthorizedStep`, `genuineAuthorizedStep`, the two `no_safeAuthStep_for_poison` / `no_safeAuthorizedStepC_for_poison` theorems, the boundary theorem) updated mechanically.

**Verdict-layer trajectory specialization (`SafetyTrajectory.lean`).** Kept as a specialization because the verdict-layer wants to carry the actual `SafeAuthorizedStepC` (with the *real* `AuthorizedStepC` literal), not the existential-erased `SafeStep authEnv`. Renamed `AuthorizedTraj` → `AuthorizedTrajC`, `BridgedTraj` → `BridgedTrajC` (matching the `...C` "concrete" convention used by `AuthorizedStepC`); same per-hop-actor shape as the substrate, richer hop payload. `bridgedTraj_preserves` → `bridgedTrajC_preserves`. `no_bridgedTraj_to_poison_end` → `no_bridgedTrajC_to_poison_end`.

**Ledger (`AttestationLedger.lean`).** Bespoke `LedgerAuthStep`, `LedgerSafeStep`, `LedgerAuthTraj`, `LedgerBridgedTraj`, `ledgerBridgedTraj_preserves` all **deleted** — replaced by direct use of the generic substrate (`AuthStep ledgerEnv`, `SafeStep ledgerEnv`, `AuthorizedTraj ledgerEnv`, `BridgedTraj ledgerEnv`, `bridgedTraj_preserves`). `genuinePost`, `no_safeStep_for_revoke`, `revokeTraj`, `protocolHappyPath`, `protocolHappyPath_preserves`, `no_bridgedTraj_to_revoke_end`, `authorized_trajectory_loses_value` updated to consume the generic.

**`README.md` in `LeanProofs/Admissibility/`** — brick-2 and ledger sections updated.

**Build:** `lake build` green, 8305 jobs, sorry-free, no new axioms. Matches the pre-patch baseline on all green-counts.

## The acid test

The acid test (ChatGPT 2026-05-30):

> Can the generic trajectory represent a two-hop path where hop 1 is authorized by actor A and hop 2 by actor B, without pretending there is one global actor over the whole trajectory?

`protocolHappyPath : BridgedTraj ledgerEnv s0 (applyAct (applyAct s0 Act.post) Act.attest)` in `AttestationLedger.lean` is exactly this: hop 1 is `Party.writer.post`, hop 2 is `Party.auditor.attest`, packed as **one** `BridgedTraj ledgerEnv`. The trajectory type binds no actor; each hop carries its own as a field. Type-checks; builds; `protocolHappyPath_preserves` (the value floor) is discharged by the generic `bridgedTraj_preserves`, no bespoke proof.

Acid test passes by construction.

## Why Option B (not A, not C)

Three options were on the table before the patch:

- **Option A — documented-debt-only.** Backport per-hop actor into `AuthorizedStepC` / `SafeAuthorizedStepC`, drop the `(a : Actor)` parameter from `AuthorizedTraj` / `BridgedTraj`. Leaves `SafetyBridge.SafeStep` itself actor-typed. *Verdict:* insufficient. Per ChatGPT's read: "the global actor assumption is not merely in `AuthorizedTraj`. It is baked one level lower, into the primitive step type. So the ledger didn't 'diverge' casually. It had to fork because the base substrate did not permit per-hop actors." Patching only the trajectories leaves the substrate lie intact and future proofs inherit the fossil.
- **Option B — substrate fix (chosen).** Move actor to a field in `SafeStep` (and `AuthStep`, new) at the substrate. Add generic per-hop-actor trajectories at the substrate. Refactor verdict-layer and ledger to consume them. Result: one substrate, one shape, no fork.
- **Option C — full ChatGPT vision.** Option B plus rename to `AttestedTrajectory` / `SafetyPath`, add a coarser `SafetyPath` summary layer with forgetful map, add anti-laundering theorems (`forget_does_not_mint_authority`, etc.). *Deferred* — these are net-new architecture without a forcing case in the safety-axis preprint itself, and they change the shape of the public proof surface. Filed below as the staged future vision, candidate / non-binding.

Option B is the boring substrate correction. It retires the contradiction without expanding the calculus frontier — exactly what was wanted before publication. Per memory: "completeness before novelty" — finish what was opened (the substrate fork was an open obligation from the moment AttestationLedger forked); don't open new doors (SafetyPath) without a forcing case.

## Deferred — staged future vision (candidate / non-binding, per *name-early*)

Filed as a single record so a future session does not re-derive these from chat vapor. The target architecture, if and when a forcing case arrives:

```
SafeStep
  ↓ wrapped by
AttestedHop
  ↓ chained into
AttestedTrajectory
  ↓ erased/projected by
forget
  ↓
SafetyPath / SafetyTrajectoryView
```

Core invariant:

> AttestedTrajectory is the authority-bearing object. SafetyPath is a lossy view. A trajectory summary may preserve endpoints and final verdict, but it must not recreate hop authority, witness standing, custody, freshness, or non-contamination evidence.

Phased roadmap (from ChatGPT 2026-05-30):

- **Phase 1 — substrate correction.** DONE 2026-05-30 (this record).
- **Phase 2 — `AttestedHop` wrapper layer.** A wrapper carrying witness, custody, basis, value decay, timestamp, contamination check — without bloating the primitive `SafeStep`. Forcing case: first concrete consumer that needs hop-local custody / witness identity.
- **Phase 3 — `AttestedTrajectory` canonical.** Ordered chain of attested hops with adjacency / time-ordering / scope-compatibility predicates; trajectory-level properties (`EachHopAdmissible`, `NoUnauthorizedLift`, `NoScopeExpansion`, `ValueDecayRespected`, `NonContaminating`).
- **Phase 4 — `SafetyPath` summary + `forget`.** Paper-facing lossy projection. The forgetful map visibly erases hop-local actor, witness identity, attestation basis, custody, local freshness, scope justifications, contamination checks, intermediate values.
- **Phase 5 — preservation lemmas.** `forget_preserves_start` / `forget_preserves_end` / `forget_preserves_final_value` / `forget_preserves_final_verdict`. The summary is legitimate as a summary.
- **Phase 6 — anti-laundering lemmas.** What forgetting *cannot* recreate: `forget_does_not_mint_actor_authority`, `forget_does_not_preserve_witness_standing`, `forget_does_not_recover_hop_custody`, `forget_does_not_prove_no_contamination`. This is the theorem family that *earns* the architecture. Paper-facing one-liner: *a path summary may preserve shape and outcome, but cannot become proof of the authority, standing, or custody it erased.*
- **Phase 7 — `SingleActorTrajectory t a` as a predicate.** The single-actor case becomes a property over the per-hop substrate, not a primitive.

**Operational rule for any future Governor that consumes paths:**

> A summarized safe-looking path is not an admissible safety bridge. For gate decisions, the Governor needs the authority-bearing object (`AttestedTrajectory` or equivalent evidence packet); `SafetyPath` may be inspected, displayed, or used for orientation, but cannot serve as admissible proof of safety or authority.

**Forcing-case discipline.** Phase 2+ should not be implemented absent a downstream consumer whose safety claim cannot be stated under the current substrate but can under the wrapper. The substrate fix (Phase 1) was forced by the trajectory-divergence debt blocking the preprint. Phase 2+ is name-early, not authorization to build.

## Cross-references

- Original debt item: [calculus-2-tier-map-2026-05-28.md](calculus-2-tier-map-2026-05-28.md) §"Known debt" — now marked DISCHARGED.
- Exit criteria: [calculus-2-exit-criteria.md](../calculus-2-exit-criteria.md) — safety-axis section updated.
- Spine page: [admissibility-suite-spine-2026-05-28.md](../admissibility-suite-spine-2026-05-28.md) — preprint authorship can proceed against the canonicalized scaffold.
- ρ-drop decision: [safety-bridge-rho-drop-decision-2026-05-28.md](safety-bridge-rho-drop-decision-2026-05-28.md) — actor-inert bridge stays correct under the substrate fix; the bridge never read the actor, so moving actor field-wards on `SafeStep` is consistent with the ρ-drop rationale.
- Lean source of truth: `~/git/lean/LeanProofs/Admissibility/{SafetyBridge,SafetyTrajectory,AttestationLedger,AuthorizedStepNotSafeWitness,SafetyBridgeWitness}.lean`.
