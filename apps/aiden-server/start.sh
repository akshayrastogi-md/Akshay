#!/bin/bash
set -e

# Run migrations
poetry run alembic upgrade head

# Start Gunicorn
poetry run gunicorn -c gunicorn_conf.py app.main:app
