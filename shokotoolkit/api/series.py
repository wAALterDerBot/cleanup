from __future__ import annotations

from anime_cleanup.api.client import ApiClient


class SeriesApi:

    def __init__(self, client: ApiClient):

        self.client = client

    def all(self):

        return self.client.get("/v3/Series")

    def by_id(self, series_id: int):

        return self.client.get(
            f"/v3/Series/{series_id}"
        )
