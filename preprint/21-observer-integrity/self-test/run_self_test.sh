#!/usr/bin/env bash
set -euo pipefail

# Paper 21 Self-Test: Before/After Contamination Assay
# Runs 6 tasks through 3 models (claude, codex, gemini) cold and post-exposure
# Cross-model triangulation for perturbation class characterization

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EXPOSURE_FILE="$SCRIPT_DIR/exposure.txt"
OUTPUT_DIR="$SCRIPT_DIR/results"
MANIFEST="$OUTPUT_DIR/manifest.txt"

mkdir -p "$OUTPUT_DIR"/{cold,exposed}/{claude,codex,gemini}

EXPOSURE_TEXT=$(cat "$EXPOSURE_FILE")

# Task battery — 6 technical tasks, no theory vocabulary
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
    echo "=== Paper 21 Self-Test Manifest ==="
    echo "Date: $(date -Iseconds)"
    echo "Host: $(hostname)"
    echo ""
    echo "--- Tool Versions ---"
    echo "claude: $(claude --version 2>/dev/null || echo 'unknown')"
    echo "codex: $(codex --version 2>/dev/null || echo 'unknown')"
    echo "gemini: $(gemini --version 2>/dev/null || echo 'unknown')"
    echo ""
    echo "--- Tasks ---"
    for tid in "${TASK_IDS[@]}"; do
        echo "$tid: ${PROMPTS[$tid]:0:80}..."
    done
    echo ""
    echo "--- Exposure File ---"
    echo "$EXPOSURE_FILE ($(wc -c < "$EXPOSURE_FILE") bytes)"
    echo ""
    echo "--- Scoring Rubric ---"
    echo "For each cold/exposed pair, score 0-2 on:"
    echo "  MU: Metaphor uptake (theory vocabulary bleed)"
    echo "  CI: Caution inflation (hedge density increase)"
    echo "  PN: Performative neutrality (flattened/sterile tone)"
    echo "  MT: Meta-talk escalation (commentary about own stance)"
    echo ""
    echo "Verdict per model: continuous | regime-switch | unclear"
} > "$MANIFEST"

echo "=== Paper 21 Self-Test ==="
echo "$(date -Iseconds)"
echo "Manifest written to $MANIFEST"
echo ""

# Runner functions
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

# Phase 1: Cold runs
echo "--- Phase 1: Cold runs (no exposure) ---"
for tid in "${TASK_IDS[@]}"; do
    prompt="${PROMPTS[$tid]}"
    echo -n "  $tid: "

    run_claude "$prompt" "$OUTPUT_DIR/cold/claude/${tid}.txt" &
    PID_C=$!
    run_codex "$prompt" "$OUTPUT_DIR/cold/codex/${tid}.txt" &
    PID_X=$!
    run_gemini "$prompt" "$OUTPUT_DIR/cold/gemini/${tid}.txt" &
    PID_G=$!

    wait $PID_C $PID_X $PID_G 2>/dev/null || true
    echo "done"
done

echo ""
echo "--- Phase 2: Exposed runs (post-exposure) ---"

# Phase 2: Exposed runs
for tid in "${TASK_IDS[@]}"; do
    prompt="${PROMPTS[$tid]}"
    exposed_prompt="${EXPOSURE_TEXT}

---

Now respond to this task. Do not discuss the framework above unless the task requires it. Just answer the question.

${prompt}"

    echo -n "  $tid: "

    run_claude "$exposed_prompt" "$OUTPUT_DIR/exposed/claude/${tid}.txt" &
    PID_C=$!
    run_codex "$exposed_prompt" "$OUTPUT_DIR/exposed/codex/${tid}.txt" &
    PID_X=$!
    run_gemini "$exposed_prompt" "$OUTPUT_DIR/exposed/gemini/${tid}.txt" &
    PID_G=$!

    wait $PID_C $PID_X $PID_G 2>/dev/null || true
    echo "done"
done

echo ""
echo "=== Self-test complete ==="
echo "Results: $OUTPUT_DIR/"
echo ""
echo "To review, compare cold vs exposed for each model/task:"
echo "  diff $OUTPUT_DIR/cold/claude/T1.txt $OUTPUT_DIR/exposed/claude/T1.txt"
echo ""
echo "Score each pair on the 4 perturbation classes (0=none, 1=mild, 2=strong):"
echo "  MU (metaphor uptake), CI (caution inflation),"
echo "  PN (performative neutrality), MT (meta-talk escalation)"
