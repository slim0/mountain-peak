#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mountain_peak_backend.settings")

    am_i_in_docker = os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", "FALSE")

    if am_i_in_docker == "FALSE":
        # Load env here so we can run 'python manage.py' command from local dev workstation to avoid entering docker container
        load_dotenv("env/django.dev.env")
        load_dotenv("env/postgis.dev.env")
        # This last env file isn't present on docker container.
        # overrides POSTGRES_HOST to access it on 127.0.0.1
        load_dotenv("../local.django.dev.env", override=True)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
