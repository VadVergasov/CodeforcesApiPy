RMDIR /Q /S build
RMDIR /Q /S dist
RMDIR /Q /S CodeforcesApiPy.egg-info
python setup.py sdist bdist_wheel
twine check dist/*
