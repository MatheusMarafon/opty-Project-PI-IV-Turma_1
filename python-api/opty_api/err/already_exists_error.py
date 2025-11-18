"""
Already exists Error.
"""

# --- IMPORTS ---
from opty_api.err.opty_api_error import OptyApiError


# --- CODE ---
class AlreadyExistsError(OptyApiError):
    """
    Already exists Error.
    """
    message = 'Already Exists Error'
