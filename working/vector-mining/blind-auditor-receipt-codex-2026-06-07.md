# Blind-Auditor Receipt — Codex

**Audited:** 2026-06-08
**Time spent:** ~45 minutes
**Mechanical aids used:** none

## Per-claim verdicts

### Claim A
- **Verdict:** DUPLICATE
- **Citations:** [PEP635-MOTIVATION-01], [PEP634-PATTERNS-01], [WHATSNEW-OPENING-01], [WHATSNEW-OTHER-01]
- **Reasoning:** The claim is already present at rationale, specification, and changelog altitudes. PEP 635 explicitly motivates pattern matching as replacing idioms involving `isinstance()`, tuple shape checks, unpacking, and AST deconstruction. PEP 634 enumerates sequence, mapping, and class patterns, and What's New describes extraction from complex data types and branching on structure. The phrase “historical fragmentation” is the claim’s vocabulary, but the underlying unification claim is already in the corpus.
- **Uncertainty:** low; only a stronger claim that pattern matching fully replaces all such idioms would exceed the cited material.
- **Revised during audit?:** no

### Claim B
- **Verdict:** DUPLICATE + ALIAS-RISK
- **Citations:** [PEP635-CAPTURE-01], [PEP635-VALUE-01], [LANGREF-CAPTURE-01], [LANGREF-VALUE-01], [PEP636-CONSTANTS-01], [WHATSNEW-OTHER-01]
- **Reasoning:** The binding-vs-comparison fracture is directly described: capture patterns bind bare names, while value patterns use dotted names and compare by equality. The dotted-name rule is repeatedly presented as the syntactic disambiguator preventing constants from being treated as capture variables. It is also an ALIAS-RISK because “name” carries distinct roles across the corpus: a bare `NAME` captures, while a dotted name is looked up and compared. “Type safety” is not quite the corpus’s term; the corpus frames the issue as semantic disambiguation and avoiding ambiguity.
- **Uncertainty:** medium; if “type safety” is read strictly as static type soundness, the corpus does not establish that part.
- **Revised during audit?:** no

### Claim C
- **Verdict:** COUNTEREXAMPLE-CANDIDATE + INTERNAL-REFUTATION GAP
- **Citations:** [PEP635-GUARDS-01], [LANGREF-GUARDS-01], [LANGREF-OVERVIEW-01], [WHATSNEW-GUARD-01]
- **Reasoning:** The claim contradicts the normative reference: guards are explicitly allowed to have side effects, are evaluated in order, and evaluation stops once a case block is selected. That provides deterministic guard-order semantics even without side-effect freedom, though not purity of observed program state. The tempting pure/declarative framing exists in PEP 635, but the language reference refuses to require it for guards.
- **Uncertainty:** medium; the claim could be salvaged if “meaningful determinism” were narrowed to purity of case-body observations rather than execution order.
- **Revised during audit?:** yes; initially appeared to be a missing precondition, revised to counterexample/internal-refutation after reading the language reference’s explicit permission for side-effecting guards.

### Claim D
- **Verdict:** LAUNDERING
- **Citations:** [WHATSNEW-OPENING-01], [PEP635-CAPTURE-01]
- **Reasoning:** The changelog altitude introduces structural pattern matching through comparison with switch statements in C, Java, or JavaScript. But the rationale explicitly rejects the misconception that pattern matching extends switch statements, in the context of refusing explicit capture markers. The claim imports the changelog’s explanatory framing as if it were endorsed by the design rationale, so it launders a user-facing analogy into a design claim.
- **Uncertainty:** low; the exact “same in spirit” wording is broader than the corpus, but the rejected switch-extension framing is directly cited.
- **Revised during audit?:** no

### Claim E
- **Verdict:** INTERNAL-REFUTATION GAP + COMPOSITION-GAP
- **Citations:** [PEP635-CLASS-01], [LANGREF-CLASS-01], [PEP653-CONTROL-01], [PEP653-ROBUSTNESS-01], [PEP653-DIFF-01]
- **Reasoning:** The claim composes valid PEP 634-era mechanisms: `isinstance()`, `__match_args__`, built-in class handling, and `collections.abc` sequence/mapping classification. But PEP 653 directly critiques those semantics, noting privileged built-in “self” matching, delegation to `collections.abc`, attribute-access side-effect concerns, and proposed deterministic replacements. The corpus therefore contains an internal refusal of the sufficiency claim: the components exist, but their composition is not endorsed as covering all production needs.
- **Uncertainty:** low; “all observed class-matching needs” is stronger than any supporting excerpt and is undercut by PEP 653.
- **Revised during audit?:** no

## Cross-cutting observations

- **Where operator judgment is doing hidden work:** Interpreting “type safety” in Claim B as semantic disambiguation rather than formal static typing; deciding that Claim C’s “meaningful determinism” overstates the effect of side effects; distinguishing tutorial/changelog analogy from rationale-level endorsement in Claim D.
- **Where mechanical aid would have helped:** A formal grammar query could confirm capture/value syntax; an executable probe could illustrate guard side effects and binding behavior; a fuller corpus search could check whether “production use” appears outside the provided excerpts.
- **Was the verdict palette sufficient?:** yes
- **Any label-failures:** none

## Overall

- **Method discrimination assessment:** retains discrimination; the packet separates rationale, normative reference, changelog, implementation, and follow-up critique well enough to distinguish duplication from laundering and internal refusal.
- **Caveats and limitations:** The audit uses only in-bundle excerpts. No external verification was performed. Some verdicts depend on interpreting broad phrases such as “type safety,” “production use,” and “meaningful determinism.”
- **Notes the packet preparer should know:** Claim C is the least stable because the corpus both idealizes pure declarative patterns and normatively permits side-effecting guards.
