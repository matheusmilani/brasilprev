# Proposta
Você foi convidado a realizar um desafio para a vaga de desenvolvedor(a) back-end Python. Queremos avaliar sua qualidade de código, capacidade de análise, resolução de problemas e principalmente sua criatividade.

Construa uma API REST para simular uma loja virtual. Esta loja deve ter um cadastro de seus clientes, produtos e pedidos. Fique à vontade para escolher como fará a arquitetura do sistema, bem como frameworks que utilizará.


# Tecnologias utilizadas
Foi utilizado o framework Flask para a criação do sistema, utilizando banco local sqlite3, porém pode ser trocado por qualquer banco da preferência do usuário desde que seja SQL ou similar (SQL, PostgreSQL, Oracle, MariaDB, etc).

Para os testes foi utilizada a biblioteca pytest, com o total de 62 testes, sendo compostos por testes unitários e de integração.

Para o sistema de login é utilizado JWT de forma simples. A chave encontra-se na pasta \"environments\".

O sistema possui recuperação de senha. Caso queira ativá-lo, deve-se inserir os dados corretos no \"environment\". Afim de teste foi utilizado o SES da AWS com emails reais dentro e fora da sandbox.

# O sistema contempla
- Perfilamento simples
- Login
- Recuperação de senha
- CRUD de usuário
- CRUD de produtos
- CRUD de fornecedores
- CRU de pedidos

# Fluxo de Informação
## Admin

O admin é responsável por:
- cadastrar usuários
- visualizar usuários
- editar usuários
- excluir usuários
- cadastrar produtos
- visualizar produtos
- editar produtos
- excluir produtos
- cadastrar fornecedores
- visualizar fornecedores
- editar fornecedores
- excluir fornecedores
- cadastrar pedidos
- visualizar pedidos
- editar pedidos
- excluir pedidos

## Usuário comum
O usuário comum é responsável por:
- visualizar produtos
- visualizar os próprios pedidos
- cadastrar pedidos


# Inicialização do sistema
Para inicializar o sistema, é necessário:
- Python 3.7 ou superior
- Banco SQL ou similar (caso queira usar sqlite3, apenas não altere o environment)

## Instalação
Como recomendação, sugiro a criação de uma virtual env para não sujar o SO e a pasta de instalação padrão do Python.

Para instalar as dependências, use:
> pip install -r requirements.txt

[Run](run.jpg)

Lembre-se de atualizar o environment com as credenciais de sua preferência


## Run
Para rodar o sistema, use:
> flask run

ou caso queira:
> python application.py

Após rodar o sistema, faça uma requisição para qualquer URL, isso consolida a database.
Ressalto que para o primeiro caso, as tabelas serão criadas automaticamente junto com as seeds de banco para inicializar o projeto.


# Tests
Foram feitos no total de 62 testes unitários e de integração para validar as ações do sistema, com cobertura de 87%.

[Tests](tests.jpg)
[Coverage](cov.jpg)

Para rodar os testes, use:
> pytest tests\\models tests\\resources tests\\helpers --disable-pytest-warnings -v

# URLs

O sistema está hospedado na AWS, através da URL:
http://brasilprevtest-env.eba-pg2t7qem.us-east-1.elasticbeanstalk.com/

Como única ressalva, devido a motivos de custo, o envio de email está desabilitado.
Caso queira testar, por favor, avise previamente pelo email:
matheus.milani21@gmail.com

**<URL_BASE>/api/authentication**
* POST:
    > {
    > 'email': '<email:String>',
    > 'password': '<pass:String>'
    > }


**<URL_BASE>/api/recover_password**
* GET:
    >'email': '<email:String>'

* POST:
    >{
    >'email': '<email:String>',
    >'token': '<token:String>',
    >'password': '<pass:String>'
    >}

**<URL_BASE>/api/user**
* GET:
    Listar por ID:
    >'id': <id:Integer>

    Listar por email:
    >'email': '<email:String>'

    Listar usuário por cpf:
    >'cpf': '<cpf:String>'

    Listar todos os usuário:
    > Sem parâmetros

* POST:
    >{
   >'email': '<email:String>',
   >'name': '<name:String>',
   >'role': '<role:String>',
   >'cpf': '<cpf:String>',
   >'address': '<address:String>',
   >'city': '<city:String>',
   >'country': '<country:String>',
   >'cep_code': '<cep_code:String>',
   >'password': '<pass:String>'
   >}

* PUT:
    >{
   >'id': <id:Integer>,
   >'email': '<email:String>',
   >'name': '<name:String>',
   >'role': '<role:String>',
   >'cpf': '<cpf:String>',
   >'address': '<address:String>',
   >'city': '<city:String>',
   >'country': '<country:String>',
   >'cep_code': '<cep_code:String>',
   >'password': '<pass:String>'
   >}

* DELETE:
    >'id': '<id>'


**<URL_BASE>/api/order**
* GET:
    Listar por ID:
    >'id': <id:Integer>

    Listar por id_user:
    >'id_user': <id_user:Integer>

    Listar todos os pedidos:
    > Sem parâmetros

* POST:
    >{    
    >'id_user': <id_user:Integer>,
    >'products': <products:ListObject>
    >}

    Para os produtos, segue o seguinte formato:
    >[
    >>{
    >>'id': <id:Integer>,
    >>'quantity': <quantity:Integer>,
    >>}
    >]

* PUT:
    >{  
    >'id': <id:Integer>,
    >'id_user': <id_user:Integer>,
    >'products': <products:ListObject>
    >}

**<URL_BASE>/api/provider**
* GET:
    Listar por ID:
    >'id': <id:Integer>

    Listar por email:
    >'email': '<email:String>'

    Listar usuário por cnpj:
    >'cnpj': '<cnpj:String>'

    Listar todos os fornecedores:
    > Sem parâmetros

* POST:
    >{
   >'responsible_email': '<responsible_email:String>',
   >'responsible_name': '<responsible_name:String>',
   >'responsible_phone': '<responsible_phone:String>',
   >'name': '<name:String>',
   >'cnpj': '<cnpj:String>',
   >'address': '<address:String>',
   >'city': '<city:String>',
   >'country': '<country:String>',
   >'cep_code': '<cep_code:String>'
   >}

* PUT:
    >{
   >'id': <id:Integer>,
   >'responsible_email': '<responsible_email:String>',
   >'responsible_name': '<responsible_name:String>',
   >'responsible_phone': '<responsible_phone:String>',
   >'name': '<name:String>',
   >'cnpj': '<cnpj:String>',
   >'address': '<address:String>',
   >'city': '<city:String>',
   >'country': '<country:String>',
   >'cep_code': '<cep_code:String>'
   >}

* DELETE:
    >'id': '<id>'

**<URL_BASE>/api/product**
* GET:
    Listar por ID:
    > 'id': <id:Integer>

    Listar por ID_PROVIDER:
    > 'id_provider': <id_provider:Integer>

    Listar todos os produtos:
    > Sem parâmetros

* POST:
    > {
    >'name': '<name:String>',
    >'id_provider': <id_provider:Integer>,
    >'quantity': <quantity:Integer>,
    >'price': <price:Float>,
    >'available': <available:Boolean>
    >)

* PUT:
    > {
    >'id': <id:Integer>,
    >'name': '<name:String>',
    >'id_provider': <id_provider:Integer>,
    >'quantity': <quantity:Integer>,
    >'price': <price:Float>,
    >'available': <available:Boolean>
    >)

* DELETE:
    >'id': '<id>'
