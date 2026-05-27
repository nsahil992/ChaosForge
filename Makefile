.PHONY: run install freeze

APP_NAME = chaosforge
VERSION ?= 2.1.0

DOCKER_USERNAME ?= nsahil992
IMAGE = $(DOCKER_USERNAME)/$(APP_NAME):$(VERSION)

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

run:
	python app/app.py

validate:
	python -m py_compile app/app.py

# ----- DOCKER TARGETS -----
docker-test:
	hadolint Dockerfile

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run -p 5050:5050 $(IMAGE)

docker-tag:
	docker tag $(IMAGE) $(IMAGE)

docker-push:
	docker push $(IMAGE)

# ----- DOCKER COMPOSE TARGETS -----

compose-up:
	docker compose up

compose-down:
	docker compose down

