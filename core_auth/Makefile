.PHONY: install
install:
	poetry install

.PHONY: inspect-code
inspect-code:
	clear
	poetry run flake8

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	clear
	poetry run pre-commit run --all-files


.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: makemigrations
makemigrations:
	poetry run python -m core.manage makemigrations

.PHONY: run-server
run-server:
	clear
	poetry run python -m core.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: update2
update2: migrate install-pre-commit;

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: up-production
up-production:
	test -f .env || touch .env
	docker-compose -f docker-compose.yml up --force-recreate db
