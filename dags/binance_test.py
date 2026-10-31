import duckdb
import pyarrow as pa
import pyarrow.parquet as pq
import requests
from airflow.sdk import dag, task

OUT = "/opt/airflow/data/binance_test.parquet"


@dag(schedule=None)
def binance():

    @task
    def fetch():
        response = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": "BTCUSDT", "interval": "5m", "limit": 288},
            timeout=30,
        )
        response.raise_for_status()
        rows = response.json()
        table = pa.table(
            {"open_time": [r[0] for r in rows], "close": [float(r[4]) for r in rows]}
        )
        pq.write_table(table, OUT)

    @task
    def query():
        print(duckdb.sql(f"SELECT count(*), min(close), max(close) FROM '{OUT}'"))

    fetch() >> query()


binance()
