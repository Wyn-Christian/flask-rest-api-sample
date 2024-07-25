# app/routes/user_routes.py

from app.resources.user_resource import UserResource, UserListResource


user_routes = [(UserListResource, "/"), (UserResource, "/<int:user_id>")]
