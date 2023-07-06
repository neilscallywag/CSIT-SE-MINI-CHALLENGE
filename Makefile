include .env

build: build/python

build/python:
	docker build . -t neilscallywag/${PROJECT_NAME}_python_backend:${VERSION} -f python/Dockerfile
	
up:
	docker-compose -f python/docker-compose.yml up -d

down:
	docker-compose -f python/docker-compose.yml down 