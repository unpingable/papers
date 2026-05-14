# Admissibility-Trajectory Audit

**Status:** scout / audit-grounded / not primitive-promoted. Boundary object,
not framework.
**Originated:** 2026-05-14. claude-code-papers audit following an extended
chatty + web-Claude generative session on "closure standing" as a candidate
training-signal / witness-format for deployed tool-using model systems.
**Stance:** **Do not preserve the whole schema. Preserve the residue after
audit.**

The scouted material was substantially a re-coordinatization of existing
admissibility-family substrate. This note records what collapsed into the
existing kernel + working notes, what survived as residue, and the narrow
test that bounded the residue. Explicit non-promotion clauses at the end.

The filing decision follows the **Binding Reconciliation precedent**
(see [where-admissibility-fits-candidates.md](where-admissibility-fits-candidates.md)
§ Cross-cuts): when a synthesis-shaped vocabulary turns out to denote
structure already implemented in Lean + existing working notes, minting it
as a fresh primitive is *"the gloss eating its own substrate."* Captured
for retrieval, not promoted.

## Lineage

- Admissibility-decay family — [admissibility-decay-family-note.md](admissibility-decay-family-note.md)
- Temporal Basis Decay cluster — [primitives/AUDIT.md](primitives/AUDIT.md) § Cross-cutting findings
- Receipt doctrine (named-but-unfiled, third sibling of the boundary-calculus
  / admissibility-cybernetics / receipt-doctrine triad)
- FiatAdmissibility / SurfaceAuthorization / Corrective —
  `~/git/lean/LeanProofs/Admissibility/`
- Authority debt — [authority-debt-and-revocation.md](authority-debt-and-revocation.md)

---

## 1. What got scouted

Four candidate handles surfaced across a long generative session:

- **Quartet diagnostic.** *"The need for supervision over admissibility of
  commitment appears when evidence, consequence, feedback, and permission
  stop living in the same agent."*
- **Admissibility of commitment.** A discrete supervisory target over the
  trajectory by which evidence becomes authorized commitment, distinct from
  preference / step / abstention / calibration signals already inhabiting
  the LLM-supervision literature.
- **Witness / bearer language.** *"The bearer is not the model. The bearer
  is a ledger-addressable loop under a role."*
- **Withdrawn-vs-stale.** A code-audit trace (an Osprey audit where the
  `custody` tool falsified the original thesis before any binding had
  closed) forced a distinction between a closure that bound and was later
  lost (**stale**) and a provisional that was defeated before binding
  (**withdrawn**). Keeper form: *"A stale closure has lost authority. A
  withdrawn provisional never acquired it."*
  Concrete anchor: the trace was the soft-boundary thesis (*soft-boundary
  vs core-zone scar rate = 2.7×*) being defeated during analysis by a
  counting-bug correction; the corrected ratio was ~1.04×, so the durable
  finding became ambient custody weakness rather than a boundary-specific
  effect. The original thesis was defeated before binding; the published /
  retained finding was the corrected one.

Adjacent material that arose but is **not** in residue: a coupled
state-machine architecture (evidence machine + commitment machine + blocker
set + tempo), Lean module sketches `ClosureStanding.lean` v1–v4, a §1–§7
paper structure, a witness-format YAML. All set aside per the audit
guardrail.

---

## 2. What collapsed into existing substrate

| Proposed delta | Existing artifact | How it collapses |
|---|---|---|
| Authority gap (evidence sufficient, authority absent) | `FiatAdmissibility.lean` (artifact-kind × use-kind: `prestige_cannot_support`, `metaphor_cannot_derive`); `SurfaceAuthorization.lean` (cause-specific authority requires discriminating evidence); [authority-debt-and-revocation.md](authority-debt-and-revocation.md) (*delegation that cannot be withdrawn is authority debt*). | Already Lean-built. The dissociation between sufficient evidence and admissible action is the kernel's existing refusal axis. |
| Stale closure | [primitives/stale-binding.md](primitives/stale-binding.md). Failure predicate: decision bound to $S_{t_d}$ when truth has moved and no revalidation occurs before $t_c$. | Candidate primitive, P26 home. Covers the closed-then-stale half of the proposed distinction cleanly. |
| Evidence / commitment dissociation | Receipt half (`AuthorityVerdict` derives `DecidableEq, Repr` — descriptive, copyable) vs Authority half (`AuthorizedStep` consumed by `executeIfAllowed`, proof-bearing). | Structurally enforced in Lean by which constructors derive what. The "training signal teaches the model to produce admissible transitions" framing is a paraphrase of the existing kernel architecture, not a new structure. |
| Witness ledger as bearer-continuity substrate | Receipt doctrine + StateTransition partition (`PolicyStore`, `EvidenceStore`, `GapStore`, `RevocationStore`). The "Binding Reconciliation" annotation in [where-admissibility-fits-candidates.md](where-admissibility-fits-candidates.md) was already filed against this substrate and **explicitly not promoted** for the same reason. | Restatement of receipt doctrine with fresh terminology. Same filing decision applies. |
| Bearer = ledger-addressable loop under role | Same as above. Also: the kernel's three-discipline frame (construction / spend / serialization) already names *"non-replicability lives in a live custodian, not in the proof object."* | The "ledger-addressable loop under a role" is the live-custodian discipline named at a different abstraction layer. |
| Refusal held vs structural cannot | Signal Authority candidate (memory-tracked): two failure modes — unauthorized protocol extension vs authorized-but-illegitimate clause. [primitives/zombie-obligation.md](primitives/zombie-obligation.md) names Authority Decay as the dual to obligation-decay. | Already named at the protocol layer; dual already noted in the zombie-obligation entry. |
| Obligation graph survives justification graph | [primitives/zombie-obligation.md](primitives/zombie-obligation.md) headline form: *"the obligation graph survives the disappearance of the justification graph."* | Candidate primitive, already filed with the load-bearing form and a four-conditioned failure predicate. |

**Naming collisions:**

- `ClosureEligibility.lean` already exists in the kernel (NS-facing one-step
  closure module: *survival alone does not authorize closure*). A
  `ClosureStanding.lean` next to it would be adjacent-confusing.
- DCT (Deductive Closure Training, arXiv 2401.08574) owns "closure" in
  training-supervision contexts externally.
- "Authority gap" sits inside FiatAdmissibility / SurfaceAuthorization
  territory.

**Promotion-ladder check** ([tooltheory/lean-candidates.md](tooltheory/lean-candidates.md)
gate criteria — tool cited in non-trivial code + generator test + real
proof target + names physics): closure-standing meets none yet.

---

## 3. What survives the audit

Three residues, each with restricted register.

### 3a. Quartet diagnostic — keeper line, not new structure

> The need for supervision over admissibility of commitment appears when
> evidence, consequence, feedback, and permission stop living in the same
> agent.

Synthesis sentence. Names a deployment-substrate condition under which the
existing admissibility-decay family fires. Useful as a diagnostic trigger
when reviewing whether a system needs the existing apparatus — not a new
mechanism. Lives here as a keeper line; can also serve as the
"when-does-this-fire-on-deployed-tool-using-model-systems" trigger inside
[admissibility-decay-family-note.md](admissibility-decay-family-note.md)
when that note next gets touched.

### 3b. Blocker-not-missing-belief — prose lemma

> A blocker is not a missing belief. It is a failed condition for allowing
> belief to become binding.

Verbal form of a structural fact the Lean kernel already encodes:
`decideAuthority` returns `denied` (not `uncertain`), and `denied` is a
verdict about admissibility — not a calibration claim about the model's
confidence. Useful as a prose lemma when explaining the kernel's refusal
axis to readers conflating uncertainty and admissibility. No new
structure.

### 3c. Withdrawn-vs-stale — candidate sub-distinction

See § 4 for the narrow test.

---

## 4. The narrow test

**Question.** Does existing Stale Binding cover *"provisional defeated
before binding"*?

**Stale Binding's failure predicate** (from
[primitives/stale-binding.md](primitives/stale-binding.md)):

> $d$ is bound to $S_{t_d}$, $T_{t_d} \neq S_{t_d}$, and no revalidation
> occurs before $t_c$.

The predicate requires $d$ to be **bound** — committed against the cached
value with a consequence window already running. A provisional commitment
that has not yet acquired binding force is structurally outside this
predicate. The Osprey-trace case (provisional thesis $T$ contradicted by
the `custody` tool's witness $W$ *before* the consequence window opened,
then abandoned) does not satisfy SB's conditions because no $d$ was bound.

**Test outcome.** Stale Binding does not cover the withdrawn case — but
the reason is *not* that withdrawn is a missing failure mode. The reason
is that withdrawn is **not a failure at all**. It is the successful
operation of admissibility gating: the system encountered contradiction
inside the provisional window and refused to bind. No failure predicate
fires because nothing failed.

**What survives as observation.** The *asymmetry of downstream-obligation
inheritance* across two adjacent commitment trajectories:

| Trajectory | Did binding occur? | Downstream obligations | Failure mode? |
|---|---|---|---|
| bound → truth moves → stale | yes | inherited (prior actions taken under the bound schema may need review; downstream loops triggered) | **Stale Binding** |
| provisional → contradicted → withdrawn | no | none | **no failure** — successful gating |

The load-bearing claim is the *asymmetry*, not a new failure state. Stale
Binding's existing scope already handles the failure half; the withdrawn
half is what *doesn't happen* when admissibility gating works correctly.
Naming the asymmetry lets the Temporal Basis Decay cluster register it as
a boundary marker — *this is what the absence of the failure looks like* —
without minting a new primitive for a non-failure.

**Filing.** Non-failure / explanatory contrast under Temporal Basis Decay.
*Not* a new primitive. *Not* a sub-coordinate with its own predicate. The
asymmetry should be added as a one-line note in
[primitives/stale-binding.md](primitives/stale-binding.md) under "Do not
confuse with" when that file is next touched — distinguishing SB from the
withdrawn-before-binding case that resembles it but isn't a failure.

Suggested wording for the SB cross-reference (deferred until SB is being
edited for other reasons; not worth a standalone edit):

> **Withdrawn provisional** — provisional commitment defeated by
> contradicting evidence before $t_d$ closed any binding. No failure
> fires because no $d$ was bound. The asymmetry: a stale binding has
> inherited obligations; a withdrawn provisional has none.

**Keeper line (residue).**

> **A stale binding has inherited obligations. A withdrawn provisional has
> none.**

The test discriminator. When reviewing a closed-vs-not-closed trajectory in
any deployment, the question *"does the system inherit obligations from
this state?"* routes to Stale Binding (yes) vs admissibility gating (no).

---

## 5. Explicit non-promotion

The following are **explicitly not promoted** by this note:

- **No new framework.** "Closure standing" / "admissibility-trajectory
  supervision" / "authority-gap supervision" as named program — declined.
  The vocabulary covers structure already implemented in the admissibility
  kernel and named in the admissibility-decay family.
- **No `ClosureStanding.lean`.** A new module would duplicate
  `Corrective.lean`, `FiatAdmissibility.lean`, and `SurfaceAuthorization.lean`
  work while colliding with `ClosureEligibility.lean` on naming.
- **No paper dir.** P28 / numbered slot not earned. The
  boundary-calculus-program memory entry is explicit: the paper is a
  *possible* downstream artifact of forced material, not the destination
  for scouted vocabulary.
- **No witness-format spec.** The § 4 result (withdrawn-vs-stale is
  asymmetry, not failure) means no new auditable transitions need a fresh
  witness schema. Existing receipt doctrine plus the
  `EvidenceStore` / `RevocationStore` partition cover what's auditable.
- **No primitives/ entry.** Withdrawn-vs-stale lands as a one-line contrast
  inside Stale Binding's "Do not confuse with" (when SB is next touched),
  not as a separate primitives/ file.
- **No edit to other working notes from this filing.** The cross-reference
  suggestions for SB and the admissibility-decay-family note are
  deferred-touch — they ride along the next time those files are open for
  other reasons. Avoid the audit cascading into a sweep.

**Re-open triggers.** If any of the following fires, the audit's filing
decision is reviewed:

1. A deployment-substrate failure mode surfaces that *does* require
   provisional-withdrawn as a typed predicate. This would force a
   re-classification: Stale Binding sub-case, new primitive, or coordinate
   under Corrective.
2. An external citation or reader contact picks up the "admissibility of
   commitment" framing in a way that earns paper-shape (per the
   *terms-survive-reader-contact* gate that compression-becomes-authority
   already runs).
3. A Lean theorem in the existing kernel surfaces that requires the
   withdrawn distinction to typecheck. This would force a coordinate,
   possibly under `Corrective.lean`'s `StepClassification`.

Until one of those fires, this note is the artifact. The schema is not
preserved. The residue is.

---

## Keeper

> **A stale binding has inherited obligations. A withdrawn provisional has
> none.**

The test. Everything else is lineage management.

## Provenance

- 2026-05-14 generative session: chatty + web-Claude tag-team produced a
  multi-version state-machine architecture ("closure standing") with Lean
  v1–v4 sketches, a §1–§7 paper structure, and a witness-format YAML. The
  Osprey audit trace forced the withdrawn-vs-stale distinction in v4.
- claude-code-papers audit against the admissibility kernel + working-note
  tree found that most proposed deltas reduce to existing substrate; the
  Binding Reconciliation precedent was the controlling filing decision.
- Structure: chatty's five-section "option-B-with-ankle-monitors" outline
  plus an explicit non-promotion section. Filed as boundary object, not
  framework.
- Local retrieval for the Osprey / `custody` trace: claude project memory
  under the Osprey project (`project_custody_audit.md`,
  `project_osprey_findings.md`, `feedback_workflow.md`). The `custody`
  tool itself lives in a separate local audit repo; pointer kept generic
  to avoid leaking absolute paths in a push-public note.
