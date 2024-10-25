import os
import pandas as pd
import subprocess

# Extract the CAB file using cabextract (available on Linux/Windows)
subprocess.run(['cabextract', 'path_to_file.cab', '-d', 'output_directory'])

# Load extracted CSV into pandas DataFrame
df = pd.read_csv('output_directory/extracted_file.csv')

# Inspect the data
print(df.head())
print(df.info())