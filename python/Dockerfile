FROM python:3.10-alpine

WORKDIR /app
COPY . /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install --no-cache-dir -r requirements.txt
    
# Command to run the Python application
EXPOSE 8080
CMD ["python", "app.py"]