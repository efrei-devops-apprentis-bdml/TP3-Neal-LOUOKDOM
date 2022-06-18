FROM python:slim-buster

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir requests==2.27.1 hug==2.6.1

CMD hug -f meteo.py
