install:
	poetry install

runserver:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --no-input

start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

build:
	./build.sh