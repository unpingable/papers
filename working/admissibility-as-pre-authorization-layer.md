# Admissibility as the pre-authorization layer

**Filed:** 2026-06-04. **Status:** positioning note. Route sign, not doctrine. Names where the corpus's work sits in the existing security-stack taxonomy.

> **Scope banner:** *Route signs, refusal kernels, witness bridge, no cathedral.* — the four-element discipline for the admissibility-layer work. Positioning here, refusal kernels in Lean / doctrine map, substrate bridge via differential testing à la Cedar, and no full-stack unification calculus. If this note or its siblings start growing a cathedral, the discipline failed.

## The taxonomy

Standard security categories: **authn** (who the actor is), **authz** (whether the actor may act), **accounting / audit** (what happened), **attestation** (what evidence exists).

The corpus's work is none of those. It governs whether a claim, witness, credential, revocation, timestamp, standing relation, relationship edge, or resource state is *eligible to become a binding premise at all*. That category has a name:

- **Admissibility** — whether a thing may count as input to the other layers.

## The keeper

> **Authorization reasons from premises. Admissibility governs whether those premises may count.**

Equivalent phrasings:
- *Customs checkpoint before facts immigrate to the policy universe.*
- *The bouncer for facts trying to become power.*
- *Pre-authorization premise control.*

## The falsifier (this is positioning, not natural kind)

This frame is a *choice* about how to slice the security stack. It would be weakened or falsified by an authorization system that handles the laundering moves the [doctrine map](anti-laundering-doctrine-map.md) names — retroactive authorization, stale evidence, self-minted witness, cross-surface revocation, standing laundering, double-spend premise reuse — wholly inside its authz layer, without requiring a separate admissibility step.

Closest existing neighbor: **AWS Cedar Analysis** (Lean + SMT, proves properties over policy semantics across all scenarios). Cedar Analysis operates one level above the authorizer and could in principle encode some of these moves *if enough provenance is reified as entity state*. But doing so converts admissibility questions into authz questions over an enriched entity model — making the admissibility layer instrumentally invisible rather than absent. The boundary holds for now; a future system that genuinely subsumes the admissibility layer (without the reification gambit) would deprecate this positioning.

Worth naming the test in advance so the framing carries its own brake.

## External pitch shape

> **Prior art provides representations for authority transfer. This work formalizes forbidden conversions between representation, evidence, standing, time, surface, and effect.**

Question-shaped restatement (for orientation): existing authorization work mostly asks *when should access/action be allowed?*; this work asks *what kind of premise can become a binding input to that question?* — *mechanized refusal kernels for admissibility failures at the boundary of authorization systems.*

That gives the corpus a stable location in security vocabulary without competing with existing authz machinery (Cedar, ABLP / says / speaks-for credential logics, proof-carrying authorization, capability systems, temporal policy logic). Sibling layer, different question. Full prior-art map and representation menu (six buckets, each with what-it-refuses-and-doesn't): see [`tooltheory/admissibility-related-work-map.md`](tooltheory/admissibility-related-work-map.md).

**Warning on naive implementations.** The obvious "attribute bags with provenance" implementation — `{ "basis": "external", "issuer": "...", "fresh_until": ... }` — is unsafe if provenance is *just typed data*. Anyone can write the label; the label is not the witness. Macaroons / Biscuit / SPKI exist precisely because the typed-data approach is laundering-prone. Minting discipline (verifier-checked attenuation chain, cryptographic binding) is the load-bearing part. See the related-work map's DeepSeek-warning section for full treatment.

## Cedar-relative positioning (added 2026-06-06)

Cedar (and Amazon Verified Permissions) answers: *"May principal P perform action A on resource R, given context C?"* — a policy decision engine over principals / actions / resources / entities / policies / context with allow/deny outputs (default deny, forbid overrides). Honest authorization logic, well-built. The corpus's distinctive object is **one altitude upstream**:

> **Cedar guards the door. This asks whether the door is where everyone says it is, whether the badge still counts, whether the emergency exit became the main entrance, and whether the map was rewritten by the person trying to get in.**

### The upstream questions Cedar mostly assumes away

Each maps onto an obligation atom from the [bridge obligation lattice](bridge-obligation-lattice.md):

| Upstream question | Bridge family / obligation atom |
|---|---|
| Is this context admissible? | general admissibility gate |
| Is this entity graph fresh? | freshness |
| Did this event lawfully change the policy surface? | Deformation / temporal-bounding |
| Did this exception become precedent? | Exception / anti-precedent |
| Did this delegation amplify authority? | Delegation / non-amplification |
| Did this representation faithfully project the source? | Projection / type-fidelity + freshness |
| Did this label become enforcement by witnessed conversion? | Conversion / type-fidelity |

### The relationship in one line

> **Cedar trusts the application to supply the witness facts. The hard problem moves outside Cedar.**

A Cedar policy can externalize the witness check into context — `permit ... when { context.has_coupling_witness && context.horizon > now && context.scope_contains(resource) }`. But Cedar is then trusting the application to supply the witness facts honestly. The unanswered questions: *who witnessed the witness? Is the surface deformation well-typed? Did the transform match the label? Did the admissibility difference stay inside the envelope? Did the exception avoid precedent? Did composition launder the horizon?* Those live outside Cedar's frame.

The corpus is **not** "better Cedar." It is the missing notarization / governance / control layer under systems that use Cedar-like authorization — the admissibility kernels that decide whether the witness facts Cedar trusts are themselves trustworthy. The 2026-06-04 Priority 0 spike already confirmed Tallam (arXiv 2605.05440) and the WEF ACAP playbook publicly ask these upstream questions without answering them; this positioning is the corpus-side answer shape.

## Adjacent methodological theft

Cedar's Lean ↔ Rust differential randomized testing — generate many attempted transitions and witnesses (valid and malformed), classify through both the Lean model and the production substrate implementation, treat divergence as model / schema / implementation error — is the worked template for the BoundaryTransit witness-substrate gap (named in `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean`'s header). Production witnesses are signed JSON, receipt rows, ledger entries, NQ testimony packets, WLP claims, etc. The bridge from Lean witness to production witness is a *tested correspondence*, not a rhetorical equivalence. Citable methodology, not metaphor.

## Cross-references

- [`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md) — the family taxonomy this positioning organizes; each row is an admissibility refusal.
- [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) — federation doctrine consistent with the framing: no single calculus *over* admissibility, only typed refusals.
- [`tooltheory/kerberos-lineage-boundary-transit.md`](tooltheory/kerberos-lineage-boundary-transit.md) — Kerberos as adjacent prior art at the authn layer; admissibility is the separate layer Kerberos doesn't reach.
- [`custodian-binding-accountability-candidate.md`](custodian-binding-accountability-candidate.md) — instance refusal at the observation → accountability seam.
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — fenced encodability proof for the admissibility-layer pattern.

## What this note is NOT

- Not a formal definition of admissibility-as-a-class. The category is a positioning frame; the formal artifacts (refusal kernels, doctrine map, BoundaryTransit) are the specific things being positioned.
- Not a competitor to Cedar / ABLP / PCA. Sibling layer, different question.
- Not a paper or paper claim. Internal positioning note; useful for any future external pitch.
- Not a discovered taxonomic fact. A choice about how to slice the stack, with a stated falsifier.
