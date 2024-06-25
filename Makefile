install:
    poetry install

runserver:
    poetry run python3 manage.py runserver

migrate:
    poetry run python3 manage.py makemigrations
    poetry run python3 manage.py migrate

collectstatic:
    poetry run python3 manage.py collectstatic --no-input

start:
    poetry run python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

build:
    ./build.sh
