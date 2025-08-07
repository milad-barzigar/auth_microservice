# authz/authz.py

from flask import Flask, Blueprint
from flask_restful import Api

from authz.config import config

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
paiv1 = Api(apiv1_bp)

from authz import resource 

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(apiv1_bp)
    return app

