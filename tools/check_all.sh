#!/usr/bin/env bash
# Run all five pre-push validators in sequence. Exit non-zero if any fails.
# Intended as a sanity check before pushing new/updated papers to Zenodo.
#
# Usage: tools/check_all.sh
#
# Each checker prints its own output; this script collects exit codes and
# prints a unified summary. Output is verbose — pipe to `tail -N` or use
# individual scripts for targeted runs.

set -u  # unset-variable check; no -e because we want to run all checks
here="$(dirname "$0")"
repo_root="$(cd "$here/.." && pwd)"
cd "$repo_root"

declare -A results
fail=0

run() {
  local name="$1"; shift
  echo
  echo "=== $name ==="
  if python3 "$@"; then
    results[$name]="ok"
  else
    results[$name]="FAIL"
    fail=$((fail + 1))
  fi
}

run zenodo_validate        tools/zenodo_validate.py
run metadata_schema        tools/metadata_schema.py
run pdf_freshness          tools/pdf_freshness.py
run citation_graph         tools/citation_graph.py
run doi_validate           tools/doi_validate.py
run formalization_crosswalk tools/formalization_crosswalk.py

echo
echo "=== summary ==="
for name in zenodo_validate metadata_schema pdf_freshness citation_graph doi_validate formalization_crosswalk; do
  status="${results[$name]:-skipped}"
  printf "  %-27s %s\n" "$name" "$status"
done

if [ "$fail" -ne 0 ]; then
  echo
  echo "$fail check(s) failed. Do not push until resolved." >&2
  exit 1
fi
echo
echo "All checks passed. Corpus is push-ready."
exit 0
