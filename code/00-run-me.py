# Control file to completely setup the docker image

import os

# installing the dependencies
print('Installing dependencies')
print('\n')
os.system('python3 /code/01-install-python-requirements.py')

# creating the datalake
print('Creating the data lake')

os.system('python3 /code/02-setup-datalake.py')

# creating the databases

os.system('python3 /code/03-start-database.py')

# create the source tables
print('Creating the source tables')

os.system('python3 /code/04-create-source-tables.py')

# filling the source tables
print('Filling the source tables')

os.system('python3 /code/05-fill-source-tables.py')