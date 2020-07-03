from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.product import OrderModel
from resources import require_roles
from os import environ

class OrderResource(Resource):
    @require_roles('admin', 'common')
    def get(self):
        current_user = jwt.decode(request.headers['Authorization'], environ.get('JWT_SECRET_KEY'), options={'verify_exp': False})

        if Roles().enum_to_name(current_user['sub']['role']) == 'admin':
            if 'id' in request.args:
                item = OrderModel.get(request.args['id'])
                item = serialize_model(item)
                return item
            elif 'id_user' in request.args:
                itens = OrderModel.list_by_user(request.args['id_user'])
                itens = serialize_model_list(itens)
                return item
            list = OrderModel.list()
            return serialize_model_list(list)
        else:
            if 'id' in request.args:
                item = OrderModel.get(request.args['id'])
                if item.id_user == current_user['sub']['id']:
                    item = serialize_model(item)
                    return item
                else:
                    return "You don't have access", 500
            else:
                itens = OrderModel.list_by_user(current_user['sub']['id'])
                itens = serialize_model_list(itens)
                return itens

    @require_roles('admin', 'common')
    def post(self):
        try:
            data = request.get_json()
            item = OrderModel()

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.save()

            return "success", 201
        except:
            return "error", 401

    @require_roles('admin')
    def put(self):

        try:
            data = request.get_json()
            item = OrderModel.get(data['id'])

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.update()

            return "success", 201
        except:
            return "error", 401
