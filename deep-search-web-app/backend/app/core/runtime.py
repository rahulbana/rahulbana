# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Process-level runtime info (version, uptime)."""
from __future__ import annotations

import time

APP_VERSION = "2.1.0"

_STARTED_AT = time.time()


def uptime_seconds() -> float:
    return time.time() - _STARTED_AT
