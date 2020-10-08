From python:3.8.5

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev

COPY requirements.txt /app/
COPY movies.csv /app/
COPY populate.py /app/

RUN pip install -r /app/requirements.txt

RUN mkdir movies_app
WORKDIR /movies_app

