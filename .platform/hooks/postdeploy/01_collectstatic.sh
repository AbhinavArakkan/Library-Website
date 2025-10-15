#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

# Run migrations
python manage.py migrate --noinput

# Create superuser
python manage.py createsuperuser --noinput || echo "Superuser already exists!"

# Collect static files
python manage.py collectstatic --noinput

# IMPORTANT: Create symlink for nginx to serve static files
sudo mkdir -p /var/app/current/static
sudo ln -sf /var/app/current/staticfiles/* /var/app/current/static/ 2>/dev/null || true

echo "Deployment completed successfully!"