import pytest
import pandas as pd
from src.data_loader import DataLoader

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "category": ["A", "B", "A"]
    })

def test_load_csv(tmp_path):
    # Create a temporary CSV file
    file_path = tmp_path / "test.csv"
    sample_csv = "id,name,date,category\n1,Alice,2023-01-01,A\n2,Bob,2023-01-02,B\n3,Charlie,2023-01-03,A"
    file_path.write_text(sample_csv)

    loader = DataLoader()
    data = loader.load_csv(str(file_path))

    assert not data.empty
    assert list(data.columns) == ["id", "name", "date", "category"]

def test_validate_data(sample_data):
    loader = DataLoader(required_columns=["id", "name", "date"])
    validated_data = loader.validate_data(sample_data)

    assert not validated_data.empty
    assert list(validated_data.columns) == ["id", "name", "date", "category"]

    # Test missing required columns
    loader = DataLoader(required_columns=["nonexistent_column"])
    with pytest.raises(ValueError, match="Missing required columns:"):
        loader.validate_data(sample_data)

def test_filter_by_date_range(sample_data):
    loader = DataLoader()
    filtered_data = loader.filter_by_date_range(sample_data, "date", "2023-01-01", "2023-01-02")

    assert len(filtered_data) == 2
    assert filtered_data["date"].tolist() == ["2023-01-01", "2023-01-02"]

    # Test invalid date column
    with pytest.raises(ValueError, match="Date column 'invalid_date' not found in DataFrame."):
        loader.filter_by_date_range(sample_data, "invalid_date", "2023-01-01", "2023-01-02")

def test_filter_by_category(sample_data):
    loader = DataLoader()
    filtered_data = loader.filter_by_category(sample_data, "category", ["A"])

    assert len(filtered_data) == 2
    assert filtered_data["category"].tolist() == ["A", "A"]

    # Test invalid category column
    with pytest.raises(ValueError, match="Category column 'invalid_category' not found in DataFrame."):
        loader.filter_by_category(sample_data, "invalid_category", ["A"])
