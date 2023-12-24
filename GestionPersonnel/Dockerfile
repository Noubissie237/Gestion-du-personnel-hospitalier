FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

# RUN apt-get update 

RUN apt-get upgrade

RUN pip install --upgrade pip==23.0.1

RUN apt install -y openssl libssl-dev

RUN pip install -r requirements.txt