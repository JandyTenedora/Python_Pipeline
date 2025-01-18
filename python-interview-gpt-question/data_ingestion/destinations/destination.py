from abc import ABC, abstractmethod


class Destination(ABC):
    @abstractmethod
    def write_data(self, data: list) -> None:
        """
        Write data to the destination.

        Args:
            data (list): The data to be written, typically a list of dictionaries.
        """
        pass
