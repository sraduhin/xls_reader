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

clean-db:
	poetry run python app/models.py
