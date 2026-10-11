# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Presentation rendering: themes and the python-pptx builder."""

from .builder import render_deck
from .themes import THEMES, Theme, get_theme

__all__ = ["render_deck", "THEMES", "Theme", "get_theme"]
