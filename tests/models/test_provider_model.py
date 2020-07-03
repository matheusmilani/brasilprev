import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import create_test_app
from . import db

from models.provider import ProviderModel

@pytest.fixture(scope="session", autouse=True)
def before_all():
    create_test_app()


class TestProvider:
    def test_get_provider(self):
        provider = ProviderModel.get(1)
        assert provider.name == 'Fornecedor 01'

        provider = ProviderModel.get_by_cnpj('04790618000153')
        assert provider.name == 'Fornecedor 01'

        providers = ProviderModel.list()
        assert len(providers) == 1
        assert type(providers) == type([])

    def test_save_provider(self):
        providers = len(ProviderModel.list())

        new_provider = ProviderModel()
        new_provider.name = "Fornecedor 02"
        new_provider.cnpj = "98617744000154"
        new_provider.address = "Endereço 02"
        new_provider.city = "Cidade 02"
        new_provider.country = "País 02"
        new_provider.cep_code = "000000-000"
        new_provider.responsible_name = "Matheus D'Adamo Milani 01"
        new_provider.responsible_email = "matheus.milani21+provider+01@gmail.com"
        new_provider.responsible_phone = "+55(11)97717-8888"
        new_provider.active = True
        new_provider.save()

        assert providers + 1 == len(ProviderModel.list())

    def test_update_provider(self):
        provider = ProviderModel.get_by_cnpj('98617744000154')
        provider.name = "Fornecedor 02 editado"
        provider.update()

        assert provider.name == "Fornecedor 02 editado"

    def test_delete_provider(self):
        providers = len(ProviderModel.list())

        provider = ProviderModel.delete(2)

        assert providers - 1 == len(ProviderModel.list())
