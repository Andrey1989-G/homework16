from flask_config import db
from model_user.file_model_user import User
from model_order.file_model_order import Order
from model_offer.file_model_offer import Offer
from flask import jsonify


class Utils:
    def get_all(self, data_with_users):
        """
        принимает модель
        :param data_with_users: модель
        :return: список со словарем(экземплярами модели)
        """
        lst = []
        res = db.session.query(data_with_users).all()
        for i in res:
            lst.append(i.make_dict())
        return lst

    def get_by_id(self, data_with_users, numb_id):
        """
        принимает модуль, номер инт
        :param data_with_users:
        :param numb_id:
        :return:
        """
        lst = []
        res = db.session.query(data_with_users).all()
        for i in res:
            if i.make_dict()['id'] == numb_id:
                lst.append(i.make_dict())
        return lst

    def add_data_bd(self, model, data):
        """
        добавляем пользователя
        :param model: модель
        :param data: значения для колумнс модели
        :return: нон(происходит запись в БД)
        """
        res = model(**data)
        db.session.add(res)
        db.session.commit()

    def update_data_bd(self, model, data, id):
        """
        обновляем данные
        :param model:
        :param data:
        :param id:
        :return:
        """
        upd = model.query.get(id)
        upd.all = data
        db.session.add(upd)
        db.session.commit()

    def delete_data_in_bd(self, model, id):
        """
        удаляем данные
        :param model:
        :param id:
        :return:
        """
        res = model.query.get(id)
        db.session.delete(res)
        db.session.commit()



# res = Utils()
# print(res.get_all(User))
# print(res.get_by_id(User, 1))