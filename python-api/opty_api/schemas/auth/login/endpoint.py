"""
User login schema.
"""

# --- IMPORTS ---
from pydantic import BaseModel
from pydantic import EmailStr


# --- TYPES ---
from opty_api.schemas.token import Token
from opty_api.schemas.user import User


# --- CODE ---
class UserLoginPayload(BaseModel):
    """
    User login request payload.
    """
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    """
    User login request response.
    """
    token: Token
    user: User
