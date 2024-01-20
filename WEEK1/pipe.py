# import pandas as pd
# from sqlalchemy import create_engine

# engine=create_engine('postgresql://root:shekhar@localhost:5432/nyc_taxi')

# print(pd.__version__)
# df=pd.read_csv("green_tripdata_2021-01.csv")
# print(df.head())
# print(df.shape)
# df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
# df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)
# print(pd.io.sql.get_schema(df,name="green_taxi_data",con=engine))


# df_iter=pd.read_csv("green_tripdata_2021-01.csv",iterator=True,chunksize=10000)
# df=next(df_iter)

# len(df)
# print(df.head())
# print(df.shape)

# df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
# df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)
# df.to_sql(name="green_taxi_data",con=engine,if_exists='replace')

import pandas as pd
from sqlalchemy import create_engine
from time import time
print(pd.__version__)

#Connecting to postgres database
engine=create_engine('postgresql://root:shekhar@localhost:5432/nyc_taxi')

df= pd.read_csv(r'green_tripdata_2021-01.csv')
df.lpep_pickup_datetime=pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime=pd.to_datetime(df.lpep_dropoff_datetime)

print(df.head())  
#Creating schema statement
print(pd.io.sql.get_schema(df,name='green_taxi_data',con=engine))

print('Starting chunkwise insertion into postgres db nyc_taxi ')
#Doing it Chunk wise
df_iter= pd.read_csv('green_tripdata_2021-01.csv',iterator=True,chunksize=20000)
    
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
        df_chunk.to_sql(name='green_taxi_data', con=engine, if_exists='append', index=False)
        t_end = time()
        print(f'Inserted Chunk number {i}, took {t_end - t_start}')
        print(f'Shape and Size {df_chunk.shape}')

except StopIteration:
    print("No more chunks to read. Process completed.")
