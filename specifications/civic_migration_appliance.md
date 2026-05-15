# Civic Migration Appliance: Jurisdictional Portability for Online Communities

**Date:** 2026-05-15
**Status:** Specification sketch (candidate / pre-implementation). Object model locked for stable terms; not implementation-binding.
**Frame:** Notary, not legislator. Evidence crosses; authority does not.
**Related:** `../working/regime-change-with-backups.md` (concept memo, prose-shape), `atproto_governance_transfer_proof.md`, `atproto_provenance_instrument.md`

## Promotion gate

This document locks **candidate** object names and invariants so the prose in the companion working note does not let the terms drift. It is not a protocol specification yet. Promotion to specification-binding requires:

- An implementation, protocol sketch, or receipt format that needs stable terms in production, OR
- A second independent design effort that adopts the same object names and finds gaps, OR
- A paper draft making the object names load-bearing in a formal claim.

Until then: terms are stable but not authoritative. MUST/SHOULD language is deliberately absent.

## Problem

Data portability has familiar mechanisms: exports, account migration, host portability. Community portability remains unsolved. Moving a community requires moving:

- membership and roles
- moderation history
- standing and sanctions
- unresolved disputes and appeals
- governance context (who decides what, under which rules)

The naive failure mode is to make all of this self-executing in the new jurisdiction — which silently transfers the old regime's authority into a new body that has not ratified it. **Authority laundering by import.**

The opposite naive failure mode is to drop all of it on exit — losing the community's memory of its own decisions, leaving the new body to re-discover documented harassers and unresolved disputes blind.

The appliance solves the problem between these two failures.

## Two stewardship layers

The appliance separates two roles that platforms fuse:

| Layer | Concern | Role |
|---|---|---|
| **Operational stewardship** | hosting, backups, migration plumbing, security, abuse-response infrastructure | the pipes |
| **Jurisdictional stewardship** | membership basis, standing, moderation inheritance, appeals, ratification, charter execution | the civics |

The appliance is operational-stewardship infrastructure that *exposes* jurisdictional stewardship as user-owned governance, without absorbing it.

## Three constitutional artifacts

Migration is a temporal process with three distinct artifacts, produced at three different moments.

### FOUNDING_CHARTER

Produced once, at community formation. Pre-commits exit policy *before crisis*.

```
FOUNDING_CHARTER
├── membership_basis              # who is a member, how membership is verified
├── ordinary_governance           # how the community makes decisions in steady state
├── moderation_authority          # who can moderate, with what scope
├── exit_policy                   # default migration charter to use if community moves
└── charter_amendment_policy      # how the charter itself can be amended
```

The exit_policy field is load-bearing. A community without pre-committed exit policy is one that will discover its constitution in a panic.

### EXIT_CHARTER

Produced once per migration event, when migration is invoked. Applies the FOUNDING_CHARTER's exit_policy to current conditions.

```
EXIT_CHARTER
├── who_counts_now                # eligible voting body under exit_policy + current state
├── prior_policy_applicable       # which FOUNDING_CHARTER rules survive into transition
├── what_has_changed              # context delta from founding to now
├── what_requires_ratification    # decisions the new jurisdiction must mint
└── what_gets_quarantined         # imported items held in non-executable state
```

### LANDING_RECEIPT

Produced by the new jurisdiction after ratification window closes. Authoritative record of what the new body accepted.

```
LANDING_RECEIPT
├── what_moved                    # accepted artifacts
├── what_failed                   # artifacts that did not transfer (technical)
├── what_was_rejected             # artifacts the new jurisdiction refused
├── what_was_quarantined          # held in advisory state, pending re-ratification
├── what_was_ratified             # imported items now binding in new jurisdiction
└── who_now_owns_the_decisions    # explicit authority assignment in new body
```

### PROVISIONAL_EXIT_CHARTER (legacy / unchartered case)

Used for communities that did not pre-ratify a FOUNDING_CHARTER. Historically this is most communities — Discord servers, subreddits, Mastodon instances, etc. that pre-date the appliance and never held a constitutional convention.

```
PROVISIONAL_EXIT_CHARTER
├── invocation_reason             # why migration is happening (server dying, fork, etc.)
├── claimed_membership_basis      # best-effort identification of eligible body
├── inheritance_default           # MUST be "advisory_only" — no binding authority transfers
├── post_landing_ratification_window  # fixed window in which new jurisdiction must ratify
└── escalation_path               # if window closes without ratification, what happens
```

A PROVISIONAL_EXIT_CHARTER cannot transfer executable authority. All inherited sanctions, roles, and standing-affecting decisions land in `advisory_quarantine` regardless of inheritance_default in any embedded charter. The new jurisdiction must mint its own authority within the post-landing ratification window or lose the imported governance state.

This preserves Invariant 1 (authority re-minting required) without making the appliance refuse the exact communities that most need migration. Tiny mercy from the municipal water authority.

## Migration types

```
chartered_migration            # FOUNDING_CHARTER pre-exists; EXIT_CHARTER derived from it
legacy_provisional_migration   # No FOUNDING_CHARTER; PROVISIONAL_EXIT_CHARTER governs
```

The appliance accepts both. The distinction is operational, not moral.

| Capability | chartered | legacy_provisional |
|---|---|---|
| Move content (posts, threads, media) | Yes | Yes |
| Move identity and membership records | Yes | Yes (best-effort identification) |
| Move moderation evidence as testimony | Yes | Yes |
| Transfer binding sanctions on arrival | Yes (per FOUNDING_CHARTER) | **No** — all inherited sanctions are advisory_quarantine |
| Transfer binding role assignments | Yes (per FOUNDING_CHARTER) | **No** — roles re-minted in new jurisdiction |
| Transfer binding standing decisions | Yes (per FOUNDING_CHARTER) | **No** — standing re-minted |
| Skip post-landing ratification window | Possible (per FOUNDING_CHARTER) | **No** — ratification window is mandatory |
| Issue MIGRATION_EXECUTION_RECEIPT | Yes | Yes (with provisional flag set) |

The rule, plainly:

> **Pre-crisis exit policy is required for binding inheritance. Unchartered migration may move evidence and content, but not executable authority.**

Legacy_provisional migrations are not a degraded chartered migration; they are the appliance honestly admitting that most communities do not have constitutional pre-commitments. The appliance refuses to *fake* a charter. It also refuses to *refuse* the community.

## MIGRATION_PACKET

Container produced by the appliance during a migration event. Carries everything across the boundary.

```
MIGRATION_PACKET
├── identity_and_membership
│   ├── members
│   ├── roles
│   ├── standing_status
│   ├── inactive_accounts
│   └── disputed_membership
├── content_export
│   ├── posts
│   ├── threads
│   ├── media
│   └── deleted_or_unavailable_refs
├── moderation_evidence            # crosses as testimony, never as law
│   ├── actions
│   ├── reasons
│   ├── appeals
│   ├── unresolved_cases
│   └── disputed_receipts
├── migration_charter              # the EXIT_CHARTER for this move
│   ├── quorum_rule
│   ├── ratification_threshold
│   ├── ban_import_policy
│   ├── role_remapping_policy
│   ├── appeal_reopening_policy
│   ├── cooling_off_period
│   └── operator_refusal_policy
└── steward_receipts               # what operator imported/refused/quarantined and why
    ├── what_was_imported
    ├── what_was_rejected
    ├── what_was_quarantined
    └── why
```

Field order matters: `identity_and_membership` is first because the first constitutional crisis of migration is *"who is 'we' when we land?"* — not "what rules carry forward."

## Charter-template ecosystem

Communities adopt charters by reference (like license hashes), not by inheritance from steward defaults.

```
TEMPLATE
├── public_text
├── plain_language_summary
├── provenance
├── version_history
└── threat_notes

ADOPTION_RECEIPT
├── community
├── template_hash
├── amendments
├── eligible_voting_body
├── quorum_result
├── ratification_threshold
└── timestamp

MIGRATION_EXECUTION_RECEIPT
├── founding_charter_referenced
├── exit_charter_generated
├── landing_jurisdiction
├── evidence_imported
├── sanctions_quarantined
├── authority_re_minted
├── refused_items
└── steward_reasoning
```

Separation of powers:

- **The registry publishes templates.** Provenance and version history; no blessing of legitimacy.
- **The community ratifies charters.** Authority lives here, not in the registry.
- **The steward executes receipts.** Procedural, with public refusal trail.

No single layer owns the whole circuit.

## State: advisory_quarantine

Imported sanctions and standing-affecting decisions land in this state on arrival.

```
advisory_quarantine
├── source                          # which jurisdiction issued
├── original_evidence               # testimony, not authority
├── visibility                      # to moderators by default
├── enforcement                     # disabled until ratified
├── expiration_clock                # cooling-off period from EXIT_CHARTER
└── ratification_pathway            # how new jurisdiction can adopt
```

State transitions:
- `advisory_quarantine → ratified` (new jurisdiction explicitly adopts; sanction becomes live, *owned by new body*)
- `advisory_quarantine → expired` (cooling-off elapses without ratification; sanction evaporates)
- `advisory_quarantine → contested` (subject of sanction appeals during cooling-off; queued for new jurisdiction's appeals process)

The cooling-off period is load-bearing. Imported sanctions that are not affirmatively re-minted *must* expire. Default-ratification is the dark pattern this state is designed to prevent.

## Invariants (candidate)

These are the three inviolable rules from the working note, expressed as spec-candidate invariants:

1. **Authority re-minting required.** No imported sanction, role assignment, or governance decision is executable in the new jurisdiction without explicit ratification by the new jurisdiction's eligible body under its EXIT_CHARTER or PROVISIONAL_EXIT_CHARTER.
2. **Pre-crisis exit policy required for binding inheritance.** Authority transfer (binding sanctions, role inheritance, ratified standing on arrival) requires a FOUNDING_CHARTER exit_policy ratified before migration was invoked. Communities without a FOUNDING_CHARTER may migrate under PROVISIONAL_EXIT_CHARTER, which moves evidence and content but cannot transfer executable authority — all inherited governance state defaults to advisory_quarantine, and post-landing ratification within a fixed window is mandatory.
3. **Steward refusal generates receipts.** The operational steward may refuse to import any artifact on operational, legal, or evidentiary grounds; such refusal MUST appear in steward_receipts with reasoning, visible to the community.

Auxiliary invariant:

4. **Evidence ≠ authority.** Imported moderation_evidence is testimony for the new jurisdiction's consideration. It does not bind. Only ratification by the new body binds.

## Failure modes (anti-patterns the design must resist)

| Failure mode | Description |
|---|---|
| **Quorum laundering** | "Active members" defined by old platform's engagement metrics; old system decides who counts in new system |
| **Evidence poisoning** | Old moderators fabricate or exaggerate receipts; new operator treats as presumptively true |
| **Default ratification** | UI makes "import everything" the easy path; governance becomes a dark pattern |
| **Liability laundering** | Operator says "the community voted" while having structured the only viable options |
| **Undead sanctions** | Old bans survive indefinitely because no one has time to reopen them; cooling-off never resolves |
| **Charter capture** | Whoever writes default templates preloads constitutional outcome; *default migration charters are constitutional power disguised as UX* |
| **Steward-as-platform collapse** | Operator's refusal authority expands into legislative authority; "trust and safety" decisions become unappealable; notary becomes landlord |
| **Registry-as-legitimacy-authority** | Charter template registry starts blessing legitimacy instead of attesting provenance; becomes a single point of constitutional capture |

## Relationship to atproto

Atproto is the closest live substrate, but not an implementation. Mapping:

| Appliance concept | Closest atproto element | Gap |
|---|---|---|
| Operational stewardship of identity/data | PDS hosting + DID/handle | Substantially covered |
| Operational stewardship of indexing | Relay | Resource-intensive; co-op-shaped |
| Jurisdictional context (community, not user) | *no native concept* | The missing middle |
| Moderation evidence portability | Labeler outputs partially (per-actor) | Not community-scoped, not packet-shaped |
| Charter ratification | *no native concept* | Out of protocol scope; lives in appliance layer |
| Authority re-minting | *no native concept* | Out of protocol scope; lives in appliance layer |

The appliance is *protocol-agnostic by design.* It can run on atproto, on Mastodon-style ActivityPub, on Matrix, or on a custom substrate. It is the layer that protocols leave to "community admins," productized.

## Open questions

- **Membership basis verification.** What proves a member is a member at migration time? Cryptographic signature on adoption_receipt? Activity threshold? Self-attestation? Different communities need different answers; appliance must support template-level configuration without making the choice for them.
- **Composition with reputation portability.** If a user has standing in multiple communities, do those standings travel together or separately? Per-community by default seems right, but cross-community reputation networks may complicate.
- **Adversarial migration.** A bad-faith operator could invoke migration to reset accountability ("we're a new jurisdiction, old bans don't apply"). The pre-crisis exit_policy partially defends this (you can't change the exit rules after invoking exit), but the FOUNDING_CHARTER amendment_policy is a potential laundering channel. Audit trail required.
- **Steward conflict-of-interest.** What if the operational steward is also a member of the community migrating? Probably requires recusal, but mechanism unspecified.
- **Cross-jurisdiction appeals.** If a member sanctioned in community A migrates to community B (alone, not with the community), do A's sanctions follow them? The packet structure assumes community-scoped migration; individual migration with disputed history is a separate problem.

## Out of scope

- The legal entity that holds operator liability. The appliance assumes such an entity exists (community trust, cooperative, LLC, member-owned utility). Constituting that entity is a legal/institutional problem the appliance cannot solve.
- The technical implementation of receipts. Cryptographic signatures, transparency logs, etc., are implementation details to be specified at promotion time.
- The user-facing UX. The working note describes a Brenda-from-book-club usability target; concrete UX is downstream of the object model.
- Paper-shaped formalization. If/when admissibility-kernel composition pressure produces a theorem-shaped spine, that lives in the paper repo, not here.

---

**Object index (canonical names for cross-reference):**

- `FOUNDING_CHARTER`, `EXIT_CHARTER`, `LANDING_RECEIPT`
- `MIGRATION_PACKET` (with subfields above)
- `TEMPLATE`, `ADOPTION_RECEIPT`, `MIGRATION_EXECUTION_RECEIPT`
- `advisory_quarantine` (state)
- Invariants 1–4

**Cross-references:**

- `../working/regime-change-with-backups.md` — concept memo, prose-shape, full kernel-overlap audit
- `atproto_governance_transfer_proof.md` — governor pattern onto atproto layers
- `atproto_provenance_instrument.md` — sibling spec on the radar/SIGINT side
- `../working/non-reciprocal-admissibility-flow.md` — sibling primitive; charter-capture failure mode is a direct NRAF instance
- `../working/signal-authority-candidate.md` — default-ratification failure mode (null-as-verdict)
- `../working/commitment-standing-decay-candidate.md` — undead-sanctions failure mode
- `../working/admissibility-decay-family-note.md` — superclass for stale-license patterns
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — artifact-kind × use-kind kernel piece (charter binding force)
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — steward-as-notary kernel piece
