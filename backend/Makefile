.PHONY: install run dev test freeze clean

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app

dev:
	uvicorn app.main:app --reload

test:
	pytest

freeze:
	pip freeze > requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
