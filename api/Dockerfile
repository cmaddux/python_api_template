FROM python:3

RUN mkdir api
WORKDIR ./api

# Install pipenv
RUN pip3 install pipenv

# Set encoding for pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Copy in Pipfile and lock file
COPY ./core/Pipfile ./Pipfile
COPY ./core/Pipfile.lock ./Pipfile.lock

# Install project dependencies
RUN set -ex && pipenv install --system

# Install pytest 
RUN set -ex && pipenv install pytest --dev

# Install uwsgi web server
RUN set -ex && pip3 install uwsgi

# Start uwsgi web server
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini" ]
