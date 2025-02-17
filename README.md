# README: Expanded 3-Hour Python + dbt + Terraform + NoSQL Exercise

## Objective
Design and implement an end-to-end data pipeline that processes raw e-commerce data from multiple sources, transforms and validates the data, and stores it in a cloud-based reporting system. The assessment will test:

1. Python programming skills, including regex, JSON parsing, and log processing.
2. Proficiency in dbt for data modeling and transformation.
3. Ability to work with NoSQL data sources.
4. Data modeling and normalization expertise.
5. Infrastructure setup using Terraform.

---

## Assessment Breakdown

### Total Time: 3 Hours

- **Part 1 (45 minutes):** Data ingestion and regex/JSON processing.
- **Part 2 (45 minutes):** Log processing and integration with a NoSQL source.
- **Part 3 (1 hour):** Data transformation and modeling using dbt.
- **Part 4 (30 minutes):** Infrastructure setup with Terraform.
- **Bonus Task (Optional):** Advanced validation and monitoring.

---

## Project Scenario

You are tasked with building a pipeline for an e-commerce company that collects sales and customer interaction data from multiple sources:

1. A **CSV file** containing sales transactions.
2. A **JSON-based API** providing customer behavior logs.
3. A **NoSQL database** storing product catalog information (e.g., MongoDB).

The goal is to:
1. Normalize and clean the data from all sources.
2. Aggregate key metrics like daily revenue per product, customer activity patterns, and product popularity.
3. Store the cleaned and transformed data in a **BigQuery reporting table** for analysis.

---

## Part 1: Data Ingestion and Regex/JSON Parsing (45 minutes)

### Tasks

1. Write a Python script to:
   - Read raw sales data from a CSV file.
   - Parse a JSON file (or API response) containing customer activity logs. Each log entry includes:
     - `timestamp`
     - `user_id`
     - `event_type` (e.g., "click", "purchase", "view")
     - `metadata` (a JSON object with nested details).
   - Extract fields like `timestamp` and `user_id` using **regex** from improperly formatted logs.
   - Normalize the JSON `metadata` field into flat columns.

2. Clean and validate the data:
   - Handle missing or malformed fields.
   - Write the cleaned data to a **staging table** in BigQuery.

---

## Part 2: Log Processing and NoSQL Integration (45 minutes)

### Tasks

1. Simulate a log processing pipeline:
   - Parse a sample log file containing JSON lines.
   - Extract meaningful insights such as:
     - Number of events per user.
     - Most common `event_type`.

2. Integrate a NoSQL source (e.g., MongoDB or DynamoDB):
   - Connect to a MongoDB instance containing product catalog data.
   - Extract product details like `product_id`, `product_name`, and `category`.
   - Save the extracted data to another BigQuery **staging table** for further processing.

---

## Part 3: Data Transformation and Modeling (dbt) (1 Hour)

### Tasks

1. Use dbt to build models that:
   - Join sales data (from the CSV) with product data (from MongoDB) and customer logs (from JSON).
   - Calculate:
     - Daily revenue per product.
     - Top products by category.
     - Customer activity metrics (e.g., most active users, most frequent event types).
   - Write the transformed data to a **reporting table** in BigQuery.

2. Implement dbt schema tests to:
   - Validate that `product_id` and `user_id` are not null and unique where applicable.
   - Ensure that revenue calculations are consistent.

3. Normalize the data:
   - Design the schema for the reporting table to follow best practices in **data modeling and normalization** (e.g., splitting denormalized data into dimension and fact tables).

---

## Part 4: Infrastructure Setup with Terraform (30 minutes)

### Tasks

1. Write Terraform scripts to:
   - Create a BigQuery dataset (`ecommerce_data`).
   - Create tables:
     - `raw_sales_data`
     - `customer_logs`
     - `product_catalog`
     - `reporting_metrics`
   - Include IAM roles to ensure proper permissions for dbt and Python scripts.

2. Parameterize the Terraform scripts for reusability:
   - Allow different dataset names or regions to be passed as variables.

---

## Bonus Task: Advanced Validation and Monitoring (Optional)

### Tasks

1. Build a Python-based monitoring script to:
   - Compare row counts and metrics between raw and transformed data.
   - Detect anomalies in metrics (e.g., unusually high/low revenue).
   - Send alerts (e.g., via email or Slack) if discrepancies are found.

2. Extend Terraform to provision a **Cloud Storage bucket**:
   - Store raw CSV files and logs before ingestion into BigQuery.

---

## Deliverables

1. **Python Scripts**:
   - A script for data ingestion, regex/JSON parsing, and log processing.
   - A script for validation and monitoring.

2. **dbt Project**:
   - Models for staging, transformation, and reporting.
   - Schema tests for data quality.

3. **Terraform Scripts**:
   - Scripts to provision BigQuery datasets and tables, with reusable variables.

4. **Documentation**:
   - A README file explaining how to run the pipeline and the purpose of each component.

---

## What the Interviewer is Assessing

1. **Regex and JSON Parsing**: Ability to extract meaningful data from raw or messy inputs.
2. **Log Processing**: Competence in handling semi-structured data and generating insights.
3. **NoSQL Knowledge**: Understanding of how to integrate and process data from NoSQL databases.
4. **Data Transformation**: Skill in modeling and normalizing data using dbt.
5. **Terraform and Cloud Knowledge**: Proficiency in automating cloud infrastructure setup.
6. **Attention to Detail**: Accuracy in data validation and pipeline implementation.

