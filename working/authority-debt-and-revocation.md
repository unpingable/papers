# Authority Debt and Revocation

**Status:** captured note / staging primitive. 2026-05-07.
**Scope:** OS authority-substrate survey (gnat-claude doctrine + survey), the cross-substrate authority doctrine (`authority-observable-not-constructible.md`), and the Lean Admissibility kernel's corrective / revocation work (`Corrective.lean`, `CorrectiveBoundary.lean`).
**Stance:** **DO NOT PROMOTE main keeper line yet.** Held pending Hurd / seL4 / Plan 9 row review by paper-claude after the OS doctrine stabilizes. The companion sub-rule "proof-backed structural enforcement narrows the TCB but never collapses it" has already been promoted to the main authority doctrine; this note carries the second candidate sub-rule still in the staging register.

---

## Kernel thought

> **Delegation that cannot be withdrawn is authority debt.**

A substrate may make delegation structurally honest without making revocation structurally available. In that case, delegated authority persists as debt: an obligation the system has created but not equipped itself to retire.

The companion structural claim — paper-shaped, also staged:

> **Revocation is not the inverse of delegation. It is a separate obligation channel.**

These two lines are the candidate keepers from the OS authority-substrate survey (gnat-claude `survey_os_authority_substrates.md`, finding 6). Both are stronger than substrate-family-expansion alone; both are what makes the OS work earn its keep beyond extending the gnat lab matrix. Both are held pending row review.

## Why this is a separate axis (the 5a/5b split)

The 5a/5b split — attenuation vs revocation as separate columns in the OS survey — was earned post-survey by row pressure. Capsicum, Hurd, macaroons, and Fuchsia each had distinct stories for the two mechanisms, and bundling them into one bullet papered over the substrate divergence. Promoted retroactively, same shape as the 4a/4b (confer / recognize) and 7a/7b (inter-task / inter-host) splits.

The structural distinction:

- **Attenuation (5a)** — safe shaping *on the way down*. Can authority be narrowed before or during transfer? `cap_rights_limit` (Capsicum), `zx_handle_replace` with reduced rights (Fuchsia), caveat extension (macaroons), namespace narrowing on fork (Plan 9 / Linux mount-ns), `cap_copy` with narrower rights (seL4).
- **Revocation (5b)** — temporal obligation *after* transfer. Can already-delegated authority be withdrawn later? `cap_revoke` walking the derivation tree (seL4), `zx_handle_close` (Fuchsia, by holder), FD-close (Unix, crude), bind/unmount (Plan 9, namespace-shaped). Or absent in-band: Hurd has neither clean revocation primitive; macaroons defer to TTL caveats and out-of-band root-key rotation.

They look like siblings from 30,000 feet. At ground level, one is a shaping operation; the other is a continuing burden. A substrate that makes attenuation first-class while leaving revocation under-specified is making *one* of these honest and the other a TTL-and-prayer arrangement.

## Methodological note (preserve as general rule)

The 5a/5b split was earned by row pressure, not stipulated in advance. The general rule worth preserving across any future axis work:

> **Do not split an axis because the theory likes symmetry. Split it because the rows make one column lie.**

Speculative axes create fake explanatory precision. A split earns promotion only when multiple rows independently force divergent answers. Pre-stipulating a 5a/5b in advance of the survey would have looked rigorous and probably been wrong about which mechanisms actually behave as siblings. Letting the survey pressure surface the split — and the post-hoc retro-fit at the same shape as 4a/4b and 7a/7b — is the right rhythm.

This matters beyond the OS survey because it disciplines any future axis-growth in adjacent work: the language-substrate matrix, the Lean kernel's primitive ratification, the boundary-calculus investigation. *Same rhythm, same gate.*

## Why this matters — substrate evidence

The OS survey shows many substrates make possession or transfer structurally honest while leaving withdrawal underspecified, conventional, deferred, or externalized. Concrete examples to preserve for the row review:

- **Unix file descriptors.** Held-open FDs survive `chmod` permission changes; revocation is approximate at best. The mode-bit change does not retroactively close the FD held by an already-running process. Honest delegation, weak withdrawal.
- **Macaroons.** Caveat-based attenuation is elegant and works without the root key. But there is no in-band revocation primitive — only TTL caveats and out-of-band root-key rotation. Beautiful 5a, deferred 5b. The bytes survive the wire with HMAC integrity, but withdrawing a macaroon already in circulation requires either waiting out its TTL or rotating the root key (which totalises everything else minted from that key).
- **Mach / Hurd ports.** Port possession and transfer are kernel-mediated and structurally honest; the substrate makes the *delivery* of authority unforgeable. But the substrate does not equip itself with a clean revocation primitive: `mach_port_destroy` on the receive side and `no_senders` notifications are the closest available, and neither is per-send-right revocation. The user-mountable-translator feature *amplifies* the gap because untrusted code can occupy authority-bearing positions in the namespace with no withdrawal primitive available.
- **Capability systems generally.** Vary sharply by whether revocation is first-class (seL4's `cap_revoke` walking the derivation tree), derivation-tree-based (Genode parent revoking child), registry-mediated (Erlang process-capability where the live custodian honors-or-retires refs), or punted into userland (Hurd, in practice). The variation is not noise — it is exactly the 5b axis.

The pattern: substrates that have first-class 5b read as robust under adversarial composition. Substrates with strong 5a but weak 5b accept the tradeoff but pay it in time-caveats / FD-close-only / no-rewiden semantics. Substrates with neither accumulate authority debt.

## Relation to the existing doctrine

The cross-substrate authority doctrine (`authority-observable-not-constructible.md`) currently has two promoted lines from the OS survey thread:

1. **Already promoted (main doctrine):**

   > *Proof-backed structural enforcement narrows the TCB but never collapses it.*

   Substrate-agnostic, sharpens "anti-laundering, not anti-forgery," and seL4's row makes it concrete without binding it to OS context. Reads cleanly without OS-specific framing — a reader of the main doctrine encountering it does not need to know seL4 to understand the move.

2. **Held in staging (this note):**

   > *Delegation that cannot be withdrawn is authority debt.*
   > *Revocation is not the inverse of delegation. It is a separate obligation channel.*

The two staged lines are stronger but **OS-survey-shaped**. Their force depends on the row characterizations to land cleanly. Promoting them prematurely would import OS-specific framing into the main doctrine before Hurd / seL4 / Plan 9 rows have been pressure-tested by an expert. Asymmetric promotion — one sub-rule promoted now, two held pending row review — is the discipline.

## Lean / Corrective bridge

The Lean Admissibility kernel's `Corrective.lean` and same-day-landed `CorrectiveBoundary.lean` are structurally adjacent to the OS revocation findings. Sketch of the analogy:

- `Corrective.lean` models corrective transitions (revocation, gap declaration) as down-edges over the authority surface, with `CorrectiveMonotone env` carrying the proof obligation that any concrete env must discharge: corrective steps cannot widen `AuthorizedSet`. The kernel pins the *shape* of the obligation; the obligation is vacuously satisfiable in the abstract kernel because behavioral laws on store ops aren't committed.
- `CorrectiveBoundary.lean` (added 2026-05-07) closes Gate A from `nondegenerate-store-semantics.md` by exhibiting model-dependence: identity-store models make the corrective+forward existential FALSE; nondegenerate models with verdict-sensitive `BasisDerivation` make it TRUE; the abstract `NondegenerateStoreSemantics` predicate captures the three commitments and the parametric theorem proves the existential follows.

If revocation is modeled as a per-environment obligation (the Lean kernel's stance), then the OS survey supplies the *substrate-language* version of the same primitive:

> Revocation is not the inverse of delegation. It is a separate obligation channel.

Both registers see the same structural fact — the OS survey from the substrate side, the Lean kernel from the obligation side. **Do not collapse the analogy too early**: preserve it as a likely cross-pointer for when the OS doctrine paper-promotes, then verify the formal mapping carefully. The kernel's `cap_revoke`-shape (transitive walk of a derivation tree) is one specific concrete mechanism; the abstract `CorrectiveMonotone env` obligation accepts any mechanism that discharges the same algebraic property. The bridge wants a precise mapping, not a glib equivalence.

## Promotion guardrail

The keeper line should remain staged until row review answers at least:

1. **Hurd:** does Hurd genuinely lack clean revocation at the right layer, or is the relevant revocation mechanism elsewhere in the server model (e.g., auth-server reauth-handshake semantics, `mach_port_destroy` patterns, dead-name handling, `no_senders` notifications)? Hurd's documentation is famously partial; the staging note flags this row as review-needed.
2. **seL4:** does the capability derivation tree (CDT) + `cap_revoke` machinery support the keeper line directly, or does the wording need to be narrower (e.g., "revocation that does not propagate through the derivation tree is authority debt")? The proof-boundary distinction (axis 2 vs axis 6) makes seL4 sensitive to this — over- or under-claiming the proof's scope is exactly the laundering vector the doctrine catches.
3. **Plan 9:** does namespace rebinding / unmount behavior count as revocation, withdrawal of reachability, or merely reconstruction of the naming world? The wire-native authority claim and the auth file (factotum, `/proc/N/ctl`-style auth ports) need primary-source sanity check before paper handoff.

Until those three are settled, keep the line as **staged doctrine**, not main doctrine. The companion line ("revocation is a separate obligation channel") is even stronger and more paper-shaped; it should be promoted only after the keeper itself lands and the substrate examples have been row-checked.

## Constellation pointers

- `authority-observable-not-constructible.md` — main authority doctrine. Already-promoted TCB-doesn't-collapse sub-rule lives there. Border-crossing tables and three-discipline frame are the substrate-level apparatus this note's keeper sits adjacent to.
- `~/.claude/projects/-home-jbeck-git-gnat/memory/doctrine_os_authority_substrates.md` — gnat-claude OS doctrine note. Eight axes, three primary modes + temporal-self-binding modifier, Q1/Q2/Q5 resolutions, post-survey 5a/5b split discipline.
- `~/.claude/projects/-home-jbeck-git-gnat/memory/survey_os_authority_substrates.md` — gnat-claude OS survey, ten rows × eight axes (with three splits). Findings 1-10 including the keeper-line origin (finding 6) and the methodological note (post-survey split earned-by-row-pressure).
- `accountable-mutation-os-layer.md` — sibling working note on accountable mutation as missing OS-layer primitive. Asks "is this mutation still justified?"; the authority-debt question asks "*can* this mutation be unjustified later?" Both basis-validity questions, asked at different time directions.
- `admissible-recovery-semantics.md` — sibling working note on corrective monotonicity / non-laundering recovery semantics. Adjacent: same-K is the load-bearing distinction (corrective cannot relaunder failed authority for the same basis K, only re-entry through fresh K' via a forward step suffices). The authority-debt line asks the symmetric question: even with same-K corrective discipline, if revocation is structurally unavailable, the down-edge is *unenforceable* and authority accumulates regardless.
- `~/git/lean/LeanProofs/Admissibility/Corrective.lean` — Lean kernel's corrective monotonicity layer. `CorrectiveMonotone env` obligation; `corrective_no_authority_laundering` corollary.
- `~/git/lean/LeanProofs/Admissibility/CorrectiveBoundary.lean` — Lean boundary result (added 2026-05-07). Model-dependence proof of the corrective+forward existential; abstract `NondegenerateStoreSemantics` predicate; witness model satisfies the predicate.

## Falsifier

This staging primitive is **empty** if its keeper line reduces cleanly to existing capability-systems vocabulary — "transitive revocation," "capability propagation," "object-capability discipline."

Bite test: does the keeper line distinguish failure modes those vocabularies miss?

Candidate distinguishing claims (held, not promoted):

- **Authority debt is a substrate-level claim, not a system-level claim.** The capability-systems literature has rich treatments of revocation as a design choice; the keeper line claims something stronger — that the *substrate's* failure to make revocation first-class is a debt the *system* inherits, regardless of how careful the userland is.
- **5a/5b separation is a substrate fact, not a design taste.** Capability-systems vocabulary tends to treat attenuation and revocation as related design choices to be made together. The OS survey shows substrates make them independently, and the survey-pressure split was the diagnostic.
- **The Lean bridge ("separate obligation channel") makes the substrate fact formal.** If revocation collapsed cleanly into the inverse of delegation in capability theory, the Lean kernel's `Corrective.lean` would not need a separate `CorrectiveMonotone` obligation; corrective steps would just be inverse-forward steps. They aren't, and the kernel's separate obligation is the formal evidence.

If those distinguishing claims reduce cleanly to capability-systems vocabulary under careful reading, the staging primitive retires.

## Forcing case (not yet)

Per three-term vocabulary (forcing case / default future work / prewarmed branch): **prewarmed branch**, not forcing case. The OS survey is structurally complete pending row review; the keeper line is staged; the Lean bridge is sketched but not formalized.

Candidate forcing-case-shaped material:

- A concrete laundering path in `agent_gov` / `standing` / a Governor-side instantiation where revocation is structurally unavailable and the system is exhibiting authority debt operationally — the kind of thing that would make the keeper line earn an immediate paper-promotion and a Lean-side formalization sprint.
- An expert-row-review session that pressure-tests the Hurd / seL4 / Plan 9 characterizations and either ratifies the keeper line for promotion or surfaces a narrower wording.
- A first concrete `BasisDerivation` in `agent_gov` that reads `RevocationStore` — at which point `Corrective.lean`'s vacuous obligation bites, and the OS survey's keeper line gets a Lean-side cash-out via `CorrectiveBoundary.lean`'s `NondegenerateStoreSemantics`.

## Provenance

- **2026-05-07.** Origin in gnat-claude OS authority-substrate survey (sibling to the language-substrate gnat lab from 2026-05-06 → 2026-05-07). ChatGPT's "axis-resolution + post-survey refinement" pass locked the eight axes (with three splits) and identified the asymmetric promotion discipline. Survey finding 6 surfaced the keeper line; finding 7 surfaced the wire-native-authority companion sub-rule.
- **Multi-model lineage:** gnat-claude (survey + axis-locking), ChatGPT (Q1/Q2/Q5 resolutions, 5a/5b post-survey split, asymmetric promotion discipline, paper-portable wording), claude-code-papers (this writeup, Lean-bridge cross-pointer, working-note staging).
- **Same-day Lean landing:** `CorrectiveBoundary.lean` added 2026-05-07 in `~/git/lean/LeanProofs/Admissibility/`. Model-dependence boundary result that closed Gate A from `nondegenerate-store-semantics.md`. The OS survey's authority-debt line and the Lean kernel's corrective-monotonicity obligation are now structurally adjacent in two registers; the bridge is sketched here but formal mapping deferred.
- Filed as captured note / staging primitive. Repo-public artifact. **Do not promote main keeper line until Hurd / seL4 / Plan 9 row review answers the three guardrail questions.**
