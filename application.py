from dotenv import load_dotenv
from flask import Flask
from models import initialize_database
from os import environ
from resources import initialize_resources
from schema.schema_file import Schema
from sqlalchemy import create_engine

# Starting Flask application
application = Flask(__name__)

# Loading environment variables from .env file only in development
if environ.get('EBS_ENVIRONMENT') in ['local', None]:
    load_dotenv('./environments/local.env')

# Loading environment variables into Flask application
for item in environ.items():
    application.config[item[0]] = item[1]

# Starting database configuration
initialize_database(application)

# Starting RESTful endpoints
initialize_resources(application)

@application.before_first_request
def startup():
    print("Initializing migration DB")

    Schema.migration()
    Schema.prepare_db()

# Run application
if __name__ == '__main__':
    application.run(threaded=True)
