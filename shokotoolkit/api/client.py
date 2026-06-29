from __future__ import annotations

from typing import Any

import requests

from shokotoolkit.api.exceptions import (
    ApiAuthenticationError,
    ApiConnectionError,
    ApiRequestError,
)
from shokotoolkit.logging import get_logger

log = get_logger(__name__)


class ApiClient:
    """
    Low level HTTP client for Shoko.

    Responsible only for:
    - Authentication headers
    - HTTP communication
    - Error handling
    - Response decoding
    """

    DEFAULT_TIMEOUT = 30

    def __init__(
        self,
        host: str,
        api_key: str | None = None,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:

        self.host = host.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Accept": "application/json",
                "User-Agent": "ShokoToolkit/0.1",
            }
        )

        if api_key:
            self.set_api_key(api_key)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get(self, endpoint: str, **kwargs) -> Any:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> Any:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> Any:
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Any:
        return self.request("DELETE", endpoint, **kwargs)

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ) -> Any:

        url = self._build_url(endpoint)

        log.debug(
            "%s %s",
            method.upper(),
            url,
        )

        response = self._send(
            method=method,
            url=url,
            **kwargs,
        )

        self._raise_for_status(response)

        return self._decode_response(response)

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    def set_api_key(self, api_key: str) -> None:
        """
        Configure Shoko API key.
        """

        self.session.headers["apikey"] = api_key

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    def _build_url(self, endpoint: str) -> str:

        if endpoint.startswith("http://"):
            return endpoint

        if endpoint.startswith("https://"):
            return endpoint

        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"

        return f"{self.host}{endpoint}"

    def _send(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> requests.Response:

        try:

            return self.session.request(
                method=method.upper(),
                url=url,
                timeout=self.timeout,
                **kwargs,
            )

        except requests.exceptions.RequestException as exc:

            raise ApiConnectionError(
                f"Failed to connect to {url}: {exc}"
            ) from exc

    def _raise_for_status(
        self,
        response: requests.Response,
    ) -> None:

        if response.status_code == 401:

            raise ApiAuthenticationError(
                "Authentication failed. "
                "Check your API key."
            )

        if response.ok:
            return

        message = response.text.strip()

        raise ApiRequestError(
            response.status_code,
            message,
        )

    def _decode_response(
        self,
        response: requests.Response,
    ) -> Any:

        if not response.content:
            return None

        content_type = response.headers.get(
            "Content-Type",
            "",
        ).lower()

        if "application/json" in content_type:

            try:
                return response.json()

            except ValueError:

                log.warning(
                    "Invalid JSON received from API"
                )

        return response.text

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def ping(self) -> bool:
        """
        Simple connectivity test.

        Only verifies the host is reachable.
        """

        try:

            self.session.get(
                self.host,
                timeout=5,
            )

            return True

        except Exception:

            return False

    def close(self) -> None:

        self.session.close()

    def __enter__(self):

        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:

        self.close()
