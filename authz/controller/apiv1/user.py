from flask import request

from authz.authz import db
from authz.model import User
from authz.schema.apiv1 import UserSchema
from authz.util import jsonify 

class UserController:

    def get_users():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101)  # invalid media type
        try:
            users = User.query.all()
        except Exception as e:
            return jsonify(status=500, code=102) #Database error.
        users_schema = UserSchema(many=True)
        return jsonyfy(
            {"users": users_schema.dump(user)}
        )
    def get_user(user_id):
         return jsonify(status=501, code=107) # Not Implemented.
        
    def creat_user():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101) #Invalid media type .
        user_schema = UserSchema(only=["username", "password"])
        user_data = user_schema.load(request.get_json()) #read and validate user data .
        user = User.query.filter_by(username=user_data.get("username")).first()
        if user is not None:
            return jsonify(status=409, code=106) #user is already exist.
        user = User(
            username=user_data.get("username"),
            password=user_data.get("password")
        )
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return jsonify(
            {"user":user_schema.dump(user)}, 201
        )
        
    def update_user(user_id):
         return jsonify(status=501, code=107) # Not Implemented.
        
    def delete_user(user_id):
         return jsonify(status=501, code=107) # Not Implemented.
