from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.user import UserModel
from resources import require_roles
import re

class UserResource(Resource):
    @require_roles('admin')
    def get(self):
        if 'id' in request.args:
            item = UserModel.get(request.args['id'])
            item = serialize_model(item)
            return item
        elif 'email' in request.args:
            item = UserModel.get_by_email(request.args['email'])
            item = serialize_model(item)
            return item
        elif 'cpf' in request.args:
            item = UserModel.get_by_cpf(request.args['cpf'])
            item = serialize_model(item)
            return item
        list = UserModel.list()
        return serialize_model_list(list)

    @require_roles('admin')
    def post(self):
        try:
            data = request.get_json()
            item = UserModel()

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
            item = UserModel.get(data['id'])

            for parameter in data:
                setattr(item, parameter, data[parameter])
            item.update()

            return "success", 201
        except:
            return "error", 401

    @require_roles('admin')
    def delete(self):
        try:
            if 'id' in request.args:
                item = UserModel.delete(request.args['id'])
                return "success", 201
            return "No ID", 401
        except:
            return "error", 401
