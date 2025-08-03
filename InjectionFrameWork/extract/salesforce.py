import pandas as pd
from simple_salesforce import Salesforce

def extract_salesforce():
    sf = Salesforce(
        username='Sathishkumarmani@dataswitch.co',
        password='Sathish@1234',
        security_token='FL2Tj1tnXqipvUMiMPcx1m433'
    )
    data = sf.query("SELECT Id, Name, Industry FROM Account")
    records = data['records']
    for rec in records:
        rec.pop('attributes', None)
    df = pd.DataFrame(records)
    file_path = "account_data.parquet"
    df.to_parquet(file_path, index=False)
    return df, file_path
