# extensions.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_login import LoginManager


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
cors = CORS()
jwt_manager = JWTManager()
login_manager = LoginManager()
