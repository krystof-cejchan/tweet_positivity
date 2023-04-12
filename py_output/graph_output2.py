import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('../csv input data/tweets final.csv')

# Convert the date column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the index of the DataFrame
df.set_index('date', inplace=True)

# Group the DataFrame by mood and calculate the mean score for each mood
grouped = df.groupby('mood')['score'].mean()

# Plot the data as a bar graph
fig, ax = plt.subplots()
ax.bar(grouped.index, grouped.values)
ax.set_xlabel('Mood')
ax.set_ylabel('Positivity Score')
plt.show()
