setup:
	pipenv install --dev python=3.9

quality_check:
	isort .
	black .
	pylint --recursive=y .

test:
	pytest tests
