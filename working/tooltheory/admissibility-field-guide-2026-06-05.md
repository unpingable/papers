# Admissibility field guide — workplace-demon register

**Filed:** 2026-06-05. **Status:** human-facing surface for the master-frame discipline. Holds workplace-demon examples that are NOT candidate kernels in their own right — each one maps to an existing corpus kernel, an existing project memory entry, or a candidate kernel filed elsewhere. The field guide makes the discipline operational in conversation; the doctrine map carries the formal layer.

**Lean custody (updated 2026-07-14):** field-guide doctrine, not a new kernel family. The two Markdown sketches below are historical source shapes and have been superseded by checked, formalization-leading Scratch modules: `~/git/lean/LeanProofs/Scratch/SignalAuthority.lean` and `~/git/lean/LeanProofs/Scratch/StatusConversionBinding.lean`. Neither is imported by `LeanProofs.lean`; Scratch contact does not ratify the field guide or testify to a runtime system.

## Why this file exists

The 2026-06-04 / 2026-06-05 multi-model side-quest exchange produced two genuinely new candidate kernels (`LogOnlyProvesEmission`, `AggregateWitnessRequiresJoin`) and seven additional patterns that are *field-guide-shaped*, not *kernel-shaped*. The field-guide patterns are real institutional speech acts — the sentences people routinely get away with saying — but each one is already governed by an existing corpus kernel or memory entry. Filing them as the master-frame discipline's *human surface* keeps them retrievable without multiplying candidate kernels under the cathedral-by-rename trap the side-quest audit refused.

## The schema (per [anti-laundering-doctrine-map.md] § The audit unit)

Every entry uses this seven-line shape:

```text
Demon:                    workplace-demon name
Common sentence:          the institutional speech act
Predicate being discharged: what the sentence claims to settle
Evidence actually present: what was actually shown
Required witness:         the indexed witness that would discharge the predicate
Refusal:                  the audit-unit statement
Meeting incantation:      the human-interface ask
```

The schema operationalizes the master frame: every demon is *the same kernel-shape* (a forbidden conversion of evidence into discharge without the indexed witness). The variety is at the demon-name layer; the discipline is uniform.

## Entries

### 1. Silence-as-Consent

- **Demon:** Silence-as-Consent
- **Common sentence:** *"Nobody objected."*
- **Predicate being discharged:** Consent / approval / no-objection.
- **Evidence actually present:** Silence / absence of recorded objection.
- **Required witness:** `SolicitationWitness` indexed to group, decision, time, and response window.
- **Refusal:** Silence cannot discharge no-objection without solicitation.
- **Meeting incantation:** *"Did you ask?"*

**Maps to:** [[project-signal-authority]] (null-laundering / missing ACK ≠ NACK). A repaired version of the handoff shape now lives in checked Scratch as `SignalAuthority.lean`; it binds the exact group, decision, and numeric response window, requires solicitation and complete-ledger coverage, and includes positive and collapse specimens. **Not a new candidate** — `NoObjectionRequiresSolicitation` is a sub-name of Signal Authority's existing scope.

---

### 2. Internal/External Status Mismatch

- **Demon:** Internal/External Status Mismatch
- **Common sentence:** *"Green externally,"* while internally yellow / degraded / risk-accepted / done-enough.
- **Predicate being discharged:** Admissible external status report.
- **Evidence actually present:** Internal/external status mismatch with no recorded conversion.
- **Required witness:** `StatusConversionWitness` indexed to the exact internal status, external representation, justification, authorizing party, scope, and time.
- **Refusal:** Inconsistent status cannot be reported externally without a conversion witness.
- **Meeting incantation:** *"What color is it internally?"*

**Maps to:** The master frame's conversion-witness binding rule (`anti-laundering-doctrine-map.md` § The master frame) plus existing `GreenIsNotCoverage` keeper + `ClosureEligibility.lean` (partial vs total) + `RecoveryMargin.lean`. A repaired version now lives in checked Scratch as `StatusConversionBinding.lean`, with exact source/target/report/time indices and externally checked issuer standing, scope, and conversion permission. The pattern remains an instance of the existing binding rule, not a new doctrine family.

---

### 3. Escalation-Without-Result

- **Demon:** Escalation-Without-Result
- **Common sentence:** *"We escalated it."*
- **Predicate being discharged:** Handled / resolved.
- **Evidence actually present:** Escalation handoff record.
- **Required witness:** `EscalationResult` indexed to the escalation, the receiving party, the decision, and the closure time.
- **Refusal:** Escalation cannot discharge resolution without a result.
- **Meeting incantation:** *"What happened after?"*

**Maps to:** Workflow-layer instance of [[aggregate-witness-requires-join-candidate-2026-06-05]] (escalation = partial witness for the handoff slice; result is the missing join with the closure slice). Also related to [[project-commitment-standing-decay]] (rhetorical continuity, operational revocation). **Field-guide entry under `NoSilentJoin`**, not a new candidate.

---

### 4. Access-Revocation-Is-Not-Offboarding

- **Demon:** Access-Revocation-Is-Not-Offboarding
- **Common sentence:** *"We revoked their access."*
- **Predicate being discharged:** Offboarded.
- **Evidence actually present:** One closed access surface.
- **Required witness:** Completed `OffboardingRecord` joining access revocation + knowledge transfer + relationship handoff + commitment reassignment + data retention + ownership transfer, each indexed to surface, scope, recipient, and time.
- **Refusal:** Access revocation cannot discharge offboarding without the joined record.
- **Meeting incantation:** *"Who owns their relationships / commitments / knowledge now?"*

**Maps to:** Workflow-layer instance of [[aggregate-witness-requires-join-candidate-2026-06-05]] (each surface is a partial witness; offboarding is the unified claim; the join is missing). Atomic-layer is already governed by ChatGPT's earlier *"access revoked is not a surface revocation"* argument + `CrossBoundary*` typed-surface refusals. **Field-guide entry under `NoSilentJoin`**, not a new candidate.

---

### 5. Attendance-as-Consent

- **Demon:** Attendance-as-Consent
- **Common sentence:** *"Alice was in the meeting, so she approved."*
- **Predicate being discharged:** `ConsentWitness Alice Decision`.
- **Evidence actually present:** Meeting attendance plus minuted decision.
- **Required witness:** `ConsentWitness` indexed to person and decision (explicit opt-in, not presence-as-proxy).
- **Refusal:** Attendance cannot discharge consent without explicit opt-in.
- **Meeting incantation:** *"Who consented, specifically?"*

**Maps to:** Same kernel as #1 (Silence-as-Consent) at a slightly different surface — presence as proxy for opt-in. Falls under [[project-signal-authority]]. **Not a new candidate**; field-guide variant of #1.

---

### 6. Legacy-Is-Not-Waiver

- **Demon:** Legacy-Is-Not-Waiver
- **Common sentence:** *"It's legacy."*
- **Predicate being discharged:** Requirement waived / security exception granted.
- **Evidence actually present:** Legacy status.
- **Required witness:** `WaiverWitness` indexed to system, requirement, scope, issuer, and time.
- **Refusal:** Legacy status cannot discharge waiver without an explicit waiver record.
- **Meeting incantation:** *"Where's the waiver?"*

**Maps to:** Related to ChatGPT's `TemporaryWaiversDoNotBecomePolicy` candidate from the workflow-layer round (named but not filed) and to [[project-commitment-standing-decay]] (rhetorical continuity vs operational revocation — the legacy framing is the same metabolism pattern). **Field-guide entry**; a separate formal artifact would require a distinct theorem shape and overlap audit, not a forcing case.

---

### 7. Blame-Without-Contributing-Factors

- **Demon:** Blame-Without-Contributing-Factors
- **Common sentence:** *"Human error."*
- **Predicate being discharged:** Root-cause analysis complete.
- **Evidence actually present:** Human action classification.
- **Required witness:** `ContributingFactors` / systemic context analysis, indexed to incident, surface, time horizon, and contributing-system reachability.
- **Refusal:** Blame attribution cannot discharge root-cause analysis without contributing factors.
- **Meeting incantation:** *"What systemic factors contributed?"*

**Maps to:** [[feedback-blameless-not-at-fault-free]] memory entry (*"load-bearing postmortem distinction"*). The keeper already names this distinction at the operational-discipline level. **Not a new candidate**; field-guide variant of the existing keeper.

---

## Historical Lean source sketches (superseded by checked Scratch)

The Lean handoff included sketches for two of the field-guide entries above (NoObjection / ReportedStatus). They are preserved here for provenance, NOT as authoritative code or new candidate files. Formal contact exposed real defects in both: the no-objection sketch treated an empty objection list as enough without solicitation coverage, window closure, or ledger completeness; the status sketch accepted any `some witness` while leaving its fields inert. The checked Scratch modules named above repair those defects and are authoritative.

### NoObjectionRequiresSolicitation (historical source shape)

```lean
namespace Admissibility

/-!
Field-guide name: Silence-as-Consent
Parent kernel: [[project-signal-authority]]

Historical source shape for SignalAuthority.lean. Superseded by the checked
Scratch module; not a separate kernel and not a runtime-conformance claim.

Doctrine:
Silence cannot discharge no-objection without solicitation.
A SolicitationWitness must be indexed to group, decision, and time window.
-/

inductive SolicitationMethod where
  | explicitCallForObjections
  | writtenReviewPeriod (startDate : String) (endDate : String)
  | formalConsentItem
deriving DecidableEq, Repr

structure SolicitationWitness
  (group : List String) (decision : String) where
  method   : SolicitationMethod
  askedWhom : List String
  openedAt : String
  closedAt : String

structure Objection where
  person : String
  objection : String
  timestamp : String
deriving Repr

inductive NoObjectionStatus
  (group : List String) (decision : String) where
  | silence
  | solicitedNoObjection
      (solicitation : SolicitationWitness group decision)
      (objections : List Objection)

def dischargesNoObjection
  {group : List String} {decision : String} :
  NoObjectionStatus group decision → Prop
  | .silence => False
  | .solicitedNoObjection _ objections => objections = []

theorem silence_cannot_discharge_no_objection
  (group : List String) (decision : String) :
  ¬ dischargesNoObjection
      (NoObjectionStatus.silence :
        NoObjectionStatus group decision) := by
  simp [dischargesNoObjection]

end Admissibility
```

### ReportedStatusRequiresConversionWitness (historical source shape)

```lean
namespace Admissibility

/-!
Field-guide name: Internal/External Status Mismatch
Parent kernel: master-frame conversion-witness binding rule
              (anti-laundering-doctrine-map.md § The master frame)

Historical source shape illustrating the binding-rule discipline applied
to internal-vs-external status reporting. Superseded by the checked Scratch
module; not a separate kernel.

Doctrine:
An inconsistent (internal, external) status pair cannot be admissible
without a StatusConversionWitness indexed to the exact pair, with
justification, authorizing party, scope, and time.
-/

inductive InternalStatus where
  | green | yellow | red | unknown
deriving DecidableEq, Repr

inductive ExternalStatus where
  | green | degraded | red | unknown
deriving DecidableEq, Repr

structure StatusConversionWitness
  (internal : InternalStatus) (external : ExternalStatus) where
  justification : String
  authorizedBy  : String
  scope         : String
  timestamp     : Nat

def consistentStatus : InternalStatus → ExternalStatus → Prop
  | .green,   .green    => True
  | .yellow,  .degraded => True
  | .red,     .red      => True
  | .unknown, .unknown  => True
  | _,        _         => False

def admissibleStatusReport
  (internal : InternalStatus)
  (external : ExternalStatus)
  (witness  : Option (StatusConversionWitness internal external)) : Prop :=
  consistentStatus internal external ∨
    match witness with
    | none   => False
    | some _ => True

theorem inconsistent_status_without_witness_inadmissible
  (internal : InternalStatus) (external : ExternalStatus)
  (hInconsistent : ¬ consistentStatus internal external) :
  ¬ admissibleStatusReport internal external none := by
  intro hAdmissible
  cases hAdmissible with
  | inl hCons      => exact hInconsistent hCons
  | inr hNoWitness => exact hNoWitness

theorem yellow_reported_green_requires_conversion_witness :
  ¬ admissibleStatusReport
      InternalStatus.yellow
      ExternalStatus.green
      none := by
  apply inconsistent_status_without_witness_inadmissible
  simp [consistentStatus]

end Admissibility
```

## Anti-cathedral discipline

Per the 2026-06-04 / 2026-06-05 audits:

- **Do not** build `LeanProofs/Admissibility/NoLift/`, `NoSilentJoin/`, or `NoChainMagic/` directories. These are doctrine-map *layer tags*, not module hierarchies.
- **Do not** create one Lean file per field-guide demon. Formalize only a coherent, non-duplicative proposition under its parent kernel; a downstream consumer is neither necessary nor sufficient.
- **Do not** rename a field-guide demon into a separate kernel from its parent. The Frankenstein Witness ↔ `AggregateWitnessRequiresJoin` split is *one object, two surfaces* — not two candidates.
- **Do** use the schema as the in-meeting / in-postmortem operational format. The discipline lives in the seven-line shape, not in the Lean.

## Cross-references

- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The audit unit and operational discipline — the doctrine-map sibling of this field guide.
- [[documentation-keepers]] — short-form keepers for the discipline: *"Indexed or it didn't happen"*, *"Existential laundry"*, *"This evidence does not discharge that predicate"*, *"Ask for the missing witness"*, etc.
- [`log-only-proves-emission-candidate-2026-06-05.md`](log-only-proves-emission-candidate-2026-06-05.md) — atomic-layer candidate kernel (`NoLift`).
- [`aggregate-witness-requires-join-candidate-2026-06-05.md`](aggregate-witness-requires-join-candidate-2026-06-05.md) — workflow-layer candidate kernel (`NoSilentJoin`); field-guide name *Frankenstein Witness*.
- [[project-signal-authority]] — parent kernel for entries #1 and #5.
- [[project-commitment-standing-decay]] — related to entries #3 and #6.
- [[feedback-blameless-not-at-fault-free]] — parent keeper for entry #7.

## Provenance

Field-guide schema and seven entries surfaced in the 2026-06-05 multi-model handoff dump (ChatGPT compiling the field-guide format → DeepSeek extending with Lean sketches → kernel-overlap audit confirming 2 genuine candidates + 7 field-guide entries → Claude Code filing this register with the naming-split discipline preserved). Anti-cathedral containment carried forward from the 2026-06-04 audit.
