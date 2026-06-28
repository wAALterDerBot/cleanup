class ApiException(Exception):
    """Base API exception."""


class AuthenticationException(ApiException):
    """Authentication failed."""


class RequestException(ApiException):
    """HTTP request failed."""
