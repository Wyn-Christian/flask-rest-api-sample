from flask_restful import Resource, reqparse
from http_constants.status import HttpStatus
from http_constants import status

from app.models.product_model import Product
from app.models.user_model import User
from app.extensions import db

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name is required")
parser.add_argument("description", type=str, required=True, help="Name is required")
parser.add_argument("price", type=str, required=True, help="Name is required")
parser.add_argument("stock", type=str, required=True, help="Name is required")
parser.add_argument("owner_id", type=str, required=True, help="Name is required")


class ProductResource(Resource):
    def get(self, product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return {}, HttpStatus.NOT_FOUND

            return product.to_dict(), HttpStatus.OK

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, status.BAD_REQUEST

    def delete(self, product_id):
        try:
            product = Product.query.get_or_404(product_id)

            db.session.delete(product)
            db.session.commit(product)

            return product.to_dict(), HttpStatus.OK

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST


class ProductListResource(Resource):
    def get(self):
        try:
            products = Product.query.all()
            return [product.to_dict() for product in products], HttpStatus.OK

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST

    def post(self):
        try:
            args = parser.parse_args()
            owner = User.query.get(args["owner_id"])
            if not owner:
                return {
                    "message": f"`owner_id` ({args['owner_id']}) doesn't exist!"
                }, HttpStatus.NOT_FOUND

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

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST
