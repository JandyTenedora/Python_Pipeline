from google.cloud import bigquery
from typing import List
import pandas as pd

from app.data_ingestion.destinations.destination import Destination


class BigQueryDestination(Destination):
    def __init__(self, dataset_id: str, table_id: str) -> None:
        """
        Initialize the BigQueryDestination with the necessary identifiers.

        Args:
            dataset_id (str): The BigQuery dataset ID.
            table_id (str): The BigQuery table ID.
        """
        self.client = bigquery.Client()
        self.dataset_id = dataset_id
        self.table_id = table_id

    def write_data(self, data: List[dict]) -> None:
        """
        Write data to the specified BigQuery table.

        Args:
            data (list): The data to be written, typically a list of dictionaries.
        """
        table_ref = self.client.dataset(self.dataset_id).table(self.table_id)

        df = pd.DataFrame(data)

        # Ensure the data types match the BigQuery schema
        schema = self.client.get_table(table_ref).schema
        for field in schema:
            if field.field_type == "INTEGER":
                df[field.name] = df[field.name].astype("int64")
            elif field.field_type == "FLOAT":
                df[field.name] = df[field.name].astype("float64")
            elif field.field_type == "BOOLEAN":
                df[field.name] = df[field.name].astype("bool")
            elif field.field_type == "STRING":
                df[field.name] = df[field.name].astype("str")
            elif field.field_type == "TIMESTAMP":
                df[field.name] = pd.to_datetime(df[field.name])
            elif field.field_type == "DATE":
                df[field.name] = pd.to_datetime(df[field.name]).dt.date

        # Load the data into BigQuery
        job = self.client.load_table_from_dataframe(df, table_ref)

        # Wait for the job to complete
        job.result()

        print(f"Successfully loaded {job.output_rows} rows into {self.table_id}.")