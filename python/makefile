run-flask:
	@FLASK_APP=main.py python -m flask run --host=0.0.0.0 --port=8080

run-gunicorn:
	@gunicorn main:app

docker-build-debug:
	docker build \
  	--target=debug \
  	-t docker-instant-development/python-app:debug .


docker-run-debug:
	docker run -it -d \
	-v ${PWD}:/src \
	-p 8084:8080 \
	--name docker-instant-development-python-app docker-instant-development/python-app:debug \
	/bin/sh -c "FLASK_APP=main.py python -m flask run --host=0.0.0.0 --port=8080"

docker-build-publish:
	DOCKER_BUILDKIT=1 docker build \
	--target=production \
  	-t docker-instant-development/python-app:v2 .

docker-run-publish:
	docker run -it -d \
	-p 8084:8080 \
	--name docker-instant-development-python-app-publish docker-instant-development/python-app:latest