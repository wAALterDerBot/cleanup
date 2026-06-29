"""
Global constants used by the toolkit.
"""

from pathlib import Path

APP_NAME = "Shoko Toolkit"

APP_VERSION = "0.1.0"

LOG_DIR = Path("logs")

LOG_FILE = LOG_DIR / "shokotoolkit.log"

DEFAULT_HTTP_TIMEOUT = 30

USER_AGENT = "ShokoToolkit/0.1"
