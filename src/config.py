import sys
import logging
import coloredlogs
from os import environ


logger = logging.getLogger("goga")
coloredlogs.install(
    level=environ.get("LOGLEVEL", "WARN").upper(),
    logger=logger,
    fmt="[ %(asctime)s.%(msecs)03d ] %(levelname)-7s %(message)s",
)

database_path = "sqlite:///db.sqlite"  # = "postgres://172.24.24.21"

if "TG_BOT_TOKEN" not in environ:
    logger.critical("No TG_BOT_TOKEN environment variable found")
    sys.exit(1)

if "SECRET_KEY" not in environ:
    logger.critical("No SECRET_KEY environment variable found")
    sys.exit(1)

bot_token = environ["TG_BOT_TOKEN"]
secret_key = environ["SECRET_KEY"]
