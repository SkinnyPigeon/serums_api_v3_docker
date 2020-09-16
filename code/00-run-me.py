# Control file to completely setup the docker image

import os

# installing the dependencies
print('Installing dependencies')
print('\n')

os.system('python3 /code/01-install-python-requirements.py')