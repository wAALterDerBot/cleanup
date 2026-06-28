from __future__ import annotations

import logging
from pathlib import Path

from rich.logging import RichHandler

from shokotoolkit.constants import LOG_DIR, LOG_FILE


_INITIALIZED = False


def setup_logging(level: str = "INFO") -> None:
    """
    Initialize console and file logging.
    """

    global _INITIALIZED

    if _INITIALIZED:
        return

    LOG_DIR.mkdir(exist_ok=True)

    handlers = [
        RichHandler(
            rich_tracebacks=True,
            markup=True,
        ),
        logging.FileHandler(
            LOG_FILE,
            encoding="utf8",
        ),
    ]

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s %(name)-18s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S",
        handlers=handlers,
    )

    _INITIALIZED = True


def get_logger(name: str) -> logging.Logger:
    """
    Return a logger instance.
    """

    return logging.getLogger(name)
