# authz/authz.py  ( create_app)
from flask import Flask, Blueprint
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authz.config.config import config

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # init extensions
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    # ---- IMPORT RESOURCES HERE (after extensions) ----
   
    from authz.resource.apiv1.user import UserResource
    
    try:
        from authz.resource.apiv1.auth import AuthResource
    except Exception:
        AuthResource = None

    # REGISTER resources to the Api instance
    apiv1.add_resource(UserResource, "/users", "/users/<int:user_id>")
    if AuthResource is not None:
        apiv1.add_resource(AuthResource, "/auth/tokens", methods=["GET", "POST"])

    # register blueprint
    app.register_blueprint(apiv1_bp)
    return app

