# Fixed-Value Fragment — Value-Sound Gates in Lean 4

**Status:** Fixed-Value Fragment of the admissibility calculus
(2026-06-01). Working substrate; not promoted as standalone
formal-methods publication. Closes the case where `value` is
environmental — the function does not mutate while the gates are
being checked. The case where `value` and its companions mutate is
the maximal calculus, in progress at
[`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md).
The fragment exists to *hold the things still that the calculus
must learn to mutate*; the artifacts are sibling halves of the same
arc, not competing artifacts.

DeepSeek-class adversarial review correctly diagnosed the fragment
as definitional propagation dressed in heavy vocabulary. The
appropriate response is reclassification, not theorem inflation.
Five things this artifact does carry: (i) authorization ≠
preservation, (ii) local preservation ≠ composition, (iii) `bridge`
and `MergeOk` are distinct operation-specific gates, (iv) Stale as
positive necessity failure forces the basis/value layer split, (v)
§4 demonstrates the boundary-witness schema is too thin to be
keystone. Those are the load the fragment bears. Body, audit trail,
and Lean substrate references all preserved in-place below. Spine:
[paper-value-sound-gates-spine-2026-06-01.md](paper-value-sound-gates-spine-2026-06-01.md).

**Provenance:** ChatGPT drafted both an "abstract fog" variant and a
sharper variant; operator picked the sharper one. Claude-web reviewed
and proposed four precision edits (three on the abstract, two on the
contribution list, one overlapping). Integrated here as the single
controlling version per operator instruction (no model split at this
stage).

## Working title

**Value-Sound Gates: Authorization and Composition in Lean 4**

## Abstract — draft v1

Authorization is not preservation, and local preservation is not
composition. This paper formalizes both claims in Lean 4 as a bounded
admissibility sub-calculus over transition and merge. The core pattern
is *value-sound gating*: weak admissibility objects may be
constructible without the witness that makes the relevant operation
value-preserving, while strong admissibility objects carry that witness
explicitly.

At the transition layer, an authorized step records permission to act,
while a bridged step additionally carries evidence that the action
preserves an externally supplied defended value. At the composition
layer, locally bridged branches do not by themselves determine whether
reconciliation is value-sound; additional merge-specific evidence is
required. We instantiate this with three merge specimens: shared-budget
overrun, stale-evidence reconciliation, and conflict-policy loss. One
specimen (stale evidence) gates at the level of *basis* for future
value rather than present value; freshness is treated as a guard for
value-preserving continuation, not as a second defended observable.

The paper deliberately does not treat the common forgetful-map
obstruction as the main theorem. Non-surjectivity and no-section
claims — classically equivalent here — are too weak: they hold for
trivial maps such as the successor on the naturals. The substantive
content is that the strong families are value-sound gates for specific
operations. This operation-specificity is itself a finding: transition
and merge cannot be collapsed into one abstract step without losing
the joint conditions that make composition meaningful.

This is not the maximal admissibility calculus. It closes a bounded
fragment over transition and merge in which the defended value
function is environmental rather than mutable state. Self-amendment
— where the value function, or the policy predicates value-soundness
depends on, become subject to gated change — is left outside scope.

## Contribution list — draft v1

This paper makes four contributions.

1. **A Lean 4 safety gate for authorized transitions.**
   We formalize a transition-level distinction between authorized
   steps and bridged steps. Authorization supplies permission to act;
   bridge evidence supplies the value-preservation witness. The
   resulting strong family is value-sound by construction through
   `SafetyEnv.preserves`.

2. **A composition gate for locally bridged branches.**
   We show that local bridge evidence does not automatically survive
   reconciliation. Three specimens isolate distinct merge-boundary
   failures: shared-budget overrun, stale evidence at reconciliation
   time, and conflict-policy loss. Each specimen supplies both a
   negative case and a restoration condition — the witness that
   blocks the failure.

3. **A bounded value-sound gating pattern.**
   We identify the shared structure between the transition and
   composition results: weak admissibility objects become value-sound
   only when admitted by explicit witnesses. Sufficiency is
   operation-specific; for composition, necessity is characterized
   per slice and at the layer where the slice's content actually
   lives, rather than as a single universal law. The shared
   boundary-witness schema is expository rather than constitutive;
   the content lives in the operation-specific soundness obligations.

4. **A scope boundary for the larger admissibility calculus.**
   We separate this bounded sub-calculus from future self-amendment
   work. The present paper studies transition and composition where
   every gate is sound relative to an externally supplied value
   function. Self-amendment is precisely the regime where that
   externality fails: `value`, standing, bridge policy, or merge
   policy become themselves subject to gated mutation.

## §1. Introduction

The substrate of the broader Δt program admits an embarrassing
situation: an authorized action can strictly decrease an externally
defined defended value. At the verdict layer, where the kernel's
`AuthorizedStep` bundles a write-standing proof with an all-green
verdict that the action's claim is licensed by the env's basis,
precedence, and standing components, the wound takes the form

> kernel-legible all-green verdict + mutation standing
> ⇏ defended-value preservation.

This is *Frontier 1* of the substrate's frontier ledger, in the
foundational failure geometry of Paper 22 [ref]. The kernel can say
a transition is *authorized*; it cannot say the transition
*preserves defended value*. The wound is exhibited concretely in
`AuthorizedNotSafe.lean` at the standing layer and transferred to
the verdict layer in `AuthorizedStepNotSafe.lean`. Both modules
supply explicit specimens whose execution drops the defended value
floor while satisfying every authorization predicate the kernel
knows how to check.

This paper formalizes the bounded conditional answer to that wound.
Authorization records permission to act; a separate *bridge* witness
records evidence that the action preserves a defended value floor.
Safety is the conjunction of authorization and bridge evidence —
neither factor implies the other — and the substrate's `SafetyEnv`
packages the two halves so that a safety-relevant step (`SafeStep`)
cannot be inhabited without both. The conditional soundness theorem
— `SafeStep` preserves the value floor — projects through the
bridge's value-preservation obligation; authorization is carried by
the bundle but is never consumed in the proof. That absence is the
content: a concrete bridge predicate cannot earn its keep by
pointing back at authorization.

Authorization-plus-bridge, however, gates only individual
transitions. Two locally bridged trajectories — each carrying
step-level bridge evidence on every hop — can merge into a state
outside the strong family. Branch-local bridges do not see joint
resource use against a shared cap, do not see future reconciliation
time outside their validity horizon, and do not see the
reconciliation policy's verdict on incompatible branch states. The
composition axis needs its own gate witness: a *merge admissibility*
predicate `MergeOk` that supplies the joint reading branch-local
bridges cannot. Three slice specimens isolate the failure modes —
shared-resource overrun (Budget), temporal staleness (Stale), and
reconciliation-policy collision (Conflict) — each with both a
negative case and a restoration condition. One specimen (Stale)
gates at the level of *basis* for a future value-affecting action
rather than at the merge boundary itself; the substrate carries an
explicit basis-layer instantiation that pays rent without promoting
freshness to a parallel defended observable.

The pattern is the same across both axes: a weak family
(permission-to-act records; locally bridged trajectory pairs) and a
strong family obtained by adjoining the gate witness, related by a
forgetful map. Non-emptiness of the gap predicate produces weak
objects outside the strong family — explicit witnesses that the gate
is not vacuous. The shared shape is made formal in a boundary-witness
schema whose role is honest exposition; the schema is *not* the
keystone, because non-surjectivity by itself is too weak to
discriminate the bridge or merge gate from arbitrary contentless
maps (`Nat.succ` has it). The keystone's content lives per-axis, in
the operation-specific value-soundness theorems each gate witness
discharges. The witness *gates* (admits a subset of the weak
family); it does not *enrich* (distinguish within a fiber).

The paper closes a bounded sub-calculus, not the maximal
admissibility calculus. The fence is structural: every gate in the
body is sound relative to an externally supplied value, where
`value` is a field of `SafetyEnv` rather than a part of mutable
state. The regime in which `value` itself becomes part of what
mutates — and, more broadly, the regimes in which the policy
predicates value-soundness depends on become themselves subject to
gating — is deferred to a future synthesis whose title is reserved.

The remainder is structured as follows. §2 instantiates the
value-sound gating pattern at the transition layer. §3 instantiates
it at the composition layer, across the three slice specimens. §4
lifts the shared shape into the boundary-witness schema and shows
why the schema is exposition rather than keystone. §5 states the
scope fence. §6 surveys related work at working-draft level. §7
concludes.

## §2. Axis 1: authorization gated by bridge evidence

This section gives the transition-layer instantiation of the
value-sound gating pattern. The substrate is `SafetyBridge.lean`; the
per-step composability and trajectory-level preservation pieces live in
the same module. The wound it answers — that the kernel's authorization
predicate carries no preservation obligation for externally defined
values — is exhibited at the standing layer in `AuthorizedNotSafe.lean`
and transferred to the verdict layer in `AuthorizedStepNotSafe.lean`.

### 2.1 The safety environment

Fix a triple `(σ, α, ρ)` of state, action, and actor types. A *safety
environment* over the triple is a record `SafetyEnv σ α ρ` carrying
five fields: a transition function `run : σ → α → σ`; an authorization
relation `Allowed : σ → ρ → α → Prop`; an externally defined defended
value `value : σ → Nat`; a candidate-neutral bridge predicate `bridge :
σ → α → Prop`; and a constructive obligation

```
preserves : ∀ st x, bridge st x → value st ≤ value (run st x).
```

We use the *safety floor*

```
SafetyPreserving E st x  :=  E.value st ≤ E.value (E.run st x)
```

as the value-soundness predicate at the transition layer. The floor is
non-decrease rather than equality; strengthening to conservation is a
doctrinal choice a stricter environment may make.

Three design choices in `SafetyEnv` are load-bearing for the paper's
framing.

First, `value` is *external*. It is a function of state, not part of
mutable state. Every theorem in this section is sound relative to that
externality. The closure assumption that no transition reaches `value`
itself is what fences the bounded calculus off from self-amendment; we
discuss this in §5.

Second, `bridge` is a *slot*, not a chosen predicate. The substrate is
candidate-neutral: a `SafetyEnv` is constructible by anyone who can
name a bridge predicate and discharge `preserves` for it.
`SafetyBridgeWitness.lean` exhibits a non-contamination candidate to
demonstrate that the slot is non-vacuously inhabitable; we do not
ratify it here.

Third, `bridge` is *actor-inert*: its signature is `σ → α → Prop`, not
`σ → ρ → α → Prop`. Actor-relative evidence remains in `Allowed`. If a
future bridge candidate genuinely requires actor identity, the right
correction is to actor-index the transition relation itself
(`run : σ → ρ → α → σ`) rather than smuggle actor-dependence through
`bridge`. The named deferred extension `ActorSensitiveBridgeEnv` is
filed but not implemented in this paper's substrate.

### 2.2 Two step kinds: authorized and safe

We package per-hop transitions as records. An *authorized step* at
state `s : σ` is

```
structure AuthStep (E : SafetyEnv σ α ρ) (s : σ) where
  actor   : ρ
  act     : α
  allowed : E.Allowed s actor act
```

A *safe step* at the same state additionally carries a bridge witness:

```
structure SafeStep (E : SafetyEnv σ α ρ) (s : σ) where
  actor   : ρ
  act     : α
  allowed : E.Allowed s actor act
  bridged : E.bridge s act
```

The structural point that does the work for everything that follows: a
`SafeStep` is not inhabitable without a `bridged` field. The bridge is
non-optional at the safety-relevant boundary, exactly as
`AuthorizedStep` cannot be inhabited without both halves of
authorization and `RecoveryEnv` cannot omit its monotonicity witness.

The forgetful map drops the bridge:

```
SafeStep.toAuthStep : SafeStep E s → AuthStep E s.
```

The strong family `SafeStep E s` projects to the weak family
`AuthStep E s` by erasure. The reverse direction — when, and on which
authorized steps, a `SafeStep` can be reconstructed — is where the
content of this section lives.

### 2.3 Soundness

The bridge entails the floor:

```
theorem safeStep_is_safe (E : SafetyEnv σ α ρ) (s : σ) (h : SafeStep E s) :
    SafetyPreserving E s h.act :=
  E.preserves s h.act h.bridged.
```

The proof projects `E.preserves` through `h.bridged`. The `allowed`
field is carried by the bundle but is never consumed. The absence of
any `Allowed` hypothesis from the proof of `safeStep_is_safe` *is* the
content: a concrete bridge cannot earn preservation by pointing back at
authorization. That route is closed. Preservation must be discharged
through `preserves`, by whatever structural evidence the chosen bridge
predicate names.

Trajectory composition follows by transitivity. The inductive type
`BridgedTraj E s s'` is a state-threaded chain of safe steps, and

```
theorem bridgedTraj_preserves : BridgedTraj E s s' → E.value s ≤ E.value s'
```

folds the per-hop discharge through `Nat.le_trans`. Single hops
generalize to trajectories without strengthening the obligation on
`bridge`.

### 2.4 The gap and the obstruction

The kernel's authorization layer admits an unsafe witness.
`AuthorizedNotSafe.lean` exhibits a `(GovState, Actor, Step, StepAllowed)`
configuration whose execution strictly decreases an externally defined
defended value. The transfer is settled at the verdict layer by
`AuthorizedStepNotSafe.lean`: even when the kernel-legible verdict
returns `authorized` across all three component checks (basis,
precedence, standing), the bundled `AuthorizedStep` object still admits
a strict decrease. Authorization at every layer the kernel offers —
standing, claim verdict, and the combined object — carries no
preservation obligation for externally defined values.

The formal predicate naming the wound is

```
AuthorizationBridgeGap E  :=  ∃ s (x : AuthStep E s), ¬ E.bridge s x.act.
```

A gap is an authorized step whose action is not bridged. Its presence
is what makes the separation between authorized and safe non-vacuous;
in its absence every authorized step is bridged
(`no_gap_implies_authorized_steps_bridgeable`).

Where the gap holds, no `SafeStep` erases to the witnessing authorized
step:

```
theorem no_safeStep_for_unbridged_authStep
    (x : AuthStep E s) (hbad : ¬ E.bridge s x.act) :
    ¬ ∃ h : SafeStep E s, h.toAuthStep = x.
```

The argument is direct: if some `h : SafeStep E s` had
`h.toAuthStep = x`, then `h.act = x.act` and `h.bridged : E.bridge s
h.act = E.bridge s x.act`, contradicting `hbad`. The gap-level form
`gap_blocks_safeStep_lift` packages this as the existential statement
that an authorization-bridge gap produces an authorized step outside
the forgetful map's image.

This is the per-axis instance of *weak admissibility object outside
the strong family*: the authorized-but-unbridged step is an inhabitant
of the weak type `AuthStep E s` whose preimage under the forgetful map
is empty. The strong family `SafeStep E s` is a strict sub-family
precisely when a gap exists.

### 2.5 When authorization suffices

A natural question is: when does the gap matter? The collapse
characterization names this precisely. Define

```
AuthPreserves E  :=  ∀ s (x : AuthStep E s), E.value s ≤ E.value (E.run s x.act).
```

Then

```
theorem authorizedTraj_preserves_iff_authPreserves :
    (∀ s s' (t : AuthorizedTraj E s s'), E.value s ≤ E.value s') ↔ AuthPreserves E.
```

Trajectory-level preservation across *all* authorized trajectories
holds exactly when *every* authorized step preserves the floor. The
two directions are: an authorized step is itself a one-hop authorized
trajectory (forward), and trajectory preservation folds per-hop
preservation through transitivity (reverse).

The bridge is redundant for proving trajectory preservation exactly
where `AuthPreserves E` holds. This is distinct from collapse of the
weak and strong step families. A sound-but-not-complete bridge may
leave some authorized value-preserving steps unbridged; in that case
`AuthPreserves E` holds while an authorization-bridge gap still
exists. So `AuthPreserves E` collapses the *preservation
obligation*; absence of the bridge gap collapses the *reconstruction
problem* from `AuthStep` to `SafeStep`. The two are equivalent only
when the bridge is complete (every value-preserving authorized step
is bridged), and the substrate deliberately reserves the
sound-but-not-complete corner for the interesting witnesses (§2.6).

### 2.6 The degenerate corner

A bridge is *maximal* if it is logically equivalent to value
preservation:

```
MaximalBridge E  :=  ∀ s act, E.bridge s act ↔ E.value s ≤ E.value (E.run s act).
```

A maximal bridge is preservation restated. The completeness predicate

```
BridgeComplete E  :=  ∀ s act, E.value s ≤ E.value (E.run s act) → E.bridge s act
```

follows immediately by modus ponens on the iff
(`maximal_bridge_implies_complete`). Maximal bridges admit the
trivializing critique that "the bridge is just the theorem
conclusion," and they are not what the substrate aims at.

The interesting witnesses occupy the sound-but-not-complete corner: a
structural bridge that entails preservation but rejects some
value-preserving actions for lack of structural evidence.
`SafetyBridgeWitness.lean` exhibits one such candidate at the action
layer — *non-contamination* of the witness aggregator — and the
substrate exhibits the discrimination concretely.

The non-contamination predicate accepts a `recordReceipt` action
exactly when the appended receipt is genuine:

```
nonContamination st (Step.recordReceipt r)  ↔  r = true.
```

Two steps from the clean state, both `StepAllowed`. The first
(`genuineStep := Step.recordReceipt true`) appends a genuine
receipt; the second (`scenarioStep`) is the exact poison step that
produced the §2.4 wound in `AuthorizedNotSafeWitness.lean`. The
theorem `bridge_separates_authorized_steps` discharges both at
once: the bridge accepts the genuine step and rejects the poison
step, *both authorized*. `no_safeStep_for_poison` then closes the
audit at the gate — no `SafeStep` carries the poison action,
because its `bridged` field is uninhabitable.

This is the demonstration that the bridge *discriminates*. The
corner is occupied by a candidate that does refusal work — the
per-axis analog of `Nat.succ`'s anti-bullshit role in §4. And the
sound-but-not-complete property bites cleanly. Per the substrate's
header note on `SafetyBridgeWitness.lean`, `nonContamination`
rejects *any* false receipt, including one appended to an
already-poisoned store where the defended value floor (`value = 0`)
is already at the floor and the action would not further decrease
it. A maximal bridge — one logically equivalent to value
preservation — would accept such an action because its execution
does not strictly decrease defended value. `nonContamination`
refuses on local structural grounds, not on outcome. The refusal is
the design, not a limitation.

This is not a ratification of the candidate; choosing among
non-contamination, witness-encapsulation, and receipt-persistence is
doctrinal work that the substrate does not pre-decide. The point
established by exhibition is that the sound-but-not-complete corner
is occupied by a candidate that does the discrimination work the
schema (§4) cannot — refusal on structural evidence, not on whether
the forgetful map's image happens to be exhausted.

### 2.7 Summary

The transition layer factors into a weak family `AuthStep E s` of
permission-to-act records and a strong family `SafeStep E s` whose
construction requires a bridge witness. The two families are related
by an erasing forgetful map. Soundness is a projection through
`preserves`, not through `Allowed`. Non-emptiness of the gap predicate
produces explicit weak objects outside the strong family's image, both
at the step layer (`no_safeStep_for_unbridged_authStep`) and at the
gap level (`gap_blocks_safeStep_lift`). The collapse characterization
pins where the gap matters: exactly where authorized hop preservation
fails. The maximal-bridge corner is fenced off as the degenerate case;
useful bridges are sound but not complete.

This is the pattern §3 will echo and complicate. The complication is
that "the operation" is no longer a single transition: it is a merge
of two locally bridged branches, and the gate witness must speak to
the *joint* of the two branches rather than to either branch alone.

## §3. Axis 2: composition gated by merge evidence

Axis 2 instantiates the same value-sound gating pattern at the
composition layer. The operation is no longer a single transition; it
is the reconciliation of two locally bridged branches. The substrate
is `ParameterizedMerge.lean`, which schematizes three slice modules —
`BudgetMerge.lean`, `StaleEvidenceMerge.lean`, and
`MergeConflict.lean` — each exhibiting a distinct way that
branch-local bridge evidence fails to survive reconciliation.

The complication §2.7 promised: the merge admissibility witness must
speak to the *joint* of two branches, not to either branch alone.
Branch-local bridges do not see joint resource usage, do not see
future time, and do not see the reconciliation policy's verdict on
incompatible branch states. The gate witness — per slice, the
predicate `MergeOk` — is exactly what supplies the joint reading that
branch-local bridges cannot.

A further complication that does not arise in §2: not every slice
carries its content at the value layer. One of the three (Stale)
gates a *basis* for the next value-affecting action rather than gating
value preservation at the merge boundary itself. We address this
asymmetry directly in §3.4 and again in the necessity verdict (§3.5)
— it is structural, not accidental.

### 3.1 The merge frame

Fix a `SafetyEnv σ α ρ`. A *merge frame* over the environment is a
record

```
structure MergeFrame (Param σ α ρ : Type) (E : SafetyEnv σ α ρ) where
  merge   : Param → σ → σ → σ
  MergeOk : Param → σ → σ → Prop
```

The `Param` type is the slice's external input: for Stale it is the
reconciliation time; for Budget and Conflict it is `Unit`. The `merge`
operator reconciles two branch states; `MergeOk` is the
merge-boundary admissibility predicate that gates the strong family.

Three discipline choices in the frame correspond to structural
findings in the substrate.

First, *branch / input viability is not absorbed into `MergeOk`*. The
restoration theorems below carry viability hypotheses
(`E.value a = 1`, `E.value b = 1`) as separate premises. Folding them
into `MergeOk` would turn the predicate into "everything needed for
the conclusion" — the self-proving-predicate trap. Keeping them
separate is what lets `MergeOk` mean exactly *merge-boundary
admissibility*, distinct from the per-branch witnesses already on the
table.

Second, *the suite carries a single defended observable*,
`E.value : σ → Nat`. This was a deliberate cut from an earlier draft
that promoted freshness to a per-slice second observable. The cut is
preserved by the frame: `MergeOk` is what varies per slice; the floor
it protects is the same single `E.value` throughout. We return to
this when the basis layer (§3.4) introduces a `Guard : σ → Prop` —
`Guard` is a `Prop`, not a `σ → Nat`, and it does not promote.

Third, `Param` enters the frame as a type, not a field. A frame for
Budget and a frame for Stale do not share a `Param`; they are not
instances of a single fixed frame. The cross-slice structure is the
*schema*, applied with different parameters per slice, not a single
frame over a sum type.

### 3.2 Restoration shapes — sufficiency

Three restoration predicates schematize the soundness direction.

The *boundary form*:

```
def MergeRestoresValue (F : MergeFrame Param σ α ρ E) : Prop :=
  ∀ p a b, E.value a = 1 → E.value b = 1 → F.MergeOk p a b →
    E.value (F.merge p a b) = 1.
```

Viable inputs plus merge admissibility yield a viable merged
endpoint. The boundary form is the "merge survives" version of the
value floor.

The *trajectory form*:

```
def MergeComposesBridgedEndpoints (F : MergeFrame Param σ α ρ E) : Prop :=
  ∀ p s sA sB,
    BridgedTraj E s sA → BridgedTraj E s sB →
    E.value sA = E.value s → E.value sB = E.value s →
    F.MergeOk p sA sB →
    E.value (F.merge p sA sB) = E.value s.
```

The trajectory form takes the §2 trajectory result and lifts it
across reconciliation: two `BridgedTraj` witnesses from a common
start state, each preserving the start's defended value, plus a
merge-boundary admissibility predicate, yield a merged endpoint that
still preserves the start's defended value. The `BridgedTraj`
hypotheses certify branch-local preservation; `MergeOk` supplies the
reconciliation-boundary evidence; the two complete the gate.

The *basis form*:

```
def MergeRestoresBasis (F : MergeFrame Param σ α ρ E) (Guard : σ → Prop) : Prop :=
  ∀ p a b, F.MergeOk p a b → Guard (F.merge p a b).
```

The basis form is for slices whose admissibility carries content
beyond the value floor — the merged endpoint may not exhibit value
change at the boundary, but it satisfies a precondition (`Guard`)
under which the next value-affecting action preserves the floor.
Carrying `Guard` as an explicit parameter (not a frame field) keeps
the schema minimal: slices without a basis story simply do not define
an instance. Only Stale does in this paper's substrate.

### 3.3 Three specimens

The three slice modules each instantiate the frame and exhibit a
distinct failure mode for branch-local bridge evidence at
reconciliation.

#### 3.3.1 Budget — shared-resource failure

`BudgetMerge.lean` carries a state record
`BudgetState := { used, cap : Nat }`, a transition
`run s (spend n) := { s with used := s.used + n }`, and the viability
value

```
value s := if s.used ≤ s.cap then 1 else 0.
```

This is *viability-as-value*, not remaining budget; the latter would
make every spend locally value-decreasing and collapse the specimen.
Both layers are maximal in this slice: the per-step bridge is
maximal (Axis 1's `MaximalBridge` predicate holds on `budgetEnv`),
and the merge admissibility predicate is itself maximal at the merge
layer — `BudgetMergeOk a b ⟺ a.used + b.used ≤ a.cap ⟺ value(merge a
b) = 1`. The value-layer necessity theorem `budget_merge_viable_iff_admissible.mp`
therefore holds *definitionally* rather than as arithmetic content.

This makes Budget's role precise. Its substantive contributions are
two-fold: it exhibits non-emptiness of the weak-but-not-strong family
(the counterexample below), and it demonstrates that the gating
pattern survives maximal gates at both layers without degenerating
into "gate = preservation restated." Budget is not a witness for
slice-indexed necessity content; that is Stale's role (§3.5).

The merge is honest additive reconciliation:

```
merge a b := { used := a.used + b.used, cap := a.cap }.
```

The admissibility predicate is
`BudgetMergeOk a b := a.used + b.used ≤ a.cap`. The frame is
`budgetFrame` (`Param = Unit`). Sufficiency is
`budgetFrame_restores : MergeRestoresValue budgetFrame`, discharged
through `budget_merge_viable_iff_admissible.mpr`. The trajectory form
`budgetFrame_composes` lifts the result through `BridgedTraj`
framing.

The negative counterexample is `locally_bridged_fragments_can_merge_to_value_loss`
(`BudgetMerge.lean`): two locally bridged trajectories, each spending
within a viable margin (6 ≤ 10, 6 ≤ 10), merge into
`used = 12 > cap = 10` — globally non-viable. The bridge is local to
each branch's view of the budget. It does not see joint usage against
the shared cap. `BudgetMergeOk` is the missing predicate; in its
absence, the locally-bridged-but-non-admissible merge is a weak
object outside the strong family.

The failure shape is *spatial / aggregative*: honest local margins
sum past a shared cap. Scope insufficiency, not epistemic
impossibility. A bridge with global allocation context could
anticipate it; branch-local bridges cannot.

#### 3.3.2 Stale — temporal failure

`StaleEvidenceMerge.lean` carries a state record

```
structure TimedState where
  valueOk : Bool
  evidenceExpiresAt : Nat
  now : Nat
```

and the viability value `value s := if s.valueOk then 1 else 0`. The
merge operator is parameterized by reconciliation time:

```
mergeAt t a b := { valueOk := a.valueOk && b.valueOk,
                   evidenceExpiresAt := min a.evidenceExpiresAt b.evidenceExpiresAt,
                   now := t }.
```

The merged horizon is the conjunctive minimum; the merge time is the
parameter `t`. The freshness predicate is
`evidenceFresh s := s.now ≤ s.evidenceExpiresAt`. Staleness is
*computed* from the interaction of inherited horizon and
reconciliation time, not stamped by the operator:
`mergeAt_fresh_iff_within_inherited_horizon` confirms the merge is
fresh exactly when `t` is within both horizons.

The bridge in this slice is *non-maximal* — strictly stronger than
value preservation, demanding freshness *and* preservation. The slice
is the first to exercise the substrate's non-maximal-bridge path
that Budget and Conflict (both maximal) leave untested. The
admissibility predicate is
`StaleMergeOk t a b := t ≤ min a.evidenceExpiresAt b.evidenceExpiresAt`.
The frame is `staleFrame` (`Param = Nat`).

The negative counterexample is `locally_bridged_branches_can_merge_with_stale_evidence`
(`StaleEvidenceMerge.lean`): two locally bridged trajectories, each
valid at action time (`now = 5`, horizon = 10), reconciled at
`t = 12` — staleness is computed at the merged endpoint, since
`12 > min(10, 10)`. The bridge is local to each branch's view of
time. It does not see future reconciliation time. `StaleMergeOk` is
the missing predicate.

Note what the negative counterexample does *not* say: the merged state stays
viable (`merged_value_preserved`). The failure isolated by this slice
is freshness non-portability, not value loss. This is where Stale
departs from Budget and Conflict, and it is why the substrate carries
a basis layer (§3.4) in addition to the value layer.

The failure shape is *temporal*: honest local witnesses fresh at
action time are reused at a reconciliation time outside their
horizon. Scope insufficiency in the time dimension rather than the
resource dimension.

#### 3.3.3 Conflict — reconciliation-policy failure

`MergeConflict.lean` carries a state record
`MergeState := { owner, clean }` and admissibility predicate
`ConflictMergeOk a b := compatibleOwner a.owner b.owner`. The merge
writes `clean := false` directly on incompatible owners — the failure
is generated by the operator's *own* policy rather than by either of
the two branch-local-scope failures (spatial, temporal) the suite
already names.

The slice is preserved as the degenerate-corner sibling specimen for
merge-policy admissibility. The frame is `conflictFrame`
(`Param = Unit`); sufficiency is
`conflictFrame_restores : MergeRestoresValue conflictFrame`,
discharging through `conflict_merge_viable_iff_admissible.mpr` plus
cleanness recovery from input viability. The bridge is maximal.

The negative counterexample is `locally_bridged_fragments_can_merge_to_value_loss`
(`MergeConflict.lean`): the policy-loss specimen. It is included in
the suite for completeness and to make explicit that one of the three
negatives is qualitatively different — generated by the merge
operator itself, not by what either branch can see. Calling out the
corner is what fences off the "all merge failures are policy
failures" reading.

### 3.4 The basis layer (Stale only)

Slice 1's value-layer instantiation is *trivial*: under viable
inputs, the conjunctive merge `valueOk := a.valueOk && b.valueOk`
preserves `value = 1` regardless of `StaleMergeOk`. The `_ok`
hypothesis is unused in the proofs of `staleFrame_restores` and
`staleFrame_composes`. The asymmetry is the diagnostic, not a bug.
The substrate names it directly: Slice 1's load-bearing content lives
at the *basis* layer — the precondition (`evidenceFresh`) under which
the next freshness-gated action preserves the value floor — not at
the merge-boundary value layer.

Three theorems make the basis layer non-trivial.

`staleFrame_restores_basis` instantiates
`MergeRestoresBasis staleFrame evidenceFresh`: `StaleMergeOk` at the
boundary implies `evidenceFresh` at the merged endpoint. The
freshness conjunct earns its keep here exactly because it was unused
at the value layer.

`useEvidence_preserves_iff_fresh` mirrors the substrate's
`GuardCollapse.lean` analog inside Slice 1's own model: on the
freshness-gated action `useEvidence` from a viable state, value
preservation is logically equivalent to `evidenceFresh`. This is the
key observation that prevents promoting freshness to a parallel
observable. Freshness *functions as a guard* on the value-affecting
action; it does not stand alongside value as an independent defended
quantity.

`stale_basis_carries_useEvidence_value` chains the two:

```
StaleMergeOk  →  evidenceFresh (merged)  →
                 value preserved by useEvidence (merged).
```

Merge-boundary admissibility gates value preservation on the next
freshness-gated step at the merged endpoint. The basis layer pays
rent.

The single-defended-observable discipline survives this layer, but
the reasoning needs to meet the standard §5 sets. The iff theorem
`useEvidence_preserves_iff_fresh` does establish a logical
equivalence between freshness and value preservation on the gated
action — so calling freshness "a `Prop` not a `σ → Nat`" is a
typing observation, not yet a structural claim. The structural
claim is that the equivalence is *temporally local*: it holds at the
moment the freshness-gated action is taken from the merged endpoint.
Freshness is the *precondition selector* on the single defended
quantity (value), ranging across a temporal boundary; it picks out
which states `useEvidence` will leave value-preserving. It is not a
second quantity defended at the same instant. The basis layer
formalizes selection across a temporal boundary, not parallel
defense at a single instant — which is the §5-grade reading of the
single-observable discipline, not a typing slogan.

### 3.5 When merge admissibility is necessary — schema, not single theorem

Sufficiency runs the direction `MergeOk → preservation`. Necessity
runs the dual, `preservation → MergeOk`. Together they yield the
per-slice characterizations. The substrate exposes both directions at
the frame level:

```
def MergeOkNecessaryAtValue (F) : Prop :=
  ∀ p a b, E.value (F.merge p a b) = 1 → F.MergeOk p a b.

def MergeOkNecessaryAtBasis (F) (Guard) : Prop :=
  ∀ p a b, Guard (F.merge p a b) → F.MergeOk p a b.
```

The per-slice outcomes:

- *Budget* instantiates `MergeOkNecessaryAtValue`
  (`budgetFrame_value_necessity`). The substrate's
  `budget_merge_viable_iff_admissible.mp` carries the implication
  directly: a viable merged endpoint forces combined usage within the
  shared cap.
- *Conflict* instantiates `MergeOkNecessaryAtValue`
  (`conflictFrame_value_necessity`), unconditionally. A viable merged
  endpoint forces the merge into the compatible branch, since the
  incompatible branch writes `clean = false`.
- *Stale fails `MergeOkNecessaryAtValue` positively*
  (`staleFrame_value_necessity_fails`). The witness is concrete:
  `aEnd`, `bEnd` reconciled at `t = 12`. Both branches viable, merged
  value preserved (Boolean conjunction), yet
  `StaleMergeOk 12 aEnd bEnd` reduces to `12 ≤ 10`, false. The value
  layer carries no freshness information; necessity cannot flow that
  direction.
- *Stale instantiates `MergeOkNecessaryAtBasis evidenceFresh`*
  (`staleFrame_basis_necessity`). Freshness at the merged endpoint
  forces `StaleMergeOk`. The basis layer is the right home for
  Stale's necessity precisely because freshness, not value, is what
  `StaleMergeOk` controls.

The verdict is that no single generic necessity theorem covers all
three slices at the same layer. The honest formulation is
*slice-indexed necessity at the layer that carries the slice's
content*:

```
Budget   (Slice 0):   value-layer characterization  (value ⟺ MergeOk)
Stale    (Slice 1):   basis-layer characterization  (Guard ⟺ MergeOk)
Conflict (Slice 2):   value-layer characterization  (value ⟺ MergeOk).
```

The asymmetry IS the value-layer sufficiency proof's diagnostic
("`_ok` is unused"). Forcing Stale into a single generic value-layer
necessity would require either distorting the frame with a per-slice
layer indicator or distorting Stale by adding value semantics to
`mergeAt` that the slice does not have. Both are rejected. The schema
is honest at the cost of being a schema. *The calculus body is the
per-slice characterization pattern at the slice's appropriate layer*,
not a forced cross-slice value-layer iff.

This is consistent with the cross-axis structure §4 lifts off: both
refuse to collapse into a single grand statement, and the refusal is
what keeps both honest.

### 3.6 Summary

The composition layer factors into a weak family of locally bridged
trajectory pairs and a strong family of merges admitted by `MergeOk`.
The two families are related by the forgetful erasure of the merge
witness. Soundness is a per-slice projection — at the value layer for
Budget and Conflict, at the basis layer for Stale — through `MergeOk`
plus separately-carried viability hypotheses. Necessity is the dual
direction, slice-indexed at the same per-slice layer; Stale's
value-layer necessity fails positively, which is the diagnostic that
justifies the basis-layer formulation rather than a gap to be closed.

Non-emptiness of the weak-but-not-strong family is exhibited per
slice: `locally_bridged_fragments_can_merge_to_value_loss` (Budget
and Conflict), `locally_bridged_branches_can_merge_with_stale_evidence`
(Stale). Each is a concrete witness that branch-local bridge evidence
— alone — does not survive reconciliation.

The three specimens are not coordinate failure modes. Following the
substrate's epistemic weight, the three slices play distinct roles.
*Stale* is the load-bearing case: the only non-maximal bridge, the
only basis-layer instantiation, the only positive necessity failure
at the value layer (`staleFrame_value_necessity_fails`). *Budget* is
the maximal-at-merge bracket — `BudgetMergeOk ⟺ value(merge a b) =
1` makes the value-layer necessity definitional rather than
content-bearing; Budget's contribution is non-emptiness of
weak-not-strong and the demonstration that the gating pattern
survives a maximal merge gate. *Conflict* is the policy-loss
fence-post, included so the reader cannot read the suite as "all
merge failures reduce to policy decisions." The surface taxonomy
(spatial / temporal / policy) is pedagogy; the substrate roles are
witness / load-bearing case / fence-post.

Two findings from this section are structural for the paper's
overall framing.

First, *operation-specificity is structural*. The §2 gate (`bridge`)
and the §3 gate (`MergeOk`) cannot be collapsed into a single
abstract step. Transition and merge are different operations; the
joint conditions that make composition meaningful are not the same as
the conditions that make a transition value-sound.

Second, *necessity is slice-indexed, not universal*. Even within a
single axis, the layer at which `MergeOk` characterizes preservation
depends on what the slice's content actually controls. A schema with
per-slice instantiations is honest; a forced single cross-slice iff
is not.

These two findings are what §4 must address when it considers the
boundary-witness schema as a candidate keystone — and what it must
refuse to do.

## §4. The boundary-witness schema, and why it isn't the keystone

The patterns of §2 and §3 share structural shape: each axis carries a
*weak* family (`AuthStep` for Axis 1, locally bridged trajectory
pairs for Axis 2) and a *strong* family obtained by adjoining a gate
witness (`SafeStep` for Axis 1, the strong pair adjoining `MergeOk`
for Axis 2), related by a forgetful map; non-emptiness of the gap
predicate (per axis) produces weak objects outside the strong
family's image. The natural move is to ask whether this shared shape
is itself the keystone — whether there is a single abstract theorem
the two axes instantiate.

`BoundaryWitness.lean` makes the shared shape formal. It types both
axes against one signature and proves that each carries a boundary
obstruction in schema form. Then it shows, with the same
explicitness, that the schema is *not* the keystone.

The argument has three parts. First, the schema is honest about what
it carries: a forgetful map with a missing image point. Second, that
property by itself is too weak to discriminate the bridge and merge
gates from arbitrary contentless maps — `Nat.succ` has it. Third,
re-leveling to sections does not rescue the schema: classically, the
section reformulation is equivalent to non-surjectivity. The
keystone's actual content lives elsewhere, in the per-axis
value-soundness theorems that the schema cannot factor through.

This section is the load-bearing rhetorical move of the paper.
Foregrounding it last — after the per-axis content is on the table —
is deliberate. Leading with the schema would invite a reader to form
"this is just non-surjectivity dressed up" before they see the
per-axis value-soundness that rescues the result. Arriving at the
schema after Axes 1 and 2 lets the thinness of the schema-alone
reading be the deliberate deflation move rather than a bad first
impression to dig out of.

### 4.1 The shared signature

The schema is a record:

```
structure ForgetfulWitness where
  Weak   : Type
  Strong : Type
  forget : Strong → Weak.
```

`InImage F w := ∃ s, F.forget s = w` names the forgetful image; the
obstruction is

```
BoundaryObstruction F := ∃ w, ¬ InImage F w.
```

A weak object outside the strong family's forgetful image.
Tautological as stated. The content, if there is any, has to come
from the instantiations.

### 4.2 Both axes instantiate the schema

Axis 1 fixes a state `s` and reads the schema at

```
axis1Forgetful E s := { Weak := AuthStep E s,
                        Strong := SafeStep E s,
                        forget := SafeStep.toAuthStep }.
```

The non-emptiness theorem is

```
theorem axis1_boundary_obstruction
    (hgap : AuthorizationBridgeGap E) :
    ∃ s, BoundaryObstruction (axis1Forgetful E s).
```

The witnessing state and step come from the env-level gap; the
schema's no-preimage clause is exactly
`no_safeStep_for_unbridged_authStep` after definitional unfolding.
The schema does not strengthen §2's atomic obstruction; it
re-expresses it under the shared signature.

Axis 2 instantiates at the Budget slice. The weak object is a pair of
locally bridged branches from a common start state; the strong object
adjoins `BudgetMergeOk`:

```
structure WeakBudgetBranches where
  s, sA, sB : BudgetState
  branchA : BridgedTraj budgetEnv s sA
  branchB : BridgedTraj budgetEnv s sB

structure StrongBudgetBranches where
  s, sA, sB : BudgetState
  branchA : BridgedTraj budgetEnv s sA
  branchB : BridgedTraj budgetEnv s sB
  ok      : BudgetMergeOk sA sB
```

The forgetful map drops `ok`, and the obstruction theorem

```
theorem axis2_budget_boundary_obstruction :
    BoundaryObstruction axis2BudgetForgetful
```

uses the 6 + 6 > 10 specimen from §3.3.1: the weak pair from
`aliceTraj` and `bobTraj` has no strong preimage, because any such
preimage would have to supply `BudgetMergeOk aliceEnd bobEnd`, which
is `12 ≤ 10`, false. Stale and Conflict could be wired into the same
shape by the analogous construction; only Budget is minted in the
substrate, as the non-forced first specimen that confirms the
wiring works.

This is the cross-axis structural similarity made formal: both axes
type against `ForgetfulWitness`, and both carry a
`BoundaryObstruction` whose witness is the per-axis gap.

### 4.3 The schema is shape, not content

`BoundaryObstruction` says a forgetful map is not surjective. That is
all it says.

Consider `Nat.succ : Nat → Nat` as a forgetful map
(`Weak := Nat`, `Strong := Nat`, `forget := succ`). It has
`BoundaryObstruction`: 0 is not in the image of `succ`. Or take any
inclusion of a strict sub-type, or any constant map onto more than
one weak value. Non-surjectivity is cheap, and an arbitrary forgetful
map satisfying `BoundaryObstruction` carries no claim about the
structural meaning of the missing image point.

The schema does not distinguish `axis1Forgetful E s` from `Nat.succ`.
Both satisfy `BoundaryObstruction`. But the per-axis substrate
exhibits what `Nat.succ` cannot. §2.6's
`bridge_separates_authorized_steps` is a discriminator at the bridge
candidate level: the non-contamination predicate accepts the genuine
step and rejects the prior poison step on local structural grounds
— refusal that bites on action content. `Nat.succ` has no analog:
its "rejection" of 0 is a counting fact about the image, not a
structural condition on what is being refused. That structural
condition — value-soundness at the per-axis operation — is what the
schema cannot factor through.

A reasonable response is to ask whether a different reformulation
rescues the schema. The natural candidate is a *section* — a uniform
right inverse of the forgetful map. If `forget` has a section, then
every weak object reconstructs to a strong one uniformly; if it does
not, reconstruction is impossible somewhere.

```
HasSection F := ∃ g : F.Weak → F.Strong, ∀ w, F.forget (g w) = w.
```

The section direction lands a clean implication: a section hits every
weak object, so its existence entails the image is everything. The
substrate proves the obstruction-side direction constructively:

```
theorem boundaryObstruction_implies_no_section :
    BoundaryObstruction F → ¬ HasSection F.
```

The converse — `¬ HasSection F → BoundaryObstruction F` — is the
classical equivalence "not surjective iff some point is unhit." The
substrate is classical (`Classical.byContradiction` enters at the
SafetyBridge layer), so over this substrate
`HasSection F ↔ surjective F` and
`¬ HasSection F ↔ BoundaryObstruction F`. The section formulation
names "you cannot reconstruct uniformly" cleanly, but it does not
strengthen the obstruction. *Clarity, not strength*.

`Nat.succ` fails `HasSection` too: any candidate `g : Nat → Nat` with
`succ ∘ g = id` would require `g 0` to be a preimage of 0 under
`succ`, which does not exist. So re-leveling to sections does not
rescue the schema either. The same trivial counterexamples that
defeat `BoundaryObstruction` defeat `¬ HasSection`.

The schema is honest about this. It names the shared shape; it makes
the gap visible under that shape; it does not pretend the shape
itself is the content.

### 4.4 The keystone's actual content

What distinguishes the bridge gate from `Nat.succ` is
`SafetyEnv.preserves`: bridge evidence entails the value floor
(§2.3). What distinguishes the merge gate from any other
non-surjective inclusion is the `*_restores` family: `MergeOk`
entails the per-slice restoration shape at the slice's appropriate
layer (§3.2, §3.4). Both are per-axis. Both are what *makes the gate
value-sound for an operation*. Neither lifts to a `ForgetfulWitness`
field.

The reason for the per-axis split is structural, not editorial. The
value floor in each axis attaches to a different operation: the
transition `run` for Axis 1, the merge `merge` for Axis 2. To lift
value-soundness to a single schema field, one would need a uniform
"operation" type that subsumes both. That is exactly the collapse
§3.6 rejected on independent grounds: transition and merge are
different operations, and the joint conditions that make composition
meaningful are not the conditions that make a transition value-sound.
Forcing a single schema-level value-soundness predicate would either
repeat the cross-slice value-layer iff distortion the necessity
verdict rejected (§3.5), or reintroduce the arity / observable
distortion the substrate already cut.

The honest cross-axis structure is therefore *schema with
value-sound instantiations*, not a single keystone theorem. The
schema is the exposition device. The value-soundness lives per-axis.

Stated positively, the keystone is the per-axis pair of value-sound
gating results — `bridge_implies_safe` for transition, the
`*_restores` family at the slice-appropriate layer for composition —
exposed through but not collapsed into the boundary-witness schema.

### 4.5 The witness gates, it does not enrich

There is a final structural observation about the schema that the
per-axis content underwrites. The forgetful map `SafeStep.toAuthStep`
is *injective*: it drops `bridged : E.bridge s act`, which is a
`Prop`. Proof irrelevance turns two `SafeStep`s with equal
`toAuthStep` into equal `SafeStep`s. Combined with non-surjectivity
(the gap), the picture is: the strong family is a *strict sub-family*
of the weak. The bridge witness does not provide alternative
structure on the weak objects; it picks out the subset of weak
objects on which the transition is value-sound.

The Axis 2 forgetful map carries the same shape by the analogous
proof-irrelevance argument: `forgetBudget` drops the `ok` field,
which is a `Prop`. The strong pair is a sub-collection of the weak
pair, gated by `BudgetMergeOk`.

This is what value-sound *gating* means structurally:

> The witness **gates** (admits a subset of the weak family); it does
> **not** enrich (distinguish within a fiber).

The strong family is not a re-encoded version of the weak family
with extra data hanging off. It is a sub-family — exactly the
sub-family on which the operation is value-sound. The gate is
binary: admit or do not. There is no fiber structure to enrich over.

This pins what the per-axis value-soundness theorems are *doing*.
They are not adding content to the weak objects. They are
characterizing exactly which weak objects belong to the strong
sub-family — by the operation-specific soundness predicate the
bridge or `MergeOk` carries.

### 4.6 Summary

The boundary-witness schema makes the cross-axis structural
similarity formal: both axes carry a `ForgetfulWitness` with a
`BoundaryObstruction`. The schema is honest as exposition. It is not
the keystone.

It is not the keystone because non-surjectivity is too weak.
`Nat.succ` carries `BoundaryObstruction`, and so does any
non-surjective map; reformulating with sections is classically
equivalent and offers no rescue. The bridge gate and the merge gate
are distinguished from contentless maps by value-soundness, which
lives per-axis because the value floor attaches to different
operations. Lifting it into a single schema field would repeat
distortions the substrate has already rejected, twice.

The witness *gates* — admits a subset — rather than *enriches*. The
strong family is a strict sub-family of the weak, gated by an
operation-specific value-soundness condition. That structural fact,
paired with the per-axis value-sound instantiations of the gating
pattern, is what the schema cannot factor through and what the
bounded sub-calculus over Axes 1–2 actually delivers.

The remaining question is the scope fence: when does this story
hold, and when does it break? §5 takes that up.

## §5. Scope: why self-amendment is out

The bounded sub-calculus over Axes 1 and 2 is sound relative to a
specific assumption that the body sections have used without remark.
This section names it, articulates the boundary it draws, and
explains what is deferred.

### 5.1 The fuse: value is external

In every theorem of §2 and §3, the defended value `E.value : σ → Nat`
is a field of `SafetyEnv`. It is a function of state, not a part of
mutable state. The transition `run` updates `σ`; the merge `merge`
updates `σ`; neither updates `value` itself. Soundness theorems —
`bridge_implies_safe`, `safeStep_is_safe`, `bridgedTraj_preserves`,
every `*_restores` instance, every necessity dual — read `value` at
multiple points along a trajectory and assume the function is the
same function at each reading.

This is the bounded paper's fuse:

> Every gate in this paper is sound relative to an externally
> supplied value.

The gates do not promise anything about regimes in which `value` is
among the things being mutated. They do not have to. The substrate
is a `SafetyEnv` whose `value` field is part of the environment, not
part of the state.

One clarification anticipating a reviewer probe. The merge frame's
`Param` can route external information into the state σ — `mergeAt
t` writes `now := t`, and the freshness predicate reads `now`. This
does not breach the fence. The value *function* is fixed; its
*inputs* (the `σ` it reads) vary. Varying the inputs to a fixed
function is not mutation of the function. The seam is whether the
function defining `value` is itself part of mutable state, not
whether `σ` is influenced by external parameters that route through
it.

### 5.2 The wrong seam

A natural way to state the scope fence is to say the paper excludes
the regime "where the evaluator itself mutates." This phrasing is
cleanly dichotomous and reads well. It is also imprecise.

"Evaluator" suggests a metaphysical distinction — what evaluates
versus what is evaluated — that the formalism does not draw. Both
`run` and `value` are fields of `SafetyEnv`; the substrate does not
separately privilege one as the evaluator. A determined reviewer
could press: does not a sufficiently powerful composition perturb
`value`, given how much state the merge operators are allowed to
touch? The dichotomous answer ("composition does not mutate the
evaluator") sounds principled but answers the wrong question. It
invites the rejoinder that the line between "evaluator" and
"evaluated" is rhetorical, not structural.

### 5.3 The right seam

The actual seam is structural, not metaphysical. `value` is a
function of `σ` defined in `SafetyEnv`, but it is not itself a field
of `σ`. The bounded paper's transitions and merges perturb `σ`; they
do not perturb `value`. Soundness is sound relative to *this fact
about which things live where*, not relative to any general claim
about the power of composition.

The bounded paper genuinely closes against the regime in which
transitions (or merges) reach into the function that defines `value`
— making `value` itself part of what mutates. Press defence against
the composition-power reading is, accordingly, not about
composition's power. It is about what is and is not in mutable
state.

Stated this way, the fence is narrow and structural. A merge that
perturbs branch state, however baroque, does not perturb `E.value`.
A transition that updates internal records, however many, does not
update `E.value`. The seam is whether the gated operation's effect
type includes `value`, not whether the operation is "evaluator-like"
in some informal sense.

### 5.4 What stays in scope

Under this seam, several intuitively powerful regimes stay in scope.

Composition complexity stays in scope. The merge frame is
parameterized over an arbitrary state space; merges can be
arbitrarily expressive in their state updates without breaking the
fence, as long as `value` reads `σ` without itself being modified.

Policy evolution at the bridge or `MergeOk` layer stays in scope.
These are `Prop`-valued predicates that may differ across
environments; nothing prevents a `SafetyEnv` from carrying a
different `bridge` than another. The fence holds because `bridge` is
a field of `SafetyEnv`, not of `σ` — replacing it across environments
is environmental variation, not state mutation.

Externally driven changes to authorization stay in scope, for the
same reason: `Allowed` is environmental, not stateful.

The fence excludes exactly the regime where the gated operation's
effect on `σ` indirectly changes what `value` returns at later
states — by changing the function used to compute `value`, not just
the inputs it reads. That requires `value` to be part of mutable
state, not part of the environment. The bounded paper's `SafetyEnv`
makes that requirement impossible to satisfy.

### 5.5 The future synthesis

What is deferred is *what happens to value-soundness when `value` is
no longer external* — and, more broadly, when the assumptions the
bounded gates depend on become themselves subject to gating.

The shape of that future synthesis is open. It may turn out to be
one calculus or several. Among the regimes it would have to address:
amendment of the value function itself; retroactive legitimation,
where a later policy change attempts to bridge an earlier
inadmissible action; self-certifying amendment, where the rule
authorizing amendment is itself amended by the same act; mutation of
who has standing to bridge or testify; substitution of the value
basis under crisis conditions; and reflective adoption of an
obligation without legitimation of its origin. The bounded paper
does not absorb any of these. Each requires either `value` to be
part of mutable state, or the policy predicates the gates read to
undergo gated change across a temporal boundary the substrate does
not reason about. Neither extension is silent.

The title for that future synthesis is reserved. The current paper
closes a bounded sub-calculus over Axes 1 and 2; a coherent future
formalization of the seam may be developed before a runtime consumer
exists and may lead later implementation. Claiming the synthesis in
this paper would still be premature, in the precise sense that the
substrate needed to discharge that broader claim does not currently
exist.

### 5.6 Summary

The bounded sub-calculus's seam is structural: `value` is
environmental, not stateful. Every soundness theorem reads `value`
against a function that the gated operations cannot reach.

The wrong way to state the fence — "the evaluator does not mutate" —
invites a rejoinder that the evaluator / evaluated distinction is
rhetorical. The right way — "`value` is not in mutable state" — is
precise enough to hold under press.

The future synthesis concerns the regime in which `value` is no
longer external. Its shape and scope may be developed as soon as a
coherent statement, model, or countermodel is available; a forcing
case may prioritize or stress-test that work but is not permission to
begin it. The title remains reserved until the broader claim is
actually earned. The current paper closes what it claims to close,
and no more.

## §6. Related work

This is a working-draft pass. The paper sits at the intersection of
several literatures whose treatment varies in depth across the
subsections below; specific citations marked `[ref]` are placeholders
for the publication pass.

### 6.1 Authorization versus safety in formal verification

The wound this paper opens against is the gap between authorization
and value preservation: an authorized step may strictly decrease a
defended value (§2.4). The general shape — permission-to-act
distinct from effect-on-defended-property — is well-rehearsed in
formal verification.

Capability-based access control [ref: foundational capability
literature, e.g., Miller's *Robust Composition*; Dennis–Van Horn;
the OCAP tradition] separates authority-as-reference from
effect-as-execution, but typically grants the capability *as* a
license over a known interface, not as a separate witness of
value-preservation. The bridge witness in §2 occupies the latter
slot: authorization is supplied by `Allowed`; the value-preservation
evidence is supplied separately by `bridge`. The two cannot
substitute for each other.

Information-flow and non-interference [ref: Goguen–Meseguer;
Sabelfeld–Myers survey] reason about whether sensitive data leaks
across operations and resemble the bridge framing more closely:
both ask whether an externally specified property is preserved by
the operation. The paper's choice to treat the externally specified
property as a defended-value floor rather than as an interference
relation is venue-specific to the broader Δt program (§6.3); the
underlying separation of concerns is shared.

Separation logic [ref: Reynolds; O'Hearn; Calcagno–O'Hearn–Yang]
reasons about local effects against global resource state. The
*frame rule* is exactly the move that branch-local bridges in
§3.3.1 fail to support. The Budget slice's negative counterexample is a
small-scale demonstration of the frame-rule failure pattern in a
substrate that does not adopt the separation-logic discipline.

### 6.2 Merge semantics and reconciliation

The three slice modules in §3.3 instantiate failure modes whose
individual shapes are familiar from distinct literatures, even when
the combined framing (per-slice value-soundness gating) is not.

The Budget slice is the *additive-resource specimen* — joint usage
against a shared cap. The shape is kin to resource semantics under
separation logic [ref: as above] and to budget-tracking systems in
concurrency theory; the merge failure (`6 + 6 > 10`) is a small
instance of the joint-resource-violation pattern that arises
whenever local frames are reconciled against a shared resource
budget.

The Stale slice is the *temporal specimen* — local witnesses fresh
at action time, stale at reconciliation. The shape is kin to vector
clocks and version vectors [ref: Lamport; Fidge; Mattern] and to
causality-tracking systems generally. The paper's contribution is
not the freshness predicate itself but the *layer-aware
admissibility* observation: freshness gates the *next*
value-affecting action, not value preservation at the merge
boundary, and this layer asymmetry is what the substrate's basis
layer (§3.4) formalizes.

The Conflict slice is the *reconciliation-policy specimen* —
operationally adjacent to the convergence-under-merge analyses in
CRDT and operational-transformation literatures [ref: Shapiro et
al. on CRDTs; Ressel–Nitsche-Gunzenhäuser on OT]. The paper
preserves it as the degenerate corner (§3.3.3), explicitly to fence
off the reading that all merge failures reduce to policy decisions.
The substantive shapes the suite isolates are the spatial (Budget)
and temporal (Stale) specimens.

### 6.3 The broader Δt program

This paper sits within a series of working notes on temporal
coherence and authority bounds (Beck, papers P01–P27 in the Δt
framework series, Zenodo collection *delta-t-framework*). The Lean
substrate referenced throughout — `SafetyBridge.lean`,
`ParameterizedMerge.lean`, the per-slice modules,
`BoundaryWitness.lean` — lives in `LeanProofs/Admissibility/` and
is shared kernel across the series.

Specific positioning within the series. The foundational failure
geometry and scope-fence discipline of Paper 22 [ref] anchors the
substrate the bounded sub-calculus extends; the explicit scope
fence in §5 inherits from the discipline established there.
Unauthorized durability (Paper 18) [ref] supplies the
constitutional reading for the write-barrier discipline behind the
`Allowed` / `bridge` separation in §2.

The bounded sub-calculus formalized here is one slice of a broader
program candidate (boundary calculus / admissibility cybernetics)
whose final form is not pre-decided. The current paper does not
claim the program title; it instantiates a bounded fragment under
its substrate, and the program-level question of "what is the full
shape of the cross-axis story" remains an open program note.

### 6.4 Substrate context

The Lean substrate is Lean 4 core, with no Mathlib dependency. The
choice is deliberate: the paper's claims are about kernel-level
properties of records and `Prop`-valued predicates, and nothing in
the body requires the broader Mathlib infrastructure. §4's schema
reads informally as a forgetful-functor / right-inverse
construction, but the substrate does not import category theory;
the forgetful framing is exposition over concrete record types.

The substrate's classicality is concentrated in
`Classical.byContradiction` used inside `SafetyBridge.lean` (cf.
§4.3's classical-equivalence observation about `HasSection`). The
constructive direction of `boundaryObstruction_implies_no_section`
is preserved as a typed theorem; the converse is the classical
equivalence the substrate inherits rather than proves.

The bounded paper's modules are deliberately not promoted to the
public 1.0 surface (`CalculusOne.lean`) of the broader series. The
modules referenced — `ParameterizedMerge.lean`,
`BoundaryWitness.lean`, the slice modules — are scratch / candidate
under the substrate's tooltheory discipline, not minted. Promotion is
a separate custody decision: paper publication or downstream citation
identifies an intended contract but does not itself establish runtime
conformance. Conformance requires an explicit mapping plus runtime
evidence or a refinement proof.

## §7. Conclusion

The bounded sub-calculus formalized in this paper closes a fragment
of admissibility over two operations: transition and composition. The
pattern is the same at both axes — weak admissibility objects become
value-sound only when admitted by an explicit witness — and is
instantiated per axis through different gate predicates. At the
transition layer (§2) the gate is the bridge witness, and the
soundness theorem is `SafetyEnv.preserves`. At the composition layer
(§3) the gate is `MergeOk` and the soundness statement is the
per-slice `*_restores` family, layer-indexed at the slice's
appropriate layer — value layer for Budget and Conflict, basis layer
for Stale. The cross-axis structure is the shared *value-sound
gating* pattern, made formal as a schema in §4 and shown there to be
honest as exposition but too weak to carry the keystone's content on
its own. The content of the keystone is per-axis, because the value
floor attaches to different operations per axis; this is what the
boundary-witness schema cannot factor through.

Three findings from the bounded sub-calculus are load-bearing for how
the result composes with the broader program. *Operation-specificity
is structural*: transition and merge are different operations, and
collapsing them into a single abstract step erases the joint
conditions that make composition meaningful. *Necessity is
slice-indexed*: even within a single axis, the layer at which
`MergeOk` characterizes preservation depends on what the slice's
admissibility actually controls, and forcing a single cross-slice
iff distorts the substrate. *The witness gates, it does not enrich*:
the strong family is a strict sub-family of the weak, picked out by
the operation-specific soundness condition, not a re-encoded version
of the weak family with extra fibers.

What the paper does not close against is the regime in which the
value function itself becomes part of mutable state. The fence
stated in §5 is structural rather than metaphysical: it draws the
line at *what is in mutable state*, not at the cleaner-but-imprecise
"transition versus evaluator" distinction. Under this fence, several
intuitively powerful regimes — composition complexity, policy
evolution at the bridge or `MergeOk` layer, externally driven
changes to authorization — remain in scope, while the regime in
which `value` (or the policy predicates value-soundness depends on)
becomes itself subject to gating is deferred. The future synthesis
that would close that regime is the artifact for which the *maximal
admissibility calculus* title is reserved. The current paper does
not preempt that synthesis; it closes the bounded fragment under an
external, non-mutable value function, and no more.

The Lean substrate referenced throughout — `SafetyBridge.lean`,
`ParameterizedMerge.lean`, the per-slice modules,
`BoundaryWitness.lean` — together form a self-contained kernel for
the two-axis fragment. Promotion to the broader series' public
surface remains a separate custody decision, per §6.4; Scratch may
lead implementation but may not testify for or pin production. The
paper's claim is the bounded fragment, formalized. A coherent broader
claim may be formalized before a consumer exists, while its eventual
title and public promotion remain contingent on actually earning the
broader claim and its conformance evidence.

## Edits applied (audit trail)

Source: ChatGPT's sharper-variant abstract and contribution list.
Edits per Claude-web review:

- **Abstract paragraph 2 (added).** *"One specimen (stale evidence)
  gates at the level of basis for future value rather than present
  value; freshness is treated as a guard for value-preserving
  continuation, not as a second defended observable."* Restores the
  freshness-collapse finding that the sharper variant had dropped.
- **Abstract paragraph 3 (sharpened).** *"Non-surjectivity and
  no-section claims — classically equivalent here — are too weak:
  they hold for trivial maps such as the successor on the naturals."*
  Makes the weakness demonstrated rather than asserted; a reviewer
  who notices the schema is near-tautological sees the author
  noticed first.
- **Contribution 3 (necessity-clause alignment).** Added *"with
  necessity demonstrated per operation and, for composition, per
  case rather than as a single universal law."* Aligns with the
  `ParameterizedMerge.lean` schema-not-single-theorem necessity
  verdict so abstract and body agree before anyone diffs them.
- **Contribution 4 (scope-mechanism added).** Added *"every gate is
  sound relative to an externally supplied value, and self-amendment
  is precisely the regime where that externality fails."* Makes the
  fence principled rather than stipulated; names the actual seam
  (whether `value` is in the mutable state) rather than a
  metaphysical evaluator-vs-evaluated line.

### Body-pass review revisions (post-§1 read-through)

External review surfaced three seam-integrity issues plus light
prose drift. Patches applied:

- **Abstract paragraph 4 (rewritten).** Purged "fixed evaluator" /
  "evaluator itself mutates" framing in favor of "defended value
  function is environmental rather than mutable state" and
  "self-amendment — where the value function, or the policy
  predicates value-soundness depends on, become subject to gated
  change." Aligns paper-front matter with §5's seam framing instead
  of contradicting it.
- **Contribution 3 (necessity-clause sharpened).** Replaced
  "necessity demonstrated per operation" with "sufficiency is
  operation-specific; for composition, necessity is characterized
  per slice and at the layer where the slice's content actually
  lives." Avoids reading as "transition bridge is necessary for
  preservation" — which would shoot §2.6's sound-but-not-complete
  corner. Also swaps "expository rather than load-bearing" →
  "expository rather than constitutive" for the schema clause.
- **Contribution 4 (rewritten).** Same purge as abstract ¶4;
  replaces fixed-evaluator framing with "every gate is sound
  relative to an externally supplied value function" and names the
  four candidates for self-amendment (`value`, standing, bridge
  policy, merge policy).
- **§2.5 (AuthPreserves / no-gap conflation fixed).** Original
  text equated "`AuthPreserves E` holds" with "the gap predicate
  fails on every authorized step." Those are equivalent only when
  the bridge is complete; under sound-but-not-complete (which §2.6
  reserves), `AuthPreserves E` can hold while a gap exists.
  Replacement paragraph distinguishes preservation-obligation
  collapse (`AuthPreserves E`) from reconstruction-problem collapse
  (absence of bridge gap) and cross-references §2.6 to preserve
  the sound-but-not-complete corner.
- **§7 ¶3 (conclusion seam).** "Bounded fragment under a fixed
  evaluator, and no more" → "bounded fragment under an external,
  non-mutable value function, and no more."
- **"Load-bearing" reduction.** Three swaps (§3.1, §3.4, §3.6)
  from "load-bearing" → "structural" / "key" / "structural" to
  cut house-style frequency by ~50%. Retained at §2.1, §3.4 (basis
  layer), §4 opener, and §7 ¶2 where the term earns rent.

### Dual-reviewer feedback wave (post-body review)

External review surfaced six additional items. Patches applied:

- **Title** (ChatGPT pick). "Value-Sound Gates for Authorization
  and Composition" → "Value-Sound Gates: Authorization and
  Composition in Lean 4". Keeps Lean specificity, avoids
  overclaiming "calculus," reads as a paper rather than a
  repo / tool note.
- **§3.3.1 Budget reframing.** Claude-web flagged that `BudgetMergeOk
  a b ⟺ value(merge a b) = 1` makes Budget maximal at the merge
  layer (not just at the per-step layer). `budget_merge_viable_iff_admissible.mp`
  therefore holds definitionally rather than as arithmetic content.
  Added explicit acknowledgment; recast Budget's role as
  non-emptiness witness + maximal-merge bracket (substrate-survival
  demonstration), not slice-indexed necessity content.
- **§3.6 role-led reframing.** Added a paragraph leading with
  substrate roles (Stale = load-bearing; Budget = maximal-at-merge
  bracket; Conflict = policy-loss fence-post) under the surface
  spatial/temporal/policy taxonomy. Stops the three specimens
  reading as coordinate failure modes.
- **§3.4 freshness reframing.** Original closing paragraph defended
  single-defended-observable by typing freshness as `Prop` not
  `σ → Nat`. Claude-web flagged this as the typing-slogan move §5.2
  explicitly rejects. Replaced with the §5-grade structural version:
  freshness is a *precondition selector* on the single defended
  quantity across a temporal boundary, not a second quantity
  defended at the same instant.
- **§4.4 positive keystone statement.** Claude-web flagged that §4
  states the keystone only negatively. Added one declarative
  sentence stating the keystone positively: per-axis pair of
  value-sound gating results (`bridge_implies_safe` + `*_restores`
  family at slice-appropriate layer), exposed through but not
  collapsed into the boundary-witness schema.
- **§5.1 Param preemption.** Claude-web flagged that `mergeAt t`
  routes external `t` into `now`, and freshness reads `now`. Added
  one paragraph after the fuse statement clarifying that the value
  *function* is fixed; varying its inputs (via `Param`) is not
  mutation of the function. Pre-empts the "how external is value?"
  probe.
- **"Negative keeper" → "negative counterexample" swap.** Five
  instances in §3.3.1, §3.3.2, §3.3.3, §6.1. Reviewer flagged
  "keeper" as internal-doctrine register that doesn't belong in
  public prose.

- **Deflation-asymmetry fork — fork (a) applied.** §4 deflates the
  schema via `Nat.succ`; original §4.3 asserted that the per-axis
  content is contentful via "evidently doing something `Nat.succ`
  is not." User picked fork (a) per Claude-web's recommendation:
  demonstrate in-paper. §2.6 expanded with the
  `bridge_separates_authorized_steps` discriminator pair and the
  sound-but-not-complete property (substrate's header note: false
  receipt on already-poisoned store is rejected on local structural
  grounds, not on outcome). §4.3 reworked to cross-reference §2.6's
  discriminator instead of asserting via "evidently." Pre-patch
  Lean audit: all cited identifiers exist in `SafetyBridgeWitness.lean`
  (verified via grep) and the module builds clean (verified via
  `lake build`); no new Lean introduced.

### Outstanding from dual-reviewer review

- **§6.1 capability claim sharpening.** Generalization that
  capability literature grants authority "as a license over a known
  interface, not as a separate witness of value-preservation" needs
  specific contrast at backfill (the OCAP crowd will contest the
  reading). Deferred to publication-pass `[ref]` backfill.

## What this draft does NOT do yet

- Does not include `[ref]` backfill in §6 (working-draft citations
  remain placeholders).
- Does not include an abstract / contribution-list reconciliation
  pass against the now-landed body — the abstract and contribution
  list were drafted before §2–§7 and may want minor adjustment
  (e.g., the basis-layer mention in the abstract paragraph 2 should
  now cross-check against §3.4's actual content).
- Does not commit to a venue or page count. Title and venue posture
  remain per [[feedback-axis-1-venue-posture]] (Zenodo / arXiv-quality
  formal note).
- Does not absorb the "for the pocket" Axis-3 spectrum-vs-dichotomy
  reasoning from the spine into the abstract body. That stays in the
  pocket for press defence.

## Next concrete move

§1–§7 are now landed. The draft is structurally complete. Two
remaining passes before the working draft can become a publication
draft:

1. **Abstract / contribution-list reconciliation.** Both were
   drafted before the body and may want minor adjustment to align
   with the now-landed body's exact terminology — particularly the
   basis-layer mention in the abstract (paragraph 2) and the
   slice-indexed necessity clause in contribution 3 against §3.4
   and §3.5's actual phrasing.
2. **`[ref]` backfill through §6.** Specific citations for the
   capability / non-interference / separation-logic clusters
   (§6.1), the vector-clock and CRDT clusters (§6.2), and the
   Δt-series cross-references (§6.3).

Both are mechanical against the landed body and could be done in a
single pass. After that pass, the draft is ready for whatever
review / Lean-substrate audit precedes Zenodo upload per the venue
posture.

## Related records

- Spine: [paper-value-sound-gates-spine-2026-06-01.md](paper-value-sound-gates-spine-2026-06-01.md)
- Keystone verdict: [axis-2-cross-axis-keystone.md](axis-2-cross-axis-keystone.md)
- Axis 2 composition work: [axis-2-composition-boundary.md](axis-2-composition-boundary.md)
- Lean substrate: `~/git/lean/LeanProofs/Admissibility/` (`SafetyBridge.lean`, `ParameterizedMerge.lean`, `BoundaryWitness.lean`)
