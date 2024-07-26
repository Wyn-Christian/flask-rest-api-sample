# app/resources/product_resource.py

from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import jwt_required
from http_constants.status import HttpStatus

from app.models.product_model import Product
from app.models.user_model import User
from app.extensions import db


class ProductResource(Resource):
    @jwt_required()
    def get(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return abort(
                HttpStatus.NOT_FOUND,
                error="Product Not Found",
                message=f"Product ID ({product_id}) not found",
            )

        return product.to_dict(), HttpStatus.OK

    @jwt_required()
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return abort(
                HttpStatus.NOT_FOUND,
                error="Product Not Found",
                message=f"Product ID ({product_id}) not found",
            )
        db.session.delete(product)
        db.session.commit()

        return {}, HttpStatus.NO_CONTENT


class ProductListResource(Resource):
    @jwt_required()
    def get(self):
        products = Product.query.all()

        return [product.to_dict() for product in products], HttpStatus.OK

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name is required")
        parser.add_argument(
            "description", type=str, required=True, help="Name is required"
        )
        parser.add_argument("price", type=str, required=True, help="Name is required")
        parser.add_argument("stock", type=str, required=True, help="Name is required")
        parser.add_argument(
            "owner_id", type=str, required=True, help="Name is required"
        )

        args = parser.parse_args()
        owner = User.query.get(args["owner_id"])
        if not owner:
            return abort(
                HttpStatus.NOT_FOUND,
                error="Owner/User Not Found",
                message=f"Owner/User ID ({args['owner_id']}) not found",
            )

        product = Product(
            name=args["name"],
            description=args.get("description"),
            price=args["price"],
            stock=args["stock"],
            owner=owner,
        )

        db.session.add(product)
        db.session.commit()

        return product.to_dict(), HttpStatus.CREATED
