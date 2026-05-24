# Authority-Flow Linting

Status: working note; non-canonical; not public surface.

This note records the portable application of the Admissibility Calculus's central discipline: treat authorization as a derived judgment, and audit every place a system tries to smuggle derived authority back into the premise context.

## Keeper

> **Authority must be derived at the boundary where it is spent.**

Sharper diagnostic form:

> Applications appear anywhere a system mistakes a previously derived authorization for fresh premise authority.

Sibling slogan (the operational name for the discipline):

> **Cut discipline for authority-bearing systems.**

The phrase is cursed. The diagnostic is portable.

## Where the discipline travels

### 1. Agent / tool governance

Bad pattern:

```
Tool said X is okay.
Therefore future agent treats X as standing authority.
```

Discipline:

```
Tool output may be evidence.
Evidence must re-enter as basis / standing / scope.
Authorization is re-derived at action time.
```

Direct overlap with the existing `agent_gov` / Governor spine. Agent memory, tool receipts, planner outputs, prior approvals stop being self-authorizing context atoms.

### 2. NQ claim preflight

Bad:

```
Claim was previously emitted ∈ Γ
────────────────────────────────
Claim is allowed again
```

Discipline: claims are conclusions, not premises. Blocks stale testimony, copied findings, shape-compatible fake findings, *"dashboard said green yesterday"* laundering.

### 3. Wicket / CI preflight

Catches:

```
Previous job approved diff.
Therefore current merge is admissible.
```

The previous job's result is evidence with provenance: commit hash, scope, time, repo state, policy version, actor / action. Any drift requires re-derivation. Prevents CI approval replay, *"green build from wrong commit,"* policy-check cargo culting.

### 4. Standing / capability systems

Grammar for the difference between

```
has token
```

and

```
token currently authorizes effect E under state S.
```

A bearer token, receipt, macaroon, lease, role assignment, or standing grant sits in Γ only as candidate evidence. The judgment layer asks whether it *currently* derives authority under the current state. Maps directly to revocation, expiry, audience, replay, scope, PoP/bearer distinctions.

### 5. Memory systems

Bad memory architecture:

```
Memory says user prefers X.
Therefore act on X.
```

Discipline:

```
Memory says user preferred X at t under context C.
Current request requires use-kind U.
Does this memory have standing for U now?
```

Persistent memory becomes **orientation**, not authority. Continuity is not standing — exactly the agent-memory cringe vector. Composes with [[feedback-register-capture-session-hygiene]] (same axis, structural form).

### 6. Compliance / audit workflows

Much compliance is authority laundering with better fonts. Bad:

```
Control exists.
Therefore risk is controlled.
```

Discipline:

```
Control evidence + scope + freshness + owner + test result
──────────────────────────────────────────────────────────
May claim control effectiveness
```

Catches *"policy document exists"* being laundered into *"policy operates."*

### 7. Incident response / postmortems

Distinguishes:

```
Mitigation applied        (evidence)
Incident condition resolved  (derived claim requiring observation)
```

Blocks the classic ops move: *"We restarted the service, therefore it's fixed."* No — that was a corrective action; resolution requires a new judgment. Maps to `Corrective.corrective_no_authority_laundering` exactly.

### 8. AI evaluation / model cards / benchmarks

Bad:

```
Model scored high on benchmark.
Therefore model is safe for deployment class D.
```

Discipline:

```
Benchmark result has artifact-kind K.
Requested use has use-kind U.
Does K license U?
```

`FiatAdmissibility` territory. Score as evidence, not authority.

### 9. Legal / institutional delegation

```
Office issued order.
Therefore order is binding.
```

Discipline:

```
office standing + jurisdiction + procedure + time + scope + non-revocation
──────────────────────────────────────────────────────────────────────────
order binds target action
```

Separates speech act from operational standing. [[project-commitment-standing-decay]] lives here.

### 10. The reusable kernel: unsafe-cut detection

The deep application is a portable audit question:

> **Where does this system use an intermediate conclusion as if it were a primitive premise?**

That's the laundering detector. Specimen unsafe-cuts:

- Observed healthy → marked healthy → allowed rollout
- User consented once → consent token persists → future unrelated processing allowed
- Risk accepted → risk disappears from blocking path
- Expert reviewed → claim becomes authoritative outside review scope
- AI summarized policy → summary used as policy

Each one is the same shape: an intermediate derivation gets smuggled into the next layer's context as a primitive.

## Why this is the portable primitive

Not "sequent calculus for institutions." Not "admissibility logic." The portable thing is much smaller and much sharper:

> **Cut discipline for authority-bearing systems.**

The audit form: at every boundary where authorization is *spent* (a state mutation, a downstream commitment, a binding decision), require fresh derivation from current evidence. Reject any pattern where a previously derived conclusion enters the next derivation as if it were a primitive premise.

This is what makes the discipline travel beyond the Lean kernel. The kernel is the **specimen** — a small, machine-checked example of the discipline applied to one domain (governance state transitions). The discipline itself is reusable wherever authority flows and could be laundered through composition.

## What this is not

- Not a new public surface for the Admissibility Calculus. The 1.0 surface is unchanged.
- Not a marketing pitch for ten new repos. The applications listed are diagnostic targets, not build targets.
- Not a claim that the existing kernel solves any of these domains — it specifies the *shape* of the refusal, not the implementation in each domain.
- Not a sequent calculus, not a process calculus, not an admissibility logic. See [[judgmental-presentation]] § Vocabulary correction for the false-friend hazard with "admissible."

## Cross-references

- [[judgmental-presentation]] — the explanatory reading-aid layer over the existing kernel.
- [[judgmental-fragment-starting-point]] — design constraint for any future sequent-style work (authority is conclusion not atom; no free Γ; the judgmental layer can explain, it cannot mint).
- [[truce-doctrine]] — companion: contradiction blocks authorization; remediation handles force outside authorization.
- [[project-laundering-move-watchlist]] — generator: *artifact with limited standing crosses boundary into stronger role without earning transition.* The unsafe-cut audit is the proof-theoretic shadow of this watchlist.
- [[feedback-green-vs-promised]] — sibling discipline at a different boundary: compiled ≠ public; derivable ≠ authoritative.
- Kernel reference: `Execution.AuthorizedStep` (`~/git/lean/LeanProofs/Admissibility/Execution.lean:82`) — the structure-literal enforcement of "both proofs required at the spend boundary."
- DOI: `10.5281/zenodo.20369489` (concept) / `10.5281/zenodo.20369490` (v1.0.1).
