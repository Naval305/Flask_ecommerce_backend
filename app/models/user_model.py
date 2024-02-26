from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)
    is_staff = db.Column(db.Boolean, default=False)
    # fb_token = db.Column(db.String(100), nullable=True)
    # twitter_token = db.Column(db.String(100), nullable=True)
    # google_token = db.Column(db.String(100), nullable=True)

    # Define a property for the full name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Define a method to set the password securely using hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(str(password))

    # Define a method to check the password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
