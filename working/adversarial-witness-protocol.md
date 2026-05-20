# Adversarial Witness Protocol v0.1

**Status:** protocol-shaped working note
**Authority:** exploratory / not implementation doctrine
**Do not treat as NQ/AG spec.**
**Nearest neighbors:** civic systems literacy, Chronopolitics, admissibility-decay family, NQ witness discipline, compression-becomes-authority, laundering-move watchlist, FiatAdmissibility / PublicReceiptRefinement, regime-change-with-backups, ground_stops_moving
**Core warning:** buildable shape does not imply build obligation.

> AWP is the observational dual of the admissibility kernel: where the kernel defines the conditions under which a binding may be admissible, AWP defines observable contradiction patterns indicating that declared admissibility has decoupled from operational practice.

The repo skeleton at § 9 is **evidence the artifact could be operationalized, not permission to operationalize it.** The artifact embodies its own thesis (refuses to certify itself, ships its own tombstone, slogan is *"don't trust the monitor"*). Treat that as a recognition-event, not as doctrine.

Tiny goblin version: *AWP is not a tool. It is a refusal pattern with YAML tendencies.*

---

## 0. Purpose

This protocol does **not** certify legitimacy.

It produces contestable evidence of contradictions between:

[
DeclaredProcess
]

and:

[
ObservedBehavior
]

The monitor is not a judge, auditor, regulator, or priest. It is a witness generator.

Its only valid output is:

> "Under this aperture, using this method, these contradictions were observed."

No green lights. No maturity scores. No "overall health." No vibes dashboard.

AWP findings identify observable contradictions between declared process and observed behavior. They do not, by themselves, attribute cause. A contradiction may indicate capture, corruption, overload, temporal-basis decay, implementation lag, or another failure mode. The protocol produces contestable exhibits, not motive claims.

## 1. Core claim shape

Every finding must fit:

```text
DECLARED:   The system claims X.
OBSERVED:   We observed not-X or materially divergent-X.
APERTURE:   Here is what we could and could not see.
METHOD:     Here is how the observation was produced.
EVIDENCE:   Here are the receipts.
CONTEST:    Here is how this finding can be challenged.
STATUS:     Provisional / contested / superseded / withdrawn.
```

If it cannot fit that shape, it is not a finding. It is commentary. Commentary is allowed. It just doesn't get to wear the badge.

## 2. Minimal contradiction schema

```yaml
finding_id: AWP-YYYY-NNNN
title: ""
declared_process:
  source: ""
  quote_or_summary: ""
  observed_at: ""
observed_behavior:
  description: ""
  observed_at: ""
  data_sources: []
contradiction_type:
  - decorative_appeal
  - override_groove
  - asymmetric_friction
  - scope_creep
  - standing_disparity
  - receipt_without_constraint
  - vocabulary_convergence
  - evidence_enclosure
  - freshness_theater
aperture:
  visible: []
  not_visible: []
  known_biases: []
method:
  collection_steps: []
  transformation_steps: []
  reproducibility: ""
evidence:
  receipts: []
  hashes: []
  timestamps: []
contestability:
  how_to_dispute: ""
  required_counterevidence: []
status: provisional
```

Ugly. Good. Beauty is how dashboards breed.

## 3. First contradiction families

Start with boring patterns. The boring ones survive contact.

### A. Decorative appeal

```text
Declared: Appeals are available and meaningful.
Observed: Appeals rarely or never alter outcomes.
Signal: appeal_success_rate ≈ 0 despite nontrivial appeal volume.
```

Refusal line:

> "Contestability exists on paper but does not appear consequential under observed conditions."

### B. Override groove

```text
Declared: Emergency override is exceptional.
Observed: Override recurs by actor, scope, reason, time, or domain.
Signal: same override pathway becomes operationally routine.
```

Refusal line:

> "The exception path appears to be functioning as the effective constitution."

### C. Asymmetric friction

```text
Declared: Process is neutral.
Observed: similarly situated actors face materially different delay, burden, denial, or review depth.
Signal: time-to-standing / time-to-resolution divergence.
```

Refusal line:

> "The process may be formally equal while operationally classed."

### D. Receipt theater

```text
Declared: Logging creates accountability.
Observed: Receipts accumulate without constraining future decisions.
Signal: repeated violations with no changed rule, blocked action, reversal, sanction, or required review.
```

Refusal line:

> "The receipt functions as memorialization, not constraint."

### E. Scope creep

```text
Declared: Authority is limited.
Observed: limited grants become adjacent grants, then standing assumptions.
Signal: boundary expansions without explicit ratification.
```

Refusal line:

> "Prior bounded authorization appears to be converting into inherited authority."

### F. Vocabulary convergence

```text
Declared: The monitor is adversarially independent.
Observed: The monitor adopts the target's terminology, framing, success language, or euphemisms before independent evidential convergence.
Signal: lexical convergence without corresponding evidence convergence.
```

Refusal line:

> "The witness may be importing the target's interpretive frame before the contradiction has been independently resolved."

More bluntly:

> "The monitor has started speaking the defendant's language."

This is the family most likely to be missed because it doesn't trip behavioral counters — it trips lexical ones. It also has the highest false-positive risk (some vocabulary is the only available technical vocabulary), so the signal needs paired evidential divergence, not lexical convergence alone.

## 4. No-aggregation doctrine

Promoted from UI rule to structural commitment. The interface rules at § 7 are downstream of this.

> **Contradiction evidence must not be collapsed into a single health, trust, legitimacy, or compliance value.**

Refusal line:

> Roll-up converts witness into certifier.

A contradiction log is annoying. A score is manageable. A score can be optimized, explained, purchased, litigated, or put in a slide deck with a tasteful gradient. Aggregation is the vector by which witness-shaped artifacts get re-shaped into certifier-shaped artifacts.

This is not presentation polish. It is structural.

[
ContradictionLog \not\rightarrow HealthScore
]

## 5. Capture tripwire checklist

The monitor downgrades its own adversarial standing if any of these become true:

```yaml
capture_tripwires:
  exclusive_data_access: false
  nda_bound_operation: false
  pre_publication_review_by_target: false
  target_funding_dependency: false
  target_board_or_governance_seats: false
  legal_veto_over_findings: false
  dashboard_replaces_receipts: false
  health_score_added: false
  partnership_language_adopted: false
  staff_migration_from_target_above_threshold: false
  method_not_forkable: false
  findings_not_reproducible_by_others: false
```

Status transition:

```text
external_witness → recognized_witness → capture_risk → absorbed_or_compromised
```

Important: **recognized_witness** is not promotion. It is a warning state.

## 6. Tombstone template

Every witness project ships this on day one.

```markdown
# Tombstone Conditions

This project's outputs should no longer be treated as adversarial evidence if:

1. We receive funding from monitored parties.
2. We accept exclusive access unavailable to independent reproducers.
3. We submit findings for pre-publication review by monitored parties.
4. We replace contradiction logs with aggregate health scores.
5. We certify institutional legitimacy or compliance.
6. Our method cannot be independently rerun.
7. Our governance becomes materially dependent on the systems we monitor.
8. Our public outputs omit aperture, evidence, method, or contestability.
9. Our findings become primarily brand outputs rather than reproducible exhibits.

If these conditions are met, fork the method and measure us.
```

That last sentence is the load-bearing one.

## 7. Interface rule

The UI must resist greenwashing. The doctrinal commitment is § 4.

Allowed:

```text
contradiction log
finding table
receipt bundle
trend list
differential treatment table
override frequency table
appeal consequence table
method notes
aperture warnings
```

Forbidden:

```text
overall legitimacy score
red/yellow/green health indicator
trust badge
certified independent seal
compliance grade
single executive summary number
```

If the interface can be screenshotted into "Everything is fine," it is already half-dead.

## 8. The one-line doctrine

> A witness may produce exhibits. It may not become the authority that its exhibits are supposed to constrain.

That's probably the kernel.

The rest is machinery.

## 9. Repo skeleton

**Suspiciously buildable. Do not implement without a forcing case.** Kept here as evidence the artifact has implementable shape, not as a build queue.

```text
adversarial-witness-protocol/
  README.md
  doctrine/
    purpose.md
    non-certification.md
    capture-tripwires.md
    tombstone.md
  schemas/
    finding.schema.yaml
    receipt.schema.yaml
    aperture.schema.yaml
    contestation.schema.yaml
  examples/
    decorative-appeal.yaml
    override-groove.yaml
    asymmetric-friction.yaml
    receipt-theater.yaml
    scope-creep.yaml
    vocabulary-convergence.yaml
  tools/
    validate-finding.py
    hash-receipts.py
    render-contradiction-log.py
  docs/
    how-to-fork.md
    how-to-contest.md
    known-failure-modes.md
```

Very glamorous. Truly, the revolution will be valid YAML.

## 10. First working slogan

> Don't trust the monitor. Reproduce the contradiction.

That's better than "if it can't be forked, it's captured," though both belong.

The latter is doctrine. The former is user-facing.

## 11. Final guardrail

Do **not** let this become "Neutral Ambassador Certified Adversarial Liveness™."

That way lies lanyards.

The right artifact is smaller, meaner, and more useful:

> a portable contradiction format with receipts, aperture, contestability, and a built-in death label.

The first flashlight manual does not need to solve legitimacy.

It needs to make wet floors harder to relabel as "ambient moisture events."

---

## Provenance and constellation notes

### Origin

Drift trajectory: "human alignment with math" prompt → ping-pong → AWP v0.1 with YAML and a tombstone clause. The original prompt was a category error (universal sink). What came out is its anti-shape: a deliberately small, non-aggregating, self-terminating thing that refuses to certify anything.

### Position relative to existing constellation

**Not NQ-witness.**
NQ-witness asks: *"Can this system truthfully make this operational claim?"* — failure-domain testimony.
AWP asks: *"Can this institution's declared process be contradicted by observable behavior?"* — process-contradiction testimony.
Sibling, not child.

**Not Agent Governor.**
AG decides whether an action has admissible authority. AWP produces contradiction exhibits that could eventually feed such a decision but has no business becoming an authority kernel.

**Not Verifier / Standing / Custody spine.**
Those are spine pieces. AWP is an external flashlight format. It should not get too close to the spine unless there is a concrete consumer. Otherwise: parasite enters via architecture diagram.

### Family-to-primitive lineage (each contradiction family has a near-neighbor already in the kernel)

| Family | Existing-primitive neighbor |
| --- | --- |
| Decorative appeal | FiatAdmissibility — contestability declared but not constructed |
| Override groove | laundering-move-watchlist — "exception → norm" crossing |
| Asymmetric friction | non-reciprocal-admissibility-flow — process shapes admissibility differently for different actors |
| Receipt theater | FiatAdmissibility / PublicReceiptRefinement / signal-authority — record without binding |
| Scope creep | laundering-move-watchlist Section A — limited-standing → stronger-role |
| Vocabulary convergence | compression-becomes-authority — defendant's compressed terms shape witness's admissibility space |

The lineage being visible is the point. The observational-dual framing at the top of the file is the structural answer to "is this a parallel framework?" (no — it's the outward-facing complement to the same boundary).

### Candidate handles surfaced but not promoted

Two handles named here for future review, not for canonization:

1. **Pre-committed revocation / advance tombstone.** The tombstone clause is a *voluntary admissibility revocation* — the witness pre-publishes the conditions under which its own outputs should stop counting, before the incentives to obscure those conditions exist. Composes with the admissibility-decay family as its voluntary-revocation counterpart. Not promoted; needs a non-AWP instance before it earns a handle.

2. **Aggregation-as-authority-laundering.** Specific subset of the laundering-move family: roll-up of witness-shaped artifacts into certifier-shaped artifacts. The keeper line *"roll-up converts witness into certifier"* is sharper than the generic laundering-move template gives it credit for. Not promoted; check against existing laundering-move-watchlist entries before minting.

### Known under-fit (addressed at § 0)

AWP's contradiction families could be read as capture/corruption evidence. The § 0 motive-claim paragraph carries the guardrail: contradictions are evidence of declared-observed gap, not attribution of cause. Capture, corruption, overload, temporal-basis decay, and implementation lag all surface as the same family of observable contradictions; AWP does not do the work of distinguishing them.

### Kernel backing (audit 2026-05-19)

The § 0 motive-claim guardrail is *not* a new theorem. It is the prose articulation of existing no-attribution kernels in `LeanProofs/`:

- **`CollapsedSurface.collapsed_surface_not_identified`** — a collapsed surface identifies no cause. *"If two distinct causes render to the same public surface, that surface cannot identify either cause."*
- **`PublicReceiptRefinement.refines_without_identification`** — refinement narrows but does not identify. *"Narrowing is not identification."*
- **`Admissibility.SurfaceAuthorization`** keeper line — *"A collapsed surface may authorize inquiry. It may not authorize attribution."*

Kernel-overlap audit performed 2026-05-19 against `FiatAdmissibility`, `PublicReceiptRefinement`, `WitnessInvariance`, `SurfaceAuthorization`. Result: no new Lean module warranted. AWP's three proposed claims either collapse into existing kernel theorems (Claim 2 above), into existing artifact-classification machinery (Claim 1 → `FiatAdmissibility.classify`), or into structural type discipline that is not theorem-shaped (Claim 3). The candidate handles *advance tombstone* and *aggregation-as-authority-laundering* are held as named-not-promoted pending non-AWP recurrence.

The observational-dual claim at the top of this file is concrete: AWP is the protocol-level articulation of the same no-attribution discipline the kernel already proves.

### Meta-risk: the protocol is itself a vocabulary-convergence target

"Adversarial witness," "tombstone," "capture tripwire" are colorable terms. Institutions will adopt them. The vocabulary-convergence family in § 3.F applies recursively to AWP's own terminology. The tombstone conditions are partly a defense against this — but vocabulary capture can happen even when the formal tripwires haven't tripped.

### Build status

Do not build. Write it down sharply. Maybe turn into an essay later (Chronopolitics-adjacent, civic systems literacy register). The repo skeleton should stay as evidence that it *could* be operationalized, not as permission to operationalize it.
