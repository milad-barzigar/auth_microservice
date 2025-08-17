from flask import request
from jwt import encode
from time import time
from datetime import datetime, timezone

from authz.authz import db
from authz.config.config import Config
from authz.model import User
from authz.schema.apiv1 import UserSchema
from authz.util import jsonify


class AuthController:
    @staticmethod
    def create_jwt_token():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101)  # Invalid media type.

        user_schema = UserSchema(only=["username", "password"])
        try:
            user_data = user_schema.load(request.get_json())  # validate request
        except Exception:
            return jsonify(status=400, code=104)

        username = user_data.get("username")
        password = user_data.get("password")
        if not username or not password:
            return jsonify(status=400, code=105)

        try:
            user = User.query.filter_by(username=username).first()
        except Exception:
            return jsonify(status=500, code=102)  # Database error

        if user is None:
            return jsonify(status=401, code=103)  # User not found

        # TODO: Use a secure password hash check instead of plain comparison
        if user.password != password:
            user.failed_auth_at = datetime.now(timezone.utc)
            user.failed_auth_count += 1
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
            return jsonify(status=401, code=111)  # Invalid password

        if user.expires_at and user.expires_at < datetime.now(timezone.utc):
            return jsonify(status=401, code=108)  # User expired

        if user.status != Config.USER_ACTIVE_STATUS:
            return jsonify(status=401, code=109)  # Bad status

        current_time = int(time())
        try:
            user_jwt_token = encode(
                {
                    "sub": user.id,
                    "exp": current_time + Config.USER_DEFAULT_TOKEN_EXPIRY_TIME,
                    "nbf": current_time,
                    "data": {
                        "id": user.id,
                        "username": user.username,
                        "role": user.role,
                    }
                },
                Config.SECRET_KEY,
                algorithm=Config.JWT_ALGO
            )
        except Exception:
            return jsonify(status=500, code=110)  # Token encryption error

        user.last_login_at = datetime.now(timezone.utc)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return jsonify(status=500, code=102)  # Database error

        return jsonify(
            status=200,
            data={"user": UserSchema().dump(user)},
            headers={"X-Subject-Token": user_jwt_token}
        )

    @staticmethod
    def verify_jwt_token():
        return jsonify(status=501, code=107)  # Not Implemented

