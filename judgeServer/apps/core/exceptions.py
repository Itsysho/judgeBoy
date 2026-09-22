from typing import Any

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response

from apps.core.errors import ErrorStatus

_CODE_TO_STATUS = {
    status.http_code: status for status in ErrorStatus}


def _resolve_status(http_code: int) -> ErrorStatus:
    if http_code == 400:
        return ErrorStatus.INVALID_ARGUMENT
    return _CODE_TO_STATUS.get(http_code, ErrorStatus.INTERNAL)


def _build_details(data: Any) -> list[dict[str, str]]:
    details: list[dict[str, str]] = []
    if isinstance(data, dict):
        for field, messages in data.items():
            if field == "detail":
                continue
            if isinstance(messages, list):
                for message in messages:
                    details.append({"field": field, "message": str(message)})
            else:
                details.append({"field": field, "message": str(messages)})
    return details


def custom_exception_handler(exc: Exception, context: dict) -> Response | None:
    response = drf_exception_handler(exc, context)

    if response is None:
        return None

    http_code = response.status_code
    error_status = _resolve_status(http_code)

    data = response.data

    if isinstance(data, dict) and "detail" in data:
        message = str(data["detail"])
        details = []
    else:
        message = "Request validation failed."
        details = _build_details(data)

    envelope: dict[str, Any] = {
        "error": {
            "code": http_code,
            "status": error_status.status,
            "message": message,
        }
    }
    if details:
        envelope["error"]["details"] = details

    response.data = envelope
    return response
