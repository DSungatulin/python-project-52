start:
	poetry run python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

dev-start:
	poetry run python manage.py runserver

build:
	./build.sh

install:
	poetry install

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

local:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

translate:
	poetry run django-admin compilemessages

lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

selfcheck:
	poetry check

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

check:selfcheck test-coverage lint
