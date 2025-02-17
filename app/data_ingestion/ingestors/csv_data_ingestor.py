import csv

from app.data_ingestion.ingestors.data_ingestor import DataIngestor


class CSVDataIngestor(DataIngestor):
    def __init__(self, data_source, destination):
        super().__init__(data_source,destination, "CSV")


    def validate_data(self) -> None:
        """
        Validate CSV data format:
        - Ensure that required columns are present
        - Validate data types in each row
        """

        print("Validating CSV data...\n")
        with open(self.data_source, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'transaction_id' not in row:
                    raise ValueError("Missing transaction_id column in CSV")
            print("CSV data validated successfully")

    def parse_data(self) -> list:
        """
        Parse data into structured format(list of dicts)
        :return: List of dicts
        """
        print("Parsing CSV data...\n")
        parsed_data = []
        with open(self.data_source, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                parsed_data.append(row)

        print("CSV data finished parsing\n")
        return parsed_data



