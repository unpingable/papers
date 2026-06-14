# Observer Foundation — Promotion Preflight (NOT promoted)

**Status:** CANDIDATE / non-binding. Filed 2026-06-14. This is a *handle for
review*, not authorization to build. The observer scratch packet is complete
enough to establish the local no-go shape; **consolidation is ratification-tier**
and deliberately deferred. Name early, ratify lazily.

Do **not** consolidate in the same motion that produced the packet. Touching the
public foundation immediately after finding the cave is how you get a changelog
scar. Come back for this as its own deliberate act.

## What exists now (banked scratch, `~/git/lean/LeanProofs/Scratch/`)

The ladder, four fenced slices, all `lake env lean` green, `sorry`-free:

```
ConsumerRelativeFreshness     temporal → observer adapter (per-consumer clock)
  → ConsumerRelativeForce       Force : Consumer → Artifact → Prop; frame split
  → AbsoluteForceStampBridgePrice  the stamp-on-envelope priced to collapse
  → NoUniversalRoot             global section ⇔ consumer agreement (the center)
```

Enough to say observer is no longer vaporware. Not enough to freeze a public
vocabulary.

## Candidate public theorem (the nucleus claim)

> A consumer-independent force predicate exists **iff** all consumers agree on
> every artifact.

Lean: `has_global_section_iff_consumers_agree` (axiom-free).

## Candidate foundation nucleus (keep it TINY)

```lean
Consumer
Artifact
Force : Consumer → Artifact → Prop
ConsumersAgree
HasGlobalSection
has_global_section_iff_consumers_agree
```

Bias: the promoted nucleus should be exactly this and no more.

## Explicitly EXCLUDED from the foundation (stay application/scratch)

- `UniversalRoot` as a primary no-go — it is a **positive exception** for
  closed/single-root governance systems, not the foundation's no-go. (And it
  carries the empty-root vacuity: a root forcing nothing is vacuously universal.)
- `AbsoluteForceStamp` as a primitive — it is a bridge-price *application*.
- temporal clock mechanics (`ConsumerRelativeFreshness`) — the adapter, not the
  foundation.
- receipt-specific / stamp-specific semantics.

## Open taxonomy questions to settle BEFORE consolidating (the real work)

These are naming-the-taxonomy questions, not Lean-difficulty questions. Freezing
the wrong abstraction here is the kernel-goblin-with-commit-access risk.

1. **What is `Consumer`?** operator, verifier, catcher, jurisdiction, runtime,
   tenant, root, or policy domain? (Different downstreams want different ones.)
2. **What is `Force`?** admission, enforcement, reliance, constraint, visibility,
   or legal-ish consequence?
3. **Is agreement-over-all-artifacts the intended public strength?** Too strong,
   or exactly the clean no-go? (Currently: exactly clean, but confirm against the
   intended consumer.)
4. **Does `UniversalRoot` belong in the foundation at all**, or only as an
   application lemma for single-root governance (e.g. agent_gov's
   qualified-operator genesis root)?
5. **What does "stamp" mean?** receipt predicate, label, signature, attestation,
   policy claim, or envelope metadata?

## Graduation steps (when the answers above exist)

1. Write the answers to 1–5 as a one-page taxonomy decision (this doc, filled in).
2. Consolidate the duplicated `Consumer`/`Force` vocab (currently re-stated per
   scratch file) into ONE foundation module.
3. Promote `has_global_section_iff_consumers_agree` toward `CLAIM-REGISTER.md`
   (Lean repo) — that promotion is the ratification act; get explicit language.
4. Leave the adapters/bridge-price/universal-root as applications citing the
   nucleus.

## Pointers

- Lean scratch: `~/git/lean/LeanProofs/Scratch/{ConsumerRelativeFreshness,
  ConsumerRelativeForce,AbsoluteForceStampBridgePrice,NoUniversalRoot}.lean`
- Index ledger: `docs/formalization-index.md` (2026-06-14 observer entry)
- agent_gov tie: `OperatorBasisGateInput` warrant — qualified-operator = genesis
  root; `universal_root_licenses_stamp` legitimizes its stamp single-rooted;
  federation breaks the section.
