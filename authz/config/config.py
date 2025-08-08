from os import environ

class config:

##################### Application config #####################

    ENV = environ.get("TECHLAND_AUTHZ_ENV", "production")
    
    DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_DEBUG", "0")))
    
    TESTING = bool(int(environ.get("TECHLAND_AUTHZ_TESTING", "0")))
    
    SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
    
    TIMEZONE = environ.get("TECHLAND_AUTHZ_TIMEZONE", "Asia/Tehran")
    ##################### Database config #####################
    
    SQLALCHEMY_DATABASE_URI = environ.get("TECHLAND_AUTHZ_DATABASE_URI", None)
    
    SQLALCHEMY_ECHO = DEBUG
    
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
     ##################### User config ##########################
     
     USER_DEFAULT_ROLE = environ.get("TECLAND_AUTHZ-USER-DEFAULT_ROLE", "member")
     
     USER_DEFAULT_EXPIRY_TIME = int(environ.get("TECLAND_AUTHZ-USER-DEFAULT_EXPIRY_TIME", "365"))
     
     USER_DEFAULT_STATUS = int(environ.get("TECLAND_AUTHZ-USER-DEFAULT_STATUS", "3"))
   
