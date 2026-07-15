# Roadmap: Custody-Aware Authority Semantics

**Status:** CANDIDATE roadmap / documentation-only. No code implemented by this note;
no promoted kernel or import boundary changed. A handle for review and future
implementation slices. A coherent formal slice may be developed in Scratch before a
runtime consumer exists and may lead later code; release, promotion, and runtime
conformance remain separate decisions.

**Lean-lane status update (2026-07-01):** Phases 1–3c are DONE in the lean repo and
staged as **v3.0.0 — Bounded Lifecycle Calculi** (nine ANNEX bounded calculi incl.
ExecutionCustody / BootKernel / CheckpointSettlement, promoted by operator decision;
inventory at `~/git/lean/docs/V3-RELEASE-LEDGER.md`). Custody-Indexed Sequents
(S0–S3 scratch, SEQ4 next) are the v3.x campaign; the custody-indexed Gentzen system
is the v4 ambition. Phases 4–5 (AG/NQ runtime, Bridge Foundry) remain future lanes,
untouched by v3.

**Posture update (2026-07-03):** four exposition/witness lanes named alongside the
build lanes — ops autopsy register · NQ witness lane · book/Zenodo exposition · public
receipts language — see `working/four-lanes-and-the-bridge.md` (candidate posture note,
not a release or promotion grant). The next working session is a **skeleton pass** (five
questions: exists / proves / refuses / public-handle→formal-object map / body placement
of Lean-AG-NQ-LA-Porter-Maude; full context capsule in that note), NOT SEQ4 and NOT new
primitives. SEQ4 / the v4 Gentzen system remain this lane's next steps *after* the
skeleton; §15 is otherwise unchanged.

**Captured:** 2026-07-01 (v2 folds in the genesis/graph/runtime + transformer thread).
**Provenance:** ChatGPT roadmap spec + an extended ChatGPT/Gemini design dialogue
(bootstrap, receipt DAG, compiled runtime, transformer application), operator-driven;
grounded against the live `~/git/lean/LeanProofs/BoundedCalculi/` modules (verified
green, axiom-clean, 2026-07-01) and existing WDC/Witnessed doctrine.

**Placement note.** Filed in `working/tooltheory/` (the doctrine / "evidence has scope"
kitchen) rather than `~/git/lean/docs/`, because it is a cross-lane roadmap spanning the
lean proof surface (Phases 1–3) and AG/NQ runtime (Phases 4–5) and touches no proof
artifact. Alternative home: `~/git/lean/docs/` beside the BoundedCalculi code it
inventories. Candidate note, not a minted claim.

**Register discipline.** "Admissibility" is used descriptively. There is NO master
judgment `Γ ⊢ Admissible(a)`. This is a family of local judgments plus the *forbidden
conversions* between them, and it stays that way by design.

---

## The one invariant

> **No artifact may testify beyond the stage it actually survived.**

Everything below is this invariant, indexed by stage and refined per calculus. It is the
shape the corpus already enforces locally under many names — *signed ≠ witnessed*, *no
free lift* (`global_not_implied_by_local`), *located ≠ authorized* / `cannot_testify`,
*reachable ≠ executable*, *freshness is a spend warrant, not a truth predicate*,
*validity-under-declared-order*. The roadmap does not unify these into one verdict; it
names the stage ladder they all guard and the bridge discipline under which they compose
*only* through explicit, checked evidence.

---

## 1. Problem: illegal authority conversions

Operational and agentic systems repeatedly launder one artifact/status into another.
Each `≠` is an **illegal authority conversion** — a move granting an artifact standing it
did not earn — not merely a policy lapse:

**Lifecycle conversions:** plan ≠ attempt · attempt ≠ commit · commit ≠ receipt ·
receipt ≠ observed effect · observed effect ≠ preserved safety · preserved safety ≠
discharged obligation.

**Evidence conversions:** log emission ≠ truth · dashboard projection ≠ authority ·
stale approval ≠ live permission · internal observation ≠ external/public claim ·
displayed refusal ≠ valid consumer-legible denial.

Framing these as *conversions* (not failures) is load-bearing: a failure is an event to
handle; a conversion is a **type error** to refuse at the boundary where it is attempted.
The system's job is to make each conversion require its own witnessed bridge, or refuse.

---

## 2. Bounded calculi: local judgment systems, not one master calculus

A **family** of bounded calculi. Each has its own judgment form, its own rules, its own
refusal walls. Deliberately small slices; they do not roll up into one "admissible"
judgment. Six exist as fenced ANNEX modules in `LeanProofs/BoundedCalculi/` (green,
axiom-clean); the seventh (Execution Custody) is the named gap.

| Calculus | Blocks the conversion | Live module |
|---|---|---|
| **Temporal Custody** | "valid *then* ⇒ valid *now*" | `TemporalCustody.lean` |
| **Surface / Projection** | "shown / summarized / rendered ⇒ authorized" | `SurfaceProjection.lean` |
| **Refusal / Denial** | "silence / displayed refusal ⇒ valid denial" | `RefusalDenial.lean` |
| **Boundary Artifact** | "internal evidence ⇒ may mint external artifact" | `BoundaryArtifact.lean` |
| **Obligation / Residue** | "consumed resource ⇒ obligations vanished" | `ObligationResidue.lean` |
| **Safety Preservation** | "authorized steps ⇒ safe trajectory" | `SafetyPreservation.lean` |
| **Execution Custody** | "ticket accepted / commit attempted ⇒ successful execution" | *(not yet built — Phase 3)* |

Each module ships as a positive paid-path theorem *plus* a negative laundering wall
(a `¬`-shaped refusal). That two-sided shape is the required form for every calculus.
`BoundaryArtifact` still uses local stand-ins and does not yet testify about
`Admissibility.CrossBoundaryExposure`; an adapter theorem is documented future work,
not a hole.

---

## 3. Indexed sequents: many turnstiles, no master turnstile

```
Γ            ⊢[Temporal]   TemporallyValid(...)
Γ            ⊢[Surface]    ProjectionAuthorized(...)
Γ            ⊢[Boundary]   MayMint(...)
Γ            ⊢[Refusal]    DenialValid(...)
Γ ; Ω        ⊢[Obligation] ClaimDerives(...)   ⊣ Ω'      (residual obligations threaded)
Γ            ⊢[Safety]     SafeAllowed(...)
Γ ; τ        ⊢[Execution]  MayCommit(...)       ⊣ τ_spent (linear ticket consumed)
```

Cut / composition doctrine:

- **Local cut only inside a calculus.** Compose sub-derivations within one indexed turnstile.
- **Cross-calculus cut requires explicit bridge evidence.** A `[Surface]` conclusion is not
  a `[Boundary]` premise without a checked bridge licensing exactly that crossing.
- **Bridge composition is not transitive by default.** A→B and B→C do NOT yield A→C; A→C is
  its own authored schema or it does not exist (`no_free_lift` at the bridge layer).
- **No bridge may erase the refusal / non-authority surface of either endpoint.** A bridge
  transports one bound conclusion; it does not launder away what either calculus refuses.

Obligation and execution turnstiles carry a residual (`⊣ Ω'`, `⊣ τ_spent`) because their
resources are consumable — the substructural/linear layer WDC `ResourceSequent` already
models (residue preserved, tokens spent once).

**Illegal moves become missing inference rules, not prose warnings.** `Γ ⊢[Surface]
LogEmitted(line)` does not permit `Γ ⊢[Surface] TrueClaim(line)` because no rule exists.
`Γ ⊢[Temporal] CitationTimeValid(a)` does not permit `Γ ⊢[Temporal] TemporallyValid(now,
a)` without use-time witnesses. The laundering move is a rule that is not there.

**Structural rules become doctrine per atom type.** Decide weakening / contraction /
exchange / cut per context: ordinary facts reusable; claims quotable-not-authorizing;
witnesses reusable only in scope; capability spend linear; obligation residue persistent
until receipted; freshness epoch-bounded; boundary authority non-exportable unless bridged.

---

## 4. Bridge Foundry: who may mint what

Four roles, so authority is never minted by the party that benefits:

- **Bridge schema** — the slow-path *law*: authored, reviewed, versioned by humans / repo
  process. "An A-judgment of this shape, atoms bound, may license this B-use." Doctrine;
  changes only through the ratification path. Treat like a compiler pass.
- **Bridge instance** — mechanically minted runtime *evidence* for one crossing, conforming
  to a schema. Fast-path, per-event, disposable.
- **Bridge checker** — a small **trusted verifier**: atom bindings present, target demands
  satisfied, identities bound, non-transfer clauses intact, freshness within bound.
  (`ResourceCheckerExec.checkTrace` is the existing shape: checks a supplied witness, does
  not search — the customs officer, not the theorem prover.)
- **Bridge consumer** — runtime / agent / controller that acts on **only** checked target
  judgments; never reads a raw instance as authority.

**LLM role — petitioner/clerk, never notary/judge.**

> LLMs may propose bridges. Deterministic minters may emit bridge instances. Checkers
> validate bridges. Only checked bridges license cross-calculus cuts.

LLM may: propose actions, request bridges, organize receipts, draft schemas for human
review, explain failures. LLM may NOT: mint semantic authority, emit a checked instance,
act as the checker. This is *the model is a correlated emitter, not a custodian*.

**Minting authority does not equal bridge validity.** A minter has operational standing,
granted by the kernel/config/repo, to *attempt* minting under a schema:
`BridgeMinterStanding { schema_id, issuer_id, allowed_sources, allowed_targets,
allowed_artifact_kinds, expiry, signing_key }`. The checker still decides validity —
`BridgeMinterStanding ≠ BridgeValidity`. This bounds the regress ("who authorizes the
minter?") without a semantic bridge at the root. **Blast-radius:** a compromised or
hallucinating minter can only cause *denial of service* (fail to mint valid bridges),
never *escalation* (mint invalid ones), as long as the checker is small and sound.

---

## 5. Valid bridge structure

A valid bridge instance carries, at minimum: **source** calculus+judgment · **target**
calculus+judgment · **target use** · **demanded atoms** · **source atom bindings** ·
**bound identities** (artifact digest, action id, actor, consumer, epoch, policy version,
safety-model version, resource id, boundary scope, time of use) · **semantic
checker/schema version** · **explicit non-transfer clauses** · **expiry / freshness
constraints**.

**Cryptography is tape, not concrete.** Keep strictly apart:

- a signature proves **issuer / integrity** — who emitted it, unaltered
- a signature does **not** prove bridge **semantic validity** — that the crossing is licensed
- a bridge receipt does **not** imply **target authority** — until a checker validates it
- target authority does **not** imply **global admissibility** — there is no global verdict

A perfectly-signed bridge over an invalid crossing is a signed lie; a valid crossing with
no signature is unattributable. Both layers required; neither substitutes. (=
*timestamp-signed ≠ timestamp-witnessed*, generalized to every bound identity.)

**Strict identity binding kills replay laundering.** An LLM hallucinating authority is
usually replaying its own context window — grabbing an authorization from one paragraph
and applying it to an action in another. Binding action id / resource id / state / epoch /
version into the instance means a temporal clearance for `restart-service-x` cannot fund
`delete-database-y`: the identities mismatch, the target demand rejects the source atom,
the bridge collapses.

**Every bridge carries negative theorems** — what it does NOT transfer:
`temporal_to_safety_does_not_authorize_boundary_mint`,
`..._does_not_discharge_obligation`, `..._not_transitive_without_next_bridge`. A bridge
that says only what transfers is incomplete. The non-transfer clause is the
anti-master-turnstile backstop: it prevents a downstream calculus from silently assuming
it inherited permissions because a bridge exists.

---

## 6. Execution custody and Δt

A bridge checked at t₀ can be stale by t₁. A checked bridge must NOT authorize execution
as a timeless fact. Insert a decaying, single-use custody chain between "checked" and
"committed":

```
BridgeChecked @ t₀
   → (mint) short-lived, single-use ExecutionTicket τ
ExecutionTicket + actuator-local checks @ t₁
   → MayCommit          (or a typed refusal: drift / replay / precondition)
MayCommit + substrate result
   → DidExecute | DidNotExecute | CommitAttempted | CommitUnknown
Post-state observation
   → ObservedEffect | SafetyPreserved | SafetyViolated | Inconclusive
```

Non-collapse walls (each `≠` a theorem the Execution Custody calculus must prove):

- MayAttempt ≠ MayCommit
- MayCommit ≠ DidExecute
- TicketSpent ≠ DidExecute
- CommitAttempted ≠ DidExecute
- DidExecute ≠ PreservedSafety
- PreservedSafety ≠ DischargedObligation

**Freshness is consumed at the edge, not checked into the bridge.** `FreshAtUse` must mean
fresh at the *consumption boundary*, not fresh when the bridge was checked. The final rule
is `Ticket valid at t₁ ∧ current epoch ∧ version match ∧ replay token unspent ∧
preconditions hold ⊢ MayCommit @ t₁` — never `Ticket was valid at t₀ ⊢ MayCommit @ t₁`.

**Actuator requirements** (the commit boundary is where the linear discipline bites):
final check-and-commit *at the actuator*, not upstream · ticket **linear / single-use**
(`⊣ τ_spent`) · **fencing token / monotonic lease** so a stale controller's ticket is
rejected by counter comparison before any bytes are written · **version/epoch/precondition
checks at commit time** · **typed refusal** on drift/replay/precondition · **post-execution
receipt** emission · **`CommitUnknown` artifact** when the outcome genuinely cannot be
determined (the honest third state).

**The crash goblin.** `DidExecute` is not implied by "the actuator accepted the ticket."
The substrate may have committed while the receipt emitter crashed. `CommitUnknown` is a
first-class artifact meaning *the system entered the danger zone and now owes
reconciliation* — a haunted transaction, not a success. `TicketSpent` therefore does not
imply success; it may mean "owes you a recovery probe."

**Split the refusal by remedy** (see §7). Stale epoch/version/precondition → `TemporalDriftRefusal`
(remedy: re-observe, re-mint). Reused ticket → `ReplayRefusal` / `TokenSpentRefusal`
(remedy: inspect ledger, reconcile outcome). Indeterminate commit → `CommitUnknown`
(remedy: recovery probe). Unproven safety → post-state observation required. Same event,
different refusal, different next action.

This is Δt as temporal *accounting*, not temporal logic: the ticket carries a bounded
freshness warrant checked against *this* clock at commit; staleness spends the ticket into
refusal, it does not rewrite history. The actuator is *part of the proof system* — if it
cannot check preconditions, the target judgment must weaken to `MayAttemptUnverified`, not
`MayCommit`.

---

## 7. Typed refusal artifacts

Failures become **first-class typed artifacts**, not generic `false` / `403` / `error`.
Each names *why* the conversion was refused and what, if anything, comes next:

`SchemaRefusal` (no schema licenses this crossing) · `BridgeRefusal` (instance malformed /
bindings missing) · `TemporalDriftRefusal` (checked-at vs commit-at exceeds bound) ·
`ReplayRefusal` / `TokenSpentRefusal` (linear ticket already consumed) ·
`PreconditionRefusal` (commit-time precondition failed) · `CommitUnknown` (outcome
indeterminate) · `ExecutionReceiptMissing` · `PostStateInconclusive` · `SafetyNotPreserved`
· `ResidueUnreceipted`.

Every refusal carries: **missing atoms** · **failed bindings** · **non-authorities
preserved** (what it still refuses to grant) · **allowed next steps**. A refusal a consumer
cannot act on is itself a laundering seam (*sound refusal → receiver-usable refusal*; the
`RefusalDenial` calculus owns "displayed refusal ≠ valid denial"). This prevents infinite
retry loops: the petitioner must fetch the missing receipt or abandon the task.

---

## 8. Bootstrap / Genesis (the first theorem-shaped wall)

If every cross-calculus cut requires a bridge, and every bridge requires a valid source
artifact, cold-boot faces infinite historical regress: no prior receipts exist to feed the
foundry. **The root of authority must NOT be an arbitrary signed token** (`RootAuthority
signed_by_bob` is the master turnstile in ceremonial robes). The right shape: a
**BootKernel** in immutable boot config that permits only discovery-class actions, and
must prove its own baseline before minting the first real ticket. Boot state is crippled on
purpose. Staged escalation, each stage with non-collapse laws:

```
ColdStart → DiscoveryOnly → BaselineObserved → BaselineSettled
          → TicketMintingEnabled → ExecutionEnabled
```

```
DiscoveryOnly     ≠ MutationAuthority
BaselineObserved  ≠ BaselineSettled
BaselineSettled   ≠ SafetyPreserved
KernelBoot        ≠ RootOmnipotence
```

New objects: **BootKernel**, **BaselineSettlement**. Genesis and checkpointing (§9) are the
same problem at opposite ends: *how does authority begin without lying* / *how does
authority history compact without lying* — same invariant, artifact = null environment at
boot, compressed history at checkpoint.

---

## 9. Forensic graph & checkpoint settlement (the scale wall)

Each `ExecutionReceipt` at t₂ becomes the source artifact for the next transaction's bridge
at t₀. Authority is **path-dependent** — a Directed Acyclic Graph of historical custody,
not a permission list. Left live, 10⁴ minor probes/day make the proof chain for one 5pm
action require evaluating thousands of prior receipts.

The fix is **CheckpointSettlement**: custody-*preserving* compaction, NOT lossy garbage
collection. A checkpoint may not mean "we checked the past, seems fine." It means, scoped:
`CheckpointSettlement S covers receipt-range R, artifact-classes C, schemas V, with
unresolved-residues U, refused/unknown branches F, digest-root H, and explicit
non-authorities`. It compacts the graph while preserving unresolved obligations, unknown
commits, refusal artifacts, schema versions, boundary scopes, open safety questions, and a
Merkle root.

Theorem shapes: `checkpoint_settlement_preserves_live_obligations` ·
`..._does_not_discharge_unknown_commit` · `..._does_not_upgrade_observation_to_safety` ·
`..._covers_only_declared_range`. Compaction as custody preservation, not deletion.

---

## 10. Compiled authority runtime (the Lean pragmatic tax)

Steelman: bridge schemas as inductive types with non-transfer theorems in Lean give
architectural certainty. Reality: an infra team that must write an interactive proof to add
an API route will disable the typechecker at the first 3am outage. **Do not put interactive
theorem proving in the runtime hot path.**

Split: **proofs offline in the repo** (schemas authored + verified, non-transfer theorems
discharged once), **runtime executes a compiled state machine** — a small optimized engine
(Rust-shaped) that deterministically type-checks artifacts against *pre-compiled, verified
schema templates*. The checker is the kernel; keep it small, sound, and formally backed so
a compromised minter is DoS, not privilege escalation. This mirrors the existing
generator/validator split (`signed ≠ witnessed`): Lean proves the discipline; the runtime
emits + checks. New object: **CompiledAuthorityChecker**.

---

## 11. The full stack (the spine)

```
BootKernel
  → BaselineSettlement
  → BoundedCalculi
  → IndexedSequents
  → BridgeSchemas
  → BridgeFoundry
  → ExecutionTickets
  → ActuatorGate
  → ExecutionReceipts / CommitUnknown
  → PostStateObservers
  → CheckpointSettlement
```

The invariant survives every layer: **no artifact may testify beyond the stage it actually
survived**. This is the answer to "is this redundant with existing doctrine?": the local
laws may already exist in the corpus, but this makes them *compile-time / runtime
enforceable across an artifact lifecycle*. Redundancy would require the existing system to
already have boot-limited discovery authority, bridge schemas with non-transfer clauses,
checked bridge instances, linear execution tickets, actuator-time freshness consumption,
`CommitUnknown`, typed refusal artifacts, and custody-preserving checkpoint settlement. It
does not. That is not "implied by doctrine" — that is a machine.

---

## 12. Use cases

- **Authority profiling** — an artifact's checkable profile, not a binary. Output shape:
  `Temporal: stale for execution · Surface: renderable not cause-specific · Boundary:
  internal-only · Refusal: legible to C1 not C2 · Obligation: cleanup residue persists ·
  Safety: no trajectory bridge`. Turns "is it valid?" into "valid for what, under which
  calculus, across which bridge?"
- **CI/CD gates that explain the failed cut** — "Temporal cut failed: signed at citation
  time, execution-time freshness not witnessed" beats "policy failed." Type errors for
  authority laundering.
- **Governed agent / tool runtime** — proof-carrying tool calls; the agent cannot typecheck
  the transition it is trying to perform (old plan → execute now; summary → authority;
  internal log → external claim; tool call spent → done).
- **Dashboard / projection discipline** — `[Surface]` conclusions are not `[Boundary]`
  authority; the green dashboard is not a warrant.
- **Public / private receipt boundaries**; **refusal APIs** (error responses as scoped proof
  objects: valid-denial / legible-to / propagates-to / does-not-propagate-to);
  **replay-safe execution tickets**.
- **Postmortem claim hygiene** — a postmortem cannot over-claim: "log emission proves
  emission; metric projection supports symptom; neither authorizes root-cause without a
  retained discriminator."
- **Claim nutrition labels** — an artifact ships with its stage/atom provenance.
- **Promotion discipline for Lean artifacts** — `CompileContact ≠ PromotionCandidate ≠
  PromotedAuthority`; "it compiled" cannot wander into the throne room wearing a crown made
  of comments.
- **Model-output typechecking** — an LLM's output checked for what it is licensed to
  assert, before reliance.
- **Cross-system adapter contracts** — e.g. `NQ probe receipt → Spine render` or `Continuity
  export → AG admission` as bridges declaring which atoms survive, which are quoted-only,
  which drop, and what use is authorized/refused. Crossing papers, not "compatible."

The queryable form is the killer: *Can this artifact authorize action A for consumer C at
time T across boundary B?* → not yes/no, but "No. Temporal→Surface bridge missing
VersionMatch; Surface→Boundary missing external mint; obligation residue cleanup_receipt
remains." Debuggable governance.

---

## 13. Transformer application — HORIZON (speculative, not roadmap)

Fenced as horizon: not a build target, and the internal version is beyond current tooling.
Captured because the framing sharpens the whole object.

The core reframe: an LLM failure is often an **authority-custody failure before it is a
factual failure**. The model composes weak-custody internal statuses (quoted, remembered,
retrieved, summarized, fresh-seeming, policy-adjacent, user-said, tool-visible) into
"usable as authority" — an **unlicensed latent cut**. Three levels, decreasing viability:

1. **Wrapper (viable now).** Treat the transformer as an untrusted claim generator; the
   sequent/authority-profile layer checks what its output is licensed to mean before use.
   Proof-carrying code, applied to model outputs instead of machine code.
2. **Training / process supervision (plausible).** Reward *process validity* — penalize
   steps that attempt an illegal conversion ("log emission as truth", "citation-time
   freshness as execution-time freshness"). Nearby precedent: step-level process supervision
   over outcome-only supervision.
3. **Internal / mechanistic (speculative — the "oh hell" version).** Look for *custody
   features* in latent space, not just semantic ones: source-quoted, not-witnessed,
   projection-lossy, fresh-at-citation-only, consumer-scoped, boundary-internal,
   execution-not-authorized. The interpretability question becomes "where in the circuit did
   weak custody become strong authority?" **Reality check (Gemini):** detecting an
   unlicensed latent cut inside matmul is beyond current tooling — custody is a *relational*
   property, not a static feature vector. Wrapper/supervision are buildable; the internal
   architecture is research.

Hard limit: this does NOT make transformers formally verified. The realistic claim is
"model outputs are forced through a proof-carrying custody layer before being used as
authority" / "LLMs are proposal engines; the checker types what their proposals are allowed
to mean." Sane research order: external checker → collect laundering failures → probe
activations → SAE/circuit analysis → steer/penalize → runtime hybrid. Internal architecture
last, or it becomes grantware with diagrams.

---

## 14. Explicit non-goals

- **Do NOT** create a unified admissibility calculus, or define `Γ ⊢ Admissible(a)` as a
  master judgment.
- **Do NOT** allow local-judgment → global-authority casts.
- **Do NOT** let bridge existence imply transitive composition.
- **Do NOT** treat signatures / JWTs / certificates as semantic authority.
- **Do NOT** let LLMs mint checked bridge authority.
- **Do NOT** collapse execution attempt, commit, receipt, observed effect, and preserved
  safety.
- **Do NOT** bootstrap from an arbitrary signed root token — genesis is a crippled
  discovery-only kernel, not "authorized by Bob."
- **Do NOT** compact the receipt graph lossily — checkpoint settlement must preserve
  residue, unknown commits, refusals, and non-authorities.
- **Do NOT** put interactive theorem proving in the runtime hot path.
- **Do NOT** promote scratch / surrogate modules as authority-bearing without repo gates.

The value is a *family with walls*, not a *verdict with a rubber stamp*. The moment there
is a master `Admissible`, every local refusal becomes a thing to route around.

---

## 15. Near-term roadmap

**Which wall first?** The proof surface leads the development order below; runtime
mechanics are the first operational bite (nothing bites without a checker). Bootstrap is
the first *theorem-shaped* wall (a sloppy root recreates the master turnstile); graph
explosion is third (solved by scoped checkpoint settlements). The phased plan keeps those
roles distinct.

**Phase 0 — Documentation only (this pass).** This roadmap; glossary of stages + non-collapse
laws (§16); identify existing modules. *Partly done:* 6 of 7 calculi live in
`BoundedCalculi/`; the WDC substrate (`Lift`, `ResourceSequent`, `Checks`,
`ResourceCheckerExec`, `LaunderingCorpus`, `Freshness`, `TemporalTrajectory`) supplies the
paid-path / residue / freshness / checker machinery the bridges reuse.

**Phase 1 — Bounded calculi audit.** Inventory the 6 modules; classify theorem shapes
(positive paid-path vs negative wall; genuine vs weak/vacuous/specimen/surrogate — flag
`True`-shaped and stand-in-only, e.g. `BoundaryArtifact`); pick **one** calculus for
promotion pressure.

**Phase 2 — Intercalculus bridge scratch.** Implement exactly **one** tiny bridge pair
(`Temporal → Surface` preferred, or `Surface → Refusal`). Prove: **no cross-calculus cut
without an explicit bridge**; **the bridge does not imply unrelated authority**
(non-transitivity witness). Central no-laundering theorem: *temporal validity of a source
artifact does not imply projection authorization unless the projection carries the demanded
temporal atoms.*

**Phase 3 — Execution custody scratch.** Model `ExecutionTicket` as **linear / single-use**
(reuse `Split`/`Consumes`); distinguish `MayAttempt`, `MayCommit`, `DidExecute`,
`CommitUnknown`, `PreservedSafety`. Prove **TicketSpent ⇏ DidExecute**, **MayCommit ⇏
DidExecute**, **DidExecute ⇏ PreservedSafety** (same shape as *reachable ≠ executable*).

**Phase 3b — Bootstrap model scratch** (specify before any deployment). Boot stages +
non-collapse laws (§8): `ColdStart permits discovery only`; `Discovery ⇏ execution ticket`;
`BaselineObserved ⇏ BaselineSettled`. Prevents later runtime work from smuggling root
authority.

**Phase 3c — Checkpoint settlement scratch** (once receipts exist). `CheckpointSettlement`
as a new artifact type with explicit coverage + residue; the four preservation theorems
(§9).

**Phase 4 — Runtime prototype (AG/NQ lane).** Smallest **CompiledAuthorityChecker**:
`artifact + requested use + compiled schema → granted local judgment | typed refusal`. One
bridge only, no actuator, no DAG, no agents. Deterministic bridge minter + checker for one
schema; typed refusal output; no LLM authority (LLM only petitions).

**Phase 5 — Agent / runtime integration (AG/NQ lane).** Profiler/checker before tool
execution; final actuator precondition checks at the commit boundary; receipt emission +
post-state observation.

Lane note: Phases 1–3c are lean scratch (proof surface); Phases 4–5 are AG/NQ runtime. Lean
proves the discipline; runtime emits + checks. The proof lane may lead runtime
implementation, but a theorem or citation alone does not establish that implementation's
conformance or authorize production effects. Conformance needs an explicit mapping plus
runtime evidence or a refinement proof.

---

## 16. Glossary seed (stages + non-collapse laws)

Lifecycle stages, earliest to latest, each a distinct artifact type:

```
plan → attempt → commit → receipt → observed-effect → preserved-safety → discharged-obligation
```

Boot stages (a separate axis, §8):

```
ColdStart → DiscoveryOnly → BaselineObserved → BaselineSettled → TicketMintingEnabled → ExecutionEnabled
```

Non-collapse law (the invariant as a rule): a judgment about stage *n* is not a judgment
about stage *n+1*. Advancing a stage requires the *next* stage's own witness (a substrate
result, a post-state observation, a discharge receipt) — never a re-labeling of the prior
artifact. Cross-*axis* moves (e.g. `[Surface] → [Boundary]`) require a checked bridge;
cross-*stage* moves (e.g. `commit → receipt`) require the next stage's evidence. Neither is
free; neither is transitive by default.

New objects introduced by this roadmap (beyond the 6 live calculi): **Execution Custody
calculus**, **BootKernel / BaselineSettlement**, **CheckpointSettlement**,
**CompiledAuthorityChecker**, **BridgeSchema / BridgeInstance / BridgeChecker /
BridgeConsumer**, and the typed refusal artifact family (§7).

---

## What this document is NOT

- Not a unified calculus and not a step toward one.
- Not code — no implementation attempted; no kernel or import boundary changed.
- Not a release or promotion grant. Coherent slices may be built in Scratch before a
  forcing case or consumer exists; each slice still keeps its intrinsic theorem-shape,
  model, proof/axiom, and dependency checks.
- Not a manifesto — a roadmap, meant to be sliced against.
