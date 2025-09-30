# # import sys
# # sys.path.insert(0, '/usr/local/airflow/include')

# # from airflow.sdk import DAG, task
# # from datetime import datetime

# # from ingestao import bucket_build
# # from airflow.providers.standard.operators.bash import BashOperator


# # Configurações padrão do DAG
# args_ = {
#     "owner": "Vinicius",
#     "retries": 2
# }

# with DAG(
#     dag_id='extract-load-transform', 
#     start_date=datetime(2025, 9, 28), 
#     default_args=args_, # Execução manual
#     catchup=False
# ) as dag:

#     @task
#     def ingestao_task():
#         """Task para executar a ingestão de dados"""
#         bucket_build()
#         return "Ingestão concluída com sucesso"

#     # Operator para executar dbt
#     dbt_run = BashOperator(
#         task_id='dbt_run',
#         bash_command='cd /usr/local/airflow/include/dbt_workflow && dbt run'
#     )

#     # Definir dependências
#     ingestao_task() >> dbt_run

from airflow.sdk import DAG, task
from datetime import datetime
from airflow.providers.standard.operators.bash import BashOperator

# Sem imports problemáticos no nível do módulo

# Configurações padrão do DAG
args_ = {
    "owner": "Vinicius",
    "retries": 2
}

with DAG(
    dag_id='extract-load-transform', 
    start_date=datetime(2025, 9, 28), 
    default_args=args_,
    schedule=None,  # Mudou de schedule_interval para schedule
    catchup=False
) as dag:

    @task
    def ingestao_task():
        """Task para executar a ingestão de dados"""
        # Import dentro da função para evitar problemas de cache
        import sys
        sys.path.insert(0, '/usr/local/airflow/include')
        from ingestao import bucket_build
        
        bucket_build()
        return "Ingestão concluída com sucesso"

    # # Operator para executar dbt
    # dbt_run = BashOperator(
    #     task_id='dbt_run',
    #     bash_command='cd /usr/local/airflow/include/dbt_workflow && dbt run'
    # )


#     dbt_run = BashOperator(
#         task_id="dbt_run",
#         bash_command="pwd && ls -lha && which dbt && dbt --version && dbt run",
#         env={"DBT_PROFILES_DIR": "/usr/local/airflow/include/dbt_workflow"},
#         cwd="/usr/local/airflow/include/dbt_workflow"  # garante o diretório
# )

#     # Definir dependências
#     ingestao_task() >> dbt_run