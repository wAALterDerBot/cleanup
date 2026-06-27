"""
anime_cleanup.models

Shared data models used throughout the application.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# File Model
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class VideoFile:
    path: Path
    size: int


# ---------------------------------------------------------------------------
# Season Model
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class SeasonFolder:
    number: int
    path: Path
    videos: list[VideoFile] = field(default_factory=list)

    @property
    def video_count(self) -> int:
        return len(self.videos)


# ---------------------------------------------------------------------------
# Series Model
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class SeriesFolder:
    name: str
    path: Path

    tmdb_id: int | None = None
    tvdb_id: int | None = None

    seasons: list[SeasonFolder] = field(default_factory=list)
    loose_files: list[VideoFile] = field(default_factory=list)

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
    def season_numbers(self) -> list[int]:
        return sorted(season.number for season in self.seasons)

    @property
    def season_count(self) -> int:
        return len(self.seasons)

    @property
    def video_count(self) -> int:
        return (
            len(self.loose_files)
            + sum(season.video_count for season in self.seasons)
        )


# ---------------------------------------------------------------------------
# Library Model
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class Library:
    root: Path
    series: list[SeriesFolder] = field(default_factory=list)

    @property
    def series_count(self) -> int:
        return len(self.series)

    @property
    def season_count(self) -> int:
        return sum(series.season_count for series in self.series)

    @property
    def video_count(self) -> int:
        return sum(series.video_count for series in self.series)

    @property
    def tmdb_count(self) -> int:
        return sum(1 for series in self.series if series.is_tmdb)

    @property
    def legacy_count(self) -> int:
        return sum(1 for series in self.series if series.is_legacy)
