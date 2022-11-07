### Mountain Peak Backend

MFI recrutment process. Simple web service for storing and retrieving moutain peaks.

# Instructions

The context of this test is to provide a simple web service for storing and retrieving moutain peaks.

Using Django / FastAPI / Laravel / Symfony … *  and a postgresql database (postGIS can be used for geo features), implement the following features:
- models/db tables for storing a peak location and attribute: lat, lon, altitude, name
- REST api endpoints to :
  * create/read/update/delete a peak
  * retrieve a list of peaks in a given geographical bounding box

Deploy all this stack using docker and docker-compose

The source code should be delivered using github/ bitbucket with detailed explanations on how to deploy and launch the project.

# How to run the app and call the API

## Run the app
1. Clone the git project `https://github.com/slim0/mountain-peak.git`
2. install docker on your workstation !
3. run `docker compose up` from the root folder of the git project. *`-d` option can be add if you want to start the containers as a deamon process.*

## API calls
Once the application is running, you can visit the swagger URL here to make calls: [http://localhost:8000/api/v1/swagger/schema/](http://localhost:8000/api/v1/swagger/schema/).

N.B.:
- GET method on /moutain_peaks/ is implementing a filter to retrieve a list of peaks in a given geographical bounding box queryparam.

![mountain_peaks_bbox_filter.png](/img/mountain_peaks_bbox_filter.png)

- For POST, PUT and PATCH methods, the coordinates field must be a string like: "POINT(0 0)" where the first 0 is the longitude and the second the latitude.

![coordinates_field.png](/img/coordinates_field.png)

# Setup dev environment
1. Follow instructions from "How to run the app" section
2. run `poetry install` to setup your local python environment and install all the dependencies. A `.venv` should appear at the root of the project. Be sure to configure the python environment path of your IDE to `.venv/bin/python`. If using VSCODE, there is an existing `.vscode` folder with `settings.json` file in it !
3. Configure your IDE to use `.flake8` configuration file (linter)
4. Configure your IDE to use `pyproject.toml` configuration file for `isort` (sort imports) and `black` (formatter)


# DEV instruction, tips and ameliorations

## Run commands in docker container (all `python manage.py command` for exemple)

`docker compose exec web python /app/code/manage.py my_command`

## Run django tests

`docker compose exec web python /app/code/manage.py test`

## Manage python package

1. Use `poetry` on your local environment

To add a new package: `poetry add package-name`

To remove a package: `poetry remove package-name`

2. export to a requirements.txt file: `poetry export -f requirements.txt --output requirements.txt`
3. run `docker compose exec web pip install -r /code/requirements.txt` or rebuild the docker container to add requirements to the python environment of the container.
4. import the package on your .py files

See [poetry documentation](https://python-poetry.org/docs/) for more information about it !

## Delete database
Docker container database is persistent accross `./data` folder. If you nedd to erase the whole database, remove this folder and restart docker containers.

# Future improvements
- Add a production docker configuration (with nginx & uvicorn containers, production env settings)
- CI/CD
- Paginate MountainPeakViewSet list view if a lot of Mountains ! make a BaseView if other elements
