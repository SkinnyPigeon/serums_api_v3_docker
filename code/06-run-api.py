import os
os.system('gunicorn -b 0.0.0.0:5004 --workers=3 --chdir /code/api/ api:app')