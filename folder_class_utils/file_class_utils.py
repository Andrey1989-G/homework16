from flask_config import db


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

    def update_data_user(self, model, data, id):
        """
        обновляем данные пользователя
        :param model:
        :param data:
        :param id:
        :return:
        """
        upd = model.query.get(id)
        upd.first_name = data["first_name"]
        upd.last_name = data["last_name"]
        upd.age = data["age"]
        upd.email = data["email"]
        upd.role = data["role"]
        upd.phone = data["phone"]
        db.session.add(upd)
        db.session.commit()

    def update_data_order(self, model, data, id):
        """
        обновляем данные пользователя
        :param model:
        :param data:
        :param id:
        :return:
        """
        upd = model.query.get(id)
        upd.name = data["name"]
        upd.description = data["description"]
        upd.start_date = data["start_date"]
        upd.end_date = data["end_date"]
        upd.address = data["address"]
        upd.price = data["price"]
        upd.customer_id = data["customer_id"]
        upd.executor_id = data["executor_id"]
        db.session.add(upd)
        db.session.commit()

    def update_data_offer(self, model, data, id):
        """
        обновляем данные пользователя
        :param model:
        :param data:
        :param id:
        :return:
        """
        upd = model.query.get(id)
        upd.order_id = data["order_id"]
        upd.executor_id = data["executor_id"]
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
