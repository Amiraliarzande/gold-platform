FROM docker.arvancloud.ir/node:24-alpine

WORKDIR /usr/src/app

COPY ./frontend/package*.json ./

RUN npm ci

COPY ./frontend .

EXPOSE 3000