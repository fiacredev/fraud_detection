.PHONY: install dev test lint train run docker-up docker-down

install:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check .

train:
	python train.py

run:
	uvicorn app:app --reload

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down
