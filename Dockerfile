# syntax=docker/dockerfile:1

# https://github.com/django/djangoproject.com
FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.2.2 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    # POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update
RUN apt-get install binutils libproj-dev gdal-bin -y
RUN apt-get install netcat -y

RUN pip install --upgrade pip

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

WORKDIR /code
COPY mountain_peak_backend .
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry export -f requirements.txt --without dev --output requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./docker-entrypoint.sh .
RUN chmod +x /code/docker-entrypoint.sh

WORKDIR /code/mountain_peak_backend

ENTRYPOINT ["/bin/sh", "/code/docker-entrypoint.sh"]