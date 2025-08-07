# authz/authz.py

from flask import Flask
from authz.config import config
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    print(app.config)
    return app

