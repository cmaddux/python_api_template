# Example Docker Compose and Python API

This API template uses the following:

* docker
* docker-compose
* python 3
* pip 3
* pipenv
* uWSGI web server
* nginx web server
* flask web framework

## Run locally

1. Install docker (including docker-compose), instructions [here](https://docs.docker.com/install/)
2. Clone the repository
3. From project root, run `docker-compose up`
4. Visit [localhost:8080](http://localhost:8080)

## Setting up the makefile

To use the Makefile, replace the CONTAINER variable placeholder value in the makefile with the name of the container running the API. To find the name of the container running the API, use `docker ps`.

## Install new packages in container

To use the Makefile to install new packages in the container, first make sure the makefile is setup as stated above. From the projects `api/core` directory, run `make install-pkg PKG=[package_name]`.

## Run tests in container

To use the Makefile to run tests in the container, first make sure the makefile is setup as stated above. From the projects `api/core` directory, run `make test`.

## TODO

* Incorporate pylint/config
