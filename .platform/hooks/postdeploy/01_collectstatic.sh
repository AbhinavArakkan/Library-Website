#!/bin/bash
source /var/app/venv/*/bin/activate
cd /var/app/current

rm -f db.sqlite3

python manage.py migrate --noinput

python manage.py createsu

python manage.py collectstatic --noinput