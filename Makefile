develop:  ## install dependencies
	pip install -r requirements.txt
format: # autoformat with black
	black splotify/
lint:  ## run static analysis with flake8
	flake8 splotify/
test: ## run tests with coverage stats
	coverage run -m pytest
	coverage report