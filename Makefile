.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

commit:
	@NO_STAG=$$(git status -s | grep AM | wc -l) && \
	if [ "$$NO_STAG" -gt "0" ]; then\
		echo -e "\033[1;33mUnstaged files detected, please stag these files.\033[0m";\
		git status -s | grep --color=always AM;\
	else\
		pre-commit run;\
    fi

commit-add:
	git add .
	pre-commit run

lint: ## check style with black
	black -t py38 setup.py tiktok_dl tests

up-dep:
	pip-upgrade requirements.txt

up-dev:
	pip-upgrade requirements_dev.txt

up-all:
	pip-upgrade requirements.txt requirements_dev.txt

test: ## run tests quickly with the default Python
	python utils/readme.py
	pytest

test-all: ## run tests on every Python version with tox
	python utils/readme.py
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source tiktok_dl -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/tiktok_dl.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ tiktok_dl
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
	twine check dist/*

install: clean ## install the package to the active Python's site-packages
	python setup.py install
