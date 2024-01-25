# DEZoomCamp


docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="shekhar" \
-e POSTGRES_DB="nyc_taxi" \
-v /d/DEZoomCamp/WEEK1/my_taxi_postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:13


$ docker exec -it 6c437afc0ab92592f4da17f0b5977043eabc95cd63d0e9c271d73fe3c69799e0 psql -U root -d nyc_taxi



/Create network    
docker network create pg-network

docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="shekhar" \
-e POSTGRES_DB="nyc_taxi" \
-v /d/DEZoomCamp/WEEK1/my_taxi_postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13


creating a pgadmmin container

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="shekhar@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="shekhar" \
    -p 8080:80 \
    --network=pg-network \
    --name pg-admin \
    dpage/pgadmin4



python pipe.py \
    --user=root \
    --password=shekhar \
    --host=localhost \
    --port=5432 \
    --db=nyc_taxi \
    --table_name=green_taxi_data 

docker build -t taxi_ingest:v001 .

#docker image to run python pipe.py

docker run -it \
    --network=pg-network \
    --name=ingestion_pipeline \
    taxi_ingest:v001 \
        --user=root \
        --password=shekhar \
        --host=pg-database \
        --port=5432 \
        --db=nyc_taxi \
        --table_name=green_taxi_data 


Terraform Commands
init-Get the provider i need
plan-What am i about to do?
apply-Do what is in the terraform files
destroy-Delete everything in teraform file



"C:\Users\HP\Downloads\terraform_1.7.1_windows_386"
cp ~/Downloads/terraform_1.7.1_windows_386 /usr/local/bin/
cp /c/Users/HP/Downloads/terraform_1.7.1_windows_386 /usr/bin/

"C:\Users\HP\Downloads\terraform_1.7.1_windows_386\terraform.exe"

"C:\Users\HP\Downloads\terraform_1.7.1_linux_386"


#terraform format
terraform fmt