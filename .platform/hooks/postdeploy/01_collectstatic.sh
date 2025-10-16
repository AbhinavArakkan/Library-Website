#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

mkdir -p /var/app/current/staticfiles
mkdir -p /var/app/current/media
mkdir -p /var/app/current/media/imgs  # Create imgs subdirectory!

# IMPORTANT: Make parent directory writable FIRST
chmod 775 /var/app/current

# Run migrations (creates db.sqlite3)
python manage.py migrate --noinput

# Fix database permissions AFTER it's created
chmod 664 /var/app/current/db.sqlite3

# Create superuser
python manage.py createsuperuser --noinput || echo "Superuser already exists!"

# Collect static files
python manage.py collectstatic --noinput --clear

# CRITICAL: Make media writable for uploads!
chmod -R 775 /var/app/current/media
chmod -R 755 /var/app/current/staticfiles

echo "Deployment completed successfully!"