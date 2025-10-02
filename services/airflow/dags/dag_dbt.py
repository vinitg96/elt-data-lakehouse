from cosmos import ProjectConfig, ProfileConfig, ExecutionConfig, DbtTaskGroup
from airflow.sdk import DAG
from datetime import datetime
from pathlib import Path

DBT_PROJECT_PATH = "/usr/local/airflow/include/dbt_workflow"

_project_config = ProjectConfig(dbt_project_path=DBT_PROJECT_PATH)

_profile_config = ProfileConfig(
    profile_name="dbt_workflow",
    target_name="dev",
    profiles_yml_filepath=Path(f"{DBT_PROJECT_PATH}/profiles.yml")
)

_execute_file_config = ExecutionConfig(
    dbt_executable_path=f"/usr/local/airflow/dbt_venv/bin/dbt"
)


with DAG(
    dag_id="transformation_dbt",
    schedule=None, # removi o @once pq ela deve ser acionada pela dag anterior. Antes era executada 2x
    start_date=datetime(2025, 9, 28),
    catchup=False,
    max_active_tasks=1,
    max_active_runs=1,
    is_paused_upon_creation=False
) as dag:
    

    dbt_tasks = DbtTaskGroup(
        group_id='dbt_transformation',
        project_config=_project_config,
        profile_config=_profile_config,
        execution_config=_execute_file_config,
    )
    