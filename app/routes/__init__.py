from app.routes.user_routes import initialize_user_routes
from app.routes.product_routes import initialize_product_routes


def initialize_routes(api):
    initialize_user_routes(api)
    initialize_product_routes(api)
