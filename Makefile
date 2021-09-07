
build-package:
	python setup.py sdist
	./setup.py bdist_wheel
	python setup.py build