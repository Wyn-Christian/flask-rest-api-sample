from flask_restful import Api
from app.resources.user_resource import UserResource, UserListResource


def initialize_user_routes(api: Api):
    api.add_resource(UserListResource, "/api/users")
    api.add_resource(UserResource, "/api/users/<int:user_id>")
