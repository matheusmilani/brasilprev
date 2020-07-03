from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
from models.user import UserModel
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestAuthenticationResource:
    def test_admin_authentication(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})

        access_decode = json.loads(auth.data.decode())

        assert access_decode['name'] == "Matheus D'Adamo Milani"

    def test_common_authentication(self, client):
        new_user = UserModel()
        new_user.name = "Matheus D'Adamo Milani Comum"
        new_user.cpf = "23666513840"
        new_user.email = "matheus.milani21+common@gmail.com"
        new_user.password = "teste@1234"
        new_user.address = "Endereço 01"
        new_user.city = "Cidade 01"
        new_user.country = "País 01"
        new_user.cep_code = "000000-000"
        new_user.role = 2
        new_user.save()

        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})

        access_decode = json.loads(auth.data.decode())

        assert access_decode['name'] == "Matheus D'Adamo Milani Comum"
