# ---------------------------------------------------------------------------
# Name:     Rahul Singh Bana
# Email:    bana.saa@gmail.com
# LinkedIn: https://www.linkedin.com/in/rahulsinghbana
# Repo:     https://github.com/rahulbana/rahulbana
# ---------------------------------------------------------------------------
"""Data Validation reviewer."""

from .base import Reviewer


class DataValidationReviewer(Reviewer):
    """The Data Validation perspective."""

    key = "data_validation"
    title = "Data Validation"
    guidance = (
        "Check for: missing None checks; missing empty-string checks; "
        "missing input validation on external/user data; missing schema "
        "validation; where an Enum would be safer than magic strings; and "
        "missing dataclass/`__post_init__` validation."
    )
