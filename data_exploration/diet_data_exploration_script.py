"""
A simple script for exploring the diet dataset in the NutriBuddy project.
This script loads the CSV file, displays basic statistics, and shows a sample of the data.
"""

import pandas as pd

# Path to the diet dataset (update if necessary)
diet_csv_path = '../data/diet.csv'

def main():
    # Load the diet data
    diet_df = pd.read_csv(diet_csv_path)
    print('--- Diet Dataset Info ---')
    print(diet_df.info())
    print('\n--- First 5 Rows ---')
    print(diet_df.head())
    print('\n--- Basic Statistics ---')
    print(diet_df.describe(include='all'))

if __name__ == '__main__':
    main()
