FROM python:3.8-slim-buster

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .