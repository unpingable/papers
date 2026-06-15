# Fork modes & the contraction asymmetry (branching under a linear accountant)

**Filed:** 2026-06-15 in `tooltheory/`. **Status:** doctrine note / **consumer-specimen, NOT a
new kernel.** Positions a branching-layer design against existing refusal kernels. The AG
runtime decisions (singleton topology, capability wire format, `state_epoch`) are
**AG-Claude's territory — recorded here as the forcing consumer, not authored here.**
Name-early; **no Lean build** (the formal core is ContractionHinge generalized — see Overlap).

## The keeper invariant

> **A fork may duplicate information, but not spendability.**
> (Equivalently: duplication of *information* is admissible; duplication of *authority* is not.)

Branches may freely copy: observations, claims, hypotheses, candidate plans, unsigned
proposals, read-only snapshots. Branches may NOT copy: authority to mutate, budget to spend,
scarce capability, promotion standing, durable consent, revocation-sensitive permission. For
those they get a **partition** or an **escrowed speculative token**, never a copy. Let the
ghosts multiply; don't give them the checkbook.

## The formal handle (the only genuinely-new bit)

A **contraction asymmetry by object-kind**: information lives in a copyable (Cartesian,
structural-contraction-allowed) fragment; authority/spendability lives in a linear
(no-contraction) fragment. A fork *is* the contraction structural rule applied at the
branching layer — admissible on the information fragment, refused on the authority fragment.

Rhymes (heuristic, not reduction): **substructural logic** (the contraction rule; linear vs
intuitionistic), **separation logic / bunched implications** (additive copyable context vs
multiplicative separating context), and for the serialization boundary, **CALM / CRDT**
(monotone-commutative vs non-monotone). Belongs in the *linear credentials* bucket of
[`admissibility-related-work-map.md`](admissibility-related-work-map.md) — a new rhyme for it.

## Fork taxonomy (mapped to the receipt ladder)

| Mode / state | Parallel? | Rollback cost | Spend? | = existing kernel |
|---|---|---|---|---|
| **ReadOnlySnapshot** (observe / claim) | yes | none | no | — free fan-out; most branching lives here |
| **Speculative — pre-standing** | yes | **free** (no durable footprint) | no | **standing-before-spendability**, below the standing line |
| **Speculative — standing held, not yet spendable** | yes | **costs a standing-revocation** (receipted mutation — NOT free) | no | the off-by-one-rung gap; *candidate = LA `deposit`↔`basis` interval* |
| **LinearSplit(budget)** — standing + basis | yes | n/a (committed; budget conserved) | yes, sub-budget; `Σ children + reserve ≤ parent` | **ContractionHinge** |
| **Outcome-dependent** | partial — must serialize | — | after dependency resolves | read-after-write on authority state (*continuity*'s job) |

The third row is web-claude's correction: free rollback expires at the **standing** boundary,
strictly earlier than spendability (see Refinements). Losers in any speculative row emit
revocation / non-promotion receipts.

Rule: **a speculative branch may produce proposals, not effects.** Promotion converts
`candidate_output → committed_authority` only through Governor admission. Until promotion the
output is *unknown / candidate*, which by the corpus's own doctrine cannot render as ok.

## The serialization boundary (precise)

Not "the Governor serializes everything." Precisely:

> **The Governor serializes non-commutative authority transitions.**

On the receipt ladder: observe ∥, claim ∥, **sign → serial** (the only place the singleton
bites), **promote → serial** (mutates durable authority). Commuting transitions (two observes;
two budget-split spends) need no order; non-commuting ones (`promote X` / `promote Y`;
`consume` / `revoke`; `B authorized iff A succeeded`) need total order — *the system refusing
to lie about causality*, not a scalability failure.

**Issuer / verifier split** (= the Governor-is-not-the-microkernel invariant): the **issuer is
singleton** (one identity of record, so the verdict algebra stays coherent); **verifiers are a
herd** (the verdict is signed data, verified and acted on in parallel). Singleton *authority* ≠
singleton *loop* — welding the two is the panic, not the constraint.

## Overlap audit (why this is NOT a new kernel)

Every mode resolves to an existing refusal:

- LinearSplit = **ContractionHinge** at the fork (Lean specimen exists).
- SpeculativeCandidate = **standing-before-spendability** / `validity-spendability-split.md`.
- Capability lifetime = **SurfaceTypedRevocation** at the system layer.
- Outcome-dependent serialization = read-after-write on authority state (continuity).

So this is a **consumer-specimen** instantiating four existing refusals at the branching layer.
The only new handle is the *contraction-asymmetry-by-object-kind* framing, which is
ContractionHinge generalized to "information vs authority" — not a fresh kernel. Per
[[project-no-unifier-without-laundering]] / anti-acne: **do not mint a `ForkMode` kernel.** If a
Lean specimen is ever earned, it extends ContractionHinge. Name-early.

## AG-side (forcing consumer — recorded, NOT authored)

The concrete consumer is **`~/git/linearaccountant/` (LA)** — a Rust linear-capacity accountant
(`deposit` / `request_capacity` / `consume` / `revoke`); the fork primitive is unbuilt (0 hits)
and the consume path is frozen at v0. These are LA-/AG-Claude's runtime decisions; recorded so
the cross-tool seam is legible, not decided here:

1. **Signing throughput** — high sign-rate makes the singleton signer a true bottleneck
   (Amdahl). Every fix costs: batch-signing couples proposals (narrow-seam risk); sharding
   signing by domain works only if the 28/25 inventory partitions with no cross-shard edge;
   or keep signing cheap enough the serial rate doesn't matter.
2. **Revocation vs capability lifetime** — long-lived caps = parallel but weak revocation;
   short-lived = tight revocation but Governor back in the hot path.
3. **Outcome-dependent branches** — must serialize; likely continuity's domain.
4. **Throughput ≠ availability** — sharding helps throughput / hurts the single-authority
   story; consensus replication helps availability / does nothing for throughput. Don't let
   Raft get sold as a parallelism fix.

### The state-epoch footgun (cross-tool note for AG)

A signed capability must bind a snapshot/epoch (`state_epoch` / `state_root`) or parallel
verifiers all correctly verify the signature while acting against **different worlds**.
**Signature validity is not state validity.** Candidate fields: `issuer, policy_hash,
authority_scope, resource_scope, subject, decision, basis_receipt_hashes, state_epoch/state_root,
expiry, revocation_surface`. AG owns the wire format; this is the refusal it must encode.

## Refinements after LA contact (2026-06-15)

Web-claude correction, folded — the speculate/split line was drawn one rung too late, plus two
seam bugs and a residue:

**1. Off-by-one-rung (the new middle state).** Speculate-and-rollback earns its keep on one
premise: rollback is free. Rollback is free only while the branch has left *no durable
authority footprint* — and **acquiring standing IS a durable footprint** (recorded; undoing it
is a receipted standing-revocation). So free rollback expires at the **standing** boundary,
strictly earlier than spendability. The middle state — *standing held, not yet spendable* — is
speculative but its rollback already costs a revocation. (Table row 3.)

**2. Fork is resource-vectored, not branch-level.** Discipline is a property of
`(branch × resource)`. A branch may hold spend-authority over compute and propose-only over
privilege at the same instant → split the first, speculate the second, simultaneously. So
`fork(branch) → (branch, branch)` is the wrong primitive; linearity must close **per
resource-type independently**. Since LA isn't built to this point, type it resource-vectored
**now**, not retrofit. (This stiffens the contraction-asymmetry handle: contraction is refused
per-resource on the linear fragment, not per-branch.)

**3. The bug lives in the handoff, not either regime.** When a speculative branch promotes,
*kill-the-siblings* and *allocate-the-survivor's-budget* must be **one atomic act** through the
serialized promotion. Split them → either two survivors (double-spend) or dead siblings whose
notional budget never returns (leak). This is the non-commutative-transition serialization
point made sharp.

**4. The residue tail — rollback unwinds spend, not observation.** A speculative branch that
touched the world leaves append-only receipts in the witness layer (NQ) that outlive its
death: clean rollback of *authority*, append-only residue of *observation*. Fine only if
observation is side-effect-free — which, for the things a governor governs, it rarely is. (Same
shape as the readout arc: the witness layer is monotone/append-only; authority is the revocable
part.)

### LA grounding (interferometry — verified vs unverified)

Web-claude conjectured the middle state is *literally* LA's deposit-basis gap. Checked against
`~/git/linearaccountant/src/lib.rs` (Rust, single file, 725 lines):

- **Confirmed (vocabulary + separation):** LA has `deposit` (capacity pool), `request_capacity`
  → token, `consume` (spend), `revoke`, and a `basis_receipt` whose own comment is *"sealed
  pointer to a standing/watchbill/wicket receipt"* — i.e. **basis references standing; they are
  distinct objects**, leaving exactly the room for a "standing held, no basis to draw" state.
  `fork` / `speculat` / `rollback` = **0 hits** — the primitive genuinely isn't built, so "type
  it right now" is accurate.
- **NOT confirmed ("literally the same object"):** the consume/spend path is **frozen at v0** —
  `preflight_consume` returns only `ConsumePathNotThawed` ("no spend machinery exists to
  authorize against"). The deposit↔basis interval isn't *built* to point at yet; the
  basis→standing pointer is a field comment on a preflight stub. The conjecture is **plausible
  and vocabulary-aligned, not verified** — re-check when the consume path thaws.
- **Disposition:** the structural correction (free-rollback expires at standing) stands on its
  own. The "merge the fork-primitive task with the deposit-basis-gap task" payoff is a
  **candidate-if-confirmed**, not a confirmed merge. A Claude checking a Claude's synthesis
  claim: recorded the separation visible in the code, **withheld the co-signature on "same
  object."**

## Disposition

- Consumer-specimen, name-early, **no new kernel, no Lean build.**
- AG governor = forcing consumer; AG-Claude owns runtime / wire-format decisions.
- Book later gets the line: *parallelism is allowed everywhere except where the system would
  otherwise counterfeit consent* — flagged too-clean, therefore suspect.

## Cross-references

- `~/git/linearaccountant/` (LA) — the consumer codebase; fork primitive unbuilt, consume path frozen v0; `basis_receipt` → standing pointer is the deposit-basis-gap candidate.
- ContractionHinge (Lean scratch annex) + `working/validity-spendability-split.md` — the kernels this consumes.
- [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § linear credentials — home for the substructural / separation-logic / CALM rhyme.
- [[project-governor-doctrine]] / [[project-nightshift-forcing-consumer]] — AG cross-tool surface.
- [[standing-as-readout-no-free-standing-readout]] — sign is a governed readout; promote is a categorical transition; synchronic/diachronic split is the same seam.

## Provenance

Multi-model exchange, 2026-06-15 (Claude singleton / receipt-ladder / linear-tension analysis →
ChatGPT fork-taxonomy + duplication invariant + `state_epoch` footgun). Heavy synthesis; the
formal core is ContractionHinge generalized, recorded as a consumer-specimen specifically to
avoid minting a duplicate kernel.
