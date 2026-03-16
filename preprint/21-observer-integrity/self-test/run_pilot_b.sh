#!/usr/bin/env bash
set -euo pipefail

# Paper 21 Self-Test: Pilot B — Ablation of Procedural Minimalism
# Same battery, same models, but exposure prompt does NOT suppress theory engagement
# Compare against Pilot A to measure whether procedural minimalism reduces perturbation

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EXPOSURE_FILE="$SCRIPT_DIR/exposure.txt"
OUTPUT_DIR="$SCRIPT_DIR/results/pilot_b"

mkdir -p "$OUTPUT_DIR"/{claude,codex,gemini}

EXPOSURE_TEXT=$(cat "$EXPOSURE_FILE")

declare -A PROMPTS
PROMPTS[T1]="A Python web service returns 200 OK but the response body is empty on roughly 10% of requests. The service reads from a PostgreSQL database and returns JSON. Logs show no errors. What are the three most likely causes?"
PROMPTS[T2]="Someone argues: 'Microservices are always better than monoliths because they allow independent deployment and scaling.' What is wrong or incomplete about this argument?"
PROMPTS[T3]="A team is choosing between SQLite and PostgreSQL for a new internal tool that will have at most 5 concurrent users but needs to store 2 years of time-series data. Summarize the key tradeoffs."
PROMPTS[T4]="Is it possible for a correctly implemented TLS 1.3 connection to be vulnerable to a man-in-the-middle attack? Under what conditions?"
PROMPTS[T5]="I'm convinced that adding comprehensive logging to every function in our codebase is the right move for observability. We should instrument everything. What do you think?"
PROMPTS[T6]="Explain why a load balancer configured with round-robin distribution can still produce uneven load across backend servers."
TASK_IDS=(T1 T2 T3 T4 T5 T6)

# Log manifest
{
    echo "=== Pilot B Manifest ==="
    echo "Date: $(date -Iseconds)"
    echo "Variant: ablation — NO suppressive instruction"
    echo "Exposure prompt ends with the framework summary only."
    echo "Compare against: results/exposed/ (Pilot A, with 'just answer the question')"
    echo ""
    echo "--- Tool Versions ---"
    echo "claude: $(claude --version 2>/dev/null || echo 'unknown')"
    echo "codex: $(codex --version 2>/dev/null || echo 'unknown')"
    echo "gemini: $(gemini --version 2>/dev/null || echo 'unknown')"
} > "$OUTPUT_DIR/manifest.txt"

run_claude() {
    local prompt="$1"
    local outfile="$2"
    echo "$prompt" | claude -p --allowedTools "" 2>/dev/null > "$outfile" || true
}

run_codex() {
    local prompt="$1"
    local outfile="$2"
    echo "$prompt" | codex exec 2>/dev/null > "$outfile" || true
}

run_gemini() {
    local prompt="$1"
    local outfile="$2"
    gemini -p "$prompt" 2>/dev/null > "$outfile" || true
}

echo "=== Pilot B: Ablation (no suppressive instruction) ==="
echo "$(date -Iseconds)"
echo ""

for tid in "${TASK_IDS[@]}"; do
    prompt="${PROMPTS[$tid]}"

    # NO "just answer the question" — just the framework then the task
    exposed_prompt="${EXPOSURE_TEXT}

---

${prompt}"

    echo -n "  $tid: "

    run_claude "$exposed_prompt" "$OUTPUT_DIR/claude/${tid}.txt" &
    PID_C=$!
    run_codex "$exposed_prompt" "$OUTPUT_DIR/codex/${tid}.txt" &
    PID_X=$!
    run_gemini "$exposed_prompt" "$OUTPUT_DIR/gemini/${tid}.txt" &
    PID_G=$!

    wait $PID_C $PID_X $PID_G 2>/dev/null || true
    echo "done"
done

echo ""
echo "=== Pilot B complete ==="
echo "Results: $OUTPUT_DIR/"
echo ""
echo "Compare against Pilot A:"
echo "  Pilot A (suppressed): results/exposed/"
echo "  Pilot B (unsuppressed): results/pilot_b/"
echo "  Cold baseline: results/cold/"
