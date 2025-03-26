.PHONY : docs
docs :
	rm -rf docs/build/
	sphinx-autobuild -b html --watch envmodel/ docs/source/ docs/build/

.PHONY : run-checks
run-checks :
	isort --check .
	ruff format --check .
	ruff check .
	mypy .
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ envmodel/

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build
