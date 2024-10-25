import pandas as pd

# Load the CSV file
df = pd.read_csv('path_to_your_file.csv')

# Extract the headings (column names)
headings = df.columns.tolist()

# Print the headings
print("Headings:", headings)