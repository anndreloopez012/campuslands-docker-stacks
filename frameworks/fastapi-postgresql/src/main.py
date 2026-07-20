import os
from fastapi import FastAPI
import psycopg

app = FastAPI()

@app.get("/")
def root():
    conn = psycopg.connect(host="postgres", dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), password=os.getenv("POSTGRES_PASSWORD"))
    with conn.cursor() as cur:
        cur.execute("select now()")
        now = cur.fetchone()[0]
    conn.close()
    return {"stack": "FastAPI + PostgreSQL", "db_time": str(now)}
