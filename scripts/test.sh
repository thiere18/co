#!/bin/bash
# Exit in case of error
set -e

# Build and run containers
docker-compose -f docker-compose-test.yml up -d 
sleep 1
# run test 
docker-compose -f docker-compose-test.yml run --rm api pytest -v 