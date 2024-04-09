# syntax=docker/dockerfile:1
# Keep this syntax directive! It's used to enable Docker BuildKit

FROM python:3.8-slim-buster as debug
WORKDIR /src
COPY pyproject.toml poetry.lock ./
RUN pip install poetry==1.5.1 && \
    poetry config virtualenvs.create false && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install --no-cache-dir -r requirements.txt 

# The runtime image, used to just run the code provided its virtual environment
FROM debug as production
WORKDIR /app
COPY . /app
CMD ["gunicorn", "main:app"]