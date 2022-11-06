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


# Setup dev environment
1. Follow instructions from "How to run the app" section
2. run `poetry install` to setup your local python environment and install all the dependencies. A `.venv` should appear at the root of the project. Be sure to configure the python environment path of your IDE to `.venv/bin/python`. If using VSCODE, there is an existing `.vscode` folder with `settings.json` file in it !
3. Configure your IDE to use `.flake8` configuration file (linter)
4. Configure your IDE to use `pyproject.toml` configuration file for `isort` (sort imports) and `black` (formatter)


# DEV instruction, tips and ameliorations

## Manage python package

Use `poetry`!

To add a new package: `poetry add package-name`

To remove a package: `poetry remove package-name`

**You must rebuild the application after adding some requirements**

See [poetry documentation](https://python-poetry.org/docs/) for more information about it !

## Delete database
Docker container database is persistent accross `./data` folder. If you nedd to erase the whole database, remove this folder and restart docker containers.

# Future improvements
- Add a production docker configuration (with nginx & uvicorn containers, production env settings)
- CI/CD
- Paginate MountainPeakViewSet list view if a lot of Mountains ! make a BaseView if other elements
- change docker python image with alpine image (lighter)
- Swagger: Manage InBBoxFilter
