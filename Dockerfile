FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /blogging

ADD . /blogging

COPY ./requirments.txt /blogging/requirments.txt

RUN pip install -r requirments.txt

COPY . /blogging