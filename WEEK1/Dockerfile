FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY pipe.py pipe.py 
COPY ./Data/green_tripdata_2021-09.csv /app/green_tripdata_2021-09.csv

ENTRYPOINT [ "python","pipe.py" ]