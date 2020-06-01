FROM python:3

MAINTAINER CHANDU

COPY . /python

WORKDIR /python

ENV APP_HOST=127.0.0.1

ENV APP_PORT=8000

RUN  pip3 install -r requirements.txt

CMD  python3 -m unittest tests

CMD  python3 server.py

EXPOSE 8000
