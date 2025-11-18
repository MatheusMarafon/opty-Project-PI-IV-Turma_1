"""
User registration endpoint schema.
"""

# --- IMPORTS ---
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# --- TYPES ---
from typing import Optional


# --- CODE ---
class UserRegisterPayload(BaseModel):
    """
    User registration request.
    """
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str = Field(..., min_length=2)
    phone: Optional[str] = None
    birthday: Optional[str] = None
