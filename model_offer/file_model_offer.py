from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_config import db

class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    order_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)

    def make_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }