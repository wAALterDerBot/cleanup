"""
anime_cleanup.scanner

Scans an anime library and builds an in-memory representation of
all detected series, seasons and video files.

Nothing is modified.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from anime_cleanup.models import (
    Library,
    SeriesFolder,
    SeasonFolder,
    VideoFile,
)

import re

VIDEO_EXTENSIONS = {
    ".mkv",
    ".mp4",
    ".avi",
    ".m2ts",
    ".ts",
    ".mov",
    ".wmv",
    ".flv",
}


TMDB_PATTERN = re.compile(r"\{tmdb-(\d+)\}$", re.IGNORECASE)
TVDB_PATTERN = re.compile(r"\{tvdb-(\d+)\}$", re.IGNORECASE)
SEASON_PATTERN = re.compile(r"Season\s+(\d+)", re.IGNORECASE)



class LibraryScanner:

    def __init__(self, root: Path):

        self.root = root

    def scan(self) -> list[SeriesFolder]:

        series_list: list[SeriesFolder] = []

        for folder in sorted(self.root.iterdir()):

            if not folder.is_dir():
                continue

            series = self._scan_series(folder)

            series_list.append(series)

        return series_list

    def _scan_series(self, folder: Path) -> SeriesFolder:

        tmdb = None
        tvdb = None

        tmdb_match = TMDB_PATTERN.search(folder.name)
        if tmdb_match:
            tmdb = int(tmdb_match.group(1))

        tvdb_match = TVDB_PATTERN.search(folder.name)
        if tvdb_match:
            tvdb = int(tvdb_match.group(1))

        series = SeriesFolder(
            name=folder.name,
            path=folder,
            tmdb_id=tmdb,
            tvdb_id=tvdb,
        )

        for child in sorted(folder.iterdir()):

            if child.is_dir():

                season_match = SEASON_PATTERN.fullmatch(child.name)

                if season_match:

                    season = SeasonFolder(
                        number=int(season_match.group(1)),
                        path=child,
                    )

                    self._scan_videos(child, season.videos)

                    series.seasons.append(season)

            elif child.is_file():

                if child.suffix.lower() in VIDEO_EXTENSIONS:

                    series.loose_files.append(
                        VideoFile(
                            path=child,
                            size=child.stat().st_size,
                        )
                    )

        return series

    @staticmethod
    def _scan_videos(folder: Path, target: list[VideoFile]):

        for file in sorted(folder.rglob("*")):

            if not file.is_file():
                continue

            if file.suffix.lower() not in VIDEO_EXTENSIONS:
                continue

            target.append(
                VideoFile(
                    path=file,
                    size=file.stat().st_size,
                )
            )
