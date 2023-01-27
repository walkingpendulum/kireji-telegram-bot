test:
	poetry run pytest .

format:
	poetry run black src tests

lint:
	poetry run mypy .
