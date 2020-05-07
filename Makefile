setup-env:
	pip3 install pipenv
	pipenv install

start:
	pipenv run python main.py

shell:
	pipenv run celery shell
