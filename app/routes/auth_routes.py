# app/routes/auth_routes.py

from app.resources.auth_resource import (
    RegisterResource,
    LoginResource,
    LogoutResource,
    ProtectedResource,
)

auth_routes = [
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (LogoutResource, "/logout"),
    (ProtectedResource, "/protected"),
]
