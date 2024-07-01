install:
	poetry install

runserver:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

local:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

translate:
	poetry run django-admin compilemessages

collectstatic:
	python manage.py collectstatic --no-input

lint:
	poetry run flake8

test:
	poetry run python manage.py test

selfcheck:
	poetry check

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

check: selfcheck test-coverage lint

start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

build:
	./build.sh