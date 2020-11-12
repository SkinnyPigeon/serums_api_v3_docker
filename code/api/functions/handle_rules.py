from sqlalchemy import create_engine, MetaData, insert, update, and_
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path
import json

project_folder = os.path.expanduser('~/code/api_v3_docker/code/api')
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
# PASSWORD = os.environ.get('PGPASSWORD')
# PORT = os.environ.get('PGPORT')

def hospital_rule_picker(hospital):
    if hospital == 'FCRB':
        hospital = 'fcrb'
    elif hospital == 'USTAN':
        hospital = 'ustan'
    elif hospital == 'ZMC':
        hospital = 'zmc'
    connection = setup_connection(hospital)
    rule_table = select_rule_table(connection)
    return connection, rule_table

def setup_connection(hospital):
    metadata = MetaData(schema=hospital)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
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
    # filters = req_data['filters']
    serums_id = req_data['serums_id']
    connection, rule_table = hospital_rule_picker(hospital)
    try:
        rule_to_add = {"rule_id": rule_id, "tags": tags, "serums_id": serums_id}
        # rule_to_add = {"rule_id": rule_id, "tags": tags, "filters": filters, "serums_id": serums_id}
        add_query = insert(rule_table).values(rule_to_add)
        result = connection['engine'].execute(add_query)
        connection['engine'].dispose()
        return {"Result": "Success"}
    except Exception as e:
        connection['engine'].dispose()
        return e


def remove_rule_from_serums(req_data):
    rule_id = req_data['rule_id']
    hospital = req_data['hospital_id']
    connection, rule_table = hospital_rule_picker(hospital)
    try:
        rule_to_remove = rule_table.delete().where(rule_table.c.rule_id==rule_id)
        connection['session'].execute(rule_to_remove)
        connection['session'].commit()
        connection['engine'].dispose()

        return {"Result": "Success"}
    except Exception as e:
        connection['engine'].dispose()
        return e

def update_rule(req_data):
    hospital = req_data['hospital_id']
    rule_id = req_data['rule_id']
    tags = req_data['tags']
    # filters = req_data['filters']
    serums_id = req_data['serums_id']
    connection, rule_table = hospital_rule_picker(hospital)
    try:
        stmt = rule_table.update().where(rule_table.c.rule_id == rule_id).where(rule_table.c.serums_id == serums_id).values(tags=tags)
        print(stmt)
        connection['engine'].execute(stmt)
        connection['engine'].dispose()
        return {"Result": "Success"}
    except Exception as e:
        print(e)
        connection['engine'].dispose()
        return {"Error": e}

def get_rules(req_data):
    serums_id = req_data['serums_id']
    hospital = req_data['hospital_id']
    connection, rule_table = hospital_rule_picker(hospital)
    try:
        i = 0
        rules = {}
        results = connection['session'].query(rule_table).\
            filter(rule_table.c.serums_id == serums_id).all()
        for result in results:
            rules.update({i: {
                    'rule_id': result.rule_id, 
                    'tags': result.tags, 
                    'filters': result.filters
                }
            })
            i += 1
        connection['engine'].dispose()
        return rules
    except Exception as e:
            connection['engine'].dispose()
            return e