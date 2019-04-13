PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
COVERAGE ?= coverage


config:
	$(PIP) install pycodestyle
	$(PIP) install coverage
	$(PIP) install flake8
	$(PIP) install twine


lint-pycodestyle:
	@echo "\n==> Pycodestyle Linting:"
	@find pywalrus -type f -name \*.py | while read file; do echo "$$file" && pycodestyle --config=./pycodestyle --first "$$file" || exit 1; done


lint-flake8:
	@echo "\n==> Flake8 Linting:"
	@find pywalrus -type f -name \*.py | while read file; do echo "$$file" && flake8 --config=flake8.ini "$$file" || exit 1; done


lint: lint-pycodestyle lint-flake8
	@echo "\n==> All linting cases passed!"


test:
	@echo "\n==> Run Test Cases:"
	$(PYTHON) setup.py test


coverage:
	$(COVERAGE) run --source='.' setup.py test
	$(COVERAGE) report -m


ci: test coverage lint
	@echo "\n==> All quality checks passed"


build:
	rm -rf build dist
	$(PYTHON) setup.py sdist bdist_wheel


upload:
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*


release:
	$(PYTHON) -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


test_install:
	$(PYTHON) -m pip install --index-url https://test.pypi.org/simple/ pywalrus


install:
	$(PYTHON) -m pip install pywalrus


develop:
	$(PYTHON) setup.py develop


.PHONY: ci
