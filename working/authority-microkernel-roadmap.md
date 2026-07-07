# Authority Microkernel — far-out roadmap + lineage (candidate, build nothing)

*Status:* CANDIDATE / far-out roadmap, filed 2026-07-06. Captured from a live
ChatGPT thread (same session as the sequent island + dynamic admissibility).
**This is the maximal-calculus register: file-now, work-never until a forcing
case.** It is captured for two reasons only: (1) the *reframing* is
doctrinally load-bearing and worth not losing; (2) the *lineage pass* is
genuine anticipatory prior-art evidence (scars-as-evidence) that stops us
rediscovering the field under fresh vocabulary. It is NOT a build plan.

## The reframing (the part worth keeping)

The old ambition — a "universal admissibility calculus" — stays dead
([[project-no-unifier-without-laundering]], [[project-distributional-admissibility-tombstone]]).
The only survivable shape is its inversion:

> A universal authority calculus is **not a universal authority**. It is a
> universal *discipline for preventing local authority claims from becoming
> global by accident.*

Sharper:

> **Universality lives in the refusal laws, not in the permissions.**
> Permissions are local. Refusals can be universal.

You *can* have universal **negative** laws (no self-minted standing, no
authority amplification, no scope expansion, no implicit bridge, no
observation-as-permission, no proof-as-runtime, no runtime-as-proof, no
memory-as-consent, no operator-action-as-truth). Positive authority stays
local. That asymmetry is the whole content — and it is exactly the
anti-laundering posture already resident, not a new empire.

## The microkernel cut (the analogy that names the architecture)

Not a microkernel OS — a **microkernel authority calculus**. The mapping:

| Microkernel OS | This |
|---|---|
| Kernel | tiny invariant / refusal-law core |
| User-space services | local `AuthorityProfile`s (own meaning) |
| IPC | explicit `Bridge P Q` (paid crossing) |
| Capabilities | scoped receipts / effective caps |
| Drivers | adapters (Porter, Gmail, Docker, calendar, runtime) |
| Syscalls | admitted transitions |
| Fault isolation | profile-local refusal |
| No shared address space | **no shared ontology** |
| Kernel policy minimalism | universal *negative* laws only |

Doctrine line:

> **The kernel owns refusal. Profiles own meaning. Bridges own crossing.
> Receipts carry bounded authority.**

The load-bearing theorem shape (if ever built):

```text
No local profile can acquire global authority except through an explicit
Bridge P Q whose obligations are paid and whose resulting capability is
bounded by source scope, target scope, freshness, verdict, and bridge cap.
```

Cursed name: `no_free_authority_functor`. This is the generalization of the
already-shipped `cap = min(tierCap, verdictCap, bridgeCap)`
([[project-admissible-incompleteness]]) and `ratified_scope_does_not_expand`,
and of the already-proved paid-crossing discipline in the v7 Artifact
Authority Profiles surface (`profile_does_not_compose_for_free`,
`cross_profile_conversion_requires_bridge`). **Note: much of the positive
kernel already exists in the Lean stack.** What does NOT exist and must not be
minted casually is the *universal AuthorityProfile/Bridge typeclass* — that is
the no-typeclass-export line and the unifier the doctrine refuses.

## Conservation laws (the universal negatives — all already have local instances)

- **No authority amplification**: `authority(output) ≤ authority(inputs, bridges, scope, freshness)` — resident as `cap`.
- **Scope non-expansion**: `scope(after) ≤ scope(before) ∩ scope(bridge)` — resident as `ratified_scope_does_not_expand`.
- **Observation ≠ authorization**: resident as [[project-non-reciprocal-admissibility-flow]], NoFreeStandingReadout.
- **Held ≠ discharged**: resident as BestEffortCompleteness / the incompleteness verdict axis.
- **Operator-required ≠ proof**: resident as `operator_required_is_not_proof`.
- **Typed refusal is first-class** (missing_bridge, stale_receipt, insufficient_scope, cannot_testify, candidate_only, scratch_only, operator_required, profile_mismatch, unpaid_obligation, ambiguous_claim, authority_surface_exceeded) — resident piecemeal across the kernels.

## Lineage / prior-art (the genuinely valuable capture)

We did not invent the components. If this is ever built, it is a *synthesis
cut*, and these are the toes to cite (anticipatory prior-art pass, ChatGPT
2026-07-06, receipts to verify before any claim):

- **Microkernel / reference monitor / TCB**: seL4 (small verified kernel, minimized TCB); NIST reference monitor (always-invoked, tamperproof, small-enough-to-analyze); Liedtke L4.
- **Capabilities / object-caps**: *Capability Myths Demolished*; EROS (capability + microkernel); UCAN (delegable verifiable caps, SPKI/SDSI lineage); ZCAP-LD (linked-data caps, chained delegation, caveats).
- **Authorization logic**: Abadi/Burrows/Lampson/Plotkin *A Calculus for Access Control in Distributed Systems* (`says`/`speaks for`/`controls`); Appel/Felten Proof-Carrying Authentication; NAL (Nexus Authorization Logic).
- **Trust management**: KeyNote/PolicyMaker (RFC 2704) — shared syntax/semantics across apps with differing app semantics (close to kernel/profile, but positive-policy where we want negative-law).
- **Proof-carrying**: Necula PCC; PCA (ship evidence, guard checks it) — but our receipts are *typed testimony*, not necessarily proofs.
- **Information-flow / decentralized labels**: Myers/Liskov DLM (no universal principal / classification — rhymes hard with no-universal-profile); IFC across autonomous lattices (bridge semantics for IFC).
- **Heterogeneous logics**: Goguen/Burstall *institution theory* (abstract signatures/sentences/models/satisfaction over many logics) — the academic ghost under "profiles + bridges."
- **Provenance / supply chain**: W3C PROV; in-toto; SLSA; Rekor/Sigstore (append-only receipt substrate). Provenance says *what happened*; we add *therefore what authority carries forward* (often: none).
- **Modern agentic auth (active collision zone)**: OAuth 2.0 Token Exchange (RFC 8693); Macaroons (attenuating caveats); Biscuit (Datalog attenuation); IETF draft-niyikiza-oauth-attenuating-agent-tokens (capability-monotonicity: authority only narrows per delegation — very close to `cap(output) ≤ cap(inputs)`); HDP draft (human delegation provenance / chain-of-custody for agents); Cedar (authorization language with Lean-backed sound/complete semantics + Rust impl — the annoying "already walked the Lean/Rust bridge" receipt).

**Novelty posture.** Weak claim (defensible): a *synthesis* of microkernel
architecture + capability attenuation + authorization logic + provenance +
heterogeneous-logic profiles for agentic/operational governance. Strong claim
(plausible, unproven, needs hostile prior-art pressure): existing systems
model authorization/provenance/delegation/policy-eval; this proposes a
*microkernel-style admissibility calculus where the universal layer is
primarily refusal/conservation law rather than permission*. **Do NOT claim
invention of** capabilities, attenuation, PCA, `says`/`speaks for`,
provenance, microkernels, reference monitors, policy-as-code, verified
authz languages, or chain-of-custody. That is honking clown shoes.

## The three artifacts a real version would need (gate, not plan)

1. Lean kernel: abstract profiles, bridges, caps, scopes, refusal laws + non-collapse theorems.
2. Hostile specimen suite: laundering attempts that provably fail.
3. Runtime binding (the bastard): a daemon (AG / Night Shift / Porter) that *actually refuses* a scratch-derived launch and emits the matching receipt. A theorem that "scratch cannot authorize runtime" is nice; the daemon refusing it is the thing with teeth. This is the NQ/AG lane — [[project-doctrine-as-executable-architecture]].

## Names to lock in the cabinet with "enterprise ontology"

FORBIDDEN cursed artifacts: `UniversalAdmissible`, `UniversalReceipt`,
`UniversalStanding`, `GlobalAuthorityProfile`, `ConstellationCustodyProtocol`.
If any of these appears, someone is building the monolith.

## Fence (binding)

Maximal-calculus register: [[project-maximal-calculus-registers]] governs —
file now, work never, until a *specific local system presents a bounded
question* (forcing-case discipline [[feedback-forcing-case]]:
do NOT invoke for maximal-calculus work). The value already banked is (a) the
refusal-first reframing and (b) the lineage table. Nothing here authorizes a
`UniversalAuthorityProfile` typeclass; that is the refused unifier.
