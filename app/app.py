from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api

from config.config import app_config


db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(app_config)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        db.create_all()
    api = Api(app)

    from .blueprints.user_blueprints import register_routes

    register_routes(api)

    return app
