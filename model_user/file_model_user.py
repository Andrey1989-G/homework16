from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_config import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    users_email = db.Column(db.String(300))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def make_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.users_email,
            "role": self.role,
            "phone": self.phone
        }




