import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('tweets final done.csv')

# Calculate the percentage of positive and negative data
total_count = len(data)
positive_count = len(data[data['mood'] == 'POSITIVE'])
negative_count = len(data[data['mood'] == 'NEGATIVE'])
positive_percent = positive_count / total_count * 100
negative_percent = negative_count / total_count * 100

# Create a pie chart
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie([positive_percent, negative_percent],
       labels=['Positive: ' + str(positive_count), 'Negative: ' + str(negative_count)], autopct='%1.1f%%',
       startangle=90)
ax.set_title('Percentage of Positive and Negative Data')

# Display the plot
plt.show()
