# Blind-Auditor Packet — Cross-Altitude Novelty Audit

**Packet prepared:** 2026-06-07.
**Packet sealed for blind audit.** Once received by an auditor, no further communication about the audit's *expected verdicts* is permitted until the auditor returns a completed receipt.

This packet contains everything an external auditor needs to perform a Cross-Altitude Novelty Audit on the supplied corpus and claims. It contains NO prior verdicts, NO worked examples from prior audits, NO method-history, and NO expected answers. The packet preparer has performed a separate audit on the same corpus and claims; those results are held outside this packet and will be compared against the blind auditor's receipt only after that receipt is delivered.

## What you are being asked to do

You are auditing five proposed claims against a frozen corpus of eight documents. For each claim, decide whether the corpus supports the claim, refutes it, contains the proposal under different vocabulary, exhibits a hidden lexical fracture, or fits another category from the verdict palette below. Cite specific corpus locations for every verdict. Be explicit about uncertainty.

The corpus has no typechecker, no theorem prover, no executable test suite invoked. The audit operates at the prose / grammar-spec altitude only. You may use a Python interpreter or static analyzer to sharpen verdicts if you want; if you do, mark explicitly where mechanical aid was used.

You may revise verdicts on re-read. Mark any verdict that changed during your audit and explain why.

## Audit method (terse)

The Cross-Altitude Novelty Audit tests whether a proposed claim about a feature, design, or specification:

1. Already exists in the corpus at some altitude (DUPLICATE)
2. Collides with the corpus's own internal disambiguation of similar concepts (ALIAS-RISK)
3. Is explicitly refused by some altitude of the corpus itself (INTERNAL-REFUTATION GAP)
4. Imports framing one altitude of the corpus rejects, smoothing it over from another altitude (LAUNDERING)
5. Silently assumes a precondition another corpus artifact formalizes (MISSING-PRECONDITION)
6. Sits in a real gap the corpus knows about but does not authorize the claim's filling (GAP CONFIRMED + RELAY-FRAMING REFUSED)
7. Would compose two valid artifacts into a third the corpus does not endorse (COMPOSITION-GAP)
8. Is a candidate cross-altitude bridge (BRIDGE-CANDIDATE)
9. May contradict an existing claim (COUNTEREXAMPLE-CANDIDATE)
10. Has no real connection (DEAD-END)

The audit's discriminator is *cross-altitude*: a claim that looks novel at one altitude may be old or refused at another. Read across the manifest's altitudes before settling on a verdict.

## Verdict palette (definitions; use these exact labels)

| Label | Definition (use this scope; do not extend) |
|---|---|
| **DUPLICATE** | The proposed claim already exists in the corpus under different vocabulary or at a different altitude. Cite the corpus location that contains the claim. |
| **ALIAS-RISK** | A single word, phrase, or concept in the claim carries multiple distinct relations across the corpus; the claim collapses them. Cite each sense the corpus uses and the location for each. |
| **LAUNDERING** | The claim imports a framing or mental-model the corpus's decision-record altitude (rationale / proposal / design-doc) explicitly rejects; another altitude (changelog / release-notes / tutorial) carries the rejected framing as if it were endorsed. Cite the rejection and the import. |
| **INTERNAL-REFUTATION GAP** | A real gap or open question exists; the corpus itself contains the refusal of the tempting framing the claim proposes. The audit's role is to record that the refusal exists at a specific altitude. Cite the refusal. |
| **MISSING-PRECONDITION** | One corpus artifact silently assumes a condition another corpus artifact formalizes, but the dependency is not surfaced. The claim names the condition without naming the corpus dependency. Cite both artifacts. |
| **GAP CONFIRMED + RELAY-FRAMING REFUSED** | A real corpus gap exists; the claim proposes a framing the corpus is structurally not authorized to accept. Cite the gap and the structural refusal. |
| **BRIDGE-CANDIDATE** | The claim names a possible cross-altitude bridge that does not yet exist in the corpus. Bridges incur a tax: source surface, target surface, witness, licensed claim, residual scope. Cite the prospective endpoints and any obvious cost. |
| **COMPOSITION-GAP** | Two corpus artifacts are individually valid but their composition produces a result the corpus does not endorse. Cite the components and the failed composition. |
| **COUNTEREXAMPLE-CANDIDATE** | The claim contradicts an existing corpus claim under specific conditions. Cite the contradiction. |
| **DEAD-END** | No real connection; the claim is a false positive. Brief justification only. |

Multi-class verdicts (e.g., "ALIAS-RISK + INTERNAL-REFUTATION GAP") are permitted when the claim genuinely exhibits more than one class. State each class and its citation separately.

If none of the existing labels fits, record the claim as **LABEL-FAILURE** with a brief explanation of why no label applied. Do not invent new labels.

## Frozen corpus manifest

Eight documents, six altitude classes, no formal proof layer.

| # | Document | URL | Altitude |
|---|---|---|---|
| 1 | PEP 634 — Structural Pattern Matching: Specification | https://peps.python.org/pep-0634/ | normative spec / proposal |
| 2 | PEP 635 — Structural Pattern Matching: Motivation and Rationale | https://peps.python.org/pep-0635/ | argument / rationale |
| 3 | PEP 636 — Structural Pattern Matching: Tutorial | https://peps.python.org/pep-0636/ | tutorial / user-facing docs |
| 4 | Python 3.10 What's New — Structural Pattern Matching section | https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching | changelog / release residue |
| 5 | Python Language Reference — The `match` statement | https://docs.python.org/3/reference/compound_stmts.html#the-match-statement | normative reference |
| 6 | CPython implementation tracking | https://github.com/python/cpython/issues/86294 | implementation tracking |
| 7 | CPython implementation PR | https://github.com/python/cpython/pull/22917 | implementation decision |
| 8 | PEP 653 — Precise Semantics for Pattern Matching | https://peps.python.org/pep-0653/ | post-acceptance regret / re-specification |

Documents 1–5 and 8 are accessible via the URLs above. Documents 6 and 7 (GitHub issue / PR) require GitHub access; cite by URL anchors if needed.

The corpus is frozen as of 2026-06-07. Do not include other Python documentation, blog posts, or related PEPs in your audit. If you cite material outside the manifest, mark it as out-of-manifest and treat that citation as secondary evidence.

## Claims to audit

Five claims. Audit each independently. Do not let your verdict on one claim prejudice your verdict on another.

**Claim A.** *"Structural pattern matching in Python 3.10 unifies sequence unpacking, `isinstance()` checking, and dict-key extraction under a single declarative form, replacing the historical fragmentation of these idioms."*

**Claim B.** *"The match statement exhibits a binding-vs-comparison semantic fracture: capture patterns bind, value patterns compare, and the syntactic disambiguator (dotted vs bare names) is load-bearing for type safety."*

**Claim C.** *"PEP 634's first-to-match semantics silently assume guards are side-effect-free; without this assumption, the first-to-match guarantee provides no meaningful determinism over the program state observed in case bodies."*

**Claim D.** *"Pattern matching extends the switch statement found in C/Java/JavaScript to support structural decomposition of subject values; the case-clause discipline is the same in spirit, with the addition of binding semantics."*

**Claim E.** *"PEP 634's class pattern semantics are sufficient for production use because `isinstance()` plus `__match_args__` covers all observed class-matching needs, with `collections.abc` providing the sequence/mapping classification."*

## Required receipt format

Return a single markdown document with the following structure. Do not depart from this structure.

```markdown
# Blind-Auditor Receipt — [your auditor identifier]

**Audited:** [date]
**Time spent:** [approximate]
**Mechanical aids used:** [list any: Python interpreter, mypy, etc., or "none"]

## Per-claim verdicts

### Claim A
- **Verdict:** [single label or multi-class]
- **Citations:** [list specific corpus locations: which document, which section / quote]
- **Reasoning:** [2–6 sentences explaining why this verdict, not another]
- **Uncertainty:** [low / medium / high; note what would change the verdict]
- **Revised during audit?:** [yes/no; if yes, briefly: from what to what, why]

### Claim B
[same structure]

### Claim C
[same structure]

### Claim D
[same structure]

### Claim E
[same structure]

## Cross-cutting observations

- **Where operator judgment is doing hidden work:** [enumerate places your audit relied on judgment that a mechanical layer could have decided]
- **Where mechanical aid would have helped:** [enumerate]
- **Was the verdict palette sufficient?:** [yes / no / explain]
- **Any label-failures:** [if any claim required LABEL-FAILURE, explain here]

## Overall

- **Method discrimination assessment:** [retains discrimination / degrades gracefully / collapses into vibes — pick one and briefly justify]
- **Caveats and limitations:** [list]
- **Notes the packet preparer should know:** [optional; anything about packet quality, claim phrasing, label definition ambiguity]
```

Return only this receipt. Do not include external commentary outside the receipt. Do not request the packet preparer's verdicts before delivering your own.

## Audit instructions (one paragraph, important)

Read the corpus manifest fully before forming any verdict. For each claim, scan all eight documents for relevant material; identify which altitude each piece of relevant material occupies; check whether the claim's framing is consistent with all altitudes or whether it collides with one altitude while matching another. Cite from each document by section name or short quoted phrase. If a claim seems to fit two labels, state both with separate citations. If a claim seems to fit no label, mark it LABEL-FAILURE rather than inventing a new label. Verdict stability is itself an audit signal: if your verdict on a claim changes between first pass and second pass, record the change and the reason.

## Packet-quality notes (for the auditor's information)

- Documents 1, 2, 3, and 8 are PEP texts authored by named individuals (Brandt Bucher, Tobias Kohn, Guido van Rossum, Mark Shannon). Treat the rationale (PEP 635) as the design-decision-record altitude.
- Document 4 (What's New) is authored by the Python documentation team; treat as user-facing simplification.
- Document 5 (Language Reference) is the post-implementation normative anchor; it may diverge from the original PEP.
- Documents 6 and 7 (CPython issue and PR) are implementation-altitude artifacts; treat as decision records for *what shipped*, not necessarily *what the PEP specified.*
- Document 8 (PEP 653) is a follow-up PEP that exists, regardless of its acceptance status; its existence is itself evidence about Document 1.

## What this packet does NOT contain

- The packet preparer's verdicts on these claims.
- Examples of verdicts from prior audits in any corpus.
- Hints about which verdicts are common or rare for this method.
- The expected verdict distribution.
- Method history, internal context, or doctrine about which the audit is being run.

If you are unsure about a verdict, your honest uncertainty marker is the right output. Do not guess in either direction.

---

**End of packet. Audit and return receipt. Do not request expected verdicts.**
