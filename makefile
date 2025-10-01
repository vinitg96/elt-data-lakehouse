infra:
	chmod 777 ./services/dbt_workflow/datawarehouse/ && \
	docker compose up -d

airflow:
	cd services/airflow && astro dev start


	
