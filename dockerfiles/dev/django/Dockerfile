FROM docker.arvancloud.ir/python:3.10-slim-buster

LABEL maintainer="Amirali arzande"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY  ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY  ./backend .