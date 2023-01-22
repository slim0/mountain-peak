.DEFAULT_GOAL := all

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt
