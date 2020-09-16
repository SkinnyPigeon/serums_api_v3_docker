import os
os.system('apt update')
os.system('apt install python3-pip -y')
os.system('apt-get install libpq-dev python-dev -y')
os.system('pip3 install pandas sqlalchemy numpy flask flask-cors flask-restplus psycopg2 gunicorn python-dotenv')
os.system('pip3 uninstall --yes Werkzeug')
os.system('pip3 install Werkzeug==0.16.1')