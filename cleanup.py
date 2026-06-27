from pathlib import Path

from anime_cleanup.scanner import LibraryScanner

ROOT = Path("/mnt/TANK/media/anime")

library = LibraryScanner(ROOT).scan()

print("=" * 60)
print("Anime Library Scanner")
print("=" * 60)

print(f"Series         : {library.series_count}")
print(f"TMDB folders   : {library.tmdb_count}")
print(f"Legacy folders : {library.legacy_count}")
print(f"Season folders : {library.season_count}")
print(f"Video files    : {library.video_count}")

print("=" * 60)
