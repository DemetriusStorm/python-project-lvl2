install:
	poetry install

lint:
	poetry run flake8 gendiff

autotest:
	poetry run pytest --cov=gendiff --cov-report xml tests/

test:
	poetry run pytest  -vv --color=yes --cov=gendiff

selfcheck:
	poetry check

check: selfcheck autotest lint

build: check
	poetry build

.PHONY: install build lint test autotest selfcheck check
