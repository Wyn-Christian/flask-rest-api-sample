# app/resources/auth_resource.py

from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)
from http_constants.status import HttpStatus

from app.models.user_model import User
from app.extensions import db


class RegisterResource(Resource):
    def post(self):
        register_parser = reqparse.RequestParser()
        register_parser.add_argument(
            "username", type=str, required=True, help="Username is required"
        )
        register_parser.add_argument(
            "email", type=str, required=True, help="Email is required"
        )
        register_parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )

        args = register_parser.parse_args()
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
        login_parser = reqparse.RequestParser()
        login_parser.add_argument(
            "email", type=str, required=True, help="Email is required"
        )
        login_parser.add_argument(
            "password", type=str, required=True, help="Password is required"
        )

        args = login_parser.parse_args()
        email = args["email"]
        password = args["password"]

        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            return {"message": "Invalid email or password"}, HttpStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify({"message": "Login Successfully"})

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response


class LogoutResource(Resource):
    def post(self):
        response = jsonify({"message": "Logout Successfully!"})
        unset_jwt_cookies(response)
        return response


class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        return {"message": f"Welcome {user.username}"}, HttpStatus.OK
