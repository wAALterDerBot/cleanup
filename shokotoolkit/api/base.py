"""
Base service for all Shoko API services.
"""

from __future__ import annotations

from typing import Any

from shokotoolkit.api.client import ApiClient


class BaseService:
    """
    Base class for all API services.

    Provides a thin wrapper around the ApiClient so derived
    services can focus entirely on endpoint-specific logic.
    """

    def __init__(self, client: ApiClient) -> None:
        self.client = client

    # ------------------------------------------------------------------
    # HTTP Helpers
    # ------------------------------------------------------------------

    def get(self, endpoint: str, **kwargs) -> Any:
        return self.client.get(endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Any:
        return self.client.post(endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> Any:
        return self.client.put(endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Any:
        return self.client.delete(endpoint, **kwargs)

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    @property
    def host(self) -> str:
        return self.client.host

    @property
    def headers(self) -> dict[str, str]:
        return self.client.headers
