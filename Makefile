all: stability hysteresis creation

stability:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python stability.py"

hysteresis:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python hysteresis.py"

creation:
	docker run -ti -v $$(pwd):/io marijanbeg/bloch_point:finmag bash -c "cd src; python creation.py"

clean:
	rm -rf results/
