TMPREPO=/tmp/docs/cordeliachen

develop:  ## install dependencies
	python3 -m pip install .'[develop]'
build:  ## build the python library
	python3 setup.py build build_ext --inplace 
install: ## install library
	python3 -m pip install .
run: ## run main.py
	python3 splotify/main.py
test: ## run tests with coverage stats
	python3 -m pytest --cov=splotify/ splotify/tests/
format: # autoformat with black
	python3 -m black splotify/
lint:  ## run static analysis with flake8
	python3 -m flake8 splotify/

## VERSION
patch:
	bump2version patch
minor:
	bump2version minor
major:
	bump2version major

## DOCS
docs:
	$(MAKE) -C docs/ clean
	$(MAKE) -C docs/ html

pages:
	rm -rf $(TMPREPO)
	git clone -b gh-pages https://github.com/cordeliachen/splotify.git $(TMPREPO)
	rm -rf $(TMPREPO)/*
	cp -r docs/_build/html/* $(TMPREPO)
	cd $(TMPREPO);\
	touch .nojekyll;\
	git add -A ;\
	git commit -a -m 'auto-updating docs' ;\
	git push