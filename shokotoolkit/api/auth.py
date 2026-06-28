from __future__ import annotations

from anime_cleanup.api.client import ApiClient


class Authentication:

    def __init__(self, client: ApiClient):

        self.client = client

    def login(self):

        payload = {
            "user": self.client.config.username,
            "pass": self.client.config.password,
            "device": "shoko-toolkit",
        }

        result = self.client.post(
            "/auth",
            payload,
        )

        token = result["token"]

        self.client.session.headers.update(
            {
                "Authorization": f"Bearer {token}"
            }
        )

        return token
