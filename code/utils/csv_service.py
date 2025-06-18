from pathlib import Path
import csv
from abc import abstractmethod

class CSVService:
    @abstractmethod
    def write_csv(self, directory, filename, data, header=None):
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        file_path = path / filename

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(header)
            writer.writerows(data)

    @abstractmethod
    def read_csv(self, directory, filename, skip_header=True):
        file_path = Path(directory) / filename
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            if skip_header:
                next(reader, None) 
            return [row for row in reader]