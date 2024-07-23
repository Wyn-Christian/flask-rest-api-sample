from flask_restful import Api
from app.resources.product_resource import ProductResource, ProductListResource


def initialize_product_routes(api: Api):
    api.add_resource(ProductListResource, "/api/products")
    api.add_resource(ProductResource, "/api/product/<int:product_id>")
