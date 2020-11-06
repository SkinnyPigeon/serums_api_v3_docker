#!/bin/bash

service postgresql start

python3 /code/00-run-me.py

gunicorn -b 0.0.0.0:5004 --workers=3 --chdir /code/api/ api:app
