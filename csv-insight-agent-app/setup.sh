#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Setup for csv-insight-agent-app: Python 3.12 venv, dependencies, .env.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PYTHON_BIN="${PYTHON_BIN:-python3.12}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "error: $PYTHON_BIN not found. Install Python 3.12 and re-run." >&2
  exit 1
fi

cd "$ROOT/backend"
echo ">> creating backend virtual env (backend/.venv) with $PYTHON_BIN"
"$PYTHON_BIN" -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

if [ -f "$ROOT/backend/.env.example" ] && [ ! -f "$ROOT/backend/.env" ]; then
  cp "$ROOT/backend/.env.example" "$ROOT/backend/.env"
  echo ">> created $ROOT/backend/.env from .env.example -- edit it and set OPENAI_API_KEY"
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "error: npm not found. Install Node.js and re-run." >&2
  exit 1
fi
echo ">> installing frontend dependencies"
cd "$ROOT/frontend"
npm install
if [ -f "$ROOT/frontend/.env.example" ] && [ ! -f "$ROOT/frontend/.env" ]; then
  cp "$ROOT/frontend/.env.example" "$ROOT/frontend/.env"
  echo ">> created $ROOT/frontend/.env from .env.example -- edit it if needed"
fi

echo ">> setup complete. Next: ./start.sh"
