#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
# Start deep-search-agent-2-app. Extra args are passed to the app.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$ROOT"
if [ ! -d .venv ]; then echo "error: run ./setup.sh first" >&2; exit 1; fi
source .venv/bin/activate
if [ ! -f .env ]; then echo "warn: .env missing -- run ./setup.sh and set OPENAI_API_KEY" >&2; fi

# Postgres is optional (persistence only); start it if docker is available.
if command -v docker >/dev/null 2>&1 && grep -q "^DATABASE_URL=." .env 2>/dev/null; then
  docker compose up -d postgres || echo "warn: could not start postgres, continuing"
fi
echo ">> serving at http://localhost:8000"
exec uvicorn app.main:app --reload --port "${PORT:-8000}"
