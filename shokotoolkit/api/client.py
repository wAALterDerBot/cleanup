from __future__ import annotations

import requests

from shokotoolkit.logging import get_logger

log = get_logger(__name__)


class ApiClient:

    def __init__(self, host: str):

        self.host = host.rstrip("/")

        self.session = requests.Session()

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs,
    ):

        url = self.host + endpoint

        log.debug("%s %s", method.upper(), url)

        response = self.session.request(
            method,
            url,
            **kwargs,
        )

        response.raise_for_status()

        return response
