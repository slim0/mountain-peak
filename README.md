### Mountain Peak Backend

MFI recrutment process. Simple web service for storing and retrieving moutain peaks.

# Commands
`docker compose up` : build (if needed) and run app
`docker compose build` : if Dockerfile changed, then you may need to rebuild the image

`docker compose exec web python /code/mountain_peak_backend/manage.py makemigrations` : create new migration files if needed
`docker compose exec web python /code/mountain_peak_backend/manage.py flush` : empty django development database
`docker compose exec web python /code/mountain_peak_backend/manage.py migrate` : apply migrations on docker development container

`docker compose exec web python /code/mountain_peak_backend/manage.py shell_plus` : Open shell_plus python interpreter
`docker compose exec web python /code/mountain_peak_backend/manage.py createsuperuser` : Create a django superuser

# Setup development environment

1. git clone the project
2. install docker-compose on your workstation
3. run `docker compose up` from the root folder of the git project. *`-d` option can be add if you want to start the containers as a deamon process.*
