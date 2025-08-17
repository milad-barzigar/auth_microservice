# authz/config/config.py
import os

class Config:
    """Base configuration for the authz app."""
    # ----------------- Application config -----------------
    ENV = os.environ.get("TECHLAND_AUTHZ_ENV", "production")
    DEBUG = bool(int(os.environ.get("TECHLAND_AUTHZ_DEBUG", "0")))
    TESTING = bool(int(os.environ.get("TECHLAND_AUTHZ_TESTING", "0")))
    SECRET_KEY = os.environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
    TIMEZONE = os.environ.get("TECHLAND_AUTHZ_TIMEZONE", "Asia/Tehran")
    JWT_ALGO = os.environ.get("TECHLAND_AUTHZ_JWT_ALGO", "HS512")
    # ----------------- Database config -----------------
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("TECHLAND_AUTHZ_DATABASE_URI", "sqlite:///mydb.db")
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ----------------- User config -----------------
    USER_ENABLED_STATUS = 1
    USER_ACTIVATED_STATUS = 2
    USER_ALL_STATUS = 3
    USER_DEFAULT_ROLE = os.environ.get("TECHLAND_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_EXPIRY_TIME = int(os.environ.get("TECHLAND_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(os.environ.get("TECHLAND_AUTHZ_USER_DEFAULT_STATUS", "3"))
    USER_DEFAULT_TOKEN_EXPIRY_TIME = int(os.environ.get("TECHLAND_AUTHZ_USER_DEFAULT_TOKEN_EXPIRY_TIME", "46400"))
   
config = Config()

