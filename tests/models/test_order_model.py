import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app
from . import db

from models.order import OrderModel
from models.product import ProductModel
from models.user import UserModel

@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestOrder:
    def test_get_product(self):
        order = OrderModel.get(1)
        assert order != None

        orders = OrderModel.list()
        assert len(orders) == 1
        assert type(orders) == type([])

    def test_save_order(self):
        orders = len(OrderModel.list())

        new_order = OrderModel()
        new_order.user = UserModel.get_by_cpf("23666513840")
        new_order.products = str({"id": 1, "quantity": 100})
        new_order.save()

        assert orders + 1 == len(OrderModel.list())

    def test_update_order(self):
        order = OrderModel.get(2)
        order.status = 2
        order.update()

        assert order.status == 2

    def test_delete_order(self):
        orders = len(OrderModel.list())

        order = OrderModel.delete(2)

        assert orders - 1 == len(OrderModel.list())
