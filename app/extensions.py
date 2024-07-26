# extensions.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

from flask_mail import Mail

from flask_cors import CORS
from flask_jwt_extended import JWTManager


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
mail = Mail()
cors = CORS()
jwt_manager = JWTManager()
