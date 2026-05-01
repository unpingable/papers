# Δt Framework — Papers and Working Notes

This repository contains the prose side of the Δt framework: a research series on systemic failure, temporal mismatch, authority collapse, and recovery under degraded conditions.

The papers develop the theory. The companion Lean repo audits selected claims by translating them into explicit definitions and theorem statements, then checking whether they actually follow. Some survive. Some need narrower conditions. Some break.

The breakage is part of the record, not a defect — every formalized claim carries a status of BROKEN, STALE, SOUND, or OPEN in the Lean repo's `CLAIM-REGISTER.md`. That register is one of the more honest interfaces in the project: it makes legible which slogans were structural claims and which were only useful as discovery handles.

This is not a claim that Lean proves the whole theory true. The formalization is a forcing function against theory-by-metaphor; it does not replace case studies, simulations, or operational evidence.

## Companion repos

- **This repo (papers):** prose papers, working notes, primitives, exploratory writing, specifications, and the research-program structure
- **Lean repo:** [`unpingable/lean`](https://github.com/unpingable/lean) — formal claim register, proof attempts, corrected theorem statements, and the BROKEN / STALE / SOUND audit

The paper-indexed crosswalk between the two — which papers have formalization warrants, what kind (certify / sharpen / expose looseness / bridge), and whether the mapping is paper-ready — lives in [`docs/formalization-index.md`](docs/formalization-index.md). The module-indexed inverse lives in the Lean repo at `PAPER-MAP.md`.

## Structure

- `preprint/` — numbered research papers published on [Zenodo](https://zenodo.org/) as part of the *delta-t-framework* series
- `working/` — upstream framing, theoretical substrate, and exploratory writing not yet published
- `working/primitives/` — named failure shapes and meta-doctrine (e.g. `stale-binding`, `role-accretion`, `inhibitory-governance-collapse`)
- `specifications/` — formal architecture and design specifications
- `templates/` — reusable templates for metadata and READMEs
- `tools/` — operational scripts (currently: `zenodo_validate.py`, a pre-push drift checker)
- `docs/` — paper-side crosswalk to the Lean formalization

## Reading Guidance

If you're new:
- Start with the preprints — PDFs and DOCX files are the canonical published artifacts
- Use the Markdown files for source context or LLM ingestion
- See `preprint/README.md` for a conceptual map of the research program
- For the audit story (which claims survived formalization, which broke, and what the broken ones taught), see [`docs/formalization-index.md`](docs/formalization-index.md) and the companion Lean repo

## Formalization

See the dedicated section above and [`docs/formalization-index.md`](docs/formalization-index.md). Cashout classes are *certify*, *sharpen*, *expose looseness*, and *bridge artifact* — the index records which class each formalization falls into and whether the prose-to-formal mapping is currently paper-ready.

## License & Attribution

- Materials published on Zenodo are licensed CC BY 4.0, as indicated there.
- Other contents of this repository may have different licenses; see file headers where applicable.
- Unless otherwise stated, text in this repository is CC BY 4.0.
