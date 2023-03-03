develop:  ## install dependencies
	pip install -r requirements.txt
format:
	black splotify/
lint:  ## run static analysis with flake8
	flake8 splotify/
test: ## clean and run unit tests
	coverage run -m pytest
	coverage report