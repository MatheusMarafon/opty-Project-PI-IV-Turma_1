"""
Supabase Error.
"""

# --- IMPORTS ---
from opty_api.err.opty_api_error import OptyApiError


# --- CODE ---
class SupabaseError(OptyApiError):
    """
    Supabase Error.
    """
    message = 'Supabase Error'
