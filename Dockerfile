FROM python:3

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.3.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    curl \
    make \
    && curl -sSL 'https://install.python-poetry.org' | python - \
    && poetry --version


WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY . /app/

RUN poetry install
