#!/bin/env sh
set -euo pipefail
IFS=$'\n\t'

rm -rf venv

virtualenv2 venv
./venv/bin/pip install -e .
./venv/bin/pip install 'Django>=1.11,<1.12'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.10,<1.11'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.9,<1.10'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.8,<1.9'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
rm -rf venv

virtualenv3 venv
./venv/bin/pip install -e .
./venv/bin/pip install 'Django>=1.11,<1.12'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.10,<1.11'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.9,<1.10'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
./venv/bin/pip install 'Django>=1.8,<1.9'
DJANGO_SETTINGS_MODULE='django_statsd.test_settings' venv/bin/python setup.py test
rm -rf venv
