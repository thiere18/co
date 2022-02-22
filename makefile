build:
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
run-tests:
# Build and run containers
	docker-compose -f docker-compose-test.yml up --build -d 
	sleep 1
# run test 
	docker-compose -f docker-compose-test.yml run --rm api pytest -v
production:
	
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
# restart containers
	docker-compose -f docker-compose.prod.yml up -d

dev:
# run dev
	docker-compose -f docker-compose-dev.yml up 
init_test:
	python3 -m app.initial_data_test

-help:
	@echo "---------------HELP-----------------"
	@echo "available commands"
	@echo "test: for testing"
	@echo "dev: for running dev environment"
	@echo "init_test: to add initial test data"
	@echo "production: for running production environment"
	@echo "help: for running help command
	@echo "------------------------------------"

linting:
	black .
	flake8 app

