# Plain-language summary

**Companion to:** *You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems* — version 1.0, preprint.

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

A language model can give an excellent answer now and still have no durable way to make that answer constrain what it says later. It can also preserve fluent wording while changing a definition, replace a challenged citation without weakening the claim, or repeat a corrected mistake in a new session. Ordinary performance scores do not directly test these failures.

The paper treats these as failures to preserve relationships over time, not just isolated factual errors. It proposes four things a coherent system should keep stable: earlier claims should constrain later ones; meanings should survive restatement and compression; sources should genuinely constrain the claims attached to them; and corrections should leave some persistent operational residue. Prompt-based demonstrations show how deployed model families can fail each test.

The architectural contribution is a checklist for consequential, long-running AI systems. Standard transformer inference does not itself provide persistent obligation-bearing state, an explicit state-evolution rule, or a cost for contradiction. External memory, retrieval, verification, recurrent state, and separate controllers may help, but the paper's point is that each must be tested against the invariants. A good answer in one turn is not the same capability as maintaining a commitment over time.

## Claim boundary

The reported tests are illustrative diagnostic demonstrations, not a statistically powered benchmark. They concern then-current transformer deployments and do not prove a limit on every possible transformer-derived or hybrid architecture. The four proposed invariants are presented as necessary requirements, but their independence, completeness, and empirical calibration remain open. The paper diagnoses a structural risk; it does not establish that every observed failure has one exclusive architectural cause.

## Read the paper

- [Manuscript source](attention_invariants_paper.md)
- [Rendered PDF](attention_invariants_paper.pdf)
- [Paper README](README.md)
- [DOI record](https://doi.org/10.5281/zenodo.18039926)
- [Zenodo record](https://zenodo.org/records/18039927)
