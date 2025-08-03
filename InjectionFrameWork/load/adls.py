from azure.storage.blob import BlobServiceClient
from io import StringIO

def upload_to_adls(postgres_df, sql_df, sf_parquet_path):
    blob_service_client = BlobServiceClient(
        account_url="https://postgressqls.blob.core.windows.net",
        credential="MYbUHYKYv2RSTmRM1qV6J9JfMl+YAhkVDwh9m3MSGYvbFYEy9CfE0zI/YWp92SbmNHmN4WXOnqQ1+AStmMyGvQ=="
    )
    container_client = blob_service_client.get_container_client("postgresinjection")

    # PostgreSQL
    buf_pg = StringIO()
    postgres_df.to_csv(buf_pg, index=False)
    container_client.upload_blob("path/to/postgress_data.csv", buf_pg.getvalue(), overwrite=True)

    # SQL Server
    buf_sql = StringIO()
    sql_df.to_csv(buf_sql, index=False)
    container_client.upload_blob("path/to/sqlserver_data.avro", buf_sql.getvalue(), overwrite=True)

    # Salesforce
    with open(sf_parquet_path, "rb") as f:
        container_client.upload_blob("path/to/sales_force_data.parquet", f, overwrite=True)
