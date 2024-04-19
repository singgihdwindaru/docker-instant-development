# syntax=docker/dockerfile:1
# Keep this syntax directive! It's used to enable Docker BuildKit
FROM node:14 AS debug

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

FROM debug as publish

RUN npm run build

CMD ["npm", "run", "start:prod"]
