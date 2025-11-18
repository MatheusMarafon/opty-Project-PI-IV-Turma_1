"""
JWT token schema.
"""

# --- TYPES ---
from typing import Optional
from typing import TypedDict


# --- CODE ---
class Token(TypedDict):
    """
    JWT token.
    """
    access_token: str
    token_type: str = 'bearer'
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None
