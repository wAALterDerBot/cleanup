from __future__ import annotations

from anime_cleanup.api.client import ApiClient


class FilesApi:

    def __init__(self, client: ApiClient):

        self.client = client

    def all(self):

        return self.client.get("/v3/File")
