from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import pyreadstat


class TabularReader(ABC):
    @abstractmethod
    def read_file(self, file_path: str) -> pd.DataFrame:
        pass


class ExcelReader(TabularReader):
    def read_file(self, file_path: str) -> dict[Any, pd.DataFrame]:
        excel_data = pd.read_excel(file_path, sheet_name=None)

        result = {
            sheet_name: df for sheet_name, df in excel_data.items() if not df.empty
        }
        return result


class CsvReader(TabularReader):
    def read_file(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)


class SasReader(TabularReader):
    def read_file(self, file_path: str) -> pd.DataFrame:
        df, meta = pyreadstat.read_sas7bdat(file_path)
        return df


class XptReader(TabularReader):
    def read_file(self, file_path: str) -> pd.DataFrame:
        df, meta = pyreadstat.read_xport(file_path)
        return df
