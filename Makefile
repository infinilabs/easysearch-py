clean:
	docker-compose down --remove-orphans --volumes

build:
	PYTHON_VERSION=${PYTHON_VERSION} docker-compose build client

pull:
	EASYSEARCH_VERSION=${EASYSEARCH_VERSION} PYTHON_VERSION=${PYTHON_VERSION} docker-compose pull

push:
	# requires authentication.
	PYTHON_VERSION=${PYTHON_VERSION} docker-compose push client

run_tests:
	EASYSEARCH_VERSION=${EASYSEARCH_VERSION} PYTHON_VERSION=${PYTHON_VERSION} docker-compose -p "${EASYSEARCH_VERSION}-${PYTHON_VERSION}" run client python setup.py test

start_easysearch:
	EASYSEARCH_VERSION=${EASYSEARCH_VERSION} docker-compose up -d easysearch
