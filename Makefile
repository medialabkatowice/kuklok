.PHONY: default

default: lint run

APP = ./main.py
CSS = ./static/css/*css
JS  = ./static/js/*js
PYLINTRC = ./.pylintrc

initdb:
	make -C data init

lint: $(APP) $(PYLINTRC)
	@echo "-------------------------------"
	@echo ">>> Checking python source code"
	@echo "-------------------------------"
	pylint --rcfile $(PYLINTRC) $(APP)
	
	@echo "-------------------------------"
	pep8 --ignore=E127,E203,E221 $(APP)

run: $(APP)
	python $(APP)
