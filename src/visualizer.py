import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, analysis_results):
        """
        Initialize the DataVisualizer with analysis results.
        :param analysis_results: A dictionary or DataFrame containing the analysis results.
        """
        self.analysis_results = analysis_results

    def bar_chart(self, data, x, y, title="Bar Chart", color="blue", save_path=None):
        """
        Generate a bar chart.
        :param data: DataFrame containing the data.
        :param x: Column name for the x-axis.
        :param y: Column name for the y-axis.
        :param title: Title of the chart.
        :param color: Color of the bars.
        :param save_path: Path to save the chart as a file.
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        ax.bar(data[x], data[y], color=color)
        ax.set_title(title)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        if save_path:
            plt.savefig(save_path)
        return fig

    def line_chart(self, data, x, y, title="Line Chart", color="blue", save_path=None):
        """
        Generate a line chart.
        :param data: DataFrame containing the data.
        :param x: Column name for the x-axis.
        :param y: Column name for the y-axis.
        :param title: Title of the chart.
        :param color: Line color.
        :param save_path: Path to save the chart as a file.
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        ax.plot(data[x], data[y], color=color)
        ax.set_title(title)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        if save_path:
            plt.savefig(save_path)
        return fig

    def pie_chart(self, data, labels, values, title="Pie Chart", colors=None, save_path=None):
        """
        Generate a pie chart.
        :param data: DataFrame containing the data.
        :param labels: Column name for the labels.
        :param values: Column name for the values.
        :param title: Title of the chart.
        :param colors: List of colors for the pie slices.
        :param save_path: Path to save the chart as a file.
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        ax.pie(data[values], labels=data[labels], colors=colors, autopct='%1.1f%%')
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig

    def heatmap(self, data, title="Heatmap", cmap="coolwarm", save_path=None):
        """
        Generate a heatmap for correlation between variables.
        :param data: DataFrame containing the data.
        :param title: Title of the heatmap.
        :param cmap: Colormap for the heatmap.
        :param save_path: Path to save the heatmap as a file.
        :return: The seaborn heatmap figure.
        """
        fig, ax = plt.subplots()
        correlation_matrix = data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap=cmap, ax=ax)
        ax.set_title(title)
        if save_path:
            plt.savefig(save_path)
        return fig