import os
from pathlib import Path
project_folder = os.path.expanduser('~/code/api/')

from dotenv import load_dotenv
load_dotenv(os.path.join(project_folder, '.env'))
PASSWORD = os.environ.get('PGPASSWORD')

import json
import pandas as pd

from sqlalchemy import insert, select
from sources.data_vaults.fcrb import create_fcrb_dv
from sources.data_vaults.ustan import create_ustan_dv
from sources.data_vaults.zmc import create_zmc_dv

from functions.unique_schema import create_unique_schema_name, setup_data_vault_connection, create_unique_schema 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData

def create_data_vault(hospital_id):
    Base = declarative_base()
    schema = create_unique_schema_name(5)
    print(schema)
    connection = setup_data_vault_connection(schema, Base)
    create_unique_schema(connection, schema, Base)
    if hospital_id == 'FCRB':
        create_fcrb_dv(schema, Base, connection['engine'])
    elif hospital_id == 'USTAN':
        create_ustan_dv(schema, Base, connection['engine'])
    elif hospital_id == 'ZMC':
        create_zmc_dv(schema, Base, connection['engine'])

    return connection

def connect_to_existing_dv(schema):
    metadata = MetaData(schema=schema)
    Base = automap_base(metadata=metadata)
    engine = create_engine('postgresql://postgres:{}@localhost:5432/data_vault'.format(PASSWORD))
    Base.prepare(engine, reflect=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return {'base': Base, 'metadata': metadata, 'engine': engine, 'session': session, 'schema': schema}

def get_link_table_value_to_insert(hub):
  return hub[4:] + "_id"

def hubs_satellites_links(control_files, key):
    for control_file in control_files:
        if control_file['hubs']['table'] == key:
            hubs = control_file['hubs']
            satellites = control_file['satellites']
            links = control_file['links']
    return hubs, satellites, links

def get_class_by_schema_and_tablename(schema, table_fullname, base):
  for class_name in base._decl_class_registry.values():
    if hasattr(class_name, '__table__') and class_name.__table__.fullname == schema + '.' + table_fullname:
      return class_name

def handle_hubs(schema, hub, row, engine, base):
    # print("HANDLING HUBS")
    # print("HUB: {}".format(hub))
    keys_to_insert = {}
    for key in hub['keys']:
      try:
        keys_to_insert.update({key: getattr(row, key)})
      except:
        print("Wrong Key but don't worry")

    hub_to_insert = get_class_by_schema_and_tablename(schema, hub['hub'], base)
    hub_query = insert(hub_to_insert).values(keys_to_insert)
    hub_result = engine.execute(hub_query, con=engine)

    hub_id = hub_result.returned_defaults[0]

    # print("HUB NAME: {}".format(hub['hub']))
    # print("HUB ID: {}".format(hub_id))
    return hub_id


def handle_satellites(satellites, hub, hub_id, row, engine, schema, base, source_table):
    # print("HANDLING SATELLITES")
    for satellite in satellites['satellites']:
        # print("satellite: {}".format(satellite))
        if satellite['hub'] == hub['hub']:
            satellite_to_insert = get_class_by_schema_and_tablename(schema, satellite['satellite'], base)
            # print("INSERT: {}".format(satellite_to_insert))
            if len(satellite['columns']) == 0:
                continue
            else:
                columns_to_insert = {'hub_id': hub_id, 'source_table': source_table}
                for column in satellite['columns']:
                    try:
                        columns_to_insert.update({column: getattr(row, column)})
                    except:
                        print("Error")
            satellite_query = insert(satellite_to_insert).values(columns_to_insert)
            print("SAT QUERY: {}".format(satellite_query))
            satellite_result = engine.execute(satellite_query, con=engine)
            print("SAT RES: {}".format(satellite_result))

        
def setup_links(hub, hub_id, links):
    # print("SETTING LINKS")
    id_name = get_link_table_value_to_insert(hub['hub'])
    # print("ID NAME: {}".format(id_name))
    for link in links['links']:
    #   print("LINK BEFORE: {}".format(link))

      for value in link['values']:
        if value == id_name:
          link['values'][value] = hub_id
        #   print("LINK AFTER: {}".format(link))

def handle_links(schema, links, engine, base):
    # print("HANDLING LINKS")
    for link in links['links']:
        link_to_insert = get_class_by_schema_and_tablename(schema, link['link'], base)
        ids_to_insert = link['values']
        link_query = insert(link_to_insert).values(ids_to_insert)
        link_result = engine.execute(link_query, con=engine)

def copy_to_dv(source_data, control_files, connection):
    engine = connection['engine']
    base = connection['base']
    schema = connection['schema']
    for key, data_to_copy in source_data.items():
        # print(key)
        # print(data_to_copy)
        hubs, satellites, links = hubs_satellites_links(control_files, key)
        for row in data_to_copy.itertuples(index=False):
            source_table = hubs['table'].split('.')[1]
            for hub in hubs['hubs']:
                hub_id = handle_hubs(schema, hub, row, engine, base)
                handle_satellites(satellites, hub, hub_id, row, engine, schema, base, source_table)
                setup_links(hub, hub_id, links)
            handle_links(schema, links, engine, base)
    engine.dispose()
    return return_dv(schema)

def return_dv(schema):
    # print("RETURNING DV")
    output = []
    connection = connect_to_existing_dv(schema)

    session = connection['session']
    base = connection['base']
    engine = connection['engine']

    for class_name in base._decl_class_registry.values():
        if hasattr(class_name, '__table__'):
            query = session.query(class_name)
            df = pd.read_sql(query.statement, con=engine)
            df = df.to_json(orient='index')
            parsed = json.loads(df)
            table = {class_name.__table__.name: parsed}
            output.append(table)
    engine.dispose()
    # print(output)
    return json.dumps(output)
