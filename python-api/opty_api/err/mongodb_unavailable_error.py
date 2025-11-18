"""
MongoDB unavailable Error.
"""

# --- IMPORTS ---
from opty_api.err.opty_api_error import OptyApiError


# --- CODE ---
class MongoUnavailableError(OptyApiError):
    """
    MongoDB unavailable Error.
    """
    message = 'MongoDB Unavailable Error'
