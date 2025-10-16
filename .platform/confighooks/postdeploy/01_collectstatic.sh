#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

mkdir -p /var/app/current/staticfiles
mkdir -p /var/app/current/media

# IMPORTANT: Make parent directory writable FIRST
chmod 775 /var/app/current

# Run migrations (creates db.sqlite3)
python manage.py migrate --noinput

# NOW fix database permissions AFTER it's created
chmod 664 /var/app/current/db.sqlite3

# Create superuser
python manage.py createsuperuser --noinput || echo "Superuser already exists!"

# Collect static files
python manage.py collectstatic --noinput --clear

# Fix static/media permissions
chmod -R 755 /var/app/current/staticfiles
chmod -R 755 /var/app/current/media

echo "Deployment completed successfully!"