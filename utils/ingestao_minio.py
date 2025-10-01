from minio import Minio
from minio.error import S3Error
import os
from pathlib import Path
from loguru import logger

client = Minio(endpoint=os.getenv("S3_ENDPOINT", "minio:9000"),
               secret_key=os.getenv("S3_SECRET_KEY", "minio123"),
               access_key=os.getenv("S3_ACCESS_KEY", "minio123"),
               secure=False)

print(os.getenv("S3_ENDPOINT"))

def copy_files():
    PATH_DATA = Path("/usr/local/airflow/include/data/")
    for arquivo in PATH_DATA.rglob(pattern="*.csv"):
        try:
            if "crm" in str(arquivo).lower():
                client.fput_object(bucket_name="crm",
                                object_name=arquivo.name,
                                file_path=str(arquivo))
                
                logger.info(f"Arquivo {arquivo.name} movido com sucesso para o bucket CRM")
                
            elif "erp" in str(arquivo).lower():
                client.fput_object(bucket_name="erp",
                                object_name=arquivo.name,
                                file_path=str(arquivo))
                logger.info(f"Arquivo {arquivo.name} movido com sucesso para o bucket ERP")
        except S3Error as e:
            logger.error(e)

            

def configure_buckets():
    buckets_to_create = ["crm", "erp"]

    for bucket in buckets_to_create:
        if client.bucket_exists(bucket):
            logger.warning(f"Bucket {bucket} já existe.")
        else:
            client.make_bucket(bucket_name=bucket)
            logger.info(f"Bucket {bucket} criado com sucesso!")





