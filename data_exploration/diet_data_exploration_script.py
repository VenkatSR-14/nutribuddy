"""
A comprehensive script for exploring the diet dataset in the NutriBuddy project.
This script loads the CSV file, displays basic statistics, explores missing values,
visualizes distributions, checks for duplicates, and analyzes categorical features.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Check for missing values
    print('\n--- Missing Values ---')
    print(diet_df.isnull().sum())

    # Check for duplicates
    num_duplicates = diet_df.duplicated().sum()
    print(f'\n--- Number of Duplicate Rows: {num_duplicates} ---')

    # Visualize distribution of numerical features
    num_cols = diet_df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(diet_df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    # Analyze categorical features
    cat_cols = diet_df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f'\n--- Value Counts for {col} ---')
        print(diet_df[col].value_counts())
        # Visualize top 10 categories if too many unique
        if diet_df[col].nunique() < 30:
            plt.figure(figsize=(8, 4))
            sns.countplot(y=diet_df[col], order=diet_df[col].value_counts().index)
            plt.title(f'Countplot of {col}')
            plt.tight_layout()
            plt.show()
        else:
            print(f'(Too many unique values to plot for {col})')

    # Correlation heatmap (if there are enough numeric columns)
    if len(num_cols) > 1:
        plt.figure(figsize=(10, 8))
        corr = diet_df[num_cols].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.show()

    # Advanced: Group by categorical columns and summarize
    for col in cat_cols:
        if diet_df[col].nunique() < 30:
            print(f'\n--- Grouped Summary for {col} ---')
            print(diet_df.groupby(col)[num_cols].mean())

    # Advanced: Outlier detection using IQR for numeric columns
    print('\n--- Outlier Detection (IQR Method) ---')
    for col in num_cols:
        Q1 = diet_df[col].quantile(0.25)
        Q3 = diet_df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = diet_df[(diet_df[col] < Q1 - 1.5 * IQR) | (diet_df[col] > Q3 + 1.5 * IQR)]
        print(f'{col}: {len(outliers)} outliers')

    # Advanced: Pairplot for numeric columns (if not too many)
    if len(num_cols) > 1 and len(num_cols) <= 8:
        sns.pairplot(diet_df[num_cols].dropna())
        plt.suptitle('Pairplot of Numeric Features', y=1.02)
        plt.show()

    # Advanced: Missing value visualization
    try:
        import missingno as msno
        msno.matrix(diet_df)
        plt.title('Missing Values Matrix')
        plt.show()
        msno.heatmap(diet_df)
        plt.title('Missing Values Heatmap')
        plt.show()
    except ImportError:
        print('Install missingno for advanced missing value visualization (pip install missingno)')

    # Save cleaned dataset (optional example)
    cleaned_path = '../data/cleaned/diet_cleaned.csv'
    diet_df.to_csv(cleaned_path, index=False)
    print(f'\n--- Cleaned dataset saved to {cleaned_path} ---')

    print('\n--- Data Exploration Complete ---')

if __name__ == '__main__':
    main()
