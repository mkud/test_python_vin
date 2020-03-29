FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV TEST_SERVER_URL=https://s3-eu-west-1.amazonaws.com/coding-challenge.carfax.eu/

LABEL maintainer="Maksim Kudimov"

RUN pip install 'ujson==2.0.3'

COPY main.py /app/
