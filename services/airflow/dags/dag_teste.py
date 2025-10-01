from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from loguru import logger

# Função simples para teste
def teste_task():
    logger.info("Hello from Airflow test DAG!")
    print(f"Data atual: {datetime.now()}")

# Default args
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Criação da DAG
with DAG(
    dag_id="dag_teste_simples",
    default_args=default_args,
    description="DAG rápida para teste",
    start_date=datetime(2025, 9, 30),
    schedule=None,
    catchup=False,
) as dag:

    task_teste = PythonOperator(
        task_id="task_teste",
        python_callable=teste_task,
    )

    task_teste
