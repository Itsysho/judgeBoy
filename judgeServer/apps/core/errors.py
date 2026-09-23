from enum import Enum


class ErrorStatus(Enum):
    """Canonical error status strings, following Google API error codes.

    Each member maps a machine-readable status string to its HTTP status code.
    Reference: https://cloud.google.com/apis/design/errors#handling_errors
    """

    # (status_string, status_code)
    INVALID_ARGUMENT = ("INVALID_ARGUMENT", 400)
    UNAUTHENTICATED = ("UNAUTHENTICATED", 401)
    PERMISSION_DENIED = ("PERMISSION_DENIED", 403)
    NOT_FOUND = ("NOT_FOUND", 404)
    CONFLICT = ("CONFLICT", 409)
    FAILED_PRECONDITION = ("FAILED_PRECONDITION", 400)
    INTERNAL = ("INTERNAL", 500)

    def __init__(self, status: str, code: int) -> None:
        # each enum member carries both its string form and its HTTP code
        self.status = status
        self.http_code = code
