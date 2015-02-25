# Makefile

RUN_ENV = . env/bin/activate
PROTOC = protoc
PROTOC_FLAGS = --proto_path=src/tests --python_out=src/tests

all: env

env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install --upgrade -r requirements.txt
	touch env/bin/activate

test: env pb
	$(RUN_ENV); nosetests --verbose --with-coverage --cover-package=falconpb --where=src/tests

pb:
	$(PROTOC) $(PROTOC_FLAGS) src/tests/FooResource.proto

clean: clean_env clean_pyc

clean_env:
	rm -rf env

clean_pyc:
	find . -name '*.pyc' -delete
