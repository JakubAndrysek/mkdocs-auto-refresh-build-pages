.PHONY: package release release-test clean reviewCode docs-serve docs-build

# Packaging
package:
	rm -f dist/*
	python3 -m build --wheel

install: package
	python3 -m pip install --no-deps --force dist/*.whl

install-dev: package
	python3 -m pip install --force --editable .

release: package
	twine upload --repository pypi dist/*

release-test: package
	twine upload --repository testpypi dist/*

clean:
	rm -rf dist build


fixRelativeLinkDocs:
	# change ./docs/ to ./
	sed  's/\.\/docs\//\.\//g' README.md > docs/README.md

# Testing
reviewCode:
	sourcery review mkdoxy --fix

# Documentation
docs-serve: fixRelativeLinkDocs
	mkdocs serve

docs-build: fixRelativeLinkDocs
	mkdocs build

docs-static-serve:
	cd site && python3 -m http.server 8001


docs-static-serve-public:
	cd site && python3 -m http.server 8001