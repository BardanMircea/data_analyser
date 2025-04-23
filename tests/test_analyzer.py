import pytest
import pandas as pd
from src.analyzer import DataAnalyzer

@pytest.fixture
def sample_dataframe():
    data = {
        'Category': ['Food', 'Transport', 'Food', 'Entertainment', 'Transport'],
        'Spending': [100, 50, 150, 200, 75],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'CustomerID': [1, 2, 1, 3, 2]
    }
    return pd.DataFrame(data)

def test_summary_statistics(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    result = analyzer.summary_statistics('Category', 'Spending')
    assert 'mean' in result.columns
    assert 'median' in result.columns
    assert 'std' in result.columns

def test_time_series_analysis(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    result = analyzer.time_series_analysis('Date', 'Spending')
    assert len(result) == 1  # All dates fall in the same month (January 2023)
    assert result.iloc[0] == 575  # Total spending

def test_spending_distribution(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    result = analyzer.spending_distribution('Spending', bins=3)
    assert result.sum() == len(sample_dataframe)  # All rows should be accounted for

def test_top_spending_categories(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    result = analyzer.top_spending_categories('Category', 'Spending', top_n=2)
    assert len(result) == 2
    assert result.index[0] == 'Food'  # Food has the highest spending

def test_customer_segmentation(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    result = analyzer.customer_segmentation('CustomerID', 'Spending', bins=2)
    assert len(result) == 2  # Two unique customers
    assert set(result) == {'Segment 1', 'Segment 2'}  # Two segments

def test_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Category', 'Spending', 'Date', 'CustomerID'])
    analyzer = DataAnalyzer(empty_df)
    with pytest.raises(ValueError):
        analyzer.summary_statistics('Category', 'Spending')

def test_invalid_column(sample_dataframe):
    analyzer = DataAnalyzer(sample_dataframe)
    with pytest.raises(KeyError):
        analyzer.summary_statistics('InvalidColumn', 'Spending')
