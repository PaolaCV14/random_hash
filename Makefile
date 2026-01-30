install:
	pip install --upgrade pip

lint:
	python -m py_compile generate_hash.py

test:
	python generate_hash.py
