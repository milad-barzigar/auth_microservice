from uuid import uuid4
from authz.authz import db
from authz.config.config import config
from datetime import datetime, timedelta

def user_expires_at():
    return datetime.utcnow() + timedelta(days=30)

def now():
    return datetime.utcnow()

class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=lambda: uuid4().hex)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(32), nullable=False, default=config.USER_DEFAULT_ROLE)
    created_at = db.Column(db.DateTime, nullable=False, default=now)
    expires_at = db.Column(db.DateTime, nullable=False, default=user_expires_at)
    last_login_at = db.Column(db.DateTime, nullable=True, default=None)
    last_active_at = db.Column(db.DateTime, nullable=True, default=None)
    last_change_at = db.Column(db.DateTime, nullable=True, default=None)
    failed_auth_at = db.Column(db.DateTime, nullable=True, default=None)
    failed_auth_count = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=config.USER_DEFAULT_STATUS)
