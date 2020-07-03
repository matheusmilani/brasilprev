from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestProviderResource:
    def test_admin_get_provider_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/provider',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_admin_get_provider_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/provider?id=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_provider_by_cpf(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/provider?cnpj=04790618000153',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_provider_by_email(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/provider?email=matheus.milani21+provider@gmail.com',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_post_provider(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/provider',
            json={
                'name': 'teste',
                'responsible_email': 'matheus.milani21+provider_novo@gmail.com',
                'responsible_name': 'teste',
                'responsible_phone': 'admin',
                'cnpj': '65178969000100',
                'address': 'Endereço',
                'city': 'Endereço',
                'country': 'Endereço',
                'cep_code': 'Endereço'
                },
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 201

    def test_admin_delete_provider(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.delete(
            '/api/provider?id=999',
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
            '/api/provider',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401
