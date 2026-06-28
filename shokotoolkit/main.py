from shokotoolkit import __version__

from shokotoolkit.logging import (
    setup_logging,
    get_logger,
)

from shokotoolkit.constants import APP_NAME


def main():

    setup_logging()

    log = get_logger("main")

    log.info("%s %s", APP_NAME, __version__)

    log.info("Toolkit started.")
