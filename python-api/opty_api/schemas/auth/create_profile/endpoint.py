"""
Create user profile endpoint schema (for OAuth users).
"""

# --- IMPORTS ---
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# --- TYPES ---
from typing import Optional


# --- CODE ---
class CreateProfilePayload(BaseModel):
    """
    Create profile request (for OAuth users).
    """
    supabase_id: str = Field(..., min_length=1)
    email: EmailStr
    name: str = Field(..., min_length=2)
    phone: Optional[str] = None
    birthday: Optional[str] = None
    avatar_url: Optional[str] = None
