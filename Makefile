.DEFAULT_GOAL := all

requirements:
	poetry export -f requirements.txt --output requirements.txt
