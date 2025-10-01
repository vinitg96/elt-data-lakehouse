from minio import Minio
import os
from pathlib import Path
from loguru import logger

client = Minio(endpoint=os.getenv("S3_ENDPOINT"),
               secret_key=os.getenv("S3_SECRET_KEY"),
               access_key=os.getenv("S3_ACCESS_KEY"))


# PATH_DATA = Path("../data/")

# for arquivo in PATH_DATA.rglob(pattern="*.csv"):
def configure_buckets():
    buckets_to_create = ["CRM", "ERP"]

    for bucket in buckets_to_create:
        if client.bucket_exists():
            logger.warning(f"Bucket {bucket} já existe.")
        else:
            client.make_bucket(bucket_name=bucket)
            logger.info(f"Bucket {bucket} criado com sucesso!")







