# Control-path independence — candidate primitive (2026-05-29)

**Status:** Candidate primitive. Filed at candidate-density per `working/tooltheory/` convention. Names early, ratifies lazily; the Lean module `Admissibility.ControlPathIndependence` is **filed by name, not built**. Build is gated on a concrete forcing case (NQ / Wicket / Governor consumer that needs to refuse an independence claim against an inadmissible basis).

**Provenance:** Multi-model conversation 2026-05-29. DeepSeek seeded a control-theoretic abstraction of a parallel-loop / counter-power model, with Lean-flavored pseudocode. ChatGPT corrected the Lean target and proposed an "architecture linter" framing scoped to `working/`. Claude opus 4.8 on web corrected the linter framing in two directions — sharper kernel connection *up* (this is a basis predicate for binding semantics, not pre-calculus preflight) and sharper scope *down* (the linter is structurally blind to two of the three invariants it implicitly claims to cover). ChatGPT endorsed the correction. This file is the convergent reading.

---

## Compile-probe scope statement (2026-05-30)

Filed at the head of the candidate per the [annex-probe queue](annex-probe-queue-2026-05-29.md)'s gate: *CPI's compile probe is licensed only after this statement holds.* Three questions, three answers.

### 1. What bounded question does the compile probe answer?

> Does the typed shape `Arch + ReachableBy + ComponentInfluencedByOfficial + IndependentAt + InterlockBasis` hold together as a kernel-level basis-revocation candidate — recognizing **architectural** independence (reachability over named path kinds, against a transitive influence relation) as a structural reason `BasisDerivation` can refuse, while keeping the three-axis decomposition non-collapsed?

Green confirms three things:

- The reachability-over-path-kind shape (`ReachableBy sys k a b` inductively closed, separate from `flow`) type-checks as a load-bearing relation, not as decoration.
- `IndependentAt sys k target` defined as *every component reachable to the target along path kind `k` is uninfluenced by the official principal* — the reachability quantifier survives type-checking.
- `InterlockBasis` with one discharged field and two `Prop` obligations elaborates as a structure (the type system *permits* the three-axis split; it does not force the consumer to discharge standing/coupling to construct an `InterlockBasis`).

Red surfaces a kernel-shape gap: if `IndependentAt` can't be stated without smuggling a decider into the kernel, or if `InterlockBasis` collapses the three obligations into one, the candidate's "non-collapsing decomposition" claim is paper, not kernel.

### 2. What is deliberately undischarged, and what carries the obligation?

Two `Prop` fields of `InterlockBasis` are undischarged **by construction**:

| Field | Undischarged because | Carried by |
|---|---|---|
| `standing : Prop` | Historical / dynamic. No fact about `flow`, `influences`, `owner`, `powered`, or `controls` discharges it. Wiring diagrams don't contain track records. | Any downstream consumer (NQ finding, Wicket classification, Governor verdict, CLI). Either the consumer supplies its own witness or it emits the incompleteness certificate. |
| `coupled : Prop` | External coupling to the actuator's authority surface. Not in `Arch`. A welded breaker is structurally indistinguishable from a working interlock at the wiring layer. | Same. Consumer-supplied witness, or the certificate. |

The kernel module **never** provides default-`True` placeholders for either. That is a load-bearing design decision: a `True`-placeholder for `standing` would be a stuck-at-safe interlock dressed as a kernel guarantee — the exact failure mode under test. (Memory: [[feedback-lean-debt-discipline]] *classify before discharging*; vocabulary-deficient claims get `True`-placeholders, but vocabulary-out-of-scope claims get *no* placeholder, not even `True`.)

Two additional categories that the probe does **not** discharge but are not "deliberately undischarged" in the same sense:

- **Decidability of `IndependentAt` over concrete `Arch` instances.** The kernel states what independence means; deciding it for a specific architecture requires `Decidable` instances on `flow`, `influences`, etc. Those are downstream — see §3.
- **Concrete `Arch` constructors / example architectures.** None should appear in the annex. See §3.

### 3. Where does this annex stop being a slice probe and start being an architecture linter — and is that boundary intentional?

The boundary is **intentional, sharp, and load-bearing**. Slice probe vs. architecture linter splits cleanly along three lines:

| Slice probe (in scope) | Architecture linter (out of scope) |
|---|---|
| State what independence means (`IndependentAt` as a reachability predicate over `ReachableBy`) | Decide it for a concrete `Arch` (requires `Decidable` for `flow`, `influences`, `controls`, `owner`, `powered`) |
| Prove the four independence-derivable failure theorems as `¬ IndependentAt → <named bad property>` | Run those theorems against an instantiated `Arch` and emit PASS/FAIL |
| Carry `standing` and `coupled` as undischarged `Prop` obligations | Discharge them or default-`True` them |
| Namespace under `Admissibility.ControlPathIndependence`; no `LeanProofs.lean` import | Public-surface preprint claim, doctrine mint, or CLI integration |
| No example architectures | Concrete examples (the captured-audit-log, the welded breaker, etc.) |

Crossing the line — building a decider, adding example architectures, providing default discharges for standing/coupling, or importing into `LeanProofs.lean` — turns the candidate into the very compliance-checkbox failure mode it is supposed to make visible. The annex must be **structurally incomplete in the same way the consumer's verdict must be structurally incomplete.** That's not laziness; that's the shape under test.

If the build's natural slope pulls it toward decidability or examples, **stop and refile**. A linter is a different artifact from a basis-derivation candidate. The compile probe is licensed for the latter only.

### Why scope-first (not optional)

The [annex-probe queue](annex-probe-queue-2026-05-29.md) flagged this candidate as "different shape, larger than PL or CP." The risk: without the scope statement, the compile drifts. Drift looks like (a) "well, decidability is just one `decide`-tagged instance away" → linter, (b) "the example would make the theorems concrete" → public-surface bait, (c) "default-`True` for standing makes `InterlockBasis` constructible, just leave a comment" → stuck-at-safe.

This statement holds the boundary the queue's five-criterion test cannot hold alone for a candidate of this size.

### Recommended build session (if licensed)

When the operator triggers the compile probe:

1. Drop `Principal`, `Component`, `PathKind`, `Arch`, `ReachableBy`, `ComponentInfluencedByOfficial`, `IndependentAt`, `InterlockBasis` exactly as written in §"Proposed Lean shape" below.
2. Add the four failure-theorem statements from §"Failure-mode-to-theorem table" — bodies may be `sorry` (since `DomesticatedProvisioning`, `CapturedObserver`, etc., are themselves candidate predicates whose meanings are vocabulary-deficient at kernel layer). If they are stated with `sorry`, that is a *vocabulary-deficient* sorry, classified per [[feedback-lean-debt-discipline]]. The annex should label them as such in a comment.
3. Confirm no Mathlib, no `LeanProofs.lean` import, no example architecture, no `Decidable` instance.
4. `lake build LeanProofs.Admissibility.ControlPathIndependence`. Green is contact; not promotion.
5. Update this note's §"Lean annex — built status" (new section) with the compile date, build time, and any deltas from the sketch.

The compile remains gated on this statement holding. If the answers to §1–§3 above no longer match the candidate's actual shape, **rewrite this section before building, not after.**

---

## The kernel connection

The deciding insight: **control-path independence is not pre-calculus preflight. It is one concrete piece of the binding-semantics basis the calculus has been carrying as an open gap.**

Recall the open `BasisDerivation` slot in `~/git/lean/LeanProofs/Admissibility/Derivation.lean`. The current state: the kernel verifies that a basis-derivation function *exists* and the verdict pipeline *runs*, but it has no concrete `BasisDerivation` instance recognizing structural reasons a check should fail. The deferred TODO in `StateTransition.lean` names `revoked_basis_never_authorized` as the first revocation-shaped consequence; the slot for additional structural revocations is open.

Independence of the checker from the checked is one such structural revocation reason. **A captured checker — one whose sensing, memory, power, or refusal path is controlled by the thing it is supposed to check — cannot mint an admissible check.** That is a basis-revocation condition recognizable from the dependency graph alone, without temporal history or external coupling information. So it belongs in the kernel for the same reason `revoked_basis_cannot_be_authorized_step` belongs there: it names a structural condition under which the verdict cannot be `admissible`.

Filing this as "boring preflight" understates it. It is a candidate `BasisDerivation` lemma in linter clothing.

## The three-axis decomposition

DeepSeek's six failure modes (service domestication, carrier capture, compliance-checkbox substitution, loss of standing, authorization composing, welded breaker) do **not** unify into a single invariant. They cluster into three:

| Axis | Property | Verifiable how | Covers (of DeepSeek's six) |
|------|----------|----------------|----------------------------|
| **Independence** | Checker's signal / power / logic / refusal paths are not influenced by the checked party | Static graph reachability over named path kinds | service domestication; carrier capture; compliance-checkbox substitution; authorization composing (4 of 6) |
| **Standing** | Checker has track record / credibility for its outputs to be weighted non-zero | Dynamic / historical; time series of past findings vs outcomes | loss of standing (1 of 6) |
| **Coupling** | Failed checks attach to teeth (real liability surface, not a welded breaker) | External; depends on whether the actuator the interlock controls has force | welded breaker (1 of 6) |

Only **independence** is decidable from the architecture alone. **Standing** and **coupling** are not — no wiring diagram contains the information needed to discharge them.

The unification temptation says: "all six are independence failures, broadly construed." The correction: standing and coupling are *orthogonal* invariants, and forcing them into independence is the kind of unification-by-fiat that lets a green linter sign off on a captured checker because the captured checker happens to have its own power supply.

## The incompleteness-certificate discipline (load-bearing product warning)

Any consumer of an independence check (CLI, dashboard, audit tool, Governor verdict, NQ finding) **must** declare its own incompleteness in the verdict:

```
independence: PASS
standing:     NOT TESTIFIED AT THIS LAYER
coupling:     NOT TESTIFIED AT THIS LAYER
overall counterpower claim: cannot testify
```

A tool that emits `Independent loop: PASS` is a stuck-at-safe interlock for the concept of counterpower. Green on independence does not entail "real interlock"; it entails "the architecture passes the one check this layer can perform." Any consumer that treats independence-PASS as sufficient for counterpower is doing the *exact* compliance-checkbox failure mode the linter is supposed to detect. Architecture admissibility needs its own `assert_no_authority_claims()` — a linter that doesn't declare its own incompleteness is the stuck-at-safe failure under test.

Implementation: the kernel module surfaces three obligations (`independent`, `standing`, `coupled`); it provides constructors / proofs *only* for `independent`. Standing and coupling stay as `axiom`-shaped obligations the consumer must discharge separately — or explicitly leave undischarged with the certificate above. The kernel does not pretend they don't exist.

## Proposed Lean shape (candidate, not built)

Both prior sketches modeled the wrong object in complementary ways:

- **DeepSeek** erased signal types to `Unit`. Typed ports become decorative; the `dependencyGraph` function had ellipses doing the load-bearing work.
- **ChatGPT** made `Principal = official | parallel | external` a closed inductive — which *bakes the classification into the type system*, exactly the thing the failure-detector is supposed to detect. Carrier capture is `parallel` being covertly `official`; if they are distinct constructors by definitional fiat, the failure mode is assumed away. Also `independentFromOfficial : Component → Prop` as a per-component predicate misses that independence is a *reachability* property — a component owned-by-parallel and powered-by-parallel can still take its input from a sensor traceable to the official principal.

The minimal correct target — **filed as candidate, not implemented**:

```lean
-- Identity types: opaque, not enumerated
structure Principal where
  id : Nat
  deriving DecidableEq

structure Component where
  id : Nat
  deriving DecidableEq

-- Named path kinds — the dependencies that matter, separated
inductive PathKind where
  | signal       -- sensing path
  | power        -- power / resource supply
  | logic        -- interlock criteria / decision rules
  | control      -- ability to mutate component state
  | ownership    -- legal / formal ownership

-- The architecture under test
structure Arch where
  official    : Principal
  owner       : Component → Principal
  powered     : Component → Principal
  controls    : Principal → Component → Prop
  flow        : PathKind → Component → Component → Prop
  influences  : Principal → Principal → Prop  -- decidable, not definitional

-- Reachability over a named path kind
inductive ReachableBy (sys : Arch) (k : PathKind) :
    Component → Component → Prop where
  | refl  {a}     : ReachableBy sys k a a
  | step  {a b}   : sys.flow k a b → ReachableBy sys k a b
  | trans {a b c} :
      ReachableBy sys k a b →
      ReachableBy sys k b c →
      ReachableBy sys k a c

-- Influence under the transitive closure of the influence relation
def ComponentInfluencedByOfficial
    (sys : Arch) (c : Component) : Prop :=
  ∃ p, sys.influences sys.official p ∧
       (sys.owner c = p ∨ sys.powered c = p ∨ sys.controls p c)

-- Independence is a reachability property, not a local one
def IndependentAt
    (sys : Arch) (k : PathKind) (target : Component) : Prop :=
  ∀ c, ReachableBy sys k c target →
       ¬ ComponentInfluencedByOfficial sys c

-- The basis structure — three obligations, only one discharged
structure InterlockBasis (sys : Arch) (target : Component) where
  independent : IndependentAt sys PathKind.signal target ∧
                IndependentAt sys PathKind.power  target ∧
                IndependentAt sys PathKind.logic  target
  standing    : Prop  -- NOT discharged by architecture pathing
  coupled     : Prop  -- NOT discharged by architecture pathing
```

Key design pins:

1. **Opaque `Principal`, decidable `influences` relation.** No closed inductive over `official | parallel | external`. The failure mode under test is precisely that "parallel" can be covertly "official" via the influence relation; that has to be a relation, not a type-system fact.
2. **Reachability, not local check.** A memory component owned-by-parallel and powered-by-parallel can still take its sensor input from a path traceable to the official principal. Per-component predicates miss this; reachability over `PathKind.signal` catches it.
3. **Path-kind separation.** Independence is path-specific. A component can be signal-independent and power-dependent, or vice versa. Conflating them into one "independent" predicate hides the distinct failure modes the four independence-derivable theorems below are meant to express.
4. **Three-field `InterlockBasis` with two explicit gaps.** `independent` is the only field the architecture module discharges; `standing` and `coupled` stay as obligations the consumer must supply (or leave undischarged with the incompleteness certificate). The kernel module *never* provides default-True placeholders for standing or coupling.

## Failure-mode-to-theorem table (candidate, not built)

The four independence-derivable failure modes become theorems of the form `¬ IndependentAt → <named bad property>`:

| Failure mode | Path violated | Theorem shape |
|--------------|---------------|---------------|
| Service domestication | `power` path | `¬ IndependentAt sys power prov → DomesticatedProvisioning sys prov` |
| Carrier capture | `signal` path | `¬ IndependentAt sys signal memory → CapturedObserver sys memory` |
| Compliance checkbox | `logic` path | `¬ IndependentAt sys logic interlock → StuckAtSafe sys interlock` |
| Authorization composing | `signal` path on refusal channel | `¬ IndependentAt sys signal refusal → DecorativeRefusal sys refusal` |

The two non-derivable modes stay as explicit obligations:

| Failure mode | Why not derivable | Obligation kind |
|--------------|-------------------|-----------------|
| Loss of standing | Historical / dynamic; no wiring fact discharges it | `standing : Prop` — consumer-supplied or undischarged |
| Welded breaker | External coupling to actuator authority; not in the diagram | `coupled : Prop` — consumer-supplied or undischarged |

This is the unification I (CC) overclaimed earlier in the conversation, now correctly scoped: *only* the four modes it actually covers, with the other two named as siblings the architecture layer cannot discharge.

## What this candidate does NOT claim

- **Not building the Lean module.** This file names the primitive and pins its shape. Build gates on a forcing case (a concrete consumer that needs to refuse a captured-checker claim). Per "name-early, ratify-lazily," ratification follows recurrence, not speculation.
- **Not the whole binding-semantics gap.** Control-path independence is *one* basis predicate. The binding-semantics gap covers more (temporal revocation, evidence-class mismatch, conflicting precedence, etc.). Independence is a fragment, not a substitute.
- **Not a counterpower proof.** Even with all four independence-derivable failure modes formalized, the kernel module would only certify *necessary architectural conditions* for an admissible check. Sufficient counterpower also requires standing and coupling, both unverifiable at this layer.
- **Not deployable as a standalone "independence linter."** Per the incompleteness-certificate discipline, any consumer that emits `Independent loop: PASS` without naming the standing and coupling gaps is the failure mode under test, wearing a green-checkmark costume.
- **Not paper-ready.** Filed as primitive-candidate. Whether this eventually becomes paper-shaped (addendum to the safety-bridge preprint, a separate NQ-findings paper, or just kernel infrastructure cited from elsewhere) is a downstream decision after a forcing case clarifies the audience.
- **Not a claim about real institutions.** Same fence as the safety-bridge family: this layer is *structural*. Whether a real audit log / monitor / deploy pipeline / oversight body is captured is an empirical question instantiated against the structural predicate, not derivable from it.

## Forcing-case watchlist

Build is gated on at least one of:

- **NQ finding** that needs to express "this audit log is not independent because its write permissions are controlled by the audited service." Witness-family integration is the consumer.
- **Wicket classification** that refuses an admissibility claim because the architecture preflight failed.
- **Governor verdict** that needs to cite "captured checker" as a basis-revocation reason distinct from temporal revocation.
- **Concrete real-world specimen** (auth-provider audit logs writable via the provider's own admin path; deploy pipelines with their own deploy access; monitoring stacks running on the monitored substrate; backup credentials stored in the prod account; secondary regions sharing the primary's IAM root; "external" compliance dashboards populated by self-attested vendor fields) that the kernel needs to refuse.

Until one arrives, the candidate stays here. The Lean module name `Admissibility.ControlPathIndependence` is reserved.

## Adjacent existing work

- **`Admissibility/SurfaceAuthorization.lean`** — cause-specific authority refusal. Sibling in spirit: both name structural reasons a check should fail. Surface-authorization refuses based on the *kind* of action and the surface state; control-path-independence would refuse based on the *dependency graph* of the checker. Composition is open.
- **`Admissibility/Derivation.lean`** `BasisDerivation` structure — this is where a concrete `controlPathIndependentBasis : BasisDerivation` instance would land, if built.
- **`Admissibility/WitnessInvariance.lean`** — structurally adjacent (both about what a witness can / cannot survive), but distinct: WitnessInvariance is about perturbation of an existing witness; ControlPathIndependence is about the architectural admissibility of the witness in the first place. Don't confuse the two.

## Related records

- Spine page: `working/calculus-paper-spine-2026-05-28.md`
- Tier map: `working/tooltheory/calculus-2-tier-map-2026-05-28.md`
- ρ-drop decision: `working/tooltheory/safety-bridge-rho-drop-decision-2026-05-28.md`
- Exit criteria reconciliation: `working/calculus-2-exit-criteria.md`
- Frontier 1 status: `~/git/lean/FRONTIERS.md`
- Laundering-move watchlist (memory): `project-laundering-move-watchlist.md` — *control-path capture* is a new vector worth adding to the watchlist; it is the architectural-laundering sibling of the temporal-revocation laundering already tracked there.
- Kernel slot: `~/git/lean/LeanProofs/Admissibility/Derivation.lean` `BasisDerivation` structure (the deferred concrete-instance slot is the kernel-side anchor for an eventual build).
