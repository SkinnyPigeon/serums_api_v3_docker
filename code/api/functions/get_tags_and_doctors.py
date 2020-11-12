from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import load_only, sessionmaker, defer
import pandas as pd

import os
from dotenv import load_dotenv
from pathlib import Path

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

def hospital_picker(hospital_id):
    if hospital_id == 'FCRB':
        return 'fcrb'
    elif hospital_id == 'USTAN':
        return 'ustan'
    elif hospital_id == 'ZMC':
        return 'zmc'

def setup_connection(hospital):
    metadata = MetaData(schema=hospital)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {'base': Base, 'metadata': metadata, 'engine': engine, 'session': session}

def select_table_classes_tags_and_doctors(source_base, hospital):
    tags_and_doctors_classes = {}
    for class_name in source_base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == '{hospital}.hospital_tags'.format(hospital=hospital):
            tags_and_doctors_classes['tags'] = class_name
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == '{hospital}.translated_tags'.format(hospital=hospital):
            tags_and_doctors_classes['translated'] = class_name
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == '{hospital}.hospital_doctors'.format(hospital=hospital):
            tags_and_doctors_classes['doctors'] = class_name
    return tags_and_doctors_classes

def select_tags_and_doctors(tags_and_doctors_classes, connection):
    tags_and_doctors = {}
    session = connection['session']
    tag_query = session.query(tags_and_doctors_classes['tags']).all()
    doctor_query = session.query(tags_and_doctors_classes['doctors']).all()
    translated_query = session.query(tags_and_doctors_classes['translated']).all()
    for tags in tag_query:
        tags_and_doctors['tags'] = tags.__dict__['tags']
    for translation in translated_query:
        tags_and_doctors['translated'] = translation.__dict__['tags']
    tags_and_doctors['doctors'] = doctor_query
    doctor_fields = ['id', 'name', 'specialism']
    doctors = {}
    for id, doctor in enumerate(doctor_query):
        doctors[id] = str([doctor.__dict__.get(field) for field in doctor_fields]).strip('[]')
    tags_and_doctors['doctors'] = doctors
    connection['engine'].dispose()
    return tags_and_doctors

def get_tags_and_doctors(hospital_id):
    hospital = hospital_picker(hospital_id)
    connection = setup_connection(hospital)
    tags_and_doctors_classes = select_table_classes_tags_and_doctors(connection['base'], hospital)
    tags_and_doctors = select_tags_and_doctors(tags_and_doctors_classes, connection)
    print(tags_and_doctors)
    return tags_and_doctors