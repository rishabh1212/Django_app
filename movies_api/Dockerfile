From python:3.8.5

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

RUN mkdir movies_api
WORKDIR /movies_api

COPY movies.csv /movies_api/
COPY populate.py /movies_api/
COPY movies_api /movies_api/movies_api
COPY movies_app /movies_api/movies_app
COPY populate.py /movies_api/
COPY manage.py /movies_api/

COPY run.sh /
RUN chmod +x /run.sh
