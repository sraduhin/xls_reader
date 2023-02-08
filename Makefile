install:
	poetry install

docker-install:
	docker-compose build

lint:
	poetry run flake8

start:
	poetry run python app/parser.py

docker-start:
	docker-compose up

example:
	poetry run parser "files/Приложение к заданию бек разработчика.xlsx"

clean-db:
	poetry run python app/models.py
