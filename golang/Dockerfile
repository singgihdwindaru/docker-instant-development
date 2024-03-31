FROM golang:alpine AS debug

ENV CGO_ENABLED=0
ENV GOOS=linux

WORKDIR /source
# Download Go modules
COPY go.mod go.sum ./
RUN go mod download


FROM debug as publish
COPY . .
RUN go build -o /app/golang-app .

FROM alpine as final
WORKDIR /app
EXPOSE 8080
COPY --from=publish /app/golang-app /app/golang-app
CMD ["./golang-app"]