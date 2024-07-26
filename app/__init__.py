# __init__.py

import logging
from flask import Flask
from flask_restful import Api

from app.extensions import db, migrate, mail, cors, jwt_manager
from app.routes import initialize_routes
from app.utils.errors import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)
    mail.init_app(app)
    cors.init_app(app)
    jwt_manager.init_app(app)

    api = Api(app)
    initialize_routes(api)

    register_error_handlers(app)

    return app
