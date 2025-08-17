# authz/controller/apiv1/user.py
from flask import request
from marshmallow import ValidationError
from authz.util import jsonify
from authz.schema.apiv1 import UserSchema
from authz.model import User
from authz.authz import db


class UserController:
    @staticmethod
    def get_users():
        """برگشت لیست کاربران (ساده)"""
        try:
            users = User.query.all()
            user_schema = UserSchema(many=True)
            return user_schema.dump(users), 200
        except Exception:
            return jsonify(status=500, code=103)

    @staticmethod
    def create_user():
        """ایجاد کاربر — بررسی Content-Type و اعتبارسنجی JSON به شکل ایمن"""
        # فقط برای متدهایی که بدنه دارند Content-Type بررسی می‌شود
        if request.method in ("POST", "PUT", "PATCH"):
            content_type = (request.content_type or "").split(";")[0].strip()
            if content_type != "application/json":
                return jsonify(status=415, code=101)  # Unsupported Media Type

        # دریافت JSON به‌صورت safe (silent=True => None اگر parse نشود)
        data = request.get_json(silent=True)
        if data is None:
            # بدنه وجود ندارد یا JSON نامعتبر است
            return jsonify(status=400, code=102)

        # اعتبارسنجی فیلدها با marshmallow
        user_schema = UserSchema(only=["username", "password"])
        try:
            user_data = user_schema.load(data)
        except ValidationError as exc:
            # بازگرداندن خطای اعتبارسنجی داخل state تا با util.jsonify سازگار باشیم
            return jsonify(status=400, code=102, state={"errors": exc.messages})

        # چک نهایی فیلدها (به‌هرحال marshmallow باید این را پوشش دهد)
        if not user_data.get("username") or not user_data.get("password"):
            return jsonify(status=400, code=102)

        # ایجاد کاربر در دیتابیس
        try:
            user = User(username=user_data["username"], password=user_data["password"])
            db.session.add(user)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return jsonify(status=500, code=103)

        # بازگرداندن کاربر ساخته‌شده (می‌توانی user_schema کامل‌تر تعریف کنی)
        out_schema = UserSchema()
        return out_schema.dump(user), 201

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify(status=404, code=104)
        user_schema = UserSchema()
        return user_schema.dump(user), 200

    @staticmethod
    def update_user(user_id):
        # همان الگوی create_user برای بررسی content-type و json
        if request.method in ("POST", "PUT", "PATCH"):
            content_type = (request.content_type or "").split(";")[0].strip()
            if content_type != "application/json":
                return jsonify(status=415, code=101)

        data = request.get_json(silent=True)
        if data is None:
            return jsonify(status=400, code=102)

        user = User.query.get(user_id)
        if not user:
            return jsonify(status=404, code=104)

        if "username" in data:
            user.username = data["username"]
        if "password" in data:
            user.password = data["password"]

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return jsonify(status=500, code=103)

        user_schema = UserSchema()
        return user_schema.dump(user), 200

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify(status=404, code=104)
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return jsonify(status=500, code=103)
        return jsonify(status=200, code=0)

