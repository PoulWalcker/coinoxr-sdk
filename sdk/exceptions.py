class SDKError(Exception):
    """Base SDK error."""


# Client-side
class ValidationError(SDKError):
    """Bad params or local validation failed."""


class NetworkError(SDKError):
    """Transport-level (timeouts, DNS, connection issues)."""


# API-side
class APIError(SDKError):
    """Base API error from OXR."""

    def __init__(
        self,
        status: int,
        code: str | None = None,
        message: str | None = None,
        *,
        endpoint: str | None = None,
        payload: dict | None = None,
    ):
        super().__init__(message or f"OXR API error {status}")
        self.status = status
        self.code = code
        self.message = message
        self.endpoint = endpoint
        self.payload = payload


class NotFoundError(APIError): ...


class AuthError(APIError): ...


class AccessRestrictedError(APIError): ...


class NotAllowedError(APIError): ...


class InvalidBaseError(APIError): ...


# mapping table
ERROR_MAP: dict[tuple[int, str], type[APIError]] = {
    (401, "missing_app_id"): AuthError,
    (401, "invalid_app_id"): AuthError,
    (403, "access_restricted"): AccessRestrictedError,
    (404, "not_found"): NotFoundError,
    (429, "not_allowed"): NotAllowedError,
    (403, "not_allowed"): NotAllowedError,
    (400, "invalid_base"): InvalidBaseError,
}
