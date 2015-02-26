# Makefile

RUN_ENV = . env/bin/activate
PYTHON = $(RUN_ENV); python
PROTOC = protoc
PROTOC_FLAGS = --proto_path=tests --python_out=tests

all: env

env: env/bin/activate
env/bin/activate: requirements.txt
	test -d env || virtualenv env
	. env/bin/activate; pip install --upgrade -r requirements.txt
	touch env/bin/activate

test: env pb
	$(PYTHON) setup.py develop
	$(RUN_ENV); `which nosetests` --verbose --with-coverage --cover-package=falconpb --where=tests
	$(PYTHON) setup.py develop --uninstall

pb:
	$(PROTOC) $(PROTOC_FLAGS) tests/PingResource.proto

clean: clean_env clean_pyc clean_generated_protos

clean_env:
	$(PYTHON) setup.py clean
	rm -rf env

clean_pyc:
	find . -name '*.pyc' -delete

clean_generated_protos:
	find . -name '*_pb2.py' -delete

build: env
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel --universal
