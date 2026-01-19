import pandas as pd
from sqlalchemy import create_engine
import boto3
from io import BytesIO


S3_BUCKET = "etl-project3-data-warehouse-in-cloud"
AWS_ACCESS_KEY = "YOUR_AWS_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_AWS_SECRET_KEY"

DB_URL = 'postgresql://airflow:airflow@postgres:5432/airflow'
s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def upload_to_s3_as_parquet( schema='public'):
    
    engine = create_engine(DB_URL)

    tables_to_process = [
        'customers', 'products', 'sellers', 'orders', 
        'order_items', 'order_payments', 'order_reviews', 
        'geolocation', 'product_category_translation'
    ]

    for table_name in tables_to_process:
        print(f"Processing the table.: {table_name}")

        try:
            df = pd.read_sql(f"SELECT * FROM {schema}.{table_name}", engine)
            if df.empty:
                print(f"Warning: Table {table} is empty. Skipping.")
                continue
        
            parquet_buffer = BytesIO()
            df.to_parquet(parquet_buffer, index=False, engine='pyarrow')
            
            s3_key = f"bronze/{table_name}/{table_name}.parquet"
            s3_client.put_object(
                Bucket=S3_BUCKET, 
                Key=s3_key, 
                Body=parquet_buffer.getvalue()
            )
            print(f"Succes! {table_name} uploaded in s3://{S3_BUCKET}/{s3_key}")

        except Exception as e:
            print(f"Error processing {table_name}: {e}")
            continue   
    return True

