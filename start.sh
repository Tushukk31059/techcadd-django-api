#!/bin/bash
echo "🟡 Running setup commands..."


# 1. Run migrations to create the table
python manage.py migrate --noinput

# 2. Collect static files
python manage.py collectstatic --noinput
python manage.py makemigrations api

# 3. Start the Gunicorn server (This must be the final line)
echo "✅ Setup done. Starting Gunicorn..."
gunicorn techcadd_backend.wsgi --bind 0.0.0.0:$PORT