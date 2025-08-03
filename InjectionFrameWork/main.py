from sqlalchemy.sql.functions import current_time
from extract.postgresql import extract_postgresql
from extract.sqlserver import extract_sql_server
from extract.salesforce import extract_salesforce
from load.adls import upload_to_adls

def main():
    postgres_df = extract_postgresql()
    sql_df = extract_sql_server()
    sf_df, sf_parquet = extract_salesforce()
    upload_to_adls(postgres_df, sql_df, sf_parquet)
    print('Data extracted successfully.')
    print('Data Loaded successfully.')

if __name__ == "__main__":
    main()
