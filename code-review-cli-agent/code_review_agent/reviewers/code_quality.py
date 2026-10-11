# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Code Quality reviewer."""

from .base import Reviewer


class CodeQualityReviewer(Reviewer):
    """The Code Quality perspective."""

    key = "code_quality"
    title = "Code Quality"
    guidance = (
        "Check for: duplicate code; overly long methods; overly long "
        "classes; dead code; unused variables; unused methods; deep "
        "nesting; high cyclomatic complexity; and general code smells."
    )
