import sys

from app.data_ingestion.destinations.bigquery_destination import BigQueryDestination
from app.data_ingestion.ingestors.csv_data_ingestor import CSVDataIngestor
from app.data_ingestion.ingestors.json_data_ingestor import JSONIngestor
from app.data_ingestion.normalisers.customer_acitivity_log_normaliser import normalise_customer_activity_write
from app.utils.find_project_root import find_project_root

project_root = str(find_project_root())
sys.path.append(project_root)

def main():
   ## Possible new pattern to ingest without the need of io write
   # normalised_customer_activity, product_lookup = normalise_customer_activity()

   dataset_id = "ecommerce_data_raw"
   bq_sales_data = BigQueryDestination(dataset_id, "raw_sales_data")
   bq_event_logs = BigQueryDestination(dataset_id, "event_log")
   bq_customer_activity = BigQueryDestination(dataset_id, "customer_logs")
   bq_products = BigQueryDestination(dataset_id, "product_catalog")

   normalise_customer_activity_write()
   sales_csv_ingestor = CSVDataIngestor(f"{project_root}/target/raw/large_sales_data.csv", bq_sales_data)
   event_json_ingestor = JSONIngestor(f"{project_root}/target/raw/large_event_logs.json", bq_event_logs)
   customer_activity_json_ingestor = JSONIngestor(f"{project_root}/target/normalized/normalized_customer_logs.json", bq_customer_activity)
   products_json_ingestor = JSONIngestor(f"{project_root}/target/normalized/product_lookup.json", bq_products)

   sales_csv_ingestor.ingest_data()
   event_json_ingestor.ingest_data()
   customer_activity_json_ingestor.ingest_data()
   products_json_ingestor.ingest_data()

if __name__ == "__main__":
    main()