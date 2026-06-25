# Aqueduct-LOA — runtime projection of the witness-separation no-go (specimen)

**Status:** specimen note. Source: `aqueduct-loa-rust-specimen.rs` (claude-web, 2026-06-25).
NOT wired, illustrative. Build receipts below are real. Filed 2026-06-25. Not a kernel.

A single-file Rust specimen encoding three corpus refusals (claimed) at type level for a
software-supply-chain / license-attestation gate. Worth keeping for two reasons: it is a
faithful **projection** of `LeanProofs/Scratch/PredicateWitnessSeparation.lean` into a
runtime substrate, and it **embodies the predicate-witness turtle by executing it** — the
prose forbids fabrication and `main()` fabricates a witness twelve lines later.

## Build receipts (verified 2026-06-25, rustc 1.94, --edition 2021)

- Clean compile **EXIT=0**; run **EXIT=0**; all four `assert!`-guarded doctrinal properties held.
- The load-bearing claim: uncommenting `is_cleared` (`r == Resolution::Admissible`) fails with
  **`error[E0369]: binary operation == cannot be applied to type Resolution`**. That
  failure-to-compile *is* the No-Silent-Conversion proof — verified, not asserted.

## Honest grade — one property type-real, two fenced

| Kernel | How it's actually enforced | Grade |
|---|---|---|
| **No Silent Conversion** | TYPE-REAL — no `PartialEq` (compiler-proven), `#[must_use]`, `decide()` return type makes `Proceed` reachable only from `Admissible` | the real thing |
| **signed ≠ witnessed** (`verify_binding`) | RUNTIME guard at chokepoints; nothing stops a caller reading `coverage.examined` directly | runtime, not a type |
| **No Negative Clearance** (`ClosureWitness` required) | STRUCTURAL default — ships witness-less so whole-artifact clearance is `Refused` | structural; witness *soundness* out of scope |

## The header is itself a signed≠witnessed event (the self-catch)

The module header brags *"each property is enforced by a type, not a comment."* That sentence
is oversold for two of the three — and it's the **bragging sentence** that laundered
runtime-checks and a structural default into "type guarantees." The footer
("WHAT THIS FILE DOES NOT ENFORCE") bought back the *liveness* overclaim but not this one.
**The fence gap is in the header, not the footer.** The doctrine caught the demo's *author*,
not just the demo: a signed-not-witnessed event inside a file about signed-not-witnessed.

## The turtle, executed (the load-bearing finding)

`ClosureWitness` is itself subject to signed≠witnessed: `builder_digest` is carried and
**never checked**, `HermeticBuild` is unverified. The `ClosureWitness` comment says *"We
pointedly do not fabricate one"* — and `main()` fabricates one twelve lines later to light the
green path. The file could not stay honest about fabrication for the length of one file. That
inconsistency is not a bug; it is the predicate-witness turtle **executed** — the witness needs
a witness, the prose half-knew, the code contradicted it.

## Does the regress bottom out? — `no_unifier_without_laundering` reaches in

The witness regress does NOT bottom out in more witnesses. It terminates **exactly two ways**:

1. **A verified closed-world basis** — hermetic build with a *verified* builder digest,
   complete material capture: a finite, checkable ground. The only place the turtles stop
   *without* laundering.
2. **A signed human closure contract** (the commented-out `HumanContract` variant) — which does
   NOT stop the regress; it **relocates** it onto a named human who becomes the witness of
   record. ("Humans configure scope but cannot configure truth.")

`ClosureWitness::HermeticBuild { builder_digest }` with the digest unchecked is **neither — a
turtle wearing the ground's clothing.** It is precisely the laundering case this morning's Lean
no-go rules out. That is where `PredicateWitnessSeparation.lean` reaches into the Rust and names
which struct is lying.

## Provenance discipline — coherence-under-translation, NOT independent convergence

Do **not** read this as "two substrates independently discovered the recursion." claude-web
wrote the Rust while carrying the full doctrine (No Negative Clearance, signed≠witnessed, the
witness-separation shape) in context — it *imported* the turtle and the type system made it
visible. This is **one witness (the Lean file) + two faithful copies (this Rust, the AG note)**,
not three witnesses. Counting correlated copies as independent witnesses is exactly the
laundering [[project-heterogeneous-turtles-not-witnesses]] / same-custody refuses — discount it
the same way we discounted the Kalshi lanyard and Chatty's sunglasses. The map has the
territory's shape because it was *drawn from* the territory — which is itself the
`coverage ⊬ closure` relation the file is about. (My first-pass "interferometry fringe held"
read was me doing the laundering the corpus keeps flagging; corrected here.)

## Pointers — same result, three substrates

- **The witness:** `~/git/lean/LeanProofs/Scratch/PredicateWitnessSeparation.lean` (sorry-free, propext-only).
- **Canonical doctrine:** `~/git/agent_gov/docs/cross-tool/predicate-witness-infrastructure-note.md` (AG-Claude's custody root).
- **Paper/Lean companion:** `predicate-witness-gap.md`.
- **Source:** `aqueduct-loa-rust-specimen.rs` (this directory).
- Sibling non-lifts: `prediction-markets-case.md`, `distributional-shadow-tombstone.md`.
