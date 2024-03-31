docker-build--debug:
	docker build \
  	--target=debug \
  	-t docker-instant-development/golang-app:debug .

docker-run-debug:
	docker run -it -d \
	-v ${PWD}:/source \
	-p 8082:8080 \
	--name docker-instant-development-golang-app docker-instant-development/golang-app:debug \
	/bin/sh -c "go run ."


docker-build-publish:
	docker build \
  	-t docker-instant-development/golang-app:latest .

publish-docker-run:
	docker run -it -d \
	-p 8082:8080 \
	--name docker-instant-development-golang-app-publish docker-instant-development/golang-app:latest