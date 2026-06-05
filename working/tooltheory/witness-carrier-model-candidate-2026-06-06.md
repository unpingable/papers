# Witness Carrier Model — candidate (Fork B, BoundaryTransit substrate)

**Filed:** 2026-06-06 (Fri noon). **Status:** pre-ratified / candidate / non-canonical. **Not** a schema. **Not** production. **Not** Lean. **Not** a correspondence proof.

**Custody:** markdown-only candidate doctrine note. Lives above the field menu in [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § Substrate guidance § Candidate carrier sketch. Promotion path: none earned; if a downstream consumer (NQ receipt substrate, an external pitch needing a concrete artifact, Cedar-style differential harness — Level 4) ever needs the bridge, this file is the doctrinal home of the binding-obligation layer.

## 1. Purpose

Candidate **relational model** for a BoundaryTransit production-witness carrier. The field menu (11 fields) lists *what a carrier might carry*. This file names *which fields must be bound together, by whom, and which laundering move fails when the binding is absent*. That is the Fork B slice.

**The central question this model answers:**

> Which fields must be bound together, by whom, and which laundering move fails when they are not?

Not *"what packet fields might exist"* (already done). Not *"what wire format"* (substrate-specific; out of scope).

## 2. Non-claim

> *This sketch defines candidate production-witness carrier requirements; it does not establish correspondence between carrier validity and the Lean witness model.*

The Lean witness in `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` is a dependent proof object. Production carriers are signed JSON, receipt rows, ledger entries, NQ testimony packets — *not* Lean proofs. The bridge is a tested correspondence, not a rhetorical equivalence, and the harness for testing that correspondence remains unbuilt (Level 4; do not promote).

## 3. Binding obligations (not fields)

**The phrase is *signature / authority coverage over relations*, not *"packet fields."*** A field labeled `surface: prod` is decorative until the authenticity mechanism binds it to the issuer, attempt, subject, and caveats.

Worked example:

```text
attempt_id + surface + subject + valid_window + caveats
must be covered by the issuer's authenticity mechanism.
```

The mechanism may be a macaroon caveat chain, a Biscuit block/signature structure, an SPKI-style certificate chain, or any other non-launderable substrate. The model names the obligation; the substrate names the wire format. *Different substrates bind different subsets the same way; the model says which subsets must be bound regardless.*

The 11 carrier-menu fields divide into:

- **Identity-binding:** `attempt_id`, `surface`, `subject`, `issuer`. The four-tuple a verifier needs to refuse cross-attempt or cross-surface reuse.
- **Time-binding:** `issued_at`, `observed_at`, `valid_window`. The triple that catches stale and post-hoc laundering.
- **Authority-binding:** `standing_basis`, `caveats`. What the issuer claimed standing-wise; how that standing was attenuated.
- **Substrate-binding:** `signature / chain / digest`, `evidence_ref`. The cryptographic spine + the link to underlying evidence.

Identity + time + authority must be **jointly covered** by substrate. None of the three can be detached, restated, or replayed independently. That joint coverage *is* the binding obligation.

## 4. Minting predicate shape

```text
MayMint(issuer, subject, surface, attempt, now, standing_basis)
```

**Abstract shape only.** This file does NOT define policy — what counts as adequate standing for a given subject/surface/attempt is the consumer's problem, deliberately not the corpus's. The model names the predicate the issuer must satisfy *independently of the subject's own assertion* (which is the canonical self-mint failure).

Two consequences of the shape alone, even without policy:

- **The subject cannot be the only standing source.** If `standing_basis` is satisfied only by the subject's own claim, `MayMint` reduces to *"the subject says it's OK"* — self-mint.
- **`now` is the issuer's clock at minting, not the subject's claimed timestamp.** This prevents the post-hoc laundering case where a subject-supplied `issued_at` predates the actual transition.

Policy is downstream; predicate-shape is here.

## 5. Verifier check order

Order matters; it forces reality contact and lets the verifier short-circuit cheaply on the most-likely-to-fail check first.

1. **Authenticity / chain coverage.** Does the signature/chain/digest actually bind the identity-time-authority bundle? *If not, every later check is operating on advisory metadata.*
2. **Validity window.** Is `now ∈ valid_window`? Cheap; catches stale.
3. **Attempt binding.** Does `attempt_id` match the live attempt under verification? Catches wrong-attempt reuse.
4. **Surface binding.** Does `surface` match the live surface under verification? Catches wrong-surface reuse.
5. **Attenuation / non-amplification.** If the carrier is derived from a parent, do `caveats` only narrow (never widen) the parent's authority? Catches widened-after-issue.
6. **Evidence ref / standing basis.** Does `evidence_ref` resolve to extant evidence, and does that evidence support the claimed `standing_basis` under `MayMint`? Catches self-mint and absent-evidence cases.
7. **Replay / spendability** (if the substrate is consumable). Has this carrier already been spent for this attempt? Last because it's the most consumer-state-dependent.

Steps 1–4 are pure verification of the carrier itself. Steps 5–7 reach beyond the carrier into the parent chain, evidence layer, and consumer state.

## 6. Refusal invariant table — the payoff

| Refusal | Required invariant | Fields / relations involved | Substrate neighbor |
|---|---|---|---|
| **self-minted** | issuer must satisfy `MayMint` *independent of* subject assertion (subject cannot be sole standing source) | issuer, subject, standing_basis, evidence_ref | SPKI cert chains; Biscuit issuer signatures; macaroons' root key |
| **replayed** | carrier bound to attempt and/or nonce; spendability check against consumer state | attempt_id, issued_at, digest, consumer's spent-set | capability-token spendability; macaroons' third-party caveats |
| **wrong surface** | `surface` is signed/bound by the authenticity mechanism, not advisory metadata | surface, caveats, signature coverage | Biscuit block-level surface caveats; SPKI authorization constraints |
| **stale** | `now ∈ valid_window` checked against verifier clock (not subject-supplied time) | valid_window (from / until), observed_at, now | macaroon time caveats; X.509 NotBefore/NotAfter |
| **widened-after-issue** | child carrier's `caveats` can only narrow parent's authority; surface, scope, action set monotonically restrict | parent.caveats, child.caveats, attenuation chain | macaroons (append-only caveats); Biscuit (block sealing) |
| **post-hoc laundering** | `issued_at` cannot follow a transition that itself required prior authority; *the witness post-dates what it claims to have authorized* | issued_at, attempt_time, transition history, BoundaryTransit's anti-retroactivity | BoundaryTransit's `antiRetroactive` invariance field |
| **wrong attempt** | carrier binds to *this* attempt, not a same-shaped future or sibling attempt; `attempt_id` is unique per attempt and signed-covered | attempt_id, subject, surface, signature coverage | token-binding (RFC 8471); per-request nonces |

The table is the model. Every row pairs:

- a refusal (one of the 7 carrier-menu refusal cases),
- the invariant that catches it,
- the fields / relations the invariant constrains,
- the substrate neighbor that already implements this kind of binding.

A reader of this table can say *which laundering moves the candidate carrier is meant to make impossible, and which binding obligation catches each one*, without mistaking the sketch for a schema or a proof.

## 7. Guardrails (carry-forward)

These restate the substrate-guidance section's existing guardrails as they apply to the model layer:

- **Field menu is not schema.** This file does not specify a wire format. The same is true of the binding obligations; they describe relational coverage requirements, not byte layouts.
- **Label is not witness.** A field named `surface: prod` is testimony until the authenticity mechanism binds it. The binding obligation is the witness; the field name is the label.
- **Minting discipline is the load-bearing part.** `MayMint`'s predicate shape is the spine. Without it, the carrier is RFC-cosplay with no minting discipline (DeepSeek's typed-provenance warning).
- **Prior-art neighbors remain partly unread.** Aura (Jia et al., ICFP 2008) and proof-carrying authorization (Bauer et al.) remain in the Priority 1 read queue. The neighbor column above names the *closest known* substrate; a future reading may sharpen the neighbor or surface a closer one.
- **Differential harness is future Level 4.** Cedar's Lean ↔ Rust differential randomized testing is the methodological template; the harness is not built. Do not promote.

## Cross-references

- [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § Substrate guidance § Candidate carrier sketch — the menu layer (11 fields + 7 refusal cases + 5 guardrails) this model sits above.
- [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) — the obligation atoms this model instantiates: identity-binding owes type-fidelity; time-binding owes freshness + temporal-bounding; authority-binding owes non-amplification.
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — the Lean witness this model is the substrate-side companion to. The Lean file's "Witness substrate gap" section is what this model addresses.
- [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § Priority 0 readings — ACAP "agent passport" (WEF May 2026) and Tallam R2 (arXiv 2605.05440) are the publicly-articulated forcing-case instances for this model.
- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) § Cedar-relative positioning — *"Cedar trusts the application to supply the witness facts. The hard problem moves outside Cedar."* This model is what supplying-witness-facts-honestly looks like.
- [[documentation-keepers]] — keeper phrases applicable: *"the label is not the witness"*; *"indexed or it didn't happen"*; *"existential laundry"*; *"a fog machine is a bridge with the empty obligation set"*.

## Provenance

Filed 2026-06-06 (Fri noon) as Fork B of the BoundaryTransit substrate trail. Predecessor: the 2026-06-05 substrate-guidance section in the related-work map (menu layer; field list + refusal cases + 5 guardrails). Successor: none planned; Fork C (external-facing note using the 2026 agent-authz convergence as the forcing-case intro) and the Cedar-style differential harness (Level 4) remain explicitly out of scope.

Scoping refined by operator after Claude Code's initial draft: *"the central object is not 'fields'; it's binding obligations. The phrase is signature/authority coverage over relations, not packet fields."* The refusal invariant table is the payoff; everything else is scaffolding to make that table land.

## Definition of done

> *A reader can say which laundering moves the candidate carrier is meant to make impossible, and which binding obligation catches each one, without mistaking the sketch for a schema or a proof.*

Met if the refusal invariant table (§ 6) reads cleanly without the surrounding doctrine. Test: read § 6 alone; can you state the seven refusals and their invariants? If yes, done.
