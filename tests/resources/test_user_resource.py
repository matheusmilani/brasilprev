from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestUserResource:
    def test_admin_authentication(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})

        access_decode = json.loads(auth.data.decode())

        assert access_decode['name'] == "Matheus D'Adamo Milani"

    def test_admin_get_user_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/user',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_admin_get_user_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/user?id=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_user_by_cpf(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/user?cpf=23666513840',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_user_by_email(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/user?email=matheus.milani21+user@gmail.com',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_post_user(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/user',
            json={
                'email': 'matheus.milani21+user_novo@gmail.com',
                'name': 'teste',
                'role': 'admin',
                'cpf': '01340534002',
                'address': 'Endereço',
                'city': 'Endereço',
                'country': 'Endereço',
                'cep_code': 'Endereço',
                'password': 'teste@1234'
                },
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 201

    def test_admin_delete_user(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.delete(
            '/api/user?id=999',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 201

        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.delete(
            '/api/user',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401

    def test_admin_post_user_with_duplicate_cpf_or_email_params(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/user',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'name': 'teste',
                'role': 'admin',
                'cpf': '236.66513840'},
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401
        assert res.data == b'"CPF incorreto"\n'

        res = client.post(
            '/api/user',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'name': 'teste',
                'role': 'admin',
                'cpf': '23666513849'},
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401
