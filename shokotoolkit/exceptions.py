"""
Custom exceptions.
"""


class ShokoToolkitError(Exception):
    """Base exception."""


class ConfigurationError(ShokoToolkitError):
    """Configuration is invalid."""


class AuthenticationError(ShokoToolkitError):
    """Authentication failed."""


class ApiError(ShokoToolkitError):
    """API request failed."""


class ScannerError(ShokoToolkitError):
    """Library scanner failed."""


class CleanupError(ShokoToolkitError):
    """Cleanup failed."""
