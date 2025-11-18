"""
Empty Update Error.
"""

# --- IMPORTS ---
from opty_api.err.opty_api_error import OptyApiError


# --- CODE ---
class EmptyUpdateError(OptyApiError):
    """
    Empty Update Error.
    """
    message = 'Empty Update Error'
