# Desynchronized Horizons — candidate primitive, not doctrine (2026-05-30)

> **One-line abstract.** Robust plural systems survive by keeping subsystem recovery horizons decorrelated, so local closure remains carryable and does not synchronize into total collapse.
>
> **Warning label.** *Do not confuse plurality of parts with decorrelated failure modes.* (Five replicas trained on the same priors, funded by the same patrons, ranked by the same platforms, punished by the same social field, briefed by the same summary pipeline = one replica with a Greek chorus.)
>
> **Operative primitive.** *Local carryability.* See §The primitive below.
>
> **Filed as candidate primitive, not doctrine.** The prose stack is rich; the Lean residue is narrow; the temptation to backfill prose into fake formal certainty is the primary failure mode. *Worked examples inform doctrine promotion; they do not authorize formalization. The Lean splinter stays humble and local.*

**Status:** Candidate primitive at tooltheory density. Two live products: (1) prose stack — desynchronized horizons / common-mode recovery failure / horizon carriers / locks / reservoirs / bridges; (2) Lean splinter — narrow conductance hygiene lemma only. Conductance Lean splinter **built 2026-05-30** as scratch annex at `~/git/lean/LeanProofs/Admissibility/Conductance.lean` under the annex-probe queue's intrinsic five-criterion test; see §"Lean annex — built status" below. Prose stack remains working-note only.

**Policy update (2026-07-14):** consumer-gated formalization language below is superseded. Formal work may lead `agent_gov` or other implementations. Runtime cases are correspondence tests; the actual gates are theorem coherence, truth, anti-vacuity, overlap, proof, and custody. The proposed reachability-insufficiency slice is held on quantifier/nontriviality defects found by the extraction audit, not on missing demand.

**Posture:** Family is *recovery-graph / admissibility-dynamics*, **not** the projection-erases-distinction family that hosts CP / NI / PL / `SurfaceAuthorization` / `WitnessInvariance`. Different axis content; direct descendant of [[project-paper26-candidate]]'s empty-window theorem (`W = ∅` case). Filed at candidate density per [[feedback-name-early]]; kernel-overlap audit deferred but partially done by multi-model relay 2026-05-30 (DeepSeek + Claude-web + operator).

---

## Compressed doctrine (the keeper)

> **Collapse is not subsystem death. Collapse is the exhaustion, capture, or lockout of all admissible recovery paths.**
>
> **Resilience is not preventing death. Resilience is keeping death locally carryable.**
>
> **A governor that becomes necessary to all recovery paths has become the lock it was built to prevent.**

## The hinge

The move that earned this candidate slot: **horizon is relational, not scalar.**

A recovery horizon is not "time until death." It is *"the last point at which a subsystem can still recover without requiring some other already-exhausted subsystem to save it."* That relocates collapse from a countdown to a **recovery-graph reachability problem**.

P26 already had this in `W = ∅` vocabulary (admissibility maturity and consequence viability lose overlap → recovery is impossible-as-recovery, not late). What's new: **the recovery graph itself**, not just the per-claim window.

## The primitive

> **Local carryability.** A system remains viable while every local death remains carryable by an unexhausted, uncoupled, admissible recovery path.

## Five-clause recovery-path predicate

Reachability to a non-exhausted node is **not enough**. A recovery path has to be:

| Clause | Failure if missing |
|---|---|
| **Admissible** | carrier has standing to help | the help is illegitimate; cannot bind |
| **Timely** | recovery arrives before closure becomes irreversible | the help is "after the wake" |
| **Typed** | carrier has the right kind of capacity | structural mismatch; carrier exhausts trying |
| **Non-contagious** | recovery edge does not mutate carrier into same failure mode | carrier becomes the next casualty |
| **Budgeted** | help does not exhaust the carrier faster than renewal replenishes it | carrier collapses; recovery propagates as sink |

The predicate ugly-but-honest:

> Can this node reach an admissible, timely, typed, non-contagious, capacity-sufficient carrier through a bridge that does not collapse the reservoir?

## Node taxonomy (role-based, not identity-based)

| Role | Description |
|---|---|
| **Carrier** | Still inside its horizon; can act as recovery substrate for another. Continuity capacity in use. |
| **Reservoir** | Low-pressure node retaining recognitions / skills / legitimacy; not yet carrying live load. Potential carrier capacity. |
| **Bridge** | Admission-controlled channel allowing reservoir → carrier transition without contagion backflow. Gated, one-way during use. |
| **Sink** | Consumes recovery capacity faster than it can be renewed. Often disguised as a needy carrier. |
| **Lock** | Mechanism forcing multiple nodes to share the same recovery trigger / failure interpretation. Synchronization enforcer. |

**Critical caveat:** these are *roles under a recovery relation*, not permanent node identities. A node can be carrier for one failure mode, reservoir for another, sink under wrong pressure, lock when its interpretation becomes mandatory. *"This institution is a reservoir"* is HR-department ontology disease. Correct form: *"This institution is a reservoir for this recovery relation, under this pressure, with this bridge, until this exhaustion condition."* Tedious. That's how the ghosts get evicted.

## Conductance operator layer

The "shared edge" question becomes a layered conductance question — *every edge conducts multiple things*, and the design target is selective conductance:

| Conductance | What it transmits | Design target |
|---|---|---|
| **Coordination** | ability to share action | high |
| **Recovery** | ability to carry repair | high |
| **Contagion** | ability to transmit failure state | low |
| **Authority** | ability to make interpretation binding | low |
| **Exhaustion** | ability to drain capacity | low |

**The bridge-design question in one sentence:** *how do you raise coordination + recovery conductance without raising contagion + authority + exhaustion conductance on the same edges?*

The relay's candidate split (Claude-web + operator): conductance separability is **not** a property of the edge; it is a property of the *protocol layered on the edge*. Same wire, different semantics. The defense is gating: pull-type coordination, push-type failure only with receiver-local admission.

> **Coordinate by pull. Propagate failure only by admitted testimony. Never let the same edge that lets the system act-as-one make it die-as-one.**

## Five candidate theorems (named, not built)

Recorded so the audit trail shows what was *named* without authorizing build. Per [[feedback-name-early]].

1. **Reachability insufficiency.** A path to a carrier does not imply recoverability if any required edge is inadmissible, mistyped, too late, contagion-capable, or budget-exceeding. *Blocks "graph exists, therefore resilience" laundering.*
2. **Lock / articulation theorem.** If all recovery paths from a class of nodes pass through one mandatory bridge or gate, failure or capture of that gate synchronizes closure across the class. *The priest theorem.*
3. **Reservoir protection theorem.** If a bridge is pull-gated and prohibits reverse mutation of reservoir state absent reservoir-local admission, recovery request visibility does not itself exhaust the reservoir. *Closest to the existing Conductance hygiene fragment.*
4. **Sink depletion theorem.** If a sink has priority access to carrier capacity and consumes capacity faster than it enables renewal, global recovery capacity monotonically decreases. *Circuit-breaker basis without "be cruel because vibes."*
5. **Governor non-sovereignty theorem.** A governor preserves desynchronization only if its removal does not eliminate all admissible recovery paths. *Graph translation: the governor cannot be an articulation point in the recovery graph. Possibly the cleanest formal hook.*

## Lean annex — built status (2026-05-30, same day)

`~/git/lean/LeanProofs/Admissibility/Conductance.lean` is green as a scratch annex. ~262ms. Not in `LeanProofs.lean`. No public-surface promotion. `coordinationSignal` declared-but-unused (load-bearing absence preserved).

Discipline preserved:

- Compile is *contact*, not publication. Green confirms the pull-gated / passive-contagion shape type-checks; it does not promote Conductance to doctrine.
- Five-clause recovery-path predicate, Recovery Graph machinery, the four remaining candidate theorems (reachability-insufficiency, lock/articulation, sink depletion, governor non-sovereignty), and the separability question stay in prose.
- Public-surface gating preserved: no `LeanProofs.lean` import, no preprint claim, no doctrine mint.
- The audit was the first receipt; the green compile is the second receipt; the doctrine receipt is still upstream.

Build invocation:

```bash
cd ~/git/lean && lake build LeanProofs.Admissibility.Conductance
```

### Build-surfaced finding: `failureSignal` cannot infer `Subsystem`

The relay's sketch called `Protocol.failureSignal sig` directly. Lean rejected: `failureSignal`'s type signature only mentions `Signal`, not `Subsystem`. So the class field projection cannot determine `Subsystem` from arguments, which breaks typeclass instance synthesis for `Protocol Subsystem Signal`.

The annex resolves this by writing `@Protocol.failureSignal Subsystem Signal _ sig` at both callsites (the `ContagionCapableEdge` definition and the `passive_failure_implies_contagion_capable` hypothesis). The `_` lets Lean infer the instance once `Subsystem` is supplied.

This is a *real* shape finding, not a cosmetic fix:

- It says the Protocol class has a field whose semantic content is signal-only (failure-status), while the other four fields are signal-and-subsystem joint relations.
- The honest decomposition would be **two classes**: one signal-side (e.g., `class SignalKind (Signal : Type) where failureSignal, coordinationSignal : Signal → Prop`), one transport-side (`class Protocol (Subsystem Signal : Type) where transmits, localAdmits, changesState : Subsystem → Subsystem → Signal → Prop` etc.).
- This refactor is **optional cleanup**, not blocked on a downstream consumer. The hygiene theorems do not depend on the decomposition and the explicit `@` annotation is locally sufficient. Split the classes only if it removes a real type-design ambiguity or supports a distinct signal-side theorem; avoid churn for its own sake.
- Filed as a note here so a future session does not re-derive the surprise.

## The Conductance hygiene fragment (Lean — built 2026-05-30 as scratch annex)

The relay's residue. *Not the separability theorem* — `coordinationSignal` is declared but unused in the proofs, confirming this is the contagion-hygiene lemma only. **Built** at `~/git/lean/LeanProofs/Admissibility/Conductance.lean`. The sketch below is preserved as the recoverable artifact; the annex file differs only in (a) namespacing under `Admissibility.Conductance`, (b) explicit `@Protocol.failureSignal Subsystem Signal _ sig` form at the two callsites that need it (see §"Build-surfaced finding" above), and (c) annex-preamble matching the CP / PL precedents.

Binder fix already applied per relay-Claude flag (`{src dst : Subsystem sig : Signal}` → `{src dst : Subsystem} {sig : Signal}` — split the binder; first form parses `Subsystem sig` as an application).

```lean
namespace Admissibility.Conductance

variable {Subsystem Signal : Type}

class Protocol (Subsystem Signal : Type) where
  transmits : Subsystem → Subsystem → Signal → Prop
  localAdmits : Subsystem → Signal → Prop
  changesState : Subsystem → Signal → Prop
  failureSignal : Signal → Prop
  coordinationSignal : Signal → Prop

variable [Protocol Subsystem Signal]

def PassiveStateChange (dst : Subsystem) (sig : Signal) : Prop :=
  Protocol.changesState dst sig ∧ ¬ Protocol.localAdmits dst sig

def ContagionCapableEdge (src dst : Subsystem) : Prop :=
  ∃ sig,
    Protocol.transmits src dst sig ∧
    Protocol.failureSignal sig ∧
    PassiveStateChange dst sig

def PullGatedReceiver (dst : Subsystem) : Prop :=
  ∀ sig,
    Protocol.changesState dst sig →
    Protocol.localAdmits dst sig

theorem pull_gated_blocks_passive_contagion
    {src dst : Subsystem}
    (hgate : PullGatedReceiver dst) :
    ¬ ContagionCapableEdge src dst := by
  intro h
  rcases h with ⟨sig, _htrans, _hfail, hchange, hnot_admit⟩
  exact hnot_admit (hgate sig hchange)

theorem passive_failure_implies_contagion_capable
    {src dst : Subsystem} {sig : Signal}
    (htrans : Protocol.transmits src dst sig)
    (hfail : Protocol.failureSignal sig)
    (hchange : Protocol.changesState dst sig)
    (hnoadmit : ¬ Protocol.localAdmits dst sig) :
    ContagionCapableEdge src dst :=
  ⟨sig, htrans, hfail, hchange, hnoadmit⟩

end Admissibility.Conductance
```

**Scope fence (verbatim from relay-Claude):**

> This does not prove desynchronized horizons. It pins the local safety condition required by the prose theory: coordination edges become contagion-capable when remote failure can mutate receiver state without local admission.

**Filename when built:** `~/git/lean/LeanProofs/Admissibility/Conductance.lean`. **Companion note when built:** `working/tooltheory/conductance-hygiene-candidate-2026-05-DD.md` (or this note becomes the companion).

**What `coordinationSignal` being unused tells us:** this fragment captures **contagion hygiene**, not coordination/contagion separability. The separability question stays in prose. *That's exactly why "green contact, not doctrine promotion" is the right label.*

## The hard implementation edge (the deep bridge problem)

> **How does a witness become a carrier without adopting the failed system's ontology as the price of being heard?**

The fallen node will usually demand help in its own corrupted terms. The reservoir has to accept enough signal to help without accepting the frame that produced the failure. So a bridge can't just carry "request." It has to carry:

- bounded claim
- typed need
- admissible evidence
- refusal rights
- time-limited standing
- no identity merger
- no automatic legitimacy transfer

**Existing-vocabulary translation:** *the reservoir must admit the recovery claim, not become the failed subsystem's afterlife.* This is the cancer / capture failure mode at the bridge layer.

## Family placement (NOT projection-erases-distinction)

**Distinct from** the CP / NI / PL / `SurfaceAuthorization` / `WitnessInvariance` family. Those are *projection erases load-bearing distinction*. This is *recovery graph topology under correlated failure.* Different axis content.

| Sibling | Relation |
|---|---|
| [[project-paper26-candidate]] (empty-window) | **Direct ancestor.** `W = ∅` is local carryability's null case. P26 is per-claim window; LC is per-recovery-path graph. |
| [[project-consequence-partition]] (CP, built) | Adjacent family. CP refuses *expressibility laundering*; LC refuses *recovery-graph laundering*. Both projection-shaped at top level, different axis. |
| [negative-inclusivity-candidate-2026-05-30](negative-inclusivity-candidate-2026-05-30.md) (NI, candidate) | Adjacent. NI's Hermeneutical Enclosure terminal state is *one specific* sink/lock pattern in LC's vocabulary: civic-speech-substrate sensors self-silence because their bridge has become a contagion edge. LC generalizes; NI is one row. |
| `Admissibility.ConsolidationDenial` (built, public) | Decay-shape adjacency. CD: fluency does not witness settlement; LC's Hermeneutical Enclosure / sensor-decay has similar shape. CD is per-cycle settlement; LC is per-recovery-graph reachability. Not member. |
| `Admissibility.SafetyTrajectory` (built, public, safety-bridge family) | Closest *trajectory* sibling. SafetyTrajectory's no-lift theorem is per-trajectory value preservation; LC is per-recovery-path admissible reachability. Trajectory triple has shape kinship with the recovery path; not the same primitive. |
| [[project-governor-doctrine]] (`agent_gov`) | LC's governor non-sovereignty theorem is the formalization of the *cite-don't-extract* discipline already in agent_gov. The relay flagged that `agent_gov` is a partial implementation harness for the LC primitive: polling not pushing, scoped roles, recovery_horizon field. Direct downstream consumer. |
| [[project-admissibility-decay-family]] | Sink dynamic + Hermeneutical-Enclosure-style sensor decay are decay-shape but admit-suppression rather than stale-license. Adjacent. |
| [[project-controller-continuity]] | LC's *role-not-identity* node taxonomy is the recovery-graph form of controller-continuity's hybrid-control reading. Sibling. |
| `~/git/continuity` ([[project-continuity-doctrine]]) | Continuity is reliance-boundary; LC adds recovery-graph topology over the reliance boundary. Composable; not member. |

**The structural delta that earns the candidate slot:**

1. **Recovery-graph reachability** as a load-bearing object. No existing kernel / candidate carries the graph as primitive structure.
2. **Conductance as multi-axis edge property.** Existing kernels treat edges as single-purpose. The five-conductance layering is new framing.
3. **Synchronization-as-failure-mode.** Phase-locked horizon closure is a load-bearing failure pattern not in any built sibling.
4. **Role-not-identity discipline** baked into the taxonomy. Prevents the family from sliding into ontology HR.

## Overlap audit (paper/Lean Claude, 2026-05-30)

Operator-supplied seven-question audit framework. Run against the candidate; not a hype audit; verdict per question.

### Q1 — Genuinely new kernel terrain, or covered by existing machinery?

**Mixed.** Three sub-findings:

- **Recovery-graph topology is structurally new.** Existing kernel has *trajectory* shape (`SafetyTrajectory`, `Corrective`) and *bundled-construction* shape (`Execution.AuthorizedStep`). Neither carries a *web* of inter-subsystem recovery relations. Trajectory ≠ recovery graph; the graph property (which nodes can save which) is not a sequence property.
- **Per-edge content largely decomposes** into existing predicates. Recovery edge `A → B` is *"B is in a state such that B can act as carrier for A"* — a joint-state predicate that lifts existing admissibility / standing / freshness / capacity primitives. Composition discipline, not new atoms.
- **Two genuine gaps in the existing kernel:** *typed capacity* (the carrier has the right *kind* of capacity, not just any capacity) and *capacity-sufficient bound* (the carrier has *enough* capacity to renew faster than it exhausts). These are not in any existing module; `RecoveryMargin` is the closest cousin (refuses visible-green → capacity inference) but RecoveryMargin is signal refusal, not capacity bound.

**Verdict:** new compositional joint + two new atoms (typed/capacity) + Recovery Graph as new topological object. *Not* a clean replacement for existing kernels.

### Q2 — Smallest theorem-shaped residue

**Two candidates, ordered by bounded-ness:**

**(a) Conductance hygiene** (already filed in §The Conductance hygiene fragment below).
- Smallest. Bounded. Bug pre-flagged.
- Proves: pull-gated receiver ⇒ no contagion-capable edge from this receiver.
- Does *not* prove the separability theorem (`coordinationSignal` unused — load-bearing absence).
- Queue position: post-PL, post-CPI.

**(b) Reachability insufficiency** (the user's #1 candidate; the anti-laundering theorem).
- Form: `ReachableCarrier(n) ∧ ¬(Admissible ∧ Timely ∧ Typed ∧ NonContagious ∧ Capacity) ⇒ ¬Recoverable(n)`.
- **Caveat:** requires bounded `Recoverable` definition. The honest formalization either pulls in the whole `Surface`/`Trajectory` machinery (large) OR introduces `Recoverable` as an axiom-shaped abstract predicate with five-clause-conjunction shape (smaller, but the theorem becomes a one-liner trivially derived from definitions).
- *Either way, the theorem is real; the scope work is what gates the build.* Like CPI: needs a scope statement before annex-probe license fires.

**Verdict:** Conductance hygiene is the smaller, more bounded residue. Reachability insufficiency is the more *interesting* residue but requires a scope-statement pass first.

### Q3 — Disposition per artifact

| Artifact | Disposition |
|---|---|
| Desynchronized Horizons (umbrella prose) | **Working note only.** This note. Promotion to anything else requires worked examples (relay's three-case test: ops / institutional / political). |
| Local Carryability (operative primitive) | **Prose doctrine in this note.** Not Lean-shaped at this density. |
| Recovery Graph (machinery) | **Prose doctrine, no Lean.** Graph-theoretic formalization is premature; would launder reachability into the kernel as primitive. |
| Conductance operator layer (five conductances) | **Prose doctrine; one Lean fragment (the hygiene splinter).** Separability stays prose. |
| Conductance hygiene fragment | **Checked fenced annex.** Built 2026-05-30 as `Admissibility/Conductance.lean`; contagion hygiene only, not separability. |
| Reachability insufficiency theorem | **Held on theorem shape.** The source statement is invalid/trivial under its displayed quantifiers; repair the recovery quantification and prove a non-definitional delta before extraction. |
| Lock / articulation theorem | **NO-OP.** Tautology once formalized (articulation point + closure = unreachable; true by graph theory). The substantive claim is *design*, not theorem. |
| Reservoir protection theorem | **Subsumed by Conductance hygiene.** Same content; don't double-mint. |
| Sink depletion theorem | **Deferred.** Requires numeric machinery (capacity bound + monotone decrease); too much infrastructure for the marginal payoff. |
| Governor non-sovereignty theorem | **Scratch candidate if a nontrivial admissibility delta can be stated.** Graph theory supplies articulation; the formal residue must come from `AdmissibleRecoveryPath` and the governor's interpretive power. `agent_gov` is a correspondence target, not an admission gate. |

### Q4 — Overlap with existing primitive families

| Primitive | Overlap | Verdict |
|---|---|---|
| Witness / admissibility | `Admissible` clause is admissibility-kernel content. Existing modules (`Authority`, `Derivation`, `Execution`) discharge it per-step. | **Reused, not duplicated.** |
| Standing | Admissible-carrier requirement includes standing. Existing `signal-authority` / governor-standing material is the closest carrier-side primitive. | **Reused.** LC adds inter-subsystem topology over standing. |
| Freshness / recovery horizon | `Timely` clause is `Freshness` content. P26 empty-window theorem is the direct ancestor of LC's *no admissible carrier remains* clause. | **Reused + extended.** P26 is per-claim window; LC is per-recovery-graph reachability. |
| Consequence Partition / Projection Laundering | Different family (projection-erases-distinction vs. recovery-graph topology). CP refuses expressibility laundering; LC refuses recovery-graph laundering. | **Adjacent, not overlap.** |
| Contagion hygiene (the Conductance fragment) | Direct hit on `NonContagious` clause. *This is one clause of the five-clause predicate.* | **Conductance fragment IS the contagion-hygiene piece of LC. Subsumed under LC.** |
| Governor non-sovereignty | Direct hit. `agent_gov` is the partial implementation harness. | **LC formalizes the constraint agent_gov was already implementing implicitly.** |

### Q5 — Test the five-clause predicate: does each clause earn its slot?

| Clause | Earns slot? | Why |
|---|---|---|
| Admissible | Yes, reused | Admissibility kernel content; one of five clauses is necessary in the conjunction. |
| Timely | Yes, reused | `Freshness` / P26 content; without time bound, recoverability claim doesn't bind to a window. |
| Typed | **Yes, new atom** | Existing kernel does not have typed-capacity. Capacity-as-quantity collapses without type-match (e.g., legal carrier cannot save technical-debt closure). |
| Non-contagious | Yes, partially new | Conductance hygiene fragment is the formal version; `WitnessInvariance` is the cousin (witness moves under wrong perturbation = contagion of disturbance). |
| Capacity-sufficient | **Yes, new atom** | Existing kernel does not have capacity bound. `RecoveryMargin` is signal-refusal cousin but does not state a bound. |

**All five earn their slot.** The two genuinely-new atoms (typed, capacity-sufficient) are where LC adds vocabulary beyond the existing kernel. The other three are *composition discipline made explicit*.

### Q6 — Lock / articulation theorem: new enough to formalize?

**No.** The theorem statement is *true by graph theory*: an articulation point's removal disconnects the graph. Formalizing it in admissibility vocabulary launders graph theory into the kernel without adding admissibility content. The *substantive claim* is a **design discipline**: "real systems should not have mandatory bridges through any single authority surface." That's a constraint on the recovery graph, not a theorem about it.

**The right form of this claim** is the **governor non-sovereignty** theorem (Q3), which states the constraint in admissibility vocabulary: a governor preserves desynchronization only if its removal does not eliminate all admissible recovery paths. The admissibility content is "admissible recovery paths"; graph theory does the rest. Formalize only when that predicate and the governor-specific delta are coherent; `agent_gov` need not exist first.

### Q7 — Find the load-bearing predicate (do not promote because vocabulary is strong)

**The load-bearing predicate is the five-clause recovery-path predicate itself**, expressed in conjunctive form:

```text
AdmissibleRecoveryPath(src, carrier) :=
  ReachableCarrier(src, carrier) ∧
  AdmissibleAtCarrier(carrier) ∧
  TimelyForSrc(carrier, src) ∧
  TypedForSrc(carrier, src) ∧
  NonContagiousEdge(src, carrier) ∧
  CapacitySufficient(carrier, src)
```

The **theorem about it** is reachability-insufficiency: `ReachableCarrier(src, carrier) ∧ ¬AdmissibleRecoveryPath(src, carrier) ⇒ ¬Recoverable(src, via carrier)`. The **doctrine about it** is local carryability: a system survives while every local closure has at least one `AdmissibleRecoveryPath` to some non-exhausted carrier.

**This predicate is the genuine new compositional joint.** It is not a new atom (its clauses are reused or new-but-narrow); it is the *structure* that makes the existing atoms' implied recovery topology explicit. *That's exactly the "composition discipline as theorem" form the relay warned about — true but not deflating.*

### Audit summary

- **Yes,** there is real new compositional terrain (Recovery Graph topology + two new atoms: typed-capacity, capacity-sufficient bound).
- **The first Lean slice is NOT desynchronized horizons itself.** Confirmed: too big, too graphy, would launder metaphor.
- **The Conductance hygiene fragment was the right first Lean cut** — bounded, audit-partial, and now checked in the fenced annex.
- **The reachability-insufficiency theorem remains held** — the later audit found a quantifier/triviality defect, so a bounded `Recoverable` scope statement alone is insufficient.
- **Lock/articulation is a no-op.** Graph theory does the work; admissibility vocabulary adds nothing.
- **Governor non-sovereignty is the cleanest remaining formal hook** — if it adds admissibility content beyond articulation; consumer demand is irrelevant to that test.
- **The five candidate theorems currently compress to one checked slice** (Conductance hygiene), one theorem-shape hold (reachability insufficiency), one possible intrinsic-delta candidate (governor non-sovereignty), and two holds (sink depletion needs justified numerics; reservoir protection is subsumed).
- **Prose stack stays as working note** until the three-case worked examples (ops / institutional / political) land.
- **Watchword honored:** *not promoting merely because vocabulary is strong.* Found the load-bearing predicate (five-clause conjunction); confirmed the formalization payoff lives in the composition-discipline-as-theorem form, not in vocabulary expansion.

## What this primitive is NOT

- **Not "death and renewal cycle."** Greek tragedy is the wrong frame; closer to Daoist *flow*. Persistence is "pattern stable across continuous non-identical renewal," not "substance that resists death."
- **Not eternal return.** Return is wheel + fate + hubris-to-collapse arc. LC is decorrelated renewal across staggered horizons.
- **Not graph-theoretic optimization.** "Maximize plurality" is not the design target; *plurality is decorrelated failure*, not count.
- **Not a governor specification.** LC names the constraint the governor must satisfy (non-sovereignty) without specifying the governor's implementation.
- **Not separability proved.** The conservation-law question (can coordination-conductance and contagion-conductance be raised independently on shared edges?) is open. The Conductance hygiene fragment proves only the contagion-hygiene lemma; the separability theorem is deferred.
- **Not the full graph model.** No Lean modeling of synchronized horizon closure tonight. Per [annex-probe-queue-2026-05-29.md](annex-probe-queue-2026-05-29.md) anti-sweep rule.

## Anti-goals

- **Historical night-of constraint:** the 2026-05-30 session did not sweep the graph model. Conductance has since been checked; this sentence is not a current stop-work rule.
- **NO governor implementation work.** `agent_gov` is a downstream consumer / partial harness, not a target for retrofit.
- **NO graph-model Lean without a coherent model.** Toy clocks, thresholds, or recovery windows that merely rename the metaphor do not earn a theorem. A consumer is neither necessary nor sufficient.
- **NO promotion of the five candidate theorems to built status without per-candidate audit.** Each one needs the annex-probe test pass on its own merits.
- **NO sweep.** This stack is rich; the temptation is to harvest five theorems and three primitives in one weekend pass. *Don't.* Per [annex-probe-queue-2026-05-29.md](annex-probe-queue-2026-05-29.md) "shadow-public-surface basement governance" warning.
- **NO renaming yet.** *Local Carryability* is the working primitive name. *Recovery Graph* is the machinery. *Conductance* is the operator layer. If the names earn ratification through use, fine. Don't pre-bless.

## Formal disposition and correspondence watchlist

Each artifact has its own disposition; Lean admission and public promotion are separate:

- **Conductance hygiene Lean fragment:** checked fenced annex; no automatic public promotion.
- **Reservoir protection / Lock / Governor non-sovereignty theorems:** per-candidate truth, nontriviality, and overlap audit. Most plausible formal delta: governor non-sovereignty, with `agent_gov` as later correspondence target.
- **Graph model:** requires coherent state, path, admissibility, and falsifier definitions. Worked cases from `agent_gov`, NQ, or labelwatch may test the mapping but do not authorize the formal work.
- **Paper-shape:** requires three worked cases showing the same vocabulary cleanly explains all three without gelatin (relay's recommendation): ops case (platform outage / common control plane / backups share auth), institutional case (whistleblower / regulator capture / press as late receiver), political case (emergency power / courts / legislatures / public legitimacy horizon lock).

Until those reviews land: candidate doctrine and checked local fragment; fence held without treating runtime demand as permission.

## Provenance

- **2026-05-30** multi-model relay. Started from "is this as good as it gets?" → operator + Claude-web → DeepSeek convergence → Claude-web theorem-by-testimony reading of the Lean fragment with binder-bug flagged → operator filing.
- **Distinct chats:** the relay forked into a new chat to keep the main chain clean; both chains converged on the same primitive layer.
- **agent_gov cross-reference:** relay surfaced the existing `agent_gov` implementation as a partial harness for the LC primitive (polling, scoped roles, recovery_horizon field). DeepSeek's repo read raised the five hard implementation questions (governor self-horizon, bridge gating, synchronization-detection mode, noise-injection vs passive monitoring, sink starvation). All five remain runtime mapping questions; formal statements should lead where coherent rather than wait for an implementation slot.
- **Relay residue not folded in:** the *coordination-as-pull-only* protocol design (mutual TLS analog for social cohesion), the *witness-as-protected-pattern* discussion, the *desynchronization governor as continuous noise-injection* dynamics. These all remain prose-only; they earned no Lean residue this pass and would need their own audit before any compile probe.

## Park state

> *The audit was partial. Conductance is checked. Other slices are held on theorem shape, scope, or overlap — never merely because a forcing case is absent.*
>
> **A system survives not by preventing subsystem death, but by ensuring that death remains locally carryable.** The slab is set down. No Rust was summoned. The republic has staggered horizons, or it does not have horizons at all.
