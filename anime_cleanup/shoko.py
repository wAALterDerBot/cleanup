from __future__ import annotations

from anime_cleanup.config import ShokoConfig

from anime_cleanup.api.client import ApiClient
from anime_cleanup.api.auth import Authentication
from anime_cleanup.api.series import SeriesApi
from anime_cleanup.api.files import FilesApi


class ShokoClient:

    def __init__(self, config: ShokoConfig):

        self.client = ApiClient(config)

        Authentication(self.client).login()

        self.series = SeriesApi(self.client)
        self.files = FilesApi(self.client)
