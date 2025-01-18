import json

from data_ingestion.ingestors.data_ingestor import DataIngestor

class JSONIngestor(DataIngestor):
    def __init__(self, data_source, destination):
        super().__init__(data_source, destination, "JSON")

    def parse_data(self) -> dict:
        print("Parsing JSON Data\n")
        with open(self.data_source, "r") as file:
            data = json.load(file)
        print("Finished parsing data\n")
        return data

    def validate_data(self) -> None:
        print("Unimplemented\n")




