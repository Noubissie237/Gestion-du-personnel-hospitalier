FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN apt-get update 

RUN apt-get upgrade

RUN apt install -y openssl libssl-dev

RUN pip install -r requirements.txt