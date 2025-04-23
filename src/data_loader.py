import pandas as pd
from typing import List, Optional

class DataLoader:
    def __init__(self, required_columns: Optional[List[str]] = None):
        """
        Initialize the DataLoader with optional required columns.
        """
        self.required_columns = required_columns

    def load_csv(self, file_path: str) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")

    def validate_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Validate the DataFrame by checking for required columns and handling missing values.
        """
        if self.required_columns:
            missing_columns = [col for col in self.required_columns if col not in data.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")

        # Handle missing values (e.g., drop rows with missing values)
        data = data.dropna()
        return data

    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Perform basic data cleaning such as date parsing and type conversion.
        """
        for column in data.columns:
            # Attempt to parse dates
            if "date" in column.lower():
                try:
                    data[column] = pd.to_datetime(data[column], errors='coerce')
                except Exception:
                    pass

            # Convert numeric columns
            if data[column].dtype == 'object':
                try:
                    data[column] = pd.to_numeric(data[column], errors='ignore')
                except Exception:
                    pass

        return data

    def filter_by_date_range(self, data: pd.DataFrame, date_column: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Filter the DataFrame by a date range.
        """
        if date_column not in data.columns:
            raise ValueError(f"Date column '{date_column}' not found in DataFrame.")

        data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
        filtered_data = data[(data[date_column] >= start_date) & (data[date_column] <= end_date)]
        return filtered_data

    def filter_by_category(self, data: pd.DataFrame, category_column: str, categories: List[str]) -> pd.DataFrame:
        """
        Filter the DataFrame by specific categories.
        """
        if category_column not in data.columns:
            raise ValueError(f"Category column '{category_column}' not found in DataFrame.")

        filtered_data = data[data[category_column].isin(categories)]
        return filtered_data