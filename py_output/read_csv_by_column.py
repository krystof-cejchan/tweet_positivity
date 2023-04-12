import pandas as pd

# Read the CSV file with tabs as the delimiter
df = pd.read_csv('tweets-modified-py-sc.csv', delimiter=',')

# Print the DataFrame to verify that it has three columns
print(df)
