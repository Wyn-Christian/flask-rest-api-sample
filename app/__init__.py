from flask import Flask
from flask_restful import Api

from app.extensions import db, migrate
from app.routes import initialize_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    api = Api(app, catch_all_404s=True)
    initialize_routes(api)

    return app
