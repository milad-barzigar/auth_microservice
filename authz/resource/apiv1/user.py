from flask_restful import Resource

from authz.controller .apiv1 import UserController

class UserResource(Resource):
    def get(self, user_id=None):
        """
        GET/users --> Get list of users.
        GET/users/<user_id> --> Get user.
        """
        if user_id is None:
            return UserController.get_users()   #get list of users.
        else:
            return Usercontroller.get_user(user_id) #Get user.
        
    def post(self):
        """
        POST /users --> create new user.
        POST /users/<user_id> --> Not allowed.
        """
        return UserController.create_user() #create new user.
        
      
    def path(self, user_id):
        """
        PATH /users/<user_id> --> Not allowed.
        PATH /users/<user_id> --> update user.
        """
        return UserController.update_user(user_id) #update user
        
        
    def delete(self, user_id):
        """
        DELETE /users -->not allowed.
        DELETE /users/<user_id> --> Delete user.
        """
        return Usercontroller.delete_user(user_id) #Delete user
