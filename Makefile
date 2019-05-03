all: stability-sim hysteresis-sim creation-sim

stability-sim:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python stability.py"

hysteresis-sim:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python hysteresis.py"

creation-sim:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python creation.py"

clean:
	rm -rf results/
