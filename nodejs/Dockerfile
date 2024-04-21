# syntax=docker/dockerfile:1
# Keep this syntax directive! It's used to enable Docker BuildKit
FROM node:14-alpine AS debug
WORKDIR /src
COPY package*.json ./
RUN npm install

FROM debug as publish
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "start:prod"]
