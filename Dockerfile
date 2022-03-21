FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /party-rental
WORKDIR /party-rental

COPY requirements.txt ./
# COPY contrib/.env-sample .env
# RUN cp contrib/.env-sample .env
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


