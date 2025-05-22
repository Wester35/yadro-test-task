FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends\
    gcc \
    python3-dev \
    libpq-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -l
RUN chmod -R 755 /app

EXPOSE 8008
