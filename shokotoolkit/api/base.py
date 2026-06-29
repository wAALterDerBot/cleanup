"""
Base class for all API services.
"""

from __future__ import annotations

from shokotoolkit.api.client import ApiClient


class BaseService:

    def __init__(self, client: ApiClient):

        self.client = client

    def get(self, endpoint: str, **kwargs):

        return self.client.get(
            endpoint,
            **kwargs,
        )

    def post(self, endpoint: str, **kwargs):

        return self.client.post(
            endpoint,
            **kwargs,
        )

    def put(self, endpoint: str, **kwargs):

        return self.client.put(
            endpoint,
            **kwargs,
        )

    def delete(self, endpoint: str, **kwargs):

        return self.client.delete(
            endpoint,
            **kwargs,
        )
