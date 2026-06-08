# Blind-Auditor Receipt — Gemini CLI

**Audited:** 2026-06-07
**Time spent:** approximate 30 minutes
**Mechanical aids used:** none

## Per-claim verdicts

### Claim A
- **Verdict:** DUPLICATE
- **Citations:** [PEP635-MOTIVATION-01], [PEP634-PATTERNS-01], [WHATSNEW-OPENING-01], [WHATSNEW-OTHER-01]
- **Reasoning:** The claim that pattern matching unifies sequence unpacking, `isinstance()` checking, and dict-key extraction under a declarative form is strongly supported. [PEP635-MOTIVATION-01] shows "Before" and "After" examples that demonstrate this unification. [PEP634-PATTERNS-01] lists explicit pattern types for sequences, mappings, and classes, directly corresponding to the claim's elements. [WHATSNEW-OPENING-01] and [WHATSNEW-OTHER-01] confirm the declarative approach and the ability to extract information from complex data types like dictionaries and sequences.
- **Uncertainty:** low
- **Revised during audit?:** no

### Claim B
- **Verdict:** DUPLICATE
- **Citations:** [PEP634-PATTERNS-01], [PEP635-VALUE-01], [PEP636-CONSTANTS-01], [WHATSNEW-OTHER-01], [LANGREF-CAPTURE-01], [LANGREF-VALUE-01]
- **Reasoning:** The corpus clearly delineates that capture patterns bind values ([PEP634-PATTERNS-01], [LANGREF-CAPTURE-01]) and value patterns compare them ([PEP634-PATTERNS-01], [LANGREF-VALUE-01]). The critical role of the dotted-name syntax to distinguish between value and capture patterns (e.g., `math.pi` vs `x`) and avoid ambiguity is explicitly stated across various altitudes ([PEP635-VALUE-01], [PEP636-CONSTANTS-01], [WHATSNEW-OTHER-01]). This disambiguator is load-bearing for correct interpretation, which impacts program correctness and safety.
- **Uncertainty:** low
- **Revised during audit?:** no

### Claim C
- **Verdict:** COUNTEREXAMPLE-CANDIDATE
- **Citations:** [LANGREF-GUARDS-01], [PEP635-GUARDS-01]
- **Reasoning:** The claim that PEP 634's first-to-match semantics "silently assume guards are side-effect-free" is directly refuted by the normative language reference. [LANGREF-GUARDS-01] explicitly states, "Guards are allowed to have side effects as they are expressions." While [PEP635-GUARDS-01] describes patterns as "ideally without any side-effects," it frames guards as enabling "dynamic evaluation," indicating they can indeed have side effects. The language reference further clarifies the deterministic evaluation order of guards, maintaining determinism even with side effects.
- **Uncertainty:** low
- **Revised during audit?:** no

### Claim D
- **Verdict:** LAUNDERING
- **Citations:** [WHATSNEW-OPENING-01], [PEP635-CAPTURE-01]
- **Reasoning:** The claim imports a framing that is explicitly rejected at a higher altitude (rationale) but endorsed at a lower altitude (changelog). [WHATSNEW-OPENING-01] introduces structural pattern matching by comparing it to the "switch statement found in C, Java or JavaScript." However, [PEP635-CAPTURE-01] (rationale) states that proposals for explicit capture markers were rejected based on a "misconception that pattern matching extends switch statements." This constitutes laundering, as a rejected framing from the design rationale appears in user-facing documentation.
- **Uncertainty:** low
- **Revised during audit?:** no

### Claim E
- **Verdict:** COUNTEREXAMPLE-CANDIDATE
- **Citations:** [PEP653-MOTIVATION-01], [PEP653-CONTROL-01], [PEP653-ROBUSTNESS-01], [PEP653-DIFF-01], [LANGREF-CLASS-01]
- **Reasoning:** The claim that PEP 634's class pattern semantics are "sufficient for production use" and "covers all observed class-matching needs" is directly contradicted by the existence and motivation of PEP 653. PEP 653 was introduced to address "undefined behavior" [PEP653-MOTIVATION-01] in PEP 634, provide "explicit, deterministic semantics for all matching scenarios" [PEP653-DIFF-01], and refine the handling of builtin classes [PEP653-CONTROL-01]. These subsequent efforts demonstrate that PEP 634's initial semantics were not deemed fully sufficient or robust for all production use cases.
- **Uncertainty:** low
- **Revised during audit?:** no

## Cross-cutting observations

- **Where operator judgment is doing hidden work:**
    - Interpreting "type safety" in Claim B as encompassing correct program behavior and avoiding ambiguity in a dynamically typed language, rather than strict static typing.
    - Assessing the "sufficiency for production use" in Claim E based on the post-hoc existence and explicit motivations of a follow-up PEP that addresses perceived shortcomings of the original.
- **Where mechanical aid would have helped:**
    - A Python interpreter could confirm the behavior of guards with side effects (Claim C) to concretely observe determinism.
    - A static analyzer or linter could be used to demonstrate how ambiguities arise if the dotted-name convention for value patterns (Claim B) is not followed, reinforcing its "load-bearing" nature.
- **Was the verdict palette sufficient?:** Yes. The provided verdict palette was comprehensive and allowed for accurate classification of all claims, including nuances like "LAUNDERING" and "COUNTEREXAMPLE-CANDIDATE" which rely on cross-altitude analysis.
- **Any label-failures:** None.

## Overall

- **Method discrimination assessment:** Retains discrimination. The cross-altitude audit method effectively highlighted how claims that appear consistent at one altitude (e.g., user-facing docs) can be contradicted or framed as a misconception at another (e.g., rationale or follow-up specification), as seen in the LAUNDERING and COUNTEREXAMPLE-CANDIDATE verdicts.
- **Caveats and limitations:** The audit is limited to the provided corpus excerpts. A broader review of the full source documents might reveal additional context, but the selected excerpts were sufficiently targeted to the claims. The interpretation of some terms used in the claims (e.g., "type safety," "semantic fracture") required contextual judgment based on Python's design philosophy.
- **Notes the packet preparer should know:** The claims were well-designed to test the cross-altitude aspect of the audit, particularly through the interplay between motivations/rationales, normative specifications, and user-facing documentation/follow-up PEPs.
