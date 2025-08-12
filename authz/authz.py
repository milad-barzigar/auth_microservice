# authz/authz.py

from flask import Flask, Blueprint
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from authz.config import config

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)
    from authz import resource  
    app.register_blueprint(apiv1_bp)
    return app


