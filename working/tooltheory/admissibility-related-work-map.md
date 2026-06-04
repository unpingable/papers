# Admissibility — related-work / representation-menu map

**Filed:** 2026-06-04 in `tooltheory/`. **Status:** prior-art map + representation menu. Not doctrine. Route signs for future "isn't this just X" review challenges.

## Why this exists

The corpus's work sits adjacent to a dense literature, much of it twenty-plus years old. Each middle rung between "Cedar policy decision" and "refusal kernel for forbidden conversions" already has a name, a representation, and a paper trail. This map names the rungs so that:

1. Future-you doesn't get blindsided in review by Aura / SecPAL / macaroons / Biscuit / linear credentials as "ah, beans" prior art.
2. The corpus's distinctive object (refusal kernels) is positioned by negation against the positive machinery the rungs supply.
3. The middle rungs become a **representation menu** — you don't have to invent how to represent attenuation, delegation, freshness, or consumability; the literature has worked answers worth stealing.

## The keeper

> **Use prior-art tokens / logics for representation. Use refusal kernels for forbidden conversions.**

The middle rungs mostly formalize *how authority may travel*: delegate, attenuate, prove, consume, relate. The refusal kernels formalize *where apparent authority-conversions must fail* regardless of what the positive machinery says is well-formed.

## The map

> **Status caveat (load-bearing — read this before the table).** The "What it does NOT refuse" column is **conjectured pending reading**. Each cell in that column is an absence claim about a literature the relay summarized but did not directly witness. By the corpus's own four-receipt discipline, an absence claim composed from relay-summary is a *claim-receipt formatted as an observation-receipt* — signed but not witnessed. The table is route-signs pointing at neighborhoods; the read-queue below ratifies each cell. If a future reading discovers that, e.g., SecPAL's negation handling or some corner of the says-logic tradition *does* treat failure-to-confer-standing, the corresponding cell loses its position and the map gets corrected, not defended.
>
> The "What it represents" and "Nearest kernel neighbor" columns are claim-shape and survive secondhand transmission. The third column is the one that needs witnessing.
>
> Two keepers from the audit that caught this:
>
> > **Absence claims require witnessing.**
> >
> > **The map is route signage, not territory.**
>
> Per-row confidence status uses these levels:
> - `[unread]` — named neighbor, no direct reading yet
> - `[skimmed]` — partial reading, conjectures unrevised
> - `[witnessed]` — read with summary added; conjectured cell updated to observed claim
> - `[ratified]` — distinction with refusal kernels confirmed against the literature
> - `[collision]` — the literature already covers what we thought was distinctive; reposition or retire
>
> Current status for every bucket below: `[unread]`. The map's conjectured column will turn into observed claims only as items get checked off in the read queue.

| Bucket | What it represents | What it does NOT refuse (**CONJECTURED**) | Nearest kernel neighbor |
|---|---|---|---|
| **Cedar / Cedar Analysis** | Policy semantics; SMT-backed analysis over modeled universe. | *Conjectured:* whether the facts that became modeled entities were laundered into the universe in the first place. | All — Cedar is the outer reference point and toolchain precedent. |
| **SPKI / SDSI, macaroons, Biscuit** | Capability/certificate/token attenuation; minting and provenance representation; offline attenuation; decentralized verification. | *Conjectured:* self-mint at the substrate boundary; replay across surfaces without explicit caveats; standing-laundering through chained delegation. | BoundaryTransit witness substrate; custodian-binding candidate. |
| **ABLP / says / speaks-for / SecPAL / DKAL / NAL** | Testimony, delegation, "A says φ" credential logics; positive entailment from logical assertions; distributed knowledge. | *Conjectured:* when testimony fails to confer standing; what assertions cannot bind regardless of who made them; post-hoc retroactive claims. | Standing kernel (currently named-not-coded in BoundaryTransit). |
| **Proof-carrying authentication (Appel/Felten 1999) / proof-carrying authorization (Bauer et al., later) / Aura** | Request-time proof objects; dependently-typed authorization with proof emission for audit. Aura is uncomfortably close to "receipts": dependent types + authorization logic + audit-proof generation. | *Conjectured:* what proofs cannot be valid — the negative space of what no proof should be allowed to discharge. PCA builds the gift shop; refusal kernels are the contrapositive. | Refusal kernels generally; closest neighbor by methodology. **The most dangerous unread literature.** |
| **Linear / consumable credentials** (Bauer et al., PCFS) | Credentials/authority that can be spent, not copied; use-once tokens with explicit consumption discipline; logic-based access control with linearity. | *Conjectured:* shared-budget-reused-as-multiple-premises through narrative duplication of consumed tokens. | Spendability / multiplicity gap (ContractionHinge sibling, currently informal). |
| **Zanzibar / ReBAC** | Relationship edges as authorization substrate; per-edge attribute storage; consistent global authorization. | *Conjectured:* provenance laundering on relationship edges; whether the edge-minting itself was admissible. | Provenance-typed edges as a candidate intermediate artifact. |

## Read queue (the actual prevention)

The map exists to prevent "ah, beans" review surprises — but the *actual* prevention is the week of reading, not the map. The map without a queue can eat the meal: filing a satisfying cross-referenced object that scratches the itch the reading was supposed to scratch. So:

**Priority 1 (most dangerous unread):**

1. **Aura** (Jia et al., ICFP 2008) — *AURA: A Programming Language for Authorization and Audit*. Dependent types + authorization logic + proof emission for audit. Closest methodological neighbor; if anyone built receipts-as-types already, it's here. **Read first.**
2. **Proof-Carrying Authentication** (Appel & Felten, CCS 1999) — the original PCA paper, higher-order logic for distributed authentication. Then trace forward to:
3. **Proof-carrying authorization** (Bauer et al., later CMU work) — the named-similarly successor that uses proof objects at the gate.

**Priority 2 (load-bearing for substrate candidates):**

4. **Macaroons** (Google, NDSS 2014) — chained-HMAC credentials with caveats. Concrete substrate candidate for BoundaryTransit witness production form.
5. **Biscuit** — Datalog-based authorization token with offline attenuation. Likely modern alternative to macaroons; check current state.
6. **SPKI/SDSI** (RFC 2693 / RFC 2692) — older capability/certificate theory; mostly for lineage.

**Priority 3 (testimony/delegation neighborhood):**

7. **ABLP** (Abadi, Burrows, Lampson, Plotkin, 1993) — the founding *says* / *speaks-for* paper. Need to know what it does refuse vs. enable.
8. **SecPAL** (Becker, Fournet, Gordon, MSR) — declarative authorization with delegation; check negation handling specifically.
9. **DKAL** / **NAL** — successors; lower priority unless SecPAL turns up gaps the successors filled.

**Priority 4 (consumption / relationship rungs):**

10. **Consumable credentials in logic-based access control** (Bauer, Garriss, Reiter at MPI-SWS / CMU; PCFS) — the linearity neighborhood for spendability.
11. **Zanzibar** (Pang et al., USENIX ATC 2019) — Google's global authz; mostly for the ReBAC representation choice, not because the paper is novel theory.

**Process discipline for the reading:**

- For each item, the output is a one-paragraph note added to this file specifying: *what it actually refuses* (replacing the conjectured cell), *what it doesn't*, and *where the refusal kernels do or don't have new ground left*.
- If a reading reveals that a refusal kernel's negative-space territory is already covered by existing positive machinery, that kernel deserves either retirement, repositioning, or a sharpened version of the distinction.
- Do NOT use the existence of this queue as evidence the reading is done. Mark each item explicitly: `[ ]` unread / `[~]` skimmed / `[x]` read with summary added.

Current state: **`[ ]` all eleven items.** The map's conjectured column will turn into observed claims only as items get checked off.

## The distinctive object (negative space)

Each middle-rung formalism is **positive**: it specifies how to grant, delegate, attenuate, prove, consume, or relate correctly. The corpus's refusal kernels operate in the **negative space**: they prove certain conversions cannot be valid *regardless of what the positive machinery permits*.

> **Refusal kernels are the contrapositive discipline to proof-carrying authorization: they mechanize the conversions that no proof, credential, token, testimony, or policy context is allowed to launder into binding authority.**

That's a one-sentence positioning a PL/security reviewer parses instantly. ABLP and Aura built the gift shop; the corpus is building the museum of forbidden moves.

## Substrate guidance (the actionable part)

When the witness-substrate question comes up for any kernel earning promotion from category-2 (fenced scratch) to category-1 (wired/annex):

- **For witness substrate**: macaroons / Biscuit / SPKI are the live candidates — *not* "signed JSON" handwaved generically. The attenuation history IS the minting receipt; the verifier-side check is what makes the substrate non-launderable. The substrate gap named in BoundaryTransit's header has a worked answer here.
- **For testimony / delegation**: SecPAL / DKAL / NAL are the canonical neighbors. "A says φ" semantics with explicit speaks-for relations is the existing vocabulary.
- **For consumption**: linear-credentials / PCFS prior art. Don't reinvent linearity; the consumption discipline already exists in usable form.
- **For relationships**: Zanzibar / ReBAC + provenance-typed edges as a candidate intermediate artifact (DeepSeek named this; it's tractable).

## The DeepSeek typed-provenance warning

DeepSeek's "attribute bags with provenance" suggestion is implementable but **unsafe if provenance is just typed data**. Anyone can write:

```json
{ "basis": "external" }
```

The clown has a keyboard. The minting discipline is the load-bearing part — verify the credential, not the label. Macaroons / Biscuit / SPKI exist precisely because the typed-data approach is laundering-prone: the attenuation chain and the cryptographic verifier are what convert a typed claim into a non-launderable witness. Typed-provenance-without-minting-discipline reintroduces exactly the failure mode the refusal kernels exist to refuse.

If you ever see an implementation that has a `"basis": "external"` field with no verifier hook, that's the smell. The label is not the witness.

## Non-promotion guard

This map is positioning + representation menu. It is NOT:

- A new security-stack taxonomy. The admissibility positioning is a route sign; this map is its prior-art context.
- A doctrine file. Refusal kernels are the doctrine; this map is the neighborhood.
- A commitment to build any of the represented substrates. Whichever consumer pulls a kernel into use picks its substrate from this menu.
- A "full admissibility calculus" cathedral. Cathedral is the cope direction; representation menu + refusal kernels + tested correspondence is the cathedral-avoiding shape.

## Cross-references

- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) — positioning note that this map provides prior-art context for.
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) — family rows that the middle-rung machinery is positive-counterpart to.
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — federation doctrine consistent with the "borrow representations, refuse conversions" stance.
- [`kerberos-lineage-boundary-transit.md`](kerberos-lineage-boundary-transit.md) — sibling tooltheory note; Kerberos is in the authn neighborhood; this map covers the authz/admissibility neighborhood.
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — scratch encoding whose witness-substrate gap macaroons/Biscuit are live candidates for.

## Provenance

Surfaced 2026-06-04 from a multi-model relay (ChatGPT + Claude-web + DeepSeek) digging into prior art adjacent to BoundaryTransit and Cedar. Claude-web flagged that "Cedar gives toolchain legitimacy but not object legitimacy" — and that the middle rungs (Aura, SecPAL, macaroons, etc.) constitute the actually-dangerous-in-review prior art. This map is the route-sign list that prevents future-session "ah, beans" surprises. The afternoon of reading just became a week — but better identified now than in review.
