import argparse
import pandas as pd
import os

import matplotlib.pyplot as plt

def analyze_csv(file_path, analysis_type, visualization_type, output_file):
    try:
        # Load the CSV file
        data = pd.read_csv(file_path)
        
        # Perform analysis
        if analysis_type == "summary":
            result = data.describe()
            print(result)
        elif analysis_type == "time-series":
            if 'Date' in data.columns:
                data['Date'] = pd.to_datetime(data['Date'])
                data.set_index('Date', inplace=True)
                result = data
                print(result)
            else:
                print("Error: 'Date' column not found for time-series analysis.")
                return
        elif analysis_type == "category":
            result = data.select_dtypes(include=['object']).describe()
            print(result)
        else:
            print("Error: Unsupported analysis type.")
            return

        # Visualization
        if visualization_type == "line" and analysis_type == "time-series":
            data.plot()
            plt.title("Time-Series Line Plot")
            plt.show()
        elif visualization_type == "bar" and analysis_type == "category":
            data.select_dtypes(include=['object']).nunique().plot(kind='bar')
            plt.title("Category Bar Plot")
            plt.show()
        elif visualization_type == "histogram":
            data.hist()
            plt.title("Histogram")
            plt.show()
        else:
            print("Error: Unsupported visualization type or incompatible with analysis type.")
            return

        # Save results to file
        if output_file:
            result.to_csv(output_file)
            print(f"Results saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="CSV Data Analyzer")
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument("analysis_type", choices=["summary", "time-series", "category"], help="Type of analysis to perform")
    parser.add_argument("visualization_type", choices=["line", "bar", "histogram"], help="Type of visualization to generate")
    parser.add_argument("--output", help="File path to save the analysis results", default=None)

    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print("Error: File not found.")
        return

    analyze_csv(args.file_path, args.analysis_type, args.visualization_type, args.output)

if __name__ == "__main__":
    main()