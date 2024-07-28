# app/routes/__init__.py

from flask_restful import Api

from .user_routes import user_routes
from .product_routes import product_routes
from .auth_routes import auth_routes


def initialize_routes(api: Api):
    all_routes = [
        (auth_routes, "/auth"),
        (user_routes, "/users"),
        (product_routes, "/products"),
    ]

    for resource_routes, base_url in all_routes:
        for resource, route in resource_routes:
            api.add_resource(resource, "/api" + base_url + route)
