#!/bin/bash
# Exit in case of error
set -e

# Build and run containers
docker-compose -f docker-compose.prod.yml up -d 

# Hack to wait for postgres container to be up before running alembic migrations
sleep 5;

# Run migrations
# docker-compose run --rm api alembic downgrade base
# sleep 5;
docker-compose -f docker-compose.prod.yml run --rm api alembic upgrade head
sleep 5;

# Create initial data
docker-compose -f docker-compose.prod.yml run --rm api python3 -m app.initial_data