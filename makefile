build:
	pip install pytest

run:
	python RadixSort_Strings.py input.txt

test: 
	pytest test_sort_algorithms.py