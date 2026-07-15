# DNS as Admissibility Fossil Bed

**Status:** Working note / parking lot. Filed 2026-05-19.
**Stance:** Adjacent-domain residue from the 2026-05-19 fossil-bed survey. Not promoted, not doctrine, not module-shaped. The cluster has enough internal density to deserve a parking lot rather than scattered patches across four files.
**Posture:** Phrase mine + one named gap, **consumer-watching regime** (updated 2026-05-19, same day; policy corrected 2026-07-14). The initial audit confirmed no live consumer; same-day operator update flagged `~/git/nq-witness` (claim-preflight registry, profile-defined claim-kinds, witness-standing vocabulary) as candidate consumer with DNS potentially becoming the second claim-kind. That affects priority and possible public promotion, not permission to formalize: a coherent authoritative-absence contract may be developed in Scratch first and may lead the implementation. Naming or adopting the contract does not establish conformance; that requires an explicit mapping plus runtime evidence or a refinement proof.

---

## Why the cluster earns a parking lot

The 2026-05-19 fossil-bed audit identified DNS as the densest single source of admissibility-shaped vocabulary in pre-1990 infrastructure literature. RFC 1034 (zones / delegation / TTL), RFC 2308 (negative caching), RFC 4033 (DNSSEC), RFC 2181 (data-trustworthiness ranking) each encode primitives the kernel rediscovered under different names.

Scattering the ten DNS residues across `authority-observable-not-constructible.md`, `laundering-move-watchlist.md`, `where-admissibility-fits.md`, `signal-authority-candidate.md`, and the MultiReceiptComposition example would diffuse the cluster into loose papers in the wind. This note holds them together with explicit cross-pointers to where each would land if individual promotion is later authorized.

It is *not* doctrine. It is *not* a paper candidate. It is *not* a primitive. It is recognition vocabulary parked where future-claude can find it without re-running the audit.

---

## Seven-part mapping (DNS → admissibility kernel)

| Kernel field | DNS instantiation |
|---|---|
| **Claim** | name/type/class answer, or denial (NXDOMAIN/NODATA) |
| **Evidence** | RRset, authority section, DNSSEC chain, SOA serial, cache metadata |
| **Standing** | root/TLD/zone-authoritative server; validating resolver; cache-policy operator |
| **Scope** | zone cut, bailiwick, view/split-horizon, RR type |
| **Precedence** | authoritative > cached; signed > unsigned; fresher > stale; in-bailiwick > out-of-bailiwick |
| **Consequence** | connection routing, mail routing, service discovery, signed denial |
| **Receipt** | cached RRset + TTL + validation result + resolver response code |

The mapping is clean. DNS predates this kernel's vocabulary by ~40 years; the kernel's vocabulary is closer to DNS than DNS is to the "database lookup" frame that later compressed it.

---

## Per-candidate verdict

| Concept | Keeper | Kernel home / cross-pointer | Verdict |
|---|---|---|---|
| TTL / cache freshness | *TTL is the authorized lifetime of reuse, not the lifetime of truth.* | `Freshness.lean`; `authority-observable-not-constructible.md` (the just-filed *authorized staleness* keeper from DNS) | **Already covered** by 2026-05-19 patch |
| Negative caching | *A cached denial is still a claim.* / *Absence may be admissible, but only under signed/delegated scope and TTL.* | `Authority.BasisVerdict.noBasis` collapses two shapes; see "real gap" below | **Real gap, bounded formal candidate + stress-case spec** |
| Glue records | *A pointer needed to reach authority is not authority.* | Receipt/Authority split | Prose residue, modest |
| Bailiwick | *Additional data is not additional authority.* | Scope-of-standing: `FiatAdmissibility.outOfScope`, `SurfaceAuthorization` scope fence | **STRONG prose residue** |
| Delegation / zone cuts | *Delegation is not answer custody. It is authority to answer within a cut.* | `BasisDerivation` chains; `Examples.MultiReceiptComposition`; multi-mint doctrine | Worked example for existing multi-mint pattern |
| DNSSEC validation | *Authentication proves origin, not wisdom.* / *A signed answer can still be stale, scoped, useless or wrong-for-purpose.* | `authority-observable-not-constructible.md` (Receipt vs Authority; construction-discipline) | **STRONG prose residue** |
| Split-horizon | *Different answers are not contradiction until scope is erased.* | `Examples.MultiReceiptComposition` (DISPUTED-as-multi-mint); `SurfaceAuthorization` scope | **STRONG prose residue** |
| Lame delegation | *A named authority that cannot testify is not a witness.* | NQ aperture (witness standing); `signal-authority-candidate.md` (silence ≠ revocation, neighbor) | NQ-flavored; flag only, do not file here |
| Cache poisoning | *Poisoning is advisory data acquiring cache standing.* | `laundering-move-watchlist.md` Section A (advisory → authority; `FiatAdmissibility` requiresMediation→allowed) | **STRONG prose residue** |
| SOA serials / propagation | *Publication is not propagation. Propagation is not fresh standing.* | `signal-authority-candidate.md`; `commitment-standing-decay-candidate.md`; embargoed-CVE specimen of temporal-scope gap | Prose residue, adjacent specimen |

---

## Keeper inventory (filing targets if promotion is later authorized)

The four STRONG residues, with their natural homes — **not patched today; named so the audit isn't re-run cold:**

- **Bailiwick** *(Additional data is not additional authority.)* → `authority-observable-not-constructible.md` as scope-of-standing keeper, OR `laundering-move-watchlist.md` Section B as the *out-of-scope → in-scope* laundering handle.
- **DNSSEC** *(Authentication proves origin, not wisdom.)* → `authority-observable-not-constructible.md` near the existing Receipt/Authority split and the two filed fossil-bed keepers (authorized-staleness, delivery-not-endorsement). Composes directly with the construction-discipline doctrine.
- **Split-horizon** *(Different answers are not contradiction until scope is erased.)* → docstring keeper for `Admissibility.Examples.MultiReceiptComposition` in `Derivation.lean`, OR adjacent-domain specimen in `where-admissibility-fits.md`'s CVD entry.
- **Cache poisoning** *(Poisoning is advisory data acquiring cache standing.)* → `laundering-move-watchlist.md` Section A as cited fossil for the `FiatAdmissibility` requiresMediation→allowed laundering family.

The five modest/adjacent residues (TTL-already-filed, glue, delegation-cut, lame-delegation, SOA-propagation) live in this parking lot only. They are recognition vocabulary, not promotion candidates.

---

## The one real gap: authoritative absence

**Negative caching is the only DNS concept the kernel does not structurally encode.**

DNS distinguishes three shapes the kernel currently collapses into one:
- *No answer found* (lookup didn't happen, server unreachable, network failure) — no Receipt
- *Resolver-side timeout / SERVFAIL* — non-Receipt, consumer-side adjudication required
- *Authoritative negative answer* (NXDOMAIN/NODATA, signed and TTL-bounded, RFC 2308) — **a Receipt with denial standing**

The Lean kernel's `Authority.BasisVerdict.noBasis` collapses the third shape into the first. There is no structural way to distinguish *"we have no basis"* from *"the authority for this scope returned a signed claim that no such basis exists."* In Standing's vocabulary, this is closer to a `AssessmentResult` variant that doesn't currently exist — Standing's negative verdicts are all positive *failure*-claims, not positive *absence*-claims.

This gap is adjacent to but distinct from:
- Open Question 6 in `admissible-recovery-semantics.md` (Same-Basis Independence — about *positive* claims)
- The temporal-scope gap at the Δt crosswalk (about *when* a claim was true)
- `signal-authority-candidate.md` (silence ≠ revocation — adjacent, but signal-authority is about *receiving* silence; authoritative absence is about *issuing* signed denial)

**Stress-case spec:** distinguish *"I have no basis"* from *"I have a signed, scoped, TTL-bounded claim of absence."* A consumer instance would test and prioritize the distinction, but the abstract contract can be formalized first. The candidate filing would be a small additional `BasisVerdict` variant or a sibling `AuthoritativeAbsence.lean` module — deflationary name, refuses the Δt-universal-solvent framing.

**Update 2026-05-19 (same day, post-audit):** `nq-witness` has surfaced as candidate consumer. The repo has a profile / claim-kind registry with witness-standing-shaped vocabulary (`standing.authoritative_for`, `standing.advisory_for`, `coverage.can_testify`, `cannot_testify`, `kind` field on observations). Operator-side signal: *"DNS may be the second claim-kind forcing case for the claim-preflight registry."* The witness-standing shape is structurally adjacent to authoritative-absence (an NXDOMAIN-style verdict is a claim-kind whose authoritative answer is a signed denial within a bailiwick).

Aperture note: NQ design routes to nq-claude (cross-SME elision, per `feedback-multi-model-routing`). This note records *that* nq-witness has surfaced as candidate, not *how* DNS would map onto its registry schema. The mapping work belongs in `nq-witness/` or in nq-claude's session, not here.

Regime classification updates: gap moves from *"1 specimen, no consumer"* to *"1 specimen, consumer surfacing — watching."* Under the historical audit rubric, a live consumer implementation authorized a small axis-kernel while a named candidate did not. Under the 2026-07-14 correction, either state permits bounded Scratch formalization; a live mapped consumer instead supplies stronger priority and promotion evidence. The Standing/Freshness implementation remains useful instantiation evidence. Public promotion and a claim of `nq-witness` conformance still require the exact DNS-as-claim-kind mapping plus runtime evidence or a refinement proof.

Current status: **tracked, watching, not promoted.** Specimen count remains 1; consumer regime is *watching*. Formal development need not wait for concrete implementation.

---

## Promotion gate

This note does **NOT** by itself promote or mint:

- A new Lean module into the public surface (`DnsAdmissibility.lean`, `BailiwickStanding.lean`, `Glue.lean`, `AuthoritativeAbsence.lean`, anything DNS-shaped). A coherent bounded version may be developed in Scratch.
- A new paper directory.
- A "DNS of admissibility" doctrine or methodology piece.
- Promotion of any of the four STRONG residues into existing files without separate explicit authorization.
- A DNS-themed essay; the keepers compose into existing essay candidates (e.g. *When Compression Becomes Authority*, *The Floor Is Enough*) without their own piece.

Promotion requires evidence appropriate to the target:

- **For a Lean module's public promotion:** explicit custody review plus adequate claim and instantiation evidence. A constellation-resident mapped consumer is strong evidence, not permission to state the theorem and not conformance by citation alone. DNS-the-protocol is not a repo-mounted consumer.
- **For a paper directory:** a forcing case that escapes the existing keepers + cross-pointers above.
- **For doctrine:** three structurally-distinct independent specimens beyond DNS. The other 1980s fossils (Kerberos, AFS, NTP, SMTP, syslog, SNMP) share *Kerberos-shape* / *callback-shape* / etc. rather than DNS-shape; they are not structurally distinct specimens of the DNS gap class.
- **For patching a strong residue into an existing file:** explicit per-residue authorization. Default to lowest filing level that preserves the load-bearing claim.

---

## Cross-pointers

- `working/authority-observable-not-constructible.md` — Receipt/Authority split; fossil-bed sibling aphorisms (DNS *authorized staleness*, SMTP *delivery is not endorsement*).
- `working/authority-debt-and-revocation.md` — revocation-channel doctrine; AFS-callback sibling aphorism.
- `working/laundering-move-watchlist.md` — Section A FiatAdmissibility requiresMediation→allowed; Section B advisory→authority handles + *Schedule → standing*; Section C SNMP fossil for observe→mutate.
- `working/where-admissibility-fits.md` — Coordinated Vulnerability Disclosure entry (multi-mint specimen); Δt crosswalk sentence.
- `working/signal-authority-candidate.md` — silence ≠ revocation; adjacent to authoritative-absence gap.
- `working/commitment-standing-decay-candidate.md` — rhetorical continuity vs operational revocation; propagation-lag adjacent.
- `working/anti-collapse-runbook.md` § 2½ — kernel-overlap audit procedure (this note's parent discipline).
- `LeanProofs/Admissibility/Freshness.lean` — metric-time admissibility kernel (Standing-shaped, TTL-shaped).
- `LeanProofs/Admissibility/Derivation.lean` § `Examples.MultiReceiptComposition` — DISPUTED-as-multi-mint worked example; split-horizon residue lands here if promoted.

---

## Provenance

- **2026-05-19 fossil-bed survey** (multi-model conversation) identified DNS as densest single source of admissibility-shaped vocabulary in pre-1990 infrastructure literature.
- **ChatGPT raid** produced the seven-part mapping plus ten candidate concepts with keeper-shaped phrasing, citing RFC 1034 (zones/TTL), RFC 2308 (negative caching), RFC 2181 (data-trustworthiness ranking), RFC 4033 (DNSSEC).
- **Web-claude prediction:** working note > scattered patches, given cluster density.
- **claude-code-papers (this writeup):** executed the kernel-overlap audit procedure (anti-collapse-runbook §2½), confirmed no constellation consumer at audit time, and filed a parking-lot working note. No module was built or promoted in that pass. One real gap (authoritative absence) was tracked with an explicit stress-case spec. Four STRONG residues were named with filing targets but not patched into target files.
- **Same-day operator update (2026-05-19; policy corrected 2026-07-14):** `nq-witness` flagged as candidate consumer with DNS as potential second claim-kind. Regime classification updates from *no consumer* to *watching*. Concrete implementation remains relevant to public promotion and conformance evidence, not permission for the formal contract to lead. Aperture note added: NQ-design content elides to nq-claude per cross-SME routing discipline; this note records the surfacing without elaborating on the mapping.
