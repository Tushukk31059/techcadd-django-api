#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn techcadd_backend.wsgi
