from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestProductResource:
    def test_admin_get_product_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_admin_get_product_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product?id=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_get_product_by_provider(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product?id_provider=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_admin_post_product(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.post(
            '/api/product',
            json={
                'name': 'teste',
                'id_provider': 1,
                'quantity': 200,
                'price': 20.0,
                'available': True
                },
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 201

    def test_admin_delete_product(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+user@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.delete(
            '/api/product?id=999',
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
            '/api/product',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 401


    def test_common_get_product_endpoint(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200

    def test_common_get_product_by_id(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product?id=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None

    def test_common_get_product_by_provider(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'matheus.milani21+common@gmail.com',
                'password': 'teste@1234'})
        access_decode = json.loads(auth.data.decode())

        res = client.get(
            '/api/product?id_provider=1',
            headers={
                'Authorization': access_decode['token']})

        assert res.status_code == 200
        assert res.data != None
