#!/bin/bash
echo "🟡 Running Django migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput && gunicorn techcadd_backend.wsgi --bind 0.0.0.0:$PORT
# python manage.py migrate --noinput
python manage.py collectstatic --noinput
echo "✅ Migrations done, starting Gunicorn..."
gunicorn techcadd_backend.wsgi:application
# python manage.py migrate --noinput && gunicorn techcadd_backend.wsgi --bind 0.0.0.0:$PORT