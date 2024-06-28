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

start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

build:
	./build.sh