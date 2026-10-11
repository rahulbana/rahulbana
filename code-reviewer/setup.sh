#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Setup for code-reviewer: Python 3.12 venv, dependencies, .env.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PYTHON_BIN="${PYTHON_BIN:-python3.12}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "error: $PYTHON_BIN not found. Install Python 3.12 and re-run." >&2
  exit 1
fi

cd "$ROOT"
echo ">> creating virtual env (.venv) with $PYTHON_BIN"
"$PYTHON_BIN" -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .

if [ -f "$ROOT/.env.example" ] && [ ! -f "$ROOT/.env" ]; then
  cp "$ROOT/.env.example" "$ROOT/.env"
  echo ">> created $ROOT/.env from .env.example -- edit it and set OPENAI_API_KEY"
fi

echo ">> setup complete. Next: ./start.sh"
