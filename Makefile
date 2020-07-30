build-api:
	docker build -t graph-api -f Dockerfile.api .

run-api: build-api
	docker run -p 8000:8000 --rm -ti graph-api
