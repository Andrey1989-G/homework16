from flask import Flask, request, render_template, jsonify
from folder_class_utils.file_class_utils import Utils
from model_user.file_model_user import User
from model_order.file_model_order import Order
from model_offer.file_model_offer import Offer
from flask_config import app



@app.route('/users/<int:id_user>')
def page_users_by_id(id_user):
    res = Utils()
    return jsonify(res.get_by_id(User, id_user))

@app.route('/users/')
def page_all_users():
    res = Utils()
    return jsonify(res.get_all(User))

@app.route('/orders/<int:id_order>')
def page_orders_by_id(id_order):
    return jsonify(Utils.get_by_id(Order, id_order))

@app.route('/orders/')
def page_all_orders():
    return jsonify(Utils.get_all(Order))

@app.route('/offers/<int:id_offer>')
def page_offers_by_id(id_offer):
    return jsonify(Utils.get_by_id(Offer, id_offer))

@app.route('/offers/')
def page_all_offers():
    return jsonify(Utils.get_all(Offer))

# для юзеров

@app.route("/users/", methods=['POST'])
def page_users_upload():
    """
    создание пользователя(в хтмл должны быть соответствующие формы)
    :return:
    """
    content = request.form['content']
    result = Utils.add_data_bd(User, content)
    return "Пользователь создан"

@app.route("/user/<int:id>", methods=['PUT'])
def page_user_update(id):
    """
    обновляем данные. Должны быть все соответствующие поля в хтмл
    :param id:
    :return:
    """
    content = request.form['content']
    res = Utils.update_data_bd(User, content, id)
    return "Пользователь обновлён"

@app.route("/user/<int:id>", methods=['DELETE'])
def page_user_delete(id):
    """Страница удаления пользователя"""
    Utils.delete_data_in_bd(User, id)
    return "Пользователь обновлён"

# для офферов

@app.route("/offers/", methods=['POST'])
def page_offers_upload():
    """
    создание пользователя(в хтмл должны быть соответствующие формы)
    :return:
    """
    content = request.form['content']
    result = Utils.add_data_bd(Offer, content)
    return "Пользователь создан"

@app.route("/offer/<int:id>", methods=['PUT'])
def page_offer_update(id):
    """
    обновляем данные. Должны быть все соответствующие поля в хтмл
    :param id:
    :return:
    """
    content = request.form['content']
    res = Utils.update_data_bd(Offer, content, id)
    return "Пользователь обновлён"

@app.route("/offer/<int:id>", methods=['DELETE'])
def page_offers_delete(id):
    """Страница удаления пользователя"""
    Utils.delete_data_in_bd(Offer, id)
    return "Пользователь обновлён"

#для ордеров

@app.route("/orders/", methods=['POST'])
def page_orders_upload():
    """
    создание пользователя(в хтмл должны быть соответствующие формы)
    :return:
    """
    content = request.form['content']
    result = Utils.add_data_bd(Order, content)
    return "Пользователь создан"

@app.route("/orders/<int:id>", methods=['PUT'])
def page_orders_update(id):
    """
    обновляем данные. Должны быть все соответствующие поля в хтмл
    :param id:
    :return:
    """
    content = request.form['content']
    res = Utils.update_data_bd(Order, content, id)
    return "Пользователь обновлён"

@app.route("/order/<int:id>", methods=['DELETE'])
def page_orders_delete(id):
    """Страница удаления пользователя"""
    Utils.delete_data_in_bd(Order, id)
    return "Пользователь обновлён"


if __name__ == '__main__':
    app.run(debug=True)
