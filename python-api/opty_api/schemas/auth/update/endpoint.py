"""
User update endpoint schema.
"""

# --- IMPORTS ---
from pydantic import BaseModel


# --- TYPES ---
from typing import Optional


# --- CODE ---
class UserUpdatePayload(BaseModel):
    """
    User update request.
    """
    name: Optional[str] = None
    phone: Optional[str] = None
    birthday: Optional[str] = None
    avatar_url: Optional[str] = None
