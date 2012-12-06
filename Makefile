.PHONY: default

default: lint run

APP = ./main.py
CSS = ./static/css/*css
JS  = ./static/js/*js
PYLINTRC = ./.pylintrc

lint: $(APP) $(PYLINTRC)
	@echo "-------------------------------"
	@echo ">>> Checking python source code"
	@echo "-------------------------------"
	pylint --rcfile $(PYLINTRC) $(APP)
	
	@echo "-------------------------------"
	pep8 --ignore=E203,E221 $(APP)

run: $(APP)
	python $(APP)
