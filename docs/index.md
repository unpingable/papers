# Admissibility Research Corpus

*Δt framework · authority collapse · temporal mismatch · governed systems*

An independent research program on **admissibility**: when a system, model, observer, controller, or institution may lawfully treat a claim, observation, receipt, or memory as **usable authority for action**.

> **Monitoring asks what happened. Admissibility asks whether what happened may be *used*.**

The papers develop the theory in prose. A companion [Lean repo](https://github.com/unpingable/lean) audits selected claims by translating them into definitions and theorem statements and recording what survives. Some claims survive. Some narrow. Some break. **The breakage is kept on the record** — that is the methodology, not a disclaimer.

## What should I read first?

Route by what you care about — a full ramp is in **[Start Here](start-here.md)**.

- **Ops / control systems** → temporal coherence, capacity, fault domains: P01, P05, P09, P15, P22, P23.
- **AI governance / agent systems** → authority, durability, frame capture: P10, P11, P12, P17, P18, P19, P20.
- **Formalization / Lean** → the [Formalization Index](formalization-index.md) and the *Safety-Bridge Kernel* (admissibility suite).
- **Social platforms / institutions** → collapse and masking: P02, P04, P13, P24, P25.
- **Security / adversarial systems** → temporal structure exploited on purpose: P13, P14.
- **The current spine, not the archaeology** → the [Corpus Map](map.md) reads by concept, not date.

## The pages

| Page | What it answers |
|------|-----------------|
| **[Start Here](start-here.md)** | What is this, and where do I enter? |
| **[Corpus](corpus.md)** | Every paper — title, version, and whether it's published (DOI) or source-ahead. *(generated from metadata)* |
| **[Corpus Map](map.md)** | The conceptual order: threads, not chronology. |
| **[Methodology](methodology.md)** | How claims are made, audited, and retracted. |
| **[Formalization Index](formalization-index.md)** | Which prose claims were formalized, and what happened to them. |
| **[Falsification](method/falsification.md)** | Rival explanations, kill conditions, reclassification rules. |

## What is canonical, what is provisional

- **Canonical** — published PDFs with persistent DOIs on [Zenodo](https://zenodo.org/communities/delta-t-framework); the markdown source in this repo; the Lean register for selected formal claims.
- **Provisional** — working notes, scaffolds, drafts, and formalization gaps. A paper whose repo source is ahead of its published DOI is *source-ahead*, not yet re-minted.

## What has changed or broken

The Lean [`CLAIM-REGISTER.md`](https://github.com/unpingable/lean/blob/main/CLAIM-REGISTER.md) records every formally examined claim as **BROKEN / STALE / SOUND / OPEN / ADMITTED**. This is first-class trust machinery, not a footnote: displaying the failure is the discipline. See [Methodology](methodology.md) for what each status means and why retractions are kept.

## Two boundaries, two repos

- **Papers** — [`unpingable/papers`](https://github.com/unpingable/papers) — develops the theory. *(this repo)*
- **Lean** — [`unpingable/lean`](https://github.com/unpingable/lean) ([reading portal](https://unpingable.github.io/lean/)) — audits selected claims.

The vocabulary is also being forced against real operations in governed software systems (in development); those are downstream contact surfaces where the theory meets practice, not authority over it. **Site as map, repo as substrate, Zenodo as publication boundary, Lean as audit boundary.**

## What this is not

This is not a claim that Lean proves the whole theory true. Lean tests selected structural claims: whether they follow from explicit definitions, whether they need narrower conditions, or whether they were only useful as discovery slogans. It is a forcing function against theory-by-metaphor; it does not replace case studies, simulations, or operational evidence. It is not a manifesto, not credentialed academic work, and not an oracle — see [Methodology](methodology.md).
