# യുവജന വായനശാല & ഗ്രന്ഥാലയം

Local Library website built with Django.

## Setup

1. Clone repository
2. Create virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file with required variables
5. Run migrations: `python manage.py migrate`
6. Run server: `python manage.py runserver`

## Environment Variables

Required in `.env`:
- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- DJANGO_ALLOWED_HOSTS