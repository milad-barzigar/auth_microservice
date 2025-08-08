from datetime import timedalta

from authz.config import config
from authz.util import now

def user_expires_at():
	return now() + timedelta(days=config.USER_DEFAULT_EXPIRY_TIME)
