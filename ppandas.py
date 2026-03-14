import pandas as pd

# Load CSV file
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Basic analysis
print("\nShape of dataset:", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nStatistical summary:")
print(df.describe())
