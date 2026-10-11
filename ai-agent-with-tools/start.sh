#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Start ai-agent-with-tools. Extra args are passed to the app.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$ROOT"
if [ ! -d .venv ]; then echo "error: run ./setup.sh first" >&2; exit 1; fi
source .venv/bin/activate
if [ ! -f .env ]; then echo "warn: .env missing -- run ./setup.sh and set OPENAI_API_KEY" >&2; fi

exec python -m app "$@"
