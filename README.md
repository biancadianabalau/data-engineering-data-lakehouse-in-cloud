# E-Commerce Cloud - Data Lakehouse Project
Project Overview - in progress

An end-to-end Data Engineering pipeline that ingests, transforms, and standardizes e-commerce data from an on-premise PostgreSQL environment to a scalable Cloud Data Lakehouse on AWS S3 using Databricks.

## Architecture
The project follows the Medallion Architecture (Bronze -> Silver -> Gold) to ensure data quality and reliability.

Tech Stack
- Ingestion: Python (Pandas/SQLAlchemy), PostgreSQL.

- Cloud Storage: AWS S3 (Parquet & Delta formats).

- Data Processing: Databricks SQL, Apache Spark.

- Data Governance: Delta Lake (ACID Transactions, Time Travel).

- Orchestration: Airflow (Work in Progress).

## Pipeline Phases
### 1. Ingestion & Pre-processing
Original CSV datasets are loaded into PostgreSQL via Python.

A Python script extracts data from PostgreSQL and offloads it to AWS S3 as Parquet files to reduce storage costs and improve read performance.

### 2. Medallion Layering (Databricks)
- Bronze Layer: Raw data is registered in Databricks as external tables pointing to S3 Parquet files.

- Silver Layer: * Data cleaning: Whitespace removal (TRIM), case standardization (UPPER).

- Type Casting: Precision handling for financial data (DECIMAL), coordinates (DOUBLE), and timestamps (ISO 8601).

- Storage: The Silver layer is migrated back to S3 using the Delta Lake format, providing ACID compliance and schema enforcement.

## Key Features
- Data Integrity: Handled missing delivery timestamps as NULL to maintain business logic accuracy.

- Performance: Optimized storage by using Delta Lake, enabling faster queries and data versioning.

- Cloud Scalability: Decoupled compute (Databricks) from storage (S3).
