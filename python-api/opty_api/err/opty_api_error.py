"""
Base Opty Api error.
"""

# --- TYPES ---
from typing import Any


# --- GLOBAL ---
DEFAULT_MESSAGE = 'Generic Opty Api error'


# --- ERROR CLASS ---
class OptyApiError(Exception):
    """
    Base Opty Api error.
    """
    message = DEFAULT_MESSAGE

    def __init__(self, *args: Any) -> None:
        """
        Initialize a Opty Api error.

        :param *args: Optional additional context or details for the error.

        :returns: None.
        """
        super().__init__(self.message, *args)
