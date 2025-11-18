"""
Responder's error handlers.
"""

# --- IMPORTS ---
from fastapi import Request
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from opty_api.app import app
from opty_api.err.already_exists_error import AlreadyExistsError
from opty_api.err.empty_update_error import EmptyUpdateError
from opty_api.err.mongodb_unavailable_error import MongoUnavailableError
from opty_api.err.not_found_error import NotFoundError
from opty_api.err.supabase_error import SupabaseError
from supabase_auth.errors import AuthApiError


# --- CODE ---
@app.exception_handler(AlreadyExistsError)
async def already_exists_error_handler(
    request: Request,  # pylint: disable=W0613
    error: AlreadyExistsError
) -> JSONResponse:
    """
    Handle AlreadyExistsError exceptions.

    :param request: http request.
    :param error: AlreadyExistsError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.args[1]}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = 409,
    )


@app.exception_handler(EmptyUpdateError)
async def empty_update_error_handler(
    request: Request,  # pylint: disable=W0613
    error: EmptyUpdateError
) -> JSONResponse:
    """
    Handle EmptyUpdateError exceptions.

    :param request: http request.
    :param error: EmptyUpdateError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.args[1]}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = 400,
    )


@app.exception_handler(AuthApiError)
async def auth_api_error_handler(
    request: Request,  # pylint: disable=W0613
    error: AuthApiError
) -> JSONResponse:
    """
    Handle AuthApiError exceptions.

    :param request: http request.
    :param error: AuthApiError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.message}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = error.status,
    )


@app.exception_handler(MongoUnavailableError)
async def database_unavailable_error_handler(
    request: Request,  # pylint: disable=W0613
    error: MongoUnavailableError
) -> JSONResponse:
    """
    Handle MongoUnavailableError exceptions.

    :param request: http request.
    :param error: MongoUnavailableError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.args[1]}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = 503,
    )


@app.exception_handler(NotFoundError)
async def not_found_error_handler(
    request: Request,  # pylint: disable=W0613
    error: NotFoundError
) -> JSONResponse:
    """
    Handle NotFoundError exceptions.

    :param request: http request.
    :param error: NotFoundError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.args[1]}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = 404,
    )


@app.exception_handler(SupabaseError)
async def supabase_error_handler(
    request: Request,  # pylint: disable=W0613
    error: SupabaseError
) -> JSONResponse:
    """
    Handle SupabaseError exceptions.

    :param request: http request.
    :param error: SupabaseError instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # log error
    print(f'[ERROR     ] {error.args[1]}')

    # fail request
    return JSONResponse(
        {'error': error.message},
        status_code = 500,
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    error: HTTPException
) -> JSONResponse:
    """
    Handle HTTPException exceptions.

    :param request: http request.
    :param error: HTTPException instance.

    :returns: JSONResponse with 'error' field describing the exception.
    """
    # get error parameters
    method = request.scope['method']
    path = request.scope['path']
    status = error.status_code
    detail = error.detail

    # log errors
    print(f'[ERROR     ] Request "{method} {path}" failed with {status}: {detail}')

    # fail request
    return JSONResponse(
        {'error': error.detail},
        status_code = error.status_code,
    )


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(
    request: Request,
    error: RequestValidationError
) -> JSONResponse:
    """
    Handle RequestValidationError exceptions.

    :param request: http request.
    :param error: exception instance.

    :returns: properly formatted JSONResponse
    """

    # Initialize list with all errors.
    errors = []

    # Get request body validation errors.
    for err in error.errors():

        # Get full error path.
        path = ' -> '.join(map(str, err['loc'][1:]))

        # Add error to errors list.
        errors.append(f'{path}: {err["msg"]}')

    # get error parameters
    method = request.scope['method']
    path = request.scope['path']
    status = 422
    detail = '\n'.join(errors)

    # log errors
    print(f'[ERROR     ] Validation request "{method} {path}" failed with status {status}: {detail}')

    # Return proper error message.
    return JSONResponse({'error': '\n'.join(errors)}, status_code = 422)
