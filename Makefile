IPYNBPATH=figures/*.ipynb
PYTHON?=python3

all: stability hysteresis creation

stability:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python stability.py"

hysteresis:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python hysteresis.py"

creation:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python creation.py"

test-ipynb:
	$(PYTHON) -m pytest --nbval-lax $(IPYNBPATH)

travis-build:
	docker build -f docker/Dockerfile -t dockertestimage .
	docker run -e ci_env -ti -d --name testcontainer dockertestimage
	docker exec testcontainer make test-ipynb
	docker stop testcontainer
	docker rm testcontainer

load-image:
	docker load < bloch_point.tar.gz

clean:
	rm -rf results/
