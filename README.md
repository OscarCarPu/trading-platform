# Trading Platform 

Data platform for loading and preparing market data, foundation for future trading 

## Stack 

| Function | Tech |
| ---|---|
| Orchestration | Airflow |
| Processing | Spark |
| Storage | Parquet |
| Query and exploration interface | DuckDB |

## Initial Scope 

- Scheduled loading of historical market data 
- Historical backfills 
- Cleaning and normalization
- Data validation 
- Exploratory querying

## Setup 

```bash
cp .env.example .env 
sed -i "s/^AIRFLOW_UID=.*/AIRFLOW_UID=$(id -u)/" .env 
sed -i "s/^AIRFLOW__API_AUTH__JWT_SECRET=.*/AIRFLOW__API_AUTH__JWT_SECRET=$(openssl rand -hex 32)/" .env
make up

```

| UI | URL |
|---|---|
| Airflow | http://localhost:8080 |
| Spark master | http://localhost:8081 |
| Spark worker | http://localhost:8082 |

- `make recatch-files`: load new or changed DAGs from `dags/` straight away and show import errors 
- `make down`: stop the stack (data and the Airflow DB are kept)


## More Docs 

- [Plan](docs/plan.md)
- [Architecture](docs/architecture.md)
