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
        table = self.client.get_table(table_ref)

        df = pd.DataFrame(data)
        # Insert the data into BigQuery
        errors = self.client.insert_rows_from_dataframe(table, df)

        if all(not error for error in errors):
            print(f"Successfully inserted {len(data)} rows into {self.table_id}.")
        else:
            print(f"Encountered errors while inserting rows: {errors}")