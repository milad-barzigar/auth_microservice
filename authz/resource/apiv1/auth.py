from flask import request
from flask_restful import Resource
# ایمپورت مستقیم از زیرماژول کنترلر (برای جلوگیری از circular import)
from authz.controller.apiv1.auth import AuthController

class AuthResource(Resource):
    def get(self):
        """
        GET /api/v1/auth/tokens  -> Validate token (expects Authorization: Bearer <token>)
        """
        auth_controller = AuthController()
        return auth_controller.verify_jwt_token()

    def post(self):
        """
        POST /api/v1/auth/tokens -> Create a new token.
        JSON body used as payload.
        """
        payload = request.get_json(silent=True) or {}
        auth_controller = AuthController()
        return auth_controller.create_jwt_token(payload)

