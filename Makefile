.PHONY: clean sync requirements runserver build

clean:
	rm -rf build

sync:
	uv sync

# generated from uv.lock for the cloudflare pages build, which installs with pip
requirements.txt: uv.lock
	uv export --no-hashes --no-dev --no-emit-project -o $@

requirements: requirements.txt

runserver:
	uv run devserver.py

build: requirements.txt
	uv run build.py
