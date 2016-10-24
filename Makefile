test:
	venv/bin/python -m example_tests

flake8:
	venv/bin/flake8 --max-line-length=119 --exclude=venv .

venv:
	virtualenv --python=python3 venv

install: venv
	venv/bin/pip install -r requirements.txt
