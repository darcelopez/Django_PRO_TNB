.PHONY: install
install:
	poetry install

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
	poetry run python -m core.manage runserver

.PHONY: update
update: install migrate;