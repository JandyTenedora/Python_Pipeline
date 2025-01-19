from google.cloud import firestore
from typing import List
from app.data_ingestion.destinations.destination import Destination

class FirestoreDestination(Destination):
    def __init__(self, database_name: str, collection_name: str) -> None:
        """
        Initialize the FirestoreDestination with the necessary identifiers.

        Args:
            collection_name (str): The Firestore collection name.
            database_name (str): The Firestore database name. Defaults to "(default)".
        """
        self.client = firestore.Client(database=database_name)
        self.collection_name = collection_name

    def write_data(self, data: List[dict]) -> None:
        """
        Write data to the specified Firestore collection.

        Args:
            data (list): The data to be written, typically a list of dictionaries.
        """
        collection_ref = self.client.collection(self.collection_name)
        batch = self.client.batch()

        for i, record in enumerate(data):
            doc_ref = collection_ref.document()
            batch.set(doc_ref, record)

            # Commit the batch every 500 writes
            if (i + 1) % 500 == 0:
                batch.commit()
                batch = self.client.batch()

        # Commit any remaining writes
        if len(data) % 500 != 0:
            batch.commit()

        print(f"Successfully written {len(data)} records to the {self.collection_name} collection.")