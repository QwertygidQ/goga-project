import logging
import os
import sys
import telegram
import time

logger = logging.getLogger()
logger.setLevel(level=os.environ.get("LOGLEVEL", "ERROR").upper())


def test_db():
    from database import session, User, Event

    u = User(telegram_id=str(int(time.time())))
    print(u)

    session.add(u)
    for i in range(7):
        e = Event(expired=(i % 2 == 0))
        session.add(e)
        u.events.append(e)
    session.commit()

    print(*Event.upcoming_events(session, 2), sep="\n")


test_db()


if "TG_BOT_TOKEN" not in os.environ:
    logger.critical("No TG_BOT_TOKEN environment variable found")
    sys.exit(1)

bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])
print(bot.get_me())
