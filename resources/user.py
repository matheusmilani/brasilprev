from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from helpers import *
from models.user import UserModel
from resources import require_roles
import re

class UserResource(Resource):
    def get(self):
        if 'id' in request.args:
            item = UserModel.get(request.args['id'])
            item = serialize_model(item)
            return item
        list = UserModel.list()
        return serialize_model_list(list)

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

    def delete(self):
        try:
            if 'id' in request.args:
                item = UserModel.delete(request.args['id'])
                return "success", 201
            return "No ID", 401
        except:
            return "error", 401
