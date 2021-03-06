from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import load_only, sessionmaker, defer
import pandas as pd
from tabulate import tabulate

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


from sources.tags.fcrb import fcrb_tags
from sources.tags.ustan import ustan_tags
from sources.tags.zmc import zmc_tags

def hospital_picker(hospital_id):
    if hospital_id == 'FCRB':
        return 'fcrb', fcrb_tags
    elif hospital_id == 'USTAN':
        return 'ustan', ustan_tags
    elif hospital_id == 'ZMC':
        return 'zmc', zmc_tags

def setup_connection(hospital):
    metadata = MetaData(schema=hospital)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:{}/source'.format(PASSWORD, PORT))
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {'base': Base, 'metadata': metadata, 'engine': engine, 'session': session}

def select_table_classes(hospital, source_base):
    tables = {}
    for class_name in source_base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname not in ['{hospital}.serums_ids'.format(hospital=hospital), '{hospital}.patient_rules'.format(hospital=hospital), '{hospital}.hospital_tags'.format(hospital=hospital), '{hospital}.hospital_doctors'.format(hospital=hospital)]:
            tables.update({class_name.__table__.fullname: class_name})
    return tables

def select_lookup_table_class(source_base, table_name):
    for class_name in source_base._decl_class_registry.values():
        if hasattr(class_name, '__table__') and class_name.__table__.fullname == table_name:
            return class_name

def select_source_patient_id_name(hospital):
    connection = setup_connection(hospital)
    metadata = connection['metadata']
    table_dict = dict.fromkeys(metadata.sorted_tables)
    connection['engine'].dispose()
    for keys, values in table_dict.items():
        if keys.name == 'serums_ids':
            for column in keys.columns:
                if ".serums_id" not in str(column):
                    return str(column).split(".")[1]

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

def select_source_patient_id_value(source_session, id_class, serums_id, key_name):
    result = source_session.query(id_class).filter_by(serums_id=serums_id).one()
    res = object_as_dict(result)
    return res[key_name]

def select_tags_from_rule_table(source_session, rule_class, rule_id):
    query = source_session.query(rule_class).filter_by(rule_id=rule_id).one()
    result = object_as_dict(query)
    return result['tags'], result['filters']

def select_source_fields(source_session, tables, hospital, hospital_tags, patient_tags, filters, patient_id, key_name, connection):
    to_return = {}
    # print(patient_tags)
    for hospital_tag in hospital_tags:
        # print(hospital_tag)
        try:
            if hospital_tag['tag'] in patient_tags:
                to_return[hospital_tag['table']] = []
                class_name = tables[hospital_tag['table']]
                # print(class_name)
                results = get_results(source_session, class_name, hospital_tag['fields'], patient_id, filters, key_name, hospital_tag['key_lookup'], connection)
                for result in results:
                    to_return[hospital_tag['table']].append(object_as_dict(result))
        except:
            pass
    return to_return

def get_results(source_session, class_name, fields, patient_id, filters, key_name, key_lookup, connection):
    string_fields = ', '.join(fields)
    # print(fields)
    query = source_session.query(class_name)
    # print("QUERY: {}".format(query))
    try:
        try:
            all_filters = {key_name: patient_id}
            all_filters.update(filters)
            for attr,value in all_filters.items():
                query = query.filter(getattr(class_name,attr)==value).options(load_only(*fields))
                # print("QUERY 1: {}".format(query))
        except:
            all_filters = {key_name: patient_id}
            for attr,value in all_filters.items():
                query = query.filter(getattr(class_name,attr)==value).options(load_only(*fields))
                # print("QUERY 2: {}".format(query))

    except:
        query = get_results_via_alternative_key(key_name, patient_id, connection, source_session, key_lookup, class_name)
        # print("QUERY 3: {}".format(query))
    results = query.all()
    # print("RESULTS: {}".format(results))
    connection['engine'].dispose()
    return results

def get_results_via_alternative_key(key_name, patient_id, connection, source_session, key_lookup, class_name):
    search_values = []
    all_filters = {key_name: patient_id}
    lookup_class = select_lookup_table_class(connection['base'], key_lookup['table'])
    query = source_session.query(lookup_class)
    for attr, value in all_filters.items():
        query = query.filter(getattr(lookup_class, attr)==value)
    results = query.all()
    for result in results:
        result = object_as_dict(result)
        search_values.append(result[key_lookup['field']])
    query = source_session.query(class_name)
    all_filters = {key_lookup['field']: None}
    for attr, value in all_filters.items():
        query = query.filter(getattr(class_name, attr).in_(search_values))
    return query

def results_to_df(results):
    for key, value in results.items():
        results[key] = pd.DataFrame(results[key])
    return results

def get_source_data(req_data):
    hospital, hospital_tags = hospital_picker(req_data['hospital_id'])
    connection = setup_connection(hospital)
    source_base = connection['base']
    source_session = connection['session']
    tables = select_table_classes(hospital, source_base)
    id_class = source_base.classes.serums_ids
    rule_class = source_base.classes.patient_rules
    key_name = select_source_patient_id_name(hospital)
    patient_id = select_source_patient_id_value(source_session, id_class, req_data['serums_id'], key_name)
    # print(patient_id)
    patient_tags, filters = select_tags_from_rule_table(source_session, rule_class, req_data['rule_id'])
    # print(patient_tags)
    source_data = select_source_fields(source_session, tables, hospital, hospital_tags, patient_tags, filters, patient_id, key_name, connection)
    # print(source_data)
    source_data = results_to_df(source_data)
    for key, values in source_data.items():
        print("RESULT: ")
        print(print(tabulate(values, headers='keys', tablefmt='psql')))

    connection['engine'].dispose()
    return source_data, patient_tags