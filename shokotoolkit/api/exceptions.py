"""
Custom exceptions used by the API client.
"""


class ApiError(Exception):
    """Base API exception."""


class ApiConnectionError(ApiError):
    """Raised when the API cannot be reached."""


class ApiAuthenticationError(ApiError):
    """Raised when authentication fails."""


class ApiRequestError(ApiError):
    """Raised when the API returns an unexpected response."""

    def __init__(
        self,
        status_code: int,
        message: str,
    ) -> None:

        self.status_code = status_code
        self.message = message

        super().__init__(f"{status_code}: {message}")
