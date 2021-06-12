FROM python:3.8

EXPOSE 5000

RUN apt-get update && apt-get install -y mariadb-client

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD python server.py
