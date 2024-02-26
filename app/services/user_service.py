from flask import current_app

from app.models.user_model import User
from app.app import db


class UserService:
    @staticmethod
    def create_user(first_name, last_name, email, password):
        new_user = User(first_name=first_name, last_name=last_name, email=email)

        new_user.set_password(password)

        with current_app.app_context():
            db.session.add(new_user)
            db.session.commit()
            id = new_user.id

        return id

    @staticmethod
    def get_users():
        return User.query.all()
