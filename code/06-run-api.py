import os
os.system('gunicorn -b 0.0.0.0:5000 --workers=3 --chdir /code/api/ api:app')