# Kerberos lineage for the BoundaryTransit pattern

**Filed:** 2026-06-04 in `tooltheory/` (sideways kitchen — operational fossil-record read, not doctrine, not Lean).

**Provenance:** distilled from a multi-day relay (DeepSeek + ChatGPT + operator) chewing on whether BoundaryTransit's shape has a deployed precedent. Operator has direct historical experience with Kerberos and current experience with adjacent (private, unnameable) systems sharing the shape; the lineage is grounded, not analogy fishing.

## The pithy line

> **Kerberos is a ticket mint for identity. BoundaryTransit is a refusal-preserving ticket mint for authority crossings.**

Kerberos answers: *"did the KDC mint a valid ticket for this principal/service/time?"*
BoundaryTransit asks: *"is this attempted crossing allowed to promote claim/evidence/status X into authority-bearing status Y across this surface, at this time, under these kernels?"*

Same family. Nastier question.

## What Kerberos proves operationally

Kerberos has been securing enterprise logins for 30+ years. The architectural fact it establishes:

> **Services should not accept self-attested identity. They should accept a ticket minted by a trusted third party.**

That's the deployable proof that ticket-mediated authority is workable at scale. The industry already lives with indirection when direct self-claim is too dangerous. The shape is not exotic.

## Comparison

| Kerberos                                         | BoundaryTransit (the shape)                                       |
| ------------------------------------------------ | ------------------------------------------------------------------ |
| trusted KDC mints tickets                        | checker mints witnesses / refusal receipts                         |
| ticket proves authenticated access basis         | witness proves crossing-admissibility basis                        |
| service validates ticket                         | consumer validates receipt / witness                               |
| errors are mostly protocol / auth failures       | refusals preserve typed failure reasons                            |
| composition is intended via TGT / service tickets | composition is refused unless separately witnessed                |
| trust centralizes in KDC / realm                 | trust decomposes into kernels / surfaces / basis / freshness / standing |

The weird part of BoundaryTransit is not the ticket. The weird part is making **failure** first-class, typed, and accumulating rather than short-circuiting.

## Fossil-record mappings — Kerberos features as doctrine-map rows

Each Kerberos feature is also a known operational failure mode if uncontrolled. The doctrine map's family rows turn out to be exactly the surfaces Kerberos had to engineer defenses around:

| Kerberos feature       | Bad inference if uncontrolled                                  | Doctrine-map row                          |
| ---------------------- | -------------------------------------------------------------- | ----------------------------------------- |
| Cross-realm trust      | admissibility on realm B → admissibility on realm A's services | Surface boundary                          |
| Delegation             | service holds user's ticket → service has user's standing      | Custodian binding / standing propagation  |
| Forwardable tickets    | ticket valid here → ticket valid on next hop indefinitely      | Replay / spendability                     |
| Renewable tickets      | ticket was issued → ticket is current                          | Freshness / expiry                        |
| Constrained delegation | delegation valid → delegation valid for all services           | Scope (adjacent to surface boundary)      |
| KDC compromise         | trusted issuer remains trusted                                 | Witness-issuer capture (meta-failure)     |

The last row is the meta-failure mode of any centralized-witness system: witness validity depends on issuer integrity; a captured issuer launders into every receipt it ever signed. BoundaryTransit's decomposition into per-kernel proofs is a structural response — no single issuer holds the whole admission decision.

## Witness substrate is not the load-bearing piece

Lean was the adversarial reviewer that forced the shape. The production substrate can be anything:

- signed JSON receipt
- database row with foreign-key integrity
- ledger entry (on-chain or off-chain)
- NQ testimony packet
- Wicket verdict
- AG receipt
- HSM-signed attestation

What Lean enforced — and what carries to any substrate — is the API pattern:

```text
caller provides claims and evidence
checker returns witness OR typed refusal receipt
witness cannot be caller-supplied
failures accumulate; no first-failure short-circuit
```

That's the deployable contract. The proof-shaped toy discovered which idioms are inadmissible (see `anti-laundering-doctrine-map.md` § "Meta-pattern: control-flow laundering" and § "Operational translations").

## Smart-contract precision (a correction worth keeping)

A common bad framing: `require(msg.sender == owner)` is "self-attestation."

It is not. `msg.sender` is execution-context data, not the caller's say-so. The actual fit for BoundaryTransit-shaped checks in smart contracts is the place where authority *is* being delegated, mutated, or bridged:

- bridge attestations (cross-chain state claims)
- DAO vote → execution authority
- oracle claim → contract mutation
- multisig signer-set changes
- admin upgrade authority
- cross-chain bridge messages

Those are the surfaces where fake continuity hurts. Naming `msg.sender == owner` as self-attestation misses the actual seam.

## Practical application ranking (operator's order)

For where this pattern could earn its keep, ranked by how concrete the consumer is:

1. **NQ claim preflight** — *instrumented ≠ accountably monitored*. The Prom → NQ seam is the most concrete forcing case in the corpus right now.
2. **AG action gate** — *evidence / receipt / policy text ≠ authorized mutation*. Pre-action gate that turns refusals into action blocks.
3. **Code review / CI lint** — detect bad transits before they harden into code. Less runtime, more design discipline.
4. **API gateway refusal receipts** — productizable if anyone hates themselves enough.
5. **Supply chain / provenance** — possible but crowded by SLSA / in-toto / SBOM; would need to position as anti-laundering around provenance, not new framework.

Smart contracts are not in this ranking. If they appear later, the entry points are the bridge / DAO / oracle surfaces named above.

## What this note is NOT

- Not a claim that BoundaryTransit is Kerberos, or a replacement for it, or a generalization of it.
- Not a Lean obligation. The Lean scratch already exists; this note is the operational reading, not a new formalization target.
- Not a productization plan. Application ranking is informational ordering, not a roadmap.
- Not exhaustive on Kerberos. Real Kerberos has revocation, replay-cache, PA-data extensions, KDC HA, FAST armoring, etc. — each of which is its own fossil-record entry if pulled. This note covers the load-bearing six features.
- Not a public-facing essay. Tooltheory layer; sideways kitchen.

## Cross-references

- Scratch encoding: `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (category-2 fenced proof-of-encodability).
- Parent doctrine map: [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) — family rows are what the Kerberos features map onto.
- Custodian-binding row: [`../custodian-binding-accountability-candidate.md`](../custodian-binding-accountability-candidate.md) — Kerberos delegation maps here.
- Federation result: [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — the doctrine the BoundaryTransit shape exists to enforce.
- Related sideways notes: other entries in `working/tooltheory/` for adjacent operational patterns.
