# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Readability reviewer."""

from .base import Reviewer


class ReadabilityReviewer(Reviewer):
    """The Readability perspective."""

    key = "readability"
    title = "Readability"
    guidance = (
        "Check: clear naming; reasonable function and class length; "
        "descriptive variable names; and boolean names that read as "
        "predicates (`is_`, `has_`, `should_`)."
    )
