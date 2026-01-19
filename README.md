# E-Commerce Cloud - Data Lakehouse Project
Project Overview -

An end-to-end Data Engineering pipeline designed to automate the flow of e-commerce data. 
The system migrates raw data from an on-premise PostgreSQL environment to a scalable Cloud Data Lakehouse on AWS S3 using Apache Airflow for orchestration and Databricks/Spark for processing.

## Architecture & Design
The project implements the Medallion Architecture to ensure data integrity:

- Bronze (Raw): Landing zone for raw CSV/PostgreSQL data.

- Silver (Cleansed): Standardized, deduplicated, and typed data in Parquet/Delta format.

- Gold (Analytics): Business-ready tables for BI and reporting.

  <img width="1100" height="493" alt="architecture-docker-arhitectura drawio" src="https://github.com/user-attachments/assets/278e1ee2-7e02-4e42-8356-3e7b3142c46f" />

## 🛠 Tech Stack
- Orchestration: Apache Airflow (Dockerized).

- Ingestion: Python (Pandas & SQLAlchemy), PostgreSQL.

- Cloud Storage: AWS S3 (Optimized storage).

- Data Processing: Azure Databricks, Apache Spark SQL.

- Data Format: Delta Lake (ACID Transactions).

- Containerization: Docker & Docker Compose.



## Infrastructure & Setup (Installation Guide)
1. Prerequisites
- Docker Desktop installed.
- AWS Account: An S3 bucket and IAM User keys (Access Key & Secret Key).
- Databricks Workspace: Access to a cluster and a Personal Access Token (PAT).

2. Local Environment Setup (Airflow)
   
2.1 Clone the repository:
 in Bash: git clone https://github.com/yourusername/your-repo-name.git cd your-repo-name

2.2 Configure Environment Variables: Create a .env file in the root folder:
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
S3_BUCKET=your_bucket_name

2.3 Launch Airflow via Docker:
in Bash: docker-compose up -d

2.4 Access Airflow UI: 
Go to http://localhost:8085 (Username: admin, Password: admin).

3. Airflow Connections Setup
   
In the Airflow UI, go to Admin -> Connections and add:

databricks_default: Type Databricks, Host: your-databricks-url, Password: your-PAT-token.

aws_default: Type Amazon Web Services, Login: Access Key, Password: Secret Key.





## Pipeline Phases
### 1. Ingestion & Pre-processing
Original CSV datasets are loaded into PostgreSQL via Python.

A Python script extracts data from PostgreSQL and offloads it to AWS S3 as Parquet files to reduce storage costs and improve read performance.

### 2. Medallion Layering (Databricks)
- Bronze Layer: Raw data is registered in Databricks as external tables pointing to S3 Parquet files.

- Silver Layer: Data cleaning: Whitespace removal (TRIM), case standardization (UPPER).
  - Type Casting: Precision handling for financial data (DECIMAL), coordinates (DOUBLE), and timestamps (ISO 8601).
  - Storage: The Silver layer is migrated back to S3 using the Delta Lake format, providing ACID compliance and schema enforcement.
  
- Gold Layer: Data Modeling: Implementation of a Star Schema architecture consisting of 5 specialized tables (2 Fact tables and 3 Dimension tables) optimized for Business Intelligence
  - Fact Tables: Calculation of key financial metrics such as Total Order Value (Price + Freight) and multi-level granularity (Order-level vs. Item-level).
  - Dimension Tables: Enrichment of master data with performance tiers for sellers and geographical segmentation for customers.

 -Storage: Final analytical tables are materialized as External Delta Tables in S3, ensuring high-speed query performance for Power BI while maintaining low compute costs.

 <img width="800" height="750" alt="gold-layer drawio" src="https://github.com/user-attachments/assets/f092a48f-77e6-441a-a20d-42d16dcea09f" />


## Monitoring & Visuals (Screenshots)
##### 1. Airflow Pipeline (DAG)
The automated workflow successfully orchestrated:

<img width="1912" height="715" alt="graph dag" src="https://github.com/user-attachments/assets/07e8186c-cd20-4ece-a1b6-29132c8c3af3" />


##### 2. Docker Infrastructure
Multi-service setup running smoothly: 

<img width="1460" height="240" alt="docker" src="https://github.com/user-attachments/assets/00f99016-c418-4bc5-bf7c-be01c9f1d00c" />


##### 3. Data Lakehouse Structure (S3)
Decoupled storage in AWS S3: 
<img width="1892" height="789" alt="bronze" src="https://github.com/user-attachments/assets/c8cdb859-a3ca-43f6-b2a7-1f377ecf5abb" />
<img width="1902" height="653" alt="silver" src="https://github.com/user-attachments/assets/94726359-5f0d-4ddb-9afb-cb52dcfd45ee" />
<img width="1893" height="612" alt="gold" src="https://github.com/user-attachments/assets/2dd678e9-abb0-469d-8d12-cd714d4a63a8" />


## Key Features
- Data Integrity: Handled missing delivery timestamps as NULL to maintain business logic accuracy.

- Performance: Optimized storage by using Delta Lake, enabling faster queries and data versioning.

- Cloud Scalability: Decoupled compute (Databricks) from storage (S3).


## Data Source
This project utilizes the Brazilian E-Commerce Public Dataset by Olist, a comprehensive collection of 100k real-world anonymized orders from 2016 to 2018, providing a complex relational structure ideal for demonstrating large-scale data integration.

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/discussion?sort=hotness


<img width="800" height="626" alt="tables_relationshi drawio" src="https://github.com/user-attachments/assets/ae947aa7-0f49-4aa9-8b33-f6fb441f5ebe" />


