#!/bin/bash

# Static files & migrations

# echo "Dealing with static files..."
# python manage.py collectstatic --no-input

echo "Running migrations..."
python3 manage.py migrate

# Run the server

echo "Running server..."
python manage.py runserver 0.0.0.0:8000
