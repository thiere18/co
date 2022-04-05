build:
# Build and run containers
	bash scripts/build.sh
run_tests:
	bash scripts/test.sh

dev:
	docker-compose up --build

build_prod:
	bash scripts/build_prod.sh
