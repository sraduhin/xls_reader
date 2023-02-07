#FROM python:3.11-alpine as builder
FROM python:3


RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --extras psycopg2-binary

WORKDIR /usr/local/src/xls_reader

CMD ["make", "start"]