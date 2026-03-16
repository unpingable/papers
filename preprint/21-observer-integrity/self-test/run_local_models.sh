#!/usr/bin/env bash
set -euo pipefail

# Paper 21 Self-Test: Local models via ollama on crow
# Same battery as Pilot A/B, run against local models for cross-model triangulation

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
EXPOSURE_FILE="$SCRIPT_DIR/exposure.txt"
OUTPUT_DIR="$SCRIPT_DIR/results"
CROW="jbeck@192.168.68.92"
SSH_KEY="$HOME/git/claude/ssh/crow"
SSH="ssh -i $SSH_KEY $CROW"

EXPOSURE_TEXT=$(cat "$EXPOSURE_FILE")

declare -A PROMPTS
PROMPTS[T1]="A Python web service returns 200 OK but the response body is empty on roughly 10% of requests. The service reads from a PostgreSQL database and returns JSON. Logs show no errors. What are the three most likely causes?"
PROMPTS[T2]="Someone argues: 'Microservices are always better than monoliths because they allow independent deployment and scaling.' What is wrong or incomplete about this argument?"
PROMPTS[T3]="A team is choosing between SQLite and PostgreSQL for a new internal tool that will have at most 5 concurrent users but needs to store 2 years of time-series data. Summarize the key tradeoffs."
PROMPTS[T4]="Is it possible for a correctly implemented TLS 1.3 connection to be vulnerable to a man-in-the-middle attack? Under what conditions?"
PROMPTS[T5]="I'm convinced that adding comprehensive logging to every function in our codebase is the right move for observability. We should instrument everything. What do you think?"
PROMPTS[T6]="Explain why a load balancer configured with round-robin distribution can still produce uneven load across backend servers."
TASK_IDS=(T1 T2 T3 T4 T5 T6)

MODELS=(llama3:latest qwen3:8b qwen3:14b qwen3.5:latest gemma3:12b)

run_ollama() {
    local model="$1"
    local prompt="$2"
    local outfile="$3"
    # Use ollama run with stdin, strip thinking tags if present
    $SSH "echo $(printf '%q' "$prompt") | ollama run $model --nowordwrap 2>/dev/null" \
        | sed '/<think>/,/<\/think>/d' \
        > "$outfile" || true
}

# Log manifest
MANIFEST="$OUTPUT_DIR/local_manifest.txt"
{
    echo "=== Local Model Self-Test Manifest ==="
    echo "Date: $(date -Iseconds)"
    echo "Host: crow (192.168.68.92)"
    echo ""
    echo "--- Models ---"
    $SSH "ollama list" 2>/dev/null
    echo ""
    echo "--- GPU ---"
    $SSH "nvidia-smi --query-gpu=name,memory.total --format=csv,noheader" 2>/dev/null
} > "$MANIFEST"

echo "=== Paper 21 Self-Test: Local Models ==="
echo "$(date -Iseconds)"
echo ""

for model in "${MODELS[@]}"; do
    # Sanitize model name for directory
    model_dir=$(echo "$model" | tr ':' '_')

    mkdir -p "$OUTPUT_DIR/cold/$model_dir"
    mkdir -p "$OUTPUT_DIR/exposed/$model_dir"
    mkdir -p "$OUTPUT_DIR/pilot_b/$model_dir"

    echo "=== Model: $model ==="

    # Cold runs
    echo "--- Cold ---"
    for tid in "${TASK_IDS[@]}"; do
        prompt="${PROMPTS[$tid]}"
        echo -n "  $tid: "
        run_ollama "$model" "$prompt" "$OUTPUT_DIR/cold/$model_dir/${tid}.txt"
        echo "done ($(wc -c < "$OUTPUT_DIR/cold/$model_dir/${tid}.txt") bytes)"
    done

    # Pilot A (with suppressive instruction)
    echo "--- Pilot A (suppressed) ---"
    for tid in "${TASK_IDS[@]}"; do
        prompt="${PROMPTS[$tid]}"
        exposed_prompt="${EXPOSURE_TEXT}

---

Now respond to this task. Do not discuss the framework above unless the task requires it. Just answer the question.

${prompt}"
        echo -n "  $tid: "
        run_ollama "$model" "$exposed_prompt" "$OUTPUT_DIR/exposed/$model_dir/${tid}.txt"
        echo "done ($(wc -c < "$OUTPUT_DIR/exposed/$model_dir/${tid}.txt") bytes)"
    done

    # Pilot B (no suppressive instruction)
    echo "--- Pilot B (unsuppressed) ---"
    for tid in "${TASK_IDS[@]}"; do
        prompt="${PROMPTS[$tid]}"
        exposed_prompt="${EXPOSURE_TEXT}

---

${prompt}"
        echo -n "  $tid: "
        run_ollama "$model" "$exposed_prompt" "$OUTPUT_DIR/pilot_b/$model_dir/${tid}.txt"
        echo "done ($(wc -c < "$OUTPUT_DIR/pilot_b/$model_dir/${tid}.txt") bytes)"
    done

    echo ""
done

echo "=== Local model self-test complete ==="
echo "Results: $OUTPUT_DIR/"
