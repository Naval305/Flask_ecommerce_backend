from datetime import datetime, timedelta

import jwt
from flask import current_app

from app.services.user_service import UserService


def validate_user_data(data):
    required_fields = ["first_name", "last_name", "email", "password"]
    if not all(field in data for field in required_fields):
        return {"message": "Missing required fields"}, 400

    if UserService().check_user_existance(data["email"]):
        return {"message": "Email address already in use"}, 400

    return None


def generate_jwt(user):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    payload = {
        'identity': user.id,
        'email': user.email,
        'exp': expiration_time
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
