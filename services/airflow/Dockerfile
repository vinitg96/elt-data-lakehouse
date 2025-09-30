FROM astrocrpublic.azurecr.io/runtime:3.1-1

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
pip install --no-cache-dir dbt-duckdb  && deactivate


#RUN pip install --no-cache-dir dbt-core dbt-duckdb minio



