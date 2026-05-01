# Δt Framework

A research series on systemic failure, temporal mismatch, authority collapse, and recovery under degraded conditions.

The papers develop the theory. The Lean repo audits selected claims. The point is not to make the theory look inevitable; the point is to record what survives contact with formal definitions.

Some claims survive. Some narrow. Some break. The breakage is kept on the record.

## Start here

1. **What is the Δt framework?** — [`preprint/README.md`](https://github.com/unpingable/papers/blob/main/preprint/README.md) is the conceptual map of the research program: paper titles, themes, and how the series fits together.
2. **Paper map** — [`formalization-index.md`](formalization-index.md) crosswalks every paper against its formalization status: certified, sharpened, exposed-as-loose, or bridged.
3. **Claim register** — the companion Lean repo records every formalized claim's status as BROKEN, STALE, SOUND, or OPEN. The register is `CLAIM-REGISTER.md` in [`unpingable/lean`](https://github.com/unpingable/lean) ([reading portal](https://unpingable.github.io/lean/)).
4. **Published preprints** — current versions are on [Zenodo](https://zenodo.org/) under the *delta-t-framework* series.

## What this is not

This is not a claim that Lean proves the whole theory true.

Lean is used to test selected structural claims from the prose: whether they follow from explicit definitions, whether they require narrower conditions, or whether they were only useful as discovery slogans. The formalization is a forcing function against theory-by-metaphor; it does not replace case studies, simulations, or operational evidence.

The BROKEN and STALE entries in the claim register are evidence of where the original prose overreached. They are kept deliberately. The project's honesty about that is part of what makes the audit register legible — it stops the framework from being post-orientation prose presented as pre-orientation prose.

## The two repos

- **Papers** — [`unpingable/papers`](https://github.com/unpingable/papers) — develops the theory.
- **Lean** — [`unpingable/lean`](https://github.com/unpingable/lean) ([reading portal](https://unpingable.github.io/lean/)) — audits selected claims.

This side develops; that side audits.
