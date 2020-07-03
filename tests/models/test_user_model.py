import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app
from . import db

from models.user import UserModel

@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestUser:
    def test_get_user(self):
        admin = UserModel.get_by_cpf("23666513840")
        assert admin.email == 'matheus.milani21+user@gmail.com'
        assert admin.cpf == '23666513840'

        admin = UserModel.get_by_email("matheus.milani21+user@gmail.com")
        assert admin.email == 'matheus.milani21+user@gmail.com'
        assert admin.cpf == '23666513840'

        wrong_user = UserModel.get_by_cpf("11111111")
        assert wrong_user == None

    def test_authenticate_correct_user(self):
        authenticate = UserModel.authenticate('matheus.milani21+user@gmail.com', 'teste@1234')
        assert authenticate == UserModel.query.filter_by(email='matheus.milani21+user@gmail.com').first()

        authenticate = UserModel.authenticate('reseller@gmail.com', 'teste@1234')
        assert authenticate == UserModel.query.filter_by(email='reseller@gmail.com').first()

    def test_no_authenticate_wrong_user(self):
        authenticate = UserModel.authenticate('wrong_user@wrong_user.com', '1234')
        assert authenticate is None

    def test_no_authenticate_wrong_password(self):
        authenticate = UserModel.authenticate('matheus.milani21+user@gmail.com', 'wrong-pass')
        assert authenticate is None

    def test_save_user(self):
        users = len(UserModel.list())

        new_user = UserModel()
        new_user.name = "Teste"
        new_user.cpf = "1234567890"
        new_user.email = "teste@gmail.com"
        new_user.password = "teste@1234"
        new_user.address = "Endereço 01"
        new_user.city = "Cidade 01"
        new_user.country = "País 01"
        new_user.cep_code = "000000-000"
        new_user.role = 2
        new_user.save()

        assert users + 1 == len(UserModel.list())

    def test_delete_user(self):
        users = len(UserModel.list())

        user = UserModel.delete(2)

        assert users - 1 == len(UserModel.list())
