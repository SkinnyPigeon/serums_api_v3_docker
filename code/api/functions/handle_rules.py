from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path
import json

project_folder = os.path.expanduser('~/code/api/')
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.getenv('PASSWORD')

def hospital_rule_picker(hospital):
    if hospital == 1:
        hospital = 'fcrb'
    elif hospital == 2:
        hospital = 'ustan'
    elif hospital == 3:
        hospital = 'zmc'
    connection = setup_connection(hospital)
    rule_table = select_rule_table(connection)
    return connection, rule_table

def setup_connection(hospital):
    metadata = MetaData(schema=hospital)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:5434/source'.format(PASSWORD))
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {'base': Base, 'metadata': metadata, 'engine': engine, 'session': session}

def select_rule_table(connection):
    tables = connection['metadata'].sorted_tables
    for table in tables:
        if table.name == 'patient_rules':
            return table

def add_rule_to_hospital_db(req_data):
    hospital = req_data['hospital_id']
    rule_id = req_data['rule_id']
    tags = req_data['tags']
    filters = req_data['filters']

    connection, rule_table = hospital_rule_picker(hospital)

    try:
        rule_to_add = {"rule_id": rule_id, "tags": tags, "filters": filters}
        add_query = insert(rule_table).values(rule_to_add)
        result = connection['engine'].execute(add_query)
        connection['engine'].dispose()
        return json.dumps({"Result": "Success"})
    except:
        connection['engine'].dispose()
        return json.dumps({"Result": "Error"})