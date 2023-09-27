#.PHONY explicity instructs makefile that these commands don't use files;

### POETRY ###
.PHONY: activate
activate:
	C:\.dev\Python\pypoetry\bin\poetry.exe shell

.PHONY: install
install:
	C:\.dev\Python\pypoetry\bin\poetry.exe install

.PHONY: install-pre-commit
install-pre-commit:
	C:\.dev\Python\pypoetry\bin\poetry.exe run pre-commit uninstall -t pre-commit; C:\.dev\Python\pypoetry\bin\poetry.exe run pre-commit install -t pre-commit

.PHONY: lint
lint:
	C:\.dev\Python\pypoetry\bin\poetry.exe run pre-commit run --all-files

.PHONY: update
update: install migrate install-pre-commit lint


### DJANGO ###
.PHONY: shell
shell:
	py backend/manage.py shell

.PHONY: showmigrations
showmigrations:
	py backend/manage.py showmigrations

.PHONY: migrate
migrate:
	py backend/manage.py migrate

.PHONY: makemigrations
makemigrations:
	py backend/manage.py makemigrations

.PHONY: runserver
runserver:
	py backend/manage.py runserver

.PHONY: createsuperuser
createsuperuser:
	py backend/manage.py createsuperuser

.PHONY: spectacular
spectacular:
	py backend/manage.py spectacular --file schema.yml


### TESTS ###
.PHONY: test
test:
	pytest

.PHONY: test-verbose
test-verbose:
	pytest -s

.PHONY: coverage
coverage:
	pytest --cov=backend

.PHONY: relatory
relatory:
	coverage html

### DOCKER ###
# .PHONY: backend
# backend:
# 	docker container exec -it tv_backend bash;

# .PHONY: root-backend
# root-backend:
# 	docker container exec -it -u root tv_backend bash;

# .PHONY:database
# database:
# 	docker container exec -it tv_database bash;

# .PHONY: root-database
# root-database:
# 	docker container exec -it -u root tv_database bash;
