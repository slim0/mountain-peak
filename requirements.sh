#!/bin/sh

poetry export -f requirements.txt --output requirements.txt
echo "requirements.txt file updated !"

DOCKER_CONTAINER_NAME="web"
IS_WEB_CONTAINER_RUNNING=$(docker compose ps ${DOCKER_IMAGE_NAME})

if [[ -n ${IS_WEB_CONTAINER_RUNNING} ]]; then
    docker compose exec ${DOCKER_CONTAINER_NAME} pip install -r ../requirements.txt
    echo "Requirements updated inside docker 'web' container !"
fi