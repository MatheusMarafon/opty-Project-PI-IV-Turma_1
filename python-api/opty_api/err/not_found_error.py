"""
Not found Error.
"""

# --- IMPORTS ---
from opty_api.err.opty_api_error import OptyApiError


# --- CODE ---
class NotFoundError(OptyApiError):
    """
    Not found Error.
    """
    message = 'Not Found Error'
