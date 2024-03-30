docker-build--debug:
	docker build \
  	--target=debug \
  	--platform=linux/amd64 \
  	--build-arg TARGETARCH=linux-musl-x64 \
  	-t docker-instant-development/csharp:debug .

docker-run-debug:
	docker run -it -d \
	-v ${PWD}/TodoApi:/source \
	-p 8081:8080 \
	-e ASPNETCORE_URLS='http://+:8080' \
	--name docker-instant-development-csharp docker-instant-development/csharp:debug \
	/bin/sh -c "dotnet run"


docker-build-publish:
	docker build \
  	--platform=linux/amd64 \
  	--build-arg TARGETARCH=linux-musl-x64 \
  	-t docker-instant-development/csharp:latest .

publish-docker-run:
	docker run -it -d \
	-p 8081:8080 \
	--name docker-instant-development-csharp-publish docker-instant-development/csharp:latest