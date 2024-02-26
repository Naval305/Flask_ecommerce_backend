from flask_smorest import Api
from flask_smorest import Blueprint


blp = Blueprint(
    "users", __name__, url_prefix="/api/users", description="User Operations"
)
from app.apis.user_api import *


def register_routes(api: Api):
    api.register_blueprint(blp)
