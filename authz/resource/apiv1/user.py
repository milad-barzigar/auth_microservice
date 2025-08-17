# authz/resource/apiv1/user.py
from flask_restful import Resource
from authz.controller.apiv1.user import UserController

class UserResource(Resource):
    def __init__(self):
       
        self.controller = UserController()

    def get(self, user_id=None):
        if user_id is None:
            return self.controller.get_users()
        return self.controller.get_user(user_id)

    def post(self):
        return self.controller.create_user()

    def patch(self, user_id):
        return self.controller.update_user(user_id)

    def delete(self, user_id):
        return self.controller.delete_user(user_id)

