# Annex Phase D — Adapter extraction audit (2026-05-26)

**Status:** Audit document for Annex Phase D per `~/.claude/plans/i-want-a-plan-groovy-stardust.md`. Decides whether the duplicated chain-adapter machinery in `RefusalPropagation.lean` should be extracted into a generic construction within the annex. Filed 2026-05-26 after Nightshift adapter landed as fourth chain consumer.

**Posture:** Audit only. No Lean changes during the audit itself. The audit's *conclusion* may authorize a small bounded Lean experiment; that is a separate follow-up step, not part of this document.

---

## Input set

Four chain-shaped consumer namespaces in `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean`:

| Consumer | Substrate domain | Entity inductive |
|---|---|---|
| `NQDependency` | Hardware basis chain | `device_enumeration_witness` → `smart_witness` → `disk_state` |
| `NQOnNQ` | Cross-instance NQ aggregate | `nq_a_receipt_health` → `nq_b_about_nq_a` → `fleet_status` |
| `Labelwatch` | Social-telemetry feature→claim ladder | `labeler_cooccurrence` → `burst_finding` → `coordinated_abuse_claim` |
| `Nightshift` | Deferred-agent reconciliation | `nq_finding` → `reconcile_packet` → `proposal` |

Plus one structurally-distinct fan-in consumer (`NQFanOut`) which does NOT use the chain adapter and is NOT in scope for this audit.

## The duplicated machinery

Each chain consumer duplicates (byte-identical up to type renaming) the following **eight elements**:

1. `inductive State where | observable | refused` (5 lines + deriving)
2. `def Refused (state : Entity → State) (e : Entity) : Prop := state e = State.refused`
3. `def CascadeSound (state : Entity → State) : Prop := ∀ dep anc, DependsOn dep anc → Refused state anc → Refused state dep`
4. `def BindingAdmissible (state : Entity → State) (e : Entity) : Prop := state e = State.observable`
5. `theorem refused_blocks_binding ...` (6 lines including proof)
6. `abbrev RequiredFor : Entity → Entity → Prop := fun ancestor dependent => DependsOn dependent ancestor`
7. `abbrev WitnessesInSnapshot (state : Entity → State) : Entity → Entity → Prop := fun _source target => BindingAdmissible state target`
8. `theorem cascade_implies_basis_inheriting ...` (12 lines including proof)

Substrate-specific (NOT duplicated): each consumer's `Entity` inductive, `DependsOn` inductive, and target theorem (e.g. `disk_state_cannot_bind_when_device_enumeration_refused`, `fleet_status_cannot_bind_when_nq_a_refused`, etc.).

**Approximate duplication:** ~40 lines × 4 consumers = ~160 lines of byte-identical machinery. Net per-consumer-specific content: ~15-20 lines (Entity + DependsOn + target theorem).

---

## Q1: Does the repeated adapter machinery still carry substrate evidence, or has duplication become clerical burden?

**Verdict: clerical burden. Yes-to-extract.**

The duplication did epistemically productive work while substrate evidence was being collected. Each new consumer namespace demonstrated that the same eight-element machinery instantiates over a structurally-distinct substrate domain. At 1 instance, the machinery was a one-off proof. At 2, a pattern. At 3, a confirmed pattern. **At 4, the duplication is no longer surfacing new information — every Lean line is byte-identical to the prior three copies.**

Future consumers (if any land) will add more duplication without adding more evidence about the pattern. The pattern is now known to be: *any binary-state, declared-dependency, cascade-sound substrate admits the same chain adapter*. The 8-element machinery is the *frame*; the substrate is in the `Entity` + `DependsOn` inductives + target theorem. Extracting the frame doesn't lose the substrate evidence — that evidence lives in the consumer-specific parts that would remain.

**Counter-argument considered:** self-contained namespaces are easier to read in isolation (a reader landing on `Nightshift` sees the full machinery without indirection). This is real, but at 4 instances the readability benefit is overwhelmed by the maintenance signal — *"these are four copies of the same thing"* is now harder to miss than a parameterized construction would be.

## Q2: Would extraction preserve the brakes?

**Verdict: yes, with the discipline applied during extraction.**

Brake-by-brake:

- **No cross-kernel claim.** Extraction stays inside `RefusalPropagation.lean`, parameterized over `Entity` and `DependsOn`. It does NOT reach across refusal-kernel families (`SurfaceAuthorization`, `FiatAdmissibility`, etc.). ✓
- **No claim graph.** The extracted construction must take `DependsOn : Entity → Entity → Prop` as a parameter, NOT introduce a graph type with metadata. Each consumer's `DependsOn` remains an inductive with named constructors. ✓
- **No path metadata smuggled into `DependsTrans`.** `DependsTrans` is in the `Composition` namespace and is unaffected by chain-adapter extraction. The extraction touches only the per-consumer adapter pattern, not the generic Composition theorems. ✓
- **No quorum / weight / probability algebra.** Fan-out machinery (`NQFanOut`) is in its own namespace and does NOT use the chain adapter. Extraction of chain adapter does not touch fan-out. ✓
- **No public `CalculusOne` movement.** Extraction is annex-internal; `CalculusOne.lean` remains untouched; no `[1.0]` tags. ✓

All five brakes preservable. The extraction must be done with the discipline; this audit answers whether the discipline *can* be applied, not whether it *will* be. The next-step experiment is what verifies the discipline holds in practice.

## Q3: Can the extracted shape stay boring?

**Verdict: yes — boring shape is just parameterization.**

The acceptable extraction shape: *"given a type `Entity` and a relation `DependsOn : Entity → Entity → Prop`, produce the eight-element adapter (State, Refused, CascadeSound, BindingAdmissible, refused_blocks_binding, RequiredFor, WitnessesInSnapshot, cascade_implies_basis_inheriting)."*

This is parameterization, not abstraction-in-the-pejorative-sense. No new vocabulary, no new abstractions over abstractions, no new ontology. The consumer picks its `Entity` and `DependsOn`, and the rest derives.

**Concrete failure modes to refuse during extraction:**
- A `RefusalDomain` typeclass with multiple instances and registration → kill.
- A `ChainConsumer` structure with auxiliary fields beyond Entity/DependsOn → kill.
- Pulling `State` into a generic `StateAlgebra` type → kill.
- Adding severity-states, scope, time, use-kind, or provenance → kill.
- "Composability" between extracted adapters that lets consumers extend other consumers → kill.

**The boring shape that survives:** a single `ChainAdapter` namespace (or section) parameterized over `(Entity : Type) (DependsOn : Entity → Entity → Prop)` providing the eight elements. Each consumer's namespace shrinks to: `Entity` inductive + `DependsOn` inductive + target theorem. No more, no less.

**Lean-engineering note:** the extraction will require section variables, `open` directives, and possibly `abbrev` aliasing in each consumer. This is conventional Lean style, not exotic. Indirection cost is real but bounded — a reader of `Nightshift` will need to know that `Refused`, `CascadeSound`, etc. come from `ChainAdapter`. That's one cross-reference, not a maze.

---

## Conclusion

**Annex Phase D opens.** All three audit questions answer yes.

The duplication has done its evidentiary work (Q1: yes-to-extract). The brakes are preservable under the extraction discipline (Q2: yes). The extracted shape can stay boring (Q3: yes, with vigilance against the named failure modes).

## Recommended next step (NOT in this audit)

**Optional small Lean experiment** in `RefusalPropagation.lean`:

- Add a `ChainAdapter` namespace parameterizing the eight-element machinery over `Entity` and `DependsOn`.
- Refactor *one* consumer (suggest `Nightshift` since it's the most-recently-added and least-load-bearing in this session's narrative) to use the extracted construction.
- Build green.
- Evaluate: does the refactored consumer read more cleanly? Does total code shrink? Are the brakes still visible?
- If yes to all three: refactor the remaining three chain consumers (`NQDependency`, `NQOnNQ`, `Labelwatch`) to use the same construction.
- If no: revert the experiment and record what went wrong in this audit's deferral note. The deletion clause covers reversion.

**Bounded cost estimate:** ~30-50 lines added (the `ChainAdapter` namespace), ~30 lines removed per refactored consumer, net ~50-80 lines reduction if all four refactor cleanly. Experiment is reversible; failure is informative.

## What this audit does NOT do

- Does NOT authorize Public Phase D. The two gates are independent per the plan.
- Does NOT change `CalculusOne.lean`. No public-surface movement.
- Does NOT add `[1.0]` tags.
- Does NOT touch `Composition` namespace theorems (`refusal_composes`, `_two_hop`, `_propagates_transitively`) — those are already canonical and not duplicated.
- Does NOT touch `NQFanOut` — fan-out is structurally distinct and not in scope.
- Does NOT advance the runtime-conformance question (`publish.rs` masking-cascade still parked as unbounded).

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — the file under audit.
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Annex Phase D / Public Phase D versioning plan.
- [[refusal-rebar-status-2026-05-26]] — end-of-day state receipt that identified shared adapter extraction as audit-worthy.
- [[nq-testimony-dependency-contract.md]], [[nq-on-nq-forcing-case.md]], [[nq-forcing-case-audit.md]] — consumer-side notes for the NQ chain instances.
- [[labelwatch-driftwatch-admissibility.md]] — substrate doc for the Labelwatch consumer.
- `~/git/nightshift/docs/DESIGN.md`, `~/git/nightshift/docs/GAP-nq-nightshift-contract.md` — substrate docs for the Nightshift consumer.

## Provenance

- 2026-05-26. Audit performed by claude-code after Nightshift adapter landed as fourth chain consumer at operator's request. Three audit questions per the Annex Phase D specification (added to plan earlier in session at ChatGPT's reframing of Phase D as Annex-D + Public-D split). All three answer yes. Audit document filed without attempting the bounded Lean experiment — that is a separate follow-up authorized by this audit but requiring its own operator go-ahead.

> **Annex Phase D opens. The bounded Lean experiment is the next pressure point.**

---

## Addendum: experiment results (same day, 2026-05-26)

After the audit filed, the bounded Lean experiment ran:

1. Added `Admissibility.RefusalPropagation.ChainAdapter` namespace (~51 lines) parameterizing the eight-element machinery over `(Entity : Type)` and `(DependsOn : Entity → Entity → Prop)`.
2. Refactored all four chain consumers in order (Nightshift → NQDependency → NQOnNQ → Labelwatch), each refactor verified by `lake build` green before moving to the next.

**File size:** ~880 lines → 734 lines (-146 lines net, after accounting for ChainAdapter additions and docstring updates).

**Per-consumer reductions** (consumer namespace only):
- `Nightshift`: ~82 → ~38 lines (-44)
- `NQDependency`: ~170 → ~78 lines (-92)
- `NQOnNQ`: ~100 → ~50 lines (-50)
- `Labelwatch`: ~80 → ~36 lines (-44)

Each refactored consumer is now: `Entity` inductive + `DependsOn` inductive + `open ChainAdapter` + target theorem(s). The shared machinery (`State`, `Refused`, `BindingAdmissible`, `refused_blocks_binding`, `WitnessesInSnapshot`, `CascadeSound`, `RequiredFor`, `cascade_implies_basis_inheriting`) lives in `ChainAdapter` exactly once.

**Brakes that held during extraction:**
- ✓ No `RefusalDomain` typeclass with instance registration.
- ✓ No `ChainConsumer` structure with auxiliary fields.
- ✓ No `StateAlgebra` generalization.
- ✓ No severity / scope / time / use-kind / provenance.
- ✓ No "composability" between extracted adapters.
- ✓ `NQFanOut` remains untouched (structurally distinct, doesn't use chain adapter).
- ✓ `Composition` namespace untouched (`refusal_composes` / `_two_hop` / `_propagates_transitively` were already factored).
- ✓ `CalculusOne.lean` untouched.
- ✓ No `[1.0]` tags.

**Final file structure** (7 namespaces, all annex):
- `Narrowing` — C.1 case analysis
- `Composition` — generic refusal-composition theorems
- `ChainAdapter` — extracted shared machinery (new)
- `NQDependency`, `NQOnNQ`, `Labelwatch`, `Nightshift` — chain consumers (refactored)
- `NQFanOut` — fan-in (untouched)

`lake build` green at 8298 jobs.

**Annex Phase D status:** opened, experiment succeeded, refactoring complete. The duplication is no longer in the file; the substrate evidence remains in each consumer's `Entity` + `DependsOn` + target theorem. The frame is now factored out exactly once.

> **Audit-worthy → audited → opened → experimented → closed. The annex maintenance step is complete.**
