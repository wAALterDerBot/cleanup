"""
anime_cleanup.models

Shared data models used throughout the application.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class VideoFile:
    path: Path
    size: int


@dataclass(slots=True)
class SeasonFolder:
    number: int
    path: Path
    videos: list[VideoFile] = field(default_factory=list)


@dataclass(slots=True)
class SeriesFolder:
    name: str
    path: Path

    tmdb_id: int | None = None
    tvdb_id: int |None = None

    seasons: list[SeasonFolder] = field(default_factory=list)
    loose_files: list[VideoFile] = field(default_factory=list)


@dataclass(slots=True)
class Library:
    root: Path
    series: list[SeriesFolder] = field(default_factory=list)

    @property
    def is_tmdb(self) -> bool:
    return self.tmdb_id is not None


    @property
    def is_legacy(self) -> bool:
    return self.tmdb_id is None


    @property
    def has_seasons(self) -> bool:
    return len(self.seasons) > 0


    @property
    def has_loose_files(self) -> bool:
    return len(self.loose_files) > 0
    
    @property
    def series_count(self) -> int:
        return len(self.series)

    @property
    def season_count(self) -> int:
        return sum(len(s.seasons) for s in self.series)

    @property
    def video_count(self) -> int:
        total = 0

        for series in self.series:
            total += len(series.loose_files)

            for season in series.seasons:
                total += len(season.videos)

        return total

    @property
    def tmdb_count(self) -> int:
        return sum(1 for s in self.series if s.tmdb_id)

    @property
    def legacy_count(self) -> int:
        return self.series_count - self.tmdb_count
