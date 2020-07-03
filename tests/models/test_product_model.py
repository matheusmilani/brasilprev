import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app
from . import db

from models.product import ProductModel
from models.provider import ProviderModel

@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestProduct:
    def test_get_product(self):
        product = ProductModel.get(1)
        assert product.name == 'Produto 01'

        products = ProductModel.list()
        assert len(products) == 1
        assert type(products) == type([])

    def test_save_product(self):
        products = len(ProductModel.list())

        new_product = ProductModel()
        new_product.name = "Produto 02"
        new_product.provider = ProviderModel.get_by_cnpj("04790618000153")
        new_product.quantity = 100
        new_product.price = 10.0
        new_product.available = True
        new_product.save()

        assert products + 1 == len(ProductModel.list())

    def test_update_product(self):
        product = ProductModel.get(2)
        product.name = "Produto 02 editado"
        product.quantity = 0
        product.price = 50.0
        product.available = False
        product.update()

        assert product.name == "Produto 02 editado"
        assert product.available == False

    def test_delete_product(self):
        products = len(ProductModel.list())

        product = ProductModel.delete(2)

        assert products - 1 == len(ProductModel.list())
