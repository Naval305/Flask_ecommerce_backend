from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from app.blueprints.user_blueprints import blp
from app.interfaces.user_interface import BaseApiView
from app.schemas.custom_response import CustomResponse
from app.utils.users import generate_jwt, validate_user_data
from app.services.user_service import UserService
from app.schemas.user_schemas import CreateUserSchema, UserListSchema, UserLoginSchema


@blp.route("/list", methods=["GET"])
class GetUserList(BaseApiView):

    @blp.response(200, UserListSchema(many=True))
    def get(self):
        """Get user list"""

        try:
            users = UserService().get_users()

            return users
        except SQLAlchemyError as e:
            return CustomResponse.error(
                message="Database error", status_code=500, exception=e
            )
        except Exception as e:
            return CustomResponse.error(
                message="Internal server error", status_code=500, exception=e
            )


@blp.route("/registration", methods=["POST"])
class Registration(BaseApiView):

    @blp.arguments(CreateUserSchema)
    def post(self, data):
        """Register a new user"""

        try:
            validation_result = validate_user_data(data)
            if validation_result is not None:
                return validation_result

            new_user_id = UserService().create_user(
                data["first_name"], data["last_name"], data["email"], data["password"]
            )
            return CustomResponse.success(
                message="User created successfully",
                data={"user_id": new_user_id},
                status_code=201,
            )
        except SQLAlchemyError as e:
            return CustomResponse.error(
                message="Database error", status_code=500, exception=e
            )
        except Exception as e:
            return CustomResponse.error(
                message="Internal server error", status_code=500, exception=e
            )


@blp.route("/login", methods=["POST"])
class Login(MethodView):

    def __init__(self, user_service=None) -> None:
        self.user_service = user_service or UserService()

    @blp.arguments(UserLoginSchema)
    def post(self, auth):
        """User login"""
        try:
            email = auth.get("email")
            password = auth.get("password")

            if not auth or not email or not password:
                return CustomResponse.error(
                    message="Missing email or password", status_code=401
                )

            user = self.user_service.check_user_existance(email=email)
            if user is None:
                return CustomResponse.error(
                    message="Could not verify, User does not exist", status_code=401
                )

            if self.user_service.check_user_password(user, password):
                token = generate_jwt(user)
                return CustomResponse.success(data={"token": token})

            return CustomResponse.error(
                message="Could not verify, Incorrect password", status_code=403
            )
        except Exception as e:
            return CustomResponse.error(
                message="Internal server error", status_code=500, exception=e
            )
