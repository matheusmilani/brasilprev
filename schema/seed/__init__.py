from models.user import UserModel
from models.provider import ProviderModel
from models.product import ProductModel

def first_user():
    if UserModel.get_by_cpf("23666513840") != None:
        return
    new_user = UserModel()
    new_user.name = "Matheus D'Adamo Milani"
    new_user.cpf = "23666513840"
    new_user.email = "matheus.milani21+user@gmail.com"
    new_user.password = "teste@1234"
    new_user.role = 1
    new_user.save()
    return

def first_provider():
    if ProviderModel.get_by_cnpj("04790618000153") != None:
        return
    new_provider = ProviderModel()
    new_provider.name = "Fornecedor 01"
    new_provider.cnpj = "04790618000153"
    new_provider.address = "Endereço 01"
    new_provider.city = "Cidade 01"
    new_provider.country = "País 01"
    new_provider.cep_code = "000000-000"
    new_provider.responsible_name = "Matheus D'Adamo Milani"
    new_provider.responsible_email = "matheus.milani21+provider@gmail.com"
    new_provider.responsible_phone = "+55(11)97717-9999"
    new_provider.active = True
    new_provider.save()
    return

def first_product():
    if ProviderModel.get_by_cnpj("04790618000153") == None:
        first_provider()
        return
    new_product = ProductModel()
    new_product.name = "Produto 01"
    new_product.provider = ProviderModel.get_by_cnpj("04790618000153")
    new_product.quantity = 100
    new_product.price = 10.0
    new_product.available = True
    new_product.save()
    return
