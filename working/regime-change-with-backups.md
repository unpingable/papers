# Regime Change with Backups: Jurisdictional Portability and the Civic Migration Appliance

**Status:** Working concept / not a specification. Filed 2026-05-15. Surfaced via multi-model conversation (Gemini → chatty → DeepSeek → user) about platform exit, federation, and atproto's missing middle layer.

**Spec promotion gate:** Promote object model to `specifications/civic_migration_appliance.md` (stub already filed alongside this note) when an implementation, protocol sketch, or receipt format needs stable terms. Do not promote prose; promote the object model.

---

## The hook

> **Platform exit is regime change with backups.**

Data portability moves files. Jurisdictional portability moves communities without laundering old authority.

## The problem

Platforms succeeded by unbundling the *experience* of infrastructure from the *liability* of running it. "We'll own the pipes. You bring the culture." Then: also the culture is our asset, the rules are opaque, the export button is decorative, and the landlord has opinions.

The federation/self-hosting counterproposal usually fails because it answers the wrong question. It says "you can own the infrastructure." Normal people hear: **"You can become the infrastructure."** That is a second job with worse documentation.

> Everybody wants the affordances of infrastructure with the liability profile of vibes.

Atproto has the right shape as a substrate: PDS for identity/data hosting, Relay for indexing, AppView for product experience. DID-based identity. Account migration as a stated portability goal. But moderation and community health land precisely in Relays and AppViews — the expensive, resource-intensive, legally exposed layers where social gravity pools.

You can own the mailbox. The sorting office still has leverage.

## The thesis

The missing middle is not better managed Mastodon, not better PDS hosting, not a new protocol. It is:

> **A civic migration appliance for online communities.**

The appliance is *boring by design.* It exists to move communities — not just data — between governance environments without laundering authority. It is not the community. It is not the sovereign. It is a notary, not a legislator.

Two slogans worth keeping:

> **Evidence crosses. Authority does not.**

> **The steward is a notary, not a legislator.**

## Two stewardship layers

The product boundary that makes "bounded stewardship" more than managed hosting:

1. **Operational stewardship** — hosting, backups, security, migration plumbing, abuse-response infrastructure. The pipes.
2. **Jurisdictional stewardship** — membership basis, standing, moderation inheritance, appeals, ratification thresholds, charter execution. The civics.

Most current candidates address layer 1. Layer 2 is where the labor and the liability and the political reality actually live. Naming it as a separate layer is most of the work.

## Three constitutional moments

Migration is not a cut-over event. It is a process with a before, a liminal moment, and an after. Three distinct artifacts:

```
FOUNDING_CHARTER   — pre-committed at community formation
EXIT_CHARTER       — generated when migration is invoked
LANDING_RECEIPT    — produced when new jurisdiction ratifies
```

The founding charter must include exit policy. Crisis-time governance is garbage. Consent under duress isn't consent. The platform's anesthetic works partly because it puts you in the burning house, then offers a blue button labeled "Start Fresh (Lose Everything)." The alternative: *"You already wrote down how you'd leave. Here's that plan. Do you want to execute it, or amend it first?"*

**Legacy fallback:** most communities pre-date the appliance and have no FOUNDING_CHARTER. They get a `PROVISIONAL_EXIT_CHARTER` path: evidence and content move, but no binding authority transfers; all inherited governance state lands in advisory_quarantine, with mandatory post-landing ratification. The appliance refuses to fake a charter, and also refuses to refuse the community. See `specifications/civic_migration_appliance.md` for the chartered-vs-legacy_provisional distinction.

## The migration packet

```
community_migration_packet
├── identity_and_membership      # WHO is migrating — first admissibility gate
│   ├── members
│   ├── roles
│   ├── standing_status
│   ├── inactive_accounts
│   └── disputed_membership
├── content_export                # the files (table stakes)
│   ├── posts
│   ├── threads
│   ├── media
│   └── deleted_or_unavailable_refs
├── moderation_evidence           # crosses as testimony, not as law
│   ├── actions
│   ├── reasons
│   ├── appeals
│   ├── unresolved_cases
│   └── disputed_receipts
├── migration_charter             # the exit charter for this move
│   ├── quorum_rule
│   ├── ratification_threshold
│   ├── ban_import_policy
│   ├── role_remapping_policy
│   ├── appeal_reopening_policy
│   ├── cooling_off_period
│   └── operator_refusal_policy
└── steward_receipts              # what the operator did/refused, with reasons
    ├── what_was_imported
    ├── what_was_rejected
    ├── what_was_quarantined
    └── why
```

Identity comes first because the first constitutional crisis is "who is 'we' when we land?" If the old platform's membership logic silently defines the voting body, you've inherited the old regime's political geography before casting a single vote. Quorum laundering by default.

## The advisory quarantine

Imported sanctions land in a non-executable state:

```
advisory_quarantine — visible to moderators, nonbinding by default, expires unless ratified
```

This resolves the temporal tension between continuity and sovereignty. The new jurisdiction isn't operating blind (you don't accidentally re-invite a documented harasser into a fresh start). But the sanctions are not self-executing law. If no one re-ratifies, they evaporate. If the new moderation team wants to keep a ban, they must own it — which moves liability to the body that has the standing to carry it.

## Failure modes

1. **Quorum laundering** — "active members" defined by old platform engagement metrics, so the old system decides who counts in the new system.
2. **Evidence poisoning** — old mods fabricate or exaggerate receipts; new operator treats them as presumptively true.
3. **Default ratification** — UI makes "import everything" the easy path. Governance becomes a dark pattern.
4. **Liability laundering** — operator says "the community voted" while having structured the only viable options.
5. **Undead sanctions** — old bans survive indefinitely because nobody has time to reopen them.
6. **Charter capture** — whoever writes the default templates preloads the constitutional outcome. *Default migration charters are constitutional power disguised as UX.*

## Doctrine (three inviolable rules)

1. **Evidence crosses; authority does not.** No binding authority transfers across jurisdictional boundaries without re-minting in the new body.
2. **Pre-crisis exit policy is required for binding inheritance.** Unchartered migration may move evidence and content, but not executable authority. A community without a pre-committed exit policy can still migrate — but only under a provisional path that quarantines all inherited governance state and requires post-landing ratification. The appliance does not fake a charter; it does not refuse the community either.
3. **The steward designs the workflow but does not own the constitutional defaults.** Templates are public, forkable, ratifiable by users; the steward's refusal to execute generates a public receipt, not a shadow decision.

Auxiliary keepers:

> Some friction is the texture of consent.

> Regime change with backups, notarized receipts, and no secret king.

## Kernel-overlap audit

The civic migration appliance is, structurally, an applied taxonomy for substantial pieces of the admissibility kernel:

- **`FiatAdmissibility`** (artifact-kind × use-kind) — charters as artifacts whose kind does not license demanded use ("constitutional binding force") without re-minting in the new jurisdiction.
- **`SurfaceAuthorization`** — the steward surface is authorized for procedural execution, not for legislative content. "Notary, not legislator" *is* the SurfaceAuthorization cut applied here.
- **`Signal Authority`** (working/signal-authority-candidate.md) — the "default ratification" failure mode is exactly null-as-verdict: inaction treated as consent, silence laundered into a binding vote.
- **`Commitment Standing Decay`** (working/commitment-standing-decay-candidate.md) — undead sanctions are textbook decay: rhetorical continuity ("you are banned") with operational revocation ("the body that issued the ban no longer has jurisdiction over you").
- **`non-reciprocal admissibility flow`** (working/non-reciprocal-admissibility-flow.md, filed earlier today) — charter capture failure mode is a direct instance: a template provider shapes the future jurisdiction of every community using its defaults; community has no reciprocal standing in the template-provider's admissibility channel; presented as neutral UX configuration; full state consequence. Not a sixth-domain spontaneous instance (same session as the NRAF filing), but a strong cross-reference for the generativity claim.
- **`Local-Global Validity Gap`** (working/local-global-validity-gap.md) — composition-axis sibling: individually-valid migration steps (export, ratify, import) can compose into globally-invalid authority laundering if any layer treats imported authority as self-executing.

The appliance is not a new primitive. It is an applied scenario where five+ existing admissibility primitives compose. This composition pressure is itself a useful audit on the kernel: where the appliance forces a primitive into uncomfortable shapes is where the primitive needs sharpening.

## Closest live substrates

- **Atproto as substrate** (not Bluesky as platform) — PDS gives identity/data sovereignty; Relay/AppView are where the missing middle is. Closest architectural fit.
- **Mastodon / managed Mastodon** — real communities, real admins, weak portability ("you may flee the village, your house stays"). Live practice of layer 2 stewardship at small scale.
- **Micro.blog / IndieWeb custom-domain publishing** — boring durable ownership pattern, but solves personal publishing better than social-network governance. Cabin, not town square.

The appliance does not replace any of these. It is the *missing middle layer* between substrate (atproto) and community (Mastodon-style), where jurisdictional portability gets done.

## Spec candidate surface

The following are stable enough to lock as candidate object names. Promoted to spec stub at `specifications/civic_migration_appliance.md`:

- `FOUNDING_CHARTER`, `EXIT_CHARTER`, `LANDING_RECEIPT`
- `MIGRATION_PACKET` (with sub-objects above)
- `ADOPTION_RECEIPT`, `MIGRATION_EXECUTION_RECEIPT`
- `advisory_quarantine` as state

Invariants for spec lock:

- Evidence crosses; authority does not.
- No imported sanction is executable on arrival.
- Exit policy must exist before crisis.
- Steward is notary, not legislator.

## Brenda from book club (the usability test)

The appliance succeeds when Brenda can:

1. Join a community with a custom domain, never see a terminal.
2. At formation, encounter *one* moment of deliberate friction: "If we ever leave, how do we want to inherit ourselves? Here are two plain-language options."
3. Forget about it for years.
4. At migration: see a brief summary, a cooling-off calendar, and a button that says "Ratify my membership in the new space."
5. Wake up in a new room that still feels like her book club.

She never holds the scalpel. She does point to the part that hurts, consent to a plan she half-understands but fundamentally trusts, and the steward handles the rest *without becoming her landlord.*

> The texture of sovereignty, remembered.

## Posture (what NOT to do)

- **Do not turn this into a Substack essay yet.** The hooks are good ("regime change with backups," "evidence crosses authority does not," "no secret king"). But the essay-shape lives in the essay archive when written, not here.
- **Do not turn this into a paper yet.** The paper version needs a narrower theorem-shaped spine. The composition-with-admissibility-kernel angle might earn one if developed; not today.
- **Do not implement.** The spec stub names candidate objects; that is sufficient name-early discipline. Implementation requires either an operator who wants to build it or a community that wants to commission it.
- **Do not let the joke version eat the serious version.** "Regime change with backups" is compression. The serious version is the object model and the three inviolable rules.

---

**Cross-references:**

- `specifications/civic_migration_appliance.md` — spec stub (object model, candidate-status)
- `working/non-reciprocal-admissibility-flow.md` — sibling primitive filed same day; charter-capture failure mode is a direct NRAF instance
- `working/signal-authority-candidate.md` — null-as-verdict / default ratification failure mode
- `working/commitment-standing-decay-candidate.md` — undead sanctions / rhetorical-continuity operational-revocation
- `working/local-global-validity-gap.md` — composition axis
- `working/admissibility-decay-family-note.md` — superclass for the stale-license patterns
- `specifications/atproto_governance_transfer_proof.md` — governor pattern transfer to atproto layers
- `specifications/atproto_provenance_instrument.md` — sibling spec on the SIGINT/radar side
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — artifact-kind × use-kind kernel piece
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — closest existing kernel piece on steward-as-notary
