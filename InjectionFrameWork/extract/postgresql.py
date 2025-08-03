import pandas as pd
import psycopg2
from datetime import datetime

def extract_postgresql():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Sathish@1234"
    )
    query = "SELECT * FROM Ds_Injection"
    df = pd.read_sql_query(query, conn)
    df["injection_time"] = datetime.now()
    df["Owner"] = "DataSwitch"
    conn.close()
    return df
