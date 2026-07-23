FROM docker.arvancloud.ir/node:24-alpine

WORKDIR /usr/src/app

COPY ./frontend/package*.json ./

RUN npm ci

COPY ./frontend .

RUN chown -R node:node /usr/src/app

USER node

EXPOSE 3000