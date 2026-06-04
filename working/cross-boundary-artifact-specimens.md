# Cross-Boundary Artifact Specimens

**Filed:** 2026-05-21
**Status:** Specimens landed (4 bricks, `lake build` green, no `sorry`); intentionally unwired at root. Hygiene round complete: README addendum + formalization-index entry + this note + projection-pattern documentation + gh-pages note on the main `README.md`.
**Lean modules:**
- `LeanProofs/Admissibility/CrossBoundaryExposure.lean`
- `LeanProofs/Admissibility/CrossBoundaryDegradation.lean`
- `LeanProofs/Admissibility/CrossBoundaryFailureMint.lean`
- `LeanProofs/Admissibility/CrossBoundaryCascade.lean`

## What this is

Four Lean specimens applying the admissibility kernel's forbidden-artifact-unconstructible discipline to a new artifact family: boundary-crossing exposures. Together they pin a small cross-boundary sub-kernel within `Admissibility/` without minting a new proof family or root namespace.

The four keepers:

```text
Boundary authorization is the exposure mint.
This is degradation provenance only. Not damage. Not failure leakage. Not cascade.
Failure is not exposure. Exposure from failure is minted only by boundary authorization.
Cascade is authorized exposure reachability. Not inevitability. Not degradation. Not damage.
```

The first three are negative theorems against forbidden artifacts; the fourth is the first *affirmative* theorem in the family, existentially stating that authorized paths *permit* (not inevitabilize) propagation. Each brick reuses the kernel containment theorem via projection rather than re-proving it. Composition discipline is what makes the quartet composable instead of four independent specimens that happen to share a directory.

## Audit provenance

Two-aperture audit dialectic produced these bricks:

- **Outside-aperture / category audit.** Fresh-context model (DeepSeek, no repo memory) was asked *"is this a process calculus?"* then *"what would it take to be one?"* The category-question forced the auditor to derive process-calculus requirements from first principles and check the existing admissibility kernel against them. Surfaced candidate structural residue (exposure artifact, Internal/External partition, provenance-bearing Cause, failure-to-exposure mint discipline).
- **Inside-aperture / kernel-overlap audit.** Paper-Claude ran the standard kernel-overlap audit against the candidates. Finding: the *proof pattern* (forbidden-artifact-unconstructible via authorized constructor + reach-preserved invariant) already existed three ways in the kernel — `StateTransition` trapdoor invariants, `Execution.AuthorizedStep` bundled construction, `TaxonomyGraph` forward-closed lane proofs. The *novelty* was the artifact vocabulary, not the proof family.

Demoted/reparented:

- ~~`Delta/Containment.lean`~~ (proposed by DeepSeek; would have minted a new root namespace) → **`Admissibility/CrossBoundaryExposure.lean`** (sibling specimen inside existing family)
- ~~"Δ-calculus" branding~~ → **cross-boundary artifact specimens** inside the pre-ratified `boundary-calculus / admissibility-cybernetics` candidate program (see [boundary-kernels-program-candidate.md](./boundary-kernels-program-candidate.md))
- ~~hard-coded `Domain := dn | dobs | da | external`~~ → **abstract `Domain` parameter** with operator-supplied `BoundaryPartition`
- ~~hard-coded `Failure` enum~~ → **abstract `Failure` parameter**

Two-tracks rule filed as memory `feedback-kernel-vs-process-calculus`: kernel-specimen track builds now; process-calculus/composition track (parallel composition, monitors, refinement, bisimulation) defers until a forcing case demands them.

Outside-aperture methodology filed as memory `feedback-outside-aperture-audit`: rare cadence, must funnel through inside-aperture before any landing, *fresh aperture can surface missing shape, it cannot assign repo authority.*

## The three bricks

### Brick 1: CrossBoundaryExposure

**Artifact:** `Exposure (origin, target, failure)` — a first-class boundary-crossing record with provenance.

**Mint rule:** `Step.expose e` requires `Boundary.authorized e.origin e.target = true`. No other constructor adds exposures.

**Theorem:** `no_external_exposure_without_authorized_edge` — under `hNoExport : ∀ di dOut, P.Internal di → P.External dOut → B.authorized di dOut = false`, no reachable configuration contains an exposure with Internal origin and External target.

**Utility:** `Reach.trans` lives here as the kernel utility used by downstream slices to chain projected reachabilities.

### Brick 2: CrossBoundaryDegradation

**Artifact:** `Cause.direct | Cause.fromExposure (e : Exposure)` — degradation cause with optional exposure provenance.

**Mint rules:**
- `Step.degrade_direct` updates a grade without any exposure precondition (direct external trigger licensed).
- `Step.degrade_fromExposure` requires `e ∈ c.exposures ∧ e.target = d` as constructor arguments. No anonymous blame.

**Theorem:** `no_external_degradation_from_internal_exposure` — under a sealed boundary, no `degrade_fromExposure` step targeting an External domain can cite an exposure with Internal origin. Proved by projection through the exposure kernel.

**Scope fence:** `Grade` abstract; recovery and hysteresis belong on the persistence side, not here.

### Brick 3: CrossBoundaryFailureMint

**Artifact:** `FailureEvent (domain, failure)` — recorded failure, domain-local.

**Mint rules:**
- `Step.fail d f` records a failure event with no boundary precondition (failure is local).
- `Step.exposeFromFailure e` requires both `⟨e.origin, e.failure⟩ ∈ c.failures` AND `B.authorized e.origin e.target = true`.

**Theorems:**
- `no_exposeFromFailure_internal_to_external` (step-local) — direct from the authorization precondition.
- `no_external_exposure_from_internal_failure` (reachable-config) — projection corollary.

**The English sentence finally has a spine:**

```text
internal failure (Step.fail)
  → recorded failure event
  → authorized exposure mint (Step.exposeFromFailure, requires both preconditions)
  → (later, via Cascade) propagated immediate-origin exposures along authorized hops
  → (further downstream, deferred) consequence
```

Each arrow is a constructor or theorem application. No prose glue.

### Brick 4: CrossBoundaryCascade

**Artifact:** `AuthorizedPath B d₀ dₙ` — an abstract transitive closure of `B.authorized`, with two constructors (`edge` for single hops, `cons` for chained). Not a graph; not `TaxonomyGraph` reachability.

**Mint rule:** `Step.exposeFromExposure e_in dNext` requires `e_in ∈ c.exposures ∧ B.authorized e_in.target dNext = true`. Mints `Exposure(e_in.target, dNext, e_in.failure)` — immediate-origin discipline, *not* root-origin.

**Theorem:** `authorized_path_permits_endpoint_exposure` — given an `AuthorizedPath B d₀ dₙ` and a failure kind `f`, *there exists* a reachable cascade configuration containing some exposure to `dₙ` with failure `f`. Bootstrap: `Step.fail d₀ f` + `Step.exposeFromFailure ⟨d₀, d_first_hop, f⟩` + chain `Step.exposeFromExposure` along the path via induction on `AuthorizedPath`.

**Why immediate-origin matters.** A path `d₀ → d₁ → … → dₙ` provides authorization on every immediate hop, not on the root-to-final shortcut `B.authorized d₀ dₙ`. If cascade minted `Exposure(d₀, dₙ, f)` directly, the kernel projection would demand `B.authorized d₀ dₙ = true`, which is *not* what an authorized path supplies. Per-hop immediate-origin minting keeps each cascade step kernel-projectable. If ultimate (root-cause) provenance is ever needed, a separate `CascadeChain` witness can record the chain of minted exposures explicitly. Do *not* overload `Exposure.origin` to mean both "immediate crossing origin" and "root cause."

**Scope fence.** Cascade is the first affirmative theorem in the family — extra-strict wording: *permits*, *reachable*, *exists*, *can in principle*. Never *inevitable*, *will*, *must*, *almost surely*, *eventually*. No scheduling, no fairness, no rates, no scheduler theology. *Topology, not selection.* The seam-line: **Cascade is topology. Scheduling is selection. Do not let selection sneak into topology.**

**The five `≠` axioms** the operator emphasized while this brick was being built, and which the cascade brick honors at the constructor level:

```text
topology ≠ scheduling
reachability ≠ inevitability
exposure ≠ degradation
failure ≠ external claim
hiding ≠ containment
```

## The projection pattern

The composition discipline that lets each downstream brick reuse the kernel containment theorem without reproving it. Five steps:

### 1. Richer Config

Each brick defines its own `Config Domain Failure [Grade ...]` carrying the kernel's exposure set plus whatever new artifacts the brick introduces.

```lean
-- Kernel
structure CrossBoundaryExposure.Config where
  exposures : Finset (Exposure Domain Failure)

-- Degradation
structure CrossBoundaryDegradation.Config where
  exposures : Finset (Exposure Domain Failure)
  grades : Domain → Grade

-- Failure mint
structure CrossBoundaryFailureMint.Config where
  failures : Finset (FailureEvent Domain Failure)
  exposures : Finset (Exposure Domain Failure)
```

The exposure-set field has the same name and type as the kernel's. This is what makes `toExposureConfig` definitionally clean.

### 2. toExposureConfig projection

```lean
def toExposureConfig (c : Config ...) : CrossBoundaryExposure.Config ... :=
  ⟨c.exposures⟩
```

Drops the new artifacts, preserves the exposure set. `toExposureConfig (initialConfig ...) = CrossBoundaryExposure.initialConfig ...` holds by `rfl` in both downstream bricks. This is load-bearing for the final step.

### 3. step_to_exposure_reach

Per-step projection lemma:

```lean
lemma step_to_exposure_reach (h : Step B c a c') :
    CrossBoundaryExposure.Reach B (toExposureConfig c) (toExposureConfig c')
```

Steps that *don't* touch exposures (degrade, fail) project to `Reach.refl`. Steps that *do* mint exposures (expose, exposeFromFailure) project to a single kernel `Step.expose` with the same authorization argument. The cited authorization is reused literally, not re-derived.

### 4. reach_to_exposure_reach

Chain the per-step projections using `CrossBoundaryExposure.Reach.trans`:

```lean
lemma reach_to_exposure_reach (h : Reach B c₀ c₁) :
    CrossBoundaryExposure.Reach B (toExposureConfig c₀) (toExposureConfig c₁) := by
  induction h with
  | refl => exact CrossBoundaryExposure.Reach.refl _
  | tail _hReach hStep ih =>
      exact CrossBoundaryExposure.Reach.trans ih (step_to_exposure_reach hStep)
```

### 5. Invoke kernel containment

The brick's own theorem is now a thin corollary:

```lean
theorem brick_theorem ... := by
  ...
  -- Project reach
  have hReachExp : CrossBoundaryExposure.Reach B ... := by
    have hInit : toExposureConfig (initialConfig ...) =
                 CrossBoundaryExposure.initialConfig ... := rfl
    rw [← hInit]
    exact reach_to_exposure_reach hReach
  -- Invoke kernel
  have hContained := CrossBoundaryExposure.no_external_exposure_without_authorized_edge
                       P B hNoExport (toExposureConfig c) hReachExp
  -- Use it
  ...
```

### Why this matters

The discipline is what makes the bricks composable. Three properties fall out:

1. **No re-proof.** The kernel containment theorem fires once and is reused literally.
2. **Type-level enforcement.** A new step constructor that bypasses the boundary check would break `step_to_exposure_reach` immediately — the failing case has no kernel-side witness to project to.
3. **Forward-compatible.** Any future cross-boundary slice (cascade, monitoring, anti-laundering downstream of provenance) can inherit containment by following the same five steps.

## What this does NOT warrant

- **No claim about real systems.** `Domain` and `Failure` are abstract type parameters; `Internal` and `External` are operator-supplied predicates. Concrete instantiation against `TaxonomyGraph.Domain` is a deferred sibling slice (`CrossBoundaryExposureTaxonomy.lean` shape), not present.
- **No process syntax.** No parallel composition, no monitors, no actuators, no bisimulation, no rates. Two-tracks rule applies.
- **No cascade.** Cascade is the licensed-but-not-required next rung. If it ever lands, the shape is existential reachability along authorized paths (no fairness, no inevitability), and `TaxonomyGraph` enters only as a sibling instantiation layer.
- **No persistence dynamics.** Recovery, hysteresis, capability distinctions belong on the persistence side. Cross-boundary is about boundary-crossing artifact mints, not grade trajectory.
- **No claim that direct degradation is impossible.** `Cause.direct` is licensed; the theorem speaks only about exposure-attributed degradation.

## The slice is closed

The four-brick stack is structurally complete. Further work is a *new slice*, not "one more brick." Specifically deferred (not forgotten):

- **`CrossBoundaryCascadeTaxonomy.lean`** — concrete `TaxonomyGraph.Domain` wiring. The cascade kernel keeps the boundary partition abstract; instantiation against the 15-domain cybernetic taxonomy lives in a sibling instantiation module, not in the kernel.
- **`CrossBoundaryScheduling.lean`** — selection layer. `EnabledStep` / `SchedulerAllows σ c step` / `ScheduledReach σ c₀ cₙ`. Distinguishes "permitted by topology" from "selected by policy." Where fairness, starvation, and *eventually*-claims would live if forced.
- **Process calculus** — composition, monitors vs actuators, traces, refinement, weak bisimulation, equivalence. Deferred until ≥ 2 specimens cannot state their theorem without composition.
- **Hysteresis / recovery** — belongs near `PersistenceModel`, not in the `CrossBoundary*` family. Object is grade/history/capability, not boundary-crossing.
- **Stochastic / load / hyperscale** — goblin country. The bridge phrase: *hyperscale turns possibility into exposure pressure.* The deterministic kernel says what is permitted; hyperscale says which permitted things stop being edge cases and start becoming weather. Not v0, not v1, possibly not even v2.

The hierarchy:

```text
Court first:
  Exposure
  Degradation
  FailureMint
  Cascade

Map later:
  taxonomy wiring
  scheduling
  composition
  process calculus
  trace equivalence

Goblin country:
  load
  rates
  hyperscale
  tail-risk becoming weather
```

Each rung up requires a new assumption surface. The discipline:

```text
Do not put probability on topology.
Do not put inevitability into reachability.
Do not put scheduler assumptions into cascade.
Do not put hyperscale conclusions into v0.
```

## Related

- `feedback-kernel-vs-process-calculus` (memory) — two-tracks rule
- `feedback-outside-aperture-audit` (memory) — methodology pattern
- `feedback-kernel-overlap-audit` (memory) — the inside-aperture audit gate
- [boundary-kernels-program-candidate.md](./boundary-kernels-program-candidate.md) — pre-ratified candidate program name; the trio lives under it as specimens, not as the program
- [admissibility-decay-family-note.md](./admissibility-decay-family-note.md) — sibling artifact-family work on the temporal axis
- `LeanProofs/Admissibility/README.md` — full module entries with theorem statements
- `WHAT-THE-LEAN-STACK-PROVES.md` — formalization-index section "Infrastructure: Cross-Boundary Artifact Specimens"

## Keepers

```text
Boundary authorization is the exposure mint.
This is degradation provenance only.
Failure is not exposure.
Cascade is topology. Scheduling is selection.
Reachability ≠ inevitability.
Court first, map later.
Fresh aperture surfaces shape; kernel-aware aperture assigns authority.
Hyperscale turns possibility into exposure pressure.
```

Tiny legal machine. Four new contraband categories — three forbidden, one affirmative reachability. Same courthouse.
