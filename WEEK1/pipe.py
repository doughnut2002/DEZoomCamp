
import pandas as pd
from sqlalchemy import create_engine
from time import time
import os
print(pd.__version__)
import argparse

def main(params):
    user =params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    
    #this is for docker image execution without docker yaml
    # csv_name='/app/green_tripdata_2021-01.csv'
    # os.system(f"wget {url} -O {csv_name}")
    # os.system(f"curl -LJO {url}")

    csv_name="./Data/green_tripdata_2019-09.csv"

    
    print('Starting chunkwise insertion into postgres db nyc_taxi ')
    #Connecting to postgres database
    engine=create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # df= pd.read_csv(r'green_tripdata_2021-01.csv')
    # df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
    # df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)

    df_iter= pd.read_csv(csv_name,iterator=True,chunksize=20000)
    # print(df_iter.head())  
        
    i = 0
    try:
        while True:
            t_start = time()
            df_chunk = next(df_iter)
            i += 1

            # Converting into datetime format
            df_chunk['lpep_pickup_datetime'] = pd.to_datetime(df_chunk['lpep_pickup_datetime'])
            df_chunk['lpep_dropoff_datetime'] = pd.to_datetime(df_chunk['lpep_dropoff_datetime'])

            # Ingesting data into PostgreSQL
            df_chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            t_end = time()
            print(f'Inserted Chunk number {i}, took {t_end - t_start}')
            print(f'Shape and Size {df_chunk.shape}')

    except StopIteration:
        print("No more chunks to read. Process completed.")

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name')
    parser.add_argument('--password', help='password')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')

    args = parser.parse_args()
    main(args)