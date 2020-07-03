from urllib.request import urlopen
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app, app, client
import pytest
import json


@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestEndpoint:
    def test_non_exists_endpoint(self, client):
        res = client.get('/usernonblah')

        assert res.status_code == 404

    def test_endpoint_without_authorization(self, client):
        res = client.get('/api/user')

        assert res.status_code == 403

    def test_wrong_authentication_none_email(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': '',
                'password': '1234'})
        access_decode = json.loads(auth.data.decode())

        assert access_decode['message'] == 'No Email'
        assert auth.status_code == 401

    def test_wrong_authentication_none_password(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'asd',
                'password': ''})
        access_decode = json.loads(auth.data.decode())

        assert access_decode['message'] == 'No Password'
        assert auth.status_code == 401

    def test_wrong_authentication(self, client):
        auth = client.post(
            '/api/authentication',
            json={
                'email': 'asd',
                'password': 'asd'})
        access_decode = json.loads(auth.data.decode())

        assert access_decode['message'] == 'Invalid credentials'
        assert auth.status_code == 401
