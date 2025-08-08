from datetime import datetime
from pytz import timezone, utc

from authz.config import config

def now(name=config.TIMEZONE):
    tz = timezone(name)
    return datetime.utcnow().replace(tzinfo=utc).astimezone(tz).replace(
        microsecond=0, tzinfo=None
)
