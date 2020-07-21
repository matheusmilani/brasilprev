# Proposal
You've been invited to take a challenge for a back-end Python developer job. We want to evaluate your code quality, analysis capacity, problem solving and especially your creativity.

Create a REST API for a similar online store. This store must have a register of its customers, products and orders. Feel free to choose how to use the system architecture, as well as the structures you use.


# Technologies used
The Flask framework was used to create the system, using a local sqlite3 bank, however it can be exchanged for any bank of the user's preference, provided it is SQL or similar (SQL, PostgreSQL, Oracle, MariaDB, etc.).

For the tests, the pytest library was used, with 62 tests, comprising unit and integration tests.

For the login system, JWT is used in a simple way. The key is in the folder \"environments\".

The system has password recovery. If you want to activate it, you must enter the correct data in the \"environment\". In order to test, AWS SES was used with real emails inside and outside the sandbox.

# The system includes
- Simple profiling
- Login
- Password recovery
- User CRUD
- Product CRUD
- Provider CRUD
- Order CRUS

# Information Flow
## Admin

The admin is responsible for:
- register users
- view users
- edit users
- delete users
- register products
- view products
- edit products
- exclude products
- register suppliers
- view suppliers
- edit suppliers
- exclude suppliers
- register orders
- view orders
- edit orders
- delete orders

## Common user
The common user is responsible for:
- view products
- view your own orders
- register orders


# System initialization
To boot the system, you need:
- Python 3.7 ou higher
- SQL Database or similar

## Installation
As a recommendation, I suggest creating a virtual env to avoid messing up the Python OS and default installation folder.

To install the dependencies, use:
> pip install -r requirements.txt

[Run](run.jpg)

Remember to update the environment with your preferred credentials.


## Run
To run, use:
> flask run

or:
> python application.py

After running the system, make a request for any URL, this consolidates the database.
I emphasize that for the first case, the tables will be created automatically together with the bank seeds to initialize the project.


# Tests
A total of 62 unit and integration tests were carried out to validate the system's actions, with 87% coverage.

[Tests](tests.jpg)
[Coverage](cov.jpg)

To run the tests, use:
> pytest tests\\models tests\\resources tests\\helpers --disable-pytest-warnings -v

# URLs

The system is hosted on AWS, through the URL:
http://brasilprevtest-env.eba-pg2t7qem.us-east-1.elasticbeanstalk.com/

As a single caveat, due to cost reasons, email sending is disabled.
If you want to test, please, inform in advance by email:
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
    List by ID:
    >'id': <id:Integer>

    List by email:
    >'email': '<email:String>'

    List by cpf:
    >'cpf': '<cpf:String>'

    List all users:
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
    List by ID:
    >'id': <id:Integer>

    List by id_user:
    >'id_user': <id_user:Integer>

    List all orders:
    > Sem parâmetros

* POST:
    >{    
    >'id_user': <id_user:Integer>,
    >'products': <products:ListObject>
    >}

    To products list:
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
    List by ID:
    >'id': <id:Integer>

    List by email:
    >'email': '<email:String>'

    List by cnpj:
    >'cnpj': '<cnpj:String>'

    List all providers:
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
    List by ID:
    > 'id': <id:Integer>

    List by ID_PROVIDER:
    > 'id_provider': <id_provider:Integer>

    List all products:
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
