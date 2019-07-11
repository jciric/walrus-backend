FROM python:3.7-alpine
MAINTAINER Jovana Ciric

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /walrus
WORKDIR /walrus
COPY ./walrus/ /walrus

RUN adduser -D walrus
USER walrus