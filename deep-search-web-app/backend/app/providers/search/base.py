# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Abstract base for pluggable web-search providers."""
from __future__ import annotations

import abc
from typing import List

from ...schemas.source import RawResult


class BaseSearchProvider(abc.ABC):
    name: str = "base"

    @abc.abstractmethod
    async def search(self, query: str, max_results: int) -> List[RawResult]:
        """Run a single web search and return normalised results."""
        raise NotImplementedError
