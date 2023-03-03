develop:  ## install dependencies
	pip install -r requirements.txt
setup: ## get authorization token needed to run tests
	python3 splotify/main.py
test: setup ## run tests with coverage stats
	pytest --cov=splotify/ splotify/tests/
format: # autoformat with black
	black splotify/
lint:  ## run static analysis with flake8
	flake8 splotify/