# app/routes/product_routes.py

from app.resources.product_resource import ProductResource, ProductListResource


product_routes = [(ProductListResource, "/"), (ProductResource, "/<int:product_id>")]
