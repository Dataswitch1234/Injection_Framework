import pandas as pd
import pyodbc
from datetime import datetime

def extract_sql_server():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-4655J13\\MSKN_NANDHINI;"
        "DATABASE=Finance_Data;"
        "UID=Sathish;"
        "PWD=Sathish1234;"
    )
    df = pd.read_sql("SELECT * FROM loans", conn)
    df["injection_time"] = datetime.now()
    df["Owner"] = "DataSwitch"
    conn.close()
    return df
