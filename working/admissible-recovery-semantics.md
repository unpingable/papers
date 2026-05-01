# Corrective Monotonicity: Non-Laundering Recovery Semantics for Authority-Bearing Systems

*Working note / scaffold — 2026-05-01*

## Status

Scaffold; not yet a paper.md candidate. Slot decision deferred between two
plausible homes:

- **P27 §-fold-in.** P27 ("Obligation-Unsound Reconciliation") is structurally
  the same animal: controller-correct, operator-unsound is the post-corrective
  state where machinery ran cleanly but the resulting authority surface may not
  be admissible. The Corrective.lean module reads naturally as P27's formal
  core.
- **Standalone P28.** Treated as a small formal kernel paper with its own
  scope, citing P22's failure geometry and P27's obligation algebra rather than
  living inside either.

Defer until the seven-path audit (see §11) lands. The audit decides whether the
contribution has a concrete forcing case (paper has teeth) or remains
anti-regression doctrine (likely better folded into P27 as a sub-section).

The Lean kernel exists and is proof-gate-clean: see
`~/git/lean/LeanProofs/Admissibility/Corrective.lean`, sibling to the four
existing `Admissibility/` modules (Authority, StateTransition, Derivation,
Execution).

## Abstract (stub)

Existing authorization systems typically specify when an action is permitted,
but underspecify what transitions remain admissible after authority state has
become stale, corrupted, contested, or invalidated. This gap permits recovery
paths to launder failed authority into renewed authority: restoring data,
rebuilding projections, or resolving failures can accidentally mint or widen
authorization. We introduce *corrective monotonicity*, a recovery discipline
for authority-bearing state machines. Transitions are classified as corrective,
forward, or neutral; corrective transitions may invalidate, revoke, freeze,
fork, expire, or require re-entry, but must be monotone non-increasing over the
authorized action set. Authority-increasing recovery must occur through a
separately classified forward transition with fresh admissible basis. We
mechanize the core invariant in Lean as a preorder over governance states
parameterized by an authority evaluator, making corrective monotonicity an
explicit proof obligation for concrete environments rather than a global
universal claim. The result is not a complete governance framework; it is a
small formal kernel for non-laundering recovery semantics.

## Core thesis

> Recovery in authority-bearing systems needs a transition discipline:
> corrective steps must be authority-non-increasing, while authority-increasing
> recovery must occur through a separately classified forward step with fresh
> basis.

Same-basis matters. The theorem is not that systems can never recover
authority. The theorem is that authority cannot be recovered *from the failed
authority itself.* If basis K has failed, K stays failed; a fresh K' may mint
fresh authority through the ordinary admissibility path.

Slogan: *Recovery may restore availability. Re-entry restores admissibility.*

Theorem name: *corrective monotonicity.*

## 1. Recovery is not authorization recovery

Restoring state is not the same as restoring the authority of that state.

Three structural examples (developed in §10):

- A backup restore can revive byte-level state that includes admin tokens,
  active sessions, or policy snapshots whose authority basis no longer holds.
- A reconciliation controller can reassert a desired-state record whose
  underlying approval has been revoked or expired.
- An agent's persistent memory can preserve a record of past user authorization
  whose basis has since been invalidated, then act from the remembered grant as
  though it were current.

In each case the recovery path is operating correctly under its local
specification. The category error is treating availability of state as
equivalent to admissibility of the authority that state encodes.

The thesis: corrective recovery must not increase authority for the same failed
basis.

## 2. The laundering problem

The bug class has a compact form:

```
evidence-of-failure → corrective path → fresh authority
```

A failure is detected. A corrective fires. The corrective restores or
reconstructs some component of authority-bearing state. Downstream evaluators
treat the post-corrective state as authoritative. The chain runs without any
fresh admissibility basis ever being submitted; the failure itself has been
quietly laundered into renewed authorization.

Vocabulary used throughout:

- **Authority-bearing state.** Governance state whose contents determine which
  actions are presently authorized for which actors over which scopes.
- **Basis.** The evidentiary ground that justifies a particular authority
  claim: a policy reference, a delegation receipt, a signed approval, an
  evidence root.
- **Authority claim.** A bound triple of (actor, operation, scope) with a
  specific basis K asserting admissibility.
- **Corrective transition.** A state transition whose function is to respond
  to detected failure of authority state: revoke, invalidate, freeze, fork,
  expire, require re-entry, declare gap.
- **Forward transition.** A state transition that can mint, widen, refresh, or
  promote authority via the ordinary admissibility path.
- **Neutral transition.** A state transition that records or reconstructs
  information without changing the authorized action set.
- **Same-basis laundering.** The specific failure mode where a corrective fires
  in response to K's failure and the post-corrective state treats K (not a
  fresh K') as authoritative.
- **Re-entry.** The legitimate replacement of a failed K with a fresh K'
  through a forward transition, after K has been invalidated by a corrective.

The same-basis qualifier is load-bearing. Re-entry is not laundering; it is
exactly the path the system is supposed to take when authority has failed and
must be re-established.

## 3. Transition taxonomy

The spine of the discipline:

| Class | Function | Effect on authorized action set |
|---|---|---|
| neutral | record or reconstruct information | preserve |
| corrective | respond to authority-state failure | non-increasing |
| forward | mint, widen, promote, restore through fresh basis | may increase |

The classification is total: every transition belongs to exactly one class.
The implementation surface (§5) enforces this by structural means: a transition
type without a classification is a definitional error.

The law:

```
corrective ⇒ authority-non-increasing
```

Non-strict. A corrective no-op, a redundant revocation, or a failed quarantine
is still a valid corrective; the discipline rules out *increase*, not equality.

The disjointness obligation:

```
corrective ∩ forward = ∅
```

Operational rule for new transitions: if a candidate transition is "mostly
corrective, but" can mint, widen, bless, promote, or restore authority, it
belongs on the forward side of the split, not in the corrective set. The
corrective half can be a separate transition.

## 4. Formal model

Let an *authority evaluator* be a function that, given a governance state Γ,
an actor a, and an authority claim K, returns a verdict in
{denied, advisory, authorized}. The evaluator is parameterized: different
concrete systems supply different evaluators, but the discipline is stated
uniformly over them.

Define the authorized set at a state, relative to an evaluator env:

```
AuthorizedSet(env, Γ, a) = { K : evaluator(env, Γ, a, K) = authorized }
```

Define a preorder over governance states relative to a fixed evaluator:

```
Γ' ≼_env Γ  iff  ∀ a, K. evaluator(env, Γ', a, K) = authorized
                          → evaluator(env, Γ, a, K) = authorized
```

Read: Γ' is *weakly less permissive* than Γ. Reflexive and transitive.

The discipline:

> **Corrective monotonicity.** For every transition s with `IsCorrective(s)`,
> for every governance state Γ:
>   `applyStep(Γ, s) ≼_env Γ`.

Non-laundering follows by contraposition, restricted to a single basis K:

> **Same-basis non-laundering corollary.** For every transition s with
> `IsCorrective(s)`, every Γ, a, K:
>   if `evaluator(env, Γ, a, K) ≠ authorized`,
>   then `evaluator(env, applyStep(Γ, s), a, K) ≠ authorized`.

Sequence composition is immediate from transitivity of ≼:

> **Corrective sequence monotonicity.** For every list of transitions
> [s₁, ..., sₙ] with each `IsCorrective(sᵢ)`:
>   `applySteps(Γ, [s₁, ..., sₙ]) ≼_env Γ`.

Real recovery flows are sequences — invalidation, then quarantine, then TTL
expiry, then require-reentry — not single steps. The composition theorem
licenses end-to-end reasoning.

The fixed-evaluator caveat is not cosmetic. The preorder is parameterized by
env. A separate laundering vector exists in evaluator mutation: "recover
authority by changing the evaluator instead of the state." That belongs to a
distinct theorem and is not subsumed by corrective monotonicity. Pinned in §14.

The framework does not require authority reasoning to be monotonic.
Authorization is expected to be nonmonotonic with respect to revocation,
expiry, invalidation, and contestation: new evidence retracts prior
conclusions, and the framework relies on this. Corrective monotonicity is a
path property, not a global logic property: once a transition is classified
as corrective, its effect on the authorized set must be non-increasing. The
underlying authority logic remains free to retract, demote, or expire prior
authorizations as new evidence arrives.

## 5. Lean kernel

The discipline is mechanized in
`~/git/lean/LeanProofs/Admissibility/Corrective.lean`, sibling to four existing
modules under the same namespace: Authority (verdict algebra), StateTransition
(mutation algebra plus authorized-execution wrapper), Derivation (read-side
bridge from state to verdicts), and Execution (binds mutation and verdict
through `AuthorizedStep`).

The new module contributes:

- `StepClassification` inductive type with constructors `corrective`,
  `forward`, `neutral`.
- `classify : Step → StepClassification`, total over the existing `Step` type.
  Adding a new `Step` constructor without an arm here is a Lean
  non-exhaustive-match error. *This is the enforcement surface.* It is the only
  mechanism in the kernel that prevents a future silently-corrective-and-
  authority-granting transition from sneaking in.
- `IsCorrective`, `IsForward`, `IsNeutral` predicates derived from `classify`.
- Disjointness lemmas: `corrective_not_forward`, `corrective_not_neutral`.
- `WeaklyLessPermissive env Γ' Γ` preorder, with proven reflexivity and
  transitivity.
- `CorrectiveMonotone env`, a structure carrying the monotonicity proof
  obligation as a field. Concrete evaluators (`DerivationEnv` values) discharge
  this obligation at construction time. No global axiom claims the law
  unconditionally.
- The core theorem `corrective_monotone`, which projects the obligation under
  the structure.
- The corollary `corrective_no_authority_laundering`, which restricts
  monotonicity to a single basis K via contraposition.
- `corrective_sequence_monotone`, proven by induction plus transitivity.
- `RecoveryEnv`, a structure bundling a `DerivationEnv` with its
  `CorrectiveMonotone` witness, and `applyCorrectiveRecovery`, a
  recovery-facing applier whose type signature requires a `RecoveryEnv` rather
  than a raw `DerivationEnv`. The companion theorem `recovery_monotone` is a
  boring projection through the bundle.

The design choice worth naming has two halves.

The first half: the kernel does *not* assert global monotonicity as an
unconditional theorem. It declares the shape any compliant authority evaluator
must prove. Any concrete evaluator that wants to claim corrective monotonicity
supplies a `CorrectiveMonotone env` value, which forces case analysis over the
corrective arms of `classify` plus whatever behavioral laws on the underlying
store operations are required. This mirrors the kernel's existing house style
for `BasisDerivation`, whose `revoked_never_admissible` field carries an
analogous obligation. No free-floating axioms; no decorative `sorry`; the
`lake build` proof gate remains green.

The second half is the available-versus-required distinction. The
`CorrectiveMonotone env` structure makes monotonicity *available* — any
evaluator that wants the property can prove it. `RecoveryEnv` and
`applyCorrectiveRecovery` make it *operationally required at the recovery
boundary*: a caller cannot reach the recovery-facing applier without
constructing (and therefore discharging) the obligation. Analysis tools, audit
tools, and ordinary forward-authorization paths still take raw `DerivationEnv`;
the obligation becomes load-bearing only at the recovery surface, where it
matters. The narrow gate placement keeps the kernel's surface honest without
demanding a global typeclass discipline that the obligation shape is not yet
stable enough to carry.

The paper sentence: *the kernel makes monotonicity expressible; the runtime
makes it non-optional.*

The classify-based enforcement surface earns its keep prospectively. With the
current four-constructor `Step` type, no constructor is *both* classified
corrective *and* able to widen the authorized set, so the same-basis
non-laundering corollary holds trivially. That is not a defect — it is the
audit. The forcing case is whichever future Step constructor first tempts both
classifications. The construction obligation guarantees the question gets
asked.

## 6. Re-entry semantics

The doctrine spine:

```
old K invalidated  →  fresh K' submitted  →  fresh K' admitted via forward path
```

Re-entry is not a single transition. It is a sequence: at minimum one
corrective (invalidating K) and one forward (admitting K' via the ordinary
admissibility path). The two must be distinct and the latter must use a fresh
basis.

The categorical mistake to avoid:

```
old K invalidated  →  K "recovered"  →  authority restored
```

There is no recovered K. The corrective makes the failure of K explicit; it
does not reverse the failure. Recovery rebuilds *data, projections, indices,
caches.* It cannot rebuild *authority* from the failed authority that
preceded it.

This frames a cleaner distinction than ordinary incident-recovery vocabulary
allows:

- Recovery may restore *availability.*
- Re-entry restores *admissibility.*

Both are sometimes needed. They are not the same operation and they should not
share the same step.

## 7. Structural traps

Three families of system where the laundering vector recurs. None are claimed
to actually be laundering today; the section names the structural shape, not
the violation.

### The Revert Trap

Backups, rollbacks, time-travel debugging, point-in-time restore.

```
restore bytes ≠ restore authority
```

A restored database row, deployment artifact, or session snapshot brings with
it an implicit authority claim that may have been valid only in the original
context. Restoration silently re-authorizes if downstream evaluators read the
authority basis from the restored bytes.

### The Controller Trap

Reconciliation controllers, declarative-desired-state systems, drift remediation.

```
reconcile observed against desired only if desired remains admissible
```

A controller observing drift between desired and observed state can "heal" the
divergence in either direction. If desired-state authority has lapsed, healing
toward desired silently reasserts a basis that no longer holds.

### The Agent Trap

Persistent agent memory, multi-step delegation, long-running orchestration.

```
remembered approval ≠ current authorization
```

An agent that records "user approved X at time T under basis K" must distinguish
historical receipt from current authority. If K has since been invalidated,
the record may persist as evidence that *X was authorized at T,* but it cannot
function as authorization for *X is allowed now.* The agent can remember the
event without acting from it.

These are not exhaustive. They are three shapes that recur. The discipline
applies wherever (1) state can authorize action, (2) that state can become
invalid, and (3) a recovery path exists.

## 8. Forcing case (audit pending)

This section is a stub.

The candidate forcing case for the paper's empirical wedge is an audit of
specific corrective surfaces in agent_gov (the project that motivated the
formal kernel) for concrete realizations of the laundering vector. Seven
candidates have been enumerated:

1. `declare_policy_gap` becoming de facto permission to improvise policy
2. Evidence-gate failure triggering manual override without separate standing
3. Scope-governor escalation receipts being mistaken for authority rather than
   contestation
4. Continuity fork/promote converting remembered context into binding state
5. Premise invalidation cascading HARD→SOFT while leaving downstream permissions
   alive
6. Ultrastability freeze exits through "operator resolved" without re-entry
7. Rebuilt projection/cache being treated as recovered authority rather than
   reconstructed data

Each candidate is a structural shape, not yet a confirmed violation. The audit
walks each through the current implementation and either:

- identifies a concrete code path where the laundering bites — in which case
  that path becomes the paper's central case study and the slot decision tilts
  toward standalone; or
- rules the path out with a specific argument — in which case the candidate
  becomes anti-regression doctrine and the slot decision tilts toward P27
  fold-in.

If all seven rule out cleanly, the paper is honest about that: the contribution
is then preventive, naming the discipline that keeps a class of bug from
appearing rather than fixing one that did. That is still a paper, but it is a
quieter one.

This section will be filled in after the audit runs.

## 9. Related work

To be developed. Adjacent literatures that should be situated against, not
absorbed into:

- **Authorization logics and proof-carrying authorization.** Appel and Felten's
  proof-carrying authentication; subsequent proof-carrying access control work.
  These ask whether a particular action is justified by explicit logical
  evidence. The present work asks what transitions remain admissible after
  authority state has failed.
- **Formal methods for state machines.** TLA-style specification; Lean and
  related mechanization. The present work is a small instance of the genre,
  not a methodological contribution to it.
- **Capability systems and revocation.** The literature on how to revoke
  capabilities cleanly. The present work is downstream of revocation: given
  that revocation has occurred, what transitions remain valid.
- **Incident recovery and resilience engineering.** NIST CSF Recover; SRE
  postmortem practice. The present work names the distinction these
  frameworks elide: restoration of operations versus restoration of authority.
- **Cybernetic governance.** Beer's Viable System Model and adjacent
  management-cybernetics work. The present work is narrower: not "organizations
  as control systems" but "authority-bearing state machines as objects with
  characteristic failure modes."

The contribution is not "we discovered authorization." It is recovery
semantics after authorization-state failure. Related work should not eat the
paper.

## 10. Limits and non-goals

What the discipline does not do:

- It does not prove all governance systems safe. It defines an obligation that
  systems claiming corrective recovery must discharge.
- It does not solve distributed consensus.
- It does not prescribe a global authority ledger or a single canonical schema
  for governance state.
- It does not prevent bad forward authorization. Forward transitions can mint
  garbage authority; that is a separate problem with separate machinery.
- It does not define application-specific evidence semantics; what counts as
  basis is the responsibility of the concrete evaluator.
- It does not address evaluator mutation. The preorder is parameterized by env;
  changing env is a separate laundering vector and a separate theorem.
- It does not require authority logic to be monotonic in evidence.
  Authorization is expected to be nonmonotonic — revocation, expiry,
  invalidation, and contestation all retract prior conclusions. Corrective
  monotonicity is a path property scoped to corrective transitions, not a
  global property of the underlying authority logic.
- It does not make emergency powers safe by naming the corrective/forward
  split. It only ensures that emergency power grants cannot be smuggled inside
  cleanup transitions.

What it does:

> Systems claiming corrective recovery must show that their corrective
> transitions do not increase the authorized action set, and that authority-
> increasing recovery transitions are separately classified and use fresh
> admissible basis.

That is the load-bearing sentence. Everything else is scaffolding.

## 11. Open questions

Questions deferred to subsequent work, in roughly decreasing order of how
likely they are to bite:

1. **The seven-path audit (§8).** Until run, the empirical content of the paper
   is unfixed.
2. **Receipt schema split.** The current Lean kernel classifies `recordReceipt`
   as neutral on the assumption that receipts are evidentiary ingest, not
   authority admission. If a future receipt schema makes receipts directly
   authority-relevant, the constructor must split: `recordReceipt` neutral,
   `admitReceiptAsBasis` (or equivalent) forward. Pinned in the Lean file's
   open-questions footer.
3. **Re-entry as a first-class transition.** Currently expressible as a
   sequence (corrective then forward). If `requireReentry` becomes a single
   transition, it must be classified corrective and must not by itself create
   authority; the forward half lives in a separate constructor.
4. **Fork-versus-promote.** Continuity fork is corrective. Promotion of a
   forked lineage to authority-bearing must be a separate forward transition,
   never a side-effect of fork.
5. **Evaluator mutation is forward, not corrective.** Corrective monotonicity
   is stated relative to a fixed evaluator `env`. Changing the authority
   evaluator is itself authority-relevant and must be modeled as a forward
   transition, not as corrective recovery. Otherwise a system can keep
   governance state fixed while laundering authority through interpretation
   changes.
6. **Same-basis independence.** The non-laundering corollary is same-basis.
   Future work must define when a fresh basis `K′` is derivationally
   independent from failed basis `K`, rather than merely syntactically
   distinct. Without such a relation, `K` could be repackaged as `K′` and
   authorized through a forward path while preserving the spirit of
   laundering. Requires the currently-opaque `AuthorityClaim` to gain
   derivation-lineage structure; not a Lean change yet.
7. **Higher-order authorization carve-out.** The doctrine note "authority-
   increasing recovery requires a separate higher-order authorization path"
   becomes, in this kernel, simply: the higher-order path is a transition not
   classified corrective. There is no special exception type. If a future
   construct seems to need an in-corrective authority bump, that is the
   signal to refactor, not to add an exception flag.
8. **Typeclass promotion of `CorrectiveMonotone`.** Currently kept as an
   explicit-witness structure carried by `RecoveryEnv`. Promoting to a
   typeclass — so any `DerivationEnv` in scope automatically resolves a
   monotonicity instance — is premature while the obligation shape is still
   moving. Reconsider after the first concrete `BasisDerivation` reading
   `RevocationStore` lands and the obligation stops being vacuous.

## Notes on framing

A handful of register notes for the eventual paper.md draft:

- AG (agent_gov) is the lab animal that motivated the discipline. AG should
  appear in introduction motivation and possibly as an implementation note,
  not as the object of the paper. The object is authority-bearing state
  machines in general.
- The slogan "Don't let the repair path mint root" is talk/blog material, not
  paper material.
- "Conservation of authority" is wrong: authority can be created, just not by
  a corrective path. The right name is *corrective monotonicity* with the
  side note *no authority creation on corrective paths.*
- The strongest contribution sentence: "Authorization systems typically ask
  whether an action is allowed. We ask what transitions remain allowed after
  the authority basis for action has failed." Use it once, in the
  introduction.
- Length target: 8–12 pages. Not 15. Beyond 15 the formal-methods register
  starts borrowing prose from a different paper.

## Decision pointer

After the seven-path audit completes:

- If two or more candidates yield concrete laundering paths, draft as
  standalone P28 with the audited paths as central case studies.
- If all candidates rule out cleanly, fold this material into P27 as a
  formal-recovery-discipline section, citing it as anti-regression machinery
  rather than a corrective for an extant bug.
- Either way, the Lean kernel reference stands.
