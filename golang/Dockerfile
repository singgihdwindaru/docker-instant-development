FROM golang:alpine AS builder

LABEL stage=gobuilder

ENV CGO_ENABLED=0
ENV GOOS=linux

RUN apk update --no-cache 
RUN apk add --no-cache git

WORKDIR /build

COPY . .

RUN go mod tidy
RUN go build -o golang-app .

FROM alpine as final
WORKDIR /app
EXPOSE 8080
COPY --from=debug build/golang-app /app/golang-app
CMD ["./golang-app"]