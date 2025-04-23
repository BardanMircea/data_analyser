import pandas as pd

class DataAnalyzer:
    def __init__(self, dataframe):
        """
        Initialize the DataAnalyzer with a pandas DataFrame.
        """
        self.dataframe = dataframe

    def summary_statistics(self, category_column, value_column):
        """
        Calculate summary statistics (mean, median, std dev) by category.
        """
        return self.dataframe.groupby(category_column)[value_column].agg(['mean', 'median', 'std'])

    def time_series_analysis(self, date_column, value_column):
        """
        Analyze spending trends over time.
        """
        self.dataframe[date_column] = pd.to_datetime(self.dataframe[date_column])
        return self.dataframe.groupby(self.dataframe[date_column].dt.to_period('M'))[value_column].sum()

    def spending_distribution(self, value_column, bins=10):
        """
        Analyze spending distribution.
        """
        return pd.cut(self.dataframe[value_column], bins=bins).value_counts()

    def top_spending_categories(self, category_column, value_column, top_n=5):
        """
        Identify top spending categories.
        """
        return self.dataframe.groupby(category_column)[value_column].sum().nlargest(top_n)

    def customer_segmentation(self, customer_column, value_column, bins=4):
        """
        Segment customers by spending patterns.
        """
        total_spending = self.dataframe.groupby(customer_column)[value_column].sum()
        return pd.qcut(total_spending, q=bins, labels=[f'Segment {i+1}' for i in range(bins)])

# Example usage:
# df = pd.read_csv('your_data.csv')
# analyzer = DataAnalyzer(df)
# print(analyzer.summary_statistics('Category', 'Spending'))
# print(analyzer.time_series_analysis('Date', 'Spending'))
# print(analyzer.spending_distribution('Spending'))
# print(analyzer.top_spending_categories('Category', 'Spending'))
# print(analyzer.customer_segmentation('CustomerID', 'Spending'))