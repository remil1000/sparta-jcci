run:
	docker run --rm \
		-p 5004:5004 \
		-v$(PWD)/data:/app/data \
		-e SPARTA_EXPOSED_HOST=localhost \
		-e SPARTA_ORG=my-organization \
		sparta-jcci:latest

image:
	docker build -t sparta-jcci:latest .
