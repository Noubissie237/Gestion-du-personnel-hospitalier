FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt