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
