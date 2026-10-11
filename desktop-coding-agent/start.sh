#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Start desktop-coding-agent.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$ROOT/backend/.venv" ]; then echo "error: run ./setup.sh first" >&2; exit 1; fi
if [ ! -f "$ROOT/backend/.env" ]; then echo "warn: backend/.env missing -- run ./setup.sh and set OPENAI_API_KEY" >&2; fi

cd "$ROOT/frontend"
PYTHON="$ROOT/backend/.venv/bin/python" npm run dev
