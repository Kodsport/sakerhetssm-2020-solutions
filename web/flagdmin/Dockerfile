FROM node:latest

RUN apt-get update && apt-get install -y redis-server

WORKDIR /usr/src/app

COPY src/package*.json ./

RUN npm install

COPY src/ .

RUN npm run build

EXPOSE 6969

CMD [ "node", "build/app.js" ]