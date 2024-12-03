clean:
	rm -rf dist

runserver:
	python devserver.py
	
build:
	python build.py
