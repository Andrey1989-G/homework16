import json
from model_order.file_model_order import Order

from flask_config import db
from model_offer.file_model_offer import Offer
from model_user.file_model_user import User


def load_json(path):
    """
    загружаем джейсон файл
    пример пути path = 'model_offer/data/data_offer.json'
    :param path: путь
    :return: +
    """
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def insert_data_user(data):
    """
    загрузка юзеров в бд
    :param data: 
    :return: 
    """""
    for i in data:
        db.session.add(User(
            id=i.get("id"),
            first_name=i.get("first_name"),
            last_name=i.get("last_name"),
            age=i.get("age"),
            users_email=i.get("email"),
            role=i.get("role"),
            phone=i.get("phone")
        ))
        db.session.commit()


def insert_data_order(data):
    """
    загрузка заказов в бд
    :param data:
    :return:
    """
    for i in data:
        db.session.add(Order(
            id=i.get("id"),
            name=i.get("name"),
            description=i.get("description"),
            start_date=i.get("start_date"),
            end_date=i.get("end_date"),
            address=i.get("address"),
            price=i.get("price"),
            customer_id=i.get("customer_id"),
            executor_id=i.get("executor_id")
        ))
        db.session.commit()


def insert_data_offer(data):
    """
    загрузка офферов в бд
    :param data:
    :return:
    """
    for i in data:
        db.session.add(Offer(
            id=i.get("id"),
            order_id=i.get("order_id"),
            executor_id=i.get("executor_id")
        ))
        db.session.commit()


#заполняем БД
def fill_db():
    insert_data_user(load_json('model_user/data/data_user.json'))
    insert_data_offer(load_json('model_offer/data/data_offer.json'))
    insert_data_order(load_json('model_order/data/data_order.json'))

db.create_all()
fill_db()


