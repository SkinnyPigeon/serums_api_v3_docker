from sqlalchemy import create_engine, MetaData, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path
import json

# project_folder = os.path.expanduser('~/code/api_v3_docker/code/api')
# load_dotenv(os.path.join(project_folder, '.env'))
# PORT = os.getenv('PGPORT')
# PASSWORD = os.getenv('PGPASSWORD')
# PASSWORD = os.environ.get('PGPASSWORD')
# PORT = os.environ.get('PGPORT')

project_folder = os.path.expanduser('~/code/api_v3_docker/code/api')
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
if PORT == None:
    PASSWORD = os.environ.get('PGPASSWORD')
    PORT = os.environ.get('PGPORT')


def hospital_id_picker(hospital_id):
    if hospital_id == 'FCRB':
        hospital = 'fcrb'
    elif hospital_id == 'USTAN':
        hospital = 'ustan'
    elif hospital_id == 'ZMC':
        hospital = 'zmc'
    connection = setup_connection(hospital)
    id_column, id_table = select_id_column(connection)
    return connection, id_column, id_table

def patient_id_picker(hospital_id):
    if hospital_id == 'FCRB':
        patient_id = 4641202
    elif hospital_id == 'USTAN':
        patient_id = 2606566626
    elif hospital_id == 'ZMC':
        patient_id = 1075835
    return patient_id

def setup_connection(hospital):
    metadata = MetaData(schema=hospital)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {'base': Base, 'metadata': metadata, 'engine': engine, 'session': session}

def select_id_column(connection):
    tables = connection['metadata'].sorted_tables
    for table in tables:
        if table.name == 'serums_ids':
            for column in table.c:
                if str(column) != 'serums_ids.serums_id':
                    return str(column).split('.')[1], table

def add_user_to_serums(req_data):
    serums_id = req_data['serums_id']
    patient_id = req_data['patient_id']
    hospital = req_data['hospital_id']

    connection, id_column, id_table = hospital_id_picker(hospital)

    try:
        patient_to_add = {id_column: patient_id, 'serums_id': serums_id}
        add_query = insert(id_table).values(patient_to_add)
        result = connection['engine'].execute(add_query)
        connection['engine'].dispose()
        return {"Result": "Success"}
    except Exception as e:
        connection['engine'].dispose()
        return {"Result": e}

def add_poc_user_to_serums(req_data):
    serums_id = req_data['serums_id']
    hospital = req_data['hospital_id']
    patient_id = patient_id_picker(req_data['hospital_id'])

    connection, id_column, id_table = hospital_id_picker(hospital)

    try:
        patient_to_add = {id_column: patient_id, 'serums_id': serums_id}
        add_query = insert(id_table).values(patient_to_add)
        result = connection['engine'].execute(add_query)
        connection['engine'].dispose()
        return {"Result": "Success"}
    except Exception as e:
        connection['engine'].dispose()
        return {"Result": e}

def remove_user_from_serums(req_data):
    serums_id = req_data['serums_id']
    hospitals = req_data['hospitals']

    for hospital in hospitals:
        connection, id_column, id_table = hospital_id_picker(hospital)
        patient_to_remove = id_table.delete().where(id_table.c.serums_id==serums_id)
        connection['session'].execute(patient_to_remove)
        connection['session'].commit()
        connection['engine'].dispose()

    return {"Result": "Success"}