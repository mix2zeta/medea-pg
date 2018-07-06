FROM python:3.7.0-slim

COPY / /usr/src

RUN pip install -r /usr/src/requirements/base.txt /usr/src/requirements/dev.txt 