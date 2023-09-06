#.PHONY explicity instructs makefile that these commands don't use files;

### POETRY ###
.PHONY: activate
activate:
	poetry shell

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall -t pre-commit; poetry run pre-commit install -t pre-commit

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: update
update: install migrate install-pre-commit lint;

### DJANGO ###
.PHONY: migrate
migrate:
	py backend/manage.py migrate

.PHONY: migrations
migrations:
	py backend/manage.py makemigrations

.PHONY: runserver
runserver:
	py backend/manage.py runserver

.PHONY: createsuperuser
createsuperuser:
	py backend/manage.py createsuperuser

### DOCKER ###
.PHONY: backend
backend:
	docker container exec -it tv_backend bash

.PHONY: root-backend
root-backend:
	docker container exec -it -u root tv_backend bash

.PHONY:database
database:
	docker container exec -it tv_database bash

.PHONY: root-database
root-database:
	docker container exec -it -u root tv_database bash
