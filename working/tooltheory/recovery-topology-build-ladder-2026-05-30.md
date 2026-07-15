# Recovery topology — build ladder (2026-05-30)

**Status:** Build ladder, not doctrine. Not a candidate note. Not a Lean target. Not a paper. Filed as the staged plan for returning to recovery-topology / `AdmissibleRecoveryPath` work after the [annex-probe queue](annex-probe-queue-2026-05-29.md)'s PL → CPI scope → Conductance → reachability-insufficiency scope cycle landed 2026-05-30.

**Policy update (2026-07-14):** this dated ladder originally treated downstream consumers as build authorization. That condition is superseded. Formalization may lead implementation. The surviving brakes are intrinsic: coherent theorem shape, correct quantifiers, non-vacuity, overlap, proof, and explicit custody. Runtime cases remain correspondence and scenario tests. The proposed reachability-insufficiency theorem was audited separately and is currently held because its displayed form is invalid/trivial, not because no consumer asked.

**Frame:** ladder, not task list. The danger this ladder is built to refuse: accidentally birthing a grand unified resilience ontology and then spending six weeks feeding it graph nouns.

**Doctrine sources:**

- [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md) — prose stack and audit; the doctrine source for the five-clause predicate.
- [reachability-insufficiency-candidate-2026-05-30.md](reachability-insufficiency-candidate-2026-05-30.md) — first scope statement around the central predicate; artifact-1-prep-work that now sits inside this ladder's context.
- `~/git/lean/LeanProofs/Admissibility/Conductance.lean` — built 2026-05-30; covers the `NonContagious` clause's receiver-side hygiene.

**Center stays:**

```text
AdmissibleRecoveryPath(src, carrier)
```

Everything else is either a clause, a consumer, or a falsifier.

---

## Step 0 — Lock the boundary

**First rule:**

> **Recovery topology is a composition surface, not a new sovereign primitive.**

It composes existing machinery under failure pressure.

The first document (Artifact 1 in §7) must explicitly say:

- not doctrine yet
- not a paper yet
- not "desynchronized horizons" formalized
- not a general graph theory project
- not a new taxonomy registry
- not replacing Standing / Witness / Freshness / ConsequencePartition / Conductance
- yes, it may expose missing atoms: **typed capacity** and **capacity-sufficient bound**

**Keeper line:**

> **Reachability is topology. Recoverability is admissibility over topology.**

That's the difference.

## Step 1 — Define the object, not the universe

The minimum formal/prose object:

```text
AdmissibleRecoveryPath(src, carrier, damage_kind, time_basis)
```

Clauses:

1. `Reachable(src, carrier)`
2. `CarrierAdmissible(carrier, damage_kind)`
3. `TimelyFor(src, carrier, time_basis)`
4. `TypedFor(carrier, damage_kind)`
5. `NonContagious(src, carrier)`
6. `CapacitySufficient(carrier, src, damage_kind)`

DeepSeek's earlier read said five clauses, but with reachability included it's six unless reachability is treated as the substrate predicate. Keep it visibly separate:

```text
Reachable  +  five admissibility clauses
```

That avoids confusing graph existence with recovery validity.

**Delta from [reachability-insufficiency-candidate-2026-05-30.md](reachability-insufficiency-candidate-2026-05-30.md):** the existing scope statement uses a five-clause form with `ReachableCarrier` as one of the five. This ladder splits reachability out as substrate, leaving five admissibility clauses. When Artifact 1 is written, the predicate signature should be revisited to honor this split; the reachability-insufficiency scope statement's "open scope-statement question #2" (per-source vs per-pair) becomes easier with the substrate-separated form.

## Step 2 — Proposed reachability-insufficiency cut (held on theorem shape)

This was proposed as the clean theorem-shaped residue. The 2026-07-14
extraction audit found that the displayed candidate does not yet earn a Lean
artifact: one version concludes `True` and leaves its path/bridge hypotheses
unused; failure of one carrier does not refute per-source recovery through
another carrier; strengthening the premise to say every carrier fails makes the
headline an immediate restatement of the supplied recovery-factorization
hypothesis. The hold is truth/quantifier/nontriviality, not consumer absence.

**Not:**

```text
Here is a full recovery graph calculus.
```

**But:**

```text
ReachableCarrier does not imply Recoverable.
```

Sharper:

```text
A carrier reachable through a path missing any required recovery clause
does not constitute an admissible recovery path.
```

This can be boring Lean. Boring is good. Boring proves the joint exists.

Likely theorem family (one per missing clause):

```text
reachable_without_admissibility_not_recoverable
reachable_without_timeliness_not_recoverable
reachable_without_type_match_not_recoverable
reachable_without_noncontagion_not_recoverable
reachable_without_capacity_not_recoverable
```

Then one umbrella theorem:

```text
reachable_not_enough :
  Reachable src carrier →
  ¬ AdmissibleAtCarrier carrier kind →
  ¬ AdmissibleRecoveryPath src carrier kind basis
```

The point is not brilliance. The point is making **false reachability** impossible to launder.

**Formal admission test:** Artifact 1 must stabilize, the bridge-axiom-vs-hypothesis and per-source-vs-per-pair questions must be answered, and the resulting statement must add a nontrivial proposition rather than unfold its own recovery predicate. If no such delta remains, the correct disposition is prose/definition only.

## Step 3 — Do not formalize a graph tautology

Lock/articulation is graph tautology unless the admissibility interpretation adds a genuinely new proposition. That theorem-shape delta, not consumer pressure, decides whether there is formal residue.

Don't mint:

```text
all paths through B means B is important
```

Graph theory has entered the chat.

What would make it nontrivial is the admissibility layer:

```text
All admissible recovery paths pass through authority B.
B can alter admissibility interpretation.
Therefore B is a synchronization lock, not merely an articulation point.
```

That is more interesting and may be formalized once `AdmissibleRecoveryPath` and the governor's interpretive power are stated without merely renaming articulation. `agent_gov` is a correspondence target, not permission to prove it. (See [annex-probe-queue](annex-probe-queue-2026-05-29.md) §"Fifth candidate (deferred): Governor non-sovereignty".)

## Step 4 — Treat typed capacity as the real missing atom

This is the part that may actually expand the calculus.

Existing primitives can mostly cover:

- standing
- basis
- evidence
- freshness
- witness scope
- consequence separation
- refusal
- non-contagion (now covered by `Admissibility.Conductance`)

But they do **not** fully cover:

> this carrier has the right kind of recovery capacity, and enough of it, under this damage mode, before exhaustion.

Two candidate additions:

```text
CapacityKind
HasCapacity(carrier, capacity_kind)
CapacitySufficient(carrier, demand, bound)
```

**Avoid the numerics goblin.** First version qualitative:

```text
insufficient | sufficient
```

or:

```text
CapacityStatus := absent | mismatched | insufficient | sufficient
```

Later, if needed:

```text
available_capacity ≥ required_capacity + reserve_margin
```

But not first. That's how the spreadsheet demon gets in.

## Step 5 — Build a scenario suite before building more Lean

The next serious work after Step 2 is **adversarial scenarios**, because they will tell whether the topology is real or just good vocabulary.

Prose fixtures first.

### Scenario A: false reachability

Carrier exists. Path exists. Recovery invalid because carrier lacks standing or type.

Expected verdict:

```text
reachable_but_not_recoverable
```

### Scenario B: bridge capture

Recovery requires the reservoir to adopt the failed subsystem's ontology.

Expected verdict:

```text
path_exists_but_contagion_capable
```

### Scenario C: witness non-activation

Witness survives with memory/legitimacy, but no admissible bridge converts it into carrier capacity.

Expected verdict:

```text
continuity_present_but_not_recoverable
```

### Scenario D: sink masquerading as carrier

Node requests recovery capacity but converts assistance into more failure.

Expected verdict:

```text
candidate_carrier_reclassified_sink
```

Prose only for now.

### Scenario E: governor as mandatory bridge

All recovery paths require governor interpretation.

Expected verdict:

```text
governor_is_lock_candidate
```

Formalize only after the claim gains admissibility content beyond graph articulation; `agent_gov` may later test the mapping.

## Step 6 — Consumer mapping

Where this becomes useful instead of scholastic CrossFit.

### NQ

NQ should eventually testify to **which clauses it can observe**.

Not:

```text
recoverable: true
```

But:

```text
reachable:           observed
timely:              cannot_testify
typed_capacity:      unknown
non_contagion:       cannot_testify
capacity_sufficient: unobserved
```

**Keeper:**

> A witness may report a recovery edge. It may not launder edge existence into admissible recovery.

### Nightshift

Nightshift consumes recovery topology as proceed/refuse basis.

It should not infer:

```text
fallback exists → safe to proceed
```

It should ask:

```text
fallback is admissible, fresh, typed, non-contagious, capacity-sufficient?
```

Otherwise it becomes false-reachability laundering.

### Agent Governor (`agent_gov`)

AG's hook:

> Governor may coordinate recovery, but must not become the only admissible recovery bridge.

Later gap candidate (when implementation pressure exists):

```text
GOV_GAP_RECOVERY_TOPOLOGY_LOCK_001
```

### Standing

Standing gets carrier/bridge/caller distinctions:

- who may request recovery
- who may carry recovery
- who may activate a bridge
- who may refuse becoming a carrier

Probably important.

### Wicket

Wicket should stay narrow:

> Does this proposed recovery action have admissible basis before execution?

Do not let Wicket become recovery topology. It can check a recovery claim, not own the graph.

## Step 7 — Artifact sequence

When returning to this, the artifact order:

### Artifact 1 — working note

```text
working/tooltheory/recovery-topology-candidate-YYYY-MM-DD.md
```

Sections:

- status: candidate, not doctrine
- core distinction: reachability ≠ recoverability
- load-bearing predicate
- clause definitions (the split-substrate form from Step 1)
- overlap audit
- scenario probes (Step 5 scenarios A–E)
- Lean candidates
- consumer hooks (Step 6)
- anti-promotion brakes

### Artifact 2 — Lean scratch annex

Only after Artifact 1 stabilizes and the Step-2 quantifier/nontriviality defect
is repaired.

Possibly:

```text
LeanProofs/Scratch/RecoveryReachability.lean
```

Only if the scope is tiny. No graph algorithms. No topology cathedral. Just:

```text
ReachableCarrier ≠ Recoverable
```

The Step-2 theorem family above is source material, not currently admitted
content. A repaired theorem must add more than definitional unfolding. The
Conductance annex is the precedent for bounded scope and explicit custody.

### Artifact 3 — gaps only when precisely evidenced

Possible later:

```text
TYPED_RECOVERY_CAPACITY_GAP
CAPACITY_SUFFICIENT_BOUND_GAP
RECOVERY_TOPOLOGY_LOCK_GAP
```

Don't file all three just because they sound good. A gap needs an exact missing
formal or runtime obligation. Formal gaps may be stated before their runtime
consumers; correspondence gaps require a concrete mapping. That's how this
avoids Concept Pokémon without reinstating consumer permission.

## Step 8 — The main test question

Every future iteration must answer:

> What laundering move does this block?

**Good answers:**

- "reachable carrier" laundering into "recoverable"
- "witness survived" laundering into "witness can carry renewal"
- "fallback exists" laundering into "fallback is admissible"
- "governor can coordinate" laundering into "governor may become mandatory"
- "help is available" laundering into "help will not exhaust the helper"
- "bridge exists" laundering into "bridge is non-contagious"

**Bad answers:**

- "this gives us a richer vocabulary"
- "this feels like a topology"
- "this unifies the framework"
- "DeepSeek liked it"

The last one is how the priest gets a Hugging Face account.

## Step 9 — The actual plan, compressed

When returning:

1. **Write the candidate note** around `AdmissibleRecoveryPath`.
2. **Keep reachability separate** from the five admissibility clauses.
3. **Add scenario probes** before more formalization.
4. **Repair the negative theorem before Lean:** the current per-carrier source shape is invalid/trivial; state the actual quantifiers or record that no distinct theorem remains.
5. **Defer lock/articulation** until it has admissibility content beyond graph tautology, not until a consumer asks.
6. **Track typed capacity** as the only likely new atom.
7. **Map consumer obligations** for NQ, Nightshift, Standing, AG, Wicket.
8. **Promote nothing automatically:** Scratch, public import, paper claim, and runtime conformance are separate custody decisions.

The big frame:

> Recovery topology is not another module. It is the shape that appears when admissibility is evaluated over failure paths.

That's the thing to preserve. Everything else is furniture.

---

## Relation to existing artifacts

- **[reachability-insufficiency-candidate-2026-05-30.md](reachability-insufficiency-candidate-2026-05-30.md):** scope statement filed earlier today. Now sits inside this ladder as Artifact-1-prep-work. The scope statement's four open shape questions remain valid; this ladder reframes them as Step-1-and-Step-2 decisions. When Artifact 1 is written, the reachability-insufficiency note should either fold into Artifact 1 or be explicitly subsumed.
- **[desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md):** doctrine source. Stays as-is. This ladder is the build plan for the kernel residue identified in its §Q-audit.
- **`~/git/lean/LeanProofs/Admissibility/Conductance.lean`:** built scratch annex. Covers the `NonContagious` clause's receiver-side hygiene. When Step 2's per-clause theorems are written, `reachable_without_noncontagion_not_recoverable` can cite the Conductance contagion-hygiene shape rather than re-derive it.
- **[annex-probe-queue-2026-05-29.md](annex-probe-queue-2026-05-29.md):** the queue. Step 2's build slot is "after Artifact 1 stabilizes"; that earns its own annex-probe test pass and queue entry at that point. This ladder does *not* pre-license the Step 2 build.

## Anti-goals (preserved from parent notes)

- No graph-model Lean (per parent §Anti-goals).
- No promotion without theorem-scope, overlap, proof, and custody review. Runtime correspondence evidence may contribute but is not an admission token.
- No sweep (per [annex-probe-queue](annex-probe-queue-2026-05-29.md) "shadow-public-surface basement governance" warning).
- No numerics goblin (Step 4).
- No Concept Pokémon (Step 7 Artifact 3).
- No priest with a Hugging Face account (Step 8).

## Provenance

- **2026-05-30** (same day as PL build, CPI scope, Conductance build, reachability-insufficiency scope). Build ladder synthesized after operator approval of the queue's day-of landings and ChatGPT's read-back. The ChatGPT read named the build-ladder-not-task-list framing and produced sections 0–9 in close to filed form.
- **Historical step gates, corrected 2026-07-14:** Step 1's clause definitions still depend on Artifact 1 becoming coherent. Step 2 depends on repairing the theorem's quantifiers and nontriviality. Typed-capacity work depends on a precise capacity proposition, not a forcing case. Consumer mapping can follow the formal object and does not authorize it. No step automatically promotes the next.

## Park state

> The ladder is the plan. The plan is not the build. Each step has its own gate. Recovery topology is composition over existing admissibility under failure pressure — not a new sovereign primitive, not a new module, not a new framework.

When the next session returns to this work: read this ladder before opening any new candidate note or any new Lean file. The right next action is Step 7 Artifact 1 (the candidate note), not Step 2 (the Lean cut).
