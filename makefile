infra:
	docker compose up -d

airflow:
	cd services/airflow && astro dev start
