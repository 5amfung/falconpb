# Makefile

RUN_ENV = . env/bin/activate

all: env

env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install --upgrade -r requirements.txt
	touch env/bin/activate

clean: clean_env clean_pyc

clean_env:
	rm -rf env

clean_pyc:
	find . -name '*.pyc' -delete
