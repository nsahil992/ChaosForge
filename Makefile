.PHONY: run install freeze

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run:
	python app/app.py