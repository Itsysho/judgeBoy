from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from apps.core.serializers import ErrorResponseSerializer


def _error_response(status_label: str, code: int, message: str) -> OpenApiResponse:
    # build a reusable OpenApiResponse with a realistic example
    return OpenApiResponse(
        response=ErrorResponseSerializer,
        examples=[
            OpenApiExample(
                status_label,
                value={
                    "error": {
                        "code": code,
                        "status": status_label,
                        "message": message,
                    }
                },
            )
        ],
    )


# pre-built, reusable error responses for common cases
VALIDATION_ERROR_RESPONSE = _error_response(
    "INVALID_ARGUMENT", 400, "Request validation failed."
)
UNAUTHENTICATED_RESPONSE = _error_response(
    "UNAUTHENTICATED", 401, "Authentication credentials were not provided."
)
PERMISSION_DENIED_RESPONSE = _error_response(
    "PERMISSION_DENIED", 403, "You do not have permission to perform this action."
)
NOT_FOUND_RESPONSE = _error_response(
    "NOT_FOUND", 404, "Not found."
)
CONFLICT_RESPONSE = _error_response(
    "CONFLICT", 409, "Conflict."
)
INTERNAL_RESPONSE = _error_response(
    "INVALID_ARGUMENT", 500, "Internal Server Error."
)
