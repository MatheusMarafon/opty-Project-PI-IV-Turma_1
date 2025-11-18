"""
User schema definitions.
"""

# --- IMPORTS ---
from datetime import datetime


# --- TYPES ---
from typing import Literal
from typing import Optional
from typing import TypedDict


# --- CODE ---
class User(TypedDict, total=False):
    """
    User data stored in MongoDB.
    """
    supabase_id: str
    email: str
    name: str
    phone: Optional[str]
    birthday: Optional[str]
    avatar_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    is_active: bool
    role: Literal['user', 'supervisor']
