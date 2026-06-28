from __future__ import annotations

from typing import Any

import requests

from shokotoolkit.api.exceptions import (
    ApiConnectionError,
    ApiRequestError,
)
from shokotoolkit.logging import get_logger

log = get_logger(__name__)


DEFAULT_TIMEOUT = 30


class ApiClient:
    """
    Low level HTTP client for Shoko.
    """

    def __init__(
        self,
        host: str,
        api_key: str | None = None,
    ) -> None:

        self.host = host.rstrip("/")

        self.session = requests.Session()

        self.timeout = DEFAULT_TIMEOUT

        if api_key:
            self.set_api_key(api_key)

    @property
    def headers(self) -> dict[str, str]:
        return dict(self.session.headers)

    def set_api_key(self, api_key: str) -> None:
        """
        Configure the API key used for all requests.
        """

        self.session.headers.update(
            {
                "apikey": api_key,
                "Accept": "application/json",
            }
        )

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ) -> Any:

        url = f"{self.host}{endpoint}"

        log.debug("%s %s", method.upper(), url)

        try:

            response = self.session.request(
                method=method.upper(),
                url=url,
                timeout=self.timeout,
                **kwargs,
            )

        except requests.exceptions.RequestException as exc:
            raise ApiConnectionError(str(exc)) from exc

        if not response.ok:

            message = response.text.strip()

            raise ApiRequestError(
                response.status_code,
                message,
            )

        if not response.content:
            return None

        content_type = response.headers.get(
            "Content-Type",
            "",
        )

        if "application/json" in content_type:
            return response.json()

        return response.text

    def get(
        self,
        endpoint: str,
        **kwargs,
    ) -> Any:

        return self.request(
            "GET",
            endpoint,
            **kwargs,
        )

    def post(
        self,
        endpoint: str,
        **kwargs,
    ) -> Any:

        return self.request(
            "POST",
            endpoint,
            **kwargs,
        )

    def put(
        self,
        endpoint: str,
        **kwargs,
    ) -> Any:

        return self.request(
            "PUT",
            endpoint,
            **kwargs,
        )

    def delete(
        self,
        endpoint: str,
        **kwargs,
    ) -> Any:

        return self.request(
            "DELETE",
            endpoint,
            **kwargs,
        )
