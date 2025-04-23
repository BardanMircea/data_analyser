import pytest
import pandas as pd
from src.visualizer import DataVisualizer
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Category": ["A", "B", "C"],
        "Values": [10, 20, 30],
        "Percentages": [0.2, 0.3, 0.5]
    })

@pytest.fixture
def visualizer():
    return DataVisualizer(analysis_results={})

def test_bar_chart(sample_data, visualizer):
    fig = visualizer.bar_chart(sample_data, x="Category", y="Values", title="Test Bar Chart")
    assert isinstance(fig, plt.Figure)

def test_line_chart(sample_data, visualizer):
    fig = visualizer.line_chart(sample_data, x="Category", y="Values", title="Test Line Chart")
    assert isinstance(fig, plt.Figure)

def test_pie_chart(sample_data, visualizer):
    fig = visualizer.pie_chart(sample_data, labels="Category", values="Values", title="Test Pie Chart")
    assert isinstance(fig, plt.Figure)

def test_heatmap(sample_data, visualizer):
    # Add a numerical column to test correlation
    sample_data["Extra"] = [5, 15, 25]
    fig = visualizer.heatmap(sample_data, title="Test Heatmap")
    assert isinstance(fig, plt.Figure)

def test_empty_data(visualizer):
    empty_data = pd.DataFrame()
    with pytest.raises(ValueError):
        visualizer.bar_chart(empty_data, x="Category", y="Values")

def test_invalid_columns(sample_data, visualizer):
    with pytest.raises(KeyError):
        visualizer.bar_chart(sample_data, x="Invalid", y="Values")
