docker-build-debug:
	docker build \
  	--target=debug \
  	-t docker-instant-development/nodejs-app:debug .

docker-run-debug:
	docker run -it -d \
	-v ${PWD}:/src \
	-p 8082:8080 \
	--name docker-instant-development-nodejs-app docker-instant-development/nodejs-app:debug \
	/bin/sh -c "npm start"


docker-build-publish:
	docker build \
  	-t docker-instant-development/nodejs-app:latest .

publish-docker-run:
	docker run -it -d \
	-p 8082:8080 \
	--name docker-instant-development-nodejs-app-publish docker-instant-development/nodejs-app:latest