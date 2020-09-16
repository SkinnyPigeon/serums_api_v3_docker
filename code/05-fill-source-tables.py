# Creating the id tables in PostgreSQL

# Setup
from sqlalchemy import create_engine, text
import os
pwd = os.environ.get('PGPASSWORD')

engine = create_engine("postgresql://postgres:{}@localhost:5432/source".format(pwd))

# Creating source tables

tables = ['fcrb_data', 'ustan_data', 'zmc_data']

for table in tables:
    sql_file = open('/code/api/reset_sql/sql/{table}.sql'.format(table=table), 'r')
    sql = text(sql_file.read())
    engine.execute(sql)