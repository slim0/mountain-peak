# syntax=docker/dockerfile:1

# https://github.com/django/djangoproject.com
FROM python:3.11.0

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # poetry
    POETRY_VERSION=1.2.2 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    # POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    # PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update
RUN apt-get install binutils libproj-dev gdal-bin -y
RUN apt-get install netcat -y

RUN pip install --upgrade pip

COPY . /code/
RUN pip install -r /code/requirements.txt

WORKDIR /code/mountain_peak_backend

ENTRYPOINT ["/bin/sh", "/code/docker-entrypoint.sh"]