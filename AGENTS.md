# Repository instructions

## Portable names and paths

- Do not introduce the internal workspace name `skunkworks` into committed
  prose, metadata, examples, or comments. Describe it as the **development
  environment**, **private development environment**, or **archived development
  workspace**, whichever is accurate.
- Do not introduce machine-local Lean paths such as `~/git/lean` or
  `/home/<user>/git/lean`. In prose, say **the companion Lean repository** and
  cite a repository-relative path such as `LeanProofs/Admissibility/Authority.lean`.
  When readers need a navigable cross-repository reference, use the public
  `https://github.com/unpingable/lean` URL or a `blob/main/...` link.
- Code must not hard-code a user's home-directory layout. Cross-repository tools
  should accept a configurable repository path and may use a portable sibling
  repository fallback when appropriate.
- When substantively editing a file that already contains an internal workspace
  name or machine-local path, normalize the occurrences in the touched material.
  Do not silently rewrite exact historical quotations or immutable publication
  artifacts; label those as historical when they must be retained.
- Before finishing a documentation or metadata change, search the changed files
  for the forbidden workspace name, `~/git/lean`, and absolute home-directory
  Lean paths. This instruction file is the expected exception because it defines
  the rule.
