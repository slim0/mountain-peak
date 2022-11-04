#!/bin/sh

# https://github.com/django/djangoproject.com

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# python /code/mountain_peak_backend/manage.py flush --no-input
python /code/mountain_peak_backend/manage.py migrate
# python /code/mountain_peak_backend/manage.py collectstatic --no-input --clear

exec "$@"