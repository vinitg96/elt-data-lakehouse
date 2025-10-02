from airflow.sdk import DAG, task
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

args_ = {
    "owner": "Vinicius",
    "retries": 2
}

with DAG(
    dag_id='extract_load_minio', 
    start_date=datetime(2025, 9, 30), 
    default_args=args_,
    schedule="@once", 
    catchup=True,
    is_paused_upon_creation=False
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
    
    #acionar dag do dbt
    trigger_next_dag = TriggerDagRunOperator(
        task_id='trigger_transformation_dbt',
        trigger_dag_id='transformation_dbt',
        wait_for_completion=False
    )



    build_buckets() >> copy_files_minio() >> trigger_next_dag