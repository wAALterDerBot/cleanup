from pathlib import Path

from scanner import LibraryScannerr

ROOT = Path("/mnt/TANK/media/anime")

scanner = LibraryScanner(ROOT)

library = scanner.scan()

print()
print("=" * 60)
print("Anime Library Scanner")
print("=" * 60)

series_count = len(library)
season_count = 0
video_count = 0
tmdb_count = 0
legacy_count = 0

for series in library:

    if series.tmdb_id:
        tmdb_count += 1
    else:
        legacy_count += 1

    season_count += len(series.seasons)

    for season in series.seasons:
        video_count += len(season.videos)

    video_count += len(series.loose_files)

print(f"Series          : {series_count}")
print(f"TMDB folders    : {tmdb_count}")
print(f"Legacy folders  : {legacy_count}")
print(f"Season folders  : {season_count}")
print(f"Video files     : {video_count}")
print("=" * 60)
