from flask import Flask, request, render_template, jsonify
from folder_class_utils.file_class_utils import Utils
from model_user.file_model_user import User
from model_order.file_model_order import Order
from model_offer.file_model_offer import Offer
from flask_config import app


# для пользователей после ревью

@app.route('/user/<int:id_user>', methods=['GET', 'PUT', 'DELETE'])
def page_users_by_id(id_user):
    """
    в зависимости от запроса
    показываем пользователя по айди, либо
    обновляем данные либо,
    удаляем пользователя
    :param id_user:
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_by_id(User, id_user))
    elif request.method == 'PUT':
        content = request.form['content']
        res = Utils().update_data_bd(User, content, id_user)
        return "Пользователь обновлён"
    else:
        Utils().delete_data_in_bd(User, id_user)
        return "Пользователь удален"


@app.route("/users/", methods=['GET', 'POST'])
def page_all_users():
    """
    в зависимости от запроса
    показываем всех пользователей, либо
    создаем пользователя
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_all(User))
    else:
        content = request.json
        res = Utils().add_data_bd(User, content)
        return "Пользователь создан"


# для заказов после ревью

@app.route('/order/<int:id_order>', methods=['GET', 'PUT', 'DELETE'])
def page_order_by_id(id_order):
    """
    в зависимости от запроса
    показываем заказ по айди, либо
    обновляем данные, либо
    удаляем заказ
    :param id_order:
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_by_id(Order, id_order))
    elif request.method == 'PUT':
        content = request.json
        res = Utils().update_data_bd(Order, content, id_order)
        return "Заказ обновлён"
    else:
        Utils().delete_data_in_bd(Order, id_order)
        return "Заказ удален"


@app.route("/orders/", methods=['GET', 'POST'])
def page_all_orders():
    """
    в зависимости от запроса
    показываем все заказы, либо
    создаем заказ
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_all(Order))
    else:
        content = request.json
        res = Utils().add_data_bd(Order, content)
        return "Заказ создан"


# для предложений после ревью

@app.route('/order/<int:id_offer>', methods=['GET', 'PUT', 'DELETE'])
def page_offer_by_id(id_offer):
    """
    в зависимости от запроса
    показываем предложение по айди, либо
    обновляем данные, либо
    удаляем предложение
    :param id_offer:
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_by_id(Offer, id_offer))
    elif request.method == 'PUT':
        content = request.json
        res = Utils().update_data_bd(Offer, content, id_offer)
        return "Предложение обновлено"
    else:
        Utils().delete_data_in_bd(Offer, id_offer)
        return "Предложение удалено"


@app.route("/offers/", methods=['GET', 'POST'])
def page_all_offers():
    """
    в зависимости от запроса
    показываем все предложения, либо
    создаем предложение
    :return:
    """
    if request.method == "GET":
        res = Utils()
        return jsonify(res.get_all(Offer))
    else:
        content = request.json
        res = Utils().add_data_bd(Offer, content)
        return "Предложение создано"


# ----------------------------------------------------------------

#
# @app.route('/order/<int:id_order>')
# def page_orders_by_id(id_order):
#     return jsonify(Utils.get_by_id(Order, id_order))
#
# @app.route('/orders/')
# def page_all_orders():
#     return jsonify(Utils.get_all(Order))
#
# @app.route('/offer/<int:id_offer>')
# def page_offers_by_id(id_offer):
#     return jsonify(Utils.get_by_id(Offer, id_offer))
#
# @app.route('/offers/')
# def page_all_offers():
#     return jsonify(Utils.get_all(Offer))
#
# # для юзеров
#
# # @app.route("/users/", methods=['POST'])
# # def page_users_upload():
# #     """
# #     создание пользователя(в хтмл должны быть соответствующие формы)
# #     :return:
# #     """
# #     content = request.form['content']
# #     result = Utils.add_data_bd(User, content)
# #     return "Пользователь создан"
#
# # @app.route("/user/<int:id>", methods=['PUT'])
# # def page_user_update(id):
# #     """
# #     обновляем данные. Должны быть все соответствующие поля в хтмл
# #     :param id:
# #     :return:
# #     """
# #     content = request.form['content']
# #     res = Utils.update_data_bd(User, content, id)
# #     return "Пользователь обновлён"
# #
# # @app.route("/user/<int:id>", methods=['DELETE'])
# # def page_user_delete(id):
# #     """Страница удаления пользователя"""
# #     Utils.delete_data_in_bd(User, id)
# #     return "Пользователь обновлён"
#
# # для офферов
#
# @app.route("/offers/", methods=['POST'])
# def page_offers_upload():
#     """
#     создание пользователя(в хтмл должны быть соответствующие формы)
#     :return:
#     """
#     content = request.form['content']
#     result = Utils.add_data_bd(Offer, content)
#     return "Пользователь создан"
#
# @app.route("/offer/<int:id>", methods=['PUT'])
# def page_offer_update(id):
#     """
#     обновляем данные. Должны быть все соответствующие поля в хтмл
#     :param id:
#     :return:
#     """
#     content = request.form['content']
#     res = Utils.update_data_bd(Offer, content, id)
#     return "Пользователь обновлён"
#
# @app.route("/offer/<int:id>", methods=['DELETE'])
# def page_offers_delete(id):
#     """Страница удаления пользователя"""
#     Utils.delete_data_in_bd(Offer, id)
#     return "Пользователь удален"
#
# #для ордеров
#
# @app.route("/orders/", methods=['POST'])
# def page_orders_upload():
#     """
#     создание пользователя(в хтмл должны быть соответствующие формы)
#     :return:
#     """
#     content = request.form['content']
#     result = Utils.add_data_bd(Order, content)
#     return "Пользователь создан"
#
# @app.route("/orders/<int:id>", methods=['PUT'])
# def page_orders_update(id):
#     """
#     обновляем данные. Должны быть все соответствующие поля в хтмл
#     :param id:
#     :return:
#     """
#     content = request.form['content']
#     res = Utils.update_data_bd(Order, content, id)
#     return "Пользователь обновлён"
#
# @app.route("/order/<int:id>", methods=['DELETE'])
# def page_orders_delete(id):
#     """
#     страни
#     :param id:
#     :return:
#     """
#     Utils.delete_data_in_bd(Order, id)
#     return "Пользователь обновлён"


if __name__ == '__main__':
    app.run(debug=True)
