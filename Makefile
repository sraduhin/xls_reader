install:
	poetry install

docker-install:
	docker-compose build

lint:
	poetry run flake8

example:
	poetry run parser "files/Приложение к заданию бек разработчика.xlsx"

docker-db:
	docker-compose run python_app poetry run python app/models.py

docker-example:
	docker-compose run python_app poetry run parser "files/Приложение к заданию бек разработчика.xlsx"
	
clean-db:
	poetry run python app/models.py
