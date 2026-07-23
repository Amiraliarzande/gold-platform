FROM docker.arvancloud.ir/python:3.10-slim-buster

LABEL maintainer="Amirali Arzande"

ENV PYTHONUNBUFFERED=1

RUN groupadd -r app && useradd -r -g app app

WORKDIR /usr/src/app

COPY ./backend/requirements.txt .

RUN pip install -r requirements.txt

COPY --chown=app:app ./backend .

USER app