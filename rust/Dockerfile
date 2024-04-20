# build stage
FROM rust:1.75.0 AS builder
WORKDIR /usr/src/

# install musl tools
RUN apt-get update && \
    apt-get install -y musl-tools pkg-config libssl-dev

RUN rustup target add x86_64-unknown-linux-musl

RUN USER=root cargo new hello_world
WORKDIR /usr/src/hello_world
COPY Cargo.toml ./
RUN cargo build --release

# ENV OPENSSL_DIR /usr/include/openssl

COPY src ./src
RUN cargo install --target x86_64-unknown-linux-musl --path .

# bundle stage
FROM scratch
COPY --from=builder /usr/local/cargo/bin/hello_world .
USER 1000
CMD ["./hello_world", "-a", "0.0.0.0", "-p", "8080"]
