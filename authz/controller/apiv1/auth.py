cat > authz/controller/apiv1/auth.py <<'PY'
import os
import datetime
import jwt  # PyJWT
from flask import request
from authz.util import jsonify

class AuthController:
    def __init__(self):
        self.secret = os.environ.get("JWT_SECRET", "dev-secret")
        self.alg = os.environ.get("JWT_ALG", "HS256")

    def create_jwt_token(self, payload: dict | None = None):
        if payload is None:
            payload = request.get_json(silent=True) or {}
        if not isinstance(payload, dict):
            payload = {}

        now = datetime.datetime.utcnow()
        payload = payload.copy()
        payload.setdefault("iat", int(now.timestamp()))
        payload.setdefault("exp", int((now + datetime.timedelta(hours=1)).timestamp()))

        token = jwt.encode(payload, self.secret, algorithm=self.alg)
        if isinstance(token, bytes):
            token = token.decode("utf-8")

        return jsonify(status=200, code=0, token=token), 200

    def verify_jwt_token(self, token: str | None = None):
        if token is None:
            auth_header = request.headers.get("Authorization", "")
            parts = auth_header.split()
            if len(parts) == 2 and parts[0].lower() == "bearer":
                token = parts[1]

        if not token:
            return jsonify(status=400, code=106, message="Missing token"), 400

        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.alg])
            return jsonify(status=200, code=0, data=payload), 200
        except jwt.ExpiredSignatureError:
            return jsonify(status=401, code=108, message="Token expired"), 401
        except jwt.InvalidTokenError:
            return jsonify(status=401, code=109, message="Invalid token"), 401
        except Exception as e:
            return jsonify(status=500, code=110, message=str(e)), 500
PY

