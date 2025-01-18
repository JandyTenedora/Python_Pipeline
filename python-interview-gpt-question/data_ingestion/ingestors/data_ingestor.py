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

    @abstractmethod
    def ingest_data(self):
        pass

    @abstractmethod
    def log_progress(self):
        print(f"Ingesting data from {self.data_source} to {self.destination}")
