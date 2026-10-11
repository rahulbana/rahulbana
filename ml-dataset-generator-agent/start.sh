#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Start ml-dataset-generator-agent. Extra args are passed to the app.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$ROOT"
if [ ! -d .venv ]; then echo "error: run ./setup.sh first" >&2; exit 1; fi
source .venv/bin/activate
if [ ! -f .env ]; then echo "warn: .env missing -- run ./setup.sh and set OPENAI_API_KEY" >&2; fi

# With arguments: run the CLI. Without: start the API on :8000.
if [ "$#" -gt 0 ]; then
  exec python -m app.cli "$@"
fi
exec uvicorn app.api.main:app --reload --port "${PORT:-8000}"
