.PHONY: default

default: init

init:
	@echo "-------------------------------"
	@echo ">>> Initializing sample data   "
	@echo "-------------------------------"
	sqlite3 sample_data.db < init_db.sql
	python generate_sample_data.py 2000
	python aggregate_sample_data.py

clean:
	@echo "-------------------------------"
	@echo ">>> Cleaning db                "
	@echo "-------------------------------"
	rm sample_data.db
