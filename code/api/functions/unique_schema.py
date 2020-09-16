from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

import os
from dotenv import load_dotenv
from pathlib import Path

project_folder = os.path.expanduser('~/code/api/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

import random
import string

def create_unique_schema_name(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    return '_' + ''.join((random.choice(letters_and_digits) for i in range(length)))

def setup_data_vault_connection(unique_schema, Base):
    class_registry = {}
    metadata = MetaData(schema=unique_schema)
    base = Base(metadata=unique_schema)
    engine = create_engine('postgresql://postgres:{}@localhost:5434/data_vault'.format(PASSWORD))
    Session = sessionmaker(bind=engine, autoflush=True, autocommit=False)
    session = Session()
    return {'base': base, 'metadata': metadata, 'engine': engine, 'session': session, 'schema': unique_schema}

def create_unique_schema(connection, schema, base):
    try:
        connection['engine'].execute(CreateSchema(schema))
        return connection, schema
    except:
        print("Trying a new schema name")
        schema = create_unique_schema_name(32)
        connection = setup_data_vault_connection(schema, base)
        create_unique_schema(connection, schema, base)
        return connection, schema