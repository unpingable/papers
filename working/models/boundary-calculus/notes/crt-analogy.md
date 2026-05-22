# Speculative Analogy: Boundary Merge as Local-to-Global Gluing

Status: speculative analogy / non-doctrinal / candidate handle
Logged: 2026-05-21
Lives near: [locality-and-merge](./locality-and-merge.md); surfaces after the aperture proof in `LeanProofs/Admissibility/LocalBoundary.lean` closed without `sorry`, which made the "local-to-global compatibility" shape visible enough to name.

## The bridge

> Local boundary composition is a gluing problem.

This is not "number theory" in the primes / zeta / analytic-NT sense. It is number theory in the **local-to-global discipline** sense: congruences, CRT, gcd/lcm overlap logic. The bridge is methodological, not technical.

## CRT-shape of MergeAdmissible

CRT compatibility:

```text
x ≡ a (mod m)
x ≡ b (mod n)
```

has a coherent global solution iff `a ≡ b (mod gcd(m, n))` — the local claims agree on the overlap.

`MergeAdmissible`:

```text
LocalAllows lb₁ α → ¬(lbₘ.partition forbids α)
LocalAllows lb₂ α → ¬(lbₘ.partition forbids α)
```

is a compatibility condition between two local authorization claims and a merged observation space. It is not a global oracle; it is the *agreement-on-overlap* condition expressed in admissibility vocabulary.

## gcd / lcm picture

- `gcd` = shared substrate / overlap
- `lcm` = least envelope into which both embed
- coprime = no shared authority surface, trivial compatibility
- non-coprime = overlap exists, compatibility must be proven

`left_sound` / `right_sound` each say: "this local authorization embeds soundly into the merged envelope." That is closer to **lcm with compatibility** than to naive set union.

The DeepSeek near-miss (`lbₘ.authorized = lb₁.authorized OR lb₂.authorized`) was the naive-union move — pointwise OR with no overlap check. The aperture refused it by separating authorization (local) from safety judgment (merged), with a soundness predicate carrying the load.

## Candidate decomposition

If this analogy survives contact, `MergeAdmissible` could split into:

```lean
structure MergeAdmissible ... where
  overlap_compatible : OverlapCompatible lb₁ lb₂
  left_sound  : ...
  right_sound : ...
```

where `OverlapCompatible` names the shared substrate where the two local boundaries disagree-or-agree. That would be the CRT-shaped formal move. Not now.

## Scope fence

- This is a speculative analogy. Do not summon sheaves, schemes, or Grothendieck topologies on the strength of one closed theorem.
- The actual mathematical home is probably algebraic structure over permissions / partitions / observations — not primes, not zeta, not Galois.
- CRT and gcd/lcm are useful as **disciplined analogies** for local-to-global compatibility logic. They are not the calculus.
- Do not file an `OverlapCompatible` Lean definition until a forcing case makes it earn its keep. The current two-field merge predicate is sufficient for the aperture; expansion requires a specimen the current shape cannot handle.

## Why the analogy is annoyingly good

The aperture proved that local authorization plus a compatibility predicate is enough for global safety. That is structurally the CRT move: don't appeal to a global oracle; demand the locals agree on the overlap. The reason it feels load-bearing is that the proof's collapse through `MergeAdmissible.{left,right}_sound` was structurally the same shape as a CRT existence argument: combine the residues *via* the compatibility, not despite it.

That doesn't make the calculus number-theoretic. It makes it part of the same family of local-to-global discipline patterns.

## Keeper (speculative)

> Local permissions compose only when they agree on the overlap they create.

## Forward-pointing

- If a future slice needs `OverlapCompatible`, this note is where the candidate is parked.
- If sheaf vocabulary becomes tempting, run the [[feedback-kernel-overlap-audit]] before promoting any of it — the kernel substrate is already dense, and "sheaves on the admissibility site" is the kind of phrase that minted a field once and could mint a generic one here.
- Do not retire this note when the analogy is no longer load-bearing; archive its conclusion if/when it stops paying rent.
