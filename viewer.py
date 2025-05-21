import pandas as pd
from pathlib import Path
from reader import ExcelReader, CsvReader, SasReader, XptReader


class TabularViewer:
    def __init__(self):
        self.readers = {
            ".xlsx": ExcelReader(),
            ".csv": CsvReader(),
            ".sas7bdat": SasReader(),
            ".xpt": XptReader(),
        }

    def view_file(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File {file_path} not found.")

        reader = self.readers.get(path.suffix.lower())
        if not reader:
            raise ValueError(f"Unsupported file format: {path.suffix}")

        try:
            data = reader.read_file(str(path))
            return data
        except Exception as e:
            raise Exception(f"Error reading file: {e}")
