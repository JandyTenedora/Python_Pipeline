import sys

from app.data_ingestion.destinations.bigquery_destination import BigQueryDestination
from app.data_ingestion.destinations.firestore_destination import FirestoreDestination
from app.data_ingestion.ingestors.csv_data_ingestor import CSVDataIngestor
from app.data_ingestion.ingestors.json_data_ingestor import JSONIngestor
from app.utils.find_project_root import find_project_root

project_root = str(find_project_root())
sys.path.append(project_root)

class DataIngestor:
   def __init__(self, project_root, bq_dataset_id, firestore_dataset_name):
      self.project_root = project_root
      self.bq_dataset_id = bq_dataset_id
      self.firestore_dataset_name = firestore_dataset_name

   def ingest_data(self):
      # Create all bq and fs destinations
      bq_sales_data = BigQueryDestination(self.bq_dataset_id, "raw_sales_data")
      fs_event_logs = FirestoreDestination(self.firestore_dataset_name, "event_log_raw")
      bq_customer_activity = BigQueryDestination(self.bq_dataset_id, "customer_logs")

      # Create necessary ingestors
      sales_csv_ingestor = CSVDataIngestor(f"{self.project_root}/target/raw/large_sales_data.csv", bq_sales_data)
      event_json_ingestor = JSONIngestor(f"{self.project_root}/target/raw/large_event_logs.json", fs_event_logs)
      customer_activity_json_ingestor = JSONIngestor(f"{self.project_root}/target/normalized/normalized_customer_logs.json", bq_customer_activity)

      # Run ingestion
      sales_csv_ingestor.ingest_data()
      event_json_ingestor.ingest_data()
      customer_activity_json_ingestor.ingest_data()


def main():
   dataset_id = "ecommerce_data_raw"
   firestore_dataset_name = "ecommerce-firestore"
   data_ingestor = DataIngestor(project_root, dataset_id, firestore_dataset_name)
   data_ingestor.ingest_data()


if __name__ == "__main__":
    main()