# Creating the id tables in PostgreSQL

# Setup
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/code/api_v3_docker/code/api')
load_dotenv(os.path.join(project_folder, '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
# PASSWORD = os.environ.get('PGPASSWORD')
# PORT = os.environ.get('PGPORT')

engine = create_engine("postgresql://postgres:{}@localhost:{}/source".format(PASSWORD, PORT))

# Creating source tables

tables = ['fcrb_data', 'ustan_data', 'zmc_data']

for table in tables:
    sql_file = open('./api/reset_sql/sql/{table}.sql'.format(table=table), 'r')
    # sql_file = open('/code/api/reset_sql/sql/{table}.sql'.format(table=table), 'r')
    sql = text(sql_file.read())
    engine.execute(sql)