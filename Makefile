.PHONY: up down recatch-files 

up: 
	docker compose up -d --build 

down:
	docker compose down 

recatch-files:
	docker compose exec airflow-dag-processor airflow dags reserialize
	docker compose exec airflow-dag-processor airflow dags list-import-errors
