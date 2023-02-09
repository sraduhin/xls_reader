# xls parser
#### Тестовое задание "Написать парсер для xls файла".

Запуск приложения выполняется через docker контейнер,
либо непосредственно из терминала с предварительной установкой зависимостей (через Poetry)
и возможностью подлкючения к БД.

#### Установка
```python
# Склонировать репозиторий
git clone https://github.com/sraduhin/xls_reader.git
cd xls_reader
```
В директории уже находится xls файл к тестовому заданию. Но если необходимо протестировать другой файл
с идентичной структурой, необходимо разместить его в директории приложения.

#### Запуск через Docker
```python
# сборка образа
docker-compose build
```
```python
# создание таблиц
make docker-db # тут периодически возникает ошибка, нужно повторить команду
```
```python
# запуск точки входа с уже готовой фикстурой
make docker-example
```
```python
# либо парсинг своего файла
docker-compose run python_app poetry run parser <filepath>
```
#### Локальный запуск предполагает установку зависимостей и создание переменных окружения (.env) для подключения к БД. Смотри .env.example
```python
# установка зависимостей
make install
# формирование таблиц
make clean-db
```
```python
# запуск точки входа с уже готовой фикстурой
make example
```
```python
# либо парсинг своего файла
poetry run parser <filepath>
```
# Как это работает. Пример с установкой.
#### Docker
<a href="https://asciinema.org/a/SLn9ZaAtHO34K2WgvRgFXCNdJ" target="_blank"><img src="https://asciinema.org/a/SLn9ZaAtHO34K2WgvRgFXCNdJ.svg" /></a>
#### Local
<a href="https://asciinema.org/a/VxVNCFpA5o4WXm743lIIGFnvY" target="_blank"><img src="https://asciinema.org/a/VxVNCFpA5o4WXm743lIIGFnvY.svg" /></a>
