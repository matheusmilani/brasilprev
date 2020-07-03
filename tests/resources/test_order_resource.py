from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestOrderResource:
    def test_admin_get_order_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_admin_get_order_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order?id=1',
            headers={
                'Authorization': access_decode['token']})
        print(res.data)
        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_order_by_user(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order?id_user=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_post_order(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/order',
            json={
                'id_user': 1,
                'products': [{"id": 1, "quantity": 10}],
                },
            headers={
                'Authorization': access_decode['token']})
        print(res.data)
        assert res.status_code == 201

    def test_common_get_order_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_common_post_order(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/order',
            json={
                'id_user': 2,
                'products': [{"id": 1, "quantity": 10}],
                },
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 201

    def test_common_get_order_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order?id=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401
        assert str(res.data) == str(b'"You don\'t have access"\n')

    def test_common_get_self_order_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/order',
            headers={
                'Authorization': access_decode['token']})
        self_order = eval(res.data.decode())[0]
        print(self_order)
        res_1 = client.get(
            '/api/order?id=' + str(self_order['id']),
            headers={
                'Authorization': access_decode['token']})

        assert res_1.status_code == 200
