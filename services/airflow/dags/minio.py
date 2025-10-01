from airflow.sdk import DAG, task
from datetime import datetime
#from airflow.providers.standard.operators.bash import BashOperator


# Sem imports problemáticos no nível do módulo

# Configurações padrão do DAG
args_ = {
    "owner": "Vinicius",
    "retries": 2
}

with DAG(
    dag_id='extract_load_minio', 
    start_date=datetime(2025, 9, 28), 
    default_args=args_,
    schedule=None,  # Mudou de schedule_interval para schedule
    catchup=False
) as dag:

    @task
    def build_buckets():
        import sys
        sys.path.insert(0, '/usr/local/airflow')
        from ingestao_minio import configure_buckets
        """Task para executar a ingestão de dados"""

        
        configure_buckets()
        return "Configuração dos Buckets Concluidas Com sucesso"


    @task
    def copy_files_minio():
        import sys
        sys.path.insert(0, '/usr/local/airflow')
        from ingestao_minio import copy_files
        copy_files()
        return "Ingestão concluída com sucesso"



    build_buckets() >> copy_files_minio()