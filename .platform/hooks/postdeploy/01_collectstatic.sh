#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

mkdir -p /var/app/current/staticfiles
mkdir -p /var/app/current/media

python manage.py migrate --noinput
python manage.py createsuperuser --noinput || echo "Superuser already exists!"
python manage.py collectstatic --noinput --clear

# CRITICAL: Fix database permissions!
chmod 664 /var/app/current/db.sqlite3
chmod 775 /var/app/current

# Fix static/media permissions
chmod -R 755 /var/app/current/staticfiles
chmod -R 755 /var/app/current/media

echo "Deployment completed successfully!"