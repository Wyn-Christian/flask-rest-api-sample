# app/resources/auth_resource.py

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from http_constants.status import HttpStatus

from app.models.user_model import User
from app.extensions import db

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, required=True, help="Username is required")
parser.add_argument("email", type=str, required=True, help="Email is required")
parser.add_argument("password", type=str, required=True, help="Password is required")


class RegisterResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        email = args["email"]
        password = args["password"]

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, HttpStatus.BAD_REQUEST

        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, HttpStatus.BAD_REQUEST

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, HttpStatus.CREATED


class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        email = args["email"]
        password = args["password"]

        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            return {"message": "Invalid email or password"}, HttpStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return response, HttpStatus.OK


class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        return {"message": f"Welcome {user.username}"}, HttpStatus.OK
