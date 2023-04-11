import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('tweets final done.csv', parse_dates=['date'])

# Split data into positive and negative
positive_data = data[data['mood'] == 'POSITIVE']
negative_data = data[data['mood'] == 'NEGATIVE']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Plot positive data on the left subplot
ax1.fill_between(positive_data['date'], positive_data['score'], color='green', alpha=0.5)
ax1.set_title('Positive Data')
ax1.set_xlabel('Date')
ax1.set_ylabel('Score')

# Plot negative data on the right subplot
ax2.fill_between(negative_data['date'], negative_data['score'], color='red', alpha=0.5)
ax2.set_title('Negative Data')
ax2.set_xlabel('Date')
ax2.set_ylabel('Score')

# Display the plot
plt.show()
