from flask_restful import Resource, reqparse
from http_constants.status import HttpStatus

from app.models.user_model import User
from app.extensions import db

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required")
parser.add_argument("email", type=str, required=True, help="Email is required")


class UserResource(Resource):
    def get(self, user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return {}, HttpStatus.NOT_FOUND

            return user.to_dict(), HttpStatus.OK

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST

    def delete(self, user_id):
        try:
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            return "", HttpStatus.NO_CONTENT

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST


class UserListResource(Resource):
    def get(self):
        try:
            users = User.query.all()

            return [user.to_dict() for user in users], HttpStatus.OK

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST

    def post(self):
        try:
            args = parser.parse_args()
            user = User(username=args["username"], email=args["email"])
            db.session.add(user)
            db.session.commit()
            return user.to_dict(), HttpStatus.CREATED

        except Exception as e:
            print(f"An Error occured: {str(e)}")
            return {"message": str(e)}, HttpStatus.BAD_REQUEST
