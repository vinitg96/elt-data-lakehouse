from minio import Minio
from minio.error import S3Error 
import os
from loguru import logger
from pathlib import Path

def bucket_build():

    client = Minio(endpoint=os.getenv("S3_ENDPOINT", "localhost:9000"),
                access_key=os.getenv("S3_ACCESS_KEY", "minio123"),
                secret_key=os.getenv("S3_SECRET_KEY", "minio123"),
                secure=False)

    #files_path = "/data/raw/"
    files_path = "/usr/local/airflow/include/data/"
    bucket_names = ["crm", "erp"]

    for bucket_name in bucket_names:
        if client.bucket_exists(bucket_name):
            logger.warning(f"Bucket {bucket_name} já existe")
        else:
            client.make_bucket(bucket_name)
            logger.info(f"Bucket {bucket_name} criado com sucesso")

    #copiar arquivos
    path = Path(files_path)
    for arquivo in path.rglob("*.csv"):
        if "erp" in str(arquivo):
            client.fput_object(bucket_name="erp", object_name=arquivo.name, file_path=arquivo)
            logger.info(f"Arquivo {arquivo.name} movido com sucesso para o bucket erp")
        elif "crm" in str(arquivo):
            client.fput_object(bucket_name="crm", object_name=arquivo.name, file_path=arquivo)
            logger.info(f"Arquivo {arquivo.name} movido com sucesso para o bucket crm")
        else:
            logger.warning(f"Arquivo {arquivo.name} deve estar dentro do diretorio erp ou crm")

    