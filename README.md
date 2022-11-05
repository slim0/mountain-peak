### Mountain Peak Backend

MFI recrutment process. Simple web service for storing and retrieving moutain peaks.

# Instructions

The context of this test is to provide a simple web service for storing and retrieving moutain peaks.

Using Django / FastAPI / Laravel / Symfony … *  and a postgresql database (postGIS can be used for geo features), implement the following features:
- models/db tables for storing a peak location and attribute: lat, lon, altitude, name
- REST api endpoints to :
  * create/read/update/delete a peak
  * retrieve a list of peaks in a given geographical bounding box<>

Deploy all this stack using docker and docker-compose

The source code should be delivered using github/ bitbucket with detailed explanations on how to deploy and launch the project.

# Commands

`docker compose up` : build (if not built yet) and run app

`docker compose build` : if Dockerfile changed, then you may need to rebuild the image

`docker compose exec web python /code/mountain_peak_backend/manage.py makemigrations` : create new migration files if needed. To create the initial migration of a new app, you need to specify the app name at the end of this command. Also don't forget to add the app into INSTALLED_APPS django settings.

`docker compose exec web python /code/mountain_peak_backend/manage.py showmigrations` : show migrations (and what migrations are applied onto the database)

`docker compose exec web python /code/mountain_peak_backend/manage.py flush` : empty django development database

`docker compose exec web python /code/mountain_peak_backend/manage.py migrate` : apply migrations on docker development container

`docker compose exec web python /code/mountain_peak_backend/manage.py shell_plus` : Open shell_plus python interpreter

`docker compose exec web python /code/mountain_peak_backend/manage.py createsuperuser` : Create a django superuser

# How to run the app

1. git clone the project `https://github.com/slim0/mountain-peak.git`
2. install docker-compose on your workstation
3. run `docker compose up` from the root folder of the git project. *`-d` option can be add if you want to start the containers as a deamon process.*

# Setup dev environment
1. Follow instructions from "How to run the app" section
2. run `poetry install`
3. run `poetry shell` on a terminal

# Add python package / requirements

You must use `poetry`!

To add a new package: `poetry add package-name`

To remove a package: `poetry remove package-name`

`docker compose exec web`

See [poetry documentation](https://python-poetry.org/docs/) for more about it !
