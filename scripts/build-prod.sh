#!/bin/bash

# Exit in case of error
set -e

# Build and run containers
docker-compose -f  docker-compose.prod.yml up --build -d

# Hack to wait for postgres container to be up before running alembic migrations
sleep 5;

# Run migrations
docker-compose  -f  docker-compose.prod.yml run --rm backend alembic upgrade head

# Create initial data
docker-compose  -f  docker-compose.prod.yml run --rm backend python3 app/initial_data.py