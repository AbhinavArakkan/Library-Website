#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

mkdir -p /var/app/current/staticfiles
mkdir -p /var/app/current/media

python manage.py migrate --noinput
python manage.py createsuperuser --noinput || echo "Superuser already exists!"
python manage.py collectstatic --noinput --clear

chmod -R 755 /var/app/current/staticfiles
chmod -R 755 /var/app/current/media

echo "Deployment completed successfully!"