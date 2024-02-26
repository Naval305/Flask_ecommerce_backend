from flask import request
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from app.models.user_model import User
from app.blueprints.user_blueprints import blp
from app.services.user_service import UserService
from app.schemas.user_schemas import CreateUserSchema, UserListSchema


@blp.route("/get-create")
class CreateUser(MethodView):

    def __init__(self) -> None:
        self.user_service = UserService()

    @blp.response(200, UserListSchema(many=True))
    def get(self):
        """Get user list"""

        try:
            users = self.user_service.get_users()
            return users
        except SQLAlchemyError as e:
            return {"message": "Database error"}, 500
        except Exception as e:
            return {"message": "Internal server error"}, 500

    @blp.arguments(CreateUserSchema)
    @blp.response(201, CreateUserSchema)
    def post(self):
        """Create a new user"""

        try:
            data = request.get_json()

            validation_result = self.validate_user_data(data)
            if validation_result is not None:
                return validation_result

            new_user_id = self.user_service.create_user(
                data["first_name"], data["last_name"], data["email"], data["password"]
            )

            return {"message": "User created successfully", "user_id": new_user_id}, 201
        except SQLAlchemyError as e:
            return {"message": "Database error"}, 500
        except Exception as e:
            return {"message": "Internal server error"}, 500

    @classmethod
    def validate_user_data(self, data):
        required_fields = ["first_name", "last_name", "email", "password"]
        if not all(field in data for field in required_fields):
            return {"message": "Missing required fields"}, 400

        if User.query.filter_by(email=data["email"]).first():
            return {"message": "Email address already in use"}, 400

        return None
