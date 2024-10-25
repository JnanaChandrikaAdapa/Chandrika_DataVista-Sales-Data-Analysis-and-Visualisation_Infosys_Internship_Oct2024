import pandas as pd
import numpy as np
from scipy import stats

# Load data from a CSV file
df = pd.read_csv('path_to_your_file.csv')

# Inspect the data
print("Original DataFrame:")
print(df.head())
print("\nDataFrame Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Handling Missing Values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Drop rows with any missing values (optional)
# df_cleaned = df.dropna()

# Fill missing values with a specific value (e.g., 0)
df.fillna(value=0, inplace=True)

# Fill missing values with the mean of the column for a specific column
# df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Removing Duplicates
print("\nNumber of Duplicate Rows:", df.duplicated().sum())
df_cleaned = df.drop_duplicates()

# Changing Data Types
# Convert a column to a specific data type (e.g., integer)
# df_cleaned['column_name'] = df_cleaned['column_name'].astype(int)

# Convert a string column to datetime
# df_cleaned['date_column'] = pd.to_datetime(df_cleaned['date_column'])

# Renaming Columns
df_cleaned.rename(columns={'OldName': 'NewName'}, inplace=True)

# Filtering Rows
# Filter rows where 'column_name' > threshold_value
# df_filtered = df_cleaned[df_cleaned['column_name'] > threshold_value]

# Standardizing Text Data
# Convert a text column to lowercase
df_cleaned['text_column'] = df_cleaned['text_column'].str.lower()
# Remove leading and trailing whitespace
df_cleaned['text_column'] = df_cleaned['text_column'].str.strip()
# Replace specific strings
# df_cleaned['text_column'] = df_cleaned['text_column'].str.replace('old_value', 'new_value')

# Binning Continuous Data
# Bin a continuous variable into categories
# bins = [0, 50, 100]
# labels = ['Low', 'High']
# df_cleaned['binned_column'] = pd.cut(df_cleaned['continuous_column'], bins=bins, labels=labels)

# Outlier Detection and Removal
df_cleaned = df_cleaned[(np.abs(stats.zscore(df_cleaned['numeric_column'])) < 3)]

# Final Check
print("\nCleaned DataFrame Info:")
print(df_cleaned.info())
print("\nCleaned DataFrame:")
print(df_cleaned.head())

# Export the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_data.csv', index=False)