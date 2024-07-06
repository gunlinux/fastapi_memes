VERSION = 0.0.1

all: check

lint:
	flake8 blog app.py

pytest:
	FLASK_ENV=testing FLASK_APP=pro pytest

check: lint pytest

run:
	uvicorn memes_app.main:app --reload

docker-build:
	docker build . --tag="memes:$(VERSION)"

docker-shell:
	docker run --rm -it --entrypoint="" -p 8000:8000 memes:$(VERSION) sh 

docker-test:
	docker build --target test-image -t memes:$(VERSION)-test .
