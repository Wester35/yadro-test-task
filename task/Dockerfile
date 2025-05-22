FROM python:3.12-slim

WORKDIR /app/task

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY task/ .

RUN ls -l

EXPOSE 8008
