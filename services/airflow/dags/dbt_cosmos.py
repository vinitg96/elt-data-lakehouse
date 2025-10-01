from cosmos import ProjectConfig, ProfileConfig, ExecutionConfig, DbtDag
import os
from datetime import datetime
from pathlib import Path

#posso apontar o profile ou usar connection do airflow para centralizar tudo
DBT_PROJECT_PATH = "/usr/local/airflow/include/dbt_workflow"
DBT_EXECUTABLE_PATH = os.getenv('AIRFLOW_HOME')

_project_config = ProjectConfig(dbt_project_path=DBT_PROJECT_PATH)

_profile_config = ProfileConfig(profile_name="dbt_workflow",
                                target_name="dev",
                                profiles_yml_filepath=Path(f"{DBT_PROJECT_PATH}/profiles.yml")
                                
                                )

_execute_file_config = ExecutionConfig(
    dbt_executable_path=f"/usr/local/airflow/dbt_venv/bin/dbt"
)

my_dag = DbtDag(
    dag_id="transformation_dbt",
    project_config=_project_config,
    profile_config = _profile_config,
    execution_config = _execute_file_config,
    schedule="@daily",
    start_date=datetime(2025,9,28),
    catchup=False,
    max_active_tasks=1

)