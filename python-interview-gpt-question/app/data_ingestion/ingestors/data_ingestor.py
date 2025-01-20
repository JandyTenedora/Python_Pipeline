from abc import ABC, abstractmethod
class DataIngestor(ABC):
    def __init__(self, data_source, destination, file_type):
        self.data_source = data_source
        self.destination = destination
        self.file_type = file_type

    @abstractmethod
    def parse_data(self):
        pass

    @abstractmethod
    def validate_data(self):
        pass

    def log_progress(self):
        print(f"Ingesting {self.file_type} data from {self.data_source} to {self.destination}")

    def ingest_data(self) -> None:
        """
        Ingest data into destination
        :return: None
        """
        self.validate_data()
        parsed_data = self.parse_data()

        self.log_progress()
        self.destination.write_data(parsed_data)
